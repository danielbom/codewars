-- https://www.codewars.com/kata/sql-padding-encryption/train/sql
-- My solution
select rpad(md5, char_length(sha256), '1') as md5,
  lpad(sha1, char_length(sha256), '0')  as sha1,
  sha256
from encryption

-- ...
SELECT 
  CONCAT(md5, REPEAT('1', (LENGTH(sha256) - LENGTH(md5)))) as md5,
  CONCAT(REPEAT('0', (LENGTH(sha256) - LENGTH(sha1))), sha1) as sha1,
  sha256
FROM encryption