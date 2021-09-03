import itertools
from collections import Counter

from pandas.io.formats.format import Datetime64Formatter
from parse import load_dataframes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import folium
import webbrowser


def set_config():
    # 폰트, 그래프 색상 설정
    font_list = fm.findSystemFonts(fontpaths=None, fontext="ttf")
    if any(["notosanscjk" in font.lower() for font in font_list]):
        plt.rcParams["font.family"] = "Noto Sans CJK JP"
    else:
        if not any(["malgun" in font.lower() for font in font_list]):
            raise Exception(
                "Font missing, please install Noto Sans CJK or Malgun Gothic. If you're using ubuntu, try `sudo apt install fonts-noto-cjk`"
            )

        plt.rcParams["font.family"] = "Malgun Gothic"

    sns.set_palette(sns.color_palette("Spectral"))
    plt.rc("xtick", labelsize=6)


def show_store_categories_graph(dataframes, n=50):
    """
    Tutorial: 전체 음식점의 상위 `n`개 카테고리 분포를 그래프로 나타냅니다.
    """

    stores = dataframes["stores"]

    # 모든 카테고리를 1차원 리스트에 저장합니다
    categories = stores.category.apply(lambda c: c.split("|"))
    categories = itertools.chain.from_iterable(categories)

    # 카테고리가 없는 경우 / 상위 카테고리를 추출합니다
    categories = filter(lambda c: c != "", categories)
    categories_count = Counter(list(categories))
    best_categories = categories_count.most_common(n=n)
    df = pd.DataFrame(best_categories, columns=["category", "count"]).sort_values(
        by=["count"], ascending=False
    )
    # print(df)
    # 그래프로 나타냅니다
    chart = sns.barplot(x="category", y="count", data=df)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("음식점 카테고리 분포")
    plt.show()


def show_store_review_distribution_graph(dataframes, n=50):
    """
    Req. 1-3-1 전체 음식점의 리뷰 개수 분포를 그래프로 나타냅니다. 
    """
    reviews_cnt = dataframes["reviews"]["store"].value_counts()
    reviews_cnt = pd.DataFrame(data={'store' : reviews_cnt.index, 'reviews_cnt' : reviews_cnt})
    df = pd.merge(dataframes["stores"], reviews_cnt, left_on="id", right_on="store")
    df = pd.DataFrame(data={"store_name": df["store_name"], "reviews_cnt" : df["reviews_cnt"]}, columns=["store_name", "reviews_cnt"])
    df = df.sort_values("reviews_cnt", ascending=False)[:n]
    print(df)
    chart = sns.barplot(x="store_name", y="reviews_cnt", data=df)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("음식점 리뷰 분포")
    plt.show()

def show_store_average_ratings_graph(dataframes, n=50, reviews_num=30):
    """
    Req. 1-3-2 각 음식점의 평균 평점을 그래프로 나타냅니다. 리뷰 수는 30개 이상
    """
    c= dataframes["reviews"]["store"].value_counts()[dataframes["reviews"]["store"].value_counts() >= reviews_num]
    df = pd.DataFrame(data=c.index, columns=['store'])
    stores_reviews = pd.merge(df, dataframes["reviews"], on="store")
    scores = stores_reviews.groupby(["store"]).mean().sort_values(['score'], ascending=False)
    df = pd.merge(scores, dataframes["stores"], left_on="store", right_on="id")

    chart = sns.barplot(x="store_name", y="score", data=df)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("음식점 평균 평점 분포")
    plt.show()

def show_user_review_distribution_graph(dataframes, n=50):
    """
    Req. 1-3-3 유저의 리뷰 개수 분포를 그래프로 나타냅니다.
    """
    df = dataframes["reviews"]["user"].value_counts()[:n]
    df = pd.DataFrame(data={'user':df.index, 'reviews' : df})
    df = pd.merge(df, dataframes["users"], left_on="user", right_on="id")

    chart = sns.barplot(x="user", y="reviews", data=df)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("유저 리뷰 개수 분포")
    plt.show()

def show_user_age_gender_distribution_graph(dataframes):
    """
    Req. 1-3-4 전체 유저의 성별/나이대 분포를 그래프로 나타냅니다.
    """

    df = dataframes["users"]
    age = df["age"].value_counts()
    print(age)
    age = pd.DataFrame(data={"age" : age.index, "cnt" : age})
    print(age)
    chart = sns.barplot(x="age", y="cnt", data=age)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("유저 나이 분포")
    plt.show()

def show_stores_distribution_graph(dataframes):
    """
    Req. 1-3-5 각 음식점의 위치 분포를 지도에 나타냅니다.
    """
    df = dataframes["stores"][dataframes["stores"]["area"] == "광주"]
    df = df[df["category"] =="술집"]
    df = df.reset_index(drop=True)

    m = folium.Map(location=[35.1595454, 126.8526012], zoom_start=13)
    for store in df.iterrows():
        center = []
        center.append(float(store[1].latitude))
        center.append(float(store[1].longitude))
        marker = folium.Marker(center, popup=store[1].store_name, icon=folium.Icon(color='red'))
        marker.add_to(m)

    m.save('folium_kr.html')
    webbrowser.open_new("folium_kr.html")

def main():
    set_config()
    data = load_dataframes()
    show_store_categories_graph(data)
    show_store_review_distribution_graph(data)
    show_store_average_ratings_graph(data)
    show_user_review_distribution_graph(data)
    show_user_age_gender_distribution_graph(data)
    show_stores_distribution_graph(data)

if __name__ == "__main__":
    main()
