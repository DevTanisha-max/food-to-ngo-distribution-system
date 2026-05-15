const BASE_URL = "http://127.0.0.1:5000";

// ---------------- HELPER FUNCTIONS ----------------
function getRestaurantId(user) {
    return user.restaurant_id;
}

function getNgoId(user) {
    return user.ngo_id;
}

// ---------------- SIGNUP (UPDATED FOR FILE UPLOAD) ----------------
async function signup() {
    const role = document.getElementById("role").value;

    const formData = new FormData();
    formData.append("name", document.getElementById("name").value);
    formData.append("email", document.getElementById("email").value);
    formData.append("password", document.getElementById("password").value);
    formData.append("role", role);

    if (role === "ngo") {
        formData.append("total_capacity_smu", document.getElementById("capacity").value);
    }

    if (role === "restaurant") {
        const file = document.getElementById("certificate").files[0];
        formData.append("certificate", file);
    }

    const res = await fetch(BASE_URL + "/signup", {
        method: "POST",
        body: formData
    });

    const result = await res.json();

    if (res.ok) {
        alert("Signup successful! You can login now.");
        window.location.href = "login.html";
    } else {
        alert(result.error);
    }
}

// ---------------- LOGIN ----------------
async function login() {
    const res = await fetch(BASE_URL + "/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        })
    });

    const data = await res.json();

    if (data.user) {
        sessionStorage.setItem("user", JSON.stringify(data.user));

        if (data.user.role === "restaurant") {
            window.location.href = "restaurant.html";
        } else {
            window.location.href = "ngo.html";
        }
    } else {
        alert(data.error);
    }
}

// ---------------- ADD FOOD (RESTAURANT) ----------------
async function addFood() {
    const user = JSON.parse(sessionStorage.getItem("user"));

    const res = await fetch(BASE_URL + "/add-food", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            restaurant_id: getRestaurantId(user),
            food_name: document.getElementById("food_name").value,
            food_type: document.getElementById("food_type").value,
            shelf_life_hours: parseInt(document.getElementById("shelf").value),
            dry_or_wet: document.getElementById("dry").value,
            calorific_value: parseInt(document.getElementById("cal").value),
            smu_equivalent: parseInt(document.getElementById("smu").value),
            quantity_available_smu: parseInt(document.getElementById("qty").value)
        })
    });

    const data = await res.json();

    if (res.ok) {
        alert("Food added successfully!");
    } else {
        alert(data.error);
    }
}

// ---------------- LOAD FOOD (NGO) ----------------
async function loadFood() {
    const res = await fetch(BASE_URL + "/get-food");
    const data = await res.json();

    const container = document.getElementById("food-list");
    container.innerHTML = "";

    if (data.length === 0) {
        container.innerHTML = "<p>No food available at the moment.</p>";
        return;
    }

    data.forEach(food => {
        container.innerHTML += `
            <div class="food-item-card">
                <span class="badge">${food.dry_or_wet === 'dry' ? 'Dry Food' : 'Wet Food'}</span>
                <h3>${food.food_name}</h3>
                <p><strong>Type:</strong> ${food.food_type.charAt(0).toUpperCase() + food.food_type.slice(1)}</p>
                <p><strong>Available SMU:</strong> ${food.quantity_available_smu}</p>
                <p><strong>Calories/SMU:</strong> ${food.calorific_value}</p>
                <button class="btn-success" onclick="placeOrder(${food.food_id})" style="margin-top: 1rem;">Request Food</button>
            </div>
        `;
    });
}

// ---------------- LOGOUT ----------------
function logout() {
    sessionStorage.removeItem("user");
    window.location.href = "login.html";
}

// ---------------- PLACE ORDER ----------------
async function placeOrder(food_id) {
    const user = JSON.parse(sessionStorage.getItem("user"));

    const qty = prompt("Enter SMU quantity:");

    if (!qty) return;

    try {
        const res = await fetch(BASE_URL + "/place-order", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                ngo_id: getNgoId(user),
                food_id: food_id,
                quantity_smu: parseInt(qty)
            })
        });

        const data = await res.json();

        if (res.ok) {
            alert("Order placed! OTP: " + data.otp);
            window.location.href = "otp.html";
        } else {
            alert(data.error);
        }
    } catch (error) {
        alert("Error placing order: " + error);
    }
}

// ---------------- VERIFY OTP ----------------
async function verifyOTP() {
    const order_id = document.getElementById("order_id").value;
    const otp = document.getElementById("otp").value;

    const res = await fetch(BASE_URL + "/verify-otp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            order_id: parseInt(order_id),
            otp: otp
        })
    });

    const data = await res.json();

    if (res.ok) {
        alert("Pickup verified successfully!");
    } else {
        alert(data.error);
    }
}