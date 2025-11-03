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
    if url.startswith("https://balanceship.net"):
        url = url.replace("https://balanceship.net", "https://www.balanceship.net", 1)
        return redirect(url, code=301)

# --- Gestione automatica del meta noindex ---
def maybe_noindex():
    """
    Aggiunge il meta noindex solo se il dominio NON è www.balanceship.net.
    Serve per evitare che sitemap.balanceship.net venga indicizzato.
    """
    if "www.balanceship.net" not in request.host:
        return '<meta name="robots" content="noindex, follow">'
    return ''

# --- HOME ---
@app.route('/')
def home():
    return f'''
    <html lang="en">
    <head>
        <meta name="google-site-verification" content="P8TBKoEhxpfTVVZF7CTXHNp9dQVC0ynMTo18I9xdzvo" />
        {GA_TAG}
        {maybe_noindex()}
        <link rel="canonical" href="https://www.balanceship.net/" />
        <title>Balanceship - Smart Financial Insights</title>
        <meta name="description" content="Balanceship helps you explore KPIs, dashboards, and financial data of listed companies in a visual, interactive way." />
    </head>
    <body>
        <h1>Welcome to Balanceship</h1>
        <p>This is a support service for sitemap and SEO indexing.</p>
    </body>
    </html>
    '''

# --- GRAPH ---
@app.route('/Graph')
def graph():
    return f'''
    <html>
    <head>
        {GA_TAG}
        {maybe_noindex()}
        <link rel="canonical" href="https://www.balanceship.net/Graph" />
        <title>Company Financial Graphs - Balanceship</title>
        <meta name="description" content="View interactive financial graphs of public companies. Track revenue, profit, and key indicators over time." />
    </head>
    <body>
        <h1>Graph Page</h1>
        <p>Visualize financial KPIs in dynamic graphs.</p>
    </body>
    </html>
    '''

# --- DATABASE ---
@app.route('/Database')
def database():
    return f'''
    <html>
    <head>
        {GA_TAG}
        {maybe_noindex()}
        <link rel="canonical" href="https://www.balanceship.net/Database" />
        <title>Financial Database - Balanceship</title>
        <meta name="description" content="Access a curated database of public companies with financial data from global stock exchanges." />
    </head>
    <body>
        <h1>Database Page</h1>
        <p>Explore company data by sector, geography, and more.</p>
    </body>
    </html>
    '''

# --- KPI DASHBOARD ---
@app.route('/KPI_Dashboard')
def kpi_dashboard():
    return f'''
    <html>
    <head>
        {GA_TAG}
        {maybe_noindex()}
        <link rel="canonical" href="https://www.balanceship.net/KPI_Dashboard" />
        <title>KPI Dashboards - Balanceship</title>
        <meta name="description" content="Analyze KPIs like EBITDA, EPS, and Free Cash Flow through dashboards for better insights." />
    </head>
    <body>
        <h1>KPI Dashboard</h1>
        <p>Compare company performance across key metrics.</p>
    </body>
    </html>
    '''

# --- WHO WE ARE ---
@app.route('/Who_we_are')
def who_we_are():
    return f'''
    <html>
    <head>
        {GA_TAG}
        {maybe_noindex()}
        <link rel="canonical" href="https://www.balanceship.net/Who_we_are" />
        <title>Who We Are - Balanceship</title>
        <meta name="description" content="Learn about the mission, vision, and team behind Balanceship, your financial data partner." />
    </head>
    <body>
        <h1>About Us</h1>
        <p>Meet the team and discover our purpose.</p>
    </body>
    </html>
    '''

# --- SITEMAP ---
@app.route('/sitemap.xml')
def sitemap():
    sitemap_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.balanceship.net/</loc><lastmod>2025-01-16</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>
  <url><loc>https://www.balanceship.net/Database</loc><lastmod>2025-01-16</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>
  <url><loc>https://www.balanceship.net/KPI_Dashboard</loc><lastmod>2025-01-16</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>
  <url><loc>https://www.balanceship.net/Graph</loc><lastmod>2025-01-16</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>
  <url><loc>https://www.balanceship.net/Who_we_are</loc><lastmod>2025-01-16</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>
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
