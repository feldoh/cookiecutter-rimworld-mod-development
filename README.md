# cookiecutter-rimworld-mod-development
A cookiecutter project that builds the basic Rimworld mod development file structure and sets up a sane build environment.

# Table of Contents  
- [Install/Setup](#installsetup)
  - [Windows Command Prompt](#windows-command-prompt)
    - [Required Programs](#required-programs)
    - [Usage](#usage-inside-rimworldmods-folder)
  - [Microsoft Visual Studio Integration](#microsoft-visual-studio-integration)
    - [Required Programs](#required-programs-1)
    - [Usage](#usage)
- [Basic Features](#basic-features)
  - [Folder Structure](#folder-structure)
  - [VS Setup Automation](#vs-setup-automation)


# Install/Setup
### Usage from Windows Command Prompt
##### Required Programs
- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/downloads/)
- [cookiecutter](https://github.com/audreyr/cookiecutter) (or `pip install cookiecutter`)
  - Recommend cookiecutter 2.0+ (`pip install cookiecutter>=2`). On older versions (1.x), you will be prompted for `_visual_studio` — just type `{}` and press Enter.

##### Usage (inside Rimworld/Mods folder)
1. `cookiecutter https://github.com/feldoh/cookiecutter-rimworld-mod-development`
2. `[Answer the prompts]`
3. Open the folder you just created and double-click the `ModName.sln` file
4. In the Solution Explorer view on the right, right click `RimWorldWin` and click `Set as Startup Project`
    
### Usage from Microsoft Visual Studio
##### Required Programs

- [Visual Studio Community](https://www.visualstudio.com/downloads/)

##### Install (if no `File -> New -> From Cookiecutter...` option is available)
1. Open up VS Installer (In Visual Studio -> Tools -> Gets Tools and Features)
2. Click Modify
3. Click Individual Components
4. Scroll to Development activities
5. Click the Cookiecutter template support checkbox
6. Click Modify

##### Usage
1. Open Visual Studio
2. `File -> New -> From Cookiecutter...`
3. Search for `rimworld`
4. Double-click `feldoh/cookiecutter-rimworld-mod-development`
5. Change the Template Options:
   - `Create To` => `[...]/RimWorld/Mods`
   - `Mod name`
   - `Author` (Use your Steam username for automatic linking of mod to profile) (can change later in About-Release.xml)
   - `Mod Description` (not required, can change later in About-Release.xml)
   - A few more options are available
6. `Create and Open Project`


# Basic Features
### Folder Structure
This cookiecutter builds the entire standard mod folder structure, with empty folders as the default. `namespace_name` is automatically calculated.
- {{cookiecutter.mod_name}}
  - About
    - About.xml
    - Preview.png
  - 1.X
    - Assemblies
    - Defs
    - Patches
    - Source
      - `namespace_name`
        - Properties
          - AssemblyInfo.cs
        - Settings.cs
        - `namespace_nameMod.cs`
        - `namespace_nameDefOf.cs`
        - `namespace_name.csproj`
      - `namespace_name.sln`
  - Common
    - Languages
      - English
        - Keyed
          - `namespace_name_Misc_Gameplay.xml`
    - Sounds
    - Textures
  - CONTINUITY.md
  - README.md
  - LICENSE
  - .gitignore
  - .gitattributes
  - .editorconfig

Note that samples demonstrating use of MayRequire and Loadfolders use Royalty as an example, simply swap this out as you need.

### Preview images
A preview image Asset is provided as a [Krita file](Assets/Preview.kra) you may wish to use [Krita](https://krita.org/) which is a free art tool or something else.
The template provided uses the [Rimworld Font](https://github.com/spdskatr/RWModdingResources/raw/master/RimWordFont.ttf) from Marnador.
Make sure to export as a png file and place the Preview.png in About/Preview.png

### VS Setup Automation
- Links Rimworld and UnityEngine .dlls for importing in code
- Sets build events to automate file management of About-$Version.xml for tagging development versions.
- Clears the default set trace constant
- Creates a VS solution with correctly defined paths
- Clicking `Start ▶️` will preform the designated build sequence and start Rimworld.exe tied to a Visual Studio resource monitor.

# Issues
### The imported project "C:\Program Files (x86)\...\Microsoft.CSharp.Core.targets" was not found
If you're not using Visual Studio you may need to tell the project where your MS Build actually is.
- You can download MSBuild from [Microsoft](https://dotnet.microsoft.com/en-us/download/dotnet-framework/thank-you/net472-developer-pack-offline-installer)
- It will already be in your Rider directory and can be found under File -> Settings -> Build, Execution, Deployment -> Toolset and Build -> MSBuild Version

### Cannot Resolve Symbol HarmonyLib (`using HarmonyLib` is red)
Run `dotnet restore` on the .csproj file for your code then try re-doing the nuget restore.

# Thanks
* alextd and n-fisher for the prior version of this template
* Marnador for the [Rimworld Font](https://github.com/spdskatr/RWModdingResources/raw/master/RimWordFont.ttf)
