# Question 1
def answer_one():
    best_country = df[df["Gold"] == max(df["Gold"])]
    return best_country.index.tolist()[0]

answer_one()
