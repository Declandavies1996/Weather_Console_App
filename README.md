# Weather Information Retrieval using `requests` Library - Read Me

Welcome to the Weather Information Retrieval project utilizing the `requests` library! This project provides a practical demonstration of using the `requests` library in Python to interact with external APIs and retrieve weather data from OpenWeatherMap. By following this guide, you'll learn how to set up your API key, retrieve weather information for a specific city, and handle the API response using the `requests` library.

## Project Overview

The provided code demonstrates how to use the `requests` library to fetch weather information for a given city from the OpenWeatherMap API. The main components of this project include:

1. **API Key Setup**: Before running the application, you'll need to obtain an API key from OpenWeatherMap and replace `'Enter API Key Here'` with your actual API key in the code.

2. **Function Definition**: The `get_weather(city_name)` function is defined to make an API request to OpenWeatherMap using the provided city name and API key. This function encapsulates the API call and JSON parsing process.

3. **API Request**: The `requests.get()` method sends a GET request to the OpenWeatherMap API using the constructed URL. The API response contains weather data in JSON format.

4. **JSON Parsing**: The `response.json()` method parses the JSON data from the API response into a Python dictionary (`data`). This allows you to access and utilize the weather information.

5. **Display Weather Information**: The code checks the API response code (`cod`) to determine if the city was found (`cod == 200`). If found, the weather description, temperature, and humidity are extracted from the JSON response and displayed to the user.

## How to Run the Application

1. **Obtain an API Key**: Sign up on the OpenWeatherMap website to acquire an API key. Replace `'Enter API Key Here'` with your actual API key in the `API_KEY` variable.

2. **Run the Application**: Execute the Python script in a terminal or command prompt. You'll be prompted to enter the name of a city. After providing the city name, the application will fetch and display the current weather details using the OpenWeatherMap API.

## Learning Outcomes

By engaging with this project, you'll achieve the following learning outcomes:

- **API Key Integration**: Learn how to securely integrate an API key into your Python code to authenticate API requests.

- **HTTP Requests**: Gain hands-on experience making HTTP GET requests to external APIs using the `requests` library.

- **JSON Handling**: Understand how to parse JSON data from API responses and extract relevant information for further processing.

- **Function Usage**: Learn the importance of function definition and usage to encapsulate and modularize code functionality.

- **User Interaction**: Discover how to interact with users by collecting input and providing output within a command-line environment.

- **Conditional Statements**: Develop skills in implementing conditional statements to make decisions based on API response data.

- **Data Display**: Learn how to format and display retrieved data in a user-friendly manner using print statements and string formatting.

## Next Steps

Upon completing this project, you'll be well-equipped to explore more advanced projects and concepts related to API integration, data manipulation, and building interactive applications using Python. Consider expanding your knowledge by working on projects that involve data visualization, database integration, and web application development. Happy coding!
