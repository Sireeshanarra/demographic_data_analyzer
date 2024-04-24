import pandas as pd

# Load the dataset
data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']
df = pd.read_csv(data_url, names=column_names, na_values=' ?')

# 1. Count of People by Race
race_counts = df['race'].value_counts()

# 2. Average Age of Men
average_age_men = df[df['sex'] == ' Male']['age'].mean()

# 3. Percentage of People with a Bachelor's Degree
percentage_bachelors = (df['education'] == ' Bachelors').mean() * 100

# 4. Percentage of People with Advanced Education Earning >50K
higher_education = df['education'].isin([' Bachelors', ' Masters', ' Doctorate'])
percentage_high_earners = (df[higher_education & (df['salary'] == ' >50K')].shape[0] / df[higher_education].shape[0]) * 100

# 5. Percentage of People without Advanced Education Earning >50K
lower_education = ~higher_education
percentage_low_earners = (df[lower_education & (df['salary'] == ' >50K')].shape[0] / df[lower_education].shape[0]) * 100

# 6. Minimum Number of Hours Worked per Week
min_work_hours = df['hours-per-week'].min()

# 7. Percentage of Minimum Hours Workers Earning >50K
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage = (num_min_workers[num_min_workers['salary'] == ' >50K'].shape[0] / num_min_workers.shape[0]) * 100

# 8. Country with the Highest Percentage of People Earning >50K
highest_earning_country = (df[df['salary'] == ' >50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
highest_earning_country_percentage = (df[df['native-country'] == highest_earning_country]['salary'] == ' >50K').mean() * 100

# 9. Most Popular Occupation for High Earners in India
top_IN_occupation = df[(df['native-country'] == ' India') & (df['salary'] == ' >50K')]['occupation'].value_counts().idxmax()

# Display the results
print("Question 1:")
print(race_counts)
print("\nQuestion 2:")
print(round(average_age_men, 1))
print("\nQuestion 3:")
print(round(percentage_bachelors, 1))
print("\nQuestion 4:")
print(round(percentage_high_earners, 1))
print("\nQuestion 5:")
print(round(percentage_low_earners, 1))
print("\nQuestion 6:")
print(min_work_hours)
print("\nQuestion 7:")
print(round(rich_percentage, 1))
print("\nQuestion 8:")
print(f"{highest_earning_country}: {round(highest_earning_country_percentage, 1)}%")
print("\nQuestion 9:")
print(top_IN_occupation)
