Dynamo DB
===
- NoSQL database service that provides fast and predictable performance with seamless scalability.
- Offers **encyrption at rest**
- You can create database tables that can store and retrieve any amount of data, and serve any level of request traffic
- You can **scale up or scale down your tables' throughput capacity without downtime or performance degradation**, and use the AWS Management Console to monitor resource utilization and performance metrics.
- Provides on-demand backup capability as well as enable **point-in-time recovery** for your DynamoDB tables. With point-in-time recovery, you can restore that table to any point in time during the __last 35 days__.
- All of your data is stored in partitions, backed by solid state disks (SSDs) and **automatically replicated across multiple AZs in an AWS region**, providing built-in high availablity and data durability.
- You can create **tables that are automatically replicated across two or more AWS Regions, with full support for multi-master writes.**

## Core Components
- __Table__: a collection of items
    - DynamoDB stores data in a table, which is a collection of data
    - Are schemaless
    - initial limit of **256 tables per region**
- __Items__: a collection of attributes
    - DynamoDB uses __primary keys__ to uniquely identify each item in a table and __secondary indexes__ to provide more querying flexibility
    - Each table contains zero or more items
- __Attribute__: a fundamental data element
    - DynamoDB supports nested attributes **up to 32 levels deep**.
- __Primary Key__: uniquely identifies each item in the table, so that no two items can have the same key. Must be scalar
    - __Partition key__: a simple primary key, composed of one attribute
    - __Partition key and short key__ (_composite primary key_): composed of two attributes
    - DynamoDB uses the partition key value as input to an internal hash function. The output from the hash function determines the partition in which the item will be stored. All items with the same partition key are stored together, in sorted order by sort key value. If no sort key is used, no two items can have the same partition key value.
- __Secondary Indexes__: lets you query the data in the table using an alternate key, in addition to queries against the primary key.
    - You can create one or more secondary indexes on a table.
    - Two kinds of indexes:
        - __Global secondary index (GSI)__: An index with a partition key and sort key that can be differnt from those on the table
        - __Local secondary index (LSI)__: An index that has the same partition key as the table, but a different sort key
    - You can define up to 5 global secondary indexes and 5 local secondary indexes per table.
- __DynamoDB Streams__: an optional feature that captures data modification events in DynamoDB tables
    - The naming convention for DynamoDB Streams endpoints is _streams.dynamodb..amazonaws.com_
    - Each event is represented by a _stream record_, and captures the following events:
        - A new item is added to the table: captures an image of the entire item, including all of its attributes.
        - An item is updated: captures the "before" and "after" image of any attributes that were modified in the item.
        - An item is deleted from the table: captures an image of the entire item before it was deleted.
    - Each stream record also contains the name of the table, the event timestamp, and other metadata
    - Stream records are organized into groups, or __shards__. Each shard acts as a container for multiple stream records, and contains information required for accessing and iterating through these records.
    - Stream records have a **lifetime of 24 hours**; after that, they are automatically removed from the stream.
    - You can use **DynamoDB Streams together with AWS Lambda to create a _trigger_**, which is a code that executes automatically whenever an event of interest appears in a stream.
    - DynamoDB Streams enables powerful solutions such as **data replication within and across Regions**, **materialized views of data in DynamoDB tables**, **data analysis using Kinesis materialized views**, and much more.
![dynamodb_streams](./images/dynamodb_streams.png)

## Data Types for Attributes
- __Scalar Types__
    - A scalar type can represent exaclty one value. 
    - The scalar types are number, string, binary, Boolean, and null.
    - Primary keys should be scalar types.
- __Document Types__
    - A document type can represent a complex structure with nested attributes.
    - such as you would find in a JSON document. 
    - The document types are list and map.
- __Set Types__
    - A set type can represent multiple scalar values.
    - The set types are string set, number set, and binary set.

## Throughput Management
- DynamoDB **auto scaling**
    - Define a range (upper and lower limits) for __read and write capacity units__, and define a target utilization percentage within that range.
    - A table or a global secondary index can increase its __provisioned read and write capacity__ to handle sudden increases in traffic, without request throttling.
    - DynamoDB auto scaling can decrease the throughput when the workload decreases so that you don't pay for unused provisioned capacity.
- **Provisioned throughput**
    - manually defined maximum amount of capacity that an application can consume from a table or index. If your application exceeds your provisioned throughput settings, **it is subject to request throttling**.
- **Reserved capacity**
    - with reserved capacity, you pay a **one-time upfront fee** and commit to a **minimum usage level** over a period of time, for cost-saving solutions.

## Throttling
- _Throttling_ prevents your application form consuming too many capacity units. DynamoDB can throttle read or write requests that exceed the throughput settings for a table, and can also throttle read requests exceeds for an index
- When a request is throttled, it fails with an __HTTP 400__ code (Bad Request) and a `provisionedThroughputExceededException`

## Other Notes
- When you read data from a DynamoDB table, the response might not reflect the results of a recently completed write operation. The response might include some stale data, but you should __eventually have consistent reads__.
- When you request a __strongly consistent read__, DynamoDB returns a response with the most up-to-date data, reflecting the updates from all prior write operations that were successful. A stongly consistent read might not be available if there is a network delay or outage.
- DynamoDB **does not support stongly consistent reads across AWS regions**
- When you create a table or index in DynamoDB, **you must specify your throughput capacity requirements for read and write activity** in terms of:
    - One __read capacity unit__ represents one stongly consistent read per second, or two eventually consistent reads per second, for an item **up to 4 KB in size**. If you need to read an item that is larger than 4 KB, DynamoDB will need to consume additional read capacity units.
    - One __write capacity unit__ represents one write per second for an item **up to 1 KB in size**. If you need to write an item that is larger than 1 KB, DynamoDB will need to consume additional write capacity units.