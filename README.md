#  Weather App (Python + Flask + OpenWeatherMap API)

A simple, clean weather application built with **Python**, **Flask**, and the **OpenWeatherMap API**.  
Users can enter any city and instantly view:

- ✔️ Current temperature  
- ✔️ Weather description + emoji icons  
- ✔️ Real-time weather alerts (if any)  
- ✔️ Clean web interface (HTML + CSS)  
- ✔️ Error handling for invalid cities  

This project demonstrates real-world API usage, backend development, and web integration — a strong portfolio piece for junior developers.

---

##  Features

###  **Current Weather**
- Temperature in Celsius  
- Description (e.g., "broken clouds")  
- Weather emoji icons  
- City name formatting  

###  **Weather Alerts**
Displays government-issued alerts (if available), including:
- Severe storms  
- Flood warnings  
- Extreme temperature alerts  

If no alert exists, shows:  
`No active alerts 🎉`

###  **Web Interface**
- Clean, simple input page  
- Dynamic results page  
- “Back” button navigation  

---

##  Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3** | Core logic & backend |
| **Flask** | Web framework |
| **OpenWeatherMap API** | Weather + alerts |
| **HTML/CSS** | Frontend templates |
| **Requests** | API calls |
| **Colorama (CLI version only)** | Terminal colors |

---

## Installation & Run
Prerequisites

Python 3.8+ installed
An OpenWeather API key (get one at https://openweathermap.org/
).
Do not commit your API key to the repo.

1. Clone the repository
git clone https://github.com/sharedee2776/Weather_app_project.git
cd Weather_app_project

2. (Optional but recommended) Create a virtual environment
-  Windows — Command Prompt

python -m venv venv
venv\Scripts\activate 

-  Windows — PowerShell

python -m venv venv
.\venv\Scripts\Activate.ps1

-  macOS / Linux

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

- If pip is not recognized:

python -m pip install -r requirements.txt

4. Add your API key 
-- Create a file named .env in the project root:

API_KEY=your_openweather_api_key_here

.env is ignored in .gitignore — safe for development.

5. Run the app

python app.py

You should see:

 * Running on http://127.0.0.1:5000
 * Debug mode: on

Open your browser and visit:

 http://127.0.0.1:5000/

 6. Test the app

Try cities like:

London

New York

Nairobi

https://weather-app-project-mswz.onrender.com

Contact;
damoladauda10@gmail.com







