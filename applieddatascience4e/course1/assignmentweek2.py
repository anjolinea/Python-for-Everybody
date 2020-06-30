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

#Question 3
def answer_three():
    a = df[(df["Gold"]>0) & (df["Gold.1"]>0)]
    max_compare_value = max((a["Gold"]-a["Gold.1"])/a["Gold.2"])
    the_answer = a[(a["Gold"]-a["Gold.1"])/a["Gold.2"] == max_compare_value]
    return the_answer.index.tolist()[0]

answer_three()

# Question 4

