from flask import Flask, render_template, request, session, redirect
from modules import item
from modules.user import User
from common.database import Database

app = Flask(__name__)
app.secret_key = "kevin@test.com"


@app.before_first_request
def init_db():
    Database.initialize()


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def login_method():
    session['inLoginPage'] = True
    session['inRegisterPage'] = False
    if request.method == 'POST':
        account = request.form['InputAccount']
        password = request.form['InputPassword']
        check = User.is_login_valid(account, password)
        if check == True:
            session['account'] = account
            session['name'] = User.find_user_data(account).get('name')
            session['login'] = True
            return redirect("/")
        else:
            message = "Your account or password is invalid !!"
            return render_template("login.html", message=message)
    else:
        return render_template("login.html")


@app.route("/register", methods=['GET', 'POST'])
def register_method():
    session['inLoginPage'] = False
    session['inRegisterPage'] = True
    if request.method == 'POST':
        name = request.form['InputName']
        account = request.form['InputAccount']
        password = request.form['InputPassword']
        result = User.register_user(name, account, password)
        if result == True:
            session['account'] = account
            session['name'] = User.find_user_data(account).get('name')
            return redirect("/")

        else:
            message = "Your account is already exist !!"
            return render_template("register.html", message=message)
    else:
        return render_template("register.html")


@app.route("/logout")
def logout_method():
    session['account'] = None
    session['login'] = False
    session['inLoginPage'] = False
    session['inRegisterPage'] = False
    return redirect("/")


@app.route("/results")
# get input from name=searuch,
def result_page():
    page = request.args.get('sp')
    # if page bar dosen't exist in the page, then it is the first page,
    if page == None:
        search = request.args.get('search')
        soup = item.find_search_content(search)
        all_item = item.every_video(soup)
        all_page = item.page_bar(soup)
        # take value of search and bring to result page
        return render_template("result.html", search=search, all_item=all_item, all_page=all_page)
    # if page exist, which mean it's nexts
    elif page != None:
        search = request.args.get('search_query')
        page = request.args.get('sp')
        current_page = request.args.get('current_page')
        # Get URL of next page
        value = "search_query={}".format(search) + "&" + "sp={}".format(page)
        # Get content of next page
        soup = item.find_page_content(value)
        all_item = item.every_video(soup)
        all_page = item.page_bar(soup)
        # take value of search and bring to result page
        return render_template("result_page.html", search=search, all_item=all_item, all_page=all_page,
                               current_page=current_page, int=int)


@app.route("/download")
def download():
    value = request.args.get('value')
    download_type, url = value.split('&')
    if download_type == "MP3":
        item.download_mp3(url)
        return render_template("download.html")
    elif download_type == "MP4":
        item.download_mp4(url)
        return render_template("download.html")


if __name__ == "__main__":
    app.run(debug=True)
