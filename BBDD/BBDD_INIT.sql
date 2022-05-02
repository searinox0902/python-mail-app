
create database appmailpython

use appmailpython

create table user_data (
	Id_User varchar(15) primary key not null,
	NameUser varchar(50) not null,
	City varchar(50) not null,
	Age int not null,
	mail varchar(50) not null,
)

create table product_buy (
	IdProduct varchar(10) primary key not null,
	NameProduct varchar(50) not null,
	DescriptionProduct varchar(250),
	Precio int not null,
	DateBuy date not null,

	-- foreign keys -- 
	Id_User varchar(15) not null,
	foreign key (Id_user) references user_data(Id_User)
)


INSERT INTO user_data (Id_User, NameUser, City, Age, mail) 
VALUES ('1', 'DEFAULT', 'DEFAULT', 18, 'example@example.com')

INSERT INTO user_data (Id_User, NameUser, City, Age, mail) 
VALUES ('11152713344', 'JUAN VALDEZ', 'TARAZÁ', 23, 'svquintana98@gmail.com')

INSERT INTO product_buy (IdProduct, NameProduct, DescriptionProduct, Precio, DateBuy, Id_User) 
VALUES ('00001', 'Taza de té', 'Taza de té de Cobalto', 1000, GETDATE(), '1')

INSERT INTO product_buy (IdProduct, NameProduct, DescriptionProduct, Precio, DateBuy, Id_User) 
VALUES ('00002', 'TV 50 Pulgadas', 'TV grande, bonito y muy caro.', 111000, GETDATE(), '1')
