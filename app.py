from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from db import get_connection
from datetime import datetime, timedelta
import random
import os

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return app.send_static_file('login.html')

@app.route("/<path:path>")
def serve_static(path):
    if os.path.exists(os.path.join(app.static_folder, path)):
        return app.send_static_file(path)
    return app.send_static_file('login.html')


# ------------------ SIGNUP ------------------
@app.route("/signup", methods=["POST"])
def signup():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")

        conn = get_connection()
        cursor = conn.cursor()

        # Insert user with auto-approve
        cursor.execute(
            "INSERT INTO users (name, email, password, role, is_approved) VALUES (?, ?, ?, ?, ?)",
            (name, email, password, role, 1)
        )

        user_id = cursor.lastrowid

        # ---------------- RESTAURANT ----------------
        if role == "restaurant":
            file = request.files.get("certificate")

            filepath = None
            if file:
                os.makedirs("uploads", exist_ok=True)
                filepath = os.path.join("uploads", file.filename)
                file.save(filepath)

            cursor.execute("""
                INSERT INTO restaurants 
                (user_id, restaurant_name, certificate, is_verified)
                VALUES (?, ?, ?, ?)
            """, (user_id, name, filepath, 1))

        # ---------------- NGO ----------------
        elif role == "ngo":
            total_capacity = request.form.get("total_capacity_smu")

            cursor.execute("""
                INSERT INTO ngos 
                (user_id, ngo_name, total_capacity_smu, remaining_capacity_smu)
                VALUES (?, ?, ?, ?)
            """, (user_id, name, total_capacity, total_capacity))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Signup successful! You can login now."})

    except Exception as e:
        return jsonify({"error": str(e)})


# ------------------ LOGIN ------------------
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "Invalid credentials"})

        # Convert to dict using indexes
        user_dict = {
            'id': user[0],
            'name': user[1],
            'email': user[2],
            'password': user[3],
            'role': user[4],
            'certificate': user[5],
            'is_approved': user[6],
            'created_at': user[7]
        }
        
        # Check verification for restaurant
        if user_dict["role"] == "restaurant":
            cursor.execute(
                "SELECT restaurant_id, is_verified FROM restaurants WHERE user_id=?",
                (user_dict["id"],)
            )
            res = cursor.fetchone()
            
            if not res or res[1] != 1:
                return jsonify({"error": "Wait for admin verification"}), 403
            
            user_dict["restaurant_id"] = res[0]

        elif user_dict["role"] == "ngo":
            cursor.execute(
                "SELECT ngo_id FROM ngos WHERE user_id=?",
                (user_dict["id"],)
            )
            res = cursor.fetchone()
            if res:
                user_dict["ngo_id"] = res[0]

        cursor.close()
        conn.close()

        return jsonify({
            "message": "Login successful",
            "user": user_dict
        })

    except Exception as e:
        return jsonify({"error": str(e)})


# ------------------ ADD FOOD ------------------
@app.route("/add-food", methods=["POST"])
def add_food():
    try:
        data = request.get_json()

        shelf_life = data.get("shelf_life_hours")
        expiry_time = datetime.now() + timedelta(hours=shelf_life)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO food_items 
            (restaurant_id, food_name, food_type, shelf_life_hours, dry_or_wet,
             calorific_value, smu_equivalent, quantity_available_smu, expiry_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data.get("restaurant_id"),
            data.get("food_name"),
            data.get("food_type"),
            shelf_life,
            data.get("dry_or_wet"),
            data.get("calorific_value"),
            data.get("smu_equivalent"),
            data.get("quantity_available_smu"),
            expiry_time
        ))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Food added successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})


# ------------------ GET FOOD ------------------
@app.route("/get-food", methods=["GET"])
def get_food():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM food_items WHERE expiry_time > datetime('now')")
        rows = cursor.fetchall()
        
        food_list = []
        for row in rows:
            food_list.append({
                'food_id': row[0],
                'restaurant_id': row[1],
                'food_name': row[2],
                'food_type': row[3],
                'shelf_life_hours': row[4],
                'dry_or_wet': row[5],
                'calorific_value': row[6],
                'smu_equivalent': row[7],
                'quantity_available_smu': row[8],
                'expiry_time': row[9]
            })

        cursor.close()
        conn.close()

        return jsonify(food_list)

    except Exception as e:
        return jsonify({"error": str(e)})


# ------------------ PLACE ORDER ------------------
@app.route("/place-order", methods=["POST"])
def place_order():
    try:
        data = request.get_json()

        ngo_id = data.get("ngo_id")
        food_id = data.get("food_id")
        requested_smu = data.get("quantity_smu")

        print(f"Placing order: NGO={ngo_id}, Food={food_id}, Quantity={requested_smu}")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT remaining_capacity_smu FROM ngos WHERE ngo_id=?", (ngo_id,))
        ngo = cursor.fetchone()

        if not ngo or ngo[0] < requested_smu:
            return jsonify({"error": "SMU limit exceeded"}), 400

        otp = str(random.randint(1000, 9999))
        otp_expiry = datetime.now() + timedelta(minutes=10)

        print(f"Generated OTP: {otp}")

        cursor.execute("""
            INSERT INTO orders (ngo_id, food_id, quantity_smu, otp, otp_expiry)
            VALUES (?, ?, ?, ?, ?)
        """, (ngo_id, food_id, requested_smu, otp, otp_expiry))

        cursor.execute("""
            UPDATE ngos 
            SET remaining_capacity_smu = remaining_capacity_smu - ? 
            WHERE ngo_id=?
        """, (requested_smu, ngo_id))

        cursor.execute("""
            UPDATE food_items 
            SET quantity_available_smu = quantity_available_smu - ? 
            WHERE food_id=?
        """, (requested_smu, food_id))

        conn.commit()

        cursor.close()
        conn.close()

        # Return OTP in response
        return jsonify({
            "message": "Order placed",
            "otp": otp
        }), 200

    except Exception as e:
        print(f"Error in place-order: {str(e)}")
        return jsonify({"error": str(e)}), 500

# ------------------ VERIFY OTP ------------------
@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    try:
        data = request.get_json()

        order_id = data.get("order_id")
        entered_otp = data.get("otp")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM orders WHERE order_id=?", (order_id,))
        order = cursor.fetchone()

        if not order:
            return jsonify({"error": "Order not found"})

        if order[4] != entered_otp:  # otp is at index 4
            return jsonify({"error": "Invalid OTP"})

        if datetime.now() > datetime.strptime(order[5], '%Y-%m-%d %H:%M:%S.%f'):
            return jsonify({"error": "OTP expired"})

        cursor.execute(
            "UPDATE orders SET order_status='collected' WHERE order_id=?",
            (order_id,)
        )

        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "Pickup verified successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)