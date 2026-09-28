import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Config:
    # WooCommerce API Configuration
    WC_URL = os.getenv('WC_URL', 'http://demostore.supersqa.com')
    WC_CONSUMER_KEY = os.getenv('WC_CONSUMER_KEY', '')
    WC_CONSUMER_SECRET = os.getenv('WC_CONSUMER_SECRET', '')

    # Test Configuration
    BROWSER = os.getenv('BROWSER', 'chrome')
    # In CI (GitHub Actions sets CI=true) there is no display, so Chrome must
    # run headless unless explicitly overridden via the HEADLESS env var.
    _HEADLESS_DEFAULT = 'true' if os.getenv('CI') == 'true' else 'False'
    HEADLESS = os.getenv('HEADLESS', _HEADLESS_DEFAULT).lower() == 'true'
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
    
    # Test Data
    TEST_USERNAME = os.getenv('TEST_USERNAME', 'testuser')
    TEST_PASSWORD = os.getenv('TEST_PASSWORD', 'testpass')

    # API Timeouts
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))

    @staticmethod
    def validate():
        """Validate required environment variables are set"""
        required_vars = ['WC_CONSUMER_KEY', 'WC_CONSUMER_SECRET']
        missing_vars = [var for var in required_vars if not getattr(Config, var)]
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}") 