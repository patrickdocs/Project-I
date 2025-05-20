from colorama import Fore, Style
from datetime import date
import random
import sqlite3
from description import descriptions
from prediction import getZodiacSign, getPrediction, createUser, getUserByBirthdate, saveLookupHistory, getLookupHistory

DATABASE_NAME = 'zodiac.db'

def init_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    zodiac_data = [
        ('Bạch Dương', 3, 21, 4, 19),
        ('Kim Ngưu', 4, 20, 5, 20),
        ('Song Tử', 5, 21, 6, 20),
        ('Cự Giải', 6, 21, 7, 22),
        ('Sư Tử', 7, 23, 8, 22),
        ('Xử Nữ', 8, 23, 9, 22),
        ('Thiên Bình', 9, 23, 10, 22),
        ('Bọ Cạp', 10, 23, 11, 21),
        ('Nhân Mã', 11, 22, 12, 21),
        ('Ma Kết', 12, 22, 1, 19),
        ('Bảo Bình', 1, 20, 2, 18),
        ('Song Ngư', 2, 19, 3, 20)
    ]

    # Bảng thông tin cung hoàng đạo
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS zodiac_info (
            name TEXT PRIMARY KEY,
            start_month INTEGER NOT NULL,
            start_day INTEGER NOT NULL,
            end_month INTEGER NOT NULL,
            end_day INTEGER NOT NULL
        )
    ''')
    cursor.executemany("INSERT OR IGNORE INTO zodiac_info VALUES (?, ?, ?, ?, ?)", zodiac_data)

    # Bảng dự đoán
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            zodiac_sign TEXT PRIMARY KEY,
            prediction TEXT NOT NULL
        )
    ''')
    try:
        from prediction import get_all_predictions
        predictions_data = get_all_predictions().items()
        prediction_list = [(sign, ' '.join(preds)) for sign, preds in predictions_data]
        cursor.executemany("INSERT OR IGNORE INTO predictions VALUES (?, ?)", prediction_list)
    except ImportError:
        print(Fore.YELLOW + "Cảnh báo: Không tìm thấy hàm get_all_predictions trong prediction.py. Bảng predictions sẽ trống.")

    # Bảng mô tả
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS descriptions (
            zodiac_sign TEXT PRIMARY KEY,
            description TEXT NOT NULL
        )
    ''')
    cursor.executemany("INSERT OR IGNORE INTO descriptions VALUES (?, ?)", descriptions.items())

    # Bảng người dùng
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            birth_day INTEGER NOT NULL,
            birth_month INTEGER NOT NULL,
            zodiac_sign TEXT NOT NULL
        )
    ''')

    # Bảng lịch sử tra cứu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            history_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            lookup_date TEXT NOT NULL,
            zodiac_sign TEXT NOT NULL,
            prediction TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')

    # Tạo index để tăng hiệu suất truy vấn
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_birthdate ON users (birth_month, birth_day)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_history_userid ON history (user_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_history_lookupdate ON history (lookup_date)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_history_zodiac ON history (zodiac_sign)")

    conn.commit()
    conn.close()

def generate_lucky_number(zodiac_sign):
    """Tạo một số may mắn dựa trên cung hoàng đạo."""
    base_number = random.randint(1, 5)
    length_factor = len(zodiac_sign)
    initial = base_number + length_factor + random.randint(0, 20)

    lucky_number = (initial % 15) + 1       # Do tôi chỉ muốn số từ 1 - 15
    return lucky_number

def display_main_menu():
    print(Fore.CYAN + Style.BRIGHT + "\n--- Ứng Dụng Tra cứu Cung Hoàng Đạo ---")
    print(Fore.WHITE + "1. Xem mô tả cung hoàng đạo")
    print("2. Xem tử vi hôm nay")
    print("3. Xem lịch sử tra cứu")
    print("4. Thoát")
    print(Fore.CYAN + Style.BRIGHT + "--------------------------")
    choice = input("Chọn chức năng (1-4): ")
    return choice

def main():
    init_database()
    user_info = None  # Lưu thông tin người dùng (user_id, name, zodiac)

    print(Fore.WHITE + "Chào mừng bạn đến với ứng dụng Tra cứu Cung Hoàng Đạo!")
    user_name = input("Nhập họ tên của bạn: ")
    while True:
        try:
            day_of_birth = int(input("Nhập ngày sinh (1-31): "))
            month_of_birth = int(input("Nhập tháng sinh (1-12): "))
            if not 1 <= month_of_birth <= 12 or not 1 <= day_of_birth <= 31:
                raise ValueError("Ngày hoặc tháng sinh không hợp lệ.")
            break
        except ValueError as e:
            print(Fore.RED + f"Lỗi: {e}")

    with sqlite3.connect(DATABASE_NAME) as conn:
        zodiacSign = getZodiacSign(conn, day_of_birth, month_of_birth)
        if not zodiacSign:
            print(Fore.RED + "Không thể xác định cung hoàng đạo.")
            return

        user = getUserByBirthdate(conn, day_of_birth, month_of_birth)
        user_id = None
        if not user:
            user_id = createUser(conn, day_of_birth, month_of_birth, zodiacSign, user_name)
            print(Fore.YELLOW + f"Chào {user_name}!")
        else:
            user_id, stored_name, stored_zodiac = user
            print(Fore.YELLOW + f"Chào {user_name} trở lại!")

        user_info = (user_id, user_name, zodiacSign)

        while True:
            choice = display_main_menu()

            if choice == '1':
                print(Fore.BLUE + f"\n--- Mô tả cung hoàng đạo ---")
                description = descriptions.get(user_info[2], "Không có mô tả.")
                print(Fore.BLUE + f"{description}")
                print(Fore.BLUE + "--------------------------")
            elif choice == '2':
                print(Fore.MAGENTA + Style.BRIGHT + "\n--- Tử vi hôm nay ---")
                print(Fore.BLUE + f"Cung hoàng đạo: {user_info[2]}")
                prediction = getPrediction(conn, user_info[2])
                print(Fore.BLUE + f"Dự đoán: {(prediction if prediction else 'Không có dự đoán.')}")
                lucky_number = generate_lucky_number(user_info[2])
                print(Fore.GREEN + f"Số may mắn: {lucky_number}")
                print(Fore.MAGENTA + Style.BRIGHT + "-----------------------")
                if user_info[0] and prediction:
                    saveLookupHistory(conn, user_info[0], user_info[2], prediction)
            elif choice == '3':
                history = getLookupHistory(conn, user_info[0])
                if history:
                    print(Fore.CYAN + "\n--- Lịch sử tra cứu ---")
                    for item in history:
                        print(Fore.CYAN + f"- Ngày: {item[0]}, Cung: {item[1]}, Dự đoán: {item[2]}")
                    print(Fore.CYAN + "-----------------------")
                else:
                    print(Fore.CYAN + "\nLịch sử tra cứu trống.")
            elif choice == '4':
                print(Fore.WHITE + "Cảm ơn bạn đã sử dụng ứng dụng!")
                break
            else:
                print(Fore.RED + "Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
