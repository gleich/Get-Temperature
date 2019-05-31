# Get_Temperature

[![Build Status](https://travis-ci.org/Matt-Gleich/Get-Temperature.svg?branch=master)](https://travis-ci.org/Matt-Gleich/Get-Temperature)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/776c7271a1b0430e967b329e6f2715b8)](https://www.codacy.com/app/matthewgleich/Get-Temperature?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Matt-Gleich/Get-Temperature&amp;utm_campaign=Badge_Grade)

## Description
The Get-Temperature program will get the temperature and humidity from from a sensor (DHT11 Temperature and Humidity Sensor) and write it to a google sheet. It also get the date and time and write that too.

## Features
Below is a list of all the features of this program:

1. Collects the temperature, humidity, current time, and current date.
2. Gets that data and writes it a JSON locally.
3. Updates the data to a Google Sheet that shows the most recent reading
4. Writes the data to a Google Sheet that lists all the readings

## Missing files
In order to write to the google sheet, the program needs a file called `gs_creds.json` that holds the API key for the Google Sheet. If you are looking for a tutorial on how to get this key, here is a link to a tutorial on how:
[Tutorial Video](https://www.youtube.com/watch?v=cnPlKLEGR7E)