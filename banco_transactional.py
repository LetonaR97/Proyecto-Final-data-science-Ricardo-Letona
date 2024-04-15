DDL_QUERY =  '''
CREATE TABLE rol (
  idrol SERIAL PRIMARY KEY,
  nombre VARCHAR(20),
  descripcion VARCHAR(255),
  estado BOOLEAN
);

CREATE TABLE categoria (
  idcategoria SERIAL PRIMARY KEY,
  nombre VARCHAR(50),
  descripcion VARCHAR(255),
  estado BOOLEAN
);

CREATE TABLE persona (
  idpersona SERIAL PRIMARY KEY,
  tipo_persona VARCHAR(20),
  nombre VARCHAR(100),
  tipo_documento VARCHAR(20),
  num_documento VARCHAR(20),
  direccion VARCHAR(70),
  telefono VARCHAR(20),
  email VARCHAR(50)
);

CREATE TABLE usuario (
  idusuario SERIAL PRIMARY KEY,
  idrol INTEGER,
  nombre VARCHAR(100),
  tipo_documento VARCHAR(20),
  num_documento VARCHAR(20),
  direccion VARCHAR(70),
  telefono VARCHAR(20),
  email VARCHAR(50),
  clave BYTEA,
  estado BOOLEAN,
  FOREIGN KEY (idrol) REFERENCES rol(idrol)
);

CREATE TABLE articulo (
  idarticulo SERIAL PRIMARY KEY,
  idcategoria INTEGER,
  codigo VARCHAR(50),
  nombre VARCHAR(100),
  precio_venta NUMERIC(11,2),
  stock INTEGER,
  descripcion VARCHAR(255),
  imagen VARCHAR(240),
  estado BOOLEAN,
  FOREIGN KEY (idcategoria) REFERENCES categoria(idcategoria)
);

CREATE TABLE venta (
  idventa SERIAL PRIMARY KEY,
  idcliente INTEGER,
  idusuario INTEGER,
  tipo_comprobante VARCHAR(20),
  serie_comprobante VARCHAR(7),
  num_comprobante VARCHAR(10),
  fecha TIMESTAMP,
  impuesto NUMERIC(4,2),
  total NUMERIC(11,2),
  estado VARCHAR(20),
  FOREIGN KEY (idcliente) REFERENCES persona(idpersona),
  FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);

CREATE TABLE detalle_venta (
  iddetalle_venta SERIAL PRIMARY KEY,
  idventa INTEGER,
  idarticulo INTEGER,
  cantidad INTEGER,
  precio NUMERIC(11,2),
  descuento NUMERIC(11,2),
  FOREIGN KEY (idventa) REFERENCES venta(idventa),
  FOREIGN KEY (idarticulo) REFERENCES articulo(idarticulo)
);

CREATE TABLE ingreso (
  idingreso SERIAL PRIMARY KEY,
  idproveedor INTEGER,
  idusuario INTEGER,
  tipo_comprobante VARCHAR(20),
  serie_comprobante VARCHAR(7),
  num_comprobante VARCHAR(10),
  fecha TIMESTAMP,
  impuesto NUMERIC(4,2),
  total NUMERIC(11,2),
  estado VARCHAR(20),
  FOREIGN KEY (idproveedor) REFERENCES persona(idpersona),
  FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);

CREATE TABLE detalle_ingreso (
  iddetalle_ingreso SERIAL PRIMARY KEY,
  idingreso INTEGER,
  idarticulo INTEGER,
  cantidad INTEGER,
  precio NUMERIC(11,2),
  FOREIGN KEY (idingreso) REFERENCES ingreso(idingreso),
  FOREIGN KEY (idarticulo) REFERENCES articulo(idarticulo)
);
'''