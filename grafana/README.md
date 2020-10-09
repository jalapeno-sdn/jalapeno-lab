## Adding Grafana Dashboards to Jalapeno

Jalapeno's installation script does not automatically add Grafana dashboards.  
To do so:

1.  Connect to Grafana: Http://<jalapeno_ip>:30300
2.  User/pw = root/jalapeno 
3.	After authenticating click on add data source, choose InfluxDB
4.  Enter InfluxDB parameters:
```
URL: http://influxdb:8086
Database: mdt_db
Basic Auth: root/jalapeno
Http method GET
```
5.  Click 'save and test'
4.  Once added, hover over the Dashboard icon (4 squares on the left), click 'Manage'
5.	Click import on the right side of the screen
6.	Import telemetry json files.  Examples for the Jalapeno-lab topology are in this directory
7.  Modify the json as necessary to fit your topology



