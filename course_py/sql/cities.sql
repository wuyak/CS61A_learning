
create table cities as
select 38 as latitude, 122 as longitude, 'Berkeley' as name union
select 42, 71, 'Cambridge' union
select 45, 93, 'Minneapolis' union
select 33, 117, 'San Diego' union
select 26, 80, 'Miami' union
select 90, 0, 'North Pole';

create table cold as
select name from cities where latitude >= 43;

create table distances as
select a.name as first, b.name as second,
60*(b.latitude - a.latitude) as distance
from cities as a, cities as b;

select 'hello,' || ' world';

create table phrase as select 'hello, world' as s;
select substr(s,4,2) || substr(s, instr(s, ' ')+1, 1) from phrase;
