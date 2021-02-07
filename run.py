from flaskapp.app import app, creat_routes

if __name__ == "__main__":
    creat_routes()
    app.run(debug=True)