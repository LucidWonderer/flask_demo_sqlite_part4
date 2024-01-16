
from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)

@app.route('/form', methods=['POST'])
def form_post():   # extract name from [post] using requests
    last_form_request = request.form['user_text']
    print(type(last_form_request))
    str_last_req = str(last_form_request)
    connection = sqlite3.connect(database="identifier.sqlite")
    db_cursor = connection.cursor()
    db_cursor.execute("insert into web_form_data('form_text') values (?)", (str_last_req,))
    connection.commit()
    connection.close()
    return render_template('form.html', last_request=last_form_request )


    # db_cursor.execute("insert into web_form_data('form_text') values (?)", (insert_variable,))
    # db_cursor.execute("insert into web_form_data('form_text') values(?)", ("inserts text",))

@app.route('/form', methods=['GET'])
def chat_get():
    last_request = "Good has more value than great. ~ me"
    return render_template('form.html', previous=last_request)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/home')
def render_home():  # each def name must be unique
    love_rocks = "Good has more value than great. ~ me"
    return render_template("home.html", app_data=love_rocks)


@app.route('/data')
def handle_data():  # notice the def name changes
    connection = sqlite3.connect(database="identifier.sqlite")
    results = connection.execute("SELECT * FROM web_form_data[form_text]")
    res = results.fetchall()
    connection.close()
    tbl_str, text_simple = display_table(res)
    return render_template("data.html", db_records=res[0][1], table_string=text_simple)






def display_table(database_result):
    tbl_start = "<table class='dyno'>"
    tbl_hd = "<th><tr>Data From Web Form</tr></th>"
    tr_start = "<tr>"
    row_data = ""
    tr_end = "</tr>"
    tbl_end = "</table>"
    text_simple = ""
    table_final = tbl_start + tbl_hd + tr_start
    for each, value in database_result:
        table_final += tr_start + value + tr_end
        text_simple += value + ","
    table_final += tbl_end
    return table_final, text_simple

if __name__ == '__main__':
    app.run()
