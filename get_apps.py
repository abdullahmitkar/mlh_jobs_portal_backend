from flask import request
from flask import session
from flask import render_template
from vaccine_blueprint import vaccine_blueprint

import utils

@vaccine_blueprint.route('/getapps', methods=['GET'])
def get_apps():
    print(request)
    error = None
    # if request.method == 'POST':
    #     print("===================")
    #     print("Request", request.json["name"])
    #     print("===================")
    #     request_dict = {"name": request.json['name'], "password":request.json['password'], "portal":request.json['portal']}
    #     # print(request_dict)
    #     done_flag, user_detail = db_main.insert_user(request_dict)
    #     # if done_flag:
    #     #     flash('You are successfully registered. Your User ID is:  {}'.format(user_detail))
    #     #     return render_template('login_redirect.html', error=error)
    #     # else:
    #     #     flash('Cannot register. {}'.format(user_detail))
    #     #     return render_template('login_redirect.html', error=error)

    if request.method == 'GET':
        # print(request.form["name"])
        data = {}

        data["companyName"]="Company";
        data["role"]="SDE";
        data["location"]="NY";
        data["status"]="ACC";

        return data;
        # return render_template('register.html', error=error)