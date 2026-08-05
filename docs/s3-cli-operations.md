# S3 CLI Operations

## Overview

This document records hands-on practice with S3 object storage operations using AWS CLI commands.

The objective was to understand common object storage workflows:

- Uploading objects
- Organizing objects using prefixes
- Listing objects
- Downloading objects
- Synchronizing data locally
- Removing objects

These operations represent common workflows used when managing files, datasets, and application artifacts in object storage environments.

---

## Environment

Tools used:

- AWS CLI v2
- Linux (WSL2 Ubuntu)
- S3-compatible practice environment

---

# 1. Upload Objects

Uploaded CSV sales data files into structured storage paths.

### Upload January sales data

```bash
aws s3 cp january.csv s3://raw-data/sales/2024/01/data.csv
```

Result:

```
upload: ./january.csv to s3://raw-data/sales/2024/01/data.csv
```

### Upload February sales data

```bash
aws s3 cp february.csv s3://raw-data/sales/2024/02/data.csv
```

Result:

```
upload: ./february.csv to s3://raw-data/sales/2024/02/data.csv
```

---

# 2. Create and Upload a Report File

Generated a summary report file:

```bash
echo "processed on $(date)" > summary.txt
```

Uploaded the report:

```bash
aws s3 cp summary.txt s3://processed-data/reports/summary.txt
```

Result:

```
upload: ./summary.txt to s3://processed-data/reports/summary.txt
```

---

# 3. List Objects

## List all objects recursively

Command:

```bash
aws s3 ls s3://raw-data --recursive
```

Example output:

```
2026-08-05 02:23:45        124 sales/2024/01/data.csv
2026-08-05 02:24:35         99 sales/2024/02/data.csv
```

This demonstrates how objects are organized using prefixes.

S3 does not use traditional folders. Instead, paths such as:

```
sales/2024/01/data.csv
```

are object key names that provide a folder-like structure.

---

# 4. List Objects by Prefix

## January data

```bash
aws s3 ls s3://raw-data/sales/2024/01/
```

Output:

```
2026-08-05 02:23:45        124 data.csv
```

## February data

```bash
aws s3 ls s3://raw-data/sales/2024/02/
```

Output:

```
2026-08-05 02:24:35         99 data.csv
```

---

# 5. Download Objects

Downloaded January sales data from storage:

```bash
aws s3 cp s3://raw-data/sales/2024/01/data.csv january-back.csv
```

Result:

```
download: s3://raw-data/sales/2024/01/data.csv to ./january-back.csv
```

Verified downloaded content:

```bash
cat january-back.csv
```

Example output:

```csv
date,region,sales
2024-01-01,us-east,1200.00
2024-01-02,us-east,980.50
2024-01-02,us-west,980.50
2024-01-03,eu-west,1540.00
```

---

# 6. Synchronize Objects

Downloaded all sales data under the 2024 prefix:

```bash
aws s3 sync s3://raw-data/sales/2024/ ./local-sales/
```

Result:

```
download: s3://raw-data/sales/2024/01/data.csv to local-sales/01/data.csv
download: s3://raw-data/sales/2024/02/data.csv to local-sales/02/data.csv
```

The `sync` command compares source and destination and transfers only required changes.

---

# 7. Delete Objects

## Delete a single object

Removed the generated summary report:

```bash
aws s3 rm s3://processed-data/reports/summary.txt
```

Result:

```
delete: s3://processed-data/reports/summary.txt
```

---

## Delete objects recursively

Removed February sales data:

```bash
aws s3 rm s3://raw-data/sales/2024/02 --recursive
```

Result:

```
delete: s3://raw-data/sales/2024/02/data.csv
```

Removed January sales data:

```bash
aws s3 rm s3://raw-data/sales/2024/01 --recursive
```

Result:

```
delete: s3://raw-data/sales/2024/01/data.csv
```

---

# Key Concepts Learned

## Object Storage

S3 stores data as objects consisting of:

- Object key
- Object content
- Metadata

Example:

```
sales/2024/01/data.csv
```

---

## Prefix-Based Organization

Objects can be logically grouped using prefixes:

```
raw-data/
└── sales/
    └── 2024/
        ├── 01/
        │   └── data.csv
        └── 02/
            └── data.csv
```

---

## AWS CLI Skills Practiced

Commands used:

| Command | Purpose |
|---|---|
| `aws s3 cp` | Upload and download objects |
| `aws s3 ls` | List objects |
| `aws s3 sync` | Synchronize directories |
| `aws s3 rm` | Delete objects |

---

# Summary

Completed practical exercises covering fundamental S3 workflows:

✅ Uploading objects  
✅ Organizing data using prefixes  
✅ Listing objects  
✅ Downloading objects  
✅ Synchronizing data  
✅ Deleting objects  

These operations form the foundation for working with object storage in cloud environments.
