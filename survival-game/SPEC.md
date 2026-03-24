# Wasteland Survivors - Game Specification

## Concept
Post-apocalyptic survival management game where players manage a group of survivors, build their base, send expeditions for resources, and make tough moral decisions.

## Core Mechanics

### Day Cycle
- Each "day" represents a cycle of actions
- Resources consumed daily: Food, Water, Energy
- Random events occur each night

### Resources
- 🍖 Food - consumed by each survivor per day
- 💧 Water - consumed by each survivor per day
- 🔋 Energy - used for base operations and expeditions
- 🧱 Materials - for building/upgrading
- 💊 Meds - for healing

### Base Building
Rooms that can be built/upgraded:
- 🏠 Shelter - increases max survivors
- 🌱 Greenhouse - produces food
- 💧 Water Filter - produces water
- ⚡ Generator - produces energy
- 🔧 Workshop - enables crafting
- 🏪 Storage - increases resource caps

### Expedition System
Send 1-3 survivors to locations for resources:
- 🏭 Abandoned Factory - high materials, medium risk
- 🏥 Hospital - meds, high risk
- 🏪 Supermarket - food, low risk
- ⚡ Power Plant - energy, high risk
- 🏠 Residential - random loot, low risk
Each survivor has hidden traits affecting success.

**⚠️ NACHBESSERUNG NÖTIG:**
- Max 1-2 Expeditionen pro Survivor pro Tag (nicht unbegrenzt)
- Expeditionen brauchen Zeit

### Survivor System
Survivors have:
- 👤 Name
- 💪 Health (0-100)
- 🛠️ Skill (Scavenging, Combat, Medical, Technical)
- 😶 Trait (hidden - can be positive or negative)
- 🎒 Inventory

**Recruitment:** Survivors occasionally arrive at the gate (NICHT jederzeit frei rekrutierbar!)

### Random Events
- Stranger at gate requesting entry
- Raider attack
- Disease outbreak
- Found supplies
- Trader arrival

## UI Layout
- Left: Base view (grid of rooms)
- Top: Resource bar
- Right: Survivor list + Actions
- Bottom: Event log / Expedition results

## Tech Stack
- Single HTML file
- Vanilla JS
- CSS with retro aesthetic
- Emoji graphics

## First Prototype Features
1. Resource display
2. Day cycle with consumption
3. Simple base building (3 room types)
4. 2-3 starting survivors
5. One expedition type
6. Basic random events
7. Save to localStorage

---

## ✅ ERLEDIGT (2026-03-24)

Alle 4 User-Feedback-Punkte implementiert:
- ✅ Expedition-Limit: Max 2 pro Survivor/Tag
- ✅ Start-Survivors: 1-2 beim Spielstart  
- ✅ Zufälliges Recruiting: CHECK GATE (1x pro Tag)
- ✅ Echtzeit-Modus: 1 Sekunde = 1 Spielstunde