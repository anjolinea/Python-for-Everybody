# Question 1
def get_list_of_university_towns():
    df = pd.DataFrame(columns=["State", "RegionName"])
    fhand = open("university_towns.txt")
    num = 0
    for line in fhand:
        line = line.rstrip()
        if "[edit]" in line:
            line = line[:-6]
            state = line
            continue
        else:
            bracket_position = line.find("(")
            regionname = line[:bracket_position-1]
            df.loc[num] = state, regionname
            num += 1
    return df

get_list_of_university_towns()

# Question 2
def get_recession_start():
    df = pd.read_excel("gdplev.xls",skiprows=7)
    df = df.rename(columns={"Unnamed: 6":"GDP", "Unnamed: 4": "Quarter"})
    df = df[["Quarter", "GDP"]]
    place_2000q1 = df[df["Quarter"] == "2000q1"].index.tolist()[0]
    df = df[place_2000q1:]
    for i in range(len(df)):
        if df["GDP"].iloc[i] > df["GDP"].iloc[i+1] > df["GDP"].iloc[i+2]:
            answer = (df["Quarter"].iloc[i+1])
            break
    return answer

get_recession_start()

# Question 3
def get_recession_end():
    df = pd.read_excel("gdplev.xls",skiprows=7)
    df = df.rename(columns={"Unnamed: 6":"GDP", "Unnamed: 4": "Quarter"})
    df = df[["Quarter", "GDP"]]
    # new code
    place_beg = df[df["Quarter"] == "2008q3"].index.tolist()[0]
    df_new = df[place_beg - place_2000q1: ]
    for i in range(len(df_new)):
        if df_new["GDP"].iloc[i] < df_new["GDP"].iloc[i+1] < df_new["GDP"].iloc[i+2]:
            answer = df_new["Quarter"].iloc[i+2]
            break
    return answer

get_recession_end()

