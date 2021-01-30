from flask import Flask,render_template,request,jsonify 

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
        
    return render_template('order.html',numbers=orders,quantity=count)

  else:
    return render_template('order.html')
    
@app.route('/visneta', methods=['POST','GET'])
def visneta():
  
  if request.method == 'POST':

    count = 0
    final_text = None
    
    filer = request.files['filer']
    fh = str(filer.read())
    
    parts = fh.split('Inspection - ')
    # locator = parts[30].find('\\t')
    # endor = parts[30].find('-1')
    # hello = parts[30][locator+2:endor]
    
    for part in parts:
      if '-1 ' in part:
        count += 1
        start_pos = part.find('\\t')
        end_pos = part.find('-1')
        temporal = part[start_pos+2:end_pos]
              
        if final_text is None:
          final_text = temporal + ' - 1'
        else:
          final_text += ',' + temporal + ' - 1'
          
    # return jsonify(final_text,count)
    return render_template('visneta.html',filecon=final_text,quantity=count)
  
  else:
    return render_template('visneta.html')

# @app.route('/national-field')




if __name__ == '__main__':
    app.run(debug=True)