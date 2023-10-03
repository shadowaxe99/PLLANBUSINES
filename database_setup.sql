CREATE DATABASE business_plan_builder;

USE business_plan_builder;

CREATE TABLE ExecutiveSummary (
    id INT AUTO_INCREMENT,
    content TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE CompanyDescription (
    id INT AUTO_INCREMENT,
    content TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE MarketAnalysis (
    id INT AUTO_INCREMENT,
    content TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE CompetitiveAnalysis (
    id INT AUTO_INCREMENT,
    content TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE OrganizationManagement (
    id INT AUTO_INCREMENT,
    content TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE ProductLineServices (
    id INT AUTO_INCREMENT,
    content TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE MarketingSalesStrategy (
    id INT AUTO_INCREMENT,
    content TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE FundingRequest (
    id INT AUTO_INCREMENT,
    content TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE FinancialProjections (
    id INT AUTO_INCREMENT,
    content TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE Appendix (
    id INT AUTO_INCREMENT,
    content TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE UserFeedback (
    id INT AUTO_INCREMENT,
    rating INT,
    review TEXT,
    PRIMARY KEY (id)
);