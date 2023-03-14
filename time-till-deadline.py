import datetime

user_input = input("enter the goal along with deadline in date format separated by colon:\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

today_date = datetime.datetime.today()

remaining_time = deadline_date - today_date
# remaining_days_split = str(remaining_time).split(",")
# remaining_days = remaining_days_split[0]
print(f"Dear user you have {remaining_time.days} left to reach your goal : {goal}")
print(f"That means you have {int(remaining_time.total_seconds() / 60 /60) } hours left.")

