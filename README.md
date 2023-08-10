# Weather Information Retrieval using requests Library - Read Me

Welcome to the Weather Information Retrieval project utilizing the `requests` library! This project serves as a practical demonstration of utilizing the `requests` library in Python to interact with external APIs and retrieve weather data from OpenWeatherMap. By following this guide, you will learn how to set up your API key, retrieve weather information for a specific city, and manage the API response using the `requests` library.

## Project Overview

The provided code exemplifies how to use the `requests` library to fetch weather information for a specified city from the OpenWeatherMap API. The main components of this project include:

### API Key Setup

Before executing the application, you must acquire an API key from OpenWeatherMap. Replace `'Enter API Key Here'` with your actual API key in the code.

### Function Definition

The `get_weather(city_name)` function is defined to initiate an API request to OpenWeatherMap using the provided city name and API key. This function encapsulates the API call and the subsequent JSON parsing process.

### API Request

The `requests.get()` method dispatches a GET request to the OpenWeatherMap API using the constructed URL. The API's response contains weather data in JSON format.

### JSON Parsing

The `response.json()` method decodes the JSON data from the API response into a Python dictionary (`data`). This facilitates the access and utilization of the weather information.

### Display Weather Information

The code evaluates the API response code (`cod`) to ascertain whether the city was located (`cod == 200`). If the city is found, the weather description, temperature, and humidity are extracted from the JSON response and presented to the user.

## How to Run the Application

### Obtain an API Key

Sign up on the OpenWeatherMap website to obtain an API key. Replace `'Enter API Key Here'` with your actual API key in the `API_KEY` variable.

### Run the Application

Execute the Python script in a terminal or command prompt. You will be prompted to input a city name. After supplying the city name, the application will retrieve and display the current weather details using the OpenWeatherMap API.

## Learning Outcomes

By engaging with this project, you will accomplish the following learning outcomes:

- **API Key Integration:** Learn the process of securely incorporating an API key into your Python code to authenticate API requests.

- **HTTP Requests:** Gain practical experience in crafting HTTP GET requests to external APIs utilizing the `requests` library.

- **JSON Handling:** Grasp the concept of parsing JSON data from API responses and extracting pertinent information for further manipulation.

- **Function Usage:** Understand the significance of defining and employing functions to encapsulate and structure code functionality.

- **User Interaction:** Discover the methodology of interacting with users by gathering input and providing output within a command-line environment.

- **Conditional Statements:** Develop skills in implementing conditional statements to make informed decisions based on API response data.

- **Data Display:** Acquire knowledge in formatting and presenting retrieved data in a user-friendly manner using print statements and string formatting. This experience is beneficial for integration and web application development.
