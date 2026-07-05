# 🚀 Collab Workspace

> Коллаборативное рабочее пространство реального времени с AI-функциями, построенное на современных веб-технологиях.

![Status](https://img.shields.io/badge/status-in%20development-orange)
![License](https://img.shields.io/badge/license-MIT-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5.3-blue)
![Python](https://img.shields.io/badge/Python-3.11%2B-green)

## 📖 О проекте

Collab Workspace — это коллаборативная платформа для редактирования документов, вдохновлённая Notion и Google Docs. Она поддерживает синхронизацию в реальном времени, работу офлайн и генерацию контента с помощью ИИ.

Проект создан для демонстрации экспертизы в:
- **Коллаборации в реальном времени с использованием CRDT (Yjs)**
- **Full-stack архитектуре TypeScript/Python**
- **Современных DevOps практиках (Docker, CI/CD, тестирование)**
- **Интеграции ИИ (готовность к OpenAI/LangChain)**

## 🏗 Архитектура

### Модульный монолит в монорепо
Проект построен как **модульный монолит** в формате **монорепо**. Это осознанный архитектурный выбор, который балансирует между простотой разработки и готовностью к масштабированию.

## ✨ Возможности

### Основные
- 📝 **Редактор форматированного текста** — на базе TipTap с поддержкой Markdown
- 🔄 **Синхронизация в реальном времени** — мгновенное обновление у всех подключённых клиентов
- 👥 **Присутствие** — видно, кто просматривает/редактирует документ, с живыми курсорами
- 💾 **Офлайн-режим** — продолжайте работать без интернета, автосинхронизация при восстановлении связи
- 🏢 **Рабочие пространства** — организация документов в коллаборативные пространства

### Технические
- ⚡ **На базе CRDT** — бесконфликтное слияние с помощью Yjs
- 🔐 **Аутентификация** — безопасная JWT-аутентификация
- 🎨 **Современный UI** — Tailwind CSS + shadcn/ui
- 📊 **Типобезопасность** — End-to-end TypeScript с генерацией из OpenAPI
- 🐳 **Готов к Docker** — запуск локально одной командой

### ИИ (Скоро)
- 🤖 **AI-ассистент** — генерация, суммаризация и преобразование контента
- 💡 **Умные подсказки** — контекстное автодополнение
- 🌐 **Мультиязычность** — Real-time translation

## 🛠 Технологический стек

### Frontend
- **Фреймворк:** Next.js 15 (App Router) + React 19
- **Язык:** TypeScript 5.3
- **Стилизация:** Tailwind CSS v4 + shadcn/ui
- **Редактор:** TipTap + Yjs (CRDT)
- **Состояние:** Zustand + React Query
- **Архитектура:** Feature-Sliced Design (FSD)

### Backend
- **Фреймворк:** FastAPI (Python 3.11+)
- **Real-time:** WebSocket + Socket.io
- **База данных:** PostgreSQL 16 + SQLAlchemy 2.0 (async)
- **Кэш/PubSub:** Redis 7
- **CRDT:** y-py (Python Yjs implementation)
- **Валидация:** Pydantic v2

### DevOps и качество
- **Контейнеризация:** Docker + docker-compose
- **CI/CD:** GitHub Actions
- **Тестирование:** Vitest (Unit) + Playwright (E2E) + Pytest
- **Линтеры:** ESLint + Prettier (JS) | Ruff + Mypy (Python)
- **Git-хуки:** Husky + lint-staged + pre-commit

## 🚀 Быстрый старт

### Требования
- Docker & Docker Compose
- Node.js 20+
- Python 3.11+
- npm

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/YOUR_USERNAME/collab-workspace.git
cd collab-workspace
```

### 2. Запустите инфраструктуру
```bash
docker-compose up -d
```

### 3. Настройте Backend
```bash
cd apps/server
python -m venv venv
source venv/bin/activate  # On Windows: venv/Scripts/activate
pip install -r requirements-dev.txt
alembic upgrade head
python run.py
```

### 4. Настройте Frontend
```bash
npm install
npm run dev
```

### 5. Open the app
```bash
Visit http://localhost:3000
```

### 📂 Project Structure
```bash
collab-workspace/
├── apps/
│   ├── web/                    # Next.js фронтенд (FSD)
│   │   ├── app/                # Страницы App Router
│   │   ├── widgets/            # Составные блоки
│   │   ├── features/           # Пользовательские фичи
│   │   ├── entities/           # Бизнес-сущности
│   │   └── shared/             # Переиспользуемый код
│   │
│   └── server/                 # FastAPI бэкенд (DDD)
│       ├── app/
│       │   ├── api/            # REST эндпоинты
│       │   ├── ws/             # WebSocket обработчики
│       │   ├── core/           # Конфигурация, безопасность
│       │   ├── db/             # Модели базы данных
│       │   └── services/       # Бизнес-логика
│       └── tests/
│
├── packages/
│   ├── ui/                     # Общие UI компоненты
│   └── config/                 # Общие конфигурации
│
├── docker-compose.yml
├── .github/workflows/          # CI/CD
└── README.md
```

### 🧪 Тестирование

# Frontend tests
```bash
cd apps/web
npm run test          # Unit тесты (Vitest)
npm run test:e2e      # E2E тесты (Playwright)
```

# Backend tests
```bash
cd apps/server
pytest             # Unit тесты
pytest --e2e       # Интеграционные тесты
```

### 🗺 Дорожная карта
```bash
Project setup & architecture
Authentication (JWT)
Workspace CRUD
Document CRUD
Real-time editor with Yjs
Presence & cursors
Offline-first sync
AI integration (OpenAI)
File attachments
Comments & mentions
Mobile responsive
```

### 📸 Скриншоты
Скоро...

### 🤝 Участие в проекте
Это портфолийный проект, но обратная связь приветствуется! Создавайте issue или PR.
📄 Лицензия
MIT © Данила, Елена
<div align="center">

### Создано с ❤️ для обучения и демонстрации современной веб-разработки
</div>
