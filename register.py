from flask import request
from flask import session
from flask import render_template, flash
from vaccine_blueprint import vaccine_blueprint

from db_module import db_main

@vaccine_blueprint.route('/register', methods=['POST', 'GET'])
def register():
    print(request)
    error = None
    if request.method == 'POST':
        print("===================")
        print("Request", request.json["name"])
        print("===================")
        request_dict = {"name": request.json['name'], "password":request.json['password'], "portal":request.json['portal']}
        # print(request_dict)
        done_flag, user_detail = db_main.insert_user(request_dict)
        # if done_flag:
        #     flash('You are successfully registered. Your User ID is:  {}'.format(user_detail))
        #     return render_template('login_redirect.html', error=error)
        # else:
        #     flash('Cannot register. {}'.format(user_detail))
        #     return render_template('login_redirect.html', error=error)

    elif request.method == 'GET':
        print(request.form["name"])
        return render_template('register.html', error=error)

    return render_template('register.html', error=error)

    #
    #
    # return render_template('register.html', error=error)

