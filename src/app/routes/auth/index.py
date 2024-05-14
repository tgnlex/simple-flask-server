from flask import session, make_response, request, redirect, url_for
from src import app

@app.route('/auth')
def index():
  if 'username' in session:
    return f'Logged in as {session['username']}'
  return 'You are not logged in.'

@app.post('/auth/login')
def post_register():
  ############################## TODO #########################################
  # data = request.form['username', 'email', 'password','confirmed', 'terms'] #
  # validated = validate_function(data)                                       #
  # if validated === True:                                                    #
  #   add_user(validated)                                                     #
  # else                                                                      #
  # return make_response('something went wrong')                              #
  #############################################################################
  # validation and add_user functions needed first #
  ##################################################
  return make_response('Post @ login hit')

@app.post('/auth/login')  
def post_login():
  session['username'] = request.form['username', 'password', 'enail']
  return make_response('Post @ register hit')

@app.post('/auth/logout')
def post_logout():
  session.pop()
  make_response('Post @ Logout hit')
  return redirect(url_for('index'))