import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

# 1. Define your download directory (Change this to your actual path)
download_dir = r"C:\Users\mdfai\Downloads\rdr2"

# Ensure the directory exists
os.makedirs(download_dir, exist_ok=True)

# 2. Setup Chrome options to automatically download to the specified folder
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False, # Don't ask where to save
    "directory_upgrade": True,
    "safebrowsing.enabled": True 
}
options.add_experimental_option("prefs", prefs)

# Initialize the browser
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

# list of URLs
urls = [

]
# How many files to download at once
batch_size = 5
# How long to wait for the batch to finish (in seconds). 4 minutes = 240 seconds.
wait_time_per_batch = 120

# This splits your long 'urls' list into chunks of 5
for i in range(0, len(urls), batch_size):
    current_batch = urls[i:i + batch_size]
    print(f"\n--- Starting new batch of {len(current_batch)} files ---")
    
    # Trigger the downloads for just these 5 links
    for url in current_batch:
        print(f"Visiting: {url}")
        driver.get(url)
        
        try:
            button_selector = ".link-button.text-5xl.gay-button"
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector)))
            main_window = driver.current_window_handle
            
            # --- FIRST CLICK ---
            try:
                button.click()
            except ElementClickInterceptedException:
                driver.execute_script("arguments[0].click();", button)
            
            time.sleep(2) # Let pop-up open
            
            # --- CLOSE POP-UP ---
            all_windows = driver.window_handles
            if len(all_windows) > 1:
                for window in all_windows:
                    if window != main_window:
                        driver.switch_to.window(window)
                        driver.close()
                driver.switch_to.window(main_window)
            
            # --- SECOND CLICK ---
            time.sleep(1) 
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector)))
            try:
                button.click()
            except ElementClickInterceptedException:
                driver.execute_script("arguments[0].click();", button)
                
            print(f"Download initiated.")
            time.sleep(3) # Brief pause so the browser registers the download before loading next URL
            
        except Exception as e:
            print(f"An error occurred with {url}: {e}")

    # After triggering 5 files, pause the entire script for 4 minutes
    print(f"\nBatch triggered. Sleeping for {wait_time_per_batch / 60} minutes to let them download...")
    print(f"Total time rem : {(len(urls)-i-1) * wait_time_per_batch/batch_size}")
    time.sleep(wait_time_per_batch) 

print("\nAll batches processed.")
input("Press Enter to close the browser...")
driver.quit()