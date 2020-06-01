import random

Mothers_Children = ["jacob", "joline"]
Fathers_Children = Mothers_Children
moms_favourite_child = random.choice(Mothers_Children)
dads_favourite_child = random.choice(Fathers_Children)

while True:
    if moms_favourite_child and dads_favourite_child == "joline":
        print("Mom's favourite child is", moms_favourite_child)
        print("Dad's favourite child is", dads_favourite_child)
        break
    else:
        moms_favourite_child = random.choice(Mothers_Children)
        dads_favourite_child = random.choice(Fathers_Children)
print("All done!")
