$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
$env:PYTHONUTF8 = "1"

# 过滤日志。把DEBUG INFO类型的日志给过滤掉。保留WARING ERROR CRITICAL
$env:LOG_LEVEL = "WARNING"
$pythonExe = "D:\AAADownload\pAnaconda\install_path\envs\langgraph-dev\python.exe"
if (-not (Test-Path -LiteralPath $pythonExe)) {
    throw "langgraph-dev Python not found: $pythonExe"
}
# & $pythonExe -m langgraph_cli dev --config langgraph.local.json --host 127.0.0.1 --port 2024 --allow-blocking --no-browser
& $pythonExe -m langgraph_cli dev --config langgraph.local.json --host 127.0.0.1 --port 2024 --allow-blocking --no-browser --server-log-level WARNING