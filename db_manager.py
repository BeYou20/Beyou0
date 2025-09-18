import sqlite3

def init_db():
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    # جدول المستخدمين
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        gender TEXT,
        age INTEGER,
        country TEXT,
        city TEXT,
        phone TEXT,
        email TEXT,
        registered INTEGER DEFAULT 0
    )''')
    # جدول الدورات
    c.execute('''CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        category_id INTEGER,
        price INTEGER,
        seats INTEGER,
        active INTEGER DEFAULT 1
    )''')
    # جدول التصنيفات
    c.execute('''CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )''')
    # جدول تسجيلات الدورات
    c.execute('''CREATE TABLE IF NOT EXISTS registrations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        course_id INTEGER,
        paid INTEGER DEFAULT 0
    )''')
    conn.commit()
    conn.close()

def add_user(user_id):
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE id=?", (user_id,))
    exists = c.fetchone()
    if exists:
        conn.close()
        return False
    c.execute("INSERT INTO users (id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()
    return True

def get_all_admins():
    # يمكن تعديلها لاحقاً إذا أردت إدارة المشرفين من قاعدة البيانات
    from config import ADMIN_IDS
    return ADMIN_IDS
