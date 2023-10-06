## weather-data-fetcher
Weather Data Fetcher is a Python-based project that enables users to retrieve weather information for specific dates through a user-friendly command-line interface (CLI). The project consists of two primary components:  Flask API (app.py) and CLI Program (cli_program.py) 

Flask API (app.py): A straightforward Flask web application serving weather data in JSON format. The API provides endpoints to access temperature, wind speed, and pressure data for user-specified dates.

CLI Program (cli_program.py): The command-line tool allows users to interact with the Flask API seamlessly. Users can choose to fetch and display temperature, wind speed, or pressure data by providing a desired date.

This project showcases how to efficiently retrieve data from an external API using Python's requests library and present the data through a convenient CLI interface. The Weather Data Fetcher can be used as a foundation to build upon more advanced weather-related functionalities in various applications.

## Key features

Data Retrieval: The project demonstrates efficient data retrieval from an external API, leveraging Python's requests library.

Flask API: The Flask API follows a RESTful architecture, making it easy to integrate with various applications or services.

CLI Interface: The CLI program offers a user-friendly way to interact with the weather data, making it accessible to both developers and non-developers.

## Usage
To use the Weather Data Fetcher:

1. Clone the repository: git clone https://github.com/nirajccs1999/weather_data_fetcher.git
2. Navigate to the project directory: cd weather_data_fetcher
3. Run the Flask API: python app.py
4. In a separate terminal, use the CLI program to fetch weather data: python cli_program.py

## Results

<img width="960" alt="cli_get-weather" src="https://github.com/nirajccs1999/weather-data-fetcher/assets/121447767/b2e1ecd8-0e76-4907-83bf-02d8624fc655">
<img width="960" alt="cli_get-wind-pressure-wrong_date" src="https://github.com/nirajccs1999/weather-data-fetcher/assets/121447767/7a6e0b0c-4fa4-4230-ba01-9d1d2a4efbd9">
<img width="958" alt="post_get-pressure" src="https://github.com/nirajccs1999/weather-data-fetcher/assets/121447767/5ae08f77-f618-4979-8720-bd71d1ac8b4c">
<img width="958" alt="postman_get-Weather" src="https://github.com/nirajccs1999/weather-data-fetcher/assets/121447767/0c3290a6-f757-4e0d-bd93-da84e0a3e31d">
<img width="960" alt="postman_get-wind-speed" src="https://github.com/nirajccs1999/weather-data-fetcher/assets/121447767/8ab5f7e5-57be-42f6-a952-21f9b05962fa">
