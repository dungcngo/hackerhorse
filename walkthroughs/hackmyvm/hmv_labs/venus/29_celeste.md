# 0x29
This write-up explains the steps taken to complete mission 0x29, starting from user `celeste` and escalating to `nina`.

## Mission
As always, read the objective:
```bash
celeste@venus:~$ cat mission.txt 
################
# MISSION 0x29 #
################

## EN ##
The user celeste has access to mysql but for what?
```

## Method of solving
We checked the home directory and, seeing no other leads, we logged into the local MySQL (MariaDB) instance using the credentials provided in the mission hint.
```bash
celeste@venus:~$ mysql -u celeste -p
```
Once inside the database monitor, we explored the avaiable data. We found a database named `venus` containing a table called `people`.
```bash
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 1507
Server version: 10.11.6-MariaDB-0+deb12u1 Debian 12

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| venus              |
+--------------------+
2 rows in set (0.008 sec)

MariaDB [(none)]> use venus;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [venus]> show tables;
+-----------------+
| Tables_in_venus |
+-----------------+
| people          |
+-----------------+
1 row in set (0.001 sec)
```
We queried the `people` table to see if it contained any credentials. The table listed several users and their associated "pazz" (passwords).
```bash
MariaDB [venus]> select * from people;
+-----------+---------------+--------------------------------+
| id_people | uzer          | pazz                           |
+-----------+---------------+--------------------------------+
|         1 | nuna          | ixpfdsvcxeqdW                  |
|         2 | nona          | ixpvcxvcxeqdW                  |
|         3 | manue         | ixpfdsfdseqdW                  |
|         4 | samoa         | ixperrewrweqdW                 |
|         5 | dsaewq        | ixpefdsfsqdW                   |
|         6 | fdsfewrew     | ixpedvcxv4qdW                  |
|         7 | koiuoiudsadas | ixpredsfdeqdW                  |
|         8 | vcxfdsfew     | ixp342432eqdW                  |
|         9 | dasd          | ixpeiuyiuyqdW                  |
|      .....| .....         | ................               |
|        74 | nina          | ixpeqdWuvC5N9kG                |
|        75 | nunu          | ixpeSFDSFDSVCXqdW              |
|        76 | fdse          | ixpeDFSWEF2qdW                 |
|        77 | dsar          | ixpeF43F3F34qdW                |
|        78 | yop           | ixpeqdWCSDFDSFD                |
|        79 | loco          | ixpeF43F34F3qdW                |
|        80 | zaza          | ixpeYUTHNYGTHYTqdW             |
|        81 | jhon          | ixpeFDSJYTUJTYqdW              |
|        82 | tell          | ixpeHYTTqdW                    |
|        83 | ma            | uyixptje4FSFWEFqdW             |
|        84 | mum           | jghixpeqdW                     |
|        85 | nanaa         | 432432ixpeqdW                  |
|        86 | nnnniinn      | irewxpeqdW                     |
|        87 | iourewoiure   | rewixpeqdW                     |
|        88 | lkjfdsoiu     | dsaixpeqdW                     |
|        89 | vcxnoj        | dasdasixpeqdW                  |
|        90 | ioyuwer       | ixpeqdvcxvcxW                  |
|        91 | kaka          | ixpeqdW                        |
|        92 | nini          | ixpeqdvcxW                     |
|        93 | zong          | ixpeqdWfdsfsdf                 |
|        94 | nana          | ixpefdsafdsqdW                 |
|        95 | ninna         | ixpeqOPUIFDSFDSdW              |
+-----------+---------------+--------------------------------+
95 rows in set (0.014 sec)
```
With the password retrieved of user `nina` from the database, logged in and verify it, get the flag.
```bash
celeste@venus:~$ su - nina
Password: 
nina@venus:~$ id ; whoami
uid=1030(nina) gid=1030(nina) groups=1030(nina)
nina
```

## Key command
`mysql -u celeste -p`

`show databases` 

`use XXX`

`show tables`

`select * from YYY`

***You are welcome!***
