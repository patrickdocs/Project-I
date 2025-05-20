# Ứng dụng Xem Tử Vi Dòng Lệnh

Một ứng dụng đơn giản cho phép bạn xem cung hoàng đạo, mô tả tính cách và dự đoán tử vi dựa trên ngày sinh. Dữ liệu người dùng và lịch sử tra cứu được lưu trữ bằng SQLite.

## Cài đặt

1.  Cài đặt Python 3.x.
2.  Cài đặt các thư viện cần thiết:
    ```bash
    pip install -r requirements.txt
    ```
3.  Chạy ứng dụng:
    ```bash
    python project.py
    ```

## Hướng dẫn sử dụng

Khi chạy ứng dụng, bạn sẽ thấy một menu các chức năng. Hãy chọn số tương ứng để thực hiện:

1.  **Xem cung hoàng đạo và thông tin:** Nhập ngày và tháng sinh của bạn để xem cung hoàng đạo và mô tả tính cách. Thông tin người dùng và lịch sử tra cứu sẽ được lưu lại.
2. **Xem tử vi hôm nay:** Xem dự đoán tử vi và số may mắn của bạn trong hôm nay (dựa trên ngày sinh đã nhập trước đó).
3.  **Xem lịch sử tra cứu:** Xem lại lịch sử các lần xem tử vi trước đó của bạn (dựa trên ngày sinh đã nhập trước đó).
4.  **Thoát:** Đóng ứng dụng.

## Cấu trúc dự án
Zodiac_Generator/
├── project.py
├── description.py
├── prediction.py
├── test_project.py
├── requirements.txt
├── README.md
└── zodiac.db


## Đóng góp

Bạn có thể đóng góp vào dự án này bằng cách... (thêm thông tin
