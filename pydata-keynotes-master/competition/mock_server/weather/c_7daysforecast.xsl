<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<body>
<p><h3>For a complete dataset, please download the XML for further processing.  Thank you.</h3></p>
Last Update: <xsl:value-of select="SevenDaysForecast/System/SysPubdate"/>

<table border="1" cellSpacing="0" cellPadding="8" >
<xsl:for-each select="SevenDaysForecast/Custom/WeatherForecast">
	<tr>
		<td><xsl:value-of select="ValidFor"/></td>
		<td><xsl:value-of select="c_DayOfWeek"/></td>
		<td><xsl:value-of select="Icon/IconName"/></td>
		<xsl:for-each select="Temperature">
			<td><xsl:value-of select="Value"/><xsl:value-of select="MeasureUnit"/></td>
		</xsl:for-each>
		<xsl:for-each select="Humidity">
			<td><xsl:value-of select="Value"/><xsl:value-of select="MeasureUnit"/></td>
		</xsl:for-each>
		<td><xsl:value-of select="WeatherDescription"/></td>		
	</tr>
</xsl:for-each>
</table>


  
</body>
</html>