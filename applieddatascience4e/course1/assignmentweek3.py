# Question 1
def answer_one():
    # first section
    energy = pd.read_excel("Energy Indicators.xls", skiprows=17, skipfooter=(38), index_col=0, usecols=[2,3,4,5])
    energy.index.name = "Country"
    energy = (energy.rename(columns={"Petajoules": 'Energy Supply',
                                     "Gigajoules": 'Energy Supply per Capita',
                                     "%": '% Renewable'})
              .replace("...", np.nan)
              .reset_index())

    # " \(.*\)|[0-9]+" is "( any characters )" OR any numbers
    energy["Country"].replace(r" \(.*\)|[0-9]+","", regex=True, inplace=True)
    energy["Country"] = energy["Country"].replace({"Republic of Korea": "South Korea",
                                                   "United States of America": "United States",
                                                   "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                                                   "China, Hong Kong Special Administrative Region": "Hong Kong"})
    energy["Energy Supply"] *= 1000000

    # second section
    GDP = pd.read_csv("world_bank.csv", skiprows=4)
    GDP["Country Name"] = GDP["Country Name"].replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"})
    GDP = GDP[['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    GDP = GDP.rename(columns={"Country Name": "Country"})

    # third section
    ScimEn = pd.read_excel("scimagojr-3.xlsx")

    # fourth section - merge the databases
    temp_1 = pd.merge(ScimEn[:15], energy, how="inner", left_on="Country", right_on="Country")
    df = pd.merge(temp_1, GDP, how="inner", left_on="Country", right_on="Country")
    df = df.set_index("Country")
    return df

answer_one()
# Question 2
def answer_two():
    # first section
    energy = pd.read_excel("Energy Indicators.xls", skiprows=17, skipfooter=(38), index_col=0, usecols=[2,3,4,5])
    energy.index.name = "Country"
    energy = (energy.rename(columns={"Petajoules": 'Energy Supply',
                                     "Gigajoules": 'Energy Supply per Capita',
                                     "%": '% Renewable'})
              .replace("...", np.nan)
              .reset_index())

    # " \(.*\)|[0-9]+" is "( any characters )" OR any numbers
    energy["Country"].replace(r" \(.*\)|[0-9]+","", regex=True, inplace=True)
    energy["Country"] = energy["Country"].replace({"Republic of Korea": "South Korea",
                                                   "United States of America": "United States",
                                                   "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                                                   "China, Hong Kong Special Administrative Region": "Hong Kong"})
    energy["Energy Supply"] *= 1000000

    # second section
    GDP = pd.read_csv("world_bank.csv", skiprows=4)
    GDP["Country Name"] = GDP["Country Name"].replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"})
    GDP = GDP[['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    GDP = GDP.rename(columns={"Country Name": "Country"})

    # third section
    ScimEn = pd.read_excel("scimagojr-3.xlsx")

    # fourth section - merge the databases - inner
    temp_1 = pd.merge(ScimEn, GDP, how="inner", left_on="Country", right_on="Country")
    df1 = pd.merge(temp_1, energy, how="inner", left_on="Country", right_on="Country")
    df1 = df1.set_index("Country")

    # fifth section - get outer, return difference
    temp_2 = pd.merge(ScimEn, GDP, how="outer", left_on="Country", right_on="Country")
    df2 = pd.merge(temp_2, energy, how="outer", left_on="Country", right_on="Country")
    df2 = df2.set_index("Country")
    return df2.shape[0]-df1.shape[0]

answer_two()
# Question 3

