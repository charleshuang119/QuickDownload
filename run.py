from flask import Flask,render_template,request
from modules import item

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("base.html")

@app.route("/result")
# get input from name=searuch,
def result_page():
    search = request.args.get('search')
    soup = item.find_search_content(search)
    all_item = item.every_video(soup)
    #take value of search and bring to result page
    return render_template("result.html",search=search,all_item = all_item )

if __name__=="__main__":
    app.run(debug=True)