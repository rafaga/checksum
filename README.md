# checksum
An utility to quick compare shasum output files from directories

## Dependencies

 * python 3
 * argparse library

### Generating SHASUM files

First you need to create 2 shasum files with different directories, if you don't know how, you can do it with this bash script:

```Bash
find {directory} -type f -exec shasum -a 256 {} \; > {output_file}
```

This command will generate a file using the algorithm SHA256 to compute recursively each file in the specified directory

### How to use this tool 

before you can use this tool you need to modify two variables in `checksum.py` named `token1` and `token2` with the directory name used in each file to compute the hashes

```Bash
python3 checksum.py --prod={file1} --resp={file2} --out={output_file}
```

Running this command will generate an output file comparing both files named resultados.txt, opening this file will give information about which files are diferent or missing in one file or another.

```
[-1-] = the file is only present in file1
[-2-] = the file is only present in file2
[=/=] = the file is present in both files but the content in both files are different.
```
### Parameters

```
	--file1 : Specify the first SHASUM filename to compare
	--file2 : Specify the second SHASUM filename to compare
	--out  : Specify a custom output filename
```

### TO-DO

 * Remove the requeriment to edit `token1` and `token2` variables.
 * Transate all the commentaries in Spanich to English.
 * Improve the speed of the tool.