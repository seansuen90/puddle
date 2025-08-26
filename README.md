

# 🐳 Puddle Django Project

Welcome to **Puddle**, a Django-based marketplace app! This guide will walk you step by step through the project setup, apps, and features.
source venv/bin/activate

---

## 1️⃣ Initial Project Setup

- ⚡ Method: Set up a Python virtual environment: python 3 -m venv env and activate it with source env/bin/activate
- 📦 Method: Install Django: pip install Django
- 🏗 Method: Create a Django project named "puddle": django-admin startproject puddle
- 📂 File Configuration:
  - manage.py → administrative tasks
  - settings.py → global configuration
  - urls.py → project table of contents
- ▶️ Method: Run the development server to verify installation: python manage.py runserver

---

## 2️⃣ Core Application Setup (Front Page, Base Template, Contact Page)

- 🛠 Method: Create a new Django app called "core": python manage.py startapp core
- ⚙️ Configuration: Register the "core" app in INSTALLED_APPS in settings.py

### 🏠 Front Page

- ✏️ Method: Define an index view in core/views.py to render core/index.html
- 📝 HTML: Create core/templates/core/index.html with basic HTML structure and heading
- 🔗 URL: Link root / to core.views.index in puddle/urls.py, named index

### 📐 Base Template (Reusability)

- 🖋 HTML: Create core/templates/core/base.html, move most of index.html code into it, using {% block content %} and {% block title %}
- 🔄 HTML: Update index.html to extend base.html and place content inside the content block
- 🌐 HTML: Add <nav> and <footer> with links: New Item, Browse, Sign up, Login

### 📬 Contact Page

- ✏️ Method: Define a contact view in core/views.py rendering core/contact.html
- 📝 HTML: Create core/templates/core/contact.html extending base.html
- 🔗 URL: Create core/urls.py, set app_name = 'core', add paths for index and contact
- ⚙️ Configuration: Include core.urls in puddle/urls.py
- 🌐 HTML: Update contact link in base.html to {% url 'core:contact' %}

---

## 3️⃣ Item Application (Categories and Items)

- 🛠 Method: Create a new Django app called "item": python manage.py startapp item
- ⚙️ Configuration: Register "item" in INSTALLED_APPS

### 🗂 Category Model

- ✏️ Model: Define Category in item/models.py with name field
- 🔧 Method: Run migrations: makemigrations and migrate
- 🖥 Admin Interface: Register Category in item/admin.py
- 📝 Enhancements: Override __str__, set Meta options for verbose_name_plural and ordering

### 📦 Item Model

- ✏️ Model: Define Item in item/models.py with fields: name, description, price, is_sold, created_at, created_by, category, image
- 📦 Method: Install Pillow: pip install pillow
- 🔧 Method: Run migrations
- ⚙️ Configuration: Set MEDIA_URL and MEDIA_ROOT in settings.py
- 🖥 Admin Interface: Register Item in item/admin.py
- 📝 Enhancements: Override __str__
- 🔗 URL: Add + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) to puddle/urls.py

### 🏠 Front Page Display

- ✏️ Method: Update index view to query six newest items (not sold) and all categories
- 📝 HTML: Display newest items and categories in a grid in index.html

### 🔍 Item Detail Page

- ✏️ Method: Define detail view in item/views.py, fetch related items
- 📝 HTML: Create item/templates/item/detail.html extending base.html
- 🔗 URL: Add item/urls.py with detail path, include in puddle/urls.py
- 🌐 HTML: Update links in index.html to item:detail passing item ID

---

## 4️⃣ User Authentication (Sign Up & Login)

### 📝 Sign Up

- ✏️ Form: Create SignupForm in core/forms.py inheriting from UserCreationForm
- 🔧 Method: Define signup view in core/views.py (POST validates & saves, GET shows empty form)
- 🖋 HTML: Create signup.html extending base.html
- 🔗 URL: Add signup path in core/urls.py
- 🌐 HTML: Update nav link in base.html to {% url 'core:signup' %}

### 🔑 Login

- ✏️ Form: LoginForm inherits from AuthenticationForm, custom widgets
- 🔗 URL: Add login path using Django's LoginView
- 🖋 HTML: Create login.html extending base.html
- ⚙️ Configuration: Set LOGIN_REDIRECT_URL, LOGIN_URL, LOGOUT_REDIRECT_URL
- 🌐 HTML: Conditional nav links: Inbox & Dashboard if authenticated, Sign up / Login otherwise

---

## 5️⃣ Dashboard Application

- 🛠 Method: Create dashboard app: python manage.py startapp dashboard
- ⚙️ Configuration: Register in INSTALLED_APPS

### 📋 Dashboard Index

- ✏️ Method: @login_required view, queries items by current user
- 🖋 HTML: Create dashboard/index.html showing "My Items"
- 🔗 URL: Add dashboard path, include in puddle/urls.py
- 🌐 HTML: Update Dashboard link in nav

### 🗑 Delete Item

- ✏️ Method: Delete view with @login_required, user ownership check
- 🔗 URL: Add delete path in item/urls.py
- 🌐 HTML: Conditional Delete button in item detail

### ✏️ Edit Item

- ✏️ Form: EditItemForm in item/forms.py
- 🔧 Method: Edit view in item/views.py
- 🖋 HTML: Reuse form.html template
- 🔗 URL: Add edit path
- 🌐 HTML: Conditional Edit button in item detail

---

## 6️⃣ Browse Page (Search & Filter)

- ✏️ Method: items view queries unsold items, handles search & category filter
- 🖋 HTML: items.html sidebar search form, categories list, Clear Filters, main content lists items
- 🔗 URL: Add items path in item/urls.py
- 🌐 HTML: Update Browse link in nav

---

## 7️⃣ Conversation Application

- 🛠 Method: Create conversation app: python manage.py startapp conversation
- ⚙️ Configuration: Register in INSTALLED_APPS

### 💬 Conversation Models

- ✏️ Conversation: item, members, created_at, modified_at
- ✏️ ConversationMessage: conversation, content, created_by, created_at
- 🔧 Method: Run migrations
- 🖥 Admin: Register models

### 📝 Message Form

- ✏️ Form: ConversationMessageForm in conversation/forms.py

### ✨ New Conversation

- ✏️ Method: new_conversation view, POST creates conversation & message, GET shows empty form
- 🖋 HTML: new.html extending base.html
- 🔗 URL: Add path in conversation/urls.py, include in puddle/urls.py
- 🌐 HTML: Update "Contact Seller" button in item detail

### 📥 Inbox Page

- ✏️ Method: inbox view queries all conversations of user
- 🖋 HTML: inbox.html lists conversations: item image, other member, last modified, item name
- 🔗 URL: Add inbox path
- 🌐 HTML: Update Inbox link in nav

### 📄 Conversation Detail Page

- ✏️ Method: detail view handles POST to add messages, GET shows form
- 🖋 HTML: detail.html displays messages and form
- 🔗 URL: Add detail path
- 🌐 HTML: Link conversations in inbox to detail page

---

🎉 Congratulations! You now have a complete, step-by-step guide to understand the Puddle Django project flow.
