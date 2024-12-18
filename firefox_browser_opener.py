import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Load the CSV file containing titles and URLs
file_path = 'Key_Contributions_with_URLs.csv'  # Update with the correct path if needed
try:
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(file_path)
except FileNotFoundError:
    # Raise an error if the file is not found
    raise FileNotFoundError(f"The file '{file_path}' was not found. Ensure it is in the correct location.")
except pd.errors.EmptyDataError:
    # Raise an error if the file is empty
    raise ValueError(f"The file '{file_path}' is empty. Please provide a valid CSV file.")
except pd.errors.ParserError:
    # Raise an error if the file is malformed
    raise ValueError(f"The file '{file_path}' is malformed and could not be parsed. Please check its format.")

# Check if required columns ('Title' and 'URL') are present in the CSV file
if not {'Title', 'URL'}.issubset(data.columns):
    raise ValueError("The CSV file must contain 'Title' and 'URL' columns.")

# Set up Firefox WebDriver
firefox_driver_path = "/Users/username/firefox_driver/geckodriver"  # Update with the actual path to geckodriver
options = Options()
options.add_argument("--start-maximized")  # Maximize the browser window on start

# Initialize the WebDriver service for Firefox
service = Service(firefox_driver_path)
driver = webdriver.Firefox(service=service, options=options)

# Iterate through each row in the DataFrame to open URLs
for index, row in data.iterrows():
    title = row['Title']  # Extract the title of the paper
    url = row['URL']  # Extract the URL of the paper
    try:
        print(f"Opening: {title} -> {url}")

        # Open a new tab in the browser
        driver.execute_script("window.open('about:blank', '_blank');")
        
        # Switch to the newly opened tab
        driver.switch_to.window(driver.window_handles[-1])
        
        # Navigate to the URL
        driver.get(url)

        # Optional: Wait for a few seconds to visually verify the page is loaded
        time.sleep(5)

    except Exception as e:
        # Log an error message if the URL cannot be opened
        print(f"Error opening {url}: {e}")

# # Close the browser after processing all URLs
# driver.quit()

print("Completed opening all URLs.")
