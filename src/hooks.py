"""
Self-Improving Claw - Hooks Manager Module
"""

from pathlib import Path
from typing import List, Dict, Any
import importlib.util


class HookManager:
    """Manager for loading and applying improvement hooks."""
    
    def __init__(self, workspace: Path):
        self.workspace = Path(workspace)
        self.hooks_path = self.workspace / 'hooks'
        self.hooks_path.mkdir(parents=True, exist_ok=True)
        
    def apply_all(self):
        """Apply all available hooks."""
        hooks = self._load_hooks()
        
        for hook in hooks:
            self._apply_hook(hook)
    
    def _load_hooks(self) -> List[Any]:
        """Load all hooks from the hooks directory."""
        hooks = []
        
        for hook_file in self.hooks_path.glob('*.py'):
            hook = self._load_hook(hook_file)
            if hook:
                hooks.append(hook)
        
        return hooks
    
    def _load_hook(self, hook_file: Path):
        """Load a single hook from file."""
        spec = importlib.util.spec_from_file_location(
            hook_file.stem,
            hook_file
        )
        
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            if hasattr(module, 'apply'):
                return module
        
        return None
    
    def _apply_hook(self, hook):
        """Apply a single hook."""
        try:
            hook.apply()
        except Exception as e:
            print(f"⚠️  Hook failed: {e}")
