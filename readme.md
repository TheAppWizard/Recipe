# Recipe Mock Backend

This project is a mock backend for a recipe management system built with Python Flask and Pandas. It uses an Excel file as a database for storing recipe information.

## Table of Contents
1. [Setup](#setup)
2. [Running the Application](#running-the-application)
3. [API Endpoints](#api-endpoints)
4. [Usage Examples](#usage-examples)

## Setup

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Setting up the Virtual Environment

1. Open a terminal and navigate to your project directory.

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install flask pandas openpyxl
   ```

## Running the Application

1. Ensure your virtual environment is activated.

2. Run the Flask application:
   ```
   python app.py
   ```

   The server should start running on `http://localhost:5000`.

## API Endpoints

- `GET /recipes`: Retrieve all recipes
- `GET /recipe/<dish_id>`: Retrieve a specific recipe
- `POST /recipe`: Create a new recipe
- `PUT /recipe/<dish_id>`: Update an existing recipe
- `DELETE /recipe/<dish_id>`: Delete a recipe
- `GET /doc`: Get the API documentation

## Usage Examples

Here are examples of how to use the API endpoints using curl:

### Get all recipes
```
curl -X GET http://localhost:5000/recipes
```

### Get a specific recipe
```
curl -X GET http://localhost:5000/recipe/1
```
Replace '1' with the desired dish_id.

### Create a new recipe
```
curl -X POST http://localhost:5000/recipe \
-H "Content-Type: application/json" \
-d '{
"dish_name": "Spaghetti Carbonara",
"description": "Classic Italian pasta dish",
"spice": "Mild",
"prep_time": "15 minutes",
"serves": 4,
"dietary_info": "Contains dairy, eggs",
"cook_time": "20 minutes",
"ingredients": "400g spaghetti, 200g pancetta, 4 eggs, 100g Pecorino cheese, Black pepper",
"instructions": "1. Cook pasta. 2. Fry pancetta. 3. Mix eggs and cheese. 4. Combine all ingredients.",
"image_url": "https://example.com/carbonara.jpg"
}'
```

### Update an existing recipe
```
curl -X PUT http://localhost:5000/recipe/1 \
-H "Content-Type: application/json" \
-d '{
"dish_name": "Spaghetti Carbonara Deluxe",
"description": "Upgraded classic Italian pasta dish",
"spice": "Medium",
"prep_time": "20 minutes"
}'
```
Replace '1' with the desired dish_id.

### Delete a recipe
```
curl -X DELETE http://localhost:5000/recipe/1
```
Replace '1' with the desired dish_id.

### Get the documentation
```
curl -X GET http://localhost:5000/doc
```

This will return the HTML documentation for the API.

## Note

This is a mock backend using an Excel file as a database. For production use, consider using a more robust database solution.
