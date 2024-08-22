from inventory import create_app
from tests import test_auth

app = create_app()
test_app=test_auth.create_app()

if __name__ == '__main__':
    test_app.run(debug=True)
    app.run(debug=True)
