DDL_QUERY =  '''
DROP TABLE IF EXISTS fact_ventas;
DROP TABLE IF EXISTS dim_tiempo;
DROP TABLE IF EXISTS dim_producto;
DROP TABLE IF EXISTS dim_categoria;
DROP TABLE IF EXISTS dim_empleado;
DROP TABLE IF EXISTS dim_cliente;

CREATE TABLE dim_tiempo (
    date_key INT NOT NULL AUTO_INCREMENT,
    date DATE NOT NULL,
    year INT NOT NULL,
    quarter INT NOT NULL,
    month INT NOT NULL,
    week INT NOT NULL,
    day_of_week INT NOT NULL,
    PRIMARY KEY (date_key)
);

CREATE TABLE dim_producto (
    producto_key INT NOT NULL AUTO_INCREMENT,
    idarticulo INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    precio_venta NUMERIC(11,2) NOT NULL,
    PRIMARY KEY (producto_key)
);

CREATE TABLE dim_categoria (
    categoria_key INT NOT NULL AUTO_INCREMENT,
    idcategoria INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255),
    PRIMARY KEY (categoria_key)
);

CREATE TABLE dim_empleado (
    empleado_key INT NOT NULL AUTO_INCREMENT,
    idusuario INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    rol VARCHAR(20),
    PRIMARY KEY (empleado_key)
);

CREATE TABLE dim_cliente (
    cliente_key INT NOT NULL AUTO_INCREMENT,
    idpersona INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(70),
    telefono VARCHAR(20),
    email VARCHAR(50),
    PRIMARY KEY (cliente_key)
);

CREATE TABLE fact_ventas (
    venta_key INT NOT NULL AUTO_INCREMENT,
    date_key INT NOT NULL,
    producto_key INT NOT NULL,
    categoria_key INT NOT NULL,
    empleado_key INT NOT NULL,
    cliente_key INT NOT NULL,
    cantidad INT NOT NULL,
    total NUMERIC(11,2) NOT NULL,
    PRIMARY KEY (venta_key),
    FOREIGN KEY (date_key) REFERENCES dim_tiempo (date_key),
    FOREIGN KEY (producto_key) REFERENCES dim_producto (producto_key),
    FOREIGN KEY (categoria_key) REFERENCES dim_categoria (categoria_key),
    FOREIGN KEY (empleado_key) REFERENCES dim_empleado (empleado_key),
    FOREIGN KEY (cliente_key) REFERENCES dim_cliente (cliente_key)
);

'''