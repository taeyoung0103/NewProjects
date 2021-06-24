from flask import Flask, request, render_template
from dao import EDAO
from dto import EDTO
from dtoo import EODTO
from daoo import EODAO

app = Flask(__name__)
app.config["SECRET_KEY"] = "alert"

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')

@app.route('/signin', methods=['POST'])
def signin():

    error = None

    admin_id = 'admin'
    admin_pw = '9876'
    guest_id = 'guest'
    guest_pw = '1234'

    if request.form.get('id') == admin_id and \
       request.form.get('pw') == admin_pw:

        return render_template('admin.html')

    elif request.form.get('id') == guest_id and \
         request.form.get('pw') == guest_pw:

        return render_template('guest.html') 

    else:
        error = "Please check the information you've entered"
        return render_template('main.html', error = error)
        

@app.route("/custnumber", methods=["post"])
def custnumber():
    dao = EDAO()
    order_id = request.form.get('order_id')
    # data = dao.empone(order_id)
    # return data
    return dao.empone(order_id)

# --------------------------------------------------------

@app.route("/insert", methods=["post"])
def inserproduct():
    daoo = EODAO()
    dtoo = EODTO(request.form.get("product_id"), request.form.get("product_name"), request.form.get("standard_cost"), request.form.get("list_price"), request.form.get("category_id"))
    print(dtoo)
    print('------1------')
    daoo.insertproduct(dtoo)
    print('------2------')

    return ''


@app.route("/update", methods=["put"])
def updateProduct():
    daoo = EODAO()
    dtoo = EODTO(request.form.get("product_id"), request.form.get("product_name"),0, request.form.get("list_price"),0)
    
    print(dtoo)
    daoo.updateProduct(dtoo)

    return ''


@app.route('/delete', methods=['DELETE'])
def deleteProduct():
    # dao = EDAO()
    daoo = EODAO()
    product_id = EODTO(request.form.get("product_id"), request.form.get("product_name"), request.form.get("standard_cost"), request.form.get("list_price"), request.form.get("category_id"))
    daoo.deleteproduct(product_id)

    return ''



if __name__ == '__main__':
    app.run(port = 5050, debug = True)
