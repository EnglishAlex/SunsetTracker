
![SunTracker](./images/SunTracker.jpeg)


# SunsetTracker
Track the day's progress and time to sunset using the [Pimoroni InkyPhat](https://shop.pimoroni.com/products/inky-phat)

- It take a long 2 or 3 seconds to render the InkyPhat display making development slow.
- With a bit of hacking you can simulate the InkyPhat inside a jupyter notebook and speed up development.
- Inside a notebook its quick and easy to learn how to use the Python Image Library "PIL" and try out your code.
- Working example in `sunset_timer.ipynb`

## Virtual InkyPhat
![virtual_inkyphat](./images/virtual_inkyphat.png)

## How to use
- Install the Inky-Phat, run the examples to know that it's working.
- Clone this code to your pi i.e. ``git clone https://github.com/EnglishAlex/SunsetTracker.git``
- Running  `sunrise.py` opens the ``sunrise2020.csv`` reads the sunrise/set times and renders the InkyPhat.
- Set the crontab to run script every few minutes [pi.cron.txt](./pi.cron.txt)

## smart addition to your Pi
![Sun Tracker in action](./images/inkyphat-on-pi.jpeg)

## improvments
- [ ] Explain how to generate your own sunrise sunset times from [timeanddate.com](https://www.timeanddate.com/sun/uk/london?month=1&year=2020)
- [ ] Use API to fetch sunrise/sunset for your location
- [ ] Make it interactive with [buttons](https://shop.pimoroni.com/products/button-shim)
- [ ] Tidy the code a lot
- [ ] Better explanations of how it works


## References
- https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat
- https://github.com/pimoroni/inky
- https://shop.pimoroni.com/products/inky-phat

## snippets
Convert a jupyter notebook to python script
`jupyter nbconvert --to script <your notebook>.ipynb --output <your new scriptfile.py`
