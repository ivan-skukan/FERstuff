CREATE TABLE drzava
(
  ISO CHAR(2) NOT NULL,
  nazDrzava VARCHAR(100) NOT NULL,
  PRIMARY KEY (ISO),
  UNIQUE (nazDrzava)
);

CREATE TABLE vrstaNastave
(
  kratVNast VARCHAR(5) NOT NULL,
  naziv VARCHAR(50) NOT NULL,
  PRIMARY KEY (kratVNast)
);

CREATE TABLE predmet
(
  sifPredmet INT NOT NULL,
  naziv VARCHAR(100) NOT NULL,
  ECTS NUMERIC(4, 2) NOT NULL,
  PRIMARY KEY (sifPredmet)
);

CREATE TABLE akGod
(
  sifAkGod INT NOT NULL,
  kratAkGod VARCHAR(50) NOT NULL,
  PRIMARY KEY (sifAkGod),
  UNIQUE (kratAkGod)
);

CREATE TABLE vrstNastPred
(
  sifVNP INT NOT NULL,
  ukBrSati INT NOT NULL,
  sifPredmet INT NOT NULL,
  kratVNast VARCHAR(5) NOT NULL,
  PRIMARY KEY (sifVNP),
  FOREIGN KEY (sifPredmet) REFERENCES predmet(sifPredmet),
  FOREIGN KEY (kratVNast) REFERENCES vrstaNastave(kratVNast),
  CONSTRAINT chkUkSati CHECK (ukBrSati BETWEEN 1.0 AND 300.0)
);

CREATE TABLE mjesto
(
  sifMjesto INT NOT NULL,
  post VARCHAR(50),
  nazMjesto VARCHAR(100) NOT NULL,
  ISO CHAR(2) NOT NULL,
  PRIMARY KEY (sifMjesto),
  FOREIGN KEY (ISO) REFERENCES drzava(ISO)
);

CREATE TABLE ulica
(
  sifUlica INT NOT NULL,
  nazUlica VARCHAR(100) NOT NULL,
  sifMjesto INT NOT NULL,
  PRIMARY KEY (sifUlica),
  FOREIGN KEY (sifMjesto) REFERENCES mjesto(sifMjesto)
);

CREATE TABLE nastavnik
(
  sifNast INT NOT NULL,
  imeNast VARCHAR(50) NOT NULL,
  prezNast VARCHAR(50) NOT NULL,
  datumRod DATE NOT NULL,
  datumPoc DATE NOT NULL,
  datumKraj DATE NOT NULL,
  email VARCHAR(50) NOT NULL,
  sifMjesto INT NOT NULL,
  sifUlica INT,
  PRIMARY KEY (sifNast),
  FOREIGN KEY (sifMjesto) REFERENCES mjesto(sifMjesto),
  FOREIGN KEY (sifUlica) REFERENCES ulica(sifUlica),
  UNIQUE (email),
  CONSTRAINT chkDatumiZaposlenja CHECK (datumPoc < datumKraj)
);

CREATE TABLE nastNastavnika
(
  brSati INT NOT NULL,
  sifNast INT NOT NULL,
  sifVNP INT NOT NULL,
  sifAkGod INT NOT NULL,
  PRIMARY KEY (sifNast, sifVNP, sifAkGod),
  FOREIGN KEY (sifNast) REFERENCES nastavnik(sifNast),
  FOREIGN KEY (sifVNP) REFERENCES vrstNastPred(sifVNP),
  FOREIGN KEY (sifAkGod) REFERENCES akGod(sifAkGod)
);