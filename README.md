# Harkness

![a gif image of jack harkness from doctor who](https://media.giphy.com/media/AJzz2zfBDd19C/giphy.gif)

----

A simple Python script to find out the battery level on an Ubuntu laptop, and turn the power supply on and off accordingly, so it stays powered up constantly but without overheating.

----

## Why?

At some point I would like to run a basic server at home, or at least have somewhere to run scripts and cron jobs without using my 'proper' computer.

I had a couple of old laptops hanging around and thought of using those but the thought of leaving them plugged in 24/7 was not a happy one for me.

Hence Harkness.


----
## What do you need to run this?

- a laptop. Mine runs Ubuntu and the code works with that. You might need to dig around in your system files if you're not on Ubuntu, to find the right ones.
- [Python](https://docs.python-guide.org/starting/install3/linux/). If you've not used Python before, welcome aboard! I've only been doing it about a month, myself. If you are looking for resources I would recommend "Python Crash Course" or "Automate the Boring Stuff with Python" from No Starch Books.
- a smart-plug. I'm using one from Kasa that was on sale on Amazon. It's important (vital, in fact) that your plug works with [IFTTT](https://ifttt.com/).
- an [IFTTT](https://ifttt.com/) account. You'll need to set up a couple of [webhooks](https://ifttt.com/services/maker_webhooks) to work with your plug. Hoopefully it should be fairly self-explanatory once you're doing it.
- some way of notifying yourself that it's working. I guess this is optional really - I find it quite comforting to get occasional updates but you might not. I'm using a [Telegram](https://telegram.org/) bot, using the [telepot](https://telepot.readthedocs.io) module.
- um
- that's it

Also there's not much point having this set up if you're not running it every so often. I have a cron job set up to run it every 15 minutes and that seems to work pretty well.
More info on cron jobs [here](https://danvatterott.com/blog/2017/09/01/automating-jobs-on-ubuntu/).
