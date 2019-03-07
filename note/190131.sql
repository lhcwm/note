 1,表结构调整:(alter table)
   1,添加字段
    在后面添加字段
    alter table 表名 add 字段名 类型
    在最前面添加字段
    alter table 表名 add 字段名 类型 first
    在指定字段后面添加
    alter table 表名 add 字段名 类型 after 字段名

    示例:
    alter table student add age int;
  2,修改字段
    修改类型
    alter table 表名 modify 字段名 类型(宽度)
    修改名称
    alter table 表名 change 原字段名 新字段名 类型(宽度)
    示例:

  3,删除字段:
    语法:alter table 表名 drop 字段名
    示例:alter table student drop id;

 2,约束:
   1,定义:为保证数据的 正确性,完整性,一致性
       数据必须遵循的规则,
   2,约束类型:
     非空约束:字段的值不能为空
     唯一性约束:字段值唯一
     主键约束:字段作为主键,非空,唯一
     默认值:未填写值时,设置默认值
     自动增加:字段值自动增加
     外键约束:

     1,非空约束:(not null)
       指定字段的值不能为空,如果插入时该字段值为空,则报错,无法插入
       语法:字段名称 数据类型(宽度) not null
       示例:
       create table customer(
       cust_no varchar(32) not null,
       cust_name varchar(64) not null,
       tel_no varchar(32) not null)
       default charset=utf8;

     2,唯一约束:
       该字段的值唯一,不重复
       语法:字段名称 数据类型 unique
       示例:
       create table customer(
        cust_no varchar(32) unique,
       cust_name varchar(64) not null)
       default charset=utf8;

     3,主键:(primary key,简称PK)
       主键用来唯一标识表中的一笔记录,非空唯一
       主键和一比数据有唯一的对应关系
       一个表最多只能有一个主键
       可以单个字段作为主键,也可以多个字段共同构成主键
       语法:字段名称 类型(宽度) Primary key
       示例:
       create table customer(
        cust_no varchar(32) Primary key,
       cust_name varchar(64) not null)
       default charset=utf8;
     4,默认值:(default)
       指定某个字段的默认值,如果插入一比数据,该字段没有值,系统会自动添加默认值
       语法:字段名称 类型(宽度) default 默认值
       create table customer(
        cust_no varchar(32) Primary key,
       cust_name varchar(64) not null,
       status int default 0)
       default charset=utf8;

     5,自动增长:(auto_increment)
       指定为自动增长的字段,插入时不需要设置值,系统会在最大值的基础上加1,
       可以和主键共同使用
       语法:字段名称 数据类型(宽度) auto_increment
       示例:
       create table ai_test
        (id int Primary key auto_increment,  -- 自动增长的字段类型需是整数型
            name varchar(32) not null)
        default charset=utf8;

        insert table ai_test values
            (null,'jason');    -- 添加值时,自动添加的位置需要补充null.

     6,外键约束
       外键:在当前表中不是主键,在另一个表中是主键.
       外键的作用:保证数据一致性,完整性
       使用外键的条件:
        1,表的存储引擎类型为innodb
        2,被参照字段在外表中必须是主键
        3,当前表和外表中类型必须一致
       语法:
       constraint 外键名称 foreign key(当前表字段)
       references 参照表(参照字段)

       示例:
       create table account(
        acct_no varchar(32) Primary key,
        cust_no varchar(32) not null,
        constraint fk_cust_no foreign key(cust_no)
        references customer(cust_no))
        default charset=utf8;
      在account表中插入cust_no为'C0001'的数据,插入失败,(account参照一个不存在的实体)
      注:
      若参照表中没有要插入的数据,则外键表是无法插入的,
      需先在参照表中插入要插入的数据,再在外键表中插入

      若想删除参照表中的某个数据,需先将外检表的数据删除再删除参照表中的数据

     7,索引:
       查看索引:show index from 表名;
      1,定义:
       索引是提高查询效率的一种技术(相当于一本字典的索引或目录)
       索引是一种单独存放的数据结构,包含着数据表中所有记录的引用指针
       根据索引能快速找到数据所在位置
       通过避免全表扫描提高检索效率
      2,索引类别
       普通索引,唯一索引
       单列索引,组合索引
      3,创建索引:
       语法:
       index|unique|Primary key(字段名称)
       说明:
        index:创建普通索引
        unique:创建唯一索引
        Primary key 主键自动成为唯一索引

        示例:
        create table acct_trans_detail(
            trans_sn varchar(32) not null, -- 流水号
            trans_date datetime not null, -- 交易时间
            acct_no varchar(32) not null, -- 账号
            trans_type int null, -- 交易类型
            amt decimal(10,2) not null, -- 交易金额
            unique(trans_sn),  -- 交易流水建唯一索引
            index(trans_date)); -- 交易日期建普通索引
       通过修改方式创建索引
       - idx_acct_no是索引名称
       - acct_no是字段名称
       alter table acct_trans_detail add index idx_acct_no(acct_no);
       或
       create index idx_acct_no on acct_trans_detail(acct_no);
     4,删除索引:
       语法:drop index 索引名称 on 表的名称

     5,索引的优缺点
       优点:
        提高查询效率
        唯一索引能够保证数据的唯一性
        在使用分组,排序等子句时,能提高效率
       缺点:
        索引需要额外的存储空间
        维护索引结构需要额外的开销
        会降低增删改的效率

     6,索引使用原则:
       1,使用恰当的索引,不是越多越好
       2,避免对经常更新的表使用过多的索引
       3,在经常作为查询条件的字段上建立索引
       4,字段值太少不宜使用索引(如性别,状态)
       5,主键和唯一索引查询效率较高
       6,在经常排序的字段上使用索引
       7,数据量太少不宜使用索引
       8,二进制类型字段不适合使用索引

    4,表的复制,重命名
      1,复制:
        完全复制
        create table acct_new select * from acct;
        部分复制(只复制满足条件的数据)
        create table acct_new select * from acct where balance<5000;
        只复制结构,不复制数据
        create table acct_new select * from acct where 1=0;

        注:该方式复制代表不会复制键的属性

      2,重命名:
        格式: alter table 原表名 rename to 新表名
        示例:
        alter table acct rename to acct_new;


alter table 表名 modify 字段名 类型(宽度)
alter table orders modify order_id varchar(32) primary key ;
alter table orders modify cust_id varchar(32) not null,
alter table orders modify order_date datetime not null,
alter table orders modify products_num int not null;
alter table orders modify status enum
       ('1','2','3','4','5','6','9') default 1;
alter table orders add index order_date(order_date);