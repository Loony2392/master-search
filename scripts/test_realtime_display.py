#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick test to verify real-time display feature works correctly
"""

import sys
import os
import time
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from file_search_tool import FileSearchTool
from queue import Queue

def test_callback_mechanism():
    """Test that FileSearchTool can send real-time updates via callback"""
    print("🧪 Testing Real-Time Status Callback Mechanism...\n")
    
    # Create a test queue to capture status updates
    status_updates = []
    
    def capture_status(status_data):
        """Capture status updates"""
        status_updates.append(status_data)
        if status_data.get('type') == 'progress':
            processed = status_data.get('processed', 0)
            total = status_data.get('total', 0)
            matches = status_data.get('matches', 0)
            percent = status_data.get('percent', 0)
            print(f"  Progress: {processed:,}/{total:,} files | {matches:,} matches | {percent:.1f}% complete")
        elif status_data.get('type') == 'complete':
            total = status_data.get('total', 0)
            matches = status_data.get('matches', 0)
            elapsed = status_data.get('elapsed_time', 0)
            speed = status_data.get('speed', 0)
            print(f"  ✅ Search Complete: {total:,} files scanned, {matches:,} matches found in {elapsed:.2f}s ({speed:.0f} files/sec)\n")
    
    # Create search tool
    search_tool = FileSearchTool(verbose=False)
    search_tool.search_path = str(Path.cwd())  # Search current directory
    search_tool.search_terms = ["test"]
    search_tool.search_mode = "any"
    search_tool.case_sensitive = False
    search_tool.use_regex = False
    search_tool.max_workers = 2
    search_tool.use_multiprocessing = False
    
    # Attach callback
    search_tool.status_callback = capture_status
    
    # Run search
    print(f"📂 Searching: {search_tool.search_path}")
    print(f"🔍 Term: {search_tool.search_terms[0]}\n")
    
    try:
        search_tool.search_files_and_folders()
    except Exception as e:
        print(f"❌ Error during search: {e}")
        return False
    
    # Verify we received updates
    if len(status_updates) == 0:
        print("❌ No status updates received!")
        return False
    
    progress_updates = [u for u in status_updates if u.get('type') == 'progress']
    complete_updates = [u for u in status_updates if u.get('type') == 'complete']
    
    print(f"📊 Status Updates Received:")
    print(f"   ✅ Progress updates: {len(progress_updates)}")
    print(f"   ✅ Complete updates: {len(complete_updates)}")
    print(f"   ✅ Total updates: {len(status_updates)}")
    
    if len(complete_updates) > 0:
        final = complete_updates[-1]
        print(f"\n✅ Final statistics:")
        print(f"   Total files: {final.get('total', 0):,}")
        print(f"   Matches: {final.get('matches', 0):,}")
        print(f"   Time: {final.get('elapsed_time', 0):.2f}s")
        print(f"   Speed: {final.get('speed', 0):.0f} files/sec")
    
    return len(status_updates) > 0

if __name__ == "__main__":
    print("=" * 60)
    print("Real-Time Display Feature Test")
    print("=" * 60 + "\n")
    
    success = test_callback_mechanism()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ All Tests Passed!")
    else:
        print("❌ Tests Failed!")
    print("=" * 60)
    
    sys.exit(0 if success else 1)
