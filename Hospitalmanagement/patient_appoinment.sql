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
-- Table structure for table `patient_appoinment`
--

CREATE TABLE IF NOT EXISTS `patient_appoinment` (
  `id` varchar(30) NOT NULL,
  `patient_name` varchar(30) NOT NULL,
  `gender` varchar(30) NOT NULL,
  `SelectDate` varchar(30) NOT NULL,
  `appt` varchar(30) NOT NULL,
  `Doctors_name` varchar(30) NOT NULL,
  `Symptoms` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient_appoinment`
--

INSERT INTO `patient_appoinment` (`id`, `patient_name`, `gender`, `SelectDate`, `appt`, `Doctors_name`, `Symptoms`) VALUES
('', 'priya', 'female', '2021-04-02', '11:55', '0', ''),
('', 'sss', 'female', '2021-04-10', '14:02', '0', ''),
('', 'saritha', 'female', '2021-04-02', '09:24', '0', ''),
('', 'vikrnt', 'male', '2021-05-05', '11:07', '0', ''),
('', 'saritha', 'female', '2021-05-06', '12:15', '0', ''),
('', 'vikki', 'male', '2021-05-11', '16:25', '0', ''),
('', 'priya', 'female', '2021-05-06', '16:26', '0', ''),
('', 'saritha', 'female', '2021-05-05', '16:30', '0', ''),
('', 'saritha', 'female', '2021-05-13', '17:31', '0', ''),
('', 'roja', 'female', '2021-05-08', '15:33', '0', ''),
('', 'alex', 'male', '2021-05-20', '17:36', '0', 'Liver'),
('', 'alexa', 'female', '2021-05-28', '16:40', 'Dr.Varma', 'fever'),
('', 'saritha', 'female', '2021-04-29', '18:00', 'Dr.Varma', 'Cardio'),
('', 'saritha', 'female', '2021-05-14', '09:02', 'Dr.Varma', 'Cardio'),
('1', 'saritha', 'female', '2021-05-05', '13:09', 'Dr.Varma', 'Cardio'),
('7', 'vikki', 'female', '2021-05-13', '11:10', 'Dr.Varma', 'Liver'),
('5', 'vikrnt', 'male', '2021-05-07', '10:24', 'sangeetha', 'Liver');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
