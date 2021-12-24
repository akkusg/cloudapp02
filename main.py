from flask import Flask, render_template, request, redirect, session
import pymongo


from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'bizim cok zor gizli sozcugumuz'

myclient = pymongo.MongoClient("mongodb+srv://yeditepeuser:yeditepe34@cluster0.tqcqy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb = myclient["atlasDenemeDB"]
kullanicilar_tablosu = mydb["kullanicilar"]





@app.route('/')
def baslangic():
    return "Ana Sayfa"


@app.route('/kullanicilar')
def kullanicilari_listele():
    kullanicilar = list(kullanicilar_tablosu.find({}))
    return render_template("kullanicilar.html", kullanicilar=kullanicilar)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

