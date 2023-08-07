Weather Console Application using OpenWeather API
This project is a simple weather console application built using Python and the OpenWeatherMap API. By developing this application, you will have learned several fundamental Python concepts and gained practical experience in working with external APIs and handling JSON data.

Python Concepts Learned:
Importing Modules:
The import requests statement at the beginning of the code demonstrates how to import external modules in Python. The requests module is used to make HTTP requests to the OpenWeatherMap API.

Variables and String Formatting:
Throughout the code, you'll encounter the use of variables to store data such as the API key, base URL, city name, weather description, temperature, and humidity. The f-string formatting method is used to seamlessly integrate variables into strings.

User Input:
The input() function is used to collect user input for the city name. This showcases how to interact with users within a command-line environment.

Function Definition and Usage:
The get_weather(city_name) function is defined to make a request to the OpenWeatherMap API using the provided city name and API key. This function encapsulates the API call and JSON parsing.

HTTP Requests:
The requests.get() method is utilized to send a GET request to the OpenWeatherMap API. The response received contains weather data in JSON format.

JSON Parsing:
The response.json() method is used to parse the JSON data from the API response into a Python dictionary. This demonstrates how to work with JSON data in Python.

Conditional Statements:
A conditional statement (if weather_data['cod'] == 200) is used to check if the API response indicates a successful retrieval of weather data. Depending on the result, the program either displays weather information or informs the user that the city was not found.

Accessing Dictionary Values:
The code accesses specific values within the nested dictionaries of the JSON response. For example, weather_data['weather'][0]['description'] retrieves the weather description.

Formatted Output:
The program uses print() statements to display weather information in a user-friendly format. This involves string concatenation and formatting using variables.

How to Run the Application:
Obtain an API Key:
Before running the application, sign up on the OpenWeatherMap website and obtain an API key. Replace 'Enter API Key Here' with your actual API key in the API_KEY variable.

Run the Application:
Run the Python script in a terminal or command prompt. You will be prompted to enter the name of a city. After entering the city name, the application will fetch and display the current weather details using the OpenWeatherMap API.

Learning Outcome:
By working on this project, you will have gained a solid understanding of using Python to interact with external APIs, make HTTP requests, and parse JSON data. Additionally, you'll have honed your skills in variables, user input, conditional statements, and formatted output. This project serves as a practical introduction to real-world data retrieval and manipulation within a simple command-line application.
