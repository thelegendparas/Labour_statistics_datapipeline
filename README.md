# Labour Statistics Data Pipeline

A personal project demonstrating a data pipeline to process and analyze labor statistics, providing insights into employment trends and job market dynamics. This project uses real-world data from the **United States Bureau of Labor Statistics API** for accurate and reliable information.

---

## 📂 Project Overview

This pipeline fetches, processes, and visualizes labor statistics using a variety of employment-related indicators. Users can select data for different **seasonal periods** and choose from multiple **keys representing different employment factors** such as job gains, losses, and net changes.

Additionally, the processed data can be **exported to Excel** and graphs can be **exported across different time series**, making it easy to share insights or integrate with other reporting tools.

The project was built as a demonstration of **data engineering, analysis, and visualization skills**, showcasing how raw labor data can be transformed into actionable insights.

---

## 📂 Project Structure

- **`main.ipynb`**: Jupyter Notebook containing the main workflow for data extraction, processing, and analysis.  
- **`api_test.py`**: Python script for testing API endpoints and fetching labor data.  
- **`time_series_data.csv`**: Raw time series labor statistics data downloaded from the API.  
- **`out.csv`**: Processed output data after cleaning and analysis.  
- **`QUARTERLY_GROSS_JOB_GAINS.png`**: Example visualization showing quarterly gross job gains.  
- **`.env`**: Environment variables storing API keys and configuration parameters.

---

## 🛠️ Technologies Used

- **Languages & Tools**: Python, Jupyter Notebook  
- **Data Analysis**: Pandas, NumPy  
- **Visualization**: Matplotlib  
- **API**: United States Bureau of Labor Statistics API  
- **Data Export**: Excel (via Pandas)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x  
- Time series insights  
- Recommended: Create a virtual environment  

### Installation

1. Clone the repository:

```bash
git clone https://github.com/thelegendparas/Labour_statistics_datapipeline.git
cd Labour_statistics_datapipeline
