# LearnCrawlWebsite
Tất cả chỉ để cào 1 trang web `hocvalamtheobac.vn`
## Hướng dẫn sử dụng
- Tải project này về máy, để đâu cũng được
  - Nếu có git thì:
    ```
    git clone https://github.com/lehoangtrong/LearnCrawlWebsite
    ```
  - Không thì ấn nút `Code` xanh xanh góc trên bên trái, rồi `Download as ZIP`
- Cài đặt Python 3 (và PIP 3) nếu chưa cài. Đảm bảo rằng Python đã được thêm vào PATH của máy, kiểm tra bằng cách chạy thử Python từ Console (cái màn hình đen đen nhiều chữ, trông ngầu như hacku ấy, trên Windows người ta gọi là Command Prompt hay `cmd`)
  - Windows: `python --version`
  - *nix (Linux, MacOS): `python3 --version`
  - Nếu hiện ra số phiên bản trông kiểu kiểu như sau thì đã cài thành công:
    ```
    > python3 --version
    Python 3.X.X
    ```
- Tạo file text chứa các tên người dùng và mật khẩu, tên người dùng trên một dòng và mật khẩu cho tên người dùng đó ở dòng mới ngay bên dưới. VD:
  ```
  nguyenvana1234
  passwordnguyenvana
  IAmHandsome
  passwordIAmHandsome
  ...
  ```
- Copy đường dẫn đến file vừa tạo và thay vào `<account file here>` trong file `config.txt`, nghĩa là dòng đầu tiên
- Trở lại Console, chuyển đến thư mục chứa project này bằng
  ```bash
  cd <đường dẫn đến thư mục chứa project>
  ```
- Cài đặt thư viện bằng PIP 3:
  - **Windows**: `python -m pip install -r requirements.txt`
  - ***nix**: `python3 -m pip install -r requirements.txt`
- Chạy chương trình bằng Python:
  - **Windows**: `python main.py`
  - ***nix**: `python3 main.py`
## Lưu ý
Mình chưa test thử trường hợp tên thư mục là tiếng Việt, có hệ lụy gì đừng bắt đền mình nhé *uwu*
## Thư viện sử dụng
- XlsxWriter 3.0.2
- BeautifulSoup 4.10.0
- lxml 4.6.4
- python-time 0.3.0
- requests 2.26.0
- progressbar2 3.55.0

## Credit
Coder Super Idol : `lehoangtrong` 😂
*Superman Squad*
