import re

html_path = "static/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update the newsletter form to give it an ID
news_form = '<form action="mailto:selvamthiru712@gmail.com" method="post" enctype="text/plain" class="flex w-full max-w-md flex-col gap-3 sm:flex-row">'
news_form_id = '<form id="newsletter-form" action="mailto:selvamthiru712@gmail.com" method="post" enctype="text/plain" class="flex w-full max-w-md flex-col gap-3 sm:flex-row">'

if news_form in content:
    content = content.replace(news_form, news_form_id)

    # Let's inject a quick script to store newsletter email in localStorage before submitting
    script_injection = """
  </script>
  <script>
    const newsletterForm = document.getElementById('newsletter-form');
    if (newsletterForm) {
      newsletterForm.addEventListener('submit', (e) => {
        const emailInput = newsletterForm.querySelector('input[type="email"]');
        if (emailInput && emailInput.value) {
          const subscribers = JSON.parse(localStorage.getItem('newsletterSubscribers') || '[]');
          subscribers.push(emailInput.value);
          localStorage.setItem('newsletterSubscribers', JSON.stringify(subscribers));
          alert('Subscribed! Email saved.');
        }
      });
    }
    """
    content = content.replace("  </script>\n</html>", script_injection + "\n  </script>\n</html>")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Newsletter JS added.")
else:
    print("Newsletter form not found.")
