import sqlite3
from datetime import date

horoscope_predictions = {
    "Bạch Dương": [
        "Dành nhiều thời gian hơn cho mối quan hệ.",
        "Các nhiệm vụ chuyên môn có vẻ khó khăn nhưng bạn sẽ xử lý được.",
    ],
    "Kim Ngưu": [
        "Một mối quan hệ lãng mạn hạnh phúc đang chờ đợi bạn.",
        "Tận hưởng tình hình tài chính vững mạnh.",
    ],
    "Song Tử": [
        "Một chuyện tình cảm siêng năng là những gì tử vi dự đoán cho bạn.",
        "Đa nhiệm để hoàn thành mọi công việc trong thời hạn.",
        "Sức khỏe tài chính sẽ tốt trong ngày hôm nay.",
    ],
    "Cự Giải": [
        "Một đời sống tình cảm hạnh phúc được hỗ trợ bởi thành công trong công việc sẽ làm cho ngày của bạn tốt đẹp.",
        "Các vấn đề tài chính nhỏ sẽ tồn tại và hãy xử lý chúng một cách cẩn thận.",
        "Cũng nên kiểm tra sức khỏe.",
    ],
    "Sư Tử": [
        "Tránh xa các mối quan hệ độc hại trong ngày hôm nay.",
        "Thành công trong công việc sẽ ở bên bạn.",
        "Hãy vui vẻ vì cả tiền bạc và sức khỏe đều tốt suốt cả ngày.",
    ],
    "Xử Nữ": [
        "Bước vào mối quan hệ cũ trong ngày hôm nay.",
        "Tận dụng các cơ hội nghề nghiệp để phát triển.",
        "Đưa ra các quyết định tiền bạc thông minh & tận hưởng sức khỏe tốt.",
    ],
    "Thiên Bình": [
        "Giải quyết các vấn đề liên quan đến tình yêu bằng thái độ trưởng thành.",
        "Những thách thức chuyên môn sẽ tồn tại nhưng hãy đối phó với chúng.",
        "Cả tài chính và sức khỏe sẽ ở bên bạn trong ngày hôm nay.",
        "Hãy để mắt đến các cơ hội.",
    ],
    "Bọ Cạp": [
        "Một mối quan hệ lãng mạn hạnh phúc đang chờ đợi bạn.",
        "Bất chấp những thách thức, bạn sẽ làm tốt trong công việc.",
        "Hôm nay là một ngày tốt để đầu tư.",
    ],
    "Nhân Mã": [
        "Hãy thận trọng khi giải quyết các vấn đề tình cảm trong ngày hôm nay.",
        "Những thách thức chuyên môn tồn tại nhưng bạn sẽ khắc phục được chúng.",
        "Vận may tài chính sẽ ở bên bạn.",
    ],
    "Ma Kết": [
        "Tử vi gợi ý giải quyết các vấn đề trong mối quan hệ.",
        "Các nhiệm vụ chuyên môn có vẻ khó khăn nhưng hãy xử lý chúng một cách thông minh.",
    ],
    "Bảo Bình": [
        "Hãy đón nhận hạnh phúc trong đời sống tình cảm hôm nay.",
        "Những thách thức chuyên môn sẽ được biến thành cơ hội.",
        "Giữ gìn sức khỏe.",
    ],
    "Song Ngư": [
        "Hãy chân thành trong mối quan hệ hôm nay và bỏ qua những tranh luận không cần thiết.",
        "Các trách nhiệm công việc sẽ khiến bạn bận rộn suốt cả ngày.",
    ],
}

def getZodiacSign(conn, day, month):
    cursor = conn.cursor()
    cursor.execute("SELECT name, start_month, start_day, end_month, end_day FROM zodiac_info")
    zodiac_list = cursor.fetchall()

    for zodiac in zodiac_list:
        name, start_month, start_day, end_month, end_day = zodiac

        if start_month <= month <= end_month:
            if start_month == end_month:
                if start_day <= day <= end_day:
                    return name
            elif month == start_month and day >= start_day:
                return name
            elif month == end_month and day <= end_day:
                return name
        elif (start_month > end_month): # Trường hợp cung kéo dài qua năm mới (ví dụ: Ma Kết, Bảo Bình)
            if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
                return name

    return None

def getPrediction(conn, zodiac_sign):
    cursor = conn.cursor()
    cursor.execute("SELECT prediction FROM predictions WHERE zodiac_sign = ?", (zodiac_sign,))
    result = cursor.fetchone()
    return result[0] if result else None

def createUser(conn, birth_day, birth_month, zodiac_sign, name=None):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (birth_day, birth_month, zodiac_sign, name) VALUES (?, ?, ?, ?)",
                   (birth_day, birth_month, zodiac_sign, name))
    user_id = cursor.lastrowid
    conn.commit()
    return user_id

def getUserByBirthdate(conn, birth_day, birth_month):
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, name, zodiac_sign FROM users WHERE birth_day = ? AND birth_month = ?",
                   (birth_day, birth_month))
    result = cursor.fetchone()
    return result

def saveLookupHistory(conn, user_id, zodiac_sign, prediction):
    cursor = conn.cursor()
    lookup_date = date.today().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO history (user_id, lookup_date, zodiac_sign, prediction) VALUES (?, ?, ?, ?)",
                   (user_id, lookup_date, zodiac_sign, prediction))
    conn.commit()

def getLookupHistory(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT lookup_date, zodiac_sign, prediction FROM history WHERE user_id = ? ORDER BY lookup_date DESC", (user_id,))
    history = cursor.fetchall()
    return history

def get_all_predictions():
    return horoscope_predictions
