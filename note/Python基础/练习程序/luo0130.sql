作业:

create database eshop
  default charset=utf8;

create table orders
  (order_id varchar(32),cust_id varchar(32),
    order_date datetime,status enum('1','2','3','4','5','6','9'),
    products_num int,amt decimal(10,2))default charset=utf8;

insert into orders values
    ('2019013001','C001',now(),'1',2,28.6),
    ('2019013002','C006',now(),'2',3,62.56),
    ('2019013003','C011',now(),'5',1,12.5),
    ('2019013004','C001',now(),'6',1,22.54),
    ('2019013005','C051',now(),'3',2,42);

select * from orders where status='1';
select * from orders where status='3' or status='4'or status='5';
select order_id from orders where cust_id='C006' and status='2';
select order_date,status from orders where order_id='2019013005';
select * from orders where cust_id='C001' order by order_date desc;
select status '状态',count(*) from orders group by status;
select max(amt),min(amt),avg(amt),sum(amt) from orders;
select order_id,amt from orders order by amt desc limit 3;
updata orders set status=4 where order_id='2019013005';
delete from orders where status=9;

