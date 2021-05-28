# razorpay-django-sample
<h1>Razorpay Django Sample app</h1>

We assume that you have already created a Django Project with following command:
```
django-admin startproject yourappname
```

<br>

<h3>Initial setup to your existing Django Project:</h3>

- Open your project's settings.py and add following line in INSTALLED_APPS list (ignore dots):

	```
	...


	INSTALLED_APPS = [
		...
		'payment_integrator.apps.PaymentIntegratorConfig'
	]


	...
	``` 

- Download and extract this project and copy payment_integrator folder to your project's root
- Copy html files from templates folder to your project's template directory
- Update urls.py of your project pointing to payment_integrator, for example:
	
	```
	urlpatterns = [
		...
		path("", include("payment_integrator.urls")),  # I am using home page as payment, customize accordingly
	]
	```
	


<br/>
<br/><br/>
<h3>Post-Initial Setup</h3>

- Check <a href="https://github.com/yashkoli44/razorpay-django-sample/blob/master/templates/payment.html">templates/payment.html<a> and update with your app_key that you generated in your Razorpay Dashboard, or for any help <a href="https://razorpay.com/docs/payment-gateway/server-integration/python/usage/#generate-api-key">click here</a>

- Customize <a href="https://github.com/yashkoli44/razorpay-django-sample/blob/master/templates/success.html">template/success.html</a> as you want your success page to look like.

- Update <a href="https://github.com/yashkoli44/razorpay-django-sample/blob/a21cc54cd4384023299b0b5004eed882e42cb16e/payment_integrator/views.py#L8">payment_integrator/views.py</a> with your key and secret provided by Razorpay.

	<code>razorpay_client = razorpay.Client(auth=("<YOUR_KEY>", "<YOUR_SECRET>"))</code>


App is ready to run.

After all, the app is all yours so customize it as you want.
