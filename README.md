# 🍽️ Smart Surplus Food Distribution System

A web-based platform designed to reduce food wastage by enabling **fair, secure, and efficient distribution** of surplus food from restaurants to verified NGOs.

[![Live Demo](https://img.shields.io/badge/Live_Demo-View_App-00C7B7?style=for-the-badge&logo=render)](https://food-to-ngo-distribution-system.onrender.com)
[![GitHub Repository](https://img.shields.io/badge/GitHub-View_Code-181717?style=for-the-badge&logo=github)](https://github.com/DevTanisha-max/food-to-ngo-distribution-system)

---

## 🌐 Live Demo

🔗 **[Click here to access the live application](https://food-to-ngo-distribution-system.onrender.com)**

*Note: The free tier may take 30-60 seconds to wake up on first visit.*

---

## 📌 Overview

Food wastage is a major issue in urban areas, while many NGOs struggle to meet daily food requirements. This project provides a **centralized system** that connects restaurants with NGOs and ensures **equitable distribution based on actual need**, not speed or size.

The system introduces a **Standard Meal Unit (SMU) model** to enforce fairness and prevent resource hoarding.

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| ✅ **Verified NGO & Restaurant Onboarding** | Secure signup with certificate upload |
| ⚖️ **Capacity-Based Distribution (SMU Model)** | Fair allocation based on need |
| 📍 **Geo-location Based Matching** | Find nearby food donations |
| 🔐 **OTP-Based Secure Pickup** | Safe and verified food collection |
| 🍴 **Menu-Based Surplus Entry** | No repetitive input needed |
| ⏱️ **Automatic Food Expiry Handling** | Prevents stale food distribution |
| 🚫 **Order Limitation** | Prevents hoarding of resources |

---

## 🧠 Core Concept: Standard Meal Unit (SMU)

The system measures food in Standard Meal Units (SMU) to ensure fair allocation.

| Category | SMU Value |
|----------|-----------|
| 👨 Adult | 1.0 SMU |
| 👧 Child | 0.7 SMU |
| 👴 Elderly | 0.8 SMU |

> **1 SMU ≈ 600 kcal**

- NGOs are assigned a **fixed SMU capacity**
- Orders exceeding capacity are automatically blocked

---

## ⚙️ System Workflow

┌──────────────┐
│ Restaurant │
│ Login │
└──────┬───────┘
↓
┌──────────────┐
│ Menu Upload │
│ (One-Time) │
└──────┬───────┘
↓
┌──────────────┐
│ Daily Surplus│
│ Entry │
└──────┬───────┘
↓
┌──────────────┐
│ Food Stored │
│ in Database │
└──────┬───────┘
↓
┌──────────────┐
│ NGO Login │
└──────┬───────┘
↓
┌──────────────┐
│ SMU Capacity │
│ Validation │
└──────┬───────┘
↓
┌──────────────┐
│ Nearby Food │
│ Display │
└──────┬───────┘
↓
┌──────────────┐
│Order Placement│
│(Within Limit)│
└──────┬───────┘
↓
┌──────────────┐
│ OTP Generated│
└──────┬───────┘
↓
┌──────────────┐
│Pickup & Verify│
└──────┬───────┘
↓
┌──────────────┐
│ Food │
│ Distribution │
└──────────────┘



---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Python Flask |
| **Frontend** | HTML, CSS, JavaScript |
| **Database** | PostgreSQL (Supabase) / SQLite |
| **Deployment** | Render.com |
| **Authentication** | Session-based |
| **Version Control** | Git & GitHub |

---

## 🚀 Detailed Local Setup Guide

Follow these steps to run the project on your own computer for development or testing.

### Prerequisites

- **Python 3.8+** – [Download here](https://www.python.org/downloads/)
- **Git** (optional, for cloning) – [Download here](https://git-scm.com/)
- **pip** (comes with Python)

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/DevTanisha-max/food-to-ngo-distribution-system.git
cd food-to-ngo-distribution-system



