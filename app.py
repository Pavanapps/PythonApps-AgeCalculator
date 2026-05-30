from flask import Flask, render_template, request
from datetime import datetime, date

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    age = None
    next_birthday = None
    days_lived = None
    error = None

    if request.method == 'POST':

        try:
            dob_str = request.form['dob']
            dob = datetime.strptime(dob_str, "%Y-%m-%d").date()

            today = date.today()

            # Calculate age
            age = today.year - dob.year - (
                (today.month, today.day) < (dob.month, dob.day)
            )

            # Days lived
            days_lived = (today - dob).days

            # Next birthday
            next_bday_year = today.year

            if (today.month, today.day) > (dob.month, dob.day):
                next_bday_year += 1

            next_birthday = date(next_bday_year, dob.month, dob.day)

        except Exception as e:
            error = f"Error: {str(e)}"

    # IMPORTANT: This return must be outside the if block
    return render_template(
        'index.html',
        age=age,
        next_birthday=next_birthday,
        days_lived=days_lived,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True)