from playwright.sync_api import sync_playwright
import os




def main():

     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://souhrada.github.io/playwright-exam/")
        page.fill('input#login','Jarmil')
        page.fill('input#pass', 'Admin123')
        page.click('button.login-btn') 

        secret = page.locator('p.super-secret-text').text_content()
        print(secret)
    

        page.wait_for_timeout(10000)
        browser.close()
    

if __name__ == "__main__":
    main()
