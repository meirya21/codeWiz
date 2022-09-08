import os
from crypt import methods
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from form import *
from ldap_authentication import *
import pyotp


app = Flask(__name__, template_folder="./templates")

bootstrap = Bootstrap(app)
app.config.from_object('settings')
app.secret_key = os.urandom(24)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

csrf = CSRFProtect(app)


@app.route('/', methods=['GET','POST'])
def login():

    form = LoginValidation()

    if request.method in ('POST') :
        login_id = form.user_name.data
        login_password = form.user_pass.data

        login_msg = ldap_authentication(login_id, login_password)

        if login_msg == "Success":
            success_message = f"*** Authentication Success "
            flash(success_message)
            return redirect('/2fa/')

        else:
            error_message = f"*** Authentication Failed - {login_msg}"
            flash(error_message)
            return render_template('login.html', form=form)

    return render_template('login.html', form=form)


@app.route("/2fa/")
def login_mfa():
    secret = pyotp.random_base32()
    return render_template("login_mfa.html", secret=secret)


@app.route("/2fa/", methods=["POST"])
def login_mfa_form():
    secret = request.form.get("secret")
    otp = int(request.form.get("otp"))


    if pyotp.TOTP(secret).verify(otp):
        flash("Welcome")
        return redirect(url_for("login_mfa"))
    else:
        flash("Wrong token!, Try again")
        return redirect(url_for("login_mfa"))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8888)