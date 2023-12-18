CREATE TABLE DRŽAVA
(
  ISOoznaka CHAR(2) NOT NULL,
  nazivDrzava VARCHAR(100) NOT NULL,
  PRIMARY KEY (ISOoznaka),
  UNIQUE (nazivDrzava)
);

CREATE TABLE VRSTA_NASTAVE
(
  kraticaVrsta VARCHAR(5) NOT NULL,
  nazivVrsta VARCHAR(50) NOT NULL,
  PRIMARY KEY (kraticaVrsta)
);

CREATE TABLE PREDMET
(
  sifPredmet INT NOT NULL,
  nazivPredmet VARCHAR(100) NOT NULL,
  ECTSbod NUMERIC NOT NULL,
  PRIMARY KEY (sifPredmet)
);

CREATE TABLE AK_GODINA
(
  sifAkGod INT NOT NULL,
  kraticaAkGod VARCHAR(50) NOT NULL,
  PRIMARY KEY (sifAkGod),
  UNIQUE (kraticaAkGod)
);

CREATE TABLE VRSTA_PRED
(
  sifraVrPred INT NOT NULL,
  ukBrojSati INT NOT NULL,
  kraticaVrsta VARCHAR(5) NOT NULL,
  sifPredmet INT NOT NULL,
  PRIMARY KEY (sifraVrPred),
  FOREIGN KEY (kraticaVrsta) REFERENCES VRSTA_NASTAVE(kraticaVrsta),
  FOREIGN KEY (sifPredmet) REFERENCES PREDMET(sifPredmet),
  CONSTRAINT chkUkSati CHECK (ukBrojSati BETWEEN 1 AND 300)
);

CREATE TABLE MJESTO
(
  sifMjesto INT NOT NULL,
  postBroj VARCHAR(50),
  nazivMjesto VARCHAR(100) NOT NULL,
  ISOoznaka CHAR(2) NOT NULL,
  PRIMARY KEY (sifMjesto),
  FOREIGN KEY (ISOoznaka) REFERENCES DRŽAVA(ISOoznaka),
  UNIQUE (postBroj)
);

CREATE TABLE ULICA
(
  nazivUlica VARCHAR(100) NOT NULL,
  sifUlica INT NOT NULL,
  sifMjesto INT NOT NULL,
  PRIMARY KEY (sifUlica),
  FOREIGN KEY (sifMjesto) REFERENCES MJESTO(sifMjesto)
);

CREATE TABLE NASTAVNIK
(
  sifNastavnik INT NOT NULL,
  imeNastavnik VARCHAR(50) NOT NULL,
  prezNastavnik VARCHAR(50) NOT NULL,
  datumRodjenja DATE NOT NULL,
  datumKrajZap DATE NOT NULL,
  datumPocZap DATE NOT NULL,
  email VARCHAR(50) NOT NULL,
  sifMjesto INT NOT NULL,
  sifUlica INT,
  PRIMARY KEY (sifNastavnik),
  FOREIGN KEY (sifMjesto) REFERENCES MJESTO(sifMjesto),
  FOREIGN KEY (sifUlica) REFERENCES ULICA(sifUlica),
  UNIQUE (email),
  CONSTRAINT chkDatumiZaposlenja CHECK (datumKrajZap - datumPocZap > 0)
);

CREATE TABLE NASTAVA
(
  sifNastavnik INT NOT NULL,
  sifAkGod INT NOT NULL,
  PRIMARY KEY (sifNastavnik, sifAkGod),
  FOREIGN KEY (sifNastavnik) REFERENCES NASTAVNIK(sifNastavnik),
  FOREIGN KEY (sifAkGod) REFERENCES AK_GODINA(sifAkGod)
);

CREATE TABLE odradSto
(
  brojSatiNast INT NOT NULL,
  sifNastavnik INT NOT NULL,
  sifraVrPred INT NOT NULL,
  sifAkGod INT NOT NULL,
  PRIMARY KEY (sifNastavnik, sifAkGod, sifraVrPred),
  FOREIGN KEY (sifNastavnik, sifAkGod) REFERENCES NASTAVA(sifNastavnik, sifAkGod),
  FOREIGN KEY (sifraVrPred) REFERENCES VRSTA_PRED(sifraVrPred)
);