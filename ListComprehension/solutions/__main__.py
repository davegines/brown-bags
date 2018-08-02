from ListComprehension import sample_data


# Return all of the years from the sample_data.years array
def one():
    years = [year for year in sample_data.years]
    return years


# Return all of the odd years from the sample_data.years array
def two():
    odd_years = [year for year in sample_data.years if year % 2 == 1]
    return odd_years


# For each given year in sample_data.years, return all 12 months from sample_data.months so the year and month are
# a record. Format however you'd like
def three():
    years_and_months = ['{}-{}'.format(year, month) for year in sample_data.years for month in sample_data.months]
    return years_and_months


# For each odd year in sample_data.years, return the odd months from sample_data.months so the year and month are
# a record. Format however you'd like
def four():
    odd_year_odd_month = ['{}-{}'.format(year, month) for year in sample_data.years if year % 2 == 1
                          for month in sample_data.months if sample_data.months.index(month) % 2 == 0]
    return odd_year_odd_month


print('*** #1 ***')
print(one())

print('*** #2 ***')
print(two())

print('*** #3 ***')
print(three())

print('*** #4 ***')
print(four())
