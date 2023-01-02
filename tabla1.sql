create table Productos
(
	idProducto int(11) unsigned Not null auto_increment,
    Nombre	varchar(50)	Not null,
    Precio	double	null,
    Marca	varchar(30)	Not null,
    Categoria	varchar(30)	Not null,
    Stock	int(6)	Not null,
    Disponible	boolean Null default false
    
)
