from flask import Flask, render_template, request

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send1', methods=['POST'])
def retirement_():
    if request.method=='POST':
        try:
            age=int(request.form['age'])
            annual_salary=int(request.form['annual_salary'])
            percentage_saved=int(request.form['percentage_saved'])
            savings_goal=int(request.form['savings_goal'])
            checker=True
        except:
            checker=False
        if(checker==True):
            years_to_achieve =retirement__(age, annual_salary, percentage_saved, savings_goal)
            return render_template('index.html',years_to_achieve="It takes "+str(years_to_achieve), age_="You will achieve at the age of "+str(float(years_to_achieve)+age))

        elif(checker==False):
            age_error="Age needs to be an integer and less than 100"
            annual_salary_error="Annual salary needs to be an integer"
            percentage_saved_error="Percentage saved needs to be an integer"
            savings_goal_error="Savings goal needs to be an integer"
            return render_template('index.html', age_error=age_error, annual_salary_error=annual_salary_error, percentage_saved_error=percentage_saved_error, savings_goal_error=savings_goal_error)

       

def retirement__(age, annual_salary, percentage_saved, savings_goal):
        
    monthly_salary=annual_salary/12
    monthly_saving=monthly_salary*(percentage_saved/100)
    monthly_saving=monthly_saving+(monthly_saving*(35/100))
    yearly_saving=monthly_saving*12
    years_to_achieve=round((savings_goal/yearly_saving),2)
    
    return years_to_achieve



@app.route('/send', methods=['POST'])
def bmi_():
    if request.method =='POST':
        try:
            weight_pounds=int(request.form['weight_pounds'])
            height_feet=int(request.form['height_feet'])
            height_inches=int(request.form['height_inches'])
            checker=True
        except:
            checker=False
        if(checker):
            BMI__=bmi(weight_pounds, height_feet, height_inches)
            BMI_ct=""
            if(BMI__<=18.5):
                BMI_ct="underweight"
            elif(BMI__>18.5 and BMI__<24.9):
                BMI_ct="normal weight"
            elif(BMI__>25 and BMI__<29.9):
                BMI_ct="over weight"
            elif(BMI__>=30):
                BMI_ct="obese"
            return render_template('index.html',BMI__=BMI__, BMI_ct=BMI_ct )
        elif(checker==False):
            return render_template('index.html', weight_error="Weight needs to be an integer", feet_error="Height in feet needs to be an integer", inch_error="Height in inches need to be an integer")
def bmi(weight_pounds, height_feet, height_inches):
        weight_kilograms=weight_pounds*0.45
        height_meters=((height_feet*12)+(height_inches))*0.025
        BMI__=float(format((weight_kilograms)/(height_meters*height_meters), '.2f'))
        return BMI__


if(__name__=="__main__"):
    app.run(debug=True)