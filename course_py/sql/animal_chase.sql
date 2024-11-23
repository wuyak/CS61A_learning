create table nouns as
select 'dog' as phrase union
select 'cat' union
select 'bird';

create table ands as
select first.phrase || ' and ' || second.phrase as phrase
from nouns as first, nouns as second
where first.phrase <> second.phrase;

select subject.phrase || ' chased ' || object.phrase
from ands as subject, ands as object
where subject.phrase <> object.phrase;
