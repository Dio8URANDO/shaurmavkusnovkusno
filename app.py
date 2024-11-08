from flask import Flask, render_template, request

app = Flask(__name__)

# Страница для оформления заказа
@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        # Получаем данные заказа из формы
        shaurma_type = request.form['shaurma_type']
        price = 250 if shaurma_type == 'chicken' else 300  # Цены для куриной и говяжьей шаурмы
        # Здесь вы можете добавить логику для обработки оплаты, например, с использованием Stripe

        return render_template('confirmation.html', shaurma_type=shaurma_type, price=price)

    return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True)
