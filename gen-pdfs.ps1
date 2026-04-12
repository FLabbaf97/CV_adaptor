# 1. Find all .tex files recursively (excluding anything already in a build folder to avoid loops)
$texFiles = Get-ChildItem -Filter "*.tex" -Recurse | Where-Object { $_.FullName -notmatch "\\build\\" }

foreach ($texFile in $texFiles) {
    # Define the directory where the .tex file lives
    $sourceDir = $texFile.DirectoryName
    # Define the build directory path
    $buildDir = Join-Path -Path $sourceDir -ChildPath "build"
    
    # Expected PDF path
    $pdfName = $texFile.BaseName + ".pdf"
    $pdfPath = Join-Path -Path $buildDir -ChildPath $pdfName

    # Check if we need to build
    $shouldBuild = $true
    if (Test-Path -Path $pdfPath) {
        $texTime = $texFile.LastWriteTime
        $pdfTime = (Get-Item $pdfPath).LastWriteTime
        
        if ($pdfTime -gt $texTime) {
            Write-Host "Skipping $($texFile.Name): Build is already up to date." -ForegroundColor Gray
            $shouldBuild = $false
        }
    }

    if ($shouldBuild) {
        # 2. Ensure the build directory exists
        if (-not (Test-Path -Path $buildDir)) {
            New-Item -ItemType Directory -Path $buildDir | Out-Null
            Write-Host "Created build directory at: $buildDir" -ForegroundColor Cyan
        }

        Write-Host "Building: $($texFile.Name)..." -ForegroundColor Yellow

        # 3. Run pdflatex
        # -output-directory: redirects all aux and pdf files to the build folder
        # -interaction=nonstopmode: prevents the script from hanging on errors
        pdflatex -interaction=nonstopmode -output-directory="$buildDir" "$($texFile.FullName)"

        # Check if the build was successful by looking for the PDF
        if (Test-Path -Path $pdfPath) {
            Write-Host "Success! Moving $pdfName to $sourceDir" -ForegroundColor Green
            
            # 4. Copy the PDF to the parent of the build folder (the source directory)
            Copy-Item -Path $pdfPath -Destination $sourceDir -Force
        } else {
            Write-Warning "Failed to generate PDF for $($texFile.Name). Check LaTeX logs in the build folder."
        }
    }
}

Write-Host "Process complete." -ForegroundColor Green