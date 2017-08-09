<h1>Local Weather Station</h1>
<h3>Application</h3>
<p>This ia a local weather station application that integrates a Raspberry PI with a 
temperature, humidity and barometric sensor module.
<h3>How it works</h3>
</p><p>The sensor suite is interfaced with Python to monitor the sensors and control the 
8x8 RGB LED matrix display. Python gets a reading every 15 minutes and stores the data in a PostgreSQL database, while displaying 
live temperature, humidity and barometric pressure on the LED.
</p>
<p>The Postgres database has two tables, one for storing the temperature, humidity and 
pressure sensor readings.  The second table stores a US Census zip code data base with longitude 
and latitude coordinates for each zipcode in the United States</p>
<p>Using JavaScript on the front end, sensor data and geo cordinates can be accessed and displayed.  
The <a href="http://darksky.net">Dark Sky</a> weather API was added to provide US weather information independant 
of the local data.  Using the PostgreSQL zip code information cordinates are requested from the Dark Sky API</p>
<p>Local measurments can displayed using Chart.js to see trends and history.<p>
<p><strong>Weather Station</strong> is a multipage progressive web app that reinforced the skills I learned while attending
<a href="http://digitalcrafts.com">DigitalCrafts</a> coding boot camp.<p>
<p><strong>Weather Station</strong> application takes advantage of the Raspberry PI to host the web application 
locally behind a firewall through a <a href="https://dataplicity.com>Dataplicity"></a> connection monitoring the local host.<p>


<h3>Tools</h3>
<ul>
<li>Python</li>
<li>Threading/li>
<li>Time</li>
<li>PostgreSQL</li>
<li>JavaScript</>
<li>Express</li>
<li>HTML</li>
<li>CSS</li>
<li>Apicache</li>
<li>Axios</li>
<li>Chart.js</li>
<li>HBS</ui>
<li>PG-Promise</li>
</ul>

