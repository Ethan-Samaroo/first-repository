from datetime import date, datetime
now = datetime.now()
new_year = datetime(1970, 1, 1)
result = now - new_year
print(result)