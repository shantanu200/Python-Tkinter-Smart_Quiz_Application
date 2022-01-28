-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 28, 2022 at 11:37 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python`
--

-- --------------------------------------------------------

--
-- Table structure for table `add_data`
--

CREATE TABLE `add_data` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  `time` time NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `add_data`
--

INSERT INTO `add_data` (`id`, `username`, `email`, `password`, `date`, `time`) VALUES
(1, 'Shantanu16', 'shantanu16@gmail.com', '12010490', '2022-01-25', '20:29:05'),
(2, 'Aditya', 'aditya123@gmail.com', 'aditya', '2022-01-27', '12:32:17'),
(3, 'Sanskar', 'sanskar123@gmail.com', 'sanskar', '2022-01-27', '12:33:06'),
(4, 'Mayur', 'mayur123@gmail.com', 'mayur', '2022-01-27', '12:33:57'),
(5, 'admin', 'admin@gmail.com', 'admin', '2022-01-27', '23:26:26'),
(6, 'new_user', 'new_user@gmail.com', 'newuser', '2022-01-28', '16:02:50');

-- --------------------------------------------------------

--
-- Table structure for table `hard_quiz`
--

CREATE TABLE `hard_quiz` (
  `num` int(11) NOT NULL,
  `question` text NOT NULL,
  `option1` text NOT NULL,
  `option2` text NOT NULL,
  `option3` text NOT NULL,
  `option4` text NOT NULL,
  `answer` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hard_quiz`
--

INSERT INTO `hard_quiz` (`num`, `question`, `option1`, `option2`, `option3`, `option4`, `answer`) VALUES
(3, 'Indus river originates in –', 'Kinnaur', 'Ladakh', 'Nepal', 'Tibet', '4'),
(4, 'Which of the following is not a nuclear power center?', 'Narora', 'Kota', 'Chamera', 'Kakrapara', '3'),
(5, 'Gravity setting chambers are used in industries to remove', 'NOx', 'SOx', 'CO', 'suspended particulate matter', '4'),
(6, 'First Afghan War took place in', '1839', '1848', '1843', '1833', '1'),
(7, 'Guwahati High Court is the judicature of', 'Assam', 'Nagaland', 'Arunachal Pradesh', 'All of the above', '4');

-- --------------------------------------------------------

--
-- Table structure for table `medium_quiz`
--

CREATE TABLE `medium_quiz` (
  `num` int(11) NOT NULL,
  `question` text NOT NULL,
  `option1` text NOT NULL,
  `option2` text NOT NULL,
  `option3` text NOT NULL,
  `option4` text NOT NULL,
  `answer` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medium_quiz`
--

INSERT INTO `medium_quiz` (`num`, `question`, `option1`, `option2`, `option3`, `option4`, `answer`) VALUES
(1, 'The Central Rice Research Station is situated in?', ' Chennai', 'Cuttack', 'Bangalore', 'Quilon', '2'),
(2, 'The metal whose salts are sensitive to light is?', 'Zinc', 'Silver', 'Copper', 'Aluminum', '2'),
(3, 'The country that has the highest in Barley Production?', 'China', 'India', 'Russia', 'France', '3'),
(4, 'Tsunamis are not caused by', 'Hurricanes', 'Earthquakes', 'Undersea landslides', 'Volcanic eruptions', '1'),
(8, 'D.D.T. was invented by?', 'Mosley', 'Rudolf', 'Karl Benz', 'Dalton', '1'),
(9, 'Where was the electricity supply first introduced in India –', 'Mumbai', 'Dehradun', 'Darjeeling', 'Chennai', '3'),
(10, 'Which peninsular river is least seasonal in flow?', 'Narmada', 'Krishna', 'Godavari', 'Cauvery', '3');

-- --------------------------------------------------------

--
-- Table structure for table `score_user`
--

CREATE TABLE `score_user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `score` int(11) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  `time` time NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `score_user`
--

INSERT INTO `score_user` (`id`, `username`, `score`, `date`, `time`) VALUES
(8, 'Shantanu16', 24, '2022-01-28', '15:46:46'),
(9, 'Shantanu16', 0, '2022-01-28', '15:47:13'),
(10, 'Shantanu16', 24, '2022-01-28', '15:48:45'),
(11, 'Shantanu16', 0, '2022-01-28', '16:01:37');

-- --------------------------------------------------------

--
-- Table structure for table `smart_quiz`
--

CREATE TABLE `smart_quiz` (
  `num` int(11) NOT NULL,
  `question` text NOT NULL,
  `option1` text NOT NULL,
  `option2` text NOT NULL,
  `option3` text NOT NULL,
  `option4` text NOT NULL,
  `answer` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `smart_quiz`
--

INSERT INTO `smart_quiz` (`num`, `question`, `option1`, `option2`, `option3`, `option4`, `answer`) VALUES
(1, 'What is Your name?', 'Shantanu', 'Mayur', 'Ajay', 'Ramesh', '1'),
(2, 'What is Your age?', '10', '20', '19', '30', '3'),
(3, 'What is your favourite sport?', 'Cricket', 'Football', 'Hockey', 'Tennis', '1'),
(4, 'Which Programming You like most?', 'C++', 'Java', 'Python', 'JavaScript', '1'),
(5, 'What is Your Keyboard', 'Hyperx', 'Asus', 'Logitech', 'Razer', '1'),
(6, 'Chambal river is a part of –', 'Sabarmati basin', 'Ganga basin', 'Narmada basin', 'Godavari basin', '3');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `add_data`
--
ALTER TABLE `add_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hard_quiz`
--
ALTER TABLE `hard_quiz`
  ADD PRIMARY KEY (`num`);

--
-- Indexes for table `medium_quiz`
--
ALTER TABLE `medium_quiz`
  ADD PRIMARY KEY (`num`);

--
-- Indexes for table `score_user`
--
ALTER TABLE `score_user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `smart_quiz`
--
ALTER TABLE `smart_quiz`
  ADD PRIMARY KEY (`num`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `add_data`
--
ALTER TABLE `add_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `hard_quiz`
--
ALTER TABLE `hard_quiz`
  MODIFY `num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `medium_quiz`
--
ALTER TABLE `medium_quiz`
  MODIFY `num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `score_user`
--
ALTER TABLE `score_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `smart_quiz`
--
ALTER TABLE `smart_quiz`
  MODIFY `num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
