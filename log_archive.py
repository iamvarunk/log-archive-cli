#!/usr/bin/env python3

import sys
import os
from datetime import datetime
import tarfile

# Check argument count
if len(sys.argv) != 2:
    print("Usage: log-archive <log-directory>")
    sys.exit(1)

log_dir = sys.argv[1]

# Check if path exists
if not os.path.exists(log_dir):
    print("Error: Directory does not exist")
    sys.exit(1)

# Check if it is a directory
if not os.path.isdir(log_dir):
    print("Error: Path is not a directory")
    sys.exit(1)

print("Valid log directory:", log_dir)

# Generate timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
print("Timestamp:", timestamp)

# Archive Name
archive_name = f"logs_archive_{timestamp}.tar.gz"
print("Archive name:", archive_name)

# Create archive directory
archive_dir = "log_archives"
os.makedirs(archive_dir, exist_ok=True)
print("Archive directory ready:", archive_dir)

# Create archive path
archive_path = os.path.join(archive_dir, archive_name)

# Compress the log directory
with tarfile.open(archive_path, "w:gz") as tar:
    tar.add(log_dir, arcname=os.path.basename(log_dir))

print("Logs archived at:", archive_path)

# Log archive details
log_file = "archive.log"

with open(log_file, "a") as f:
    f.write(
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
        f"Archived {log_dir} -> {archive_path}\n"
    )

print("Archive history updated")
