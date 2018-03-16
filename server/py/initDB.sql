DROP TABLE if EXISTS eeg_raw;
DROP TABLE if EXISTS eeg_avg;
DROP TABLE if EXISTS eeg_repeattime;
DROP TABLE if EXISTS ptrial;
DROP TABLE if EXISTS tperson;
DROP TABLE if EXISTS lost_pair;
DROP TABLE if exists ptime;

CREATE TABLE eeg_raw (
time int(10) NOT NULL,
theta float(10) DEFAULT NULL,
alpha float(10) DEFAULT NULL,
low_beta float(10) DEFAULT NULL,
high_beta float(10) DEFAULT NULL,
gamma float(10) DEFAULT NULL,
trials int(10) NOT NULL,
person char(20) default null
);

create table eeg_avg (
time int(10) NOT NULL,
theta float(10) DEFAULT NULL,
alpha float(10) DEFAULT NULL,
low_beta float(10) DEFAULT NULL,
high_beta float(10) DEFAULT NULL,
gamma float(10) DEFAULT NULL,
person char(20) default null
);

create table eeg_repeatTime (
time int(10) NOT NULL,
theta float(10) DEFAULT NULL,
alpha float(10) DEFAULT NULL,
low_beta float(10) DEFAULT NULL,
high_beta float(10) DEFAULT NULL,
gamma float(10) DEFAULT NULL,
trials int(10) NOT NULL,
person char(20) default null
);

create table lost_pair(
time int(10) NOT NULL,
person char(20) default null,
trials int(10) NOT NULL
);
create table tperson(
trials int(10) NOT NULL,
person char(20) default null
);
create table ptime(
person char(20) default null,
time int(10) NOT NULL
);
