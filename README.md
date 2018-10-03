# checksum
An utility to quick compare shasum output files from directories

## Dependencies

	* python 3
		* argparse library

### Generating SHASUM files

First you need to create 2 shasum files with different directories, if you don't know how. you can do it with:

```Bash
find {directory} -type f -exec shasum -a 256 {} \; > {output_file}
```

This command will generate a file using the algorithm SHA256 to compute recursively each file in the specified directory

### How to use this tool 

```Bash
python3 checksum.py --prod={file1} --resp={file2} --out={output_file}
```

Parameters

```
	--prod : Specify the first SHASUM filename to compare
	--resp : Specify the second SHASUM filename to compare
	--out  : Specify a custom output filename
```

