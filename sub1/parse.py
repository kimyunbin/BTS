from datetime import datetime
import json
import pandas as pd
import os
import shutil
import numpy as np

DATA_DIR = "../data"
DATA_FILE = os.path.join(DATA_DIR, "data.json")
DUMP_FILE = os.path.join(DATA_DIR, "dump.pkl")

store_columns = (
    "id",  # 음식점 고유번호
    "store_name",  # 음식점 이름
    "branch",  # 음식점 지점 여부
    "area",  # 음식점 위치
    "tel",  # 음식점 번호
    "address",  # 음식점 주소
    "latitude",  # 음식점 위도
    "longitude",  # 음식점 경도
    "category",  # 음식점 카테고리
)

review_columns = (
    "id",  # 리뷰 고유번호
    "store",  # 음식점 고유번호
    "user",  # 유저 고유번호
    "score",  # 평점
    "content",  # 리뷰 내용
    "reg_time",  # 리뷰 등록 시간
)

menu_columns = (
    "id", # 메뉴 고유번호
    "store", # 음식점 고유번호
    "menu_name", # 메뉴 이름
    "price", # 메뉴 가격
)

user_columns = (
    "id", # 유저 고유번호
    "gender", # 유저 성별
    "age", # 유저 연령
)

def import_data(data_path=DATA_FILE):
    """
    Req. 1-1-1 음식점 데이터 파일을 읽어서 Pandas DataFrame 형태로 저장합니다
    """
    try:
        with open(data_path, encoding="utf-8") as f:
            data = json.loads(f.read())
    except FileNotFoundError as e:
        print(f"`{data_path}` 가 존재하지 않습니다.")
        exit(1)

    stores = []  # 음식점 테이블
    reviews = []  # 리뷰 테이블
    menus = [] # 메뉴 테이블
    users = [] # 유저 테이블
    user_check = []

    for d in data:

        categories = [c["category"] for c in d["category_list"]]
        stores.append(
            [
                d["id"],
                d["name"],
                d["branch"],
                d["area"],
                d["tel"],
                d["address"],
                d["latitude"],
                d["longitude"],
                "|".join(categories),
            ]
        )

        for review in d["review_list"]:
            r = review["review_info"]
            u = review["writer_info"]

            reviews.append(
                [r["id"], d["id"], u["id"], r["score"], r["content"], r["reg_time"]]
            )

        for menu in d["menu_list"]:

            menus.append(
                [d["id"], d["id"], menu["menu"], menu["price"]]
            )

        for review in d["review_list"]:
            u = review["writer_info"]

            if u["id"] not in user_check:
                users.append(
                    [u["id"], u["gender"], datetime.today().year - int(u["born_year"]) + 1]
                )
                user_check.append(u["id"])

    store_frame = pd.DataFrame(data=stores, columns=store_columns)
    review_frame = pd.DataFrame(data=reviews, columns=review_columns)
    menu_frame = pd.DataFrame(data=menus, columns=menu_columns)
    user_frame = pd.DataFrame(data=users, columns=user_columns)

    return {"stores": store_frame, "reviews": review_frame, "menus": menu_frame, "users": user_frame}

def user_store_ratings(dataframes):
    """
    Req. 4-1 유저 음식점 행렬 만들기
    """
    reviews=dataframes["reviews"][["user", "store", "score"]]
    df = pd.merge(reviews, dataframes["stores"], left_on="store", right_on="id")
    df = df[["user", "store_name", "score"]]
    df = df.pivot_table("score", index="user",columns="store_name")
    print(df)
    # return df

def user_category_mean_ratings(dataframes):
    """
    Req. 4-2 유저 카테고리 행렬 만들기
    """
    reviews=dataframes["reviews"][["user", "store", "score"]]
    df = pd.merge(reviews, dataframes["stores"], left_on="store", right_on="id")
    df = df[["user", "score", "category"]]
    df = df.groupby(['user', 'category']).mean()
    df = df.pivot_table("score", index="user",columns="category" )
    print(df)

def dump_dataframes(dataframes):
    pd.to_pickle(dataframes, DUMP_FILE)


def load_dataframes():
    return pd.read_pickle(DUMP_FILE)


def main():

    data = load_dataframes()
    # user_store_ratings(data)
    user_category_mean_ratings(data)

    # print("[*] Parsing data...")
    # data = import_data()
    # print("[+] Done")

    # print("[*] Dumping data...")
    # dump_dataframes(data)
    # print("[+] Done\n")

    # data = load_dataframes()

    # term_w = shutil.get_terminal_size()[0] - 1
    # separater = "-" * term_w

    # print("[음식점]")
    # print(f"{separater}\n")
    # print(data["stores"].head())
    # print(f"\n{separater}\n\n")

    # print("[리뷰]")
    # print(f"{separater}\n")
    # print(data["reviews"].head())
    # print(f"\n{separater}\n\n")
    
    # print("[메뉴]")
    # print(f"{separater}\n")
    # print(data["menus"].head())
    # print(f"\n{separater}\n\n")
    
    # print("[유저]")
    # print(f"{separater}\n")
    # print(data["users"].head())
    # print(f"\n{separater}\n\n")


if __name__ == "__main__":
    main()
