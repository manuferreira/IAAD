CREATE SCHEMA companhia_aerea;
USE companhia_aerea;

CREATE TABLE aeroporto (
	Codigo_aeroporto VARCHAR(5) NOT NULL,
    Nome VARCHAR(45) NOT NULL,
    Cidade VARCHAR(45) NOT NULL,
    Estado VARCHAR(45),
    PRIMARY KEY(Codigo_aeroporto)
);

CREATE TABLE voo (
	Numero_voo VARCHAR(6) NOT NULL,
    Companhia_aerea VARCHAR(45) NOT NULL,
    Dia_da_semana VARCHAR(45) NOT NULL,
    PRIMARY KEY(Numero_voo)
);

CREATE TABLE trecho_voo(
	Numero_trecho INT NOT NULL,
    Numero_voo VARCHAR(6) NOT NULL,
    Codigo_aeroporto_partida VARCHAR(5) NOT NULL,
    Codigo_aeroporto_chegada VARCHAR(5) NOT NULL,
    Horario_partida_previsto VARCHAR(10),
    Horario_chegada_previsto VARCHAR(10),
    PRIMARY KEY(Numero_trecho, Numero_voo)
);

CREATE TABLE instancia_trecho(
	Numero_voo VARCHAR(6) NOT NULL,
    Numero_trecho INT NOT NULL,
    Data DATE NOT NULL,
    Numero_assentos_disponiveis VARCHAR(45),
    Codigo_aeronave VARCHAR(5),
    Codigo_aeroporto_partida VARCHAR(5),
    Horario_partida VARCHAR(10),
    Codigo_aeroporto_chegada VARCHAR(5),
    Horario_chegada VARCHAR(10),
    PRIMARY KEY(Numero_voo, Numero_trecho, Data)
);

CREATE TABLE tarifa(
	Numero_voo VARCHAR(6) NOT NULL,
    Codigo_tarifa INT NOT NULL,
    Quantidade INT,
    Restricoes VARCHAR(50),
    PRIMARY KEY(Numero_voo, Codigo_tarifa)
);

CREATE TABLE tipo_aeronave(
	Nome_tipo_aeronave VARCHAR(20) NOT NULL,
    Qtd_max_assentos VARCHAR(10),
    Companhia VARCHAR(45),
    PRIMARY KEY(Nome_tipo_aeronave)
);

CREATE TABLE pode_pousar(
	Nome_tipo_aeronave VARCHAR(45) NOT NULL,
    Codigo_aeroporto VARCHAR(5) NOT NULL,
    PRIMARY KEY(Nome_tipo_aeronave, Codigo_aeroporto)
);

CREATE TABLE aeronave(
	Codigo_aeronave VARCHAR(5) NOT NULL,
    Numero_total_assentos VARCHAR(10),
    Tipo_aeronave VARCHAR(20),
    PRIMARY KEY(Codigo_aeronave)
);

CREATE TABLE reserva_assento(
	Numero_voo VARCHAR(6) NOT NULL,
    Numero_trecho INT NOT NULL,
    Data DATE NOT NULL,
    Numero_assento VARCHAR(10) NOT NULL,
    Nome_cliente VARCHAR(50),
    Telefone_cliente VARCHAR(10),
    PRIMARY KEY(Numero_voo, Numero_trecho, Data, Numero_assento)
);


/*INSERINDO NAS TABELAS*/
INSERT INTO aeroporto VALUES 
    ('10001','AEROPORTO DE MANUSSA','HELLCIFE','PE'),
    ('30003','AEROPORTO DE RENATO', 'ORLINDA','MG'),
    ('15030', 'AEROPORTO DE VICTOR', 'CAMARABRIGE','TI'),
    ('20002','AEROPORTO DE NINGUEM','NOONEKNOWS','IDK');

INSERT INTO voo VALUES
    ('111116','MANUSENDS','QUARTA'),
    ('222226','RENATRAVEL','SEGUNDA'),
    ('333336','VITORRIVE','SEXTA'),
    ('444446','NOONEGOES','DOMINGO');

INSERT INTO trecho_voo VALUES
    ('111116',1,'10001','20002','11:11','00:00'),
    ('222226',2,'20002','15030','22:22','00:00'),
    ('333336',3,'15030','30003','00:33','00:00'),
    ('444446',4,'30003','10001','00:44','00:00');

INSERT INTO instancia_trecho VALUES
    ('111116',1,'2021/01/01','20','11115','10001','11:11','20002','00:00'),
    ('222226',2,'2021/10/01','10','22225','20002','22:22','15030','00:00'),
    ('333336',3,'2021/02/09','3','33335','15030','00:33','30003','00:00'),
    ('444446',4,'2021/02/04','0','44445','30003','00:44','10001','00:00');

INSERT INTO  tarifa VALUES
    ('111116',11,20,'NA'),
    ('222226',12,10,'NA'),
    ('333336',13,3,'NA'),
    ('444446',14,0,'NA');

INSERT INTO tipo_aeronave VALUES
    ('Jatinho','30','MANUSENDS'),
    ('Boing','120','RENATRAVEL'),
    ('Foguete','4','VITORRIVE'),
    ('Teleporte','1000','NOONEGOES');

INSERT INTO pode_pousar VALUES 
    ('Jatinho','20002'),
    ('Boing','15030'),
    ('Foguete','30003'),
    ('Teleporte','10001');

INSERT INTO aeronave VALUES
    ('11115','30','Jatinho'),
    ('22225','120','Boing'),
    ('33335','3','Foguete'),
    ('44445','1000','Teleporte');


INSERT INTO reserva_assento VALUES 
    ('111116',1,'2021/01/01','M01','Manussa','8190909090'),
    ('222226',2,'2021/10/01','R02','Renato','8198080808'),
    ('333336',3,'2021/02/09','J03','J. Victor','8197070707'),
    ('444446',4,'2021/02/04','N04','No One','8196060606');


ALTER TABLE trecho_voo ADD FOREIGN KEY(Numero_voo) REFERENCES voo(Numero_voo);
ALTER TABLE trecho_voo ADD FOREIGN KEY(Codigo_aeroporto_partida) REFERENCES aeroporto(Codigo_aeroporto);
ALTER TABLE trecho_voo ADD FOREIGN KEY(Codigo_aeroporto_chegada) REFERENCES aeroporto(Codigo_aeroporto);
ALTER TABLE instancia_trecho ADD FOREIGN KEY(Numero_voo) REFERENCES voo(Numero_voo);
ALTER TABLE instancia_trecho ADD FOREIGN KEY(Numero_trecho) REFERENCES trecho_voo(Numero_trecho);
ALTER TABLE instancia_trecho ADD FOREIGN KEY(Codigo_aeronave) REFERENCES aeronave(Codigo_aeronave);
ALTER TABLE instancia_trecho ADD FOREIGN KEY(Codigo_aeroporto_partida) REFERENCES aeroporto(Codigo_aeroporto);
ALTER TABLE instancia_trecho ADD FOREIGN KEY(Codigo_aeroporto_chegada) REFERENCES aeroporto(Codigo_aeroporto);
ALTER TABLE tarifa ADD FOREIGN KEY(Numero_voo) REFERENCES voo(Numero_voo);
ALTER TABLE pode_pousar ADD FOREIGN KEY(Nome_tipo_aeronave) REFERENCES tipo_aeronave(Nome_tipo_aeronave);
ALTER TABLE pode_pousar ADD FOREIGN KEY(Codigo_aeroporto) REFERENCES aeroporto(Codigo_aeroporto);
ALTER TABLE aeronave ADD FOREIGN KEY(Tipo_aeronave) REFERENCES tipo_aeronave(Nome_tipo_aeronave);
ALTER TABLE reserva_assento ADD FOREIGN KEY(Numero_voo, Numero_trecho, Data) REFERENCES instancia_trecho(Numero_voo, Numero_trecho, Data);



