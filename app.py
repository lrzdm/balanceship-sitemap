from flask import Flask, Response, request, redirect

app = Flask(__name__)

# --- Google Analytics ---
GA_TAG = '''
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-Q5FDX0L1H2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-Q5FDX0L1H2');
</script>
'''

# --- Redirezioni verso HTTPS e www ---
@app.before_request
def force_https_www():
    url = request.url
    if url.startswith("http://"):
        url = url.replace("http://", "https://", 1)
        return redirect(url, code=301)
    # Commento questa parte perché il worker gestisce già www vs non-www
    # if url.startswith("https://balanceship.net"):
    #     url = url.replace("https://balanceship.net", "https://www.balanceship.net", 1)
    #     return redirect(url, code=301)

# --- Gestione automatica del meta noindex ---
def maybe_noindex():
    """
    Aggiunge il meta noindex solo se il dominio NON è www.balanceship.net.
    Serve per evitare che sitemap.balanceship.net venga indicizzato.
    """
    if "www.balanceship.net" not in request.host and "balanceship.net" not in request.host:
        return '<meta name="robots" content="noindex, follow">'
    return ''

# --- HOME ---
@app.route('/')
@app.route('/index.html')
def home():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="P8TBKoEhxpfTVVZF7CTXHNp9dQVC0ynMTo18I9xdzvo" />
    {GA_TAG}
    {maybe_noindex()}
    <link rel="canonical" href="https://balanceship.net/" />
    
    <!-- SEO Meta Tags -->
    <title>Balanceship – Global Financial Dashboard | Company KPIs & Investment Insights</title>
    <meta name="description" content="Explore company KPIs and financial data on BalanceShip. Use AI-powered insights to guide smart investment decisions. Access financial dashboards for thousands of listed companies worldwide.">
    
    <!-- Open Graph / LinkedIn -->
    <meta property="og:title" content="Balanceship – Global Financial Dashboard">
    <meta property="og:description" content="Explore KPIs, revenue, and financial ratios for thousands of companies.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://balanceship.net">
    <meta property="og:image" content="https://balanceship.net/images/icon.png">
    <meta property="og:site_name" content="Balanceship">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Balanceship – Global Financial Dashboard">
    <meta name="twitter:description" content="Explore KPIs, revenue, and financial ratios for thousands of companies.">
    <meta name="twitter:image" content="https://balanceship.net/images/icon.png">
    
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; margin-top: 30px; }}
        p {{ color: #555; }}
        nav {{ margin: 30px 0; padding: 20px 0; border-top: 2px solid #eee; border-bottom: 2px solid #eee; }}
        nav a {{ margin-right: 20px; color: #3498db; text-decoration: none; font-weight: bold; }}
        nav a:hover {{ text-decoration: underline; }}
        .feature {{ margin: 20px 0; padding: 15px; background: #f8f9fa; border-left: 4px solid #3498db; }}
    </style>
</head>
<body>
    <h1>Welcome to Balanceship</h1>
    <p><strong>Your Gateway to Smart Financial Analysis</strong></p>
    
    <p>Balanceship is a cutting-edge financial platform that helps investors, analysts, and finance professionals explore company performance through interactive dashboards, comprehensive KPI analysis, and AI-powered insights.</p>
    
    <h2>What We Offer</h2>
    
    <div class="feature">
        <h3>📊 Interactive Financial Dashboards</h3>
        <p>Visualize and analyze financial data from thousands of publicly listed companies worldwide. Track revenue trends, profitability metrics, and growth indicators in real-time.</p>
    </div>
    
    <div class="feature">
        <h3>📈 KPI Analysis Tools</h3>
        <p>Deep dive into critical Key Performance Indicators including EBITDA, EPS, Free Cash Flow, ROE, and more. Compare companies across sectors and identify investment opportunities.</p>
    </div>
    
    <div class="feature">
        <h3>🗄️ Comprehensive Financial Database</h3>
        <p>Access curated financial data from global stock exchanges. Filter by sector, geography, market cap, and performance metrics to find the companies that matter to you.</p>
    </div>
    
    <div class="feature">
        <h3>📉 Dynamic Financial Graphs</h3>
        <p>Explore historical trends and forecast future performance with our interactive charting tools. Visualize complex financial relationships with ease.</p>
    </div>
    
    <h2>Why Choose Balanceship?</h2>
    <p>Whether you're a professional investor, financial analyst, or an individual looking to make informed investment decisions, Balanceship provides the tools and insights you need to succeed in today's dynamic markets.</p>
    
    <ul>
        <li>Real-time financial data updates</li>
        <li>User-friendly interface designed for efficiency</li>
        <li>Comprehensive coverage of global markets</li>
        <li>AI-powered analytical insights</li>
        <li>Mobile-responsive design for on-the-go analysis</li>
    </ul>
    
    <nav>
        <a href="/">Home</a>
        <a href="/Database">Database</a>
        <a href="/KPI_Dashboard">KPI Dashboard</a>
        <a href="/Graph">Graphs</a>
        <a href="/Who_we_are">About Us</a>
    </nav>
    
    <p style="color: #777; font-size: 0.9em; margin-top: 40px;">© 2025 Balanceship. All rights reserved. | Smart Financial Insights for Better Investment Decisions</p>
</body>
</html>'''

# --- GRAPH ---
@app.route('/Graph')
@app.route('/Graph.html')
def graph():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {GA_TAG}
    {maybe_noindex()}
    <link rel="canonical" href="https://balanceship.net/Graph" />
    <title>Company Financial Graphs - Interactive Charts | Balanceship</title>
    <meta name="description" content="View interactive financial graphs of public companies. Track revenue, profit, EBITDA, cash flow and key indicators over time with dynamic visualization tools.">
    
    <meta property="og:title" content="Financial Graphs - Balanceship">
    <meta property="og:description" content="Interactive financial charts for analyzing company performance over time.">
    <meta property="og:url" content="https://balanceship.net/Graph">
    
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6; }}
        h1 {{ color: #2c3e50; }}
        nav {{ margin: 30px 0; padding: 20px 0; border-top: 2px solid #eee; }}
        nav a {{ margin-right: 20px; color: #3498db; text-decoration: none; }}
    </style>
</head>
<body>
    <h1>📉 Financial Graphs & Charts</h1>
    <p>Visualize company financial performance through interactive, dynamic graphs. Our charting tools allow you to:</p>
    
    <ul>
        <li>Track revenue and profit trends over multiple years</li>
        <li>Compare financial metrics across different time periods</li>
        <li>Analyze growth patterns and identify market cycles</li>
        <li>Visualize relationships between different KPIs</li>
        <li>Export and share custom visualizations</li>
    </ul>
    
    <h2>Available Chart Types</h2>
    <p><strong>Line Charts:</strong> Perfect for tracking trends over time</p>
    <p><strong>Bar Charts:</strong> Compare metrics across companies or periods</p>
    <p><strong>Area Charts:</strong> Visualize cumulative growth and market share</p>
    <p><strong>Candlestick Charts:</strong> Analyze stock price movements</p>
    
    <nav>
        <a href="/">Home</a>
        <a href="/Database">Database</a>
        <a href="/KPI_Dashboard">KPI Dashboard</a>
        <a href="/Who_we_are">About Us</a>
    </nav>
</body>
</html>'''

# --- DATABASE ---
@app.route('/Database')
@app.route('/Database.html')
def database():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {GA_TAG}
    {maybe_noindex()}
    <link rel="canonical" href="https://balanceship.net/Database" />
    <title>Financial Database - Global Companies Data | Balanceship</title>
    <meta name="description" content="Access a curated database of public companies with financial data from global stock exchanges. Filter by sector, market cap, geography and financial metrics.">
    
    <meta property="og:title" content="Financial Database - Balanceship">
    <meta property="og:description" content="Comprehensive database of global companies with real-time financial data.">
    <meta property="og:url" content="https://balanceship.net/Database">
    
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6; }}
        h1 {{ color: #2c3e50; }}
        nav {{ margin: 30px 0; padding: 20px 0; border-top: 2px solid #eee; }}
        nav a {{ margin-right: 20px; color: #3498db; text-decoration: none; }}
        .highlight {{ background: #fff3cd; padding: 10px; border-left: 4px solid #ffc107; margin: 20px 0; }}
    </style>
</head>
<body>
    <h1>🗄️ Global Financial Database</h1>
    <p>Explore our comprehensive database of publicly listed companies from stock exchanges worldwide. Access detailed financial information, historical data, and real-time updates.</p>
    
    <div class="highlight">
        <strong>Coverage:</strong> Thousands of companies from NYSE, NASDAQ, LSE, Euronext, and major global exchanges
    </div>
    
    <h2>Database Features</h2>
    <ul>
        <li><strong>Sector Classification:</strong> Technology, Finance, Healthcare, Energy, Consumer Goods, and more</li>
        <li><strong>Geographic Filtering:</strong> Search by country, region, or global markets</li>
        <li><strong>Market Cap Ranges:</strong> From small-cap to mega-cap companies</li>
        <li><strong>Financial Metrics:</strong> Revenue, profit margins, debt ratios, growth rates</li>
        <li><strong>Historical Data:</strong> Access years of financial statements and reports</li>
        <li><strong>Real-time Updates:</strong> Latest quarterly and annual results</li>
    </ul>
    
    <h2>How to Use</h2>
    <p>Our intuitive search and filter system allows you to quickly find companies that match your investment criteria. Compare multiple companies side-by-side and export data for further analysis.</p>
    
    <nav>
        <a href="/">Home</a>
        <a href="/KPI_Dashboard">KPI Dashboard</a>
        <a href="/Graph">Graphs</a>
        <a href="/Who_we_are">About Us</a>
    </nav>
</body>
</html>'''

# --- KPI DASHBOARD ---
@app.route('/KPI_Dashboard')
@app.route('/KPI_Dashboard.html')
def kpi_dashboard():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {GA_TAG}
    {maybe_noindex()}
    <link rel="canonical" href="https://balanceship.net/KPI_Dashboard" />
    <title>KPI Dashboards - Financial Metrics Analysis | Balanceship</title>
    <meta name="description" content="Analyze critical KPIs like EBITDA, EPS, ROE, Free Cash Flow and P/E ratios through interactive dashboards. Compare company performance across key financial metrics.">
    
    <meta property="og:title" content="KPI Dashboards - Balanceship">
    <meta property="og:description" content="Comprehensive KPI analysis tools for evaluating company financial health.">
    <meta property="og:url" content="https://balanceship.net/KPI_Dashboard">
    
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6; }}
        h1 {{ color: #2c3e50; }}
        h3 {{ color: #34495e; margin-top: 20px; }}
        nav {{ margin: 30px 0; padding: 20px 0; border-top: 2px solid #eee; }}
        nav a {{ margin-right: 20px; color: #3498db; text-decoration: none; }}
        .kpi-box {{ background: #f8f9fa; padding: 15px; margin: 15px 0; border-left: 4px solid #28a745; }}
    </style>
</head>
<body>
    <h1>📊 KPI Dashboard</h1>
    <p>Monitor and analyze the most important Key Performance Indicators for informed investment decisions. Our dashboards provide deep insights into company financial health and operational efficiency.</p>
    
    <h2>Core Financial KPIs</h2>
    
    <div class="kpi-box">
        <h3>💰 EBITDA (Earnings Before Interest, Taxes, Depreciation, Amortization)</h3>
        <p>Measure operational profitability and cash generation capacity</p>
    </div>
    
    <div class="kpi-box">
        <h3>📈 EPS (Earnings Per Share)</h3>
        <p>Track profitability on a per-share basis for shareholder value assessment</p>
    </div>
    
    <div class="kpi-box">
        <h3>💵 Free Cash Flow</h3>
        <p>Analyze cash available after capital expenditures for dividends and growth</p>
    </div>
    
    <div class="kpi-box">
        <h3>🎯 ROE (Return on Equity)</h3>
        <p>Evaluate how efficiently a company uses shareholder equity to generate profit</p>
    </div>
    
    <div class="kpi-box">
        <h3>📊 P/E Ratio (Price-to-Earnings)</h3>
        <p>Compare company valuation relative to earnings performance</p>
    </div>
    
    <div class="kpi-box">
        <h3>💳 Debt-to-Equity Ratio</h3>
        <p>Assess financial leverage and capital structure risk</p>
    </div>
    
    <h2>Dashboard Features</h2>
    <ul>
        <li>Real-time KPI calculations and updates</li>
        <li>Historical trend analysis and forecasting</li>
        <li>Peer comparison and industry benchmarks</li>
        <li>Custom KPI combinations and alerts</li>
        <li>Export capabilities for presentations and reports</li>
    </ul>
    
    <nav>
        <a href="/">Home</a>
        <a href="/Database">Database</a>
        <a href="/Graph">Graphs</a>
        <a href="/Who_we_are">About Us</a>
    </nav>
</body>
</html>'''

# --- WHO WE ARE ---
@app.route('/Who_we_are')
@app.route('/Who_we_are.html')
def who_we_are():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {GA_TAG}
    {maybe_noindex()}
    <link rel="canonical" href="https://balanceship.net/Who_we_are" />
    <title>Who We Are - About Balanceship | Our Mission & Team</title>
    <meta name="description" content="Learn about the mission, vision, and team behind Balanceship, your trusted partner for financial data analysis and investment insights.">
    
    <meta property="og:title" content="About Balanceship - Who We Are">
    <meta property="og:description" content="Discover the team and mission driving innovation in financial data analysis.">
    <meta property="og:url" content="https://balanceship.net/Who_we_are">
    
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6; }}
        h1 {{ color: #2c3e50; }}
        nav {{ margin: 30px 0; padding: 20px 0; border-top: 2px solid #eee; }}
        nav a {{ margin-right: 20px; color: #3498db; text-decoration: none; }}
        .mission {{ background: #e8f4f8; padding: 20px; border-radius: 8px; margin: 20px 0; }}
    </style>
</head>
<body>
    <h1>👋 About Balanceship</h1>
    
    <div class="mission">
        <h2>Our Mission</h2>
        <p>At Balanceship, we believe that everyone deserves access to professional-grade financial analysis tools. Our mission is to democratize financial data and empower investors, analysts, and finance professionals with the insights they need to make informed decisions.</p>
    </div>
    
    <h2>What Drives Us</h2>
    <p>We're passionate about transforming complex financial data into clear, actionable insights. Through innovative technology and user-centered design, we're building the financial analysis platform of the future.</p>
    
    <h2>Our Values</h2>
    <ul>
        <li><strong>Transparency:</strong> Clear, honest data without hidden agendas</li>
        <li><strong>Innovation:</strong> Constantly improving our tools and methodologies</li>
        <li><strong>Accessibility:</strong> Making professional analysis available to all</li>
        <li><strong>Accuracy:</strong> Rigorous data verification and quality control</li>
        <li><strong>User-Focus:</strong> Designing for real-world needs and workflows</li>
    </ul>
    
    <h2>Our Vision</h2>
    <p>We envision a world where financial analysis is no longer limited to Wall Street professionals. With Balanceship, anyone can access the same powerful tools and insights used by top investment firms.</p>
    
    <h2>Join Us</h2>
    <p>Whether you're a seasoned investor or just starting your financial journey, Balanceship is here to support you. Explore our platform and discover how we can help you achieve your financial goals.</p>
    
    <nav>
        <a href="/">Home</a>
        <a href="/Database">Database</a>
        <a href="/KPI_Dashboard">KPI Dashboard</a>
        <a href="/Graph">Graphs</a>
    </nav>
    
    <p style="color: #777; margin-top: 40px;">Questions? Contact us at: info@balanceship.net</p>
</body>
</html>'''

# --- SITEMAP ---
@app.route('/sitemap.xml')
def sitemap():
    sitemap_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://balanceship.net/</loc><lastmod>2025-01-16</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>
  <url><loc>https://balanceship.net/Database</loc><lastmod>2025-01-16</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>
  <url><loc>https://balanceship.net/KPI_Dashboard</loc><lastmod>2025-01-16</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>
  <url><loc>https://balanceship.net/Graph</loc><lastmod>2025-01-16</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>
  <url><loc>https://balanceship.net/Who_we_are</loc><lastmod>2025-01-16</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>
</urlset>'''
    return Response(sitemap_xml, mimetype='application/xml')

# --- ROBOTS.TXT ---
@app.route('/robots.txt')
def robots():
    robots_txt = '''User-agent: *
Allow: /

Sitemap: https://sitemap.balanceship.net/sitemap.xml'''
    return Response(robots_txt, mimetype='text/plain')

# --- MAIN ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
