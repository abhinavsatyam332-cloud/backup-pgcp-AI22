@echo off
git add .
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (
  set mydate=%%c-%%a-%%b
)
git commit -m "Commit for %mydate%"
git push -u origin main
pause