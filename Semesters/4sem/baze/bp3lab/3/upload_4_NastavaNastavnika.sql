CREATE TABLE Ulica
(
  SifaUlice INT NOT NULL,
  NazivUlice VARCHAR(100) NOT NULL,
  SifPripadnoMjesto INT NOT NULL,
  PRIMARY KEY (SifaUlice)
);

CREATE TABLE NastavaNastavnika
(
  BrojSati INT NOT NULL,
  SifAKGod INT NOT NULL,
  Nastavnik INT NOT NULL,
  VrstaNastave INT NOT NULL,
  PRIMARY KEY (SifAKGod),
  UNIQUE (Nastavnik),
  UNIQUE (VrstaNastave)
);

CREATE TABLE Nastavnik
(
  Sifra INT NOT NULL,
  Ime VARCHAR(50) NOT NULL,
  Prezime VARCHAR(50) NOT NULL,
  DatumRod DATE NOT NULL,
  DatumPocRad DATE NOT NULL,
  DatumKrajRad DATE NOT NULL,
  EMail VARCHAR(50) NOT NULL,
  MjestoRodenja INT NOT NULL,
  UlicaStanovanja INT,
  SifAKGod INT NOT NULL,
  SifaUlice INT NOT NULL,
  PRIMARY KEY (Sifra, SifAKGod),
  FOREIGN KEY (SifAKGod) REFERENCES NastavaNastavnika(SifAKGod),
  FOREIGN KEY (SifaUlice) REFERENCES Ulica(SifaUlice),
  UNIQUE (EMail)
  CONSTRAINT chkDatumiZaposlenja CHECK (DatumPocRad < DatumKrajRad)
);

CREATE TABLE Mjesto
(
  SifraMjesta INT NOT NULL,
  PBR VARCHAR(50) NOT NULL,
  NazivMjesta VARCHAR(100) NOT NULL,
  ISOPripadnaDrzava INT NOT NULL,
  SifaUlice INT NOT NULL,
  Sifra INT NOT NULL,
  SifAKGod INT NOT NULL,
  PRIMARY KEY (SifraMjesta),
  FOREIGN KEY (SifaUlice) REFERENCES Ulica(SifaUlice),
  FOREIGN KEY (Sifra, SifAKGod) REFERENCES Nastavnik(Sifra, SifAKGod)
);

CREATE TABLE Drzava
(
  ISO CHAR(2) NOT NULL,
  NazivDrzave VARCHAR(100) NOT NULL,
  SifraMjesta INT NOT NULL,
  PRIMARY KEY (ISO),
  FOREIGN KEY (SifraMjesta) REFERENCES Mjesto(SifraMjesta),
  UNIQUE (NazivDrzave)
);

CREATE TABLE VrstaNastave
(
  Kratica VARCHAR(5) NOT NULL,
  Naziv VARCHAR(50) NOT NULL,
  SifAKGod INT NOT NULL,
  PRIMARY KEY (Kratica),
  FOREIGN KEY (SifAKGod) REFERENCES NastavaNastavnika(SifAKGod)
);

CREATE TABLE Predmet
(
  SifPredmet INT NOT NULL,
  NazivPredmet VARCHAR(100) NOT NULL,
  BrojECTS NUMERIC(4,2) NOT NULL,
  BrojSati INT NOT NULL,
  Kratica VARCHAR(5) NOT NULL,
  PRIMARY KEY (SifPredmet),
  FOREIGN KEY (Kratica) REFERENCES VrstaNastave(Kratica)
  CONSTRAINT chkUkSati CHECK (BrojSati>1 AND BrojSati<300)
);

CREATE TABLE AKGod
(
  SifAKGod INT NOT NULL,
  KraticaAKGod VARCHAR(50) NOT NULL,
  SifAKGod INT NOT NULL,
  PRIMARY KEY (SifAKGod),
  FOREIGN KEY (SifAKGod) REFERENCES NastavaNastavnika(SifAKGod),
  UNIQUE (KraticaAKGod)
);
