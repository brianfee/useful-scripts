# useful-scripts

## PDF-Protect
### Requirements
- bash
- pdftk

### Purpose
- Creates a protected copy of a pdf.

### Usage
<pre>
pdf-protect.sh [-v] [-a <i>append</i>] [-o <i>output</i>] [-p <i>password</i>] <i>file_name</i>
</pre>

**Switches**
- -v: Verbose
- -a: Text to append at end of file name (before .pdf extension) Default: *(Protected)*
- -o: Specify output file
- -p: Specify password


## lscsv.sh
### Requirements
- bash
- python

### Purpose
- Export a list of files in current directory to a file. Default: *filelist.csv*

### Usage
<pre>
lscsv.sh [-v] [-d NUM] <i>[PATH...]</i>
</pre>

**Switches**  
- -v: Verbose
- -d: Depth

