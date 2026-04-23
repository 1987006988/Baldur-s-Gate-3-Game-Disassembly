@echo off
if "%1"=="check" (
  python scripts/check_repo.py
  exit /b %ERRORLEVEL%
)
echo Supported target: check
exit /b 1
