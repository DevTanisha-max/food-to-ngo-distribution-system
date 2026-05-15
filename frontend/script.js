// ---------------- LOGIN ----------------
async function login() {
    const res = await fetch("/login", {
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
            window.location.href = "/restaurant.html";
        } else {
            window.location.href = "/ngo.html";
        }
    } else {
        alert(data.error);
    }
}

// ---------------- SIGNUP ----------------
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

    const res = await fetch("/signup", { method: "POST", body: formData });
    const result = await res.json();

    if (res.ok) {
        alert("Signup successful! You can login now.");
        window.location.href = "/login.html";
    } else {
        alert(result.error);
    }
}

// ---------------- LOGOUT ----------------
function logout() {
    sessionStorage.removeItem("user");
    window.location.href = "/login.html";
}

// ---------------- ADD FOOD ----------------
async function addFood() {
    const user = JSON.parse(sessionStorage.getItem("user"));
    const res = await fetch("/add-food", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            restaurant_id: user.restaurant_id,
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
    alert(res.ok ? "Food added successfully!" : data.error);
}

// ---------------- LOAD FOOD ----------------
async function loadFood() {
    const res = await fetch("/get-food");
    const data = await res.json();
    const container = document.getElementById("food-list");
    if (!container) return;
    container.innerHTML = "";
    if (data.length === 0) {
        container.innerHTML = "<p>No food available.</p>";
        return;
    }
    data.forEach(food => {
        container.innerHTML += `
            <div class="food-item-card">
                <h3>${food.food_name}</h3>
                <p>Available SMU: ${food.quantity_available_smu}</p>
                <button onclick="placeOrder(${food.food_id})">Request Food</button>
            </div>
        `;
    });
}

// ---------------- PLACE ORDER ----------------
async function placeOrder(food_id) {
    const user = JSON.parse(sessionStorage.getItem("user"));
    const qty = prompt("Enter SMU quantity:");
    if (!qty) return;
    const res = await fetch("/place-order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            ngo_id: user.ngo_id,
            food_id: food_id,
            quantity_smu: parseInt(qty)
        })
    });
    const data = await res.json();
    if (res.ok) {
        alert("Order placed! OTP: " + data.otp);
        window.location.href = "/otp.html";
    } else {
        alert(data.error);
    }
}

// ---------------- VERIFY OTP ----------------
async function verifyOTP() {
    const res = await fetch("/verify-otp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            order_id: parseInt(document.getElementById("order_id").value),
            otp: document.getElementById("otp").value
        })
    });
    const data = await res.json();
    alert(res.ok ? "Pickup verified successfully!" : data.error);
}

function getRestaurantId(user) { return user.restaurant_id; }
function getNgoId(user) { return user.ngo_id; }