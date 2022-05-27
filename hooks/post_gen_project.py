import os
import shutil

#About is always made
os.makedirs("{{cookiecutter.mod_ver}}/Defs", exist_ok=True)
os.makedirs("{{cookiecutter.mod_ver}}/Patches", exist_ok=True)
os.makedirs("Common/Languages", exist_ok=True)
os.makedirs("Common/Sounds", exist_ok=True)
os.makedirs("Common/Textures", exist_ok=True)

if os.path.exists("{{cookiecutter.mod_ver}}/Source/.run"):
    os.makedirs("{{cookiecutter.mod_ver}}/Source/.idea", exist_ok=True)
    shutil.move("{{cookiecutter.mod_ver}}/Source/.idea.{{cookiecutter.mod_name}}", "{{cookiecutter.mod_ver}}/Source/.idea")
else:
    shutil.rmtree("{{cookiecutter.mod_ver}}/Source/.norun", ignore_errors=False, onerror=None)
    shutil.rmtree("{{cookiecutter.mod_ver}}/Source/.idea.{{cookiecutter.mod_name}}", ignore_errors=False, onerror=None)
