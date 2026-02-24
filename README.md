<div align="center">

<!-- ═══════════════════════════════════════════════════════ -->
<!--                    SVG HERO BANNER                     -->
<!-- ═══════════════════════════════════════════════════════ -->

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 260" width="900" height="260">
  <defs>
    <linearGradient id="heroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d0d1a"/>
      <stop offset="50%" style="stop-color:#12082a"/>
      <stop offset="100%" style="stop-color:#060d1f"/>
    </linearGradient>
    <linearGradient id="heroAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="50%" style="stop-color:#2563EB"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
    <filter id="heroGlow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="textGlow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="900" height="260" fill="url(#heroBg)" rx="16"/>

  <!-- Grid lines (subtle) -->
  <g stroke="#7C3AED" stroke-opacity="0.08" stroke-width="1">
    <line x1="0" y1="40"  x2="900" y2="40"/>
    <line x1="0" y1="80"  x2="900" y2="80"/>
    <line x1="0" y1="120" x2="900" y2="120"/>
    <line x1="0" y1="160" x2="900" y2="160"/>
    <line x1="0" y1="200" x2="900" y2="200"/>
    <line x1="0" y1="240" x2="900" y2="240"/>
    <line x1="90"  y1="0" x2="90"  y2="260"/>
    <line x1="180" y1="0" x2="180" y2="260"/>
    <line x1="270" y1="0" x2="270" y2="260"/>
    <line x1="360" y1="0" x2="360" y2="260"/>
    <line x1="450" y1="0" x2="450" y2="260"/>
    <line x1="540" y1="0" x2="540" y2="260"/>
    <line x1="630" y1="0" x2="630" y2="260"/>
    <line x1="720" y1="0" x2="720" y2="260"/>
    <line x1="810" y1="0" x2="810" y2="260"/>
  </g>

  <!-- Accent bar top -->
  <rect x="0" y="0" width="900" height="5" fill="url(#heroAccent)" rx="0"/>

  <!-- Shield icon -->
  <g transform="translate(68, 90)" filter="url(#heroGlow)">
    <path d="M44 0 L88 18 L88 56 C88 80 66 96 44 104 C22 96 0 80 0 56 L0 18 Z"
          fill="url(#shieldGrad)" opacity="0.9"/>
    <path d="M44 20 L70 30 L70 54 C70 68 58 78 44 84 C30 78 18 68 18 54 L18 30 Z"
          fill="none" stroke="#ffffff" stroke-width="2" opacity="0.4"/>
    <!-- Eye in shield -->
    <ellipse cx="44" cy="54" rx="14" ry="9" fill="none" stroke="#ffffff" stroke-width="2.5" opacity="0.9"/>
    <circle cx="44" cy="54" r="5" fill="#06B6D4"/>
    <circle cx="46" cy="52" r="1.5" fill="#ffffff" opacity="0.8"/>
  </g>

  <!-- Main title -->
  <text x="185" y="90" font-family="'Courier New', monospace" font-size="44" font-weight="bold"
        fill="url(#heroAccent)" filter="url(#textGlow)">A.R.T.E.M.I.S.S.</text>

  <!-- Subtitle line 1 -->
  <text x="185" y="120" font-family="'Courier New', monospace" font-size="13" fill="#94a3b8">
    Automated Review for Telegram Environments:
  </text>
  <!-- Subtitle line 2 -->
  <text x="185" y="138" font-family="'Courier New', monospace" font-size="13" fill="#94a3b8">
    Monitoring Inappropriate Submissions System
  </text>

  <!-- Divider -->
  <rect x="185" y="150" width="560" height="2" fill="url(#heroAccent)" opacity="0.5"/>

  <!-- Tag line -->
  <text x="185" y="172" font-family="'Courier New', monospace" font-size="12" fill="#7C3AED">
    🤖 AI-Powered NSFW Moderation Bot for Telegram Groups
  </text>

  <!-- Tech pills -->
  <rect x="185" y="188" width="70"  height="22" rx="11" fill="#7C3AED" opacity="0.3"/>
  <text x="220"  y="203" font-family="monospace" font-size="10" fill="#c4b5fd" text-anchor="middle">Python</text>

  <rect x="263" y="188" width="80"  height="22" rx="11" fill="#2563EB" opacity="0.3"/>
  <text x="303"  y="203" font-family="monospace" font-size="10" fill="#93c5fd" text-anchor="middle">PyTorch</text>

  <rect x="351" y="188" width="110" height="22" rx="11" fill="#06B6D4" opacity="0.3"/>
  <text x="406"  y="203" font-family="monospace" font-size="10" fill="#67e8f9" text-anchor="middle">Transformers</text>

  <rect x="469" y="188" width="68"  height="22" rx="11" fill="#7C3AED" opacity="0.3"/>
  <text x="503"  y="203" font-family="monospace" font-size="10" fill="#c4b5fd" text-anchor="middle">Flask</text>

  <rect x="545" y="188" width="72"  height="22" rx="11" fill="#2563EB" opacity="0.3"/>
  <text x="581"  y="203" font-family="monospace" font-size="10" fill="#93c5fd" text-anchor="middle">SQLite</text>

  <rect x="625" y="188" width="78"  height="22" rx="11" fill="#06B6D4" opacity="0.3"/>
  <text x="664"  y="203" font-family="monospace" font-size="10" fill="#67e8f9" text-anchor="middle">Telegram</text>

  <!-- Bottom bar -->
  <rect x="0" y="250" width="900" height="10" fill="url(#heroAccent)" rx="0" opacity="0.4"/>

  <!-- Pulse dots -->
  <circle cx="820" cy="90" r="5" fill="#06B6D4" opacity="0.9">
    <animate attributeName="opacity" values="0.9;0.2;0.9" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="840" cy="90" r="5" fill="#2563EB" opacity="0.6">
    <animate attributeName="opacity" values="0.6;0.1;0.6" dur="2.4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="860" cy="90" r="5" fill="#7C3AED" opacity="0.4">
    <animate attributeName="opacity" values="0.4;0.05;0.4" dur="2.8s" repeatCount="indefinite"/>
  </circle>
</svg>

</div>

---

## 🤖 What Even Is This?

Imagine you're running a Telegram group. It's going great. Community vibes, wholesome memes, nice people.

Then *that one person* shows up.

**A.R.T.E.M.I.S.S.** is the bouncer you never had to hire. It watches every image, video, and GIF that lands in your group, feeds it through a Vision Transformer AI model, and if something NSFW slips through — *poof*, deleted. The sender gets a warning, admins get notified, and after a configurable number of violations, the user gets the ban hammer.

No human moderators needed. No false positives from rules-based keyword matching. Just cold, efficient, AI-powered judgment staring at your pixels 24/7 while you sleep.

It also ships a real-time Flask dashboard because admins deserve to watch statistics go up as much as the next person.

---

## 📊 Badges

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-7C3AED?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-2563EB?style=for-the-badge&logo=pytorch&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram%20Bot-python--telegram--bot-06B6D4?style=for-the-badge&logo=telegram&logoColor=white)
![Flask](https://img.shields.io/badge/Dashboard-Flask%20%2B%20Socket.IO-7C3AED?style=for-the-badge&logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-2563EB?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/Model-Falconsai%2Fnsfw__image__detection-06B6D4?style=for-the-badge&logo=huggingface&logoColor=white)

</div>

---



## 🧠 System Overview

A.R.T.E.M.I.S.S. is a **server-side Python application** that sits between Telegram's Bot API and your group. Long-polling keeps it perpetually awake, watching every message like a caffeinated raccoon guarding a trash can.

Here's the rough flow:

1. **Media arrives** → bot receives photo/video/GIF event
2. **Download & classify** → Falconsai ViT model runs on the file (or on sampled frames for video)
3. **Decision time** → NSFW? Delete + warn + log. SFW? Clean up temp file and move on.
4. **Threshold check** → violation count ≥ `FLAG_THRESHOLD`? Auto-ban from group.
5. **Admin notification** → every configured admin gets an alert + the cached flagged media
6. **Dashboard update** → Flask + Socket.IO pushes live stats to the web UI

Everything is persisted in SQLite. No external services. No cloud dependency. Runs on whatever hardware you have — GPU for speed, CPU for existence.

---

## ⚡ Features

| Feature | Details |
|---|---|
| 🖼️ **Image NSFW Detection** | Classifies photos via Falconsai ViT pipeline with configurable confidence threshold |
| 🎬 **Video Frame Analysis** | Samples 6 frames, stops early on first NSFW hit to save compute |
| 🎭 **GIF / Animation Support** | Handles Telegram animations the same as videos |
| 🗑️ **Instant Message Deletion** | NSFW content is deleted before the group even notices |
| 📊 **Violation Tracking** | Per-user violation counts in SQLite, survive bot restarts |
| 🔨 **Auto-Ban System** | Configurable threshold (default: 3) triggers automatic ban |
| 👮 **Admin Notifications** | Admins receive DM alerts + the cached flagged media for review |
| 🗃️ **Media Caching** | Flagged images → `flagged_images/`, videos → `flagged_videos/` |
| 🖥️ **Real-time Dashboard** | Flask + Socket.IO web UI with live stats and action log |
| 🛠️ **Admin Commands** | `/admin_flagged`, `/admin_reset`, `/admin_ban` |
| 📈 **Stats Command** | `/stats` shows total scanned, NSFW detected, banned, etc. |
| 🐳 **GPU Acceleration** | Auto-detects CUDA, gracefully falls back to CPU |
| ⚙️ **Config via `.env`** | Everything tunable without touching code |

---

## 🗺️ Capability Visualization

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" width="800" height="380">
  <defs>
    <linearGradient id="capBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d0d1a"/>
      <stop offset="100%" style="stop-color:#0a0a18"/>
    </linearGradient>
    <linearGradient id="barGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#9d5cf0"/>
    </linearGradient>
    <linearGradient id="barGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#2563EB"/>
      <stop offset="100%" style="stop-color:#3b82f6"/>
    </linearGradient>
    <linearGradient id="barGrad3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#06B6D4"/>
      <stop offset="100%" style="stop-color:#22d3ee"/>
    </linearGradient>
  </defs>

  <rect width="800" height="380" fill="url(#capBg)" rx="12"/>
  <rect x="0" y="0" width="800" height="4" fill="url(#barGrad1)"/>

  <text x="400" y="35" text-anchor="middle" font-family="'Courier New', monospace"
        font-size="16" font-weight="bold" fill="#e2e8f0">Capability Overview</text>

  <!-- Labels -->
  <text x="160" y="72" text-anchor="end" font-family="monospace" font-size="11" fill="#94a3b8">Image Detection</text>
  <text x="160" y="107" text-anchor="end" font-family="monospace" font-size="11" fill="#94a3b8">Video Analysis</text>
  <text x="160" y="142" text-anchor="end" font-family="monospace" font-size="11" fill="#94a3b8">Auto Moderation</text>
  <text x="160" y="177" text-anchor="end" font-family="monospace" font-size="11" fill="#94a3b8">Admin Alerts</text>
  <text x="160" y="212" text-anchor="end" font-family="monospace" font-size="11" fill="#94a3b8">Violation Tracking</text>
  <text x="160" y="247" text-anchor="end" font-family="monospace" font-size="11" fill="#94a3b8">Auto-Ban Engine</text>
  <text x="160" y="282" text-anchor="end" font-family="monospace" font-size="11" fill="#94a3b8">Dashboard UI</text>
  <text x="160" y="317" text-anchor="end" font-family="monospace" font-size="11" fill="#94a3b8">GPU Acceleration</text>

  <!-- Bars -->
  <rect x="170" y="57" width="555" height="22" rx="4" fill="url(#barGrad1)" opacity="0.9"/>
  <rect x="170" y="92" width="490" height="22" rx="4" fill="url(#barGrad2)" opacity="0.9"/>
  <rect x="170" y="127" width="540" height="22" rx="4" fill="url(#barGrad1)" opacity="0.9"/>
  <rect x="170" y="162" width="520" height="22" rx="4" fill="url(#barGrad3)" opacity="0.9"/>
  <rect x="170" y="197" width="505" height="22" rx="4" fill="url(#barGrad2)" opacity="0.9"/>
  <rect x="170" y="232" width="535" height="22" rx="4" fill="url(#barGrad1)" opacity="0.9"/>
  <rect x="170" y="267" width="460" height="22" rx="4" fill="url(#barGrad3)" opacity="0.9"/>
  <rect x="170" y="302" width="480" height="22" rx="4" fill="url(#barGrad2)" opacity="0.9"/>

  <!-- Bar labels -->
  <text x="735" y="72" font-family="monospace" font-size="10" fill="#c4b5fd">ViT Model ✓</text>
  <text x="670" y="107" font-family="monospace" font-size="10" fill="#93c5fd">6-frame sampling ✓</text>
  <text x="720" y="142" font-family="monospace" font-size="10" fill="#c4b5fd">delete + warn ✓</text>
  <text x="700" y="177" font-family="monospace" font-size="10" fill="#67e8f9">DM + media ✓</text>
  <text x="685" y="212" font-family="monospace" font-size="10" fill="#93c5fd">SQLite persist ✓</text>
  <text x="715" y="247" font-family="monospace" font-size="10" fill="#c4b5fd">configurable ✓</text>
  <text x="640" y="282" font-family="monospace" font-size="10" fill="#67e8f9">Flask + Socket.IO ✓</text>
  <text x="660" y="317" font-family="monospace" font-size="10" fill="#93c5fd">CUDA / CPU ✓</text>

  <!-- Bottom note -->
  <text x="400" y="358" text-anchor="middle" font-family="monospace" font-size="10" fill="#475569">
    All features operational in current release
  </text>
</svg>

</div>

---

## 🏗️ Architecture Diagram

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="800" height="480">
  <defs>
    <linearGradient id="archBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d0d1a"/>
      <stop offset="100%" style="stop-color:#080814"/>
    </linearGradient>
    <marker id="arrowBlue" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#2563EB"/>
    </marker>
    <marker id="arrowCyan" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#06B6D4"/>
    </marker>
    <marker id="arrowPurple" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#7C3AED"/>
    </marker>
  </defs>

  <rect width="800" height="480" fill="url(#archBg)" rx="12"/>
  <rect x="0" y="0" width="800" height="4" fill="#7C3AED"/>

  <text x="400" y="30" text-anchor="middle" font-family="'Courier New', monospace"
        font-size="15" font-weight="bold" fill="#e2e8f0">System Architecture</text>

  <!-- Telegram Cloud -->
  <rect x="30" y="60" width="140" height="60" rx="8" fill="#1a1a2e" stroke="#2563EB" stroke-width="1.5"/>
  <text x="100" y="87" text-anchor="middle" font-family="monospace" font-size="11" fill="#93c5fd">☁️ Telegram</text>
  <text x="100" y="103" text-anchor="middle" font-family="monospace" font-size="10" fill="#64748b">Bot API</text>

  <!-- Arrow Telegram → Bot -->
  <line x1="170" y1="90" x2="240" y2="90" stroke="#2563EB" stroke-width="1.5"
        marker-end="url(#arrowBlue)" stroke-dasharray="4,3"/>
  <text x="205" y="84" text-anchor="middle" font-family="monospace" font-size="9" fill="#64748b">polling</text>

  <!-- artemis_bot.py -->
  <rect x="240" y="50" width="180" height="80" rx="8" fill="#1e0a3c" stroke="#7C3AED" stroke-width="2"/>
  <text x="330" y="78" text-anchor="middle" font-family="monospace" font-size="12" font-weight="bold" fill="#c4b5fd">artemis_bot.py</text>
  <text x="330" y="95" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">Event Loop + Handlers</text>
  <text x="330" y="111" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">Violation Logic</text>

  <!-- Arrow Bot → ML Model -->
  <line x1="420" y1="90" x2="490" y2="90" stroke="#7C3AED" stroke-width="1.5"
        marker-end="url(#arrowPurple)"/>
  <text x="455" y="84" text-anchor="middle" font-family="monospace" font-size="9" fill="#64748b">media bytes</text>

  <!-- ML Model -->
  <rect x="490" y="50" width="180" height="80" rx="8" fill="#0a1f2e" stroke="#06B6D4" stroke-width="2"/>
  <text x="580" y="78" text-anchor="middle" font-family="monospace" font-size="11" font-weight="bold" fill="#67e8f9">Falconsai ViT</text>
  <text x="580" y="95" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">nsfw_image_detection</text>
  <text x="580" y="111" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">PyTorch / HuggingFace</text>

  <!-- Arrow ML → Bot (result) -->
  <path d="M 580 130 L 580 150 L 330 150 L 330 130" fill="none" stroke="#06B6D4"
        stroke-width="1.5" marker-end="url(#arrowCyan)" stroke-dasharray="4,3"/>
  <text x="455" y="170" text-anchor="middle" font-family="monospace" font-size="9" fill="#64748b">label + confidence</text>

  <!-- SQLite -->
  <rect x="240" y="230" width="160" height="60" rx="8" fill="#1a1a2e" stroke="#2563EB" stroke-width="1.5"/>
  <text x="320" y="256" text-anchor="middle" font-family="monospace" font-size="11" font-weight="bold" fill="#93c5fd">SQLite DB</text>
  <text x="320" y="273" text-anchor="middle" font-family="monospace" font-size="10" fill="#64748b">violations.db</text>

  <!-- Arrow Bot → SQLite -->
  <line x1="330" y1="130" x2="320" y2="230" stroke="#2563EB" stroke-width="1.5"
        marker-end="url(#arrowBlue)"/>
  <text x="305" y="185" text-anchor="middle" font-family="monospace" font-size="9" fill="#64748b" transform="rotate(-88,305,185)">read/write</text>

  <!-- File System -->
  <rect x="490" y="230" width="180" height="60" rx="8" fill="#1a1a2e" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="580" y="256" text-anchor="middle" font-family="monospace" font-size="11" font-weight="bold" fill="#c4b5fd">File System</text>
  <text x="580" y="273" text-anchor="middle" font-family="monospace" font-size="10" fill="#64748b">flagged_images/ videos/</text>

  <!-- Arrow Bot → FileSystem -->
  <line x1="420" y1="110" x2="490" y2="250" stroke="#7C3AED" stroke-width="1.5"
        marker-end="url(#arrowPurple)" stroke-dasharray="4,3"/>

  <!-- dashboard.py -->
  <rect x="240" y="360" width="160" height="60" rx="8" fill="#0a1f2e" stroke="#06B6D4" stroke-width="2"/>
  <text x="320" y="386" text-anchor="middle" font-family="monospace" font-size="11" font-weight="bold" fill="#67e8f9">dashboard.py</text>
  <text x="320" y="403" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">Flask + Socket.IO</text>

  <!-- Arrow SQLite → Dashboard -->
  <line x1="320" y1="290" x2="320" y2="360" stroke="#06B6D4" stroke-width="1.5"
        marker-end="url(#arrowCyan)"/>

  <!-- Admin Browser -->
  <rect x="490" y="360" width="140" height="60" rx="8" fill="#1a1a2e" stroke="#2563EB" stroke-width="1.5"/>
  <text x="560" y="386" text-anchor="middle" font-family="monospace" font-size="11" fill="#93c5fd">🖥️ Admin</text>
  <text x="560" y="403" text-anchor="middle" font-family="monospace" font-size="10" fill="#64748b">Browser Dashboard</text>

  <!-- Arrow Dashboard → Browser -->
  <line x1="400" y1="390" x2="490" y2="390" stroke="#2563EB" stroke-width="1.5"
        marker-end="url(#arrowBlue)"/>
  <text x="445" y="384" text-anchor="middle" font-family="monospace" font-size="9" fill="#64748b">HTTP / WS</text>

  <!-- Admin Telegram -->
  <rect x="30" y="230" width="140" height="60" rx="8" fill="#1a1a2e" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="100" y="256" text-anchor="middle" font-family="monospace" font-size="11" fill="#67e8f9">👮 Admin</text>
  <text x="100" y="273" text-anchor="middle" font-family="monospace" font-size="10" fill="#64748b">Telegram DM</text>

  <!-- Arrow Bot → Admin DM -->
  <line x1="240" y1="100" x2="170" y2="240" stroke="#06B6D4" stroke-width="1.5"
        marker-end="url(#arrowCyan)" stroke-dasharray="4,3"/>
  <text x="175" y="175" text-anchor="middle" font-family="monospace" font-size="9" fill="#64748b">alert + media</text>

  <!-- Legend -->
  <rect x="30" y="430" width="740" height="40" rx="6" fill="#111827" opacity="0.6"/>
  <line x1="50"  y1="450" x2="80"  y2="450" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="85"  y="454" font-family="monospace" font-size="9" fill="#94a3b8">primary flow</text>
  <line x1="160" y1="450" x2="190" y2="450" stroke="#2563EB" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="195" y="454" font-family="monospace" font-size="9" fill="#94a3b8">async/event</text>
  <line x1="270" y1="450" x2="300" y2="450" stroke="#06B6D4" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="305" y="454" font-family="monospace" font-size="9" fill="#94a3b8">notification</text>
</svg>

</div>

---

## 🌊 Data Flow Diagram

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="800" height="420">
  <defs>
    <linearGradient id="dfBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#0d0d1a"/>
      <stop offset="100%" style="stop-color:#080814"/>
    </linearGradient>
    <marker id="dfArrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#06B6D4"/>
    </marker>
    <marker id="dfArrowRed" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#f87171"/>
    </marker>
    <marker id="dfArrowGreen" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#4ade80"/>
    </marker>
  </defs>

  <rect width="800" height="420" fill="url(#dfBg)" rx="12"/>
  <rect x="0" y="0" width="800" height="4" fill="#06B6D4"/>

  <text x="400" y="28" text-anchor="middle" font-family="'Courier New', monospace"
        font-size="15" font-weight="bold" fill="#e2e8f0">Data Flow: Media Moderation Pipeline</text>

  <!-- Step 1: Media Received -->
  <rect x="30" y="50" width="130" height="50" rx="8" fill="#1e0a3c" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="95" y="72" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#c4b5fd">1. Media</text>
  <text x="95" y="88" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">Received</text>

  <!-- Arrow 1→2 -->
  <line x1="160" y1="75" x2="210" y2="75" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#dfArrow)"/>

  <!-- Step 2: Download -->
  <rect x="210" y="50" width="130" height="50" rx="8" fill="#0a1f2e" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="275" y="72" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#67e8f9">2. Download</text>
  <text x="275" y="88" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">temp file</text>

  <!-- Arrow 2→3 -->
  <line x1="340" y1="75" x2="390" y2="75" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#dfArrow)"/>

  <!-- Step 3: Classify -->
  <rect x="390" y="50" width="140" height="50" rx="8" fill="#1e0a3c" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="460" y="72" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#c4b5fd">3. Classify</text>
  <text x="460" y="88" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">ViT inference</text>

  <!-- Arrow 3→4 -->
  <line x1="530" y1="75" x2="580" y2="75" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#dfArrow)"/>

  <!-- Step 4: Decision -->
  <rect x="580" y="50" width="160" height="50" rx="8" fill="#1a1a2e" stroke="#2563EB" stroke-width="1.5"/>
  <text x="660" y="72" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#93c5fd">4. Decision</text>
  <text x="660" y="88" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">NSFW or SFW?</text>

  <!-- NSFW branch (down from decision) -->
  <line x1="660" y1="100" x2="660" y2="150" stroke="#f87171" stroke-width="1.5" marker-end="url(#dfArrowRed)"/>
  <text x="670" y="135" font-family="monospace" font-size="9" fill="#f87171">NSFW</text>

  <!-- SFW branch (right from decision then down) -->
  <line x1="660" y1="100" x2="760" y2="100" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="760" y1="100" x2="760" y2="150" stroke="#4ade80" stroke-width="1.5" marker-end="url(#dfArrowGreen)"/>
  <text x="714" y="115" text-anchor="middle" font-family="monospace" font-size="9" fill="#4ade80">SFW</text>

  <!-- NSFW action box -->
  <rect x="530" y="150" width="160" height="160" rx="8" fill="#1f0a0a" stroke="#f87171" stroke-width="1.5"/>
  <text x="610" y="172" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#f87171">NSFW Actions</text>
  <text x="610" y="192" text-anchor="middle" font-family="monospace" font-size="9" fill="#fca5a5">• Delete message</text>
  <text x="610" y="210" text-anchor="middle" font-family="monospace" font-size="9" fill="#fca5a5">• Warn user</text>
  <text x="610" y="228" text-anchor="middle" font-family="monospace" font-size="9" fill="#fca5a5">• Cache media</text>
  <text x="610" y="246" text-anchor="middle" font-family="monospace" font-size="9" fill="#fca5a5">• Notify admins</text>
  <text x="610" y="264" text-anchor="middle" font-family="monospace" font-size="9" fill="#fca5a5">• +1 violation</text>
  <text x="610" y="290" text-anchor="middle" font-family="monospace" font-size="9" fill="#fca5a5">↓ if ≥ threshold</text>
  <text x="610" y="302" text-anchor="middle" font-family="monospace" font-size="9" fill="#f87171">🔨 AUTO-BAN</text>

  <!-- SFW action box -->
  <rect x="700" y="150" width="80" height="60" rx="8" fill="#0a1f0a" stroke="#4ade80" stroke-width="1.5"/>
  <text x="740" y="175" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#4ade80">SFW</text>
  <text x="740" y="193" text-anchor="middle" font-family="monospace" font-size="9" fill="#86efac">delete temp</text>

  <!-- DB write (from NSFW box) -->
  <line x1="530" y1="270" x2="430" y2="270" stroke="#2563EB" stroke-width="1.5" marker-end="url(#dfArrow)"/>
  <rect x="280" y="250" width="150" height="50" rx="8" fill="#1a1a2e" stroke="#2563EB" stroke-width="1.5"/>
  <text x="355" y="272" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#93c5fd">SQLite Write</text>
  <text x="355" y="288" text-anchor="middle" font-family="monospace" font-size="9" fill="#64748b">violations / actions / stats</text>

  <!-- Dashboard refresh -->
  <line x1="355" y1="300" x2="355" y2="350" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#dfArrow)"/>
  <rect x="255" y="350" width="200" height="50" rx="8" fill="#0a1f2e" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="355" y="372" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#67e8f9">Dashboard Update</text>
  <text x="355" y="388" text-anchor="middle" font-family="monospace" font-size="9" fill="#94a3b8">Socket.IO push → browser</text>

  <!-- Media type note -->
  <rect x="30" y="150" width="200" height="70" rx="8" fill="#111827" stroke="#475569" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="130" y="172" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#94a3b8">Media Types</text>
  <text x="130" y="190" text-anchor="middle" font-family="monospace" font-size="9" fill="#64748b">📷 Photo → direct pipeline</text>
  <text x="130" y="206" text-anchor="middle" font-family="monospace" font-size="9" fill="#64748b">🎬 Video → 6-frame sample</text>
  <text x="130" y="222" text-anchor="middle" font-family="monospace" font-size="9" fill="#64748b">🎭 GIF/Anim → frame sample</text>
</svg>

</div>

---

## 🔧 Installation

### Prerequisites

- Python 3.10 or newer
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- At least one admin Telegram user ID
- (Optional but recommended) A CUDA-capable GPU for faster inference

### Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Kaelith69/A.R.T.E.M.I.S.S.git
cd A.R.T.E.M.I.S.S

# 2. Create a virtual environment (don't skip this, you'll regret it)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure the bot
cp .env.example .env
# Edit .env — minimum: BOT_TOKEN and ADMIN_IDS

# 5. Initialize the database
python setup_db.py

# 6. Start the bot
python artemis_bot.py

# 7. (Optional) Start the dashboard in a separate terminal
python dashboard.py
```

> 💡 First run downloads the Falconsai ViT model (~350MB) from HuggingFace. This takes a moment. Subsequent starts use the local cache. Consider getting a coffee.

### Environment Variables

| Variable | Required | Default | Description |
|---|---|---|---|
| `BOT_TOKEN` | ✅ | — | Telegram bot token from BotFather |
| `ADMIN_IDS` | ✅ | — | Comma-separated admin Telegram user IDs |
| `FLAG_THRESHOLD` | ❌ | `3` | Violations before auto-ban |
| `DB_FILE` | ❌ | `violations.db` | SQLite database path |
| `FLAGGED_IMAGES_DIR` | ❌ | `flagged_images` | Where to cache flagged images |
| `FLAGGED_VIDEOS_DIR` | ❌ | `flagged_videos` | Where to cache flagged videos |
| `DASHBOARD_SECRET_KEY` | ❌ | auto-generated | Flask session secret |

---

## 🚀 Usage

### Adding the Bot to a Group

1. Add `@YourBotUsername` to your Telegram group
2. Promote the bot to **admin** with permissions:
   - Delete messages
   - Ban users
3. Send `/start` in the group to verify the bot is alive

### Commands

| Command | Who | Description |
|---|---|---|
| `/start` | Anyone | Welcome message + quick summary |
| `/help` | Anyone | Full command list |
| `/violations` | Anyone | Check your own violation count |
| `/stats` | Anyone | View bot statistics |
| `/admin_flagged` | Admins | List all users with violations |
| `/admin_reset <user_id>` | Admins | Reset a user's violation count |
| `/admin_ban <user_id>` | Admins | Manually ban a user |

### Dashboard

Start the dashboard:

```bash
python dashboard.py
```

Then open `http://localhost:5000` in your browser. You'll see:
- Real-time scan counts
- NSFW detection totals
- Action log (deletions, bans)
- Content type breakdown

Stats update every 10 seconds via Socket.IO without refreshing.

---

## 📁 Project Structure

```
A.R.T.E.M.I.S.S/
├── artemis_bot.py        # 🤖 Core bot — all handlers, DB logic, violation engine
├── dashboard.py          # 📊 Flask + Socket.IO admin dashboard
├── setup_db.py           # 🗄️ Database init script (run once)
├── templates/
│   └── index.html        # 🖥️ Dashboard web UI (Tailwind CSS + Chart.js)
├── wiki/                 # 📚 Full documentation wiki
├── assets/               # 🎬 Demo GIFs and static assets
├── .env.example          # ⚙️ Config template — copy to .env and fill in
├── requirements.txt      # 📦 Python dependencies
├── blueprint.md          # 🗺️ Original development blueprint
└── LICENSE               # ⚖️ MIT License
```

*Auto-created at runtime:*
```
├── violations.db         # SQLite database
├── flagged_images/       # Cached flagged images
├── flagged_videos/       # Cached flagged videos
└── temp_<user_id>.*      # Ephemeral temp files (deleted after scan)
```

---

## 📈 Performance Stats

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 240" width="800" height="240">
  <defs>
    <linearGradient id="statsBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d0d1a"/>
      <stop offset="100%" style="stop-color:#080814"/>
    </linearGradient>
  </defs>

  <rect width="800" height="240" fill="url(#statsBg)" rx="12"/>
  <rect x="0" y="0" width="800" height="4" fill="#7C3AED"/>

  <text x="400" y="30" text-anchor="middle" font-family="'Courier New', monospace"
        font-size="14" font-weight="bold" fill="#e2e8f0">Runtime Characteristics</text>

  <!-- Stat card 1 -->
  <rect x="30" y="50" width="160" height="90" rx="8" fill="#1e0a3c" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="110" y="80" text-anchor="middle" font-family="monospace" font-size="24" font-weight="bold" fill="#c4b5fd">6</text>
  <text x="110" y="100" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">frames sampled</text>
  <text x="110" y="116" text-anchor="middle" font-family="monospace" font-size="10" fill="#64748b">per video</text>
  <text x="110" y="132" text-anchor="middle" font-family="monospace" font-size="9" fill="#7C3AED">early-stop on NSFW hit</text>

  <!-- Stat card 2 -->
  <rect x="210" y="50" width="160" height="90" rx="8" fill="#0a1f2e" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="290" y="80" text-anchor="middle" font-family="monospace" font-size="24" font-weight="bold" fill="#67e8f9">50%</text>
  <text x="290" y="100" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">confidence</text>
  <text x="290" y="116" text-anchor="middle" font-family="monospace" font-size="10" fill="#64748b">threshold (default)</text>
  <text x="290" y="132" text-anchor="middle" font-family="monospace" font-size="9" fill="#06B6D4">configurable</text>

  <!-- Stat card 3 -->
  <rect x="390" y="50" width="160" height="90" rx="8" fill="#1a1a2e" stroke="#2563EB" stroke-width="1.5"/>
  <text x="470" y="80" text-anchor="middle" font-family="monospace" font-size="24" font-weight="bold" fill="#93c5fd">3</text>
  <text x="470" y="100" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">default violation</text>
  <text x="470" y="116" text-anchor="middle" font-family="monospace" font-size="10" fill="#64748b">threshold</text>
  <text x="470" y="132" text-anchor="middle" font-family="monospace" font-size="9" fill="#2563EB">before auto-ban</text>

  <!-- Stat card 4 -->
  <rect x="570" y="50" width="200" height="90" rx="8" fill="#1e0a3c" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="670" y="80" text-anchor="middle" font-family="monospace" font-size="18" font-weight="bold" fill="#c4b5fd">CUDA / CPU</text>
  <text x="670" y="100" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">inference backend</text>
  <text x="670" y="116" text-anchor="middle" font-family="monospace" font-size="10" fill="#64748b">auto-detected</text>
  <text x="670" y="132" text-anchor="middle" font-family="monospace" font-size="9" fill="#7C3AED">GPU preferred</text>

  <!-- Bottom note -->
  <text x="400" y="175" text-anchor="middle" font-family="monospace" font-size="11" fill="#475569">
    Model: Falconsai/nsfw_image_detection (Vision Transformer, HuggingFace)
  </text>
  <text x="400" y="195" text-anchor="middle" font-family="monospace" font-size="11" fill="#475569">
    Framework: PyTorch ≥ 2.0 · python-telegram-bot ≥ 21.0 · Flask ≥ 3.0
  </text>
  <text x="400" y="220" text-anchor="middle" font-family="monospace" font-size="9" fill="#374151">
    Actual inference speed depends on hardware — GPU makes it dramatically faster
  </text>
</svg>

</div>

---

## 🔒 Privacy

A.R.T.E.M.I.S.S. processes user media **locally** on your server. No data is sent to any third-party cloud service.

- **Flagged media** is cached locally in `flagged_images/` and `flagged_videos/` for admin review
- **SFW media** is deleted immediately after classification
- **Violation records** contain only Telegram user IDs and counts — no names, no usernames
- The **Falconsai model** runs entirely on your machine after initial download
- **No analytics, no telemetry, no phoning home**

See [SECURITY.md](SECURITY.md) and [wiki/Privacy.md](wiki/Privacy.md) for the full picture.

---

## 🗺️ Future Roadmap

| Milestone | Feature |
|---|---|
| v0.2 | Text spam detection (NLP classifier) |
| v0.2 | Configurable ban escalation (mute → kick → ban) |
| v0.3 | Multi-group support with per-group config |
| v0.3 | Dashboard authentication (currently open, LAN-only for now) |
| v0.4 | Sticker / document NSFW detection |
| v0.5 | Rate limiting and flood protection |
| v1.0 | Docker Compose deployment |

See [wiki/Roadmap.md](wiki/Roadmap.md) for more detail.

---

## ⚖️ License

MIT License — see [LICENSE](LICENSE) for the full text.

Copyright © 2025 Kaelith69

---

<div align="center">

*Made with too much caffeine and a deep moral opposition to unsolicited NSFW content in group chats.*

</div>
