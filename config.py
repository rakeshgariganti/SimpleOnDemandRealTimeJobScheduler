
# Scripts to run, Please make sure that the scripts are having proper absolute paths to the executables.
# Scripts can be just commands or the file names with proper shebang lines and executable permissions
# Make sure that the scripts will not run for infinite time.
# One user can run multiple scripts at a time but the output in web pages is shared, so the output of all the running
# scripts will be shown at the same place. So avoid running multiple scripts per a user at a time.


SCRIPTS = [
    "echo 'This is awesome'",
    "./program.py",
    "ping -c 3 localhost",
    "uname -a",
    "whoami",
    "date",
    "ls"
    "last",
    "who",
    "cat /etc/passwd",
    "cd / && python -m SimpleHTTPServer 55555",
    "netstat"
]

