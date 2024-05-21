import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

# Get the file path from command line arguments
file_path = sys.argv[1] if len(sys.argv) > 1 else exit("File path not provided")

# Convert relative path to absolute path
absolute_path = os.path.abspath(file_path)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get(f"file:///{absolute_path}")

# Get the size of the webpage
total_width = driver.execute_script("return Math.max( document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth ) +400;")
total_height = driver.execute_script("return document.body.parentNode.scrollHeight")

# Set the window size to the size of the webpage
driver.set_window_size(total_width, total_height)

# Then take screenshot
driver.save_screenshot("output.png")
driver.quit()