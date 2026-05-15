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

Restaurant Login
↓
Menu Upload (One-Time)
↓
Daily Surplus Entry
↓
Food Stored in Database
↓
NGO Login
↓
SMU Capacity Validation
↓
Nearby Food Display
↓
Order Placement (Within Limit)
↓
OTP Generation
↓
Pickup & Verification
↓
Food Distribution



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

## 🚀Local Setup Guide

### Prerequisites

- **Python 3.8+** – [Download here](https://www.python.org/downloads/)
- **Git** (optional) – [Download here](https://git-scm.com/)
- **pip** (comes with Python)

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/DevTanisha-max/food-to-ngo-distribution-system.git
cd food-to-ngo-distribution-system

2. Create a Virtual Environment

Windows:
python -m venv venv
venv\Scripts\activate

macOS / Linux:
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Set Up Environment Variables
Create a .env file in the project root:

Windows:

echo DATABASE_URL=sqlite:///food_to_ngo.db > .env

macOS/Linux:

touch .env
# Then add this line: DATABASE_URL=sqlite:///food_to_ngo.db

5. Initialize the Database

python setup_db.py


6. Run the Application

python app.py

7. Access the Application
Open your browser and go to: http://localhost:5000

Troubleshooting Local Setup
Issue	Solution
ModuleNotFoundError: No module named 'flask'	Run pip install -r requirements.txt again
Database error: no such table	Run python setup_db.py to create tables
Port 5000 already in use	Use python app.py --port=5001



🌍 Project Impact
🍽️ Social Impact
Reduces Food Waste: Restaurants can donate surplus instead of discarding it.

Fights Hunger: NGOs get a steady, transparent supply of food for vulnerable communities.

Fair Distribution: The SMU model prevents hoarding and ensures resources reach those in need.

Builds Trust: Certificate verification and OTP pickup create a secure, accountable system.

🌱 Environmental Impact
Every meal rescued = less methane from rotting food in landfills.

Example: 100 restaurants donating 10 SMU daily rescues 365,000 meals/year, saving approximately 365,000 kg of CO₂ equivalent.

💰 Economic Impact
Stakeholder	Benefit
Restaurants	Tax incentives, reduced waste disposal costs, positive brand image
NGOs	Lower food procurement costs, predictable supply
Society	Reduced government spending on hunger relief programs
📊 Scalability Potential
Scale	Estimated Daily Impact
1 City	500 restaurants, 200 NGOs → 10,000 meals/day
1 State	5,000 restaurants, 2,000 NGOs → 100,000 meals/day
1 Country	50,000 restaurants, 20,000 NGOs → 1,000,000 meals/day
🎯 UN Sustainable Development Goals (SDGs)
SDG 2 (Zero Hunger) – Direct meal distribution to the needy

SDG 12 (Responsible Consumption) – Reduces food loss and waste

SDG 11 (Sustainable Cities) – Promotes smart, circular food systems



📁 Project Structure

food-to-ngo-distribution-system/
├── app.py                 # Main Flask application
├── db.py                  # Database connection (SQLite/PostgreSQL)
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment configuration
├── frontend/
│   ├── login.html        # Login page
│   ├── signup.html       # Registration page
│   ├── ngo.html          # NGO dashboard
│   ├── restaurant.html   # Restaurant dashboard
│   ├── otp.html          # OTP verification page
│   ├── script.js         # Frontend JavaScript
│   └── styles.css        # Global styling
└── uploads/              # Uploaded certificates (local)



👥 User Roles
🍕 Restaurant
Register with business certificate

Wait for admin approval (or auto-approve in local/dev)

Add daily surplus food items

View incoming orders

Verify OTP before handing over food

🏢 NGO
Register with SMU capacity limit

Browse available food from nearby restaurants

Request food within remaining capacity

Receive OTP for pickup

Collect food after verification

👑 Admin
Verify restaurant certificates

Monitor system for abuse

(Auto-approval is enabled for local testing)

🔒 Security Features
OTP Verification – Prevents unauthorized food collection

Certificate Upload – Restaurants must prove legitimacy

SMU Limits – Prevents single NGO from exhausting all resources

Session-Based Auth – Secure login state management

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a feature branch: git checkout -b feature/YourFeature

Commit your changes: git commit -m 'Add some feature'

Push to the branch: git push origin feature/YourFeature

Open a Pull Request

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

👨‍💻 Author
Tanisha Sharma (DevTanisha-max)

GitHub: @DevTanisha-max

Project Repository: github.com/DevTanisha-max/food-to-ngo-distribution-system

Live Demo: food-to-ngo-distribution-system.onrender.com

🙏 Acknowledgments
Flask – Lightweight backend framework

Supabase – Free PostgreSQL hosting

Render – Free cloud deployment platform

Contributors – All those who helped shape this project

⭐ Show Your Support
If this project helps you or inspires you, please consider giving it a star on GitHub ⭐. It helps others discover the project and motivates continued development.

Built with ❤️ to reduce waste and feed communities. | MIT License







