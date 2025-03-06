# Filtering FASTQ Reads by Barcodes

## Description

This script filters FASTQ.gz files based on a list of valid barcodes. Only reads containing a valid barcode will be retained.

## Prerequisites

- Python 3
- Standard Python libraries (no additional installation required)

## Installation

Clone this repository and navigate to the directory:

```bash
git clone https://github.com/maximelepetit/fastq_filter_by_barcode.git
cd fastq_filter_by_barcode
```
## Usage 

```bash
python3 filter_fastq_barcodes.py \\
    /path/to/input_R1.fastq.gz \\
    /path/to/input_R2.fastq.gz \\
    /path/to/barcodes.txt \\
    /path/to/output \\
    filtered_R1.fastq.gz \\
    filtered_R2.fastq.gz \\
    --barcode_length 10
```

## Arguments

* R1_input.fastq.gz: Input FASTQ.gz file containing R1 reads.
* R2_input.fastq.gz: Input FASTQ.gz file containing R2 reads.
* barcode_list.txt: Text file containing valid barcodes (one per line).
* output_directory: Directory where the filtered files will be saved.
* filtered_R1.fastq.gz: Output file name for filtered R1 reads.
* filtered_R2.fastq.gz: Output file name for filtered R2 reads.
* --barcode_length: Length of the barcodes to extract and compare.

## Author

Developed by Maxime LEPETIT

## Licence

This project is licensed under the MIT License. See the LICENSE file for details.


