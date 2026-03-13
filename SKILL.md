---
name: self-improver
description: Self-improving agent system for OpenClaw. Enables continuous learning from interactions and automatic performance improvements. Features memory system, hook system, and progress tracking.
---

# Self-Improver

## 🔒 Security

- ✅ No shell command execution
- ✅ No external API calls without permission
- ✅ All data stored locally
- ✅ Open source and auditable
- ✅ No sensitive data collection

## Overview

Self-Improving Claw is an OpenClaw skill that enables continuous learning and automatic improvement. It learns from every interaction and applies improvements automatically.

## Features

- 🧠 **Continuous Learning** - Learns from every interaction
- 🔄 **Auto-Improvement** - Automatically applies improvements
- 📚 **Memory System** - Stores and retrieves learnings
- 🔌 **Hook System** - Extensible hook system
- 📊 **Progress Tracking** - Track improvement over time

## Commands

### Learn from Session

```bash
python -m self_improve_claw learn
```

### Review Learnings

```bash
python -m self_improve_claw review
```

### Export Learnings

```bash
python -m self_improve_claw export
```

## Environment Variables

```bash
# Optional: Workspace path
WORKSPACE_PATH=~/.openclaw/workspace

# Optional: Enable/disable learning
LEARNING_ENABLED=true

# Optional: Auto-apply improvements
AUTO_APPLY=true
```

## Usage Examples

### Run the Agent

```python
from self_improve_claw import SelfImprovingAgent

agent = SelfImprovingAgent()
agent.run()
```

### Learn from Last Session

```python
from self_improve_claw import LearningMemory

memory = LearningMemory()
memory.load()
learnings = memory.get_all()
```

## Architecture

```
OpenClaw Agent
     ↓
Self-Improving Claw
     ↓
┌────┴────┐
│Hooks    │
│Memory   │
└─────────┘
```

## Notes

1. **Learning**: Automatically extracts learnings from interactions
2. **Memory**: Stores learnings in JSON format
3. **Hooks**: Extensible system for custom improvements
4. **Privacy**: All data stored locally, no external transmission

## Troubleshooting

### No Learnings Found
- Ensure learning is enabled
- Check if interactions have occurred
- Verify workspace path is correct

### Import Errors
- Ensure package is installed: `pip install -e .`
- Check Python version: requires Python 3.10+

## Resources

- [GitHub Repository](https://github.com/leohuang8688/self-improve-claw)
- [OpenClaw Documentation](https://docs.openclaw.ai/)

## Changelog

### v1.0.0 (2026-03-13)
- ✅ Initial release
- ✅ Continuous learning system
- ✅ Memory system
- ✅ Hook system
- ✅ CLI interface
- ✅ OpenClaw integration

## License

MIT License

## Author

PocketAI for Leo - OpenClaw Community
