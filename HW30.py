from datetime import date
from dateutil.rrule import rrule, DAILY

# initializing the start and end date
start_date = date(2023, 3, 27)
end_date = date(2023, 8, 1)

lecture_numbers = 0
lecture_dates = []
# iterating over the dates
for d in rrule(DAILY, dtstart=start_date, until=end_date):
    if lecture_numbers < 32:
        if d.strftime("%A") == "Monday" or d.strftime("%A") == "Thursday":
            lecture_numbers += 1
            lecture_dates.append(f"Lecture  {lecture_numbers:>2}: {d.strftime('%d %b %Y')} 19:15")

for i in lecture_dates:
    print(i)

