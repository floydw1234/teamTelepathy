DROP TABLE if EXISTS eeg_avg;
create table eeg_avg (
time int(10) NOT NULL,
theta float(10) DEFAULT NULL,
alpha float(10) DEFAULT NULL,
low_beta float(10) DEFAULT NULL,
high_beta float(10) DEFAULT NULL,
gamma float(10) DEFAULT NULL,
person char(20) default null
);
/*
insert into eeg_raw
select round(time/100),avg(theta),avg(alpha),avg(low_beta),avg(high_beta),avg(gamma), trials, person
from eeg_repeattime
group by round(time/100),trails,person;
*/

insert into eeg_avg
select time, avg(theta),avg(alpha),avg(low_beta),avg(high_beta),avg(gamma), person
from eeg_repeattime
where trials<10
group by person, time;
/*
select p.time,p.person,t.trials
from ptime as p, tperson as t
where p.person = t.person and not exists
	(select *
    from eeg_raw as e
    where e.time = p.time and e.person = p.person and t.trials = e.trials);

insert into tperson
select distinct trials,person
from eeg_raw;

insert into ptime
select distinct person,time
from eeg_avg;
*/


/*
insert into lost_pair
select p.time, p.person,t.trials
from tperson as p, ptrial as t
where p.person = t.person and 
not exists	(
	select person, trials, time
    from eeg_raw as r
    where r.person = p.person and r.trials = t.trials and r.time = p.time
	);
*/
/*
insert into eeg_raw
select l.time, e.theta, e.alpha, e.low_beta,e.high_beta,e.gamma,l.trials,l.person
from lost_pair as l, eeg_raw as e
where l.time = e.time+1 and l.trials = e.trials and l.person = e.person;
*/