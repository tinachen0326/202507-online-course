# 線上課程平台 Online Course Platform（原 學生與老師 API 管理文件）

## 專案簡介

這是一個 線上課程管理平台，提供學生與老師之間的課程管理與報名功能。
專案使用 Django + Django REST Framework 作為後端，前端使用 Django Templates + Tailwind CSS，並透過 Django Admin 管理資料。

## 資料結構

<img width="1029" height="437" alt="線上課程平台" src="https://github.com/user-attachments/assets/40ac5a5c-b8ea-4933-bd8a-32f6bb0f59eb" />

### Teacher

| 欄位名稱 | 型別       | 說明           |
| -------- | ---------- | -------------- |
| id       | Integer    | 主鍵，自動產生 |
| name     | Char(100)  | 老師姓名       |
| email    | EmailField | 電子信箱，唯一 |
| bio      | Text       | 老師介紹，可選 |

### Student

| 欄位名稱 | 型別       | 說明                     |
| -------- | ---------- | ------------------------ |
| id       | Integer    | 主鍵，自動產生           |
| name     | Char(100)  | 學生姓名                 |
| email    | EmailField | 電子信箱，唯一           |
| level    | Char(20)   | 學生等級：初級/中級/高級 |

### Course

| 欄位名稱    | 型別                      | 說明                   |
| ----------- | ------------------------- | ---------------------- |
| id          | Integer                   | 主鍵，自動產生         |
| title       | Char(200)                 | 課程名稱               |
| description | Text                      | 課程說明               |
| teachers    | ManyToManyField → Teacher | 課程對應老師（多對多） |
| created_at  | DateTime                  | 課程建立時間，自動填入 |

### Enrollment

| 欄位名稱    | 型別                 | 說明               |
| ----------- | -------------------- | ------------------ |
| id          | Integer              | 主鍵，自動產生     |
| student     | ForeignKey → Student | 報名學生           |
| course      | ForeignKey → Course  | 報名課程           |
| enrolled_at | DateTime             | 報名時間，自動填入 |

限制：學生對同一門課程只能報名一次（unique_together(student, course)）

## 專案架構

```
online_course_platform/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── courses/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── course_list.html
│   │   ├── course_detail.html
│   │   ├── teacher_list.html
│   │   └── student_list.html
│   └── static/css/
└──README.md
```

## 使用技術

- 後端：Python 3, Django 5, Django REST Framework
- 前端：Django Templates, Tailwind CSS
- 資料庫：SQLite
- 其他工具：Django Admin

## API 功能與路徑對應表

| 功能         | HTTP 方法 | 路徑            | 說明                      |
| ------------ | --------- | --------------- | ------------------------- |
| 列出所有課程 | GET       | /api/courses/   | 課程列表                  |
| 課程詳細資訊 | GET       | /api/courses/2/ | 單一課程詳情              |
| 新增課程     | POST      | /api/courses/   | 新增課程（需提供老師 ID） |
| 列出所有老師 | GET       | /api/teachers/  | 老師列表                  |
| 新增老師     | POST      | /api/teachers/  | 新增老師                  |
| 列出所有學生 | GET       | /api/students/  | 學生列表                  |
| 新增學生     | POST      | /api/students/  | 新增學生                  |
| 學生報名課程 | POST      | /api/enroll/    | 新增學生報名課程          |

## POST 請求格式（JSON）

1. 新增老師 /api/teachers/

```
 {
  "name": "王老師",
  "email": "teacher_wang@example.com",
  "bio": "專長英文與文法教學"
}
```

2. 新增學生 /api/students/

```
{
  "name": "小明",
  "email": "student_ming@example.com",
  "level": "初級"
}
```

3. 新增課程 /api/courses/

```
{
  "title": "英文入門",
  "description": "基礎文法與聽力練習",
  "teachers": [1, 2]
}
```

4. 學生報名課程 /api/enroll/

```
{
  "student_id": 2,
  "course_id": 1
}
```

## 安裝與執行

1. Clone 專案

```
git clone https://github.com/tinachen0326/250723-python-practice.git
cd online_course_platform
```

2. 建立虛擬環境 & 安裝依賴

```
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

3. 資料庫遷移

```
python manage.py makemigrations
python manage.py migrate
```

4. 建立 superuser（管理員帳號）

```
python manage.py createsuperuser
```

5. 啟動開發伺服器

```
python manage.py runserver
```

6. 網站路徑

- 前端：http://127.0.0.1:8000/（課程列表）
- http://127.0.0.1:8000/teachers/ （老師列表）
- http://127.0.0.1:8000/students/ （學生列表）
- http://127.0.0.1:8000/courses/2/ （課程詳情，假設課程 ID=2）
- Django Admin：http://127.0.0.1:8000/admin/

## 使用方式

1. 在 Django Admin 新增老師與學生資料
2. 在課程列表頁面查看課程資訊
3. 在課程詳情頁面輸入學生 ID 報名課程
4. 同一學生不可重複報名同一課程
5. 老師與學生資料可透過 Admin 管理

## 版權聲明

此專案僅供個人學習參考使用，無授權用途。
