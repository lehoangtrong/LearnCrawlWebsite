from bs4 import BeautifulSoup
from re import findall
from progressbar import progressbar

import requests
import xlsxwriter

path_db = open('./config.txt', 'r').read()

workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()

url = "https://hocvalamtheobac.vn/ket-qua-thi-sinh"
login_url = 'https://hocvalamtheobac.vn/login'


def login(user, passw, row_count):
    payload = {
    '_token': '',
    'username': 'username',
    'password': 'password'
    }
    s = requests.Session()
    r = s.get(url=login_url).text
    token = findall(r'"\S{40}"', r)[0].strip('"')
    payload['_token'] = token
    payload['username'] = user
    payload['password'] = passw
    response = s.post(url=login_url, data=payload).text
    if response.find("Đăng nhập") != -1:
        return 0
    page_source = s.get(url=url)
    page_source = BeautifulSoup(page_source.text, 'lxml')
    name = page_source.select(".col-lg-4.col-md-6.col-xs-12 p strong")[0].text.title()
    worksheet.write('A' + str(row_count), name)

    # get table
    rows = page_source.find("tbody").find_all("tr")
    maxOfWeek = {}
    for row in rows:
        cells = row.find_all("td")
        try:
            weekStr = int(cells[2].text.split()[-1])
            score = int(cells[4].text)
            time = str(cells[5].text)
            if maxOfWeek.__contains__(weekStr):
                if maxOfWeek[weekStr][0] <= score:
                    if maxOfWeek[weekStr][0] == score:
                        if maxOfWeek[weekStr][1] >= time:
                            maxOfWeek[weekStr] = (score, time)
                    else:
                        maxOfWeek[weekStr] = (score, time)
            else:
                maxOfWeek[weekStr] = (score, time)
        except:
            continue
    for j in range(len(maxOfWeek)):
        for i in range(4):
            worksheet.write(chr(ord('B') + i * 2) + str(row_count), maxOfWeek[i + 1][0])
            worksheet.write(chr(ord('B') + i * 2 + 1) + str(row_count), maxOfWeek[i + 1][1])
    return 1


worksheet.write('A1', 'Tên')
column_count = 0
for i in range(1, 5):
    worksheet.write(chr(ord('B') + column_count) + "1", 'Điểm tuần ' + str(i))
    worksheet.write(chr(ord('B') + (column_count + 1)) + "1", 'Thời gian tuần ' + str(i))
    column_count += 2

f = open(path_db)
contents = f.readlines()

row_count = 2
people = 0
for i in progressbar(range(0, len(contents), 2)):
    result = login(contents[i].strip(), contents[i + 1].strip(), row_count)
    row_count += result
    people += result

print(f'Finished crawled {people} people')
print(f'There are {int(len(contents)/2) - people} wrong accounts')
print("Good day!")
f.close()
workbook.close()