import os
import shutil
import subprocess
import uuid
from datetime import datetime

#About is always made
os.makedirs("{{cookiecutter.mod_ver}}/Defs", exist_ok=True)
os.makedirs("{{cookiecutter.mod_ver}}/Patches", exist_ok=True)
os.makedirs("{{cookiecutter.mod_ver}}/Assemblies", exist_ok=True)
os.makedirs("Common/Languages", exist_ok=True)
os.makedirs("Common/Sounds", exist_ok=True)
os.makedirs("Common/Textures", exist_ok=True)

if not "{{cookiecutter.compat}}" == "y":
    shutil.rmtree("Compatibility", ignore_errors=True)

# Generate unique GUIDs and set current copyright year
PROJECT_GUID_PLACEHOLDER = "d7d21b4a-1da7-41d8-b202-c58ca8fa62aa"
SOLUTION_GUID_PLACEHOLDER = "28CF9A73-5333-4EB3-BFCC-3FBEDDA19200"
project_guid = str(uuid.uuid4())
solution_guid = str(uuid.uuid4()).upper()
current_year = str(datetime.now().year)

namespace = "{{cookiecutter.mod_name.replace(' ', '_')}}"
mod_ver = "{{cookiecutter.mod_ver}}"

assembly_info_path = os.path.join(mod_ver, "Source", namespace, "Properties", "AssemblyInfo.cs")
if os.path.exists(assembly_info_path):
    with open(assembly_info_path, "r", encoding="utf-8-sig") as f:
        content = f.read()
    content = content.replace(PROJECT_GUID_PLACEHOLDER, project_guid)
    content = content.replace("Copyright ©  2024", f"Copyright ©  {current_year}")
    with open(assembly_info_path, "w", encoding="utf-8-sig") as f:
        f.write(content)

sln_path = os.path.join(mod_ver, "Source", f"{namespace}.sln")
if os.path.exists(sln_path):
    with open(sln_path, "r", encoding="utf-8-sig") as f:
        content = f.read()
    content = content.replace(PROJECT_GUID_PLACEHOLDER.upper(), project_guid.upper())
    content = content.replace(PROJECT_GUID_PLACEHOLDER, project_guid)
    content = content.replace(SOLUTION_GUID_PLACEHOLDER, solution_guid)
    with open(sln_path, "w", encoding="utf-8-sig") as f:
        f.write(content)

# Check if git binary is available
git_path = shutil.which('git')
if git_path is not None:
    # Initialize a Git repository in the current directory
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Cookie cutter initial commit'])
else:
    print("Git binary not found. Skipping git initialisation.")
