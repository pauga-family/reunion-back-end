from app import app

@app.route('/')
def inded():
	return "Hello, World!"
