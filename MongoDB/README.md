# MongoDB Learning Roadmap

This README is a structured learning roadmap for MongoDB — topics, subtopics, exercises and resources to help you progress from beginner to intermediate/advanced.

## Quick start (what to learn first)
- What is MongoDB? Documents, collections, databases
- BSON vs JSON
- Install and run: mongosh, MongoDB Atlas overview
- Connect from your app (URI format) — do NOT hardcode credentials; use env vars/secret manager

## Core data model and CRUD
- Documents and collections
- Creating documents: `insertOne`, `insertMany`
- Reading documents: `find`, `findOne`, projections
- Updating documents: `updateOne`, `updateMany`, `replaceOne`, `$set`, `$inc`, upserts
- Deleting documents: `deleteOne`, `deleteMany`

## Indexing
- Types of indexes: single-field, compound, multikey, text, hashed
- Index creation and options (`unique`, `sparse`, `expireAfterSeconds`)
- Index usage and query planning (`explain()`)
- When not to index (write-heavy workloads)

## Aggregation framework
- Aggregation pipeline basics: stages (`$match`, `$group`, `$project`, `$sort`, `$limit`, `$unwind`, `$lookup`)
- Performance tips for aggregation
- Faceted searches and multi-stage pipelines

## Data modeling and schema design
- Schema design patterns: embedded documents vs references
- One-to-many and many-to-many patterns
- Bucket pattern, pre-aggregation, time-series considerations
- Modeling for updates, reads, and shard keys

## Transactions and concurrency
- Multi-document transactions (when and how to use)
- Read/write concerns and isolation
- Optimistic concurrency patterns

## Replication and high availability
- Replica sets: primary/secondary, election, write concern
- Failover behavior and recovery
- Backups and point-in-time recovery

## Sharding and scaling horizontally
- Sharding concepts: shard key, chunks, balancer
- Choosing a shard key and anti-patterns
- Resharding and migrating data

## Security best practices
- Authentication mechanisms (SCRAM, x.509)
- Authorization and roles (least privilege)
- Network security: IP allowlist, VPC peering, private endpoints
- TLS/SSL, encrypting data at rest (Atlas encryption)
- Secrets management (do not commit credentials)

## Administration & operations
- Monitoring (Atlas monitoring, MMS, Cloud Manager, Prometheus/Grafana)
- Logs and audit logging
- Backup & restore (mongodump/mongorestore, Atlas snapshots)
- Upgrades and maintenance windows

## Drivers & integrations
- Official drivers: Python (`pymongo`), Node.js (`mongodb`, `mongoose`), Java, Go
- ODM/ORM alternatives (Mongoose for Node.js)
- Using MongoDB with frameworks (FastAPI, Flask, Express)

## Tools and GUI
- mongosh (shell) — basic commands and scripting
- MongoDB Compass — GUI for schema, visual explain
- MongoDB CLI and Tools: `mongodump`, `mongorestore`, `mongoimport`, `mongoexport`

## Performance tuning
- Schema and index-driven performance
- Use of `explain()` and slow query logs
- Working set, memory, and paging
- Connection pooling and driver-level tuning

## Cloud: MongoDB Atlas
- Atlas basics: projects, clusters, database users
- Network access and IP allowlists
- Atlas features: Search, Data Lake, Online Archive, Triggers

## Testing, Local Dev & CI
- Running MongoDB locally with Docker
- In-memory testing patterns and test fixtures
- Test data factories and truncation strategies

## Migration, ETL & change streams
- Change Streams (watching data changes)
- Using `mongodump`/`mongorestore` and `mongoimport`/`mongoexport`
- CDC and integrating with Kafka or other pipelines

## Practical exercises and mini-projects
1. CRUD playground: create a small notes app storing documents with tags and timestamps.
2. Index practice: add indexes to speed up queries and compare `explain()` output.
3. Aggregation challenge: compute monthly reports from a sample orders dataset.
4. Transactions: implement a money transfer simulation requiring atomicity.
5. Sharding simulation: design a shard key for a social feed dataset and explain your choice.

## Cheatsheet: common commands
- Start shell: `mongosh "<connection-string>"`
- Show DBs: `show dbs`
- Switch DB: `use myDatabase`
- Show collections: `show collections`
- Find: `db.collection.find({})`
- Create index: `db.collection.createIndex({field: 1})`

## Learning resources
- Official docs: https://www.mongodb.com/docs/
- MongoDB University (free courses): https://university.mongodb.com/
- Useful books: "MongoDB: The Definitive Guide", "Designing Data-Intensive Applications" (for general patterns)
- Community: Stack Overflow, MongoDB Community Forums

## Next steps & how to use this README
- Work through the core sections first (Quick start → CRUD → Indexing → Aggregation).
- Try the practical exercises; add your solutions under `MongoDB/exercises/` in this repo.
- If you want, I can create starter notebooks or example scripts (Python/Node) for several exercises.

---

If you'd like, I can also add:
- Example Python scripts using `pymongo` for the CRUD and aggregation exercises
- Docker Compose file to run a local replica set for testing transactions
- A short `exercises/` folder with datasets and test cases

Happy learning — tell me which extra artifacts you want me to create next.
