# AGENTS.md

## 文件编码规则
- 严禁使用 PowerShell 的 `Set-Content -Encoding UTF8` 或 `Out-File -Encoding UTF8` 编辑本仓库中的任何文件，这两个命令会自动添加 UTF-8 BOM。
- 编辑文件时，使用以下方案之一写入 UTF-8 without BOM：
  - PowerShell: `$utf8 = [Text.Encoding]::UTF8; [IO.File]::WriteAllText("path", $content, $utf8)`（但需注意沙箱对覆盖旧文件的限制）
  - Python: `open("path","w",encoding="utf-8").write(content)`
  - 也可以通过 `zensical_fixed2.toml` 这类临时文件中转，再由用户手动替换
- 优先使用 `python` 进行文件写入，避免 BOM 问题。

## 配置文件特别说明
- `zensical.toml` 是 TOML 格式，解析器（tomli/tomllib）不接受 BOM。对该文件的所有编辑必须确保 UTF-8 without BOM。
