from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/order', methods=['POST','GET'])
def ordernumber():

  if request.method == 'POST':
    content = request.form['contener']
    new = content.split('INSPECTION')
    orders = None
    count = 0
    for text in new:
      if '#' in text:
        count += 1
        
        done = text.split()
        if orders is None:
          orders = done[0][1:]
        else:
          orders += ',' + done[0][1:] 
        
        # if stringer == None:
        #   stringer = numb[1:]
        # else:
        #   stringer += ',' + numb[1:]
    return render_template('order.html',numbers=orders,quantity=count)

  else:
    return render_template('order.html')
    
# @app.route('/vineta')
# def order():

# def vineta():

# @app.route('/national-field')




if __name__ == '__main__':
    app.run(debug=True)