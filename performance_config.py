#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Performance Configuration
=========================================
Performance settings and optimization configurations for Master Search.

Developer: Loony2392
Company: LOONY-TECH
Email: info@loony-tech.de
"""

import os
import threading
import multiprocessing
from typing import Dict, Any


class PerformanceConfig:
    """Performance configuration manager for Master Search."""
    
    def __init__(self):
        """Initialize performance configuration."""
        self._config = self._get_default_config()
        self._lock = threading.Lock()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default performance configuration."""
        cpu_count = multiprocessing.cpu_count()
        
        return {
            # Threading configuration
            'max_workers': min(cpu_count * 2, 16),
            'io_workers': min(cpu_count, 8),
            'search_workers': min(cpu_count, 6),
            
            # Memory management
            'max_memory_mb': 512,
            'chunk_size': 8192,
            'buffer_size': 65536,
            
            # Search optimization
            'max_file_size_mb': 100,
            'enable_binary_skip': True,
            'enable_encoding_detection': True,
            'max_results_per_file': 1000,
            
            # Cache settings
            'enable_cache': True,
            'cache_size_mb': 64,
            'cache_ttl_seconds': 300,
            
            # GUI performance
            'animation_fps': 60,
            'ui_update_interval_ms': 16,
            'progress_update_interval_ms': 100,
            
            # File system optimization
            'enable_parallel_scanning': True,
            'max_scan_depth': 50,
            'skip_system_directories': True,
        }
    
    def get(self, key: str, default=None) -> Any:
        """Get configuration value."""
        with self._lock:
            return self._config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value."""
        with self._lock:
            self._config[key] = value
    
    def get_all(self) -> Dict[str, Any]:
        """Get all configuration values."""
        with self._lock:
            return self._config.copy()
    
    def update(self, config: Dict[str, Any]) -> None:
        """Update configuration with new values."""
        with self._lock:
            self._config.update(config)
    
    def reset_to_defaults(self) -> None:
        """Reset configuration to default values."""
        with self._lock:
            self._config = self._get_default_config()
    
    def optimize_for_system(self) -> None:
        """Optimize configuration for current system."""
        cpu_count = multiprocessing.cpu_count()
        
        # Adjust for low-end systems
        if cpu_count <= 2:
            self.update({
                'max_workers': 2,
                'io_workers': 1,
                'search_workers': 1,
                'animation_fps': 30,
                'enable_cache': False,
            })
        # Adjust for high-end systems
        elif cpu_count >= 8:
            self.update({
                'max_workers': min(cpu_count * 2, 32),
                'io_workers': min(cpu_count, 12),
                'search_workers': min(cpu_count, 10),
                'cache_size_mb': 128,
            })


# Global performance configuration instance
_performance_config = PerformanceConfig()


def get_performance_config() -> PerformanceConfig:
    """Get the global performance configuration instance."""
    return _performance_config


def optimize_performance():
    """Optimize performance for current system."""
    _performance_config.optimize_for_system()


# Performance utility functions
def get_max_workers() -> int:
    """Get maximum number of worker threads."""
    return _performance_config.get('max_workers', 4)


def get_io_workers() -> int:
    """Get number of I/O worker threads."""
    return _performance_config.get('io_workers', 2)


def get_search_workers() -> int:
    """Get number of search worker threads."""
    return _performance_config.get('search_workers', 2)


def get_chunk_size() -> int:
    """Get file reading chunk size."""
    return _performance_config.get('chunk_size', 8192)


def get_buffer_size() -> int:
    """Get buffer size for file operations."""
    return _performance_config.get('buffer_size', 65536)


def get_max_file_size() -> int:
    """Get maximum file size in MB for searching."""
    return _performance_config.get('max_file_size_mb', 100)


def should_skip_binary_files() -> bool:
    """Check if binary files should be skipped."""
    return _performance_config.get('enable_binary_skip', True)


def should_detect_encoding() -> bool:
    """Check if encoding detection is enabled."""
    return _performance_config.get('enable_encoding_detection', True)


def get_animation_fps() -> int:
    """Get animation FPS for GUI."""
    return _performance_config.get('animation_fps', 60)


def get_ui_update_interval() -> int:
    """Get UI update interval in milliseconds."""
    return _performance_config.get('ui_update_interval_ms', 16)


if __name__ == "__main__":
    # Test performance configuration
    config = get_performance_config()
    print("Performance Configuration:")
    for key, value in config.get_all().items():
        print(f"  {key}: {value}")
    
    print("\nOptimizing for system...")
    optimize_performance()
    
    print("\nOptimized Configuration:")
    for key, value in config.get_all().items():
        print(f"  {key}: {value}")