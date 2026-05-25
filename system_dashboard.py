import os
import shutil
import platform
from datetime import datetime

print("=" * 50)
print("🔥 SUPERGEEK SYSTEM DASHBOARD 😎🔥")
print("=" * 50)

print(f"\n🖥️ Operating System: {platform.system()}")
print(f"💻 Hostname: {platform.node()}")
print(f"⚙️ Processor: {platform.processor()}")
print(f"🕒 Current Time: {datetime.now()}")

total, used, free = shutil.disk_usage("/")

print("\n📦 DISK USAGE")
print(f"Total: {total // (2**30)} GB")
print(f"Used:  {used // (2**30)} GB")
print(f"Free:  {free // (2**30)} GB")

print("\n🌐 NETWORK TEST")
response = os.system("ping -c 1 google.com > /dev/null 2>&1")

if response == 0:
    print("✅ Internet Connection: ACTIVE")
else:
    print("❌ Internet Connection: DOWN")

print("\n🐳 DOCKER STATUS")
docker = os.system("docker --version > /dev/null 2>&1")

if docker == 0:
    print("✅ Docker: INSTALLED")
else:
    print("❌ Docker: NOT FOUND")

print("\n🔥 SUPERGEEK ACTIVAO COMPLETE 🔥")