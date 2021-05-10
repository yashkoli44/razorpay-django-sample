# razorpay-django-sample
<h1>Razorpay Django Sample app</h1>

Check <a href="https://github.com/yashkoli44/razorpay-django-sample/blob/master/templates/payment.html">templates/payment.html<a> and update with your app_key that you generated in your Razorpay Dashboard, or for any help <a href="https://razorpay.com/docs/payment-gateway/server-integration/python/usage/#generate-api-key">click here</a>

Customize <a href="https://github.com/yashkoli44/razorpay-django-sample/blob/master/templates/success.html">template/success.html</a> as you want your success page to look like.

Update <a href="https://github.com/yashkoli44/razorpay-django-sample/blob/a21cc54cd4384023299b0b5004eed882e42cb16e/payment_integrator/views.py#L8">payment_integrator/views.py</a>

<code>razorpay_client = razorpay.Client(auth=("<YOUR_KEY>", "<YOUR_SECRET>"))</code>

with your key and secret provided by Razorpay.

**After updating above files**, run the app:

App is based on <b>Pipenv</b> Environment.

So install pipenv:

```
pip install pipenv
```

Run following commands inside app's root folder that is where manage.py file is located:

```
pipenv install
pipenv shell
python manage.py runserver
```

And then type **127.0.0.1:8000** in browser url.

After all, the app is all yours so customize it as you want.
