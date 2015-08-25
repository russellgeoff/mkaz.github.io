---
id: 658
title: Delete Duplicate Records from Table
author: Marcus Kazmierczak
layout: post
permalink: /2011/05/24/delete-duplicate-records-from-table/
categories:
  - solutions log
tags:
  - mysql
---

A query to delete duplicate records out of a table.


```sql
DELETE from table1
    USING table1, table1 as vtable
WHERE (table1.ID > vtable.ID)
   AND (table1.field_name = vtable.field_name)
```
