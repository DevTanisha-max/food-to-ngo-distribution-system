const BASE_URL = "";

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

async function signup(){
  const res = await fetch(BASE_URL + "/signup", {
    method:"POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({
      name: name.value,
      email: email.value,
      password: password.value,
      role: role.value
    })
  });

  const data = await res.json();
  alert(data.message || data.error);
}

function logout(){
  sessionStorage.clear();
  window.location.href = "login.html";
}

async function loadFood(){
  const res = await fetch(BASE_URL + "/get-food");
  const data = await res.json();

  const container = document.getElementById("food-list");
  container.innerHTML = "";

  data.forEach(f => {
    container.innerHTML += `
      <div class="food-item-card">
        <h3>${f.food_name}</h3>
        <p>Qty: ${f.quantity_available_smu}</p>
        <button onclick="placeOrder(${f.food_id})">Request</button>
      </div>
    `;
  });
}

async function placeOrder(id){
  const qty = prompt("Quantity?");

  const user = JSON.parse(sessionStorage.getItem("user"));

  const res = await fetch(BASE_URL + "/place-order", {
    method:"POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({
      ngo_id: user.ngo_id,
      food_id: id,
      quantity_smu: parseInt(qty)
    })
  });

  const data = await res.json();
  alert(data.otp ? "OTP: " + data.otp : data.error);
}

async function verifyOTP(){
  const res = await fetch(BASE_URL + "/verify-otp", {
    method:"POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({
      order_id: parseInt(order_id.value),
      otp: otp.value
    })
  });

  const data = await res.json();
  alert(data.message || data.error);
}