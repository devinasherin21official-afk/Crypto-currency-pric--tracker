from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

while True:
    driver = webdriver.Edge()

    driver.get("https://coinmarketcap.com/")
    time.sleep(5)

    rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")

    crypto_data = []

    for row in rows[1:11]:
        data = row.text.split("\n")

        if len(data) >= 5:
            rank = data[0]
            name = data[1]
            symbol = data[2]
            price = data[4]

            crypto_data.append([rank, name, symbol, price])

    driver.quit()

    df = pd.DataFrame(
        crypto_data,
        columns=["Rank", "Name", "Symbol", "Price"]
    )

    df.to_csv("crypto_prices.csv", index=False)

    print("Updated at:", time.strftime("%H:%M:%S"))

    time.sleep(60)  # Wait 60 seconds