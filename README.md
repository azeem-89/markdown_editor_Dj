# markdown-editor
## Getting Started
Follow these instructions to set up the project locally.

## Prerequisites
- Python (version 3.6 or higher)
- Django (install using pip install django)
- Markdown2 (install using pip install markdown2)

## Installation
Clone the repository:
git clone https://github.com/your-username/markdown-editor-django.git

## Navigate to the project directory:

cd md-editor-project

## Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate 
On Windows, use `venv\Scripts\activate`

## Install dependencies:

pip install -r requirements.txt

## Apply database migrations:

python manage.py migrate

## Run the development server:

python manage.py runserver
Access the Markdown editor in your web browser at http://localhost:8000/.
