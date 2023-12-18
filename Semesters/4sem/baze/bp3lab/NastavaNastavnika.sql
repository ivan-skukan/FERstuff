CREATE TABLE drzava
(
  ISO CHAR(2) NOT NULL,
  nazDr VARCHAR(100) NOT NULL,
  PRIMARY KEY (ISO),
  UNIQUE (nazDr)
);

CREATE TABLE vrsta_nastave
(
  kraticaVN VARCHAR(5) NOT NULL,
  nazivVN VARCHAR(50) NOT NULL,
  PRIMARY KEY (kraticaVN)
);

CREATE TABLE predmet
(
  sifPred INT NOT NULL,
  nazivPred VARCHAR(100) NOT NULL,
  ECTS NUMERIC(2) NOT NULL,
  PRIMARY KEY (sifPred)
);

CREATE TABLE akGod
(
  sifAkGod INT NOT NULL,
  kraticaAkGod VARCHAR(50) NOT NULL,
  PRIMARY KEY (sifAkGod),
  UNIQUE (kraticaAkGod)
);

CREATE TABLE evidencija_sati_predmeta
(
  sifEvid INT NOT NULL,
  ukBrSati INT NOT NULL,
  PRIMARY KEY (sifEvid),
  CONSTRAINT chkUkSati CHECK (uKBrSati between 1 and 300)
);

CREATE TABLE tenarna_veza
(
  kraticaVN VARCHAR(5) NOT NULL,
  sifEvid INT NOT NULL,
  sifPred INT NOT NULL,
  PRIMARY KEY (kraticaVN, sifEvid, sifPred),
  FOREIGN KEY (kraticaVN) REFERENCES vrsta_nastave(kraticaVN),
  FOREIGN KEY (sifEvid) REFERENCES evidencija_sati_predmeta(sifEvid),
  FOREIGN KEY (sifPred) REFERENCES predmet(sifPred)
);

CREATE TABLE mjesto
(
  sifMj INT NOT NULL,
  postOzn VARCHAR(50) NOT NULL,
  nazivMj VARCHAR(100) NOT NULL,
  ISO CHAR(2) NOT NULL,
  PRIMARY KEY (sifMj),
  FOREIGN KEY (ISO) REFERENCES drzava(ISO)
);

CREATE TABLE ulica
(
  sifUl INT NOT NULL,
  nazUl VARCHAR(100) NOT NULL,
  NewAttribute INT NOT NULL,
  sifMj INT NOT NULL,
  PRIMARY KEY (sifUl),
  FOREIGN KEY (sifMj) REFERENCES mjesto(sifMj)
);

CREATE TABLE nastavnik
(
  sifNas INT NOT NULL,
  ime VARCHAR(50) NOT NULL,
  prezime VARCHAR(50) NOT NULL,
  datRod DATE NOT NULL,
  datPocRad DATE NOT NULL,
  datKrajRad DATE NOT NULL,
  email VARCHAR(50) NOT NULL,
  sifMj INT NOT NULL,
  sifUl INT,
  PRIMARY KEY (sifNas),
  FOREIGN KEY (sifMj) REFERENCES mjesto(sifMj),
  FOREIGN KEY (sifUl) REFERENCES ulica(sifUl),
  UNIQUE (email),
  CONSTRAINT chkDatumiZaposlenja CHECK (datPocRad < datKrajRad)
);

CREATE TABLE evidencija_sati_nastavnika_po_akGod
(
  kraticaVN VARCHAR(5) NOT NULL,
  sifNas INT NOT NULL,
  sifAkGod INT NOT NULL,
  PRIMARY KEY (kraticaVN, sifNas),
  FOREIGN KEY (kraticaVN) REFERENCES vrsta_nastave(kraticaVN),
  FOREIGN KEY (sifNas) REFERENCES nastavnik(sifNas),
  FOREIGN KEY (sifAkGod) REFERENCES akGod(sifAkGod)
);

CREATE TABLE evidencija_nastanvika_po_akGod_vrsti_i_predmetu
(
  sifAkGod INT NOT NULL,
  sifNas INT NOT NULL,
  kraticaVN VARCHAR(5) NOT NULL,
  sifPred INT NOT NULL,
  PRIMARY KEY (sifAkGod),
  FOREIGN KEY (sifAkGod) REFERENCES akGod(sifAkGod),
  FOREIGN KEY (sifNas) REFERENCES nastavnik(sifNas),
  FOREIGN KEY (kraticaVN) REFERENCES vrsta_nastave(kraticaVN),
  FOREIGN KEY (sifPred) REFERENCES predmet(sifPred)
);
