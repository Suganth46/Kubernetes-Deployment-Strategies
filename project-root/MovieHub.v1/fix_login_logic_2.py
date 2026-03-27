import re

with open("static/login.html", "r", encoding="utf-8") as f:
    text = f.read()

new_script = """    <script>
      const loginForm = document.getElementById("login-form");
      const emailInput = document.getElementById("email-input");
      const passwordInput = document.getElementById("password-input");
      const errorMsg = document.getElementById("error-msg");

      function attemptLogin(e) {
        if (e) e.preventDefault();
        
        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();

        if (!email || !password) {
          errorMsg.textContent = "Please enter both email and password.";
          errorMsg.classList.remove("hidden");
          return false;
        }

        if (email === "selvamthiru712@gmail.com" && password === "_Thiru@4690") {
          errorMsg.classList.add("hidden");
          localStorage.setItem("adminUser", email);
          localStorage.setItem("isAdmin", "true");
          window.location.replace("admin.html");
          return true;
        } else {
          errorMsg.textContent = "Invalid credentials. Please try again.";
          errorMsg.classList.remove("hidden");
          return false;
        }
      }

      loginForm.addEventListener("submit", attemptLogin);
      document.getElementById("login-button").addEventListener("click", attemptLogin);
    </script>"""

old_script_regex = re.compile(r'<script>[\s\S]*?</script>')
text = old_script_regex.sub(new_script, text)

# Ensure the form can't submit via HTML natively to avoid refresh
text = text.replace('<form id="login-form"', '<form id="login-form" onsubmit="event.preventDefault(); return false;"')

with open("static/login.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Logic fortified.")
