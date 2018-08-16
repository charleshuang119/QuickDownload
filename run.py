from flask import Flask,render_template,request
from modules import item

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("base.html")

@app.route("/results")
# get input from name=searuch,
def result_page():
    page = request.args.get('sp')
    #if page bar dosen't exist in the page, then it is the first page,
    if page == None :
        search = request.args.get('search')
        soup = item.find_search_content(search)
        all_item = item.every_video(soup)
        all_page=item.page_bar(soup)
        #take value of search and bring to result page
        return render_template("result.html",search=search,all_item = all_item,all_page = all_page )
    #if page exist, which mean it's nexts
    elif page != None :
        search = request.args.get('search_query')
        page = request.args.get('sp')
        current_page = request.args.get('current_page')
        #Get URL of next page
        value = "search_query={}".format(search)+"&"+"sp={}".format(page)
        #Get content of next page
        soup = item.find_page_content(value)
        all_item = item.every_video(soup)
        all_page = item.page_bar(soup)
        # take value of search and bring to result page
        return render_template("result_page.html", search=search, all_item=all_item, all_page=all_page, current_page=current_page, int=int)

@app.route("/download")
def download():
    value = request.args.get('value')
    download_type,url=value.split('&')
    if download_type=="MP3":
        item.download_mp3(url)
        return render_template("download.html")
    elif download_type=="MP4":
        item.download_mp4(url)
        return render_template("download.html")


if __name__=="__main__":
    app.run(debug=True)