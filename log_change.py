#!/usr/bin/env python3
import sys,os
from datetime import datetime
if len(sys.argv)<3:
    print(f"Usage: {sys.argv[0]} <id> <change>", file=sys.stderr, flush=True)
    sys.exit(1)
now=datetime.now().astimezone()
timestamp=now.strftime("%Y.%m.%d-%H.%M.%S%z")
entry_id=sys.argv[1]
change=" ".join(sys.argv[2:])
write_header=False
if not os.path.exists("changelog.md"):
    write_header=True
else:
    try:
        with open("changelog.md","r",encoding="utf-8") as file:
            line=file.readline().rstrip("\r\n")
            if line!="# Changelog":
                print("Error: changelog.md is not a valid changelog file",file=sys.stderr)
                response=input("Create/overwrite changelog.md file? (y/n): ")
                if response.lower()=="y":
                    write_header=True
                else:
                    print("Aborting", file=sys.stderr)
                    sys.exit(1)
    except OSError:
        write_header=True
if write_header:
    try:
        with open("changelog.md", "w", encoding="utf-8") as file:
            file.write("# Changelog\n")
    except OSError:
        print("Error: Could not create changelog.md", file=sys.stderr)
        sys.exit(1)
try:
    with open("changelog.md", "a", encoding="utf-8") as file:
        print(f"{entry_id}-{timestamp}: {change}", flush=True)
        file.write(f" - {entry_id}-{timestamp}: {change}\n")
except OSError:
    print("Error: Could not open changelog.md", file=sys.stderr)
    sys.exit(1)
sys.exit(0)