from flask import Flask, request, render_template
app = Flask(__name__)

def g_function(x):
    total = 0
    while x > 0:
        x = x // 10
        total += x
    return total

def f_function(x):
    if x <= 0:
        return "x ต้องมากกว่า 0"
    return (x - 1) // 9

@app.route('/', methods=['GET', 'POST'])
def index():
    g_result = None
    f_result = None
    if request.method == 'POST':
        try:
            x = int(request.form['x'])
            g_result = g_function(x)
            f_result = f_function(x)
        except:
            g_result = f_result = 'กรุณาใส่ตัวเลขจำนวนเต็มบวก'
    return render_template('index.html', g_result=g_result, f_result=f_result)

if __name__ == '__main__':
    app.run(debug=True)