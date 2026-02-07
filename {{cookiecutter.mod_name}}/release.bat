{%if(cookiecutter.project_type == 'XML only')%}@ECHO OFF
ECHO Packaging {{cookiecutter.mod_name}} {{cookiecutter.mod_ver}} - Started

SET "RELEASE_DIR=Release"
SET "ZIP_FILE={{cookiecutter.mod_name.replace(' ', '_')}}.zip"

IF EXIST "%RELEASE_DIR%" RMDIR /S /Q "%RELEASE_DIR%"
IF EXIST "%ZIP_FILE%" DEL /Q "%ZIP_FILE%"

MKDIR "%RELEASE_DIR%"
XCOPY "About" "%RELEASE_DIR%\About\" /E /I /Q /Y
XCOPY "Common" "%RELEASE_DIR%\Common\" /E /I /Q /Y
XCOPY "{{cookiecutter.mod_ver}}" "%RELEASE_DIR%\{{cookiecutter.mod_ver}}\" /E /I /Q /Y
{%if(cookiecutter.compat == 'y')%}IF EXIST "Compatibility" XCOPY "Compatibility" "%RELEASE_DIR%\Compatibility\" /E /I /Q /Y
{%endif%}IF EXIST "loadFolders.xml" COPY /Y "loadFolders.xml" "%RELEASE_DIR%\"
IF EXIST "LICENSE" COPY /Y "LICENSE" "%RELEASE_DIR%\"
IF EXIST "README.md" COPY /Y "README.md" "%RELEASE_DIR%\"
{%if(cookiecutter.continuity != 'None')%}IF EXIST "CONTINUITY.md" COPY /Y "CONTINUITY.md" "%RELEASE_DIR%\"
{%endif%}
powershell -Command "Compress-Archive -Path '%RELEASE_DIR%\*' -DestinationPath '%ZIP_FILE%' -Force"

ECHO Packaging {{cookiecutter.mod_name}} {{cookiecutter.mod_ver}} - Complete
ECHO Press any key to exit...
PAUSE > NUL
{%else%}@ECHO OFF
ECHO Building {{cookiecutter.mod_name}} {{cookiecutter.mod_ver}} - Started

dotnet --list-sdks | findstr /R /C:"8\..*" 1>nul
if %errorlevel% neq 0 (
    ECHO .NET 8 SDK not found. Please install it using the following command:
    ECHO winget install Microsoft.DotNet.SDK.8
    PAUSE > NUL
    EXIT /B
)

@ECHO ON
dotnet restore {{cookiecutter.mod_ver}}/Source/{{cookiecutter.mod_name.replace(' ', '_')}}.sln
dotnet build {{cookiecutter.mod_ver}}/Source/{{cookiecutter.mod_name.replace(' ', '_')}}.sln /p:Configuration=Release
@ECHO OFF
ECHO Building {{cookiecutter.mod_name}} {{cookiecutter.mod_ver}} - Complete
ECHO Press any key to exit...
PAUSE > NUL
{%endif%}