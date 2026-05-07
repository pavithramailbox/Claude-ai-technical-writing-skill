
import zipfile, os

base = '/home/user/output/tech-writing-skill-v3'
zip_path = '/home/user/output/writing-technical-docs-skill.zip'

# Copy customizer.html from v2 into v3
import shutil
shutil.copy('/home/user/output/tech-writing-skill-v2/customizer.html', f'{base}/customizer.html')

# Build zip
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(base):
        for file in sorted(files):
            full_path = os.path.join(root, file)
            arcname = os.path.relpath(full_path, os.path.dirname(base))
            zf.write(full_path, arcname)

# Verify contents
print("📦 writing-technical-docs-skill.zip")
print(f"   Size: {os.path.getsize(zip_path)/1024:.1f} KB\n")
print("Contents:")
with zipfile.ZipFile(zip_path) as zf:
    for info in zf.infolist():
        print(f"  {info.filename:55s} {info.file_size/1024:6.1f} KB")
