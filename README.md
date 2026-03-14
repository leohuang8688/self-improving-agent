# 🧤 Self-Improving Agent

**OpenClaw Skill - Self-Improving Agent System**

A continuous learning agent skill for OpenClaw that learns from interactions and continuously improves its performance.

**[🇺🇸 English](README.md)** | **[🇨🇳 中文文档](README-CN.md)**

---

## ✨ Features

- 🧠 **Continuous Learning** - Learns from every interaction
- 🔄 **Auto-Improvement** - Automatically applies improvements
- 📚 **Memory System** - Stores and retrieves learnings
- 🔌 **Hook System** - Extensible hook system for custom improvements
- 📊 **Progress Tracking** - Track improvement over time
- 🔧 **Python CLI** - Easy to use command-line interface
- 🧩 **OpenClaw Skill** - Seamless integration with OpenClaw

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- OpenClaw installed
- pip or uv package manager

### Installation

#### As OpenClaw Skill

```bash
# Clone to OpenClaw skills directory
cd ~/.openclaw/workspace/skills
git clone https://github.com/leohuang8688/self-improve-claw.git
```

#### As Python Package

```bash
# Clone the repository
git clone https://github.com/leohuang8688/self-improve-claw.git
cd self-improve-claw

# Install with pip
pip install -e .

# Or install with uv
uv pip install -e .
```

### Enable in OpenClaw

Add to your OpenClaw configuration:

```json
{
  "skills": {
    "self-improve-claw": {
      "enabled": true
    }
  }
}
```

### Basic Usage

```bash
# Run the self-improving agent
python -m self_improving_agent run

# Learn from last session
python -m self_improving_agent learn

# Review all learnings
python -m self_improving_agent review

# Export learnings to file
python -m self_improving_agent export
```

---

## 📖 Commands

### `run` - Run the Agent

Executes the self-improving agent with all applied improvements.

```bash
python -m self_improving_agent run --workspace /path/to/workspace
```

### `learn` - Learn from Session

Analyzes the last session and extracts learnings.

```bash
python -m self_improving_agent learn --verbose
```

### `review` - Review Learnings

Reviews all stored learnings.

```bash
python -m self_improving_agent review --verbose
```

### `export` - Export Learnings

Exports all learnings to a markdown file.

```bash
python -m self_improving_agent export
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
