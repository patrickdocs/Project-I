# Ứng Dụng Tra Cứu Cung Hoàng Đạo

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌟 Giới Thiệu

**Ứng Dụng "Tra Cứu Cung Hoàng Đạo"** là một công cụ đơn giản nhưng hữu ích, được phát triển trên giao diện dòng lệnh (CLI). Ứng dụng này cho phép bạn dễ dàng khám phá cung hoàng đạo của mình, tìm hiểu về mô tả tính cách đặc trưng, và xem dự đoán tử vi hàng ngày dựa trên ngày sinh. Mọi thông tin cá nhân (họ tên, ngày sinh) và lịch sử tra cứu đều được lưu trữ cục bộ một cách an toàn bằng cơ sở dữ liệu **SQLite**, mang lại trải nghiệm cá nhân hóa và tiện lợi.

---

## ✨ Tính Năng Chính

* **Xác định Cung Hoàng Đạo:** Tự động xác định cung hoàng đạo của bạn chỉ với ngày và tháng sinh.
* **Mô tả Tính Cách:** Cung cấp thông tin chi tiết về đặc điểm tính cách và sở trường của cung hoàng đạo bạn.
* **Tử Vi Hôm Nay:** Xem dự đoán tử vi hàng ngày và một số may mắn được tạo ngẫu nhiên.
* **Lịch Sử Tra Cứu:** Xem lại tất cả các lần bạn đã tra cứu tử vi trước đó.
* **Quản Lý Người Dùng:** Lưu trữ thông tin người dùng và nhận diện người dùng cũ để cá nhân hóa trải nghiệm.
* **Giao Diện Thân Thiện:** Sử dụng màu sắc để làm nổi bật thông tin, giúp giao diện dòng lệnh dễ đọc và trực quan hơn.

---

## 🚀 Cài Đặt

Để chạy ứng dụng, bạn cần cài đặt **Python 3.x** và các thư viện cần thiết.

1.  **Cài đặt Python 3.x:**
    Nếu bạn chưa có Python, hãy tải xuống và cài đặt phiên bản Python 3.x từ trang web chính thức: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2.  **Tải mã nguồn:**
    Clone repository này về máy tính của bạn hoặc tải xuống dưới dạng file ZIP.
    ```bash
    git clone [https://github.com/your-username/Zodiac_Generator.git](https://github.com/your-username/Zodiac_Generator.git)
    cd Zodiac_Generator
    ```
    *(Thay `your-username` bằng tên người dùng GitHub của bạn)*

3.  **Cài đặt các thư viện phụ thuộc:**
    Ứng dụng sử dụng các thư viện Python bên ngoài. Cài đặt chúng dễ dàng bằng cách chạy lệnh sau trong thư mục gốc của dự án:
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Cách Chạy Ứng Dụng

Sau khi cài đặt thành công, bạn có thể khởi động ứng dụng bằng lệnh:

```bash
python project.py
---
```
## 📖 Hướng Dẫn Sử Dụng

Khi ứng dụng khởi chạy, bạn sẽ được chào mừng và yêu cầu nhập thông tin cá nhân. Sau đó, một menu chính sẽ xuất hiện với các tùy chọn:

1.  **Xem cung hoàng đạo và thông tin:**
    * Nhập ngày và tháng sinh của bạn.
    * Ứng dụng sẽ xác định cung hoàng đạo và hiển thị mô tả tính cách chi tiết.
    * Thông tin người dùng của bạn sẽ được lưu trữ và nhận diện cho những lần sử dụng sau.

2.  **Xem tử vi hôm nay:**
    * Xem dự đoán tử vi và số may mắn của bạn cho ngày hôm nay (dựa trên cung hoàng đạo đã xác định).
    * Kết quả tra cứu sẽ được tự động lưu vào lịch sử của bạn.

3.  **Xem lịch sử tra cứu:**
    * Xem lại danh sách tất cả các lần bạn đã tra cứu tử vi trước đó, bao gồm ngày tra cứu và dự đoán.

4.  **Thoát:**
    * Đóng ứng dụng.

---

## 📁 Cấu trúc thư mục dự án

```
Zodiac_Generator/
├── project.py             # Tệp chính của ứng dụng, xử lý giao diện và luồng điều khiển
├── description.py         # Chứa logic để truy xuất và hiển thị mô tả cung hoàng đạo
├── prediction.py          # Chứa logic để truy xuất và tạo dự đoán tử vi
├── test_project.py        # Các bài kiểm thử đơn vị (unit tests) cho các chức năng chính
├── requirements.txt       # Danh sách các thư viện Python cần thiết
├── README.md              # Tệp mô tả dự án này
└── zodiac.db              # Cơ sở dữ liệu SQLite (sẽ được tạo tự động khi chạy lần đầu)
```

---

## 🤝 Đóng Góp

Mọi đóng góp để cải thiện ứng dụng đều được chào đón! Nếu bạn có ý tưởng hoặc phát hiện lỗi, hãy:

1.  Fork repository này.
2.  Tạo một nhánh mới (`git checkout -b feature/AmazingFeature`).
3.  Thực hiện các thay đổi của bạn.
4.  Commit các thay đổi (`git commit -m 'Add some AmazingFeature'`).
5.  Push lên nhánh (`git push origin feature/AmazingFeature`).
6.  Mở một Pull Request.
