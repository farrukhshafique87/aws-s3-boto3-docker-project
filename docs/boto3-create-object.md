# Create an S3 Bucket with boto3

## Overview

This document demonstrates how to create an Amazon S3 bucket using the **boto3** SDK.

Creating a bucket is typically the first step before storing and organizing objects in Amazon S3. This example connects to an S3-compatible endpoint, creates a bucket, and provides basic error handling.

---

## Objective

The objectives of this exercise are to:

* Configure a boto3 S3 client
* Connect using environment variables
* Create an S3 bucket
* Handle common exceptions during bucket creation

---

## Prerequisites

* Python 3.9+
* boto3
* python-dotenv
* AWS CLI configured
* Docker and Docker Compose

---

## Implementation

The script:

1. Loads configuration from environment variables.
2. Creates an S3 client using boto3.
3. Attempts to create the `raw-data` bucket.
4. Displays a success or error message.

Run the script with:

```bash
python3 src/create_bucket.py
```

---

## Key Concepts

### S3 Bucket

An S3 bucket is the top-level container used to store objects.

Before an object can be uploaded, it must belong to a bucket.

---

### boto3 Client

The boto3 S3 client provides programmatic access to Amazon S3 operations such as:

* Create buckets
* Upload objects
* Download objects
* List objects
* Delete objects
* Manage bucket policies

---

### Environment Configuration

Connection settings are loaded from environment variables rather than being hardcoded into the application.

This approach improves portability and keeps configuration separate from application logic.

---

## Skills Practiced

* Creating an S3 client with boto3
* Creating S3 buckets
* Environment-based configuration
* Basic exception handling

---

## Summary

This exercise introduced the foundational step of working with Amazon S3 using Python. Successfully creating a bucket provides the starting point for storing, organizing, and managing objects through the boto3 SDK.
