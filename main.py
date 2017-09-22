from flask import Flask, request

app = Flask (__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }

            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action ="/" method="POST">
            <label> 
                Rotate by:
                <input type="text" name="rot" value=0 />
            </lable><br>
            <input type="textarea" name="text" />
            <input type="submit" value="Submit Query"
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']

    for char in text:
        if (char.isalpha()):
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char

    return "<h1>rotated</h1>"


app.run()