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
-- Table structure for table `doctor_details`
--

CREATE TABLE IF NOT EXISTS `doctor_details` (
  `id` varchar(30) NOT NULL,
  `Doctors_name` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor_details`
--

INSERT INTO `doctor_details` (`id`, `Doctors_name`, `password`) VALUES
('', 'vivek', '147'),
('', 'chitra', '123'),
('', 'john', '1234'),
('', 'chitra', '1254'),
('', 'kala', '147'),
('', 'Ram', '147'),
('', 'saritha', '12'),
('', 'johnsubash', '741'),
('', 'Dr.Varma', '123'),
('', 'Dr.Varma', '1247'),
('', 'ddddd', 'dddd'),
('', 'Dr.Varma', '123'),
('', 'johnsubash', '117'),
('', 'saritha', '147'),
('', 'johnsubash', '147'),
('7', 'sangee', '123'),
('53', 'johnsubash', '123'),
('72', 'sangeetha', '123');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
