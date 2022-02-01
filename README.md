# ascii-art
Shell-scripts archive for echoing ASCII art in shell.

This takes advantage of Github's CLI to transfer and incorporate ASCII art intto a command-line-only Linux machine.

## echo-ascii
A short python script that converts lines of text into lines to be echoed in a shell script.

Usage:

> ~$ python3 echo-ascii.py <input-file> <output-file>
  
The output file will be overwritten if it already exists and will always be appended by ".sh".
  
## Examples:
Convert text to echo in shell:

> ~$ python3 ascii-art/echo-ascii/echo-ascii.py cilantro.txt cilantro

This will output cilantro.sh in your working directory.

Download the archive:

> -$ git clone https://github.com/hellowhoami/ascii-art.git

Make a script executable:

> ~$ sudo chmod u+x ascii-art/scripts/cilantro.sh

Run a script:

> ~$ ./ascii-art/scripts/cilantro.sh

