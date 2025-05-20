import pytest
import random
import sqlite3
from project import get_zodiac_sign_from_db, get_prediction_from_db, create_user_in_db, get_user_by_birthdate_from_db, save_lookup_history_to_db, get_lookup_history_from_db, generate_lucky_number
from description import descriptions
from zodiac_info_data import zodiac_data

@pytest.fixture
def db_connection():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Tạo bảng zodiac_info
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

    # Tạo bảng predictions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            zodiac_sign TEXT PRIMARY KEY,
            prediction TEXT NOT NULL
        )
    ''')
    prediction_data = [
        ('Bạch Dương', 'Dành nhiều thời gian hơn cho mối quan hệ. Các nhiệm vụ chuyên môn có vẻ khó khăn nhưng bạn sẽ xử lý được.'),
        ('Kim Ngưu', 'Một mối quan hệ lãng mạn hạnh phúc đang chờ đợi bạn. Tận hưởng tình hình tài chính vững mạnh.'),
        ('Song Tử', 'Một chuyện tình cảm siêng năng là những gì tử vi dự đoán cho bạn. Đa nhiệm để hoàn thành mọi công việc trong thời hạn. Sức khỏe tài chính sẽ tốt trong ngày hôm nay.'),
        ('Cự Giải', 'Một đời sống tình cảm hạnh phúc được hỗ trợ bởi thành công trong công việc sẽ làm cho ngày của bạn tốt đẹp. Các vấn đề tài chính nhỏ sẽ tồn tại và hãy xử lý chúng một cách cẩn thận. Cũng nên kiểm tra sức khỏe.'),
        ('Sư Tử', 'Tránh xa các mối quan hệ độc hại trong ngày hôm nay. Thành công trong công việc sẽ ở bên bạn. Hãy vui vẻ vì cả tiền bạc và sức khỏe đều tốt suốt cả ngày.'),
        ('Xử Nữ', 'Bước vào mối quan hệ cũ trong ngày hôm nay. Tận dụng các cơ hội nghề nghiệp để phát triển. Đưa ra các quyết định tiền bạc thông minh & tận hưởng sức khỏe tốt.'),
        ('Thiên Bình', 'Giải quyết các vấn đề liên quan đến tình yêu bằng thái độ trưởng thành. Những thách thức chuyên môn sẽ tồn tại nhưng hãy đối phó với chúng. Cả tài chính và sức khỏe sẽ ở bên bạn trong ngày hôm nay. Hãy để mắt đến các cơ hội.'),
        ('Bọ Cạp', 'Một mối quan hệ lãng mạn hạnh phúc đang chờ đợi bạn. Bất chấp những thách thức, bạn sẽ làm tốt trong công việc. Hôm nay là một ngày tốt để đầu tư.'),
        ('Nhân Mã', 'Hãy thận trọng khi giải quyết các vấn đề tình cảm trong ngày hôm nay. Những thách thức chuyên môn tồn tại nhưng bạn sẽ khắc phục được chúng. Vận may tài chính sẽ ở bên bạn.'),
        ('Ma Kết', 'Tử vi gợi ý giải quyết các vấn đề trong mối quan hệ. Các nhiệm vụ chuyên môn có vẻ khó khăn nhưng hãy xử lý chúng một cách thông minh.'),
        ('Bảo Bình', 'Hãy đón nhận hạnh phúc trong đời sống tình cảm hôm nay. Những thách thức chuyên môn sẽ được biến thành cơ hội. Giữ gìn sức khỏe.'),
        ('Song Ngư', 'Hãy chân thành trong mối quan hệ hôm nay và bỏ qua những tranh luận không cần thiết. Các trách nhiệm công việc sẽ khiến bạn bận rộn suốt cả ngày.')
    ]
    cursor.executemany("INSERT OR IGNORE INTO predictions VALUES (?, ?)", prediction_data)

    # Tạo bảng users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            birth_day INTEGER NOT NULL,
            birth_month INTEGER NOT NULL,
            zodiac_sign TEXT NOT NULL
        )
    ''')

    # Tạo bảng history
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

    conn.commit()
    yield conn
    conn.close()

def test_get_zodiac_sign_from_db(db_connection):
    assert get_zodiac_sign_from_db(db_connection, 2, 3) == 'Song Ngư'
    assert get_zodiac_sign_from_db(db_connection, 27, 10) == 'Bọ Cạp'
    assert get_zodiac_sign_from_db(db_connection, 30, 2) is None

def test_get_prediction_from_db(db_connection):
    assert "tình cảm siêng năng" in get_prediction_from_db(db_connection, 'Song Tử')
    assert get_prediction_from_db(db_connection, 'Không tồn tại') is None

def test_create_user_in_db(db_connection):
    user_id = create_user_in_db(db_connection, 1, 1, 'Ma Kết', 'Test User')
    assert user_id is not None

def test_get_user_by_birthdate_from_db(db_connection):
    create_user_in_db(db_connection, 1, 1, 'Ma Kết', 'Test User')
    user = get_user_by_birthdate_from_db(db_connection, 1, 1)
    assert user is not None
    assert user[2] == 'Ma Kết'
    user_nonexistent = get_user_by_birthdate_from_db(db_connection, 2, 2)
    assert user_nonexistent is None

def test_save_lookup_history_to_db(db_connection):
    user_id = create_user_in_db(db_connection, 1, 1, 'Ma Kết', 'Test User')
    save_lookup_history_to_db(db_connection, user_id, 'Ma Kết', 'Một ngày tốt lành.')
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM history WHERE user_id = ?", (user_id,))
    history_item = cursor.fetchone()
    assert history_item is not None
    assert history_item[3] == 'Ma Kết'
    assert history_item[4] == 'Một ngày tốt lành.'

def test_get_lookup_history_from_db(db_connection):
    user_id = create_user_in_db(db_connection, 1, 1, 'Ma Kết', 'Test User')
    save_lookup_history_to_db(db_connection, user_id, 'Ma Kết', 'Dự đoán 1.')
    save_lookup_history_to_db(db_connection, user_id, 'Bảo Bình', 'Dự đoán 2.')
    history = get_lookup_history_from_db(db_connection, user_id)
    assert len(history) == 2
    assert history[0][1] == 'Bảo Bình'
    assert history[1][1] == 'Ma Kết'

def test_generate_lucky_number():
    zodiac_sign = "Song Ngư"
    lucky_number = generate_lucky_number(zodiac_sign)
    assert isinstance(lucky_number, int)
    assert 1 <= lucky_number <= 10 + len(zodiac_sign) + 5 # Kiểm tra nằm trong khoảng hợp lý
