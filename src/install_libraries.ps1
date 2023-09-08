# Verifica se lo script viene eseguito con privilegi amministrativi
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    # Se non hai i privilegi di amministratore, avvia uno nuovo processo PowerShell come amministratore
    Start-Process powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    # Esci dallo script corrente
    Exit
}

# Il resto dello script continua qui
# Imposta la politica di esecuzione per consentire lo scripting
Set-ExecutionPolicy Bypass -Scope Process -Force

# Scarica ed esegui lo script di installazione di Chocolatey
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Installa i pacchetti tramite Chocolatey
choco install ffmpeg -y

# Installa le librerie
pip install -r requirements.txt
