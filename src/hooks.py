"""
Self-Improving Claw - Hooks Manager Module

Supports:
- onSessionEnd: Triggered when session ends
- onError: Triggered when error occurs
- onRecovery: Triggered when recovery from error
- onPerformanceMetric: Triggered when performance metric is collected
"""

import os
import json
import traceback
from pathlib import Path
from typing import List, Dict, Any, Optional
import importlib.util


class HookManager:
    """Manager for loading and applying improvement hooks."""
    
    def __init__(self, workspace: Optional[Path] = None):
        """
        Initialize HookManager.
        
        Args:
            workspace: Path to workspace directory. If None, uses default location.
        """
        if workspace is None:
            # Use environment variable or default to current directory
            workspace_str = os.getenv('SELF_IMPROVING_WORKSPACE')
            if workspace_str:
                self.workspace = Path(workspace_str)
            else:
                self.workspace = Path.cwd()
        else:
            self.workspace = workspace
            
        self.hooks_path = self.workspace / 'hooks'
        self.learnings_path = self.workspace / 'learnings'
        
        # Ensure directories exist
        self.hooks_path.mkdir(parents=True, exist_ok=True)
        self.learnings_path.mkdir(parents=True, exist_ok=True)
        
        self.loaded_hooks = []
        
    def initialize(self):
        """Initialize and load all hooks."""
        self.loaded_hooks = self._load_hooks()
        
    def _load_hooks(self) -> List[Any]:
        """Load all hooks from the hooks directory."""
        hooks = []
        
        if not self.hooks_path.exists():
            return hooks
            
        for hook_file in self.hooks_path.glob('*.py'):
            if hook_file.name.startswith('_'):
                continue
                
            hook = self._load_hook(hook_file)
            if hook:
                hooks.append(hook)
        
        return hooks
    
    def _load_hook(self, hook_file: Path) -> Optional[Any]:
        """Load a single hook from file."""
        try:
            spec = importlib.util.spec_from_file_location(
                hook_file.stem,
                hook_file
            )
            
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return module
        except Exception as e:
            print(f"⚠️ Failed to load hook {hook_file}: {e}")
        
        return None
    
    def apply_all(self):
        """Apply all available hooks."""
        for hook in self.loaded_hooks:
            self._apply_hook(hook)
    
    def _apply_hook(self, hook):
        """Apply a single hook."""
        try:
            if hasattr(hook, 'apply'):
                hook.apply()
        except Exception as e:
            print(f"⚠️ Hook apply failed: {e}")
    
    def trigger_session_end(self, session: Any = None):
        """Trigger session end hooks for learning."""
        for hook in self.loaded_hooks:
            try:
                if hasattr(hook, 'onSessionEnd'):
                    hook.onSessionEnd(session)
            except Exception as e:
                print(f"⚠️ Session end hook failed: {e}")
    
    def trigger_error(self, error: Exception):
        """Trigger error hooks for learning from mistakes."""
        for hook in self.loaded_hooks:
            try:
                if hasattr(hook, 'onError'):
                    hook.onError(error)
            except Exception as e:
                print(f"⚠️ Error hook failed: {e}")
    
    def trigger_recovery(self):
        """Trigger recovery hooks for learning from recovery."""
        for hook in self.loaded_hooks:
            try:
                if hasattr(hook, 'onRecovery'):
                    hook.onRecovery()
            except Exception as e:
                print(f"⚠️ Recovery hook failed: {e}")
    
    def trigger_performance_metric(self, metric: Any):
        """Trigger performance metric hooks."""
        for hook in self.loaded_hooks:
            try:
                if hasattr(hook, 'onPerformanceMetric'):
                    hook.onPerformanceMetric(metric)
            except Exception as e:
                print(f"⚠️ Performance hook failed: {e}")


# Global hook manager instance
_hook_manager: Optional[HookManager] = None


def get_hook_manager(workspace: Optional[Path] = None) -> HookManager:
    """Get or create the global hook manager."""
    global _hook_manager
    
    if _hook_manager is None:
        _hook_manager = HookManager(workspace)
        _hook_manager.initialize()
    
    return _hook_manager


# Convenience functions for direct use
def on_session_end(session=None):
    """Convenience function to trigger session end."""
    get_hook_manager().trigger_session_end(session)


def on_error(error):
    """Convenience function to trigger error."""
    get_hook_manager().trigger_error(error)


def on_recovery():
    """Convenience function to trigger recovery."""
    get_hook_manager().trigger_recovery()


def on_performance_metric(metric):
    """Convenience function to trigger performance metric."""
    get_hook_manager().trigger_performance_metric(metric)
