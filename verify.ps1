Write-Host "Running tests..."
python -m pytest -v

Write-Host ""
Write-Host "Checking required files..."

if (Test-Path "requirements.txt") {
    Write-Host "requirements.txt found."
}
else {
    Write-Host "requirements.txt is missing."
}

if (Test-Path "config.json") {
    Write-Host "config.json found."
}
else {
    Write-Host "config.json is missing."
}

if (Test-Path "tasks.csv") {
    Write-Host "tasks.csv found."
}
else {
    Write-Host "tasks.csv is missing."
}

Write-Host ""
Write-Host "Checking Git status..."
git status --short
