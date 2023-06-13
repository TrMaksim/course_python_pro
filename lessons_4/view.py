from flask import Flask, request
from bd_pratice import get_customers


app = Flask(__name__)


@app.route('/customers')
def customers():
    state_name = request.args.get('state_name')
    city_name = request.args.get('city_name')

    customers_list = get_customers(state_name, city_name)

    return '\n'.join(customers_list)


if __name__ == '__main__':
    app.run()
