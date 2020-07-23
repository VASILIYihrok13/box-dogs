from flask import Flask, flash, redirect, render_template, url_for, request
import datetime

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
	if request.method == 'POST':
		date_from_user = request.form['date']
		error = None 
		
		if not date_from_user:
			error = "Incorrect date"
		
		if error is not None:
			flash(error)
		else:
			days = counting_days(date_from_user)
			weeks = int(days) // 7
			month = counting_month(date_from_user)

			return render_template('index.html', days = days, weeks = weeks, month = month)

	return render_template('index.html')

def counting_month(date_from_user):
	''' лічимо кількість місяців між двома датами за методом якщо вказано 25 то да 25 наступного місяця '''
	user_time = date_from_user.split('-')
	user = datetime.date(int(user_time[0]), int(user_time[1]), int(user_time[2]))
	date_now = datetime.date.today()
	month_between = (date_now.year - user.year) * 12 + (date_now.month - user.month)
	
	# якщо день який вказав юзер більший за день сьогодні забираємо один місяць. бо він ще не дійшов ))
	if user.day > date_now.day: 
		month_between -= 1

	return month_between

def counting_days(date_from_user):
	'''лічимо різницю днів між народженням користувача й сьоfгодні'''
	user_time = date_from_user.split('-')
	user = datetime.date(int(user_time[0]),int(user_time[1]),int(user_time[2]))
	date_now = datetime.date.today()
	days_between = abs(user - date_now)
	
	return str(days_between).split()[0]

