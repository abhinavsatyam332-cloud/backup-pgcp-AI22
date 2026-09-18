@echo off
setlocal enabledelayedexpansion

:: 1. Clear any stale Git lock file to prevent freezes
if exist ".git\index.lock" del /f /q ".git\index.lock"

:: 2. Ensure .gitignore exists
if not exist ".gitignore" type nul > .gitignore

:: 3. Find files > 100 MB (excluding .git folder), append to .gitignore, and untrack them
powershell -Command "$gi = [System.IO.File]::ReadAllText((Resolve-Path .gitignore)); Get-ChildItem -Recurse -File | Where-Object { $_.FullName -notmatch '\\\.git\\' -and $_.Length -gt 104857600 } | ForEach-Object { $rel = ((Get-Item $_.FullName | Resolve-Path -Relative) -replace '^\.\\', '') -replace '\\', '/'; if (-not $gi.Contains($rel)) { Add-Content -Path .gitignore -Value $rel; Write-Host \"Auto-ignored large file: $rel\" }; git rm --cached -f \"$rel\" 2>$null }"

:: 4. Stage all files (Git will naturally skip the large files we just added to .gitignore)
git add .

:: 5. Format current date for the commit message
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (
  set mydate=%%c-%%a-%%b
)

:: 6. Commit and push
git commit -m "Auto-backup %mydate%"
git push -u origin main

echo.
echo Backup Complete!
pause