CREATE DATABASE Prod_comunidades;
CREATE SCHEMA datos_prod_comunidades;

SET search_path TO datos_prod_comunidades, "$user", public;

CREATE TABLE Region(
	id_region serial PRIMARY KEY,
	nombre_region varchar(50)NOT NULL
);

CREATE TABLE Comunidad(
	id_comunidad serial PRIMARY KEY,
	region_fk int NOT NULL,
	nombre_Comunidad varchar(50)NOT NULL,
	FOREIGN KEY(region_fk) REFERENCES Region(id_region)
);

CREATE TABLE Tipo_Producto(
	id_Tipo_Producto serial PRIMARY KEY,
	nombre_Tipo_Producto varchar(50)NOT NULL
);

DROP TABLE IF EXISTS Producto;
CREATE TABLE Producto(
	id_producto serial PRIMARY KEY,
	tipo_producto_fk int NOT NULL,
	nombre_Producto varchar(50)NOT NULL,
	caracteristica varchar(50)NOT NULL,
	cantidad int NOT NULL,
	FOREIGN KEY(tipo_producto_fk) REFERENCES Tipo_Producto(id_Tipo_Producto)
);

CREATE TABLE Produc_comun(
	id_produc_comun serial PRIMARY KEY,
	producto_fk int NOT NULL,
	comunidad_fk int NOT NULL,
	FOREIGN KEY(producto_fk) REFERENCES Producto(id_producto),
	FOREIGN KEY(comunidad_fk) REFERENCES Comunidad(id_comunidad)
);