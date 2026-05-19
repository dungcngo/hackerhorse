## Sudo permissions
`sudo -l`: This command specifies which commands the current user is allowed to run as `root` without entering a password (or using the user's own password).

## SUID/SGID Files
SUID is a special flag assigned to an executable file. When a regular user runs this file, it is executed with the privileges of the file owner (usually `root`). 
`find / -perm -4000 -type f 2>/dev/null`: Compare the found list of SUID files with `GTFOBins`

## Cron Jobs
`Cron jobs` are tasks that run in the background periodically according to the system's schedule (usually run with `root` privileges).
`cat /etc/crontab` or `ls -la /etc/cron*`: 
- Check if there are any script files that run as `root` and user has write permissions. If so, simply modify that file and insert malicious code.
- Check for `Wildcard Injection` errors (if the cron job uses `*` indiscriminately).

## Processes (Check for background processes)
`ps aux | grep root`: Use `pspy` (a real-time process monitoring tool that doesn't require `root` privileges) to see if any background processes are running back and forth.

## Sensitive Files
`cat ~/.bash_history` or `cat ~/.nano_history`: The admin may have accidentally typed the password directly into the command line.

Scan directories like `/var/www/html` to find the file containing the database connection password (usually the same password as `root`).

Check the `/root/` directory to see if it's readable (usually it isn't), or look for backup files (`.bak`, `.conf`) in the system.

## Linux capabilities
`/usr/sbin/getcap -r / 2>/dev/null`: Search for all system-wide files that contain "Linux capabilities" (special permissions granted specifically to an executable file, rather than requiring full `root` privileges).
