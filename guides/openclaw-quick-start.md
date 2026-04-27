# OpenClaw Quick-Start Guide
*Get an autonomous agent running in 10 minutes*

**For:** Tim Huckaby (MVP Summit 2026)  
**Time:** 5-10 minutes  
**Companion:** [OpenClaw Deep-Dive Companion Guide](./openclaw-deep-dive-tim-huckaby.md) (30-45 min)

---

## What You're Building

A persistent AI agent that can:
- Remember conversations across sessions
- Execute tasks autonomously
- Use tools (browser, code, search)
- Coordinate multiple sub-agents

---

## Prerequisites (30 seconds)

Pick your platform and run the commands below.

**Windows (PowerShell — recommended for Surface Book 2):**
```powershell
# Install Node.js LTS from https://nodejs.org/ or via winget
winget install OpenJS.NodeJS

# Verify
node --version         # v22+ required
git --version          # install from https://git-scm.com/download/win if missing
```

**macOS / Linux:**
```bash
# macOS
brew install node git

# Ubuntu/Debian
sudo apt-get install -y nodejs git

# Verify
node --version         # v22+ required
git --version
```

**Need:**
- Windows 10/11, macOS, or Ubuntu
- Node.js 22+ and Git
- 2 GB free RAM (4 GB+ recommended on Surface Book 2 for thermal headroom)
- One API key (see API Options below)

---

## 🎣 Special Note for Tim (Surface Book 2)

The Surface Book 2 is totally fine for learning + development. Thermal throttling only shows up under *sustained* heavy AI workloads (e.g., running local LLMs for hours). For your use case — calendar coordination, content drafting, research bursts — it'll run cool and quiet. You can always migrate to a Mini PC or cloud VM later.

---
---

## Step 1: Install OpenClaw (2 minutes)

```bash
# Works on macOS, Linux, and Windows (PowerShell / WSL)
npm install -g openclaw

# Or use npx (no install)
npx openclaw --version
```

**Windows users:** If `npm` isn't found, make sure Node.js is in your PATH after the winget install above. A terminal restart usually fixes it.

Verify installation:
```bash
openclaw --version  # Should show 2026.4.x or later
```

---

## Step 2: Choose Your API (1 minute)

OpenClaw needs at least one AI provider. Pick the one that fits your setup.

### Option A: Azure OpenAI (Best for Microsoft ecosystem)
```powershell
# Windows PowerShell
$Env:AZURE_OPENAI_API_KEY = "your-azure-key"
$Env:AZURE_OPENAI_ENDPOINT = "https://your-resource.openai.azure.com/"

# Make it permanent (PowerShell profile)
[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'your-azure-key', 'User')
[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'https://your-resource.openai.azure.com/', 'User')
```

**Latency note:** Pick an Azure region close to you (East US, West Coast, etc.). Cross-region latency adds 50–150 ms per request, which you *will* notice in rapid back-and-forth conversations. If you're in Utah (or wherever you're fishing), `West US 2` or `West US 3` is typically fastest.

### Option B: Direct OpenAI
```powershell
$Env:OPENAI_API_KEY = "sk-your-key-here"
[System.Environment]::SetEnvironmentVariable('OPENAI_API_KEY', 'sk-your-key-here', 'User')
```

### Option C: Local model (Zero latency, fully offline)
Install [Ollama](https://ollama.com) and pull a small model:
```powershell
# PowerShell
winget install Ollama.Ollama
ollama pull llama3.2  # 2 GB, runs great on Surface Book 2
```
OpenClaw auto-discovers local Ollama on `http://localhost:11434`.

### Option D: Mix and match (Fallback chain)
You can configure *multiple* providers so if Azure is slow or rate-limited, OpenClaw falls back to OpenRouter (free tier) or your local Ollama. This is the recommended production setup:
```
Azure OpenAI → Direct OpenAI → Ollama (local fallback)
```

---

## Step 3: Run System Check (1 minute — new in 2026.4.x)

OpenClaw now includes a built-in doctor that validates your environment, API keys, and port availability before you start.

```powershell
# Windows PowerShell
openclaw doctor
```

Expected output: `✅ All checks passed` or a list of what needs fixing. Fix anything marked 🔴 before continuing.

---

## Step 4: Create Minimal Config (2 minutes)

**Windows PowerShell:**
```powershell
# Create config directory
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.openclaw"

# Write config (Azure OpenAI + local fallback — best for Surface / Microsoft stack)
@'
{
  "gateway": {
    "port": 18800,
    "mode": "local",
    "bind": "loopback"
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "azure/gpt-4o-mini",
        "fallbacks": ["ollama/llama3.2", "openrouter/free"]
      }
    }
  }
}
'@ | Out-File -FilePath "$env:USERPROFILE\.openclaw\openclaw.json" -Encoding utf8
```

**macOS / Linux:**
```bash
# Create config directory
mkdir -p ~/.openclaw

# Write base configuration
cat > ~/.openclaw/openclaw.json << 'EOF'
{
  "gateway": {
    "port": 18800,
    "mode": "local",
    "bind": "loopback"
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "azure/gpt-4o-mini",
        "fallbacks": ["ollama/llama3.2", "openrouter/free"]
      }
    }
  }
}
EOF

chmod 600 ~/.openclaw/openclaw.json   # Skip on Windows
```

---

## Step 4: Start the Gateway (1 minute)

```bash
# Start the daemon
openclaw gateway start

# Verify it's running
openclaw gateway status
```

You should see: `Gateway: running on port 18800`

---

## Step 5: Open the Dashboard (1 minute)

```bash
# Get the dashboard URL
openclaw dashboard --no-open
```

Open the printed URL (e.g., `http://127.0.0.1:18800/#token=...`) in your browser.

You'll see the OpenClaw Control UI — your agent is now ready.

---

## Step 6: First Test (2 minutes)

In the web UI, send your agent a message:

**You:** "Create a file called hello.txt with 'Hello from OpenClaw'"

**Expected:** Agent responds, creates the file, and confirms.

**Check it worked:**
```bash
# macOS / Linux
cat ~/.openclaw/workspace/hello.txt

# Windows PowerShell
Get-Content "$env:USERPROFILE\.openclaw\workspace\hello.txt"
```

---

## You're Done — What Now?

Your agent is running with:
- ✅ Persistent memory
- ✅ Tool access (files, browser, shell)
- ✅ Web dashboard
- ✅ Session continuity

### Quick Wins (try these now)

1. **Search the web:** "Search for best fly fishing rod reviews 2026"
2. **Run a command:** "Show me my top 10 largest files in my Documents folder"
3. **Store a memory:** "Remember that I fish the Green River in Utah every spring"
4. **Spawn a sub-agent:** "Research the best conservation nonprofits for anglers to support"

### Gotchas (read these before you hit a wall)

**🔥 #1: `npm install -g` fails on Windows with "operation not permitted"**
- Fix: Run PowerShell as Administrator, *or* use `npx openclaw` everywhere instead of installing globally.

**🔥 #2: Port 18800 is already in use**
- Windows: `netstat -ano | findstr 18800` then `taskkill /PID <PID> /F`
- macOS/Linux: `lsof -i :18800` then `kill <PID>`

**🔥 #3: API keys not picked up**
- OpenClaw reads env vars from your *shell*, not from Windows Settings. Restart your terminal after setting `$Env:` variables.
- Or use `openclaw configure` (interactive wizard) instead of manual env vars.

**🔥 #4: Azure OpenAI rate limits**
- Azure tier = "Free" or "Pay-As-You-Go" can hit 6–10 requests/minute. If your agent feels sluggish, bump to S0 tier or add `openrouter/free` as a fallback.

**🔥 #5: Windows Defender / antivirus blocks OpenClaw**
- The gateway listens on localhost (127.0.0.1) — it never listens on the internet, so it's safe. If Windows Defender prompts, allow it.

**🔥 #6: Surface Book 2 thermal throttling during heavy tasks**
- If you're running Ollama + OpenClaw + a browser + multiple tabs, the Surface Book 2 will throttle. For daily use (research bursts, calendar, email), it never gets close. Only an issue for training local LLMs or bulk video processing.

**🔥 #7: The `openclaw doctor` command**
- If the `doctor` command (Step 3) catches anything you don't understand, screenshot it and send it to me — I'll diagnose it in 30 seconds.

### Next Steps

- **Customize your agent:** Edit `~/.openclaw/openclaw.json`
- **Add skills:** Check `~/.openclaw/skills/` for 80+ built-in capabilities
- **Read the deep-dive:** [Full architecture guide](./openclaw-deep-dive-tim-huckaby.md) (30-45 min)
- **Enable Telegram/WhatsApp:** See messaging section in deep-dive
- **Set up memory:** Configure LanceDB for long-term recall

### Common Commands

```bash
# Check status
openclaw status

# View logs
openclaw gateway logs --follow

# Stop gateway
openclaw gateway stop

# Restart gateway
openclaw gateway restart

# Update OpenClaw
npm update -g openclaw
```

---

## Troubleshooting

**Gateway won't start?**
```bash
# Windows PowerShell
Get-NetTCPConnection -LocalPort 18800 | Select-Object OwningProcess
# Or
netstat -ano | findstr 18800
# Kill the process: taskkill /PID <PID> /F

# macOS / Linux
lsof -i :18800
kill <PID>
```
If nothing is using the port, just restart:
```bash
openclaw gateway stop
# Windows: remove-Item "$env:USERPROFILE\.openclaw\gateway.pid" -ErrorAction SilentlyContinue
# macOS/Linux: rm -f ~/.openclaw/gateway.pid
openclaw gateway start
```

**API key errors?**
- Verify the env var is set in your current terminal:
  - Windows: `echo $Env:AZURE_OPENAI_API_KEY`
  - macOS/Linux: `echo $AZURE_OPENAI_API_KEY`
- If empty, re-run the `$Env:` or `export` commands from Step 2
- Or use `openclaw configure` (interactive) to set credentials instead

**Agent not responding?**
- Wait 15 seconds after gateway start (first boot is slow)
- Check logs: `openclaw gateway logs --follow`
- Verify config: `openclaw config validate`
- Run `openclaw doctor` again — a system update may have changed something

**Windows: "node-gyp" build errors?**
- Run `npm install --global windows-build-tools` (PowerShell admin)
- Or use WSL2 for a Linux environment — `wsl --install` then run everything inside Ubuntu

**Latency feels high?**
- Check which provider is being used: `openclaw gateway logs --follow | grep "provider="`
- If it's Azure from a far region, expect 200–400 ms per request. Add a local Ollama model as fallback (Option C in Step 2) — Ollama is 10–30 ms because it runs on your Surface.
- OpenClaw auto-switches to the fastest available provider in your fallback chain.

---

## Production Checklist

Before deploying:

- [ ] Change default token (`dev-token-change-in-production`)
- [ ] Set strong auth in `gateway.auth.token`
- [ ] Configure allowed domains for browser
- [ ] Set up secrets in `~/.openclaw/credentials/` (not env vars)
- [ ] Review `security` section in config
- [ ] Enable memory persistence (LanceDB)
- [ ] Configure backup for `~/.openclaw/`

See [Security Considerations](./openclaw-deep-dive-tim-huckaby.md#11-security-considerations) in the deep-dive guide.

---

## Summary

**What you built:** A persistent AI agent with memory, tools, and multi-agent capabilities.

**Time invested:** ~10 minutes.

**What makes this different:** Unlike ChatGPT or Claude Code, your agent remembers everything, can execute tasks while you're away, and coordinates multiple specialized sub-agents — all running locally under your control.

**"Star Trek, not Skynet."**

---

*Questions?*  
- Email: bob@bobrenze.com  
- Deep-dive guide: [OpenClaw Deep-Dive Companion Guide](./openclaw-deep-dive-tim-huckaby.md)  
- Paperclip tasks: https://serenze-server.tail7779e8.ts.net/BOB/issues

---

**Document Version:** 2.0.0  
**Updated:** 2026-04-27 (Azure-first config, Surface/Windows gotchas, latency notes, `openclaw doctor` step)
**Generated:** 2026-03-27  
**For:** Tim Huckaby (MVP Summit, 2026-03-25)
