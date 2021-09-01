from parse import load_dataframes
import pandas as pd
import shutil


def sort_stores_by_score(dataframes, n=20, min_reviews=30):
    """
    Req. 1-2-1 각 음식점의 평균 평점을 계산하여 높은 평점의 음식점 순으로 `n`개의 음식점을 정렬하여 리턴합니다
    Req. 1-2-2 리뷰 개수가 `min_reviews` 미만인 음식점은 제외합니다.
    """
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )
    scores_group = stores_reviews.groupby(["store", "store_name"])
    reviews_group = scores_group.filter(lambda g:g["content"].count() >= min_reviews)
    reviews_group = reviews_group.groupby(["store", "store_name"])
    scores = reviews_group.mean()
    scores = scores.sort_values(["score"], ascending=False)

    return scores.head(n=n).reset_index()


def get_most_reviewed_stores(dataframes, n=20):
    """
    Req. 1-2-3 가장 많은 리뷰를 받은 `n`개의 음식점을 정렬하여 리턴합니다
    """
    # df = dataframes["reviews"]["store"].value_counts()[:n]
    # df = pd.DataFrame(data={'store' : df.index, 'reviews' : df})
    # df = pd.merge(df, dataframes["stores"], left_on="store", right_on="id")
    # print(df)
    # return df

    stores_reviews = pd.merge(
    dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )
    reviews_group = stores_reviews.groupby(["store", "store_name"])
    reviews = reviews_group.mean()
    reviews['review_cnt'] = reviews_group.size()
    reviews.sort_values(by="review_cnt", ascending=False, inplace=True)
    print(reviews)
    return reviews.head(n=n).reset_index()

def get_most_active_users(dataframes, n=20):
    """
    Req. 1-2-4 가장 많은 리뷰를 작성한 `n`명의 유저를 정렬하여 리턴합니다.
    """
    df = dataframes["reviews"]["user"].value_counts()[:n]
    df = pd.DataFrame(data={'user':df.index, 'reviews' : df})
    df = pd.merge(df, dataframes["users"], left_on="user", right_on="id")
    return df


def main():
    data = load_dataframes()

    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    # stores_most_scored = sort_stores_by_score(data)
    # print("[최고 평점 음식점]")
    # print(f"{separater}\n")
    # for i, store in stores_most_scored.iterrows():
    #     print(
    #         "{rank}위: {store}({score}점)".format(
    #             rank=i + 1, store=store.store_name, score=store.score
    #         )
    #     )
    # print(f"\n{separater}\n\n")

    store_most_reviewed = get_most_reviewed_stores(data)
    print("[최고 리뷰 음식점]")
    print(f"{separater}\n")
    for i, store in store_most_reviewed.iterrows():
        print(
            "{rank}위: {store}({reviews}개)".format(
                rank=i + 1, store=store.store_name, reviews=store.review_cnt
            )
        )
    print(f"\n{separater}\n\n")

    # most_active_users =get_most_active_users(data)
    # print("[가장 많이 리뷰를 작성한 회원]")
    # print(f"{separater}\n")
    # for i, user in most_active_users.iterrows():
    #     print(
    #         "{rank}위: {user}({reviews}개)".format(
    #             rank=i + 1, user=user.user, reviews=user.reviews
    #         )
    #     )
    # print(f"\n{separater}\n\n")


if __name__ == "__main__":
    main()
