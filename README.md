<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 260" width="900" height="260">
  <defs>
    <linearGradient id="heroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d0d1a;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#12082a;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#060d1f;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="heroAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#2563EB;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#06B6D4;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#7C3AED;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#06B6D4;stop-opacity:1" />
    </linearGradient>
    <filter id="heroGlow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="subtleGlow">
      <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
      <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <!-- Grid pattern -->
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#7C3AED" stroke-width="0.3" stroke-opacity="0.15"/>
    </pattern>
  </defs>
  <!-- Background -->
  <rect width="900" height="260" fill="url(#heroBg)" rx="16"/>
  <!-- Grid overlay -->
  <rect width="900" height="260" fill="url(#grid)" rx="16"/>
  <!-- Top accent bar -->
  <rect x="0" y="0" width="900" height="4" fill="url(#heroAccent)" rx="2"/>
  <!-- Bottom accent bar -->
  <rect x="0" y="256" width="900" height="4" fill="url(#heroAccent)" rx="2"/>
  <!-- Decorative circles (background nodes) -->
  <circle cx="820" cy="50" r="60" fill="#7C3AED" fill-opacity="0.05" stroke="#7C3AED" stroke-width="0.5" stroke-opacity="0.2"/>
  <circle cx="820" cy="50" r="35" fill="#7C3AED" fill-opacity="0.07" stroke="#7C3AED" stroke-width="0.5" stroke-opacity="0.3"/>
  <circle cx="80" cy="210" r="50" fill="#06B6D4" fill-opacity="0.04" stroke="#06B6D4" stroke-width="0.5" stroke-opacity="0.2"/>
  <!-- Shield symbol (left) -->
  <g transform="translate(72, 80)">
    <!-- Shield body -->
    <path d="M0,0 L50,0 L50,55 Q25,75 0,55 Z" fill="url(#shieldGrad)" fill-opacity="0.25" stroke="url(#shieldGrad)" stroke-width="1.5" filter="url(#heroGlow)"/>
    <!-- Shield inner check -->
    <path d="M12,28 L22,38 L38,18" stroke="#06B6D4" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round" filter="url(#subtleGlow)"/>
    <!-- Eye symbol inside shield -->
    <ellipse cx="25" cy="30" rx="10" ry="6" fill="none" stroke="#a78bfa" stroke-width="1.2" opacity="0.6"/>
    <circle cx="25" cy="30" r="3" fill="#7C3AED" opacity="0.8"/>
  </g>
  <!-- Main title -->
  <text x="460" y="88" font-family="'Courier New', Courier, monospace" font-size="40" font-weight="bold" fill="#ffffff" text-anchor="middle" filter="url(#heroGlow)" letter-spacing="3">A.R.T.E.M.I.S.S.</text>
  <!-- Gradient underline -->
  <rect x="200" y="97" width="520" height="2" fill="url(#heroAccent)" rx="1" opacity="0.7"/>
  <!-- Subtitle line 1 -->
  <text x="460" y="122" font-family="'Courier New', Courier, monospace" font-size="12" fill="#a78bfa" text-anchor="middle" letter-spacing="1">Automated Review for Telegram Environments</text>
  <!-- Subtitle line 2 -->
  <text x="460" y="140" font-family="'Courier New', Courier, monospace" font-size="12" fill="#93c5fd" text-anchor="middle" letter-spacing="1">Monitoring Inappropriate Submissions System</text>
  <!-- Tag pills -->
  <rect x="190" y="162" width="90" height="24" rx="12" fill="#7C3AED" fill-opacity="0.18" stroke="#7C3AED" stroke-width="1"/>
  <text x="235" y="178" font-family="monospace" font-size="10" fill="#a78bfa" text-anchor="middle" font-weight="bold">🤖 Telegram Bot</text>
  <rect x="294" y="162" width="72" height="24" rx="12" fill="#2563EB" fill-opacity="0.18" stroke="#2563EB" stroke-width="1"/>
  <text x="330" y="178" font-family="monospace" font-size="10" fill="#93c5fd" text-anchor="middle" font-weight="bold">AI / ML</text>
  <rect x="380" y="162" width="96" height="24" rx="12" fill="#06B6D4" fill-opacity="0.18" stroke="#06B6D4" stroke-width="1"/>
  <text x="428" y="178" font-family="monospace" font-size="10" fill="#67e8f9" text-anchor="middle" font-weight="bold">Python 3.10+</text>
  <rect x="490" y="162" width="72" height="24" rx="12" fill="#7C3AED" fill-opacity="0.18" stroke="#7C3AED" stroke-width="1"/>
  <text x="526" y="178" font-family="monospace" font-size="10" fill="#a78bfa" text-anchor="middle" font-weight="bold">HuggingFace</text>
  <rect x="576" y="162" width="76" height="24" rx="12" fill="#2563EB" fill-opacity="0.18" stroke="#2563EB" stroke-width="1"/>
  <text x="614" y="178" font-family="monospace" font-size="10" fill="#93c5fd" text-anchor="middle" font-weight="bold">MIT License</text>
  <!-- Tagline -->
  <text x="460" y="220" font-family="monospace" font-size="11" fill="#6b7280" text-anchor="middle" font-style="italic">AI-powered NSFW content moderation for Telegram groups — zero manual review required</text>
  <!-- Corner decorations -->
  <line x1="16" y1="16" x2="40" y2="16" stroke="#7C3AED" stroke-width="1.5" stroke-opacity="0.6"/>
  <line x1="16" y1="16" x2="16" y2="40" stroke="#7C3AED" stroke-width="1.5" stroke-opacity="0.6"/>
  <line x1="884" y1="16" x2="860" y2="16" stroke="#06B6D4" stroke-width="1.5" stroke-opacity="0.6"/>
  <line x1="884" y1="16" x2="884" y2="40" stroke="#06B6D4" stroke-width="1.5" stroke-opacity="0.6"/>
  <line x1="16" y1="244" x2="40" y2="244" stroke="#06B6D4" stroke-width="1.5" stroke-opacity="0.6"/>
  <line x1="16" y1="244" x2="16" y2="220" stroke="#06B6D4" stroke-width="1.5" stroke-opacity="0.6"/>
  <line x1="884" y1="244" x2="860" y2="244" stroke="#7C3AED" stroke-width="1.5" stroke-opacity="0.6"/>
  <line x1="884" y1="244" x2="884" y2="220" stroke="#7C3AED" stroke-width="1.5" stroke-opacity="0.6"/>
</svg>

</div>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-ffca28?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/Falconsai/nsfw_image_detection)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-ee4c2c?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot_API-26a5e4?style=flat-square&logo=telegram&logoColor=white)](https://core.telegram.org/bots)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-black?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003b57?style=flat-square&logo=sqlite&logoColor=white)](https://sqlite.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-7c3aed?style=flat-square)](LICENSE)

</div>

---

**A.R.T.E.M.I.S.S.** is an AI-powered Telegram group moderation bot that automatically detects and removes NSFW (Not Safe For Work) images, videos, and GIFs using state-of-the-art Vision Transformer models. It tracks repeat offenders, notifies administrators in real time, and auto-bans users who exceed a configurable violation threshold — all with zero manual review required.

---

## 📋 Table of Contents

- [System Overview](#-system-overview)
- [Core Capabilities](#-core-capabilities)
- [Architecture](#-architecture)
- [Data Flow](#-data-flow)
- [Technology Stack](#-technology-stack)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration Reference](#-configuration-reference)
- [Bot Commands](#-bot-commands)
- [Dashboard](#-dashboard)
- [Database Schema](#-database-schema)
- [Project Structure](#-project-structure)
- [Performance](#-performance)
- [Accessibility](#-accessibility)
- [Privacy & Security Model](#-privacy--security-model)
- [Design Principles](#-design-principles)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔭 System Overview

A.R.T.E.M.I.S.S. operates as a persistent Python process connected to Telegram's Bot API via long-polling. When a user sends media to a monitored group, the bot intercepts the update, classifies the content using a Vision Transformer (ViT) model hosted on HuggingFace, and takes automatic enforcement action based on the result. An independent Flask + Socket.IO dashboard provides administrators with real-time analytics and audit logs without requiring any direct bot interaction.

---

## 🧠 Core Capabilities

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 360" width="820" height="360">
  <defs>
    <linearGradient id="capBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d0d1a;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#0f172a;stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="capAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
    <filter id="capGlow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="820" height="360" fill="url(#capBg)" rx="14"/>
  <rect x="0" y="0" width="820" height="3" fill="url(#capAccent)" rx="1"/>
  <text x="410" y="32" font-family="monospace" font-size="14" fill="#a78bfa" text-anchor="middle" font-weight="bold" letter-spacing="2">CORE CAPABILITY MAP</text>

  <!-- Central node -->
  <circle cx="410" cy="185" r="46" fill="#7C3AED" fill-opacity="0.2" stroke="#7C3AED" stroke-width="2" filter="url(#capGlow)"/>
  <circle cx="410" cy="185" r="30" fill="#7C3AED" fill-opacity="0.35" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="410" y="182" font-family="monospace" font-size="9" fill="#e9d5ff" text-anchor="middle" font-weight="bold">A.R.T.E.M.I.S.S</text>
  <text x="410" y="196" font-family="monospace" font-size="8" fill="#c4b5fd" text-anchor="middle">Core Engine</text>

  <!-- Satellite nodes with connecting lines -->
  <!-- Image Detection (top-left) -->
  <line x1="375" y1="152" x2="215" y2="95" stroke="#7C3AED" stroke-width="1" stroke-dasharray="4,3" stroke-opacity="0.6"/>
  <circle cx="185" cy="80" r="36" fill="#2563EB" fill-opacity="0.18" stroke="#2563EB" stroke-width="1.5"/>
  <text x="185" y="76" font-family="monospace" font-size="9" fill="#93c5fd" text-anchor="middle" font-weight="bold">🖼️ Image</text>
  <text x="185" y="90" font-family="monospace" font-size="9" fill="#93c5fd" text-anchor="middle">Detection</text>

  <!-- Video Analysis (top-right) -->
  <line x1="445" y1="152" x2="605" y2="95" stroke="#7C3AED" stroke-width="1" stroke-dasharray="4,3" stroke-opacity="0.6"/>
  <circle cx="635" cy="80" r="36" fill="#2563EB" fill-opacity="0.18" stroke="#2563EB" stroke-width="1.5"/>
  <text x="635" y="76" font-family="monospace" font-size="9" fill="#93c5fd" text-anchor="middle" font-weight="bold">🎬 Video</text>
  <text x="635" y="90" font-family="monospace" font-size="9" fill="#93c5fd" text-anchor="middle">Analysis</text>

  <!-- Violation Engine (left) -->
  <line x1="364" y1="185" x2="228" y2="185" stroke="#06B6D4" stroke-width="1" stroke-dasharray="4,3" stroke-opacity="0.6"/>
  <circle cx="192" cy="185" r="36" fill="#06B6D4" fill-opacity="0.15" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="192" y="181" font-family="monospace" font-size="9" fill="#67e8f9" text-anchor="middle" font-weight="bold">⚠️ Violation</text>
  <text x="192" y="195" font-family="monospace" font-size="9" fill="#67e8f9" text-anchor="middle">Tracking</text>

  <!-- Auto-Ban (right) -->
  <line x1="456" y1="185" x2="592" y2="185" stroke="#06B6D4" stroke-width="1" stroke-dasharray="4,3" stroke-opacity="0.6"/>
  <circle cx="628" cy="185" r="36" fill="#06B6D4" fill-opacity="0.15" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="628" y="181" font-family="monospace" font-size="9" fill="#67e8f9" text-anchor="middle" font-weight="bold">🚫 Auto-Ban</text>
  <text x="628" y="195" font-family="monospace" font-size="9" fill="#67e8f9" text-anchor="middle">Engine</text>

  <!-- Admin Notify (bottom-left) -->
  <line x1="375" y1="218" x2="215" y2="275" stroke="#7C3AED" stroke-width="1" stroke-dasharray="4,3" stroke-opacity="0.6"/>
  <circle cx="185" cy="290" r="36" fill="#7C3AED" fill-opacity="0.18" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="185" y="286" font-family="monospace" font-size="9" fill="#c4b5fd" text-anchor="middle" font-weight="bold">📣 Admin</text>
  <text x="185" y="300" font-family="monospace" font-size="9" fill="#c4b5fd" text-anchor="middle">Notifications</text>

  <!-- Dashboard (bottom-right) -->
  <line x1="445" y1="218" x2="605" y2="275" stroke="#7C3AED" stroke-width="1" stroke-dasharray="4,3" stroke-opacity="0.6"/>
  <circle cx="635" cy="290" r="36" fill="#7C3AED" fill-opacity="0.18" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="635" y="286" font-family="monospace" font-size="9" fill="#c4b5fd" text-anchor="middle" font-weight="bold">📊 Real-Time</text>
  <text x="635" y="300" font-family="monospace" font-size="9" fill="#c4b5fd" text-anchor="middle">Dashboard</text>

  <!-- Bottom label -->
  <text x="410" y="345" font-family="monospace" font-size="10" fill="#4b5563" text-anchor="middle">ViT-based classification · SQLite persistence · Flask + Socket.IO analytics</text>
</svg>

</div>

---

## 🏗️ Architecture

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 420" width="820" height="420">
  <defs>
    <linearGradient id="archBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d0d1a;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#0f172a;stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="archAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
    <marker id="arrowBlue" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#2563EB"/>
    </marker>
    <marker id="arrowCyan" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#06B6D4"/>
    </marker>
    <marker id="arrowPurple" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#7C3AED"/>
    </marker>
  </defs>
  <rect width="820" height="420" fill="url(#archBg)" rx="14"/>
  <rect x="0" y="0" width="820" height="3" fill="url(#archAccent)" rx="1"/>
  <text x="410" y="28" font-family="monospace" font-size="13" fill="#a78bfa" text-anchor="middle" font-weight="bold" letter-spacing="2">SYSTEM ARCHITECTURE</text>

  <!-- Layer labels -->
  <text x="14" y="72" font-family="monospace" font-size="9" fill="#6b7280" transform="rotate(-90, 14, 72)" text-anchor="middle">INTERFACE</text>
  <text x="14" y="192" font-family="monospace" font-size="9" fill="#6b7280" transform="rotate(-90, 14, 192)">CORE</text>
  <text x="14" y="310" font-family="monospace" font-size="9" fill="#6b7280" transform="rotate(-90, 14, 310)">STORAGE</text>

  <!-- Layer dividers -->
  <line x1="30" y1="120" x2="790" y2="120" stroke="#1f2937" stroke-width="1" stroke-dasharray="6,4"/>
  <line x1="30" y1="250" x2="790" y2="250" stroke="#1f2937" stroke-width="1" stroke-dasharray="6,4"/>
  <line x1="30" y1="360" x2="790" y2="360" stroke="#1f2937" stroke-width="1" stroke-dasharray="6,4"/>

  <!-- ── INTERFACE LAYER ── -->
  <!-- Telegram Users box -->
  <rect x="50" y="50" width="130" height="52" rx="8" fill="#2563EB" fill-opacity="0.15" stroke="#2563EB" stroke-width="1.5"/>
  <text x="115" y="72" font-family="monospace" font-size="10" fill="#93c5fd" text-anchor="middle" font-weight="bold">👤 Telegram</text>
  <text x="115" y="88" font-family="monospace" font-size="10" fill="#93c5fd" text-anchor="middle">Group Users</text>

  <!-- Telegram API box -->
  <rect x="330" y="50" width="160" height="52" rx="8" fill="#06B6D4" fill-opacity="0.12" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="410" y="72" font-family="monospace" font-size="10" fill="#67e8f9" text-anchor="middle" font-weight="bold">☁️ Telegram Bot</text>
  <text x="410" y="88" font-family="monospace" font-size="10" fill="#67e8f9" text-anchor="middle">API (Long-Poll)</text>

  <!-- Admin browser -->
  <rect x="630" y="50" width="140" height="52" rx="8" fill="#7C3AED" fill-opacity="0.15" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="700" y="72" font-family="monospace" font-size="10" fill="#c4b5fd" text-anchor="middle" font-weight="bold">🌐 Admin</text>
  <text x="700" y="88" font-family="monospace" font-size="10" fill="#c4b5fd" text-anchor="middle">Browser / Dashboard</text>

  <!-- Arrows from Users → API -->
  <line x1="180" y1="76" x2="328" y2="76" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrowBlue)"/>
  <text x="254" y="70" font-family="monospace" font-size="8" fill="#6b7280" text-anchor="middle">media / commands</text>

  <!-- Arrow API → artemis_bot -->
  <line x1="410" y1="102" x2="410" y2="148" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#arrowCyan)"/>

  <!-- Arrow dashboard → Admin -->
  <line x1="700" y1="148" x2="700" y2="102" stroke="#7C3AED" stroke-width="1.5" marker-end="url(#arrowPurple)"/>

  <!-- ── CORE LAYER ── -->
  <!-- artemis_bot.py -->
  <rect x="50" y="148" width="480" height="80" rx="8" fill="#7C3AED" fill-opacity="0.12" stroke="#7C3AED" stroke-width="2"/>
  <text x="290" y="170" font-family="monospace" font-size="11" fill="#c4b5fd" text-anchor="middle" font-weight="bold">⚙️  artemis_bot.py  —  Core Processing Engine</text>
  <!-- Sub-boxes inside artemis_bot -->
  <rect x="68" y="182" width="88" height="32" rx="5" fill="#2563EB" fill-opacity="0.2" stroke="#2563EB" stroke-width="1"/>
  <text x="112" y="202" font-family="monospace" font-size="8" fill="#93c5fd" text-anchor="middle">Image Handler</text>
  <rect x="168" y="182" width="88" height="32" rx="5" fill="#2563EB" fill-opacity="0.2" stroke="#2563EB" stroke-width="1"/>
  <text x="212" y="202" font-family="monospace" font-size="8" fill="#93c5fd" text-anchor="middle">Video Handler</text>
  <rect x="268" y="182" width="88" height="32" rx="5" fill="#06B6D4" fill-opacity="0.18" stroke="#06B6D4" stroke-width="1"/>
  <text x="312" y="202" font-family="monospace" font-size="8" fill="#67e8f9" text-anchor="middle">Action Decider</text>
  <rect x="368" y="182" width="88" height="32" rx="5" fill="#06B6D4" fill-opacity="0.18" stroke="#06B6D4" stroke-width="1"/>
  <text x="412" y="202" font-family="monospace" font-size="8" fill="#67e8f9" text-anchor="middle">Admin Commands</text>

  <!-- dashboard.py -->
  <rect x="580" y="148" width="190" height="80" rx="8" fill="#06B6D4" fill-opacity="0.1" stroke="#06B6D4" stroke-width="2"/>
  <text x="675" y="170" font-family="monospace" font-size="11" fill="#67e8f9" text-anchor="middle" font-weight="bold">📊 dashboard.py</text>
  <text x="675" y="188" font-family="monospace" font-size="8" fill="#67e8f9" text-anchor="middle">Flask REST API</text>
  <text x="675" y="202" font-family="monospace" font-size="8" fill="#67e8f9" text-anchor="middle">Socket.IO WebSocket</text>
  <text x="675" y="216" font-family="monospace" font-size="8" fill="#67e8f9" text-anchor="middle">Chart.js Visualisation</text>

  <!-- ML Layer arrows -->
  <line x1="290" y1="228" x2="290" y2="262" stroke="#7C3AED" stroke-width="1.5" marker-end="url(#arrowPurple)"/>

  <!-- ML Models box -->
  <rect x="50" y="262" width="480" height="74" rx="8" fill="#2563EB" fill-opacity="0.1" stroke="#2563EB" stroke-width="1.5"/>
  <text x="290" y="283" font-family="monospace" font-size="11" fill="#93c5fd" text-anchor="middle" font-weight="bold">🤖  ML Inference Layer  (HuggingFace / PyTorch)</text>
  <rect x="68" y="294" width="140" height="30" rx="5" fill="#7C3AED" fill-opacity="0.2" stroke="#7C3AED" stroke-width="1"/>
  <text x="138" y="313" font-family="monospace" font-size="8" fill="#c4b5fd" text-anchor="middle">HF pipeline (image-class)</text>
  <rect x="230" y="294" width="140" height="30" rx="5" fill="#7C3AED" fill-opacity="0.2" stroke="#7C3AED" stroke-width="1"/>
  <text x="300" y="313" font-family="monospace" font-size="8" fill="#c4b5fd" text-anchor="middle">VideoContentAnalyzer</text>
  <rect x="392" y="294" width="118" height="30" rx="5" fill="#7C3AED" fill-opacity="0.2" stroke="#7C3AED" stroke-width="1"/>
  <text x="451" y="313" font-family="monospace" font-size="8" fill="#c4b5fd" text-anchor="middle">ViTImageProcessor</text>

  <!-- ML → Storage arrow -->
  <line x1="290" y1="336" x2="290" y2="372" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#arrowCyan)"/>
  <!-- dashboard → storage arrow -->
  <line x1="675" y1="228" x2="675" y2="372" stroke="#06B6D4" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arrowCyan)"/>

  <!-- ── STORAGE LAYER ── -->
  <rect x="50" y="372" width="720" height="36" rx="8" fill="#06B6D4" fill-opacity="0.08" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="162" y="394" font-family="monospace" font-size="9" fill="#67e8f9" text-anchor="middle">🗄️ SQLite: violations</text>
  <text x="322" y="394" font-family="monospace" font-size="9" fill="#67e8f9" text-anchor="middle">📋 SQLite: actions</text>
  <text x="470" y="394" font-family="monospace" font-size="9" fill="#67e8f9" text-anchor="middle">📊 SQLite: stats</text>
  <text x="630" y="394" font-family="monospace" font-size="9" fill="#67e8f9" text-anchor="middle">📁 Filesystem: flagged media</text>

  <!-- dividers inside storage -->
  <line x1="240" y1="372" x2="240" y2="408" stroke="#06B6D4" stroke-width="0.5" stroke-opacity="0.4"/>
  <line x1="400" y1="372" x2="400" y2="408" stroke="#06B6D4" stroke-width="0.5" stroke-opacity="0.4"/>
  <line x1="548" y1="372" x2="548" y2="408" stroke="#06B6D4" stroke-width="0.5" stroke-opacity="0.4"/>
</svg>

</div>

---

## 🔄 Data Flow

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 480" width="820" height="480">
  <defs>
    <linearGradient id="dfBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d0d1a;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#0f172a;stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="dfAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
    <marker id="dfArrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#06B6D4"/>
    </marker>
    <marker id="dfArrowRed" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#ef4444"/>
    </marker>
    <marker id="dfArrowGreen" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#10b981"/>
    </marker>
  </defs>
  <rect width="820" height="480" fill="url(#dfBg)" rx="14"/>
  <rect x="0" y="0" width="820" height="3" fill="url(#dfAccent)" rx="1"/>
  <text x="410" y="26" font-family="monospace" font-size="13" fill="#a78bfa" text-anchor="middle" font-weight="bold" letter-spacing="2">MEDIA PROCESSING DATA FLOW</text>

  <!-- Step 1: User sends media -->
  <rect x="300" y="46" width="220" height="40" rx="8" fill="#2563EB" fill-opacity="0.2" stroke="#2563EB" stroke-width="1.5"/>
  <text x="410" y="71" font-family="monospace" font-size="10" fill="#93c5fd" text-anchor="middle" font-weight="bold">1. User sends media to group</text>
  <line x1="410" y1="86" x2="410" y2="112" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#dfArrow)"/>

  <!-- Step 2: Message handler -->
  <rect x="300" y="112" width="220" height="40" rx="8" fill="#7C3AED" fill-opacity="0.18" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="410" y="137" font-family="monospace" font-size="10" fill="#c4b5fd" text-anchor="middle" font-weight="bold">2. MessageHandler intercepts</text>
  <!-- Branch arrow -->
  <line x1="410" y1="152" x2="410" y2="178" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#dfArrow)"/>

  <!-- Decision diamond: Image or Video? -->
  <polygon points="410,178 510,210 410,242 310,210" fill="#06B6D4" fill-opacity="0.12" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="410" y="206" font-family="monospace" font-size="9" fill="#67e8f9" text-anchor="middle" font-weight="bold">Image or</text>
  <text x="410" y="220" font-family="monospace" font-size="9" fill="#67e8f9" text-anchor="middle" font-weight="bold">Video/GIF?</text>

  <!-- Left branch: Image -->
  <line x1="310" y1="210" x2="170" y2="210" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#dfArrow)"/>
  <text x="240" y="204" font-family="monospace" font-size="8" fill="#6b7280" text-anchor="middle">Image</text>
  <rect x="60" y="190" width="110" height="40" rx="7" fill="#2563EB" fill-opacity="0.18" stroke="#2563EB" stroke-width="1.2"/>
  <text x="115" y="209" font-family="monospace" font-size="8" fill="#93c5fd" text-anchor="middle">HF pipeline</text>
  <text x="115" y="223" font-family="monospace" font-size="8" fill="#93c5fd" text-anchor="middle">image-classification</text>
  <line x1="115" y1="230" x2="115" y2="272" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#dfArrow)"/>

  <!-- Right branch: Video/GIF -->
  <line x1="510" y1="210" x2="650" y2="210" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#dfArrow)"/>
  <text x="580" y="204" font-family="monospace" font-size="8" fill="#6b7280" text-anchor="middle">Video/GIF</text>
  <rect x="650" y="190" width="120" height="40" rx="7" fill="#2563EB" fill-opacity="0.18" stroke="#2563EB" stroke-width="1.2"/>
  <text x="710" y="207" font-family="monospace" font-size="8" fill="#93c5fd" text-anchor="middle">VideoContent</text>
  <text x="710" y="221" font-family="monospace" font-size="8" fill="#93c5fd" text-anchor="middle">Analyzer (6 frames)</text>
  <line x1="710" y1="230" x2="710" y2="272" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#dfArrow)"/>

  <!-- Converge to classifier result -->
  <rect x="60" y="272" width="110" height="36" rx="7" fill="#7C3AED" fill-opacity="0.2" stroke="#7C3AED" stroke-width="1.2"/>
  <text x="115" y="289" font-family="monospace" font-size="8" fill="#c4b5fd" text-anchor="middle">ViT Classifier</text>
  <text x="115" y="302" font-family="monospace" font-size="8" fill="#c4b5fd" text-anchor="middle">label + score</text>

  <rect x="650" y="272" width="120" height="36" rx="7" fill="#7C3AED" fill-opacity="0.2" stroke="#7C3AED" stroke-width="1.2"/>
  <text x="710" y="289" font-family="monospace" font-size="8" fill="#c4b5fd" text-anchor="middle">Frame classifier</text>
  <text x="710" y="302" font-family="monospace" font-size="8" fill="#c4b5fd" text-anchor="middle">label + score</text>

  <!-- Both converge to decision -->
  <line x1="170" y1="290" x2="295" y2="326" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#dfArrow)"/>
  <line x1="650" y1="290" x2="525" y2="326" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#dfArrow)"/>

  <!-- Decision: NSFW? -->
  <polygon points="410,326 510,354 410,382 310,354" fill="#06B6D4" fill-opacity="0.12" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="410" y="350" font-family="monospace" font-size="9" fill="#67e8f9" text-anchor="middle" font-weight="bold">NSFW?</text>
  <text x="410" y="365" font-family="monospace" font-size="9" fill="#67e8f9" text-anchor="middle" font-weight="bold">(conf ≥ 0.5)</text>

  <!-- Yes path: NSFW actions -->
  <line x1="310" y1="354" x2="170" y2="354" stroke="#ef4444" stroke-width="1.5" marker-end="url(#dfArrowRed)"/>
  <text x="240" y="348" font-family="monospace" font-size="8" fill="#ef4444" text-anchor="middle">YES</text>
  <rect x="50" y="380" width="230" height="80" rx="7" fill="#ef4444" fill-opacity="0.08" stroke="#ef4444" stroke-width="1.2"/>
  <text x="165" y="400" font-family="monospace" font-size="8" fill="#fca5a5" text-anchor="middle" font-weight="bold">ENFORCEMENT ACTIONS</text>
  <text x="165" y="416" font-family="monospace" font-size="8" fill="#fca5a5" text-anchor="middle">→ Delete message</text>
  <text x="165" y="430" font-family="monospace" font-size="8" fill="#fca5a5" text-anchor="middle">→ Increment violation count</text>
  <text x="165" y="444" font-family="monospace" font-size="8" fill="#fca5a5" text-anchor="middle">→ Notify admins + cache media</text>
  <text x="165" y="458" font-family="monospace" font-size="8" fill="#fca5a5" text-anchor="middle">→ Auto-ban if threshold reached</text>

  <!-- No path: SFW -->
  <line x1="510" y1="354" x2="640" y2="354" stroke="#10b981" stroke-width="1.5" marker-end="url(#dfArrowGreen)"/>
  <text x="575" y="348" font-family="monospace" font-size="8" fill="#10b981" text-anchor="middle">NO</text>
  <rect x="640" y="334" width="130" height="40" rx="7" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.2"/>
  <text x="705" y="353" font-family="monospace" font-size="8" fill="#6ee7b7" text-anchor="middle">✅ SFW — no action</text>
  <text x="705" y="367" font-family="monospace" font-size="8" fill="#6ee7b7" text-anchor="middle">temp file removed</text>

  <!-- Both → DB update -->
  <line x1="280" y1="420" x2="390" y2="462" stroke="#06B6D4" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#dfArrow)"/>
  <line x1="705" y1="374" x2="460" y2="462" stroke="#06B6D4" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#dfArrow)"/>
  <rect x="390" y="462" width="240" height="14" rx="5" fill="#06B6D4" fill-opacity="0.12" stroke="#06B6D4" stroke-width="1"/>
  <text x="510" y="473" font-family="monospace" font-size="8" fill="#67e8f9" text-anchor="middle">SQLite update (stats · actions · contents)</text>
</svg>

</div>

---

## 🛠️ Technology Stack

| Layer | Technology | Version | Purpose |
|---|---|---|---|
| **Language** | Python | 3.10+ | Core runtime |
| **Bot Framework** | python-telegram-bot | ≥ 21.0 | Telegram API integration |
| **ML Framework** | PyTorch | ≥ 2.0 | Deep learning inference backend |
| **Model Hub** | HuggingFace Transformers | ≥ 4.30 | ViT model loading & inference |
| **NSFW Model** | Falconsai/nsfw_image_detection | latest | Vision Transformer classifier |
| **Image Processing** | Pillow | ≥ 10.0 | Image manipulation & format conversion |
| **Video Processing** | OpenCV Headless | ≥ 4.8 | Frame extraction from videos & GIFs |
| **Database** | SQLite3 | stdlib | Violation & statistics persistence |
| **Web Server** | Flask | ≥ 3.0 | Dashboard HTTP server |
| **Real-time** | Flask-SocketIO | ≥ 5.3 | WebSocket push for live dashboard |
| **Dashboard UI** | Tailwind CSS + Chart.js | CDN | Visualisation frontend |
| **Config** | python-dotenv | ≥ 1.0 | Environment variable management |

---

## ✨ Features

| Feature | Description |
|---|---|
| 🖼️ **Image Moderation** | Scans every photo with [Falconsai/nsfw_image_detection](https://huggingface.co/Falconsai/nsfw_image_detection) using HuggingFace `pipeline("image-classification")` |
| 🎬 **Video & GIF Moderation** | Samples 6 evenly-spaced frames per video via OpenCV; stops immediately on NSFW detection |
| ⚠️ **Violation Tracking** | Persists per-user violation counts to SQLite — survives bot restarts |
| 🚫 **Auto-Ban** | Automatically bans users who exceed the configurable `FLAG_THRESHOLD` (default: 3) |
| 📣 **Admin Notifications** | Forwards flagged media and alert messages directly to all configured admin Telegram IDs |
| 🗄️ **Evidence Caching** | Archives flagged images and videos to disk with timestamped filenames for audit |
| 📊 **Real-Time Dashboard** | Flask + Socket.IO dashboard with 5 live Chart.js graphs updating every 10 seconds |
| 🛡️ **Chat Owner Protection** | Gracefully handles the Telegram `Can't remove chat owner` error — no crash |
| 🔧 **Environment-Variable Config** | All secrets and operational settings live in `.env` — nothing is hard-coded |
| 🤖 **GPU Acceleration** | Auto-detects CUDA GPUs; falls back to CPU if unavailable |
| 📋 **Full Audit Log** | Every moderation action (content_removed, user_banned) is logged with timestamp |
| 📈 **Statistics Tracking** | Tracks total_contents_scanned, total_nsfw_detected, total_sfw, total_users_banned, total_violations |

---

## 🚀 Installation

### Prerequisites

- Python **3.10** or later
- A Telegram **Bot Token** — create one with [@BotFather](https://t.me/BotFather)
- The bot must be added to your group as an **admin** with *Delete Messages* and *Ban Users* permissions
- *(Optional)* A CUDA-capable GPU for faster inference

### 1 — Clone the Repository

```bash
git clone https://github.com/Kaelith69/A.R.T.E.M.I.S.S.git
cd A.R.T.E.M.I.S.S
```

### 2 — Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows
```

### 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

> **GPU users:** install the CUDA-enabled PyTorch wheel first:  
> `pip install torch --index-url https://download.pytorch.org/whl/cu121`

### 4 — Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your values:

```env
BOT_TOKEN=1234567890:AAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ADMIN_IDS=123456789,987654321
FLAG_THRESHOLD=3
DB_FILE=violations.db
FLAGGED_IMAGES_DIR=flagged_images
FLAGGED_VIDEOS_DIR=flagged_videos
DASHBOARD_SECRET_KEY=change_me_to_a_long_random_string
```

### 5 — Initialise the Database

```bash
python setup_db.py
```

### 6 — Run the Bot

```bash
python artemis_bot.py
```

### 7 — (Optional) Run the Dashboard

```bash
python dashboard.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 💻 Usage

### Monitoring a Group

1. Add the bot to your Telegram group.
2. Promote it to **admin** with *Delete Messages* and *Ban Users* permissions.
3. Start the bot process: `python artemis_bot.py`.
4. The bot will silently monitor all media sent to the group.

### Violation Lifecycle

```
Violation 1  →  warning message sent to user in group
Violation 2  →  warning message sent to user in group
Violation 3  →  user banned from group (configurable via FLAG_THRESHOLD)
             →  violation count reset
             →  all configured admins notified with the cached flagged media
```

---

## ⚙️ Configuration Reference

All configuration is done via environment variables (loaded from `.env`).

| Variable | Required | Default | Description |
|---|---|---|---|
| `BOT_TOKEN` | ✅ | — | Telegram bot token from @BotFather |
| `ADMIN_IDS` | ✅ | — | Comma-separated Telegram user IDs of admins |
| `FLAG_THRESHOLD` | ❌ | `3` | Violations before auto-ban |
| `DB_FILE` | ❌ | `violations.db` | Path to the SQLite database file |
| `FLAGGED_IMAGES_DIR` | ❌ | `flagged_images` | Directory for cached flagged images |
| `FLAGGED_VIDEOS_DIR` | ❌ | `flagged_videos` | Directory for cached flagged videos |
| `DASHBOARD_SECRET_KEY` | ❌ | random UUID | Flask session secret key |

---

## 🤖 Bot Commands

| Command | Access | Description |
|---|---|---|
| `/start` | All users | Welcome message and system overview |
| `/help` | All users | Full command reference |
| `/violations` | All users | Check your own current violation count |
| `/stats` | All users | View aggregate bot statistics |
| `/admin_flagged` | Admin only | List all users with active violations |
| `/admin_reset <user_id>` | Admin only | Reset a specific user's violation count |
| `/admin_ban <user_id>` | Admin only | Manually ban a user from the group |

---

## 📊 Dashboard

The optional Flask dashboard provides a real-time administrative view:

| Panel | Type | Description |
|---|---|---|
| **Total Scanned** | Status card | Total content items processed |
| **NSFW Detected** | Status card | Total items flagged as NSFW |
| **SFW Detected** | Status card | Total items passed as safe |
| **Users Banned** | Status card | Total unique bans issued |
| **Current Violations** | Status card | Total accumulated violations |
| **Action Trend** | Line chart | Moderation actions over time |
| **Content Breakdown** | Bar chart | SFW vs NSFW comparison |
| **Actions Distribution** | Doughnut chart | Breakdown by action type |
| **Stats Overview** | Horizontal bar | All stats in one view |
| **Analytics Comparison** | Multi-line chart | NSFW, SFW, and bans over time |
| **Recent Actions** | Live feed | Real-time audit log feed |

Data refreshes automatically every **10 seconds** via Socket.IO.

---

## 🗄️ Database Schema

```sql
-- Per-user violation counts (upserted on every NSFW detection)
CREATE TABLE violations (
    user_id INTEGER PRIMARY KEY,
    count   INTEGER
);

-- Aggregate system statistics (keyed counters)
CREATE TABLE stats (
    key   TEXT PRIMARY KEY,
    value INTEGER
);

-- Full moderation audit log
CREATE TABLE actions (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id   INTEGER,
    action    TEXT,     -- 'content_removed' | 'user_banned'
    timestamp TEXT
);

-- Individual content scan records
CREATE TABLE contents (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    type    TEXT,      -- 'image' | 'video'
    is_nsfw INTEGER    -- 0 (SFW) | 1 (NSFW)
);
```

---

## 📁 Project Structure

```
A.R.T.E.M.I.S.S/
├── artemis_bot.py          # Main bot: Telegram handlers, ML inference, DB logic, enforcement
├── dashboard.py            # Flask + Socket.IO admin dashboard (REST API + WebSocket)
├── setup_db.py             # One-shot database initialisation script
├── templates/
│   └── index.html          # Dashboard UI — Tailwind CSS + Chart.js
├── .env.example            # Environment variable template (safe to commit)
├── .gitignore              # Excludes .env, flagged media dirs, violations.db, __pycache__
├── requirements.txt        # Python package dependencies
├── blueprint.md            # Development blueprint and module design notes
└── violations.db           # SQLite database (created at runtime — git-ignored)
```

---

## ⚡ Performance

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 200" width="820" height="200">
  <defs>
    <linearGradient id="perfBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d0d1a;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#0f172a;stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="perfAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
    <linearGradient id="barPurple" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#7C3AED;stop-opacity:0.9"/>
      <stop offset="100%" style="stop-color:#7C3AED;stop-opacity:0.4"/>
    </linearGradient>
    <linearGradient id="barBlue" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#2563EB;stop-opacity:0.9"/>
      <stop offset="100%" style="stop-color:#2563EB;stop-opacity:0.4"/>
    </linearGradient>
    <linearGradient id="barCyan" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#06B6D4;stop-opacity:0.9"/>
      <stop offset="100%" style="stop-color:#06B6D4;stop-opacity:0.4"/>
    </linearGradient>
  </defs>
  <rect width="820" height="200" fill="url(#perfBg)" rx="14"/>
  <rect x="0" y="0" width="820" height="3" fill="url(#perfAccent)" rx="1"/>
  <text x="410" y="26" font-family="monospace" font-size="13" fill="#a78bfa" text-anchor="middle" font-weight="bold" letter-spacing="2">PERFORMANCE CHARACTERISTICS</text>

  <!-- Stat card 1: Image inference -->
  <rect x="40" y="46" width="160" height="130" rx="10" fill="#7C3AED" fill-opacity="0.1" stroke="#7C3AED" stroke-width="1.2"/>
  <text x="120" y="70" font-family="monospace" font-size="9" fill="#a78bfa" text-anchor="middle" font-weight="bold">IMAGE INFERENCE</text>
  <text x="120" y="108" font-family="monospace" font-size="28" fill="#c4b5fd" text-anchor="middle" font-weight="bold">~0.3s</text>
  <text x="120" y="126" font-family="monospace" font-size="9" fill="#6b7280" text-anchor="middle">CPU (single image)</text>
  <rect x="60" y="138" width="120" height="6" rx="3" fill="#1f2937"/>
  <rect x="60" y="138" width="90" height="6" rx="3" fill="url(#barPurple)"/>
  <text x="120" y="162" font-family="monospace" font-size="8" fill="#6b7280" text-anchor="middle">GPU: &lt;0.05s</text>

  <!-- Stat card 2: Video inference -->
  <rect x="220" y="46" width="160" height="130" rx="10" fill="#2563EB" fill-opacity="0.1" stroke="#2563EB" stroke-width="1.2"/>
  <text x="300" y="70" font-family="monospace" font-size="9" fill="#93c5fd" text-anchor="middle" font-weight="bold">VIDEO ANALYSIS</text>
  <text x="300" y="108" font-family="monospace" font-size="28" fill="#93c5fd" text-anchor="middle" font-weight="bold">~1.8s</text>
  <text x="300" y="126" font-family="monospace" font-size="9" fill="#6b7280" text-anchor="middle">CPU · 6 frames</text>
  <rect x="240" y="138" width="120" height="6" rx="3" fill="#1f2937"/>
  <rect x="240" y="138" width="70" height="6" rx="3" fill="url(#barBlue)"/>
  <text x="300" y="162" font-family="monospace" font-size="8" fill="#6b7280" text-anchor="middle">GPU: ~0.3s</text>

  <!-- Stat card 3: Throughput -->
  <rect x="400" y="46" width="160" height="130" rx="10" fill="#06B6D4" fill-opacity="0.1" stroke="#06B6D4" stroke-width="1.2"/>
  <text x="480" y="70" font-family="monospace" font-size="9" fill="#67e8f9" text-anchor="middle" font-weight="bold">THROUGHPUT</text>
  <text x="480" y="108" font-family="monospace" font-size="28" fill="#67e8f9" text-anchor="middle" font-weight="bold">~3/s</text>
  <text x="480" y="126" font-family="monospace" font-size="9" fill="#6b7280" text-anchor="middle">images · CPU</text>
  <rect x="420" y="138" width="120" height="6" rx="3" fill="#1f2937"/>
  <rect x="420" y="138" width="100" height="6" rx="3" fill="url(#barCyan)"/>
  <text x="480" y="162" font-family="monospace" font-size="8" fill="#6b7280" text-anchor="middle">GPU: ~20/s</text>

  <!-- Stat card 4: DB latency -->
  <rect x="580" y="46" width="200" height="130" rx="10" fill="#7C3AED" fill-opacity="0.1" stroke="#7C3AED" stroke-width="1.2"/>
  <text x="680" y="70" font-family="monospace" font-size="9" fill="#a78bfa" text-anchor="middle" font-weight="bold">DB OPERATIONS</text>
  <text x="680" y="108" font-family="monospace" font-size="28" fill="#c4b5fd" text-anchor="middle" font-weight="bold">&lt;1ms</text>
  <text x="680" y="126" font-family="monospace" font-size="9" fill="#6b7280" text-anchor="middle">SQLite read/write</text>
  <rect x="600" y="138" width="160" height="6" rx="3" fill="#1f2937"/>
  <rect x="600" y="138" width="155" height="6" rx="3" fill="url(#barPurple)"/>
  <text x="680" y="162" font-family="monospace" font-size="8" fill="#6b7280" text-anchor="middle">Dashboard refresh: 10s interval</text>
</svg>

</div>

> **Note:** Inference times are approximate and vary with hardware. The model (`Falconsai/nsfw_image_detection`) is downloaded once and cached by HuggingFace on first run.

---

## ♿ Accessibility

The real-time dashboard (`templates/index.html`) implements the following accessibility features:

- **ARIA roles and labels** on all status cards and interactive regions (`role="region"`, `aria-label`)
- **Keyboard navigation** — the Recent Actions feed is `tabindex="0"` accessible
- **Semantic loading states** — the loading spinner has `aria-label="Loading"`
- **High-contrast color choices** — status card gradients maintain ≥ 3:1 contrast ratio
- **Responsive layout** — Tailwind breakpoints ensure usability on mobile, tablet, and desktop

---

## 🔒 Privacy & Security Model

| Concern | Mitigation |
|---|---|
| **Bot token exposure** | Loaded exclusively from environment variables; `.env` is git-ignored |
| **Admin ID exposure** | Same as above — never hard-coded |
| **Flagged media retention** | Stored locally in configurable directories; excluded from version control |
| **Dashboard write access** | Dashboard is **read-only** — no write endpoints are exposed |
| **User data minimalism** | Only `user_id` (integer) is stored — no names, usernames, or message content |
| **False positive risk** | ML model may err; admin review of cached media is recommended before permanent action |
| **Telegram ToS compliance** | Bot operates within Telegram Bot API permissions; no scraping or data exfiltration |

---

## 🎯 Design Principles

1. **Zero-trust content** — every piece of media is treated as potentially harmful until proven safe.
2. **Evidence-first enforcement** — all flagged content is cached before deletion for auditability.
3. **Configurable thresholds** — no behaviour is hard-coded; operators control all enforcement parameters.
4. **Graceful degradation** — permission errors (e.g., chat owner ban) are caught and handled without crashing.
5. **Separation of concerns** — detection, enforcement, persistence, and analytics are cleanly separated.
6. **Privacy minimalism** — only the data strictly necessary for operation is collected and stored.
7. **GPU-agnostic** — the system functions on both CPU and CUDA hardware with automatic detection.

---

## 🗺️ Roadmap

| Phase | Feature | Status |
|---|---|---|
| ✅ v1.0 | Image NSFW detection | **Released** |
| ✅ v1.0 | Video / GIF frame analysis | **Released** |
| ✅ v1.0 | SQLite violation tracking | **Released** |
| ✅ v1.0 | Auto-ban + admin notifications | **Released** |
| ✅ v1.0 | Real-time Flask dashboard | **Released** |
| 🔄 v1.1 | Text spam detection (NLP) | Planned |
| 🔄 v1.1 | Escalating ban timers (1m, 5m, permanent) | Planned |
| 🔄 v1.2 | `/setflagthreshold` admin command | Planned |
| 🔄 v1.2 | PostgreSQL backend option | Planned |
| 🔜 v2.0 | Multi-group support with per-group config | Future |
| 🔜 v2.0 | Webhook mode for production deployments | Future |
| 🔜 v2.0 | Docker + Docker Compose packaging | Future |

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please read [CONTRIBUTING](wiki/Contributing.md) for full guidelines.

---

## ⚠️ Disclaimer

This bot relies on a machine-learning model and may produce false positives or false negatives. Always review flagged content before taking permanent manual action, and use the tool responsibly in compliance with [Telegram's Terms of Service](https://telegram.org/tos).

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

<div align="center">
<strong>A.R.T.E.M.I.S.S.</strong> — Keeping your Telegram groups clean and safe 🛡️
<br/><br/>
<sub>Built with ❤️ by <a href="https://github.com/Kaelith69">Kaelith69</a></sub>
</div>
