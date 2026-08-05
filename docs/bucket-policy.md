# S3 Bucket Policies

## Overview

This document demonstrates how to configure and apply an Amazon S3 bucket policy using the AWS CLI against a local S3-compatible environment.

Bucket policies are JSON-based resource policies that define which principals can access a bucket and what actions they are permitted or denied to perform.

---

## Objective

The goal of this exercise was to:

* Create a bucket policy in JSON format.
* Apply the policy to an S3 bucket.
* Verify that the policy was successfully stored.
* Understand how bucket policies control access to S3 resources.

---

## Policy Used

The policy consists of two statements:

### Public Read Access

Allows any principal to retrieve objects from the `processed-data` bucket.

Allowed action:

* `s3:GetObject`

Resource:

```
arn:aws:s3:::processed-data/*
```

---

### Restricted Write Access

Denies write operations to every principal except the `writer` IAM user.

Restricted actions:

* `s3:PutObject`
* `s3:DeleteObject`

Resource:

```
arn:aws:s3:::processed-data/*
```

---

## Applying the Policy

The bucket policy was applied using the AWS CLI:

```bash
aws s3api put-bucket-policy \
  --bucket processed-data \
  --policy file://policies/bucket-policy.json
```

---

## Verifying the Policy

The applied policy was retrieved to confirm it was successfully stored.

```bash
aws s3api get-bucket-policy \
  --bucket processed-data
```

Successful execution returned the JSON policy associated with the bucket.

---

## Key Concepts

### Bucket Policies

A bucket policy is a resource-based policy attached directly to an S3 bucket.

It specifies:

* Who can access the bucket.
* Which actions are allowed or denied.
* Which objects or resources are affected.

---

### Resource-Based Access Control

Unlike IAM policies, which are attached to users, groups, or roles, bucket policies are attached directly to the bucket itself.

This allows bucket owners to control access independently of individual IAM identities.

---

### Explicit Deny

An explicit **Deny** always takes precedence over an **Allow**.

Even if another policy grants permission, an explicit deny prevents the requested action.

This behavior is a fundamental principle of AWS authorization.

---

## Skills Practiced

* Creating S3 bucket policies
* Writing JSON policy documents
* Applying policies with the AWS CLI
* Verifying bucket configuration
* Understanding resource-based access control

---

## Summary

This exercise introduced bucket-level authorization for Amazon S3.

By creating and applying a bucket policy, I practiced defining access rules, granting read permissions, restricting write operations, and verifying policy configuration using the AWS CLI. These concepts form an important part of securing object storage in cloud environments.
