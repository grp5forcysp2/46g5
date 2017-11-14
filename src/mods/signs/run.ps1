Get-childItem $env:temp | foreach { get-filehash $env:temp\$_ -Algorithm MD5}
