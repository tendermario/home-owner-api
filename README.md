# Home Owner API

# Create db

`uv run manage.py migrate`

# Run

`uv run manage.py runserver`

# Testing

`apt install httpie`

`uv run manage.py createsuperuser`
`http --session ./session GET localhost:8000"`
`http --session ./session POST localhost:8000/login email="m@m.com" password="testtest" X-CSRFToken:...`
