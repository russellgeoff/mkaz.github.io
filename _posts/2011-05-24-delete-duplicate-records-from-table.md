---
id: 658
title: Delete Duplicate Records from Table
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=658
permalink: /2011/05/24/delete-duplicate-records-from-table/
categories:
  - solutions log
tags:
  - mysql
---
<pre><code class="sql">DELETE from table1
    USING table1, table1 as vtable
WHERE (table1.ID &gt; vtable.ID)
   AND (table1.field_name = vtable.field_name)
</code></pre>