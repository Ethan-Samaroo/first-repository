from datetime import datetime
now = datetime.now()
date = datetime.strftime(now, "%m/%d/%Y, %H:%M:%S")
print(date)