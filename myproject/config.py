import os

# Gemini AI
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Email
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True").lower() == "true"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
EMAIL_FROM_ADDRESS = os.getenv("EMAIL_FROM_ADDRESS", "")

# MapTiler
MAPTILER_API_KEY = os.getenv("MAPTILER_API_KEY", "")
MAPTILER_BASE_URL = os.getenv(
    "MAPTILER_BASE_URL",
    "https://api.maptiler.com"
)