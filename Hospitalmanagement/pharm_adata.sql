-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 03, 2021 at 12:59 PM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `pharm_adata`
--

CREATE TABLE IF NOT EXISTS `pharm_adata` (
  `id` varchar(30) NOT NULL,
  `MedicineName` varchar(30) NOT NULL,
  `Availability` varchar(30) NOT NULL,
  `Mfdate` varchar(30) NOT NULL,
  `Remaining` varchar(30) NOT NULL,
  `Exdate` varchar(30) NOT NULL,
  `NeedCount` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pharm_adata`
--

INSERT INTO `pharm_adata` (`id`, `MedicineName`, `Availability`, `Mfdate`, `Remaining`, `Exdate`, `NeedCount`) VALUES
('', 'paracetamol', 'yes', '', 'march2020', '100', 'mrch2025'),
('', 'paracetamol', 'yes', 'mrch2020', '100', 'mrch2025', '120'),
('', 'ASSURANCE', 'NO', 'OUT OF STOCK', 'OUT OF STOCK', 'NO', '1000'),
('', 'ASSURANCE', 'NO', 'OUT OF STOCK', 'OUT OF STOCK', 'NO', '1000'),
('', 'udiliv', 'NO', '12-12-2020', 'no STOCK', '12-12-2030', 'FULL'),
('', 'paracetamol', 'yes', 'mrch2020', '100', 'mrch2025', '120'),
('', 'vicks', 'yes', '12-12-2020', '15', '15-12-2021', 'FULL'),
('3', 'udiliv', 'yes', 'mrch2020', '100', 'mrch2025', '120'),
('120', 'udiliv', 'NO', 'mrch2020', '100', 'mrch2025', 'FULL'),
('5', 'ASSURANCE', 'NO', 'mrch2020', 'no STOCK', 'mrch2025', 'FULL');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
