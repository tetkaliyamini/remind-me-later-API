## Project Setup and Running Instructions

Follow these steps to set up and run your project:

1. **Create a virtual environment and install dependencies**:

```shellscript
# Create and activate a virtual environment
python -m venv venv
venv\bin\activate 

# Install required packages
pip install django djangorestframework
```


2. **Navigate to your project directory and run migrations**:

```shellscript
# Create database tables
python manage.py makemigrations
python manage.py migrate
```


3. **Start the development server**:

```shellscript
python manage.py runserver
```


4. **Your API will be available at**: `http://127.0.0.1:8000/api/reminders/`


## Testing the API

### Using cURL

```shellscript
curl -X POST \
  http://127.0.0.1:8000/api/reminders/ \
  -H 'Content-Type: application/json' \
  -d '{
    "date": "2025-06-01",
    "time": "14:30",
    "message": "Meeting with client",
    "method": "Email"
}'
```

### Using Postman

1. Open Postman
2. Create a new POST request to `http://127.0.0.1:8000/api/reminders/`
3. Set the request header: `Content-Type: application/json`
4. In the request body, select "raw" and "JSON", then enter:

```json
{
  "date": "2025-06-01",
  "time": "14:30",
  "message": "Meeting with client",
  "method": "Email"
}
```


5. Click "Send" to submit the request


## Project Structure Explanation

- **Models**: The `Reminder` model defines the database schema with fields for date, time, message, and method.
- **Serializers**: `ReminderSerializer` handles data validation and conversion between JSON and Python objects.
- **Views**: `ReminderListCreateView` processes the POST request, validates data, and saves it to the database.
- **URLs**: URL configuration routes the `/api/reminders/` endpoint to the appropriate view.


## Next Steps

- Add authentication to secure your API
- Implement GET, PUT, and DELETE endpoints for managing reminders
- Create a scheduled task to process reminders when they're due
- Add filtering and pagination for when you have many reminders
