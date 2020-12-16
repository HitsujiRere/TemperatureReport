
import os
import sys
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

sys.path.append('/home/pi/.local/lib/python3.5/site-packages/')


def halfwidth_to_fullwidth(half_text: str):
    '''
    半角数字を全角数字に置換する

    Parameters
    ----------
    half_text : str
        対象の文字列

    Returns
    -------
    full_text : str
        置換された文字列
    '''

    halfwidths = '0123456789'
    fullwidths = '０１２３４５６７８９'
    half_to_full_dict = dict(zip(halfwidths, fullwidths))

    full_text = ''
    for ch in half_text:
        full_text += half_to_full_dict[ch]
    return full_text


def report(userid: str, password: str):
    '''
    検温報告を行う

    Parameters
    ----------
    userid : str
        ユーザID
    password : str
        パスワード

    Returns
    -------
    bool
        成功したかどうか
    e : Exception
        エラー内容（失敗時）
    '''

    try:
        driver = webdriver.Chrome(
            executable_path="/usr/lib/chromium-browser/chromedriver")

        driver.implicitly_wait(3)

        # ログインページを開く
        driver.get(os.environ.get('LOGIN_URL'))
        print(driver.current_url)

        # ログインする
        driver.find_element_by_id('username').send_keys(userid)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_id('LoginBtn').click()
        print(driver.current_url)

        # 検温報告ページ一覧を開く
        driver.get(os.environ.get('REPORTS_URL'))
        print(driver.current_url)

        # 今日の検温報告ページに移動する
        button_today_text = '検温報告（{}月{}日）'.format(
            halfwidth_to_fullwidth(str(datetime.today().month)),
            halfwidth_to_fullwidth(str(datetime.today().day))
        )
        driver.find_element_by_xpath(
            '//a[text()="{}"]'.format(button_today_text)
        ).click()
        print(driver.current_url)

        # 開始する
        driver.switch_to.frame('contentsInfo')
        time.sleep(1)
        driver.find_element_by_name('next').click()
        print(driver.current_url)

        # 終了する
        driver.find_element_by_id('GradeBtn').click()
        print(driver.current_url)
        driver.find_element_by_name('grade').click()
        print(driver.current_url)

    except Exception as e:
        print(e)
        return False, e

    driver.quit()
    return True
