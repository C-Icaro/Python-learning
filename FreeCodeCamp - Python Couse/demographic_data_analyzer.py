import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("FreeCodeCamp - Python Couse/adult.data.csv")
    #print(df.head())

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df[(df.sex == "Male")]["age"].mean()

    #df['sex'] == "Male" cria uma máscara booleana (True/False para cada linha).
    # df[df['sex'] == "Male"] filtra o DataFrame, retornando apenas as linhas onde sex é "Male".
    # ['age'] seleciona apenas a coluna "age" desse DataFrame filtrado.
    # .mean() calcula a média dos valores dessa coluna.  

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df["education"].value_counts(normalize=True)["Bachelors"]*100

    ''' 
    O método value_counts() espera um booleano para normalizar ou não.

    Após o value_counts, os valores únicos da coluna (como "Bachelors") viram índices (chaves) da Series resultante. Assim, você pode acessar diretamente o valor associado a "Bachelors" como faria em um dicionário.
    No DataFrame original, "Bachelors" é apenas um valor em uma coluna, não uma chave.
    '''

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    vc = df["education"].value_counts(normalize=False)
    higher_education = vc["Bachelors"] + vc["Masters"] + vc["Doctorate"]
    lower_education = df["education"].count() - higher_education

    # percentage with salary >50K
    higher_education_rich = df[(df["education"].isin(["Bachelors", "Masters", "Doctorate"])) & (df["salary"] == ">50K")].shape[0]
    lower_education_rich = df[(~df["education"].isin(["Bachelors", "Masters", "Doctorate"])) & (df["salary"] == ">50K")].shape[0]

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df["hours-per-week"] == min_work_hours].shape[0]

    rich_min_workers = df[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")].shape[0]
    rich_percentage = (rich_min_workers / num_min_workers) * 100 if num_min_workers > 0 else 0

    # What country has the highest percentage of people that earn >50K?
    country_perc = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100).dropna()
    highest_earning_country = country_perc.idxmax()
    highest_earning_country_percentage = country_perc.max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0] if not df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].empty else None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data()