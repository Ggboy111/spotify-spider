from spider import spider


if __name__ == '__main__':
    username = "111"
    password = "123456"
    link = "https://www.spotify.com/us/family/join/invite/CbaABy24B7c1ZB6/"  # 这个链接满了

    code = int()

    s = spider.Spider()
    try:
        code = s.get_website()
    except Exception as e:
        print(e)
        print(code)

    try:
        code = s.login(username, password)
    except Exception as e:
        print(e)
        print(code)

    try:
        code = s.check_country()
    except Exception as e:
        print(e)
        print(code)

    try:
        code = s.open_other_link(link)
    except Exception as e:
        print(e)
        print(code)

    try:
        code = s.close()
    except Exception as e:
        print(e)
        print(code)

    # s.close()
    # print(driver)