# Personal Daily Journal

It is a Django-based web application called Personal Daily Journal that allows users to register, log in, and maintain a private daily journal with task management. Each user can create journal entries for different days, track their mood, add tasks to entries, and view personal statistics. The app uses an SQLite database with two main models linked by foreign keys (`DailyEntry` and `DailyTask`), plus Django's built-in User model for authentication.

## Features

- **User Authentication**: Secure registration and login system
- **Daily Entries**: Create, edit, and delete journal entries with date, title, content, and mood
- **Task Management**: Add tasks to entries with priority levels (Low, Medium, High)
- **Mood Tracking**: Record daily emotions with emoji indicators
- **Statistics Dashboard**: View total entries, tasks, completion rates, and mood patterns
- **Bootstrap Modal**: Quick task addition using a modal dialog
- **Django Admin**: Customized admin panel for data management

## Installation

To install, clone the repository and install the required packages:

```bash
git clone https://github.com/otojbo/MiniProject4---IlliaIvanov.git
cd personal-diary
pip install -r requirements.txt
```

## Usage

Before running the web app, initialize the SQLite database by executing:

```bash
python manage.py makemigrations
python manage.py migrate
```

This will create the `db.sqlite3` database file with the following tables:
- `journal_dailyentry` - stores journal entries
- `journal_dailytask` - stores tasks linked to entries
- `auth_user` - Django's built-in user table

After initializing the database, create a superuser account for admin access:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin username, email, and password.

Then, start the Django development server:

```bash
python manage.py runserver
```

Open your browser and go to:

```
http://127.0.0.1:8000
```

You can register a new user, log in, and begin writing journal entries.

To access the admin panel, navigate to:

```
http://127.0.0.1:8000/admin
```

## Project Structure

```
personal_diary/
│
├── journal/                          # Main application
│   ├── migrations/                   # Database migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── templates/                    # HTML templates
│   │   └── journal/
│   │       ├── about.html            # About page
│   │       ├── base.html             # Base template
│   │       ├── entry_confirm_delete.html  # Delete confirmation
│   │       ├── entry_detail.html     # Entry detail with tasks
│   │       ├── entry_form.html       # Create/edit entry form
│   │       ├── entry_list.html       # All entries list
│   │       ├── home.html             # Dashboard
│   │       ├── landing.html          # Landing page
│   │       └── profile.html          # User profile & stats
│   ├── __init__.py
│   ├── admin.py                      # Admin configuration
│   ├── apps.py                       # App configuration
│   ├── forms.py                      # Django forms
│   ├── models.py                     # Database models
│   ├── urls.py                       # URL routing
│   └── views.py                      # View functions
│
├── personal_diary/                   # Project settings
│   ├── __init__.py
│   ├── asgi.py                       # ASGI config
│   ├── settings.py                   # Django settings
│   ├── urls.py                       # Main URL config
│   └── wsgi.py                       # WSGI config
│
├── templates/                        # Global templates
│   └── registration/
│       ├── login.html                # Login page
│       ├── logout.html               # Logout confirmation
│       └── register.html             # Registration page
│
├── db.sqlite3                        # SQLite database
├── manage.py                         # Django management script
├── requirements.txt                  # Python dependencies
├── .gitignore                        # Git ignore rules
└── README.md                         # This file
```

## Main Functionality

### Journal Entries
- **Create Entry**: Write daily entries with title, content, mood selection, and date
- **View Entries**: Browse all entries in a card-based grid layout
- **Entry Detail**: View full entry with associated tasks
- **Edit Entry**: Modify existing entries
- **Delete Entry**: Remove entries with confirmation dialog

### Task Management
- **Add Tasks**: Use Bootstrap modal to quickly add tasks to entries
- **Task Properties**: Set task title, priority (Low/Medium/High), and completion status
- **Toggle Completion**: Mark tasks complete/incomplete with checkbox (AJAX)
- **Priority Badges**: Visual indicators for task priority levels

### User Features
- **Registration**: Create new account with username, email, and password
- **Login/Logout**: Secure authentication system
- **Profile**: View personal statistics including:
  - Total entries count
  - Total tasks count
  - Completed tasks count
  - Mood distribution chart
  - Task completion rate

### Admin Panel
- **User Management**: View and manage registered users
- **Entry Management**: Create, edit, delete entries with inline task editing
- **Search & Filters**: Filter entries by mood, date, and user
- **Bulk Actions**: Manage multiple entries at once

## Technologies Used

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Database**: SQLite3
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Authentication**: Django built-in auth system

## Pages

1. **Home** (`/`) - Landing page or dashboard depending on login status
2. **All Entries** (`/entries/`) - Grid view of all user entries
3. **Entry Detail** (`/entry/<id>/`) - Single entry with tasks and modal
4. **Create Entry** (`/entry/new/`) - Form to create new entry
5. **Edit Entry** (`/entry/<id>/edit/`) - Form to edit existing entry
6. **Profile** (`/profile/`) - User statistics and mood tracking
7. **About** (`/about/`) - Information about the application
8. **Login** (`/login/`) - User authentication
9. **Register** (`/register/`) - New user registration
10. **Admin** (`/admin/`) - Django admin interface

## Database Models

### DailyEntry
- `user` - ForeignKey to User (who wrote the entry)
- `date` - DateField (entry date)
- `title` - CharField (entry title)
- `content` - TextField (main journal content)
- `mood` - CharField with choices (happy, neutral, sad, angry, tired)
- `created_at` - DateTimeField (auto-generated)
- `updated_at` - DateTimeField (auto-updated)

### DailyTask
- `daily_entry` - ForeignKey to DailyEntry (parent entry)
- `title` - CharField (task description)
- `completed` - BooleanField (completion status)
- `priority` - CharField with choices (low, medium, high)
- `created_at` - DateTimeField (auto-generated)

## Requirements

All dependencies are listed in `requirements.txt`:
- asgiref==3.10.0
- crispy-bootstrap5==0.7
- Django==4.2.7
- django-crispy-forms==2.1
- sqlparse==0.5.3
- tzdata==2025.2
