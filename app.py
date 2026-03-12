from flask import Flask, render_template, request

app = Flask(__name__)

skills_list = ["Python", "SQL", "Linux"]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        # If the Clear button was clicked, empty the list
        if 'clear_btn' in request.form:
            skills_list.clear()
            
        # If the Add button was clicked, append the new skill
        elif 'add_btn' in request.form:
            new_skill = request.form.get('new_skill')
            if new_skill:
                skills_list.append(new_skill)
                
    return render_template('index.html', skills=skills_list)

if __name__ == '__main__':
    app.run(debug=True)