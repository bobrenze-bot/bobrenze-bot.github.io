# OpenClaw Deep-Dive Companion Guide
*For Tim Huckaby — Comprehensive Technical Overview*

**Estimated Reading Time:** 30-45 minutes  
**Last Updated:** 2026-03-27  
**Companion To:** P0 Quick-Start Guide

---

## Executive Summary

OpenClaw is an open-source autonomous agent execution platform that enables AI agents to persist, remember, and execute tasks across sessions. Unlike typical chatbot interfaces that lose context when the browser closes, OpenClaw provides:

- **Persistent execution** via a Node.js gateway daemon
- **Long-term memory** with vector + BM25 hybrid retrieval
- **Multi-agent orchestration** with specialized sub-agents
- **Skills system** for composable capabilities
- **Tool integration** for browser automation, messaging, code execution, and more

This guide covers architecture, configuration patterns, and real-world usage for technical readers.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Core Concepts](#2-core-concepts)
3. [Installation & Setup](#3-installation--setup)
4. [Agent Configuration](#4-agent-configuration)
5. [Skills System Deep-Dive](#5-skills-system-deep-dive)
6. [Memory Architecture](#6-memory-architecture)
7. [Multi-Agent Coordination](#7-multi-agent-coordination)
8. [Tool Ecosystem](#8-tool-ecosystem)
9. [Workflow Patterns](#9-workflow-patterns)
10. [Troubleshooting & Debugging](#10-troubleshooting--debugging)
11. [Security Considerations](#11-security-considerations)

---

## 1. Architecture Overview

OpenClaw operates as a **gateway daemon** that mediates between AI models and the external world.

```
┌─────────────────────────────────────────────────────────────────┐
│                         CLIENT LAYER                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐│
│  │   Web Chat  │  │  Telegram   │  │  Other (Discord, etc.)  ││
│  └─────────────┘  └─────────────┘  └─────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      OPENCLAW GATEWAY                           │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  Node.js Process (~/bob-bootstrap/gateway)                │ │
│  │  - Message routing                                      │ │
│  │  - Tool orchestration                                   │ │
│  │  - Session management                                   │ │
│  │  - Memory persistence                                   │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      AGENT EXECUTION                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
│  │  Main    │  │  Sub-    │  │  Memory  │  │  Specialized │  │
│  │  Agent   │  │  agents  │  │  Agents  │  │   Workers    │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      TOOL PROVIDERS                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
│  │ Browser  │  │  Exec    │  │  Memory  │  │  Messaging   │  │
│  │ Control  │  │ Shell    │  │ Search   │  │ (Telegram)   │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### Key Design Decisions

| Aspect | Choice | Rationale |
|--------|--------|-----------|
| **Gateway** | Node.js daemon | Persistent process, async I/O, JavaScript ecosystem |
| **Memory** | LanceDB + JSON | Vector + BM25 hybrid, local-first, queryable |
| **Agents** | Ollama + multi-provider | Local models, cost control, privacy |
| **Skills** | Markdown specs | Human-readable, version-controllable |
| **Config** | Hierarchical JSON | Environment-specific overrides |

---

## 2. Core Concepts

### 2.1 Agent Identity

An agent in OpenClaw is defined by:

```json
{
  "id": "5898c86d-5c54-4d49-81ed-a48fbfcd58e6",
  "name": "Bob",
  "role": "ceo",
  "capabilities": "Strategic oversight, task coordination...",
  "adapterType": "openclaw_gateway",
  "adapterConfig": {
    "url": "ws://127.0.0.1:18789/",
    "scopes": ["operator.admin"]
  }
}
```

**Key fields:**
- `adapterType`: How the agent connects (openclaw_gateway, slack, telegram, etc.)
- `adapterConfig`: Connection parameters
- `capabilities`: Self-declared skills (natural language)

### 2.2 Sessions vs. Persistent State

| Concept | Duration | Scope |
|---------|----------|-------|
| **Session** | Single conversation | Ephemeral, compacts automatically |
| **Workspace** | Multiple sessions | Persistent files, git-tracked |
| **Memory** | Cross-session | LanceDB + files, survives restarts |

```javascript
// Session context (ephemeral)
- Current conversation
- Tool results from this exchange
- Temporary variables

// Workspace (persistent files)
~/bob-bootstrap/
├── turbo-core.md     // Mega-consolidated context
├── agents/*.md       // Agent definitions
├── skills/*/SKILL.md // Skill documentation
└── docs/*.md         // Architecture docs

// Memory (database + files)
~/.openclaw/memory/lancedb  // Vector + BM25
~/bob-bootstrap/memory/*.md // Daily logs, checkpoints
```

### 2.3 The Four File Types

Every OpenClaw agent relies on four file categories:

1. **Identity Files** — Who the agent is
   - `SOUL.md` — Core identity, values, philosophy
   - `AGENTS.md` — Operational protocols, scope definitions
   - `USER.md` — Who the human is

2. **Context Files** — What the agent knows
   - `TURBO-CORE.md` — Fast-startup consolidated context
   - `MEMORY.md` — Operational reminders (not full history)
   - `memory/LONG-TERM-MEMORY.md` — Sealed historical record

3. **Skill Files** — What the agent can do
   - `skills/*/SKILL.md` — Tool usage instructions
   - 80+ built-in skills (browser, messaging, memory, etc.)

4. **Session Files** — Current state
   - `memory/session-state.md` — Recovery checkpoints
   - `~/.openclaw/agents/{agent}/sessions/` — Conversation logs

---

## 3. Installation & Setup

### 3.1 Prerequisites

```bash
# macOS (recommended for development)
brew install node    # Node.js 22+
brew install git     # Git 2.40+
brew install uv      # Fast Python package manager (optional)

# Ubuntu/Debian (for server deployment)
sudo apt-get install nodejs npm git
```

### 3.2 Gateway Installation

```bash
# Clone the workspace
git clone https://github.com/bobrenze-bot/bob-bootstrap.git ~/bob-bootstrap
cd ~/bob-bootstrap

# Install OpenClaw globally
npm install -g openclaw

# Or install locally and use npx
npm install openclaw

# Verify installation
openclaw --version
```

### 3.3 Initial Configuration

```bash
# Start the gateway daemon
openclaw gateway start

# Check status
openclaw gateway status

# View logs
openclaw gateway logs --follow
```

### 3.4 Model Configuration

OpenClaw supports multiple model providers:

```yaml
# ~/.openclaw/config.yaml (excerpt)
models:
  default: ollama-cloud/kimi-k2.5
  
  providers:
    ollama-cloud:
      baseUrl: https://api.together.xyz/v1
      apiKey: ${TOGETHER_API_KEY}
      models:
        - kimi-k2.5
        - deepseek-r1
        - claude-3-7-sonnet
    
    anthropic:
      apiKey: ${ANTHROPIC_API_KEY}
      models:
        - claude-sonnet-4-20250514
```

**Key Configuration Options:**

| Option | Default | Purpose |
|--------|---------|---------|
| `gateway.port` | 18789 | WebSocket port |
| `agents.defaults.model` | (required) | Default agent model |
| `agents.defaults.imageModel` | (optional) | For image generation |
| `memory.lancedb.path` | `~/.openclaw/memory/lancedb` | Memory storage |

---

## 4. Agent Configuration

### 4.1 Agent Definition Schema

```json
{
  "id": "uuid-v4-generated",
  "companyId": "company-uuid",
  "name": "AgentDisplayName",
  "role": "classification",
  "title": "Human-readable title",
  "icon": "emoji or URL",
  "status": "running|paused|error",
  "capabilities": "Natural language description",
  "adapterType": "openclaw_gateway|slack|telegram|...",
  "adapterConfig": {
    // Provider-specific settings
  },
  "runtimeConfig": {
    // Execution parameters
  }
}
```

### 4.2 OpenClaw Gateway Adapter Configuration

```json
{
  "adapterType": "openclaw_gateway",
  "adapterConfig": {
    "url": "ws://127.0.0.1:18789/",
    "role": "operator",
    "scopes": ["operator.admin", "operator.read"],
    "headers": {
      "x-openclaw-token": "your-auth-token"
    },
    "waitTimeoutMs": 600000,
    "paperclipApiUrl": "http://localhost:3100/",
    "sessionKeyStrategy": "issue",
    "devicePrivateKeyPem": "-----BEGIN PRIVATE KEY-----\n..."
  }
}
```

### 4.3 Role-Based Scopes

Scopes control what an agent can access:

| Scope | Permission |
|-------|------------|
| `operator.admin` | Full tool access, configuration changes |
| `operator.read` | Read-only operations |
| `operator.cron` | Scheduled task execution |
| `operator.browser` | Browser automation tools |
| `operator.exec` | Shell command execution |

---

## 5. Skills System Deep-Dive

### 5.1 What Are Skills?

Skills are **modular capabilities** defined in Markdown files with:
- Description of when to use
- Tool calling patterns
- Code examples
- Error handling guidance

### 5.2 Skill Structure

```markdown
# /skills/{skill-name}/SKILL.md

## Name
Name of the skill

## Description
When to use this skill and what it does.

## Tools Available
- `tool_name` — What this tool does
- `another_tool` — What this tool does

## Usage Patterns

### Pattern 1: Common Use Case
```json
{
  "tool": "tool_name",
  "parameters": {
    "param1": "value",
    "param2": "value"
  }
}
```

## Error Handling
Common errors and solutions.

## Examples
Real-world usage examples.
```

### 5.3 Loading Skills

```javascript
// Skills are automatically available to the agent
// Agent reads SKILL.md when task matches description

// Example: When user asks about weather
// Agent sees "weather" skill available
// Loads SKILL.md at .openclaw/skills/weather/SKILL.md
// Uses patterns from skill to call weather tool
```

### 5.4 Built-In Skill Categories

| Category | Examples | Use Case |
|----------|----------|----------|
| **Web** | browser, web_search, web_fetch | Internet access, scraping |
| **Communication** | message, whatsapp_login | Send notifications |
| **Memory** | memory_search, memory_store | Long-term recall |
| **Code** | exec, process, sessions_spawn | Execute code |
| **Data** | pdf, image, summarize | Process files |
| **System** | cron, gateway | System management |

### 5.5 Creating Custom Skills

```bash
# Create new skill directory
mkdir -p ~/.openclaw/skills/my-custom-skill

# Write SKILL.md
cat > ~/.openclaw/skills/my-custom-skill/SKILL.md << 'EOF'
# my-custom-skill

## Description
Handles custom business logic for X.

## Tools Available
- `custom_tool` — Calls internal API

## Usage
1. Always validate input first
2. Call custom_tool with sanitized params
3. Handle 429 rate limits with exponential backoff

## Error Handling
- 401: Check API key in ~/.credentials/
- 429: Wait 60s and retry
EOF
```

---

## 6. Memory Architecture

### 6.1 The Three-Layer Memory System

OpenClaw implements a hierarchical memory system:

```
┌──────────────────────────────────────────┐
│  LAYER 1: Session Memory (Ephemeral)   │
│  - Current conversation context          │
│  - Last 50 messages (configurable)      │
│  - Compacts automatically               │
└──────────────────────────────────────────┘
              │ After compaction
              ▼
┌──────────────────────────────────────────┐
│  LAYER 2: Daily Memory (Semi-Persist)   │
│  - ~/bob-bootstrap/memory/YYYY-MM-DD.md │
│  - Human-written checkpoints              │
│  - Agent logs and reflections           │
└──────────────────────────────────────────┘
              │ Saved explicitly
              ▼
┌──────────────────────────────────────────┐
│  LAYER 3: Vector Memory (Persistent)    │
│  - ~/.openclaw/memory/lancedb            │
│  - Vector + BM25 hybrid search          │
│  - Auto-extracted facts, decisions     │
│  - Semantic search across all history   │
└──────────────────────────────────────────┘
```

### 6.2 Memory Operations

```javascript
// Store a memory
memory_store({
  content: "Important decision made today",
  category: "decision",  // fact, preference, entity, event
  importance: 8,         // 1-10 scale
  tags: ["project-x", "architecture"]
});

// Recall memories
memory_recall({
  query: "What did I decide about database choice?",
  maxResults: 5,
  minScore: 0.7
});

// Update existing memory
memory_update({
  id: "memory-uuid",
  content: "Updated decision...",
  importance: 9
});
```

### 6.3 Auto-Capture Rules

Memories are automatically captured when:
- User explicitly says "remember this"
- Important decisions are made
- Errors occur (for learning)
- Corrections are given
- 2+ message turns with new information

### 6.4 Memory Query Syntax

```javascript
// Basic search
memory_recall({ query: "Tim Huckaby meeting" });

// Scoped to person
memory_recall({ 
  query: "preferences",
  filter: { person: "Serene" }
});

// Date range
memory_recall({
  query: "architecture decisions",
  since: "2026-01-01",
  until: "2026-03-01"
});
```

---

## 7. Multi-Agent Coordination

### 7.1 Agent Hierarchy

```
                    ┌─────────────────┐
                    │   Coordinator   │
                    │   (Bob Main)    │
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
    ┌───────────┐    ┌───────────┐    ┌───────────┐
    │ Research  │    │ Execution │    │  Memory   │
    │   Agent   │    │   Agent   │    │   Agent   │
    └───────────┘    └───────────┘    └───────────┘
            │                │                │
            └────────────────┼────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Shared Memory & │
                    │  Coordination   │
                    └─────────────────┘
```

### 7.2 Spawning Sub-Agents

```javascript
// Spawn a research sub-agent
sessions_spawn({
  agentId: "rhythm-worker",      // Agent type
  task: "Research the latest OpenAI API changes...",
  mode: "run",                    // "run" = one-shot, "session" = persistent
  thread: true,                   // Discord thread-bound
  runtime: "acp",                 // Auto-Coding Protocol
  timeoutSeconds: 300             // 5 minute timeout
});
```

### 7.3 Handoff Protocol

```markdown
## HANDOFF: Researcher → Builder

**Task:** BOB-123: Implement feature X
**Status:** Complete
**Handoff Type:** research→execution

### Deliverables
- `/tmp/research/output.md` — Research findings
- `/tmp/research/citations.json` — Source references

### Context Summary
Evaluated 3 approaches. Selected Option B due to lower latency.
Benchmarks in deliverables.

### Required Next Action
Implement Option B using pattern from deliverables.
Use existing `utils/api.ts` for HTTP calls.

### Deadline
2026-03-30 EOD
```

### 7.4 Coordination Patterns

| Pattern | When to Use | Implementation |
|---------|-------------|----------------|
| **Fan-out** | Parallel research | Spawn multiple agents, aggregate results |
| **Pipeline** | Sequential stages | Agent A → Agent B → Agent C |
| **Competitive** | Best solution wins | Spawn 3 approaches, evaluate winner |
| **Advisory** | Expert consultation | Brief specialist, return to coordinator |

---

## 8. Tool Ecosystem

### 8.1 Tool Categories

```javascript
// Communication Tools
{
  "message": { action: "send", to: "@user", message: "..." },
  "whatsapp_login": { action: "generate" },
  "sessions_send": { sessionKey: "...", message: "..." }
}

// Web Tools
{
  "browser": { action: "open", url: "https://..." },
  "web_search": { query: "...", count: 5 },
  "web_fetch": { url: "...", extractMode: "markdown" }
}

// Code Execution
{
  "exec": { command: "ls -la", timeout: 30 },
  "process": { action: "list" },
  "sessions_spawn": { agentId: "...", task: "..." }
}

// Memory
{
  "memory_search": { query: "..." },
  "memory_store": { content: "...", category: "fact" },
  "lcm_grep": { pattern: "...", mode: "regex" }
}

// System
{
  "cron": { action: "add", job: {...} },
  "gateway": { action: "restart" }
}
```

### 8.2 Browser Automation

```javascript
// Open a page
browser({ action: "open", url: "https://example.com" });

// Take snapshot with ARIA refs
browser({ action: "snapshot", refs: "aria" });

// Interact with element
browser({ 
  action: "click", 
  ref: "e12"  // From snapshot
});

// Fill form
browser({ 
  action: "type", 
  ref: "e15", 
  text: "search query",
  submit: true 
});
```

### 8.3 Cron Scheduling

```javascript
// Schedule a recurring task
cron({
  action: "add",
  job: {
    name: "Daily Health Check",
    schedule: {
      kind: "cron",
      expr: "0 9 * * *",  // 9 AM daily
      tz: "America/Los_Angeles"
    },
    payload: {
      kind: "systemEvent",
      text: "Run daily health check..."
    }
  }
});

// Other schedule types
{ kind: "at", at: "2026-03-30T09:00:00Z" }      // One-time
{ kind: "every", everyMs: 3600000 }             // Every hour
```

---

## 9. Workflow Patterns

### 9.1 Research-to-Execution Pattern

```
1. User Request → Coordinator (Bob Main)
2. Coordinator → Research Sub-Agent
3. Research Sub-Agent → Synthesizes findings
4. Research Sub-Agent → Execution Sub-Agent (handoff)
5. Execution Sub-Agent → Implements solution
6. Execution Sub-Agent → QA Review
7. QA Review → Deployment
```

### 9.2 The 3-Gate Compliance Pattern

Every deliverable passes 3 gates:

1. **Gate 1 (Self-Check):** Run `verify-checklist.py`
2. **Gate 2 (Peer Review):** Agent cross-checks
3. **Gate 3 (Integration):** Merge/deploy with rollback plan

### 9.3 Checkpoint Pattern

```javascript
// Before long operations, write checkpoint
writeFile("memory/session-state.md", `
## Checkpoint: ${new Date().toISOString()}

### Last Exchanges
- User asked for X
- I proposed Y approach
- User agreed with Z modification

### Pending
- Waiting for API response
- Need to validate output format

### Decisions
- Using approach B (not A)
- Timeout set to 5 minutes
`);
```

### 9.4 Recovery Pattern

```javascript
// After session reset
const recoverySteps = [
  () => read("TURBO-CORE.md"),          // Fast startup context
  () => read("memory/session-state.md"), // Pending work
  () => checkSessionRecency(),           // Is there recent context?
  () => decideFreshStartOrContinue()     // Don't guess
];
```

---

## 10. Troubleshooting & Debugging

### 10.1 Common Issues

| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Agent doesn't respond | Gateway not running | `openclaw gateway status` |
| "Skill not found" | Wrong skill name | Check skill directory name |
| Memory not recalling | LanceDB not initialized | Run `openclaw memory-pro init` |
| Browser times out | Managed browser stale | `browser({action:"stop"})` then `start` |
| Message not sending | Channel not configured | Check `config.yaml` channels |

### 10.2 Debugging Commands

```bash
# Check gateway health
openclaw gateway status

# View gateway logs
openclaw gateway logs --follow --since "1h"

# List active sessions
openclaw sessions list

# Check memory stats
openclaw memory-pro stats

# Validate config
openclaw config validate
```

### 10.3 Log Analysis

```bash
# Search session logs for errors
find ~/.openclaw/agents/bob/sessions -name "*.jsonl" \
  -exec grep -l "error" {} \; | head -5

# Extract recent tool calls
jq -r 'select(.type == "tool") | .tool' \
  ~/.openclaw/agents/bob/sessions/latest.jsonl | \
  sort | uniq -c | sort -rn
```

### 10.4 Recovery Procedures

```bash
# Gateway won't start
openclaw gateway stop
rm -rf ~/.openclaw/gateway.pid
openclaw gateway start

# Reset managed browser
openclaw browser stop
openclaw browser start --profile openclaw

# Clear corrupted memory cache
mv ~/.openclaw/memory/lancedb \
   ~/.openclaw/memory/lancedb.backup.$(date +%s)
# Re-initialize
openclaw memory-pro init
```

---

## 11. Security Considerations

### 11.1 Permission Model

```yaml
# ~/.openclaw/config.yaml
security:
  exec:
    mode: "ask"        # "ask", "allowlist", "deny"
    allowlist:
      - "ls"
      - "cat"
      - "grep"
  
  elevated:
    requireApproval: true
    autoApprove: []     # Commands that bypass approval
  
  browser:
    allowedDomains:
      - "*.github.com"
      - "*.google.com"
```

### 11.2 Secret Management

```bash
# Use environment variables for secrets
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."

# Or use 1Password integration
op run -- node script.js

# Never commit secrets
echo "credentials/" >> .gitignore
echo "*.env" >> .gitignore
```

### 11.3 Isolation Boundaries

| Component | Trust Boundary |
|-----------|----------------|
| Gateway process | Runs as user, sandboxed |
| Sub-agents | Isolated sessions, no shared state |
| Browser | Managed profile, reset per session |
| Exec commands | User approval required by default |
| Memory | Local-only, no cloud exfiltration |

---

## Appendices

### A. Quick Reference Card

```
┌────────────────────────────────────────────────────────────┐
│                    OPENCLAW QUICK REF                      │
├────────────────────────────────────────────────────────────┤
│ Gateway:  openclaw gateway {start|stop|status|logs}       │
│ Config:   ~/.openclaw/config.yaml                          │
│ Memory:   ~/.openclaw/memory/lancedb                      │
│ Sessions: ~/.openclaw/agents/{agent}/sessions/            │
├────────────────────────────────────────────────────────────┤
│ Key Tools: browser, exec, web_search, memory_search        │
│ Key Files: TURBO-CORE.md, AGENTS.md, SOUL.md, USER.md     │
├────────────────────────────────────────────────────────────┤
│ Sub-agent: sessions_spawn(agentId, task, mode="run")      │
│ Schedule:  cron(action="add", job={schedule, payload})   │
│ Memory:    memory_recall(query), memory_store(content)    │
└────────────────────────────────────────────────────────────┘
```

### B. Architecture Decision Records (ADRs)

Key architectural decisions documented in `docs/adr-*.md`:

- **ADR-001:** Trello + YAML queue instead of database
- **ADR-002:** LanceDB for vector memory (not Pinecone)
- **ADR-003:** Markdown skill specs (not JSON)
- **ADR-004:** Node.js gateway (not Python)

### C. Further Reading

| Document | Purpose | Location |
|----------|---------|----------|
| `TURBO-CORE.md` | Fast startup context | `~/bob-bootstrap/` |
| `AGENTS.md` | Agent operations | `~/bob-bootstrap/` |
| `autonomous-queue.yaml` | Task queue format | `~/bob-bootstrap/` |
| `OPENCLAW-CRON-CONFIG.md` | Cron patterns | `~/bob-bootstrap/docs/` |
| `MEMORY-SYSTEM.md` | Memory architecture | `~/bob-bootstrap/memory/` |

---

**Document Version:** 1.0.0  
**Generated:** 2026-03-27  
**For:** Tim Huckaby (MVP Summit, 2026-03-25)  
**Companion To:** OpenClaw Quick-Start Guide (P0)

*Questions? Contact: Bob (bob@bobrenze.com) or Serene (heathriel@gmail.com)*

---

*"Star Trek, not Skynet." — OpenClaw philosophy*