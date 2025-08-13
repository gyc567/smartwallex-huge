<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>

<xsl:template match="/">
<html>
<head>
    <title>SmartWallex - 网站地图</title>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1000px;
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
        .stats {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .stats h2 {
            color: #667eea;
            margin-top: 0;
        }
        table {
            width: 100%;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-collapse: collapse;
        }
        th {
            background: #667eea;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }
        td {
            padding: 12px 15px;
            border-bottom: 1px solid #eee;
        }
        tr:hover {
            background-color: #f8f9fa;
        }
        .url {
            color: #667eea;
            text-decoration: none;
            word-break: break-all;
        }
        .url:hover {
            text-decoration: underline;
        }
        .priority {
            text-align: center;
            font-weight: bold;
        }
        .priority.high { color: #28a745; }
        .priority.medium { color: #ffc107; }
        .priority.low { color: #6c757d; }
        .lastmod {
            font-size: 0.9em;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🗺️ SmartWallex 网站地图</h1>
        <p>专业的加密货币聪明钱信息聚合平台</p>
    </div>

    <div class="stats">
        <h2>📊 网站统计</h2>
        <p>总页面数: <strong><xsl:value-of select="count(//sitemap:url)"/></strong></p>
        <p>最后更新: <strong><xsl:value-of select="//sitemap:lastmod[1]"/></strong></p>
    </div>

    <table>
        <thead>
            <tr>
                <th>📄 页面URL</th>
                <th>📅 最后修改</th>
                <th>🔄 更新频率</th>
                <th>⭐ 优先级</th>
            </tr>
        </thead>
        <tbody>
            <xsl:for-each select="//sitemap:url">
                <xsl:sort select="sitemap:priority" order="descending"/>
                <tr>
                    <td>
                        <a href="{sitemap:loc}" class="url" target="_blank">
                            <xsl:value-of select="sitemap:loc"/>
                        </a>
                    </td>
                    <td class="lastmod">
                        <xsl:choose>
                            <xsl:when test="sitemap:lastmod">
                                <xsl:value-of select="sitemap:lastmod"/>
                            </xsl:when>
                            <xsl:otherwise>-</xsl:otherwise>
                        </xsl:choose>
                    </td>
                    <td>
                        <xsl:choose>
                            <xsl:when test="sitemap:changefreq">
                                <xsl:value-of select="sitemap:changefreq"/>
                            </xsl:when>
                            <xsl:otherwise>-</xsl:otherwise>
                        </xsl:choose>
                    </td>
                    <td class="priority">
                        <xsl:choose>
                            <xsl:when test="sitemap:priority">
                                <span>
                                    <xsl:attribute name="class">
                                        priority
                                        <xsl:choose>
                                            <xsl:when test="sitemap:priority &gt;= 0.8">high</xsl:when>
                                            <xsl:when test="sitemap:priority &gt;= 0.5">medium</xsl:when>
                                            <xsl:otherwise>low</xsl:otherwise>
                                        </xsl:choose>
                                    </xsl:attribute>
                                    <xsl:value-of select="sitemap:priority"/>
                                </span>
                            </xsl:when>
                            <xsl:otherwise>-</xsl:otherwise>
                        </xsl:choose>
                    </td>
                </tr>
            </xsl:for-each>
        </tbody>
    </table>

    <div style="text-align: center; margin-top: 40px; padding: 20px; color: #666;">
        <p>由 <a href="https://www.smartwallex.com" style="color: #667eea;">SmartWallex</a> 提供 | 
        使用 <a href="https://gohugo.io" style="color: #667eea;">Hugo</a> 生成</p>
    </div>
</body>
</html>
</xsl:template>

</xsl:stylesheet>