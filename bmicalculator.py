from flask import Flask, request, render_template

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def welcome():
    bmi=""
    if request.method=="POST" and "Weight" in request.form:
        Weight = float(request.form.get("Weight"))
        Height = float(request.form.get("Height"))
        bmi = bmi_calc(Weight,Height)
    return render_template("bmi.html", bmi=bmi)
def bmi_calc(Weight,Height):
    return round((Weight / ((Height/100) ** 2) ),2)
app.run(debug=True)
