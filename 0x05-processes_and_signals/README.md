# 0x05. Processes and Signals
---
## Resources
---
* [Linux PID](http://www.linfo.org/pid.html)
* [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
* [Linux signal](https://www.educative.io/answers/what-are-linux-signals)
* [Process management in linux](https://www.digitalocean.com/community/tutorials/process-management-in-linux)
---
### man or help
* `ps`
* `pgrep`
* `pkill`
* `kill`
* `exit`
* `trap`
---
## Learning objectives
---
* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored
---
##Tasks
---
### Task 0
* Write a Bash script that displays its own PID.

### Task 1
* Write a Bash script that displays a list of currently running processes.
* Requirements:
	* Must show all processes, for all users, including those which might not have a TTY
	* Display in a user-oriented format
	* Show process hierarchy

### Task 2
* Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
* Requirements:
	* You cannot use `pgrep`
	* The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error [here](https://github.com/koalaman/shellcheck/wiki/Ignore))

### Task 3
* Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash.`
* Requirement:
	* You cannot use `ps`

### Task 4
* Write a Bash script that displays `To infinity and beyond` indefinitely.
* Requirements:
	* In between each iteration of the loop, add a `sleep 2`

### Task 5
* Write a Bash script that stops [4-to_infinity_and_beyond](https://github.com/maiyo008/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/4-to_infinity_and_beyond) process.
* Requirements
	* You must use kill

### Task 6
* Write a Bash script that stops `4-to_infinity_and_beyond` process.
* Requirements:
	* You cannot use `kill` or `killall`

### Task 7
* Write a Bash script that displays:
	* `To infinity and beyond` indefinitely
	* With a `sleep 2` in between each iteration
	* `I am invicible!!!` when receiving a `SIGTERM` signal
* Make a copy of your `6-stop_me_if_you_can script`, name it `67-stop_me_if_you_can`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond one.`


