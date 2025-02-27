from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kamlakant'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:kamlakant@localhost/expense'  
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow().date())   

    def __repr__(self):
        return f'<Expense {self.description}>'

with app.app_context(): 
    db.create_all()  

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        category = request.form['category']
        date_str = request.form.get('date') 

        try:
            amount = float(amount)
            if date_str:
                date = datetime.strptime(date_str, '%Y-%m-%d').date() 
            else:
                date = datetime.utcnow().date() 
            new_expense = Expense(description=description, amount=amount, category=category, date=date)
            db.session.add(new_expense)
            db.session.commit()
            flash('Expense added!', 'success')
            return redirect(url_for('index'))
        except ValueError:
            flash('Invalid input. Please check amount and date format.', 'danger')
        except Exception as e: 
            flash(f'An error occurred: {e}', 'danger')


    expenses = Expense.query.order_by(Expense.date.desc()).all() 
    total_expenses = sum(expense.amount for expense in expenses)
    return render_template('index.html', expenses=expenses, total_expenses=total_expenses)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted!', 'info')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)