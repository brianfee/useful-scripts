# useful-scripts

## PDF-Protect
### Requirements
- bash
- pdftk
- python (for protect-list.py)

### Purpose
- Creates a protected copy of a pdf. protect-list.py can also password protect a list of files from a csv.

### Usage
<pre>
pdf-protect.sh [-v] [-a <i>append</i>] [-o <i>output</i>] [-p <i>password</i>] <i>file_name</i>
</pre>

<pre>
protect-list.py <i>list_file_name</i>
</pre>

**pdf-protect.sh switches**
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


## merge-csvs.py
### Requirements
- python3
  - pandas

### Purpose
- Merge two csvs based on a common column name and save to a new file *merged.csv*

### Usage
<pre>
merge-csvs.py <i>file1 file2 common_column</i>
</pre>
