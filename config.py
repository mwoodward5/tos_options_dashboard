"""
Configuration file for TOS Options Dashboard with Automated Trading
Automated Trading, Benzinga API, and Discord Alert Integration
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# API KEYS & CREDENTIALS
# ============================================================================

# ThinkOrSwim / TD Ameritrade API
TOS_API_KEY = os.getenv('TOS_API_KEY', 'your_tos_api_key_here')
TOS_ACCOUNT_ID = os.getenv('TOS_ACCOUNT_ID', 'your_account_id_here')

# Benzinga API (Market Intelligence)
BENZINGA_API_KEY = os.getenv('BENZINGA_API_KEY', 'your_benzinga_api_key_here')
BENZINGA_API_URL = 'https://api.benzinga.com/api/v2'

# Discord Webhook (For Alerts)
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', 'your_discord_webhook_url_here')

# ============================================================================
# AUTOMATED TRADING CONFIGURATION
# ============================================================================

# Paper Trading (Set to False for live trading)
PAPER_TRADING = os.getenv('PAPER_TRADING', 'True').lower() == 'true'

# Maximum number of concurrent open positions
MAX_OPEN_POSITIONS = 5

# Maximum position size (in USD)
MAX_POSITION_SIZE = 10000  # $10,000 per trade

# Overall portfolio risk limit (as % of account)
MAX_PORTFOLIO_RISK_PERCENT = 5  # Risk max 5% of account per day

# Account balance (used for position sizing)
ACCOUNT_BALANCE = os.getenv('ACCOUNT_BALANCE', 100000)  # Default $100k
try:
    ACCOUNT_BALANCE = float(ACCOUNT_BALANCE)
except ValueError:
    ACCOUNT_BALANCE = 100000

# ============================================================================
# POSITION ENTRY PARAMETERS
# ============================================================================

ENTRY_CONFIG = {
    'options': {
        'min_roi_percent': 5.0,  # Minimum ROI to trigger trade
        'max_roi_percent': 50.0,  # Don't buy if ROI too high (likely risky)
        'min_delta': 0.15,  # For calls: min delta
        'max_delta': 0.85,  # For calls: max delta
        'min_volume': 100,  # Minimum options contract volume
        'min_open_interest': 50,  # Minimum open interest
        'days_to_expiration_min': 7,  # Don't trade within 7 days of expiry
        'days_to_expiration_max': 60,  # Don't trade > 60 days out
        'contract_types': ['CALL', 'PUT'],  # Which types to trade
    },
    'stocks': {
        'min_price': 5.0,  # Don't trade penny stocks
        'max_price': 1000.0,  # Max price filter
        'min_volume': 1000000,  # Minimum daily volume
        'enable': True,  # Enable stock trading
    }
}

# ============================================================================
# POSITION EXIT PARAMETERS (Risk Management)
# ============================================================================

EXIT_CONFIG = {
    'take_profit_percent': 50,  # Close position if +50% profit
    'stop_loss_percent': 20,  # Close position if -20% loss
    'max_hold_time_minutes': 480,  # Close after 8 hours
    'trailing_stop_percent': 15,  # Trailing stop at 15%
    'use_market_orders': False,  # Use limit orders for better execution
    'limit_order_offset_percent': 0.5,  # Offset limit orders by 0.5%
}

# ============================================================================
# SIGNAL SOURCES & FILTERING
# ============================================================================

SIGNAL_SOURCES = {
    'benzinga_news': True,  # Trade on Benzinga news
    'benzinga_options_flow': True,  # Trade on unusual options activity
    'custom_scanner': True,  # Trade on custom scanner signals
    'technical_indicators': True,  # Trade on technical setups
}

BENZINGA_CONFIG = {
    'news_keywords': [
        'earnings',
        'merger',
        'acquisition',
        'FDA',
        'approval',
        'breakthrough',
        'analyst',
        'upgrade',
        'downgrade',
        'restructuring'
    ],
    'min_importance': 2,  # 1-5, where 5 is most important
    'exclude_keywords': ['penny', 'delisted', 'bankruptcy'],
}

OPTIONS_FLOW_CONFIG = {
    'unusual_volume_multiplier': 3,  # 3x average = unusual
    'min_notional_value': 100000,  # $100k minimum
    'monitor_call_ratios': True,
    'monitor_put_ratios': True,
    'track_big_block_trades': True,
}

# ============================================================================
# ALERT CONFIGURATION
# ============================================================================

ALERT_CONFIG = {
    'enabled': True,
    'send_to_discord': True,
    'send_to_email': False,  # Set up email alerts separately
    'log_trades': True,  # Log all trades to file
    'include_charts': True,  # Include price charts in alerts
}

# Alert notification thresholds
ALERT_THRESHOLDS = {
    'new_entry': True,  # Alert on new position entry
    'take_profit_hit': True,  # Alert when TP reached
    'stop_loss_hit': True,  # Alert when SL hit
    'unusual_activity': True,  # Alert on market anomalies
    'news_events': True,  # Alert on breaking news
}

# Discord message formatting
DISCORD_FORMAT = {
    'include_technicals': True,
    'include_sentiment': True,
    'include_risk_metrics': True,
    'use_embeds': True,  # Use Discord embeds for formatting
    'mention_role': '@traders',  # Role to mention (set to empty string to disable)
}

# ============================================================================
# WATCHLIST & SYMBOLS
# ============================================================================

# Add your watchlist here or load from watchlist.txt
WATCHLIST = [
    'AAPL', 'MSFT', 'TSLA', 'NVDA', 'AMZN',
    'GOOGL', 'META', 'AMD', 'INTC', 'NFLX',
    'PYPL', 'SQ', 'COIN', 'RIOT', 'MARA'
]

# Load from watchlist.txt if it exists
WATCHLIST_FILE = 'watchlist.txt'
if os.path.exists(WATCHLIST_FILE):
    try:
        with open(WATCHLIST_FILE, 'r') as f:
            WATCHLIST = [line.strip().upper() for line in f if line.strip()]
    except Exception as e:
        print(f"Error loading watchlist from {WATCHLIST_FILE}: {e}")

# ============================================================================
# LOGGING & DATA STORAGE
# ============================================================================

LOGGING_CONFIG = {
    'log_level': 'INFO',  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    'log_file': 'logs/trading.log',
    'log_trades_file': 'logs/trade_log.csv',
    'log_alerts_file': 'logs/alert_log.csv',
    'max_log_size_mb': 100,
    'backup_logs': True,
}

# ============================================================================
# DASHBOARD SETTINGS
# ============================================================================

DASHBOARD_CONFIG = {
    'host': '127.0.0.1',
    'port': 8050,
    'debug': False,
    'show_live_trades': True,
    'show_alerts_history': True,
    'refresh_interval_seconds': 5,
    'theme': 'dark',  # 'light' or 'dark'
}

# ============================================================================
# SCHEDULE & TIMING
# ============================================================================

SCHEDULE_CONFIG = {
    'market_open_time': '09:30',  # EST
    'market_close_time': '16:00',  # EST
    'pre_market_enable': False,  # Trade in pre-market (4:00-9:30 AM EST)
    'after_hours_enable': False,  # Trade in after-hours (4:00-8:00 PM EST)
    'check_signals_interval_seconds': 30,  # Check for signals every 30 seconds
    'refresh_data_interval_seconds': 60,  # Refresh market data every 60 seconds
}

# ============================================================================
# EXECUTION & ORDER SETTINGS
# ============================================================================

EXECUTION_CONFIG = {
    'order_type': 'LIMIT',  # MARKET or LIMIT
    'time_in_force': 'DAY',  # DAY or GTC (Good Till Cancel)
    'slippage_tolerance_percent': 1.0,  # Max acceptable slippage
    'order_timeout_seconds': 60,  # Cancel order if not filled in 60 sec
    'enable_iceberg_orders': False,  # Use iceberg orders for large positions
    'iceberg_order_size_percent': 25,  # Show 25% of order at a time
}

# ============================================================================
# TESTING & BACKTESTING
# ============================================================================

BACKTEST_CONFIG = {
    'enabled': False,
    'start_date': '2024-01-01',
    'end_date': '2024-12-31',
    'initial_capital': 100000,
    'commission_percent': 0.001,  # 0.1% per trade
}

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def validate_config():
    """Validate that all required configuration values are set"""
    required_keys = {
        'TOS_API_KEY': TOS_API_KEY,
        'TOS_ACCOUNT_ID': TOS_ACCOUNT_ID,
        'BENZINGA_API_KEY': BENZINGA_API_KEY,
        'DISCORD_WEBHOOK_URL': DISCORD_WEBHOOK_URL,
    }
    
    missing = []
    for key, value in required_keys.items():
        if value in ['your_' + key.lower() + '_here', '', None]:
            missing.append(key)
    
    if missing:
        print(f"WARNING: Missing configuration keys: {', '.join(missing)}")
        print("Please set these values in your .env file or environment variables.")
        return False
    return True

def get_position_size(signal_strength=1.0):
    """Calculate position size based on account balance and risk"""
    risk_amount = ACCOUNT_BALANCE * (MAX_PORTFOLIO_RISK_PERCENT / 100)
    base_size = min(risk_amount, MAX_POSITION_SIZE)
    return base_size * signal_strength

if __name__ == '__main__':
    # Test configuration
    print("TOS Options Dashboard - Configuration Loaded")
    print(f"Paper Trading: {PAPER_TRADING}")
    print(f"Account Balance: ${ACCOUNT_BALANCE:,.2f}")
    print(f"Max Position Size: ${MAX_POSITION_SIZE:,.2f}")
    print(f"Watchlist: {WATCHLIST}")
    print(f"API Keys Configured: {validate_config()}")
