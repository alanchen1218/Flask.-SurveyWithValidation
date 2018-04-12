from flask import Flask , render_template, redirect, request, flash
app = Flask(__name__)  
app.secret_key = "ThisIsSecret!"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def next():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    # print(name, location, language, comment)
    if len(name) < 1:
        flash("Please enter a name")
        return redirect('/')
    if len(comment) > 120:
        flash("A comment cannot be more than 120 characters")
        return redirect('/')
    else:
        return render_template('results.html', name=name, location=location, language=language, comment=comment)

@app.route('/index')
def back():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True) 