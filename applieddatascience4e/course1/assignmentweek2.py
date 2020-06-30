# Question 1
def answer_one():
    best_country = df[df["Gold"] == max(df["Gold"])]
    return best_country.index.tolist()[0]

answer_one()

# Question 2
def answer_two():
    the_answer = df[(df["Gold"]-df["Gold.1"]) == max(df["Gold"]-df["Gold.1"])]
    return the_answer.index.tolist()[0]

answer_two()
