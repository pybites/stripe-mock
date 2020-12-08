from unittest.mock import patch


@patch('project.services.stripe.Customer.create')
def test_create_customer(stripe_mock, app):
    stripe_mock.return_value = {"name": "bob"}  # your mock object
    with app.test_client() as test_client:
        response = test_client.get('/call-stripe/will')
        assert response.status_code == 200
