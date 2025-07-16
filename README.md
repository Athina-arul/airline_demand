# airline_demand
# Airline Market Demand Dashboard

This project is a Python Flask-based web application that visualizes airline booking market demand trends. It processes airline data, analyzes popular routes, price trends, and demand by location, and presents insights in interactive charts.

---

## 🚀 Features

- Scrapes or loads airline data (using CSV as a placeholder).
- Processes data using Pandas.
- Visualizes:
  - Popular Routes (Bar Chart)
  - Price Trend Over Time (Line Chart)
  - Demand by Destination (Pie Chart)
- Simple and responsive web interface using Flask and Chart.js.

---

## 🛠️ Tech Stack

- Python
- Flask
- Pandas
- Requests / BeautifulSoup (for scraping)
- Chart.js (Frontend Visualization)
- Gunicorn (for production deployment)
📂 Project Structure

airline_demand/
├── app.py
├── requirements.txt
├── README.md
├── data/
│ └── sample_airline_data.csv
├── templates/
│ └── dashboard.html
