# Python libraries
from fpdf import FPDF
from datetime import datetime, timedelta
import os

# Local libraries
from time_series_analysis import plot_states, plot_countries
from daily_counts import plot_daily_count_states, plot_daily_count_countries
#from create_case_maps import plot_usa_case_map, plot_global_case_map
from helper import Mode

WIDTH = 210
HEIGHT = 297

TEST_DATE = "10/20/20"

def create_title(day, pdf):
  # Unicode is not yet supported in the py3k version; use windows-1252 standard font
  pdf.set_font('Arial', '', 24)  
  pdf.ln(60)
  pdf.write(5, f"Covid Analytics Report")
  pdf.ln(10)
  pdf.set_font('Arial', '', 16)
  pdf.write(4, f'{day}')
  pdf.ln(5)

def create_analytics_report(day=TEST_DATE, filename="report_simple.pdf"):
  pdf = FPDF() # A4 (210 by 297 mm)

  states = ['New York', 'California', 'New Jersey', 'Texas', 'Alabama']

  ''' First Page '''
  pdf.add_page()
  pdf.image("./resources/letterhead.png", 0, 0, WIDTH)
  create_title(day, pdf)

  plot_daily_count_states(states, day=day, filename="./tmp/cases_day.png")
  plot_daily_count_states(states, day=day, mode=Mode.DEATHS, filename="./tmp/deaths_day.png")
  pdf.image("./tmp/cases_day.png", 5, 90, WIDTH/2-10)
  pdf.image("./tmp/deaths_day.png", WIDTH/2, 90, WIDTH/2-10)

  prev_days = 7
  plot_states(states, days=prev_days, filename="./tmp/cases2.png", end_date=day)
  plot_states(states, days=prev_days, mode=Mode.DEATHS, filename="./tmp/deaths2.png", end_date=day)
  pdf.image("./tmp/cases2.png", 5, 180, WIDTH/2-10)
  pdf.image("./tmp/deaths2.png", WIDTH/2, 180, WIDTH/2-10)

  ''' Second Page'''
  pdf.add_page()

  prev_days = 30
  plot_states(states, days=prev_days, filename="./tmp/cases3.png", end_date=day)
  plot_states(states, days=prev_days, mode=Mode.DEATHS, filename="./tmp/deaths3.png", end_date=day)
  pdf.image("./tmp/cases3.png", 5, 20, WIDTH/2-10)
  pdf.image("./tmp/deaths3.png", WIDTH/2, 20, WIDTH/2-10)

  prev_days = 90
  plot_states(states, days=prev_days, filename="./tmp/cases4.png", end_date=day)
  plot_states(states, days=prev_days, mode=Mode.DEATHS, filename="./tmp/deaths4.png", end_date=day)
  pdf.image("./tmp/cases4.png", 5, 110, WIDTH/2-10)
  pdf.image("./tmp/deaths4.png", WIDTH/2, 110, WIDTH/2-10)

  prev_days = 250
  plot_states(states, days=prev_days, filename="./tmp/cases5.png", end_date=day)
  plot_states(states, days=prev_days, mode=Mode.DEATHS, filename="./tmp/deaths5.png", end_date=day)
  pdf.image("./tmp/cases5.png", 5, 200, WIDTH/2-10)
  pdf.image("./tmp/deaths5.png", WIDTH/2, 200, WIDTH/2-10)

  '''Third Page'''
  pdf.add_page()
  pdf.write(3, f"Country Wise Analysis")
  countries = ['US', 'Pakistan', 'Vietnam', 'China', 'United Kingdom']

  plot_daily_count_countries(countries, day=day, filename="./tmp/cases_day_countries.png")
  plot_daily_count_countries(countries, day=day, mode=Mode.DEATHS, filename="./tmp/deaths_day_countries.png")
  pdf.image("./tmp/cases_day_countries.png", 5, 90, WIDTH/2-10)
  pdf.image("./tmp/deaths_day_countries.png", WIDTH/2, 90, WIDTH/2-10)

  prev_days = 7
  plot_countries(countries, days=prev_days, filename="./tmp/cases4_7.png", end_date=day)
  plot_countries(countries, days=prev_days, mode=Mode.DEATHS, filename="./tmp/deaths4_7.png", end_date=day)
  pdf.image("./tmp/cases4_7.png", 5, 180, WIDTH/2-10)
  pdf.image("./tmp/deaths4_7.png", WIDTH/2, 180, WIDTH/2-10)

  '''Fourth Page'''
  pdf.add_page()
  prev_days = 30
  plot_countries(countries, days=prev_days, filename="./tmp/cases4_30.png", end_date=day)
  plot_countries(countries, days=prev_days, mode=Mode.DEATHS, filename="./tmp/deaths4_30.png", end_date=day)
  pdf.image("./tmp/cases4_30.png", 5, 20, WIDTH/2-10)
  pdf.image("./tmp/deaths4_30.png", WIDTH/2, 20, WIDTH/2-10)

  prev_days=90
  plot_countries(countries, days=prev_days, filename="./tmp/cases4_90.png", end_date=day)
  plot_countries(countries, days=prev_days, mode=Mode.DEATHS, filename="./tmp/deaths4_90.png", end_date=day)
  pdf.image("./tmp/cases4_90.png", 5, 110, WIDTH/2-10)
  pdf.image("./tmp/deaths4_90.png", WIDTH/2, 110, WIDTH/2-10)

  prev_days = 250
  plot_countries(countries, days=prev_days, filename="./tmp/cases4_250.png", end_date=day)
  plot_countries(countries, days=prev_days, mode=Mode.DEATHS, filename=f"./tmp/deaths4_250.png", end_date=day)
  pdf.image("./tmp/cases4_250.png", 5, 200, WIDTH/2-10)
  pdf.image("./tmp/deaths4_250.png", WIDTH/2, 200, WIDTH/2-10)

  pdf.output(filename, 'F')


if __name__ == '__main__':
  yesterday = (datetime.today() - timedelta(days=2)).strftime("%m/%d/%y").replace("/0","/").lstrip("0")
  #yesterday = "10/10/20" # Uncomment line for testing
  
  create_analytics_report(day = yesterday)