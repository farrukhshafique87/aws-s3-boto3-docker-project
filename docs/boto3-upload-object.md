# Upload Objects with boto3

## Overview

This document demonstrates how to upload objects to an Amazon S3 bucket using the **boto3** SDK.

Uploading objects is one of the most common operations when working with object storage. In this example, CSV data is uploaded using the `put_object()` API.

---

## Objective

The objectives of this exercise are to:

* Connect to Amazon S3 using boto3
* Upload an object to an existing bucket
* Organize objects using key prefixes
* Specify the appropriate content type

---

## Prerequisites

* An existing S3 bucket
* Python 3.9+
* boto3
* python-dotenv
* Docker and Docker Compose

---

## Implementation

The script:

1. Loads environment variables.
2. Creates an S3 client.
3. Uploads sample CSV data using `put_object()`.
4. Stores the object under the key:

```text
sales/2024/01/data.csv
```

Run the script with:

```bash
python3 src/upload_file.py
```

---

## Object Organization

Objects are organized using key prefixes.

Example:

```text
raw-data/
└── sales/
    └── 2024/
        └── 01/
            └── data.csv
```

Although prefixes resemble folders, Amazon S3 stores objects in a flat namespace.

---

## Key Concepts

### Object Keys

Every object stored in Amazon S3 has a unique key within its bucket.

Example:

```text
sales/2024/01/data.csv
```

---

### Content Type

The uploaded object specifies:

```text
text/csv
```

Providing the correct content type helps applications correctly interpret stored objects.

---

## Skills Practiced

* Uploading objects with boto3
* Using `put_object()`
* Working with object keys
* Organizing data using prefixes
* Setting object metadata

---

## Summary

This exercise demonstrated how to upload structured data into Amazon S3 using boto3. Understanding object uploads and key organization is fundamental to building applications that use cloud object storage.
