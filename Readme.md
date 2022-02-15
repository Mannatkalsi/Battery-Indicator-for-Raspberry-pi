**Battery Indicator for Raspberry pi connected with external battery.**

As there is no way to check Battery % so i've created a battery indicator.
We need a battery low message in speaker when the battery level reaches 15% of the capacity. There is no way to count the voltage, so we are using countdown timer and beep sound in order to provide battery low notification.

**Only Information we have is :**
- System can run for 55 minutes when LED is off.
- When LED is ON the system can run for 25 minutes.

**Working :**
- When user turn on the system it ask the user if battery is fully charged or not.
- Created a text file which stores value of timer when user shutdown, reboot or close the system.
- Created a function which speed up the timer when LED is ON/OFF
- If user selects battery fully charged, timer starts from 55 mintues and if battery is not fully charged then timer reads the value from text file and starts the countdown from where timer was stopped.
- User can hear beep sound when battery at 15% and 1%. 
