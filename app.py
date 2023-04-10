from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        num_sets = int(request.form['num_sets'])
        num_per_set = int(request.form['num_per_set'])
        num_range = request.form['num_range']
        start, end = map(int, num_range.split('-'))

        if num_sets <= 0:
            raise ValueError("Number of sets must be greater than zero.")
        if num_per_set <= 0:
            raise ValueError("Number of numbers per set must be greater than zero.")
        if start >= end:
            raise ValueError("Range start must be less than range end.")
    except (ValueError, TypeError) as e:
        return render_template('error.html', message=str(e))

    result_sets = []
    for i in range(num_sets):
        result_set = []
        for j in range(num_per_set):
            result_set.append(random.randint(start, end))
        result_sets.append(result_set)

    return render_template('result.html', result_sets=result_sets, num_sets=num_sets)

if __name__ == '__main__':
    app.run(debug=True)