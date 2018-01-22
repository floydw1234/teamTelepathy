DROP TABLE if EXISTS `eeg_raw`;
CREATE TABLE `eeg_raw` (
`person` char(20) default null,
`time` int(10) NOT NULL,
`theta` float(10) DEFAULT NULL,
`alpha` float(10) DEFAULT NULL,
`low_beta` float(10) DEFAULT NULL,
`high_beta` float(10) DEFAULT NULL,
`gamma` float(10) DEFAULT NULL
);
