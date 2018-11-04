Best practice for sleep command
===

On its own, the sleep command is completely useless unless you like locking up your terminal window, but as part of a script, it can be used in many different ways, including as a pause factor before retrying a command.

For instance, imagine you had a script that processed files copied from another server. The script should not start the copy process until all of the files have finished downloading. The download process is performed by a completely seperate script.  

The script for copying the files may well contain a loop to test whether all of the files have been downloaded(i.e. it knows there should be 50 files and when 50 files have been found, the copy process is started.).  

There is no point of the script continually testing, as it takes up processor time. Instead, you might choose to test whether there are enough files copied and if there aren't, pause for a few minutes and then try again. The sleep command is perfect in these circumstances..

## How to Use the sleep Command
to puase for 5 seconds
> sleep 5s  
- s - seconds
- m - minutes
- h - hours
- d - days
When it comes to waiting days for something to happen, it might be worth considering using a cron job to run the script at regular intervals, as opposed to having a script running in the background for days on end.  

The number for the sleep command doesn't have to be a whole number. You can also use floating point numbers.

For example, it is perfectly ok to use the following syntax:
> sleep 3.5s

## An Example Use for the sleep Command
Countdown clock:
```bash
#!/bin/bash
x=10
while [ $x -gt 0 ]; do
    sleep 1s
    clear
    echo "$x seconds until blast off"
    x=$(( $x - 1))
done
```
The sleep command pauses the script for 1 second each time around the loop.  

The rest of the script clears the screen each iteration, displays the message "x seconds until blast off" (i.e. 10) and then subtracts 1 from the value of x.  

Without the sleep command, the script would zoom through and the messages would be displayed too quickly.
