Write-Host "<<<cobian_reflector>>>"
Select-String -path "C:\Program Files\Cobian Reflector\Logs\*.txt" -pattern "(Backing up the task)|(The Volume Shadow Copy image has been successfully created)|(The Volume Shadow Copy image has been successfully deleted)|(\*\* Backup for task .* ended)" -AllMatches | Foreach {$_.Line}
