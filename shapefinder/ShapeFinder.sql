-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 24, 2016 at 01:58 PM
-- Server version: 5.7.12-0ubuntu1
-- PHP Version: 7.0.4-7ubuntu2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ShapeFinder`
--

-- --------------------------------------------------------

--
-- Table structure for table `compte_admin`
--

CREATE TABLE `compte_admin` (
  `idcompte_admin` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `firstname` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `street` varchar(128) DEFAULT NULL,
  `zip` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `login` varchar(128) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  `AccessLevel` int(11) DEFAULT NULL,
  `sceances_IdSceance` int(11) NOT NULL,
  `journal_conn_idjournal_conn` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `IdCustomer` int(11) NOT NULL,
  `company` varchar(45) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `firstname` varchar(45) DEFAULT NULL,
  `street` varchar(45) DEFAULT NULL,
  `zip` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `phone1` varchar(45) DEFAULT NULL,
  `phone2` varchar(45) DEFAULT NULL,
  `title` varchar(45) DEFAULT NULL,
  `payment` varchar(45) DEFAULT NULL,
  `order_idorder` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `issues`
--

CREATE TABLE `issues` (
  `idissues` int(11) NOT NULL,
  `questions` varchar(45) DEFAULT NULL,
  `answer` varchar(45) DEFAULT NULL,
  `geometric shape` varchar(45) DEFAULT NULL,
  `way` varchar(45) DEFAULT NULL,
  `code geometric shape` varchar(45) DEFAULT NULL,
  `points` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `journal_conn`
--

CREATE TABLE `journal_conn` (
  `idjournal_conn` int(11) NOT NULL,
  `DateConn` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `LineOrder`
--

CREATE TABLE `LineOrder` (
  `idLineOrder` int(11) NOT NULL,
  `Description` varchar(100) DEFAULT NULL,
  `IdProduct` int(11) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `PriceWT` float DEFAULT NULL,
  `PriceTax` float DEFAULT NULL,
  `Tax` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `idorder` int(11) NOT NULL,
  `CodeLicenceDemo` varchar(45) DEFAULT NULL,
  `DatePayment` date DEFAULT NULL,
  `paymentYesOrNo` tinyint(1) DEFAULT NULL,
  `LineOrder_idLineOrder` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `IdProduct` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `wording` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `PriceHT` float DEFAULT NULL,
  `PriceTTC` float DEFAULT NULL,
  `path` varchar(45) DEFAULT NULL,
  `draw` varchar(45) DEFAULT NULL,
  `tax` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `sceances`
--

CREATE TABLE `sceances` (
  `IdSceance` int(11) NOT NULL,
  `ObjetSceance` blob,
  `DateDebut` date DEFAULT NULL,
  `HeureDebut` varchar(45) DEFAULT NULL,
  `DateFin` date DEFAULT NULL,
  `HeureFin` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `compte_admin`
--
ALTER TABLE `compte_admin`
  ADD PRIMARY KEY (`idcompte_admin`),
  ADD KEY `fk_compte_admin_sceances_idx` (`sceances_IdSceance`),
  ADD KEY `fk_compte_admin_journal_conn1_idx` (`journal_conn_idjournal_conn`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`IdCustomer`),
  ADD KEY `fk_customer_order1_idx` (`order_idorder`);

--
-- Indexes for table `issues`
--
ALTER TABLE `issues`
  ADD PRIMARY KEY (`idissues`);

--
-- Indexes for table `journal_conn`
--
ALTER TABLE `journal_conn`
  ADD PRIMARY KEY (`idjournal_conn`);

--
-- Indexes for table `LineOrder`
--
ALTER TABLE `LineOrder`
  ADD PRIMARY KEY (`idLineOrder`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`idorder`),
  ADD KEY `fk_order_LineOrder1_idx` (`LineOrder_idLineOrder`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`IdProduct`);

--
-- Indexes for table `sceances`
--
ALTER TABLE `sceances`
  ADD PRIMARY KEY (`IdSceance`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `compte_admin`
--
ALTER TABLE `compte_admin`
  MODIFY `idcompte_admin` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `IdCustomer` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `issues`
--
ALTER TABLE `issues`
  MODIFY `idissues` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `journal_conn`
--
ALTER TABLE `journal_conn`
  MODIFY `idjournal_conn` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `LineOrder`
--
ALTER TABLE `LineOrder`
  MODIFY `idLineOrder` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `idorder` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `IdProduct` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `sceances`
--
ALTER TABLE `sceances`
  MODIFY `IdSceance` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `compte_admin`
--
ALTER TABLE `compte_admin`
  ADD CONSTRAINT `fk_compte_admin_journal_conn1` FOREIGN KEY (`journal_conn_idjournal_conn`) REFERENCES `journal_conn` (`idjournal_conn`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_compte_admin_sceances` FOREIGN KEY (`sceances_IdSceance`) REFERENCES `sceances` (`IdSceance`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `fk_customer_order1` FOREIGN KEY (`order_idorder`) REFERENCES `order` (`idorder`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `fk_order_LineOrder1` FOREIGN KEY (`LineOrder_idLineOrder`) REFERENCES `LineOrder` (`idLineOrder`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
