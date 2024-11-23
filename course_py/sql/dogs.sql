
create table dogs as
select 'abraham' as name, 'long' as fur union
select 'barack', 'short' union
select 'clinton', 'long' union
select 'delano', 'long' union
select 'eisenhower', 'short' union
select 'fillmore', 'curly' union
select 'grover', 'short' union
select 'herbert', 'curly';

create table parents as
select 'abraham' as parent, 'barack' as child union
select 'abraham', 'clinton' union
select 'delano', 'herbert' union
select 'fillmore', 'abraham' union
select 'fillmore', 'delano' union
select 'fillmore', 'grover' union
select 'eisenhower', 'fillmore';

create table grandparents as
select a.parent as grandog, b.child as grandpup
from parents as a, parents as b
where a.child = b.parent;

select grandog from
grandparents, dogs as c, dogs as d
where c.fur = d.fur and
c.name = grandog and
d.name = grandpup;
