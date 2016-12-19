from selenium import webdriver
from time import sleep

driver = None
driver = webdriver.Firefox()

SENDER = '<SENDER NAME>'
GMAIL_USER = '<Your Gmail ID>'
GMAIL_PASSWORD = '<Your Gmail ID>'
MESSAGE = 'I will get back to you soon. \n Thanks'
MESSAGE = 'I will get back to you soon. \n Thanks'


def access_gmail():
    try:
        driver.get('http://gmail.com')
        sleep(5)
        # Go thru messages list
        m = driver.find_elements_by_css_selector('.UI table > tbody > tr')

        for a in m:
            if SENDER.lower() in a.text:
                a.click()
                break

        # take rest
        sleep(5)
        reply = driver.find_element_by_css_selector('.amn > span')
        sleep(5)
        if reply:
            reply.click()
            sleep(1)

            # Access editor to write response
            editable = driver.find_element_by_css_selector('.editable')
            if editable:
                editable.click()
                editable.send_keys(MESSAGE)

            send = driver.find_elements_by_xpath('//div[@role="button"]')
            for s in send:
                if s.text.strip() == 'Send':
                    s.click()

    except Exception as ex:
        print(str(ex))
    finally:
        return True


def login_google():
    is_logged_in = False
    google_login = 'https://accounts.google.com/Login#identifier'

    try:
        driver.get(google_login)
        sleep(5)
        html = driver.page_source.strip()

        # email box
        user_name = driver.find_element_by_id('Email')
        if user_name:
            user_name.send_keys(GMAIL_USER)

        next = driver.find_element_by_id('next')
        if next:
            next.click()

        # give em rest
        sleep(5)

        # now enter passwd
        user_pass = driver.find_element_by_id('Passwd')
        if user_pass:
            user_pass.send_keys(GMAIL_PASSWORD)

        # rest again
        sleep(3)

        sign_in = driver.find_element_by_id('signIn')
        if sign_in:
            sign_in.click()

        # rest again
        sleep(3)
        is_logged_in = True

    except Exception as ex:
        print(str(ex))
        is_logged_in = False
    finally:
        return is_logged_in


if __name__ == '__main__':
    r_log = login_google()
    if r_log:
        print('Yay')
        access_gmail()
    else:
        print('Boo!!!')

    if driver is not None:
        driver.quit()

    print('Done')
