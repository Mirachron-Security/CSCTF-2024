# Lite
Author: [Marin Radu](https://github.com/ChronosPK)

<br>

## Description
```
Open the SQLite database file to find the flag.
```

<br>

## Requirements
- `sqlitebrowser` or `sqlite3`

<br>

## Solve
Open the provided database file with SQLite tools and extract the flag.

```bash
sqlite3 mydatabase.db
```

Interact with the database:
```sql
.tables
PRAGMA table_info(users);
SELECT * FROM users WHERE password LIKE '%CSCTF%';
```

Retrieve the flag:
```sql
SELECT * FROM users WHERE password LIKE '%CSCTF%';
```

<br>

> Flag: `CSCTF{r3@d1ng_DAt@b2seS}`