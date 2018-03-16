/*
after 
change the user name 
run the script 4 times
*/

load data local infile "C:\\Users\\Angela Yang\\Desktop\\data_eeg\\all\\Jingwei_6.csv" 
	into table eeg_raw
	columns terminated by ','
    lines terminated by '\n'
    ignore 1 lines
    set person = "Jingwei", trials = 10;
 load data local infile "C:\\Users\\Angela Yang\\Desktop\\data_eeg\\all\\Jingwei_5.csv" 
	into table eeg_raw
	columns terminated by ','
    lines terminated by '\n'
    ignore 1 lines
    set person = "Jingwei", trials = 11;  
load data local infile "C:\\Users\\Angela Yang\\Desktop\\data_eeg\\all\\Jingwei_4.csv" 
	into table eeg_raw
	columns terminated by ','
    lines terminated by '\n'
    ignore 1 lines
    set person = "Jingwei",trials = 12;

load data local infile "C:\\Users\\Angela Yang\\Desktop\\data_eeg\\all\\Jingwei_2.csv" 
	into table eeg_raw
	columns terminated by ','
    lines terminated by '\n'
    ignore 1 lines
    set person = "Jingwei",trials = 13;
load data local infile "C:\\Users\\Angela Yang\\Desktop\\data_eeg\\all\\Jingwei_1.csv" 
	into table eeg_raw
	columns terminated by ','
    lines terminated by '\n'
    ignore 1 lines
    set person = "Jingwei", trials = 14;
load data local infile "C:\\Users\\Angela Yang\\Desktop\\data_eeg\\all\\Jingwei_0.csv" 
	into table eeg_raw
	columns terminated by ','
    lines terminated by '\n'
    ignore 1 lines
    set person = "Jingwei", trials = 15;

load data local infile "C:\\Users\\Angela Yang\\Desktop\\data_eeg\\all\\Jingwei_3.csv" 
	into table eeg_raw
	columns terminated by ','
    lines terminated by '\n'
    ignore 1 lines
    set person = "Jingwei", trials = 16;    