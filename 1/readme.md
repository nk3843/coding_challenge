Word, Line, and Byte Counter (WC)
This Python script provides functionality to count the number of words, lines, and bytes in one or more files. The script is implemented using the Typer library, allowing for easy command-line usage.

Usage
To use the script, follow these steps:

Installation: Ensure you have Python installed on your system.

Dependencies: The script uses the Typer library. If you haven't installed it yet, you can install it using pip:

```
pip3 install typer
```

Run the Script: Run the script with Python, passing the necessary arguments and options:
python3 wc.py [OPTIONS] FILENAME...

count_lines_words_bytes: The main command to count lines, words, and bytes.
FILENAME...: List of files to count.
Options
--lines, -l: Print the newline counts.
--words, -w: Print the word counts.
--bytes, -c: Print the byte counts.

You can use it as an executable command
save the script in a new file and add shebang on top to tell the interpreter what to do

```
#!/usr/bin/env python
```

run the following command in terminal

```
chmod +x cwcc
```

Next add path using following command

```
export PATH=$PATH:.
```
