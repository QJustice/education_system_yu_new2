/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 test202012 的数据库结构
CREATE DATABASE IF NOT EXISTS `student2022` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `student2022`;

-- 导出  表 student2022.allmessage 结构
CREATE TABLE IF NOT EXISTS `allmessage` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `MsgLevel` tinyint(4) NOT NULL,
  `SenderNo` varchar(5) NOT NULL,
  `SenderName` varchar(20) DEFAULT NULL,
  `SendTime` datetime DEFAULT NULL,
  `Title` tinytext NOT NULL,
  `Content` text,
  `statu` char(4) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  student2022.allmessage 的数据：~1 rows (大约)
DELETE FROM `allmessage`;
/*!40000 ALTER TABLE `allmessage` DISABLE KEYS */;
INSERT INTO `allmessage` (`Id`, `MsgLevel`, `SenderNo`, `SenderName`, `SendTime`, `Title`, `Content`, `statu`) VALUES
	(1, 1, '2030', 'xiaowang', '2020-02-02 00:00:00', 'A', NULL, '2030');
/*!40000 ALTER TABLE `allmessage` ENABLE KEYS */;

-- 导出  表 student2022.defaultpassword 结构
CREATE TABLE IF NOT EXISTS `defaultpassword` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `AccountLevel` tinyint(4) NOT NULL,
  `Password` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 正在导出表  student2022.defaultpassword 的数据：~3 rows (大约)
DELETE FROM `defaultpassword`;
/*!40000 ALTER TABLE `defaultpassword` DISABLE KEYS */;
INSERT INTO `defaultpassword` (`Id`, `AccountLevel`, `Password`) VALUES
	(1, 0, '123456'),
	(2, 1, '123456'),
	(3, 2, '123456');
/*!40000 ALTER TABLE `defaultpassword` ENABLE KEYS */;

-- 导出  表 student2022.lessoninfo 结构
CREATE TABLE IF NOT EXISTS `lessoninfo` (
  `lesNo` varchar(10) NOT NULL,
  `lesName` varchar(20) DEFAULT NULL,
  `TeacherNo` varchar(10) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `classRoom` varchar(20) NOT NULL,
  PRIMARY KEY (`lesNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  student2022.lessoninfo 的数据：~3 rows (大约)
DELETE FROM `lessoninfo`;
/*!40000 ALTER TABLE `lessoninfo` DISABLE KEYS */;
INSERT INTO `lessoninfo` (`lesNo`, `lesName`, `TeacherNo`, `date`, `classRoom`) VALUES
	('002', 'db', '20022', NULL, 'c203'),
	('003', 'python', '20021', NULL, 'b306'),
	('1001', 'asd', '20021', '2020-12-07 21:14:14', 'A201');
/*!40000 ALTER TABLE `lessoninfo` ENABLE KEYS */;

-- 导出  表 student2022.loginaccount 结构
CREATE TABLE IF NOT EXISTS `loginaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Account` varchar(12) NOT NULL,
  `Password` varchar(12) DEFAULT NULL,
  `AccountLevel` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- 正在导出表  student2022.loginaccount 的数据：~7 rows (大约)
DELETE FROM `loginaccount`;
/*!40000 ALTER TABLE `loginaccount` DISABLE KEYS */;
INSERT INTO `loginaccount` (`id`, `Account`, `Password`, `AccountLevel`) VALUES
	(1, '200214006', '123456', 0),
	(2, '20022', '123456', 1),
	(3, '202004', '123456', 2),
	(4, '202001', '444444', 2),
	(5, '202005', '123456', 2),
	(6, '200214007', '123456', 1),
	(7, '202006', '123456', 2);
/*!40000 ALTER TABLE `loginaccount` ENABLE KEYS */;

-- 导出  表 student2022.positionlist 结构
CREATE TABLE IF NOT EXISTS `positionlist` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `PositionNo` tinyint(4) NOT NULL,
  `PositionName` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 正在导出表  student2022.positionlist 的数据：~3 rows (大约)
DELETE FROM `positionlist`;
/*!40000 ALTER TABLE `positionlist` DISABLE KEYS */;
INSERT INTO `positionlist` (`Id`, `PositionNo`, `PositionName`) VALUES
	(1, 0, 'headmaster'),
	(2, 1, 'professor'),
	(3, 2, 'teacher');
/*!40000 ALTER TABLE `positionlist` ENABLE KEYS */;

-- 导出  表 student2022.stchoose 结构
CREATE TABLE IF NOT EXISTS `stchoose` (
  `StudentNo` varchar(10) NOT NULL,
  `lesNo` varchar(10) DEFAULT NULL,
  `score` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  student2022.stchoose 的数据：~11 rows (大约)
DELETE FROM `stchoose`;
/*!40000 ALTER TABLE `stchoose` DISABLE KEYS */;
INSERT INTO `stchoose` (`StudentNo`, `lesNo`, `score`) VALUES
	('202001', '001', 99),
	('202001', '001', 99),
	('202001', '001', 99),
	('202001', '001', 99),
	('202001', '001', 99),
	('202001', '001', 99),
	('202001', '001', 99),
	('202001', '001', 99),
	('202001', '002', NULL),
	('202001', '003', NULL),
	('202001', '002', NULL);
/*!40000 ALTER TABLE `stchoose` ENABLE KEYS */;

-- 导出  表 student2022.studentinfo 结构
CREATE TABLE IF NOT EXISTS `studentinfo` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) NOT NULL,
  `Gender` varchar(5) NOT NULL,
  `StudentNo` varchar(12) NOT NULL,
  `Birth` date DEFAULT NULL,
  `Academy` varchar(20) NOT NULL,
  `TeacherNo` varchar(5) DEFAULT NULL,
  `Major` varchar(20) NOT NULL,
  `Grade` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `StudentNo` (`StudentNo`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- 正在导出表  student2022.studentinfo 的数据：~6 rows (大约)
DELETE FROM `studentinfo`;
/*!40000 ALTER TABLE `studentinfo` DISABLE KEYS */;
INSERT INTO `studentinfo` (`Id`, `Name`, `Gender`, `StudentNo`, `Birth`, `Academy`, `TeacherNo`, `Major`, `Grade`) VALUES
	(1, 'wuyanzu', 'm', '202001', '2000-04-07', 'zzz', '20021', 'xxx', '88'),
	(2, 'wangqianyuan', 'm', '202002', '2000-03-03', 'zzz', '20021', 'xxx', '78'),
	(3, 'liudehua', 'fm', '202003', '2000-05-06', 'zzz', '20021', 'xxx', '98'),
	(4, 'yiyangqianxi', 'm', '202004', '2000-11-26', 'zzz', '20022', 'xxx', '99'),
	(5, 'cyckabylt', 'fm', '202005', '2000-01-02', 'zzz', '20021', 'xxx', '88'),
	(6, 'xiaolaji', 'm', '202006', '1999-05-08', 'zzz', '20022', 'xxx', '78');
/*!40000 ALTER TABLE `studentinfo` ENABLE KEYS */;

-- 导出  表 student2022.teacherinfo 结构
CREATE TABLE IF NOT EXISTS `teacherinfo` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) NOT NULL,
  `TeacherNo` varchar(5) NOT NULL,
  `Gender` varchar(5) NOT NULL,
  `Birth` date DEFAULT NULL,
  `PositionNo` int(11) DEFAULT NULL,
  `Salary` double DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `TeacherNo` (`TeacherNo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 正在导出表  student2022.teacherinfo 的数据：~3 rows (大约)
DELETE FROM `teacherinfo`;
/*!40000 ALTER TABLE `teacherinfo` DISABLE KEYS */;
INSERT INTO `teacherinfo` (`Id`, `Name`, `TeacherNo`, `Gender`, `Birth`, `PositionNo`, `Salary`) VALUES
	(1, 'chenglong', '20021', 'm', '1975-06-07', 2, 3000),
	(2, 'ss', '20022', 'm', '1999-09-09', 2, 3000),
	(3, 'wangwu', '20023', 'fm', '1989-11-30', 1, 5000);
/*!40000 ALTER TABLE `teacherinfo` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
