from flask import Flask

app= Flask("microblog")

@app.route("/")
def index():
    return "olámundo"

app.run()