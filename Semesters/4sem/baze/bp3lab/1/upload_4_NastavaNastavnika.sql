CREATE TABLE Drzava
(
  sifDrzava VARCHAR(50) NOT NULL,
  naziv VARCHAR(100) NOT NULL,
  PRIMARY KEY (sifDrzava)
);

CREATE TABLE Predmet
(
  sifPredmet INT NOT NULL,
  nazPredmet VARCHAR(100) NOT NULL,
  ECTS INT NOT NULL,
  PRIMARY KEY (sifPredmet)
);

CREATE TABLE EvidencijaPredmetVrsta
(
  satiNastave INT NOT NULL,
  sifEvidencijaPredmetVrsta INT NOT NULL,
  sifPredmet INT NOT NULL,
  PRIMARY KEY (sifEvidencijaPredmetVrsta),
  FOREIGN KEY (sifPredmet) REFERENCES Predmet(sifPredmet)
);

CREATE TABLE AkademskaGodina
(
  sifAkademskaGodina INT NOT NULL,
  kratAkademskaGodina VARCHAR(50) NOT NULL,
  PRIMARY KEY (sifAkademskaGodina)
);

CREATE TABLE VrstaNastave
(
  kratVrstaNastave VARCHAR NOT NULL,
  nazVrstaNastave VARCHAR(50) NOT NULL,
  sifEvidencijaPredmetVrsta INT NOT NULL,
  PRIMARY KEY (kratVrstaNastave),
  FOREIGN KEY (sifEvidencijaPredmetVrsta) REFERENCES EvidencijaPredmetVrsta(sifEvidencijaPredmetVrsta)
);

CREATE TABLE Zaposlenik
(
  sifZaposlenik INT NOT NULL,
  ime VARCHAR(50) NOT NULL,
  prezime VARCHAR(50) NOT NULL,
  datRodjenja DATE NOT NULL,
  datPocetkaZaposlenja DATE NOT NULL,
  datPrestankaZaposlenja DATE NOT NULL,
  email VARCHAR(50) NOT NULL,
  sifUlica INT,
  PRIMARY KEY (sifZaposlenik),
  FOREIGN KEY (sifUlica) REFERENCES Ulica(sifUlica),
  UNIQUE (email)
);

CREATE TABLE Mjesto
(
  sifMjesto INT NOT NULL,
  postBroj VARCHAR(50) NOT NULL,
  naziv VARCHAR(100) NOT NULL,
  sifDrzava VARCHAR(50) NOT NULL,
  sifZaposlenik INT NOT NULL,
  PRIMARY KEY (sifMjesto),
  FOREIGN KEY (sifDrzava) REFERENCES Drzava(sifDrzava),
  FOREIGN KEY (sifZaposlenik) REFERENCES Zaposlenik(sifZaposlenik)
);

CREATE TABLE Ulica
(
  sifUlica INT NOT NULL,
  naziv VARCHAR(100) NOT NULL,
  sifMjesto INT NOT NULL,
  PRIMARY KEY (sifUlica),
  FOREIGN KEY (sifMjesto) REFERENCES Mjesto(sifMjesto)
);

CREATE TABLE nastavaNastavnika
(
  sifEvidencijaPredmetVrsta INT NOT NULL,
  sifZaposlenik INT NOT NULL,
  PRIMARY KEY (sifEvidencijaPredmetVrsta),
  FOREIGN KEY (sifEvidencijaPredmetVrsta) REFERENCES EvidencijaPredmetVrsta(sifEvidencijaPredmetVrsta),
  FOREIGN KEY (sifZaposlenik) REFERENCES Zaposlenik(sifZaposlenik)
);

CREATE TABLE nastavaNastavnikaZaAkGodinu
(
  sifAkademskaGodina INT NOT NULL,
  sifEvidencijaPredmetVrsta INT NOT NULL,
  PRIMARY KEY (sifAkademskaGodina, sifEvidencijaPredmetVrsta),
  FOREIGN KEY (sifAkademskaGodina) REFERENCES AkademskaGodina(sifAkademskaGodina),
  FOREIGN KEY (sifEvidencijaPredmetVrsta) REFERENCES nastavaNastavnika(sifEvidencijaPredmetVrsta),
  CONSTRAINT chkUkSati CHECK (ukSati BETWEEN 1.0 AND 30.0)
);

