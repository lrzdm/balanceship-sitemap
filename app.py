from flask import Flask, Response

app = Flask(__name__)

# Google Analytics tag (sostituisci con il tuo ID)
GA_TAG = '''
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-PMRTNWT1ZZ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-PMRTNWT1ZZ');
</script>
'''

# Homepage SEO
@app.route('/')
def home():
    verification_tag = '<meta name="google-site-verification" content="P8TBKoEhxpfTVVZF7CTXHNp9dQVC0ynMTo18I9xdzvo" />'
    return f'''
    <html lang="en">
    <head>
        {verification_tag}
        {GA_TAG}
        <title>Balanceship - Smart Financial Insights</title>
        <meta name="description" content="Balanceship helps you explore KPIs, dashboards, and financial data of listed companies in a visual, interactive way." />
    </head>
    <body>
        <h1>Welcome to Balanceship</h1>
        <p>This is a support service for sitemap and SEO indexing.</p>
    </body>
    </html>
    '''

@app.route('/Graph')
def graph():
    return f'''
    <html>
    <head>
        {GA_TAG}
        <title>Company Financial Graphs - Balanceship</title>
        <meta name="description" content="View interactive financial graphs of public companies. Track revenue, profit, and key indicators over time." />
    </head>
    <body>
        <h1>Graph Page</h1>
        <p>Visualize financial KPIs in dynamic graphs.</p>
    </body>
    </html>
    '''

@app.route('/Database')
def database():
    return f'''
    <html>
    <head>
        {GA_TAG}
        <title>Financial Database - Balanceship</title>
        <meta name="description" content="Access a curated database of public companies with financial data from global stock exchanges." />
    </head>
    <body>
        <h1>Database Page</h1>
        <p>Explore company data by sector, geography, and more.</p>
    </body>
    </html>
    '''

@app.route('/KPI_Dashboard')
def kpi_dashboard():
    return f'''
    <html>
    <head>
        {GA_TAG}
        <title>KPI Dashboards - Balanceship</title>
        <meta name="description" content="Analyze KPIs like EBITDA, EPS, and Free Cash Flow through dashboards for better insights." />
    </head>
    <body>
        <h1>KPI Dashboard</h1>
        <p>Compare company performance across key metrics.</p>
    </body>
    </html>
    '''

@app.route('/Who_we_are')
def who_we_are():
    return f'''
    <html>
    <head>
        {GA_TAG}
        <title>Who We Are - Balanceship</title>
        <meta name="description" content="Learn about the mission, vision, and team behind Balanceship, your financial data partner." />
    </head>
    <body>
        <h1>About Us</h1>
        <p>Meet the team and discover our purpose.</p>
    </body>
    </html>
    '''

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

@app.route('/robots.txt')
def robots():
    robots_txt = '''User-agent: *
Allow: /

Sitemap: https://balanceship-sitemap.onrender.com/sitemap.xml'''
    return Response(robots_txt, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
