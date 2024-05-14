from app import app 
@app.context_processor
def inject_user():
  return dict (user=g.user)
pr