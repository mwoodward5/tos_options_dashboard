# ThinkOrSwim (TOS) Options Dashboard
## Project Description:
An interactive dashboard to filter and analyze stock options contracts (Built using data from ThinkOrSwim's Option Chain API and Plotly Dash components). It is useful for quickly scanning option chains to look for individual profitable options contracts to trade on. 
Filter options include:
* Return of Investment (ROI) Range: Percentage of premium received (by selling an contract) over the underlying amount (strike price * 100)
* Delta Range: Represents current probability that the option contract will expire [in-the-money](https://www.investopedia.com/terms/i/inthemoney.asp) (i.e. Option is exercised)
* Option Contract Type: Call/Put/All (both call and put options)
* Days to expiration: No. of days till options contract is set to expire
* Confidence Level: Represents the level of confidence in which the stock price is likely to be within the probability cone. A higher confidence level would result in a wider probability cone. 
* Historical Volatility Period: Changes the width of the probability cone calculation based on past period historical volatility (Past month, past 3 months, past year). For example, historical volatility of 40% would result in a wider probability curve than that based on a historical volatility of 25%. 
## Pre-requisites:
1. Set-up a TDAmeritrade Developer account to receive an API key. This key is necessary to authenticate each API call to extract the necessary data (e.g. stock quote date, option chain data) to required to perform financial analysis.
   
* [TOS Developers Home Page](https://developer.tdameritrade.com/)
   
* [Reddit: Guide to TOS Developer App set-up](https://www.reddit.com/r/algotrading/comments/914q22/successful_access_to_td_ameritrade_api/)
   
* If you are using Docker, proceed to step 1a), else go to step 1b). 
     a) Enter the API key into the Dockerfile.
     ```dockerfile
     ARG api_key = ENTER_API_KEY_HERE
     ```
     b) Set the API key as an environment variable (it should be named TOS_API_KEY). 
     
* [Environment Variables in Windows](https://www.youtube.com/watch?v=IolxqkL7cD8&t=136s)
     
* [Environment Variables in Mac/Linux](https://www.youtube.com/watch?v=5iWhQWVXosU)
2. Activate virtual environment in the directory of choice and install the necessary libraries outlined in requirements.txt . 
   ```python
   pip install -r requirements.txt
   ```
3. [Docker Option] To build and run the docker container, run the following lines in the terminal/command prompt. After running docker run, proceed with step 2 of the Usage section.
   	
* [Docker Troubleshooting](https://www.thegeekdiary.com/docker-troubleshooting-conflict-unable-to-delete-image-is-being-used-by-running-container/)
   ```terminal
   docker build -t tos_options_dashboard .
   docker run -p 8050:8050 tos_options_dashboard
   ```
   
   
* Note: You can override the default value of the TOS API Key set in Dockerfile by running the following command during build
   
     ```dockerfile
     docker build --build-arg api_key=<new_api_key> -t tos_options_dashboard .
     ```
## Usage:
1. Run the python file dashboard.py
   ```python
   python dashboard.py
   ```
2. The Dashboard would be running on local host (Port: 8050) by default. Open the web browser and enter the corresponding localhost address (http://127.0.0.1:8050/) to view the Dashboard.
3. To start using the Dashboard, activate Ticker mode before entering the stock ticker of interest (e.g. AAPL for Apple Inc. stock).
   Alternatively, you can type 'Apple' without activating Ticker mode to search for a particular option underlying.
   There are several options property filter options to choose from:
   
* Return on Investment (ROI) Range: (Default: More than 1%)
   
* Delta Range: (Default: Ignore Delta value)

---

## 🚀 NEW: Enhanced Features & Integrations

### Benzinga API Integration
This fork includes enhanced market intelligence through Benzinga API integration:

#### Setup Requirements:
1. **Get Benzinga API Key**
   - Sign up at [Benzinga Pro API](https://www.benzinga.com/apis/)
   - Choose a plan that includes news and options data access

2. **Configure Environment Variables**
   Add to your environment (or `.env` file):
   ```bash
   BENZINGA_API_KEY=your_benzinga_api_key_here
   TOS_API_KEY=your_tos_api_key_here
   DISCORD_WEBHOOK_URL=your_discord_webhook_url_here
   ```

#### Features:
- **Real-time Market News**: Fetch breaking news and market-moving events for your watchlist
- **Options Flow Data**: Track unusual options activity and large volume trades
- **Earnings Calendar**: Get notified about upcoming earnings for tracked tickers
- **Analyst Ratings**: View analyst upgrades/downgrades and price targets

### Discord Alert System
Receive real-time notifications for:
- High ROI options contracts matching your criteria
- Unusual options activity detected
- Breaking news for monitored tickers
- Price alerts and technical triggers

#### Discord Setup:
1. **Create Discord Webhook**
   - Go to your Discord server settings
   - Navigate to Integrations → Webhooks → New Webhook
   - Copy the webhook URL and add to environment variables

2. **Configure Alert Settings** (in `config.py` - to be created):
   ```python
   ALERT_SETTINGS = {
       'min_roi': 5.0,  # Minimum ROI % to trigger alert
       'min_volume': 1000,  # Minimum options volume
       'unusual_activity_multiplier': 3,  # 3x average volume
       'news_keywords': ['earnings', 'merger', 'FDA', 'breakthrough'],
   }
   ```

### File Structure (Enhanced)
```
tos_options_dashboard/
├── dashboard.py           # Main dashboard application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── README.md             # This file
├── config.py             # NEW: Configuration settings
├── benzinga_news.py      # NEW: Benzinga news fetcher
├── benzinga_options.py   # NEW: Benzinga options data
├── discord_alerts.py     # NEW: Discord notification system
├── alert_logic.py        # NEW: Alert triggering logic
└── utils/
    ├── data_fetcher.py   # NEW: Unified data fetching
    └── filters.py        # NEW: Enhanced filtering logic
```

### Installation (Updated)
1. **Clone this forked repository**
   ```bash
   git clone https://github.com/mwoodward5/tos_options_dashboard.git
   cd tos_options_dashboard
   ```

2. **Install dependencies** (updated requirements.txt includes new packages)
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   Create a `.env` file in the root directory:
   ```bash
   TOS_API_KEY=your_tos_key
   BENZINGA_API_KEY=your_benzinga_key
   DISCORD_WEBHOOK_URL=your_discord_webhook
   ```

4. **Run the enhanced dashboard**
   ```bash
   python dashboard.py --enable-alerts --enable-news
   ```

### Customization Guide

#### 1. Alert Triggers
Edit `alert_logic.py` to customize when alerts fire:
```python
def should_alert(option_data):
    # Custom logic here
    if option_data['roi'] > 10 and option_data['delta'] < 0.3:
        return True
    return False
```

#### 2. Discord Message Format
Customize alert appearance in `discord_alerts.py`:
```python
def format_alert(data):
    return {
        "embeds": [{
            "title": f"🎯 High ROI Alert: {data['symbol']}",
            "color": 0x00ff00,
            "fields": [
                {"name": "ROI", "value": f"{data['roi']}%"},
                {"name": "Strike", "value": f"${data['strike']}"},
            ]
        }]
    }
```

#### 3. Watchlist Configuration
Create `watchlist.txt` with your tickers:
```
AAPL
TSLA
NVDA
MSFT
AMZN
```

#### 4. News Filters
Customize news filtering in `benzinga_news.py`:
```python
NEWS_FILTERS = {
    'importance': 3,  # 1-5, where 5 is most important
    'topics': ['earnings', 'analyst-ratings', 'sec-filings'],
    'exclude_topics': ['price-target'],
}
```

### API Rate Limits & Best Practices
- **TDAmeritrade**: 120 requests/minute
- **Benzinga**: Varies by plan (check your subscription)
- Implement caching for repeated queries
- Use background tasks for periodic updates

### Docker Deployment (Enhanced)
```bash
# Build with all environment variables
docker build \
  --build-arg api_key=YOUR_TOS_KEY \
  --build-arg benzinga_key=YOUR_BENZINGA_KEY \
  --build-arg discord_webhook=YOUR_DISCORD_WEBHOOK \
  -t tos_options_dashboard:enhanced .

# Run with port mapping
docker run -p 8050:8050 -d tos_options_dashboard:enhanced
```

### Roadmap
- [ ] Add Benzinga news fetcher script
- [ ] Implement Discord webhook notifications
- [ ] Create configuration file for customization
- [ ] Add options flow analysis
- [ ] Implement real-time alert system
- [ ] Add backtesting capabilities
- [ ] Create mobile-responsive UI improvements
- [ ] Add portfolio tracking features

### Contributing
Feel free to submit issues and enhancement requests!

### License
MIT License (see original repository)

---

**Note**: This is a customized fork with enhanced features. For the original project, see [bernardcheng/tos_options_dashboard](https://github.com/bernardcheng/tos_options_dashboard)
