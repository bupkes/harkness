#!/bin/bash -e

import math
import urllib.request
import datetime
import send_notification_to
import credentials


# finding out how much energy the battery has right now
energy_now_file = '/sys/class/power_supply/BAT1/energy_now'
with open(energy_now_file) as file_object:
    energy_now = file_object.read()
    energy_now = int(energy_now.rstrip())

# finding out how much the battery could hold, theoretically
energy_full_file = '/sys/class/power_supply/BAT1/energy_full'
with open(energy_full_file) as file_object:
    energy_full = file_object.read()
    energy_full = int(energy_full.rstrip())

# finding out whether the battery is charging or discharging
battery_status = '/sys/class/power_supply/BAT1/status'
with open(battery_status) as file_object:
    battery_status = file_object.read()
    battery_status = battery_status.rstrip()

# do some maths and work out the current battery level (percentage)
percentage_int = energy_now/energy_full*100
percentage_str = str(math.ceil(percentage_int))


# Now we decide when to start sending warning signals...

hungry_battery_level = 20   # This is the battery level at which Harkness starts worrying. Set it
                            # wherever you like, really.

if percentage_int <= warning_threshold:
    message = "Battery level: " + percentage_str + "%"
    send_notification_to.my_bot(message)

# ...and send a message to say whether we're plugged in

    if battery_status == "Discharging":
        send_notification_to.my_bot("I am not charging")
    else:
        send_notification_to.my_bot("I am charging")

# Once we get very low in charge, trigger the IFTTT webhook to turn on the smart plug
# It's pretty straightforward to set one up - see https://ifttt.com/maker_webhooks

really_hungry_battery_level = 10
if percentage_int <= really_hungry_battery_level:
    if battery_status == "Discharging":
        send_notification_to.my_bot("OK I am turning on the plug to see if that helps")
        light_on = urllib.request.urlopen(switch_on).read()     # Replace switch_on with your webhook URL

# If the battery is full (or full-ish), trigger the IFTTT trigger to turn off the switch

full_battery_level = 96     # Change to your liking
if percentage_int >= full_battery_level:
    send_notification_to.my_bot("Battery is pretty much full so I'm turning the plug off for a while")
    light_off = urllib.request.urlopen(switch_off).read()   # Replace switch_off with your webhook URL
