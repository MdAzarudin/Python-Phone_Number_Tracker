from flask import Flask,render_template,request
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def home():
    if request.method == "POST":

        number = request.form.get("Number")
        number1 = phonenumbers.parse(number, "CH")
        country = geocoder.description_for_number(number1,"en")
        print(geocoder.description_for_number(number1, "en"))

        number2 = phonenumbers.parse(number, "RO")
        sim = carrier.name_for_number(number2,"en")
        print(carrier.name_for_number(number2,"en"))

        return render_template ("index.html", box = country, bag = sim, pen = number1, pen1 = number2 )
    return render_template ("index.html")

if __name__ == "__main__":
    app.run(debug=True)