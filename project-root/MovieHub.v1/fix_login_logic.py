import re

with open("static/login.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace the alert and logic
new_script = """    <script>
      const loginForm = document.getElementById("login-form");
      const emailInput = document.getElementById("email-input");
      const passwordInput = document.getElementById("password-input");
      const errorMsg = document.getElementById("error-msg");

      loginForm.addEventListener("submit", (e) => {
        e.preventDefault(); // Prevent page reload
        
        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();

        if (email === "selvamthiru712@gmail.com" && password === "_Thiru@4690") {
          // Hide error if previously shown
          errorMsg.classList.add("hidden");
          
          // Set credentials in secure local storage
          localStorage.setItem("adminUser", email);
          localStorage.setItem("isAdmin", "true");

          // Directly redirect without intrusive alerts
          window.location.href = "admin.html";
        } else {
          // Failure: Show error banner, do NOT redirect
          errorMsg.classList.remove("hidden");
        }
      });
    </script>"""

old_script_regex = re.compile(r'<script>[\s\S]*?const loginForm = document\.getElementById\("login-form"\);[\s\S]*?</script>')
text = old_script_regex.sub(new_script, text)

with open("static/login.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed logic errors in login.html")
