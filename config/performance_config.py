# Master Search - Performance Configuration
# =========================================
# Configuration file for performance optimizations
# Author: Loony2392
# Email: info@loony-tech.de

# Performance-Einstellungen
# =========================

# Multiprocessing Einstellungen
# ------------------------------
USE_MULTIPROCESSING = True          # Aktiviert Multiprocessing für CPU-intensive Aufgaben
USE_THREADING = True                # Aktiviert Threading für I/O-intensive Aufgaben
AUTO_WORKER_COUNT = True            # Automatische Erkennung der optimalen Worker-Anzahl
# Voreinstellung: 4 Kerne für die Vorauswahl (gute Balance für Desktop-Rechner)
MANUAL_WORKER_COUNT = 4             # Manuelle Worker-Anzahl (nur wenn AUTO_WORKER_COUNT = False)

# Batch-Verarbeitung
# ------------------
CHUNK_SIZE = 100                    # Number of files per worker batch
MIN_BATCH_SIZE = 50                 # Minimum Batch-Größe für Multiprocessing
MAX_BATCHES = 100                   # Maximum Anzahl Batches

# File filter
# ------------
MAX_FILE_SIZE_MB = 50               # Maximum file size in MB
SKIP_BINARY_FILES = True            # Skip binary files automatically
SKIP_LARGE_FILES = True             # Skip files over MAX_FILE_SIZE_MB

# Memory Management
# -----------------
MAX_MEMORY_USAGE_PERCENT = 80       # Maximum RAM-Nutzung in Prozent
MEMORY_CHECK_INTERVAL = 100         # Check RAM usage every N files

# I/O Optimierungen
# -----------------
USE_FAST_SCAN = True                # Schneller Directory-Scan
BUFFER_SIZE = 8192                  # Buffer size for file reading in bytes
MAX_LINE_LENGTH = 10000             # Maximum line length for text files

# Progress Reporting
# ------------------
PROGRESS_UPDATE_INTERVAL = 50       # Show progress every N files
DETAILED_STATS = True               # Zeige detaillierte Statistiken
SHOW_SYSTEM_STATS = True            # Zeige System-Auslastung (benötigt psutil)

# Encoding Detection
# ------------------
ENCODING_ATTEMPTS = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1', 'utf-16']
MAX_ENCODING_ATTEMPTS = 3           # Maximum number of encoding attempts per file
FAST_ENCODING_DETECTION = True      # Use fast encoding detection

# Error Handling
# --------------
CONTINUE_ON_ERROR = True            # Continue on file access errors
LOG_ERRORS = False                  # Logge Fehler (kann Performance beeinträchtigen)
MAX_ERRORS_PER_BATCH = 10           # Maximum Fehler pro Batch bevor Abbruch

# Advanced Features (Experimental)
# ================================

# Memory Mapping
USE_MEMORY_MAPPING = False          # Using Memory-Mapped Files (experimental)
MMAP_THRESHOLD_MB = 10              # Schwellenwert für Memory Mapping

# Caching
USE_FILE_CACHE = False              # Cache Datei-Metadaten (experimental)
CACHE_SIZE = 1000                   # Maximum Cache-Einträge

# Parallel Directory Walking
PARALLEL_DIRECTORY_WALK = False     # Paralleles Durchlaufen der Verzeichnisse (experimental)

# Performance Profiling
ENABLE_PROFILING = False            # Aktiviert Performance-Profiling
PROFILE_OUTPUT_FILE = "performance_profile.txt"

# Notes:
# ======
# 1. Diese Einstellungen können die Performance erheblich beeinflussen
# 2. Experimentelle Features sind möglicherweise instabil
# 3. Zu viele Worker können die Performance verschlechtern
# 4. Bei SSDs können höhere CHUNK_SIZE Werte besser sein
# 5. Bei HDDs sollten kleinere Batch-Größen verwendet werden
# 6. Passen Sie die Einstellungen an Ihr System an