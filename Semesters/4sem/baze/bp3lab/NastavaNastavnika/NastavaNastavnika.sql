CREATE TABLE VrstaNastava
(
  kratVrNastava VARCHAR(5) NOT NULL,
  nazivVrNastav VARCHAR(50) NOT NULL,
  PRIMARY KEY (kratVrNastava)
);

CREATE TABLE Drzava
(
  ISOOznaka VARCHAR(2) NOT NULL,
  nazDrzava VARCHAR(100) NOT NULL,
  PRIMARY KEY (ISOOznaka),
  UNIQUE (nazDrzava)
);

CREATE TABLE Predmet
(
  sifPredmet INT NOT NULL,
  nazPredmet VARCHAR(100) NOT NULL,
  ECTSBod NUMERIC(5,2) NOT NULL,
  PRIMARY KEY (sifPredmet)
);

CREATE TABLE PredmetVN
(
  sifVrNastPred INT NOT NULL,
  ukSati INT NOT NULL,
  sifPredmet INT NOT NULL,
  kratVrNastava VARCHAR(5) NOT NULL,
  PRIMARY KEY (sifVrNastPred),
  FOREIGN KEY (sifPredmet) REFERENCES Predmet(sifPredmet),
  FOREIGN KEY (kratVrNastava) REFERENCES VrstaNastava(kratVrNastava)
);

CREATE TABLE AkGodina
(
  sifAkGodina INT NOT NULL,
  kratAkGodina INT NOT NULL,
  PRIMARY KEY (sifAkGodina),
  UNIQUE (kratAkGodina)
);

CREATE TABLE Mjesto
(
  sifMjesto INT NOT NULL,
  postOzn VARCHAR(50),
  nazMjesto VARCHAR(100) NOT NULL,
  ISOOznaka VARCHAR(2) NOT NULL,
  PRIMARY KEY (sifMjesto),
  FOREIGN KEY (ISOOznaka) REFERENCES Drzava(ISOOznaka)
);

CREATE TABLE Ulica
(
  sifUlica INT NOT NULL,
  nazUlica VARCHAR(100) NOT NULL,
  sifMjesto INT NOT NULL,
  PRIMARY KEY (sifUlica),
  FOREIGN KEY (sifMjesto) REFERENCES Mjesto(sifMjesto)
);

CREATE TABLE Zaposlenik
(
  sifZaposlenik INT NOT NULL,
  imeZ VARCHAR(50) NOT NULL,
  prezZ VARCHAR(50) NOT NULL,
  datRod DATE NOT NULL,
  eMail VARCHAR(50) NOT NULL,
  datZaposlenOd DATE NOT NULL,
  datZaposlenDo DATE NOT NULL,
  sifMjesto INT NOT NULL,
  sifUlica INT,
  PRIMARY KEY (sifZaposlenik),
  FOREIGN KEY (sifMjesto) REFERENCES Mjesto(sifMjesto),
  FOREIGN KEY (sifUlica) REFERENCES Ulica(sifUlica),
  UNIQUE (eMail),
  CONSTRAINT chkDatumiZaposlenja CHECK (datZaposlenOd < datZaposlenDo)
);

CREATE TABLE NastavnikNastava
(
  ukSati INT NOT NULL,
  sifZaposlenik INT NOT NULL,
  sifVrNastPred INT NOT NULL,
  sifAkGodina INT NOT NULL,
  PRIMARY KEY (sifZaposlenik, sifVrNastPred, sifAkGodina),
  FOREIGN KEY (sifZaposlenik) REFERENCES Zaposlenik(sifZaposlenik),
  FOREIGN KEY (sifVrNastPred) REFERENCES PredmetVN(sifVrNastPred),
  FOREIGN KEY (sifAkGodina) REFERENCES AkGodina(sifAkGodina),
  CONSTRAINT chkUkSati CHECK (ukSati BETWEEN 1.0 AND 30.0)
);

