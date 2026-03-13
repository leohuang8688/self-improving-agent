# 🧤 Self-Improving Claw

**Self-Improving Agent System for OpenClaw**

A continuous learning agent system that learns from interactions and continuously improves its performance.

**[🇺🇸 English](README.md)** | **[🇨🇳 中文文档](README-CN.md)**

---

## ✨ Features

- 🧠 **Continuous Learning** - Learns from every interaction
- 🔄 **Auto-Improvement** - Automatically applies improvements
- 📚 **Memory System** - Stores and retrieves learnings
- 🔌 **Hook System** - Extensible hook system for custom improvements
- 📊 **Progress Tracking** - Track improvement over time
- 🐍 **Python CLI** - Easy to use command-line interface

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- OpenClaw installed
- pip or uv package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/leohuang8688/self-improve-claw.git
cd self-improve-claw

# Install with pip
pip install -e .

# Or install with uv
uv pip install -e .
```

### Basic Usage

```bash
# Run the self-improving agent
self-improve-claw run

# Learn from last session
self-improve-claw learn

# Review all learnings
self-improve-claw review

# Export learnings to file
self-improve-claw export
```

---

## 📖 Commands

### `run` - Run the Agent

Executes the self-improving agent with all applied improvements.

```bash
self-improve-claw run --workspace /path/to/workspace
```

### `learn` - Learn from Session

Analyzes the last session and extracts learnings.

```bash
self-improve-claw learn --verbose
```

### `review` - Review Learnings

Reviews all stored learnings.

```bash
self-improve-claw review --verbose
```

### `export` - Export Learnings

Exports all learnings to a markdown file.

```bash
self-improve-claw export
```

---

## 🏗️ Architecture

```
┌─────────────────┐
│  OpenClaw       │
│  Agent          │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│ Self-Improving  │
│ Agent           │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ↓         ↓
┌──────┐  ┌──────┐
│Hooks │  │Memory│
└──────┘  └──────┘
```

### Components

- **Agent** - Main agent logic
- **Hooks** - Improvement hooks
- **Memory** - Learning storage and retrieval

---

## 📁 Project Structure

```
self-improve-claw/
├── main.py              # CLI entry point
├── src/
│   ├── agent.py         # Core agent logic
│   ├── hooks.py         # Hooks manager
│   └── memory.py        # Memory system
├── hooks/               # Custom hooks
├── learnings/           # Stored learnings
├── scripts/             # Utility scripts
├── tests/               # Test cases
├── pyproject.toml       # Project configuration
├── README.md            # English documentation
└── README-CN.md         # Chinese documentation
```

---

## 🔧 Configuration

Create a `.env` file in your workspace:

```bash
# Workspace Configuration
WORKSPACE_PATH=~/.openclaw/workspace

# Learning Configuration
LEARNING_ENABLED=true
AUTO_APPLY=true

# Hook Configuration
HOOKS_ENABLED=true
```

---

## 📚 Learning Categories

Learnings are categorized into:

- **skill_improvement** - Skill enhancements
- **error_prevention** - Error prevention patterns
- **optimization** - Performance optimizations
- **best_practice** - Best practices
- **lesson_learned** - Lessons from failures

---

## 🔌 Hook System

Create custom hooks in the `hooks/` directory:

```python
# hooks/my_hook.py

def apply():
    """Apply this hook's improvements."""
    print("Applying my improvement...")
    # Your improvement logic here
```

---

## 📊 Progress Tracking

View your improvement progress:

```bash
# Review all learnings
self-improve-claw review

# Export to markdown
self-improve-claw export > progress.md
```

---

## 🧪 Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=src

# Format code
black src/ tests/

# Lint code
ruff check src/ tests/
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

---

## 📝 License

MIT License

---

## 👨‍💻 Author

PocketAI for Leo - OpenClaw Community

---

## 🙏 Credits

- OpenClaw Team
- Self-Improving Agent Concept
- Python Community
