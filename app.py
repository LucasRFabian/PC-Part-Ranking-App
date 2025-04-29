from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3

app = Flask(__name__)
application = app
DATABASE = 'partrankings.db'

# Initialize Database Connection
def db_get():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

# Close Database Connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Form Page
@app.route('/', methods=['GET', 'POST'])
def index():
    db = db_get()
    
    # Database Query
    gpu_models = [row['gpu_model'] for row in db.execute('SELECT gpu_model FROM gpurankings').fetchall()]
    cpu_models = [row['cpu_model'] for row in db.execute('SELECT cpu_model FROM cpurankings').fetchall()]
    
    if request.method == 'POST':
        selected_gpu = request.form.get('gpu_field')
        selected_cpu = request.form.get('cpu_field')
        
        return redirect(url_for('results', gpu=selected_gpu, cpu=selected_cpu))
    
    # Get Part Names for Form
    return render_template('index.html', gpu_models=gpu_models, cpu_models=cpu_models)

# Results Page
@app.route('/results')
def results():
    gpu_name = request.args.get('gpu')
    cpu_name = request.args.get('cpu')
    db = db_get()
    
    # Query GPU Table
    gpu_data = db.execute('SELECT gpu_model, ranking FROM gpurankings WHERE gpu_model = ?', (gpu_name,)).fetchone()

    # Query CPU Table
    cpu_data = db.execute('SELECT cpu_model, ranking FROM cpurankings WHERE cpu_model = ?', (cpu_name,)).fetchone()

    # Get Total Number of Entries
    gpu_count = db.execute('SELECT COUNT(*) FROM gpurankings').fetchone()[0]
    cpu_count = db.execute('SELECT COUNT(*) FROM cpurankings').fetchone()[0]

    # Total System Score Calculation
    if cpu_data and gpu_data:
        raw_score = (cpu_data[1] / cpu_count + gpu_data[1] / gpu_count)
        if (raw_score < .1):
            total_score = "S"
        elif (raw_score < .2 and raw_score >= .1):
            total_score = "A"
        elif (raw_score < .3 and raw_score >= .2):
            total_score = "B"
        elif (raw_score < .4 and raw_score >= .3):
            total_score = "C"
        elif (raw_score < .5 and raw_score >= .4):
            total_score = "D"
        else:
            total_score = "F"
    else:
        total_score = None

    return render_template('results.html', gpu=gpu_data, cpu=cpu_data, gpu_count=gpu_count, cpu_count=cpu_count, total_score=total_score)

@app.route('/guide')
def guide():
    return render_template('guide.html')

if __name__ == '__main__':
    app.run(debug=True)