# 🚀 Collab Workspace

> Real-time collaborative workspace with AI-powered features, built with modern web technologies.

![Status](https://img.shields.io/badge/status-in%20development-orange)
![License](https://img.shields.io/badge/license-MIT-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5.3-blue)
![Python](https://img.shields.io/badge/Python-3.11%2B-green)

## 📖 About

Collab Workspace is a production-grade collaborative editing platform inspired by Notion and Google Docs. It features real-time synchronization, offline-first capabilities, and AI-powered content generation.

Built to demonstrate expertise in:
- **Real-time collaboration** using CRDT (Yjs)
- **Full-stack TypeScript/Python** architecture
- **Modern DevOps practices** (Docker, CI/CD, testing)
- **AI integration** (OpenAI/LangChain ready)

## ✨ Features

### Core
- 📝 **Rich Text Editor** — TipTap-based with markdown support
- 🔄 **Real-time Sync** — Instant updates across all connected clients
- 👥 **Presence** — See who's viewing/editing with live cursors
- 💾 **Offline-first** — Continue working without internet, auto-sync when back online
- 🏢 **Workspaces** — Organize documents into collaborative spaces

### Technical
- ⚡ **CRDT-powered** — Conflict-free merging with Yjs
- 🔐 **Authentication** — Secure JWT-based auth
- 🎨 **Modern UI** — Tailwind CSS + shadcn/ui
- 📊 **Type-safe** — End-to-end TypeScript with OpenAPI codegen
- 🐳 **Docker-ready** — One-command local setup

### AI (Coming Soon)
- 🤖 **AI Assistant** — Generate, summarize, and transform content
- 💡 **Smart Suggestions** — Context-aware autocomplete
- 🌐 **Multi-language** — Real-time translation

## 🛠 Tech Stack

### Frontend
- **Framework:** Next.js 15 (App Router) + React 19
- **Language:** TypeScript 5.3
- **Styling:** Tailwind CSS v4 + shadcn/ui
- **Editor:** TipTap + Yjs (CRDT)
- **State:** Zustand + React Query
- **Architecture:** Feature-Sliced Design (FSD)

### Backend
- **Framework:** FastAPI (Python 3.11+)
- **Real-time:** WebSocket + Socket.io
- **Database:** PostgreSQL 16 + SQLAlchemy 2.0 (async)
- **Cache/PubSub:** Redis 7
- **CRDT:** y-py (Python Yjs implementation)
- **Validation:** Pydantic v2

### DevOps & Quality
- **Containerization:** Docker + docker-compose
- **CI/CD:** GitHub Actions
- **Testing:** Vitest (Unit) + Playwright (E2E) + Pytest
- **Linting:** ESLint + Prettier (JS) | Ruff + Mypy (Python)
- **Git Hooks:** Husky + lint-staged + pre-commit

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 20+
- Python 3.11+
- npm

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/collab-workspace.git
cd collab-workspace
```

### 2. Start infrastructure
```bash
docker-compose up -d
```

### 3. Setup Backend
```bash
cd apps/server
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

### 4. Setup Frontend
```bash
cd apps/web
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
│   ├── web/                    # Next.js frontend (FSD)
│   │   ├── app/                # App Router pages
│   │   ├── processes/          # App-wide logic
│   │   ├── widgets/            # Composite blocks
│   │   ├── features/           # User features
│   │   ├── entities/           # Business entities
│   │   └── shared/             # Reusable code
│   │
│   └── server/                 # FastAPI backend
│       ├── app/
│       │   ├── api/            # REST endpoints
│       │   ├── ws/             # WebSocket handlers
│       │   ├── core/           # Config, security
│       │   ├── db/             # Database models
│       │   └── services/       # Business logic
│       └── tests/
│
├── packages/
│   ├── ui/                     # Shared UI components
│   └── config/                 # Shared configs
│
├── docker-compose.yml
├── .github/workflows/          # CI/CD
└── README.md
```

### 🧪 Testing
```bash
# Frontend tests
cd apps/web
npm run test          # Unit tests (Vitest)
npm run test:e2e      # E2E tests (Playwright)
```

# Backend tests
```bash
cd apps/server
pytest             # Unit tests
pytest --e2e       # Integration tests
```

### 🗺 Roadmap
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

### 📸 Screenshots
Coming soon...
<!-- Add screenshots here when ready -->

### 🤝 Contributing
This is a portfolio project, but feedback is welcome! Feel free to open an issue or PR.
📄 License
MIT © Danila, Elena
<div align="center">

### Built with ❤️ for learning and showcasing modern web development
⬆ Back to top
</div>