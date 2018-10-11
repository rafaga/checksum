# checksum
An utility to quick compare shasum output files from directories

## Dependencies

 * Python >= 3.2

### Generating SHASUM files

First you need to create 2 shasum files with different directories, if you don't know how, you can do it with this bash script:

```Bash
find {directory} -type f -exec shasum -a 256 {} \; > {output_file}
```

This command will generate a file using the algorithm SHA256 to compute recursively each file in the specified directory

### How to use this tool 

Syntax

```Bash
python3 checksum.py --prod={file1} --resp={file2} --prefix1={prefix_from_file1} --prefix2={prefix_from_file2} --out={output_file}
```

Running this command will generate an output file comparing both files named `results.txt`, opening this file will give information about which files are diferent or missing in one file or another.

The output files describes only the differences, and use a nomenclature to define what kind of difference has been detected.

```
[-1-] = the file is only present in file1
[-2-] = the file is only present in file2
[=/=] = the file is present in both files, but the content is different.
```
### Parameters

```
	--file1 : Specify the first SHASUM filename to compare
	--file2 : Specify the second SHASUM filename to compare
	--prefix1 : the directory prefix used to compare files structures in file1
	--prefix2 : the directory prefix used to compare files structures in file2
	--out : Specify a custom output filename (Optional)
```

### TO-DO

 * Improve the speed of the tool.
