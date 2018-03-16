
/*
update eeg_repeattime
set trials = 3
where person = "William" and trials = 5;

update eeg_repeattime
set trials = 4
where person = "William" and trials = 6; 

update eeg_repeattime
set trials = 5
where person = "William" and trials = 7; 

update eeg_repeattime
set trials = 6
where person = "William" and trials = 8; 

update eeg_repeattime
set trials = 7
where person = "William" and trials = 9; 

update eeg_repeattime
set trials = 8
where person = "William" and trials = 10; 

update eeg_repeattime
set trials = 9
where person = "William" and trials = 11; 


select person,trials,count(distinct time)
from eeg_repeattime
where time<20000
group by person,trials;
*/


select person,trials,count(distinct time)
from eeg_repeattime
group by person,trials;
/*
select p.time,p.person,t.trials
from ptime as p, tperson as t,eeg_raw as e
where p.person = t.person and (p.time,p.person,t.trials)
not in (
select time,person,trials
from eeg_raw);
*/
/*
DROP TABLE if EXISTS lost_pair;
create table lost_pair(
time int(10) NOT NULL,
person char(20) default null,
trials int(10) NOT NULL
);*/
/*
select person,trials,count(distinct time)
from eeg_raw
group by person,trials;

select time
from eeg_raw
where person = "William" and trials = 3;*/