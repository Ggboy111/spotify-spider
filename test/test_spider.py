from spider import spider


if __name__ == '__main__':
    username = "tpfztad@163.com"
    password = "111222333"
    link = "https://www.spotify.com/us/family/join/invite/3cYb0xYyA7x95b1/"  # 这个链接满了

    s = spider.Spider()

    code = s.get_website()
    if code == "1":
        code = s.login(username, password)
        if code == "1":
            code = s.check_country()
            if code == "1":
                code = s.open_other_link(link)
    s.close()
    print(code)
