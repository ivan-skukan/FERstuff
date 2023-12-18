CREATE TABLE PREDMET
(
  šifraPredmet INT NOT NULL,
  nazivPredmet INT NOT NULL,
  ECTSbod NUMERIC(5 2) NOT NULL,
  ukBrojSati INT NOT NULL,
  PRIMARY KEY (šifraPredmet),
  UNIQUE (ukBrojSati)
);

CREATE TABLE AK_GODINA
(
  šifraAkGod INT NOT NULL,
  kraticaAkGod VARCHAR(50) NOT NULL,
  PRIMARY KEY (šifraAkGod),
  UNIQUE (kraticaAkGod)
);

CREATE TABLE DRŽAVA
(
  ISOoznaka VARCHAR(2) NOT NULL,
  nazivDržava VARCHAR(100) NOT NULL,
  PRIMARY KEY (ISOoznaka),
  UNIQUE (nazivDržava)
);

CREATE TABLE MJESTO
(
  šifraMjesto INT NOT NULL,
  pBr VARCHAR(50),
  nazivMjesto VARCHAR(100) NOT NULL,
  nazivDržava INT NOT NULL,
  ISOoznaka VARCHAR(2) NOT NULL,
  PRIMARY KEY (šifraMjesto, ISOoznaka),
  FOREIGN KEY (ISOoznaka) REFERENCES DRŽAVA(ISOoznaka),
  UNIQUE (nazivMjesto),
  UNIQUE (nazivDržava)
);

CREATE TABLE ULICA
(
  šifraUlica INT NOT NULL,
  nazivUlica VARCHAR(100) NOT NULL,
  šifraMjesto INT NOT NULL,
  PRIMARY KEY (šifraUlica, šifraMjesto),
  FOREIGN KEY (šifraMjesto) REFERENCES MJESTO(šifraMjesto)
);

CREATE TABLE brojSati
(
  šifraPredmet INT NOT NULL,
  šifraAkGod INT NOT NULL,
  chkUkSati SMALLINT
  FOREIGN KEY (šifraPredmet) REFERENCES PREDMET(šifraPredmet),
  FOREIGN KEY (šifraAkGod) REFERENCES AK_GODINA(šifraAkGod)
  CHECK (chkUkSati BETWEEN 1 AND 300)
);

CREATE TABLE NASTAVNIK
(
  šifraNastavnik INT NOT NULL,
  ime VARCHAR(50) NOT NULL,
  prezime VARCHAR(50) NOT NULL,
  datumRođenja DATE NOT NULL,
  datumZavršetka DATE NOT NULL,
  datumPočetka DATE NOT NULL
                CONSTRAINT chkDatumiZaposlenja CHECK (datumPočetka::DATE < datumZavršetka::DATE),
  email VARCHAR(50) NOT NULL,
  mjestoRođenja INT NOT NULL,
  ulicaStanovanja INT,
  šifraMjesto INT NOT NULL,
  ISOoznaka VARCHAR(2) NOT NULL,
  PRIMARY KEY (šifraNastavnik),
  FOREIGN KEY (šifraMjesto, ISOoznaka) REFERENCES MJESTO(šifraMjesto, ISOoznaka),
  UNIQUE (email)
);

CREATE TABLE VRSTA_NASTAVE
(
  kraticaNastava VARCHAR(5) NOT NULL,
  nazivNastava VARCHAR(50) NOT NULL,
  šifraNastavnik INT NOT NULL,
  šifraPredmet INT NOT NULL,
  PRIMARY KEY (kraticaNastava, šifraNastavnik),
  FOREIGN KEY (šifraNastavnik) REFERENCES NASTAVNIK(šifraNastavnik),
  FOREIGN KEY (šifraPredmet) REFERENCES PREDMET(šifraPredmet)
  
);