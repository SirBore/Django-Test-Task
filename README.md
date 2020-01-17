# Django-Test-Task
Model “Product”:
• name (CharField)
• category (choices: “Books”, “Movies”)
• price

Implement a login-protected view where products can be managed.
• There should be a datatable that shows currently existing products.
Implement the table using django-datatables-view:
https://bitbucket.org/pigletto/django-datatables-view/src/master/

• It should be possible to apply filters to the datatable:
2 checkboxes that trigger filtering by category (Books and Movies) via AJAX.
Hint: https://datatables.net/examples/server_side/custom_vars.html

• In the last column of the table should be links to the DeleteView and
UpdateView of the model. You can use separate views for those and don’t have 
to do it via modal.

• Somewhere above the table should be a button that triggers a modal to create a
new product.

# Notes:
• The UI doesn’t have to be fancy, this test is primarily to assess your Django skills
• Please make use of class based views and Django forms

Instruuctions on how to implement 

1. git clone https://github.com/SirBore/Django-Test-Task.git
2. cd Test
3. pip install -r requirements.txt
4. python manage.py createsuperuser
5. python manage.py runserver
6. Go to http://127.0.0.1:8000/signup 

