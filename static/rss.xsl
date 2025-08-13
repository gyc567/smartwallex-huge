<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>

<xsl:template match="/">
<html>
<head>
    <title><xsl:value-of select="/rss/channel/title"/> - RSS Feed</title>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }
        .header h1 {
            margin: 0 0 10px 0;
            font-size: 2.5em;
        }
        .header p {
            margin: 0;
            opacity: 0.9;
            font-size: 1.1em;
        }
        .feed-info {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .feed-info h2 {
            color: #667eea;
            margin-top: 0;
        }
        .item {
            background: white;
            margin-bottom: 20px;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: transform 0.2s ease;
        }
        .item:hover {
            transform: translateY(-2px);
        }
        .item h3 {
            margin: 0 0 10px 0;
            color: #333;
        }
        .item h3 a {
            color: #667eea;
            text-decoration: none;
        }
        .item h3 a:hover {
            text-decoration: underline;
        }
        .item .date {
            color: #666;
            font-size: 0.9em;
            margin-bottom: 15px;
        }
        .item .description {
            color: #555;
            line-height: 1.6;
        }
        .subscribe-info {
            background: #e8f4fd;
            border: 1px solid #bee5eb;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
        }
        .subscribe-info h3 {
            color: #0c5460;
            margin-top: 0;
        }
        .rss-url {
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            padding: 10px;
            font-family: monospace;
            word-break: break-all;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1><xsl:value-of select="/rss/channel/title"/></h1>
        <p><xsl:value-of select="/rss/channel/description"/></p>
    </div>

    <div class="subscribe-info">
        <h3>🔔 订阅此RSS源</h3>
        <p>这是一个RSS订阅源。您可以使用RSS阅读器（如Feedly、Inoreader等）来订阅此源，以便及时获取最新文章更新。</p>
        <div class="rss-url">
            <xsl:value-of select="/rss/channel/link"/>index.xml
        </div>
    </div>

    <div class="feed-info">
        <h2>📰 最新文章</h2>
        <p>以下是最近发布的文章列表：</p>
    </div>

    <xsl:for-each select="/rss/channel/item">
        <div class="item">
            <h3>
                <a href="{link}" target="_blank">
                    <xsl:value-of select="title"/>
                </a>
            </h3>
            <div class="date">
                📅 发布时间: <xsl:value-of select="pubDate"/>
            </div>
            <div class="description">
                <xsl:value-of select="description" disable-output-escaping="yes"/>
            </div>
        </div>
    </xsl:for-each>

    <div style="text-align: center; margin-top: 40px; padding: 20px; color: #666;">
        <p>由 <a href="{/rss/channel/link}" style="color: #667eea;">SmartWallex</a> 提供 | 
        使用 <a href="https://gohugo.io" style="color: #667eea;">Hugo</a> 生成</p>
    </div>
</body>
</html>
</xsl:template>

</xsl:stylesheet>