# 🌤️ Basic Weather App

## 📌 Project Overview

The Basic Weather App is a Python-based command-line application developed as part of the **OIBSIP Python Internship**.

This application allows users to enter a city name and fetch real-time weather information using the **OpenWeatherMap API**. The application receives weather data in JSON format, processes it, and displays important weather details in a simple and user-friendly way.

This project demonstrates Python concepts such as API integration, JSON data handling, user input validation, and exception handling.

---

## 🎯 Objective

The objective of this project is to develop a simple weather application that provides real-time weather information for a user-specified location.

The application focuses on:

- Fetching live weather data using an API
- Processing JSON responses
- Displaying accurate weather information
- Handling errors efficiently
- Improving practical Python programming skills

---

## ✨ Features

### 🌍 User Input

- User can enter any city name.
- Empty input validation is implemented.

### 🌡️ Weather Details Displayed

The application displays:

- City name
- Temperature in Celsius (°C)
- Temperature in Fahrenheit (°F)
- Humidity percentage
- Weather condition description
- Wind speed

### ⚠️ Error Handling

The application handles:

- Invalid city name
- Invalid API key
- Network connection errors
- Request timeout errors
- Empty user input

---

## 🛠️ Technologies Used

- Python
- Requests Library
- JSON
- OpenWeatherMap API

---

## 📂 Project Structure

```
Task4-BasicWeatherApp
│
├── main.py
│   └── Contains the main Python code for weather data fetching and display
│
├── requirements.txt
│   └── Contains required Python packages
│
├── README.md
│   └── Contains project documentation
│
└── screenshots
    └── output.png
        └── Application execution output screenshot
```

---

## ⚙️ Installation

Follow these steps to run the project:

### Step 1: Install Required Packages

Run the command:

```
pip install -r requirements.txt
```

### Step 2: API Configuration

This project uses the OpenWeatherMap API.

Steps to configure:

1. Create an account on OpenWeatherMap.
2. Generate an API key.
3. Replace the API key in `main.py`.

Example:

```
API_KEY = "your_api_key_here"
```

---

## ▶️ How to Run

Run the application using:

```
python main.py
```

Enter the city name when prompted.

Example:

```
Enter city name: Hyderabad
```

The application will fetch and display the current weather details.

---

## 📸 Output

After successful execution, the application displays real-time weather information.

Example Output:

```
========== WEATHER REPORT ==========

City: Hyderabad

Temperature: 29 °C

Temperature: 84.20 °F

Humidity: 65%

Weather Condition: Clear Sky

Wind Speed: 3.5 m/s

====================================
```

Output screenshot is available in:

```
screenshots/output.png
```

---

## 📚 Learning Outcomes

By completing this project, I learned:

- How to integrate external APIs with Python
- How to send HTTP requests using the Requests library
- How to handle JSON responses
- How to implement exception handling
- How to validate user input
- How to manage projects using Git and GitHub

---

## 🚀 Future Enhancements

Future improvements include:

- Developing a GUI version using Tkinter
- Adding weather icons
- Adding hourly weather forecast
- Adding daily weather forecast
- Adding automatic location detection
- Adding Celsius/Fahrenheit toggle option

---

## 👨‍💻 Author

**Your Full Name**

Python Intern  
OIBSIP Internship

---

## 📅 Project Status

Completed ✅