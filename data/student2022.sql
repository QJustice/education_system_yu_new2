/*
 Navicat Premium Data Transfer

 Source Server         : Ascetic
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : localhost:3306
 Source Schema         : student2022

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 23/11/2022 15:29:38
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for allmessage
-- ----------------------------
DROP TABLE IF EXISTS `allmessage`;
CREATE TABLE `allmessage`  (
  `Id` int NOT NULL AUTO_INCREMENT,
  `MsgLevel` tinyint NOT NULL,
  `SenderNo` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `SenderName` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `SendTime` datetime NULL DEFAULT NULL,
  `Title` tinytext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Content` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `statu` char(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`Id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of allmessage
-- ----------------------------
INSERT INTO `allmessage` VALUES (1, 1, '2030', 'xiaowang', '2020-02-02 00:00:00', 'A', NULL, '2030');

-- ----------------------------
-- Table structure for defaultpassword
-- ----------------------------
DROP TABLE IF EXISTS `defaultpassword`;
CREATE TABLE `defaultpassword`  (
  `Id` int NOT NULL AUTO_INCREMENT,
  `AccountLevel` tinyint NOT NULL,
  `Password` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`Id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of defaultpassword
-- ----------------------------
INSERT INTO `defaultpassword` VALUES (1, 0, '123456');
INSERT INTO `defaultpassword` VALUES (2, 1, '123456');
INSERT INTO `defaultpassword` VALUES (3, 2, '123456');

-- ----------------------------
-- Table structure for lessoninfo
-- ----------------------------
DROP TABLE IF EXISTS `lessoninfo`;
CREATE TABLE `lessoninfo`  (
  `lesNo` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `lesName` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `TeacherNo` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `date` datetime NULL DEFAULT NULL,
  `classRoom` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`lesNo`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lessoninfo
-- ----------------------------
INSERT INTO `lessoninfo` VALUES ('001', 'Math', '20022', '2022-11-18 12:33:36', 'MC12');
INSERT INTO `lessoninfo` VALUES ('002', 'English', '20022', NULL, 'c203');
INSERT INTO `lessoninfo` VALUES ('003', 'Python', '20021', NULL, 'b306');
INSERT INTO `lessoninfo` VALUES ('1001', 'asd', '20021', '2020-12-07 21:14:14', 'A201');

-- ----------------------------
-- Table structure for loginaccount
-- ----------------------------
DROP TABLE IF EXISTS `loginaccount`;
CREATE TABLE `loginaccount`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `Account` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Password` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `AccountLevel` tinyint NULL DEFAULT NULL,
  `sname` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 40 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of loginaccount
-- ----------------------------
INSERT INTO `loginaccount` VALUES (1, '200214006', '123456', 0, '');
INSERT INTO `loginaccount` VALUES (2, '20022', '123456', 1, '');
INSERT INTO `loginaccount` VALUES (3, '202004', '123456', 2, '');
INSERT INTO `loginaccount` VALUES (4, '202001', '444444', 2, '');
INSERT INTO `loginaccount` VALUES (5, '202005', '123456', 2, '');
INSERT INTO `loginaccount` VALUES (6, '200214007', '123456', 1, '');
INSERT INTO `loginaccount` VALUES (7, '202006', '123456', 2, '');
INSERT INTO `loginaccount` VALUES (8, '20201103035', '123456', 2, '齐家宝');
INSERT INTO `loginaccount` VALUES (9, '20201103036', '123456', 2, '阿荣娜');
INSERT INTO `loginaccount` VALUES (10, '20201103037', '123456', 2, '亢学良');
INSERT INTO `loginaccount` VALUES (11, '20201103038', '123456', 2, '高圆');
INSERT INTO `loginaccount` VALUES (12, '20201103040', '123456', 2, '李志敏');
INSERT INTO `loginaccount` VALUES (13, '20202103416', '123456', 2, '代红梅');
INSERT INTO `loginaccount` VALUES (14, '20201103041', '123456', 2, '苏日娜');
INSERT INTO `loginaccount` VALUES (15, '20201103042', '123456', 2, '前德门');
INSERT INTO `loginaccount` VALUES (16, '20201103043', '123456', 2, '苏亚');
INSERT INTO `loginaccount` VALUES (17, '20201103044', '123456', 2, '包富民');
INSERT INTO `loginaccount` VALUES (18, '20201103045', '123456', 2, '希日古');
INSERT INTO `loginaccount` VALUES (19, '20201103046', '123456', 2, '高智豪');
INSERT INTO `loginaccount` VALUES (20, '20201103047', '123456', 2, '包那日苏');
INSERT INTO `loginaccount` VALUES (21, '20201103048', '123456', 2, '木森');
INSERT INTO `loginaccount` VALUES (22, '20201103049', '123456', 2, '特日棍');
INSERT INTO `loginaccount` VALUES (23, '20201103050', '123456', 2, '伊德龙');
INSERT INTO `loginaccount` VALUES (24, '20201103051', '123456', 2, '张荣志');
INSERT INTO `loginaccount` VALUES (25, '20201103052', '123456', 2, '德乐黑');
INSERT INTO `loginaccount` VALUES (26, '20201103053', '123456', 2, '都兰');
INSERT INTO `loginaccount` VALUES (27, '20201103054', '123456', 2, '代乌尼尔');
INSERT INTO `loginaccount` VALUES (28, '20201103055', '123456', 2, '白音');
INSERT INTO `loginaccount` VALUES (29, '20201103056', '123456', 2, '敖达木');
INSERT INTO `loginaccount` VALUES (30, '20201103057', '123456', 2, '阿思亚');
INSERT INTO `loginaccount` VALUES (31, '20201103058', '123456', 2, '孟根珠拉');
INSERT INTO `loginaccount` VALUES (32, '20201103059', '123456', 2, '阿拉坦干德尔');
INSERT INTO `loginaccount` VALUES (33, '20201103060', '123456', 2, '勿日鲁格');
INSERT INTO `loginaccount` VALUES (34, '20201103061', '123456', 2, '春燕');
INSERT INTO `loginaccount` VALUES (35, '20201103062', '123456', 2, '乌友坛');
INSERT INTO `loginaccount` VALUES (36, '20201103063', '123456', 2, '东升');
INSERT INTO `loginaccount` VALUES (37, '20201103064', '123456', 2, '柴力干');
INSERT INTO `loginaccount` VALUES (38, '20192104151', '123456', 2, '草要乐');
INSERT INTO `loginaccount` VALUES (39, '20192104154', '123456', 2, '宝巴雅苏拉');

-- ----------------------------
-- Table structure for positionlist
-- ----------------------------
DROP TABLE IF EXISTS `positionlist`;
CREATE TABLE `positionlist`  (
  `Id` int NOT NULL AUTO_INCREMENT,
  `PositionNo` tinyint NOT NULL,
  `PositionName` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`Id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of positionlist
-- ----------------------------
INSERT INTO `positionlist` VALUES (1, 0, 'headmaster');
INSERT INTO `positionlist` VALUES (2, 1, 'professor');
INSERT INTO `positionlist` VALUES (3, 2, 'teacher');

-- ----------------------------
-- Table structure for stchoose
-- ----------------------------
DROP TABLE IF EXISTS `stchoose`;
CREATE TABLE `stchoose`  (
  `StudentNo` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `lesNo` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `score` float NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stchoose
-- ----------------------------
INSERT INTO `stchoose` VALUES ('202001', '001', 99);
INSERT INTO `stchoose` VALUES ('202001', '002', 78);
INSERT INTO `stchoose` VALUES ('202001', '003', 65);
INSERT INTO `stchoose` VALUES ('202001', '002', 56);
INSERT INTO `stchoose` VALUES ('1111', '111', 11);
INSERT INTO `stchoose` VALUES ('1111', '111', 11);
INSERT INTO `stchoose` VALUES ('20201103035', '001', 89);
INSERT INTO `stchoose` VALUES ('20201103036', '001', 67);
INSERT INTO `stchoose` VALUES ('20201103037', '001', 76);
INSERT INTO `stchoose` VALUES ('20201103038', '001', 97);
INSERT INTO `stchoose` VALUES ('20201103039', '001', 76);
INSERT INTO `stchoose` VALUES ('20201103040', '001', 44);
INSERT INTO `stchoose` VALUES ('20201103041', '001', 78);
INSERT INTO `stchoose` VALUES ('20201103042', '001', 67);
INSERT INTO `stchoose` VALUES ('20201103043', '001', 89);
INSERT INTO `stchoose` VALUES ('20201103044', '001', 65);
INSERT INTO `stchoose` VALUES ('20201103045', '001', 98);
INSERT INTO `stchoose` VALUES ('20201103046', '001', 12);
INSERT INTO `stchoose` VALUES ('20201103047', '001', 43);
INSERT INTO `stchoose` VALUES ('20201103048', '001', 98);
INSERT INTO `stchoose` VALUES ('20201103049', '001', 34);
INSERT INTO `stchoose` VALUES ('20201103050', '001', 21);
INSERT INTO `stchoose` VALUES ('20201103051', '001', 98);
INSERT INTO `stchoose` VALUES ('20201103052', '001', 99);
INSERT INTO `stchoose` VALUES ('20201103053', '001', 67);
INSERT INTO `stchoose` VALUES ('20201103054', '001', 78);
INSERT INTO `stchoose` VALUES ('20201103055', '001', 98);
INSERT INTO `stchoose` VALUES ('20201103056', '001', 56);
INSERT INTO `stchoose` VALUES ('20201103057', '001', 67);
INSERT INTO `stchoose` VALUES ('20201103058', '001', 69);
INSERT INTO `stchoose` VALUES ('20201103059', '001', 76);
INSERT INTO `stchoose` VALUES ('20201103060', '001', 74);
INSERT INTO `stchoose` VALUES ('20201103061', '001', 91);
INSERT INTO `stchoose` VALUES ('20201103062', '001', 94);
INSERT INTO `stchoose` VALUES ('20201103063', '001', 89);
INSERT INTO `stchoose` VALUES ('20201103064', '001', 67);
INSERT INTO `stchoose` VALUES ('20201103035', '002', 67);
INSERT INTO `stchoose` VALUES ('20201103036', '002', 98);
INSERT INTO `stchoose` VALUES ('20201103037', '002', 90);
INSERT INTO `stchoose` VALUES ('20201103038', '002', 91);
INSERT INTO `stchoose` VALUES ('20201103039', '002', 32);
INSERT INTO `stchoose` VALUES ('20201103040', '002', 89);
INSERT INTO `stchoose` VALUES ('20201103041', '002', 96);
INSERT INTO `stchoose` VALUES ('20201103042', '002', 78);
INSERT INTO `stchoose` VALUES ('20201103043', '002', 32);
INSERT INTO `stchoose` VALUES ('20201103044', '002', 43);
INSERT INTO `stchoose` VALUES ('20201103045', '002', 78);
INSERT INTO `stchoose` VALUES ('20201103046', '002', 98);
INSERT INTO `stchoose` VALUES ('20201103047', '002', 64);
INSERT INTO `stchoose` VALUES ('20201103048', '002', 34);
INSERT INTO `stchoose` VALUES ('20201103049', '002', 65);
INSERT INTO `stchoose` VALUES ('20201103050', '002', 76);
INSERT INTO `stchoose` VALUES ('20201103051', '002', 87);
INSERT INTO `stchoose` VALUES ('20201103052', '002', 54);
INSERT INTO `stchoose` VALUES ('20201103053', '002', 76);
INSERT INTO `stchoose` VALUES ('20201103054', '002', 65);
INSERT INTO `stchoose` VALUES ('20201103055', '002', 45);
INSERT INTO `stchoose` VALUES ('20201103056', '002', 98);
INSERT INTO `stchoose` VALUES ('20201103057', '002', 23);
INSERT INTO `stchoose` VALUES ('20201103058', '002', 67);
INSERT INTO `stchoose` VALUES ('20201103059', '002', 98);
INSERT INTO `stchoose` VALUES ('20201103060', '002', 34);
INSERT INTO `stchoose` VALUES ('20201103061', '002', 65);
INSERT INTO `stchoose` VALUES ('20201103062', '002', 98);
INSERT INTO `stchoose` VALUES ('20201103063', '002', 67);
INSERT INTO `stchoose` VALUES ('20201103064', '002', 98);
INSERT INTO `stchoose` VALUES ('20201103035', '003', 90);
INSERT INTO `stchoose` VALUES ('20201103036', '003', 91);
INSERT INTO `stchoose` VALUES ('20201103037', '003', 86);
INSERT INTO `stchoose` VALUES ('20201103038', '003', 89);
INSERT INTO `stchoose` VALUES ('20201103039', '003', 65);
INSERT INTO `stchoose` VALUES ('20201103040', '003', 54);
INSERT INTO `stchoose` VALUES ('20201103041', '003', 34);
INSERT INTO `stchoose` VALUES ('20201103042', '003', 76);
INSERT INTO `stchoose` VALUES ('20201103043', '003', 98);
INSERT INTO `stchoose` VALUES ('20201103044', '003', 65);
INSERT INTO `stchoose` VALUES ('20201103045', '003', 67);
INSERT INTO `stchoose` VALUES ('20201103046', '003', 76);
INSERT INTO `stchoose` VALUES ('20201103047', '003', 54);
INSERT INTO `stchoose` VALUES ('20201103048', '003', 76);
INSERT INTO `stchoose` VALUES ('20201103049', '003', 87);
INSERT INTO `stchoose` VALUES ('20201103050', '003', 76);
INSERT INTO `stchoose` VALUES ('20201103051', '003', 98);
INSERT INTO `stchoose` VALUES ('20201103052', '003', 56);
INSERT INTO `stchoose` VALUES ('20201103053', '003', 87);
INSERT INTO `stchoose` VALUES ('20201103054', '003', 71);
INSERT INTO `stchoose` VALUES ('20201103055', '003', 78);
INSERT INTO `stchoose` VALUES ('20201103056', '003', 90);
INSERT INTO `stchoose` VALUES ('20201103057', '003', 98);
INSERT INTO `stchoose` VALUES ('20201103058', '003', 69);
INSERT INTO `stchoose` VALUES ('20201103059', '003', 60);
INSERT INTO `stchoose` VALUES ('20201103060', '003', 59);
INSERT INTO `stchoose` VALUES ('20201103061', '003', 78);
INSERT INTO `stchoose` VALUES ('20201103062', '003', 90);
INSERT INTO `stchoose` VALUES ('20201103063', '003', 58);
INSERT INTO `stchoose` VALUES ('20201103064', '003', 88);

-- ----------------------------
-- Table structure for studentinfo
-- ----------------------------
DROP TABLE IF EXISTS `studentinfo`;
CREATE TABLE `studentinfo`  (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Gender` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `StudentNo` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Birth` date NULL DEFAULT NULL,
  `Academy` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `TeacherNo` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Major` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Grade` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`Id`) USING BTREE,
  UNIQUE INDEX `StudentNo`(`StudentNo`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 41 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studentinfo
-- ----------------------------
INSERT INTO `studentinfo` VALUES (1, 'wuyanzu', 'm', '202001', '2000-04-07', 'zzz', '20021', 'xxx', '66');
INSERT INTO `studentinfo` VALUES (2, 'wangqianyuan', 'm', '202002', '2000-03-03', 'zzz', '20021', 'xxx', '28');
INSERT INTO `studentinfo` VALUES (3, 'liudehua', 'fm', '202003', '2000-05-06', 'zzz', '20021', 'xxx', '40');
INSERT INTO `studentinfo` VALUES (4, 'yiyangqianxi', 'm', '202004', '2000-11-26', 'zzz', '20022', 'xxx', '16');
INSERT INTO `studentinfo` VALUES (5, 'cyckabylt', 'fm', '202005', '2000-01-02', 'zzz', '20021', 'xxx', '60');
INSERT INTO `studentinfo` VALUES (6, 'xiaolaji', 'm', '202006', '1999-05-08', 'zzz', '20022', 'xxx', '50');
INSERT INTO `studentinfo` VALUES (7, '齐家宝', '男', '20201103035', '2001-07-15', 'zzz', '20022', 'xxx', '99');
INSERT INTO `studentinfo` VALUES (8, '阿荣娜', '女', '20201103036', NULL, 'zzz', NULL, 'xxx', '97');
INSERT INTO `studentinfo` VALUES (9, '亢学良', '男', '20201103037', NULL, 'zzz', NULL, 'xxx', '74');
INSERT INTO `studentinfo` VALUES (10, '高圆', '男', '20201103038', NULL, 'zzz', NULL, 'xxx', '82');
INSERT INTO `studentinfo` VALUES (11, '李志敏', '男', '20201103039', NULL, 'zzz', NULL, 'xxx', '85');
INSERT INTO `studentinfo` VALUES (12, '代红梅', '女', '20201103040', NULL, 'zzz', NULL, 'xxx', '78');
INSERT INTO `studentinfo` VALUES (13, '苏日娜', '女', '20201103041', NULL, 'zzz', NULL, 'xxx', '37');
INSERT INTO `studentinfo` VALUES (14, '前德门', '男', '20201103042', NULL, 'zzz', NULL, 'xxx', '50');
INSERT INTO `studentinfo` VALUES (15, '苏亚', '女', '20201103043', NULL, 'zzz', NULL, 'xxx', '38');
INSERT INTO `studentinfo` VALUES (16, '包富民', '男', '20201103044', NULL, 'zzz', NULL, 'xxx', '39');
INSERT INTO `studentinfo` VALUES (17, '希日古', '男', '20201103045', NULL, 'zzz', NULL, 'xxx', '80');
INSERT INTO `studentinfo` VALUES (18, '高智豪', '男', '20201103046', NULL, 'zzz', NULL, 'xxx', '83');
INSERT INTO `studentinfo` VALUES (19, '包那日苏', '男', '20201103047', NULL, 'zzz', NULL, 'xxx', '73');
INSERT INTO `studentinfo` VALUES (20, '木森', '男', '20201103048', NULL, 'zzz', NULL, 'xxx', '19');
INSERT INTO `studentinfo` VALUES (21, '特日棍', '男', '20201103049', NULL, 'zzz', NULL, 'xxx', '72');
INSERT INTO `studentinfo` VALUES (22, '伊德龙', '男', '20201103050', NULL, 'zzz', NULL, 'xxx', '6');
INSERT INTO `studentinfo` VALUES (23, '张荣志', '男', '20201103051', NULL, 'zzz', NULL, 'xxx', '10');
INSERT INTO `studentinfo` VALUES (24, '德乐黑', '男', '20201103052', NULL, 'zzz', NULL, 'xxx', '33');
INSERT INTO `studentinfo` VALUES (25, '都兰', '女', '20201103053', NULL, 'zzz', NULL, 'xxx', '32');
INSERT INTO `studentinfo` VALUES (26, '代乌尼尔', '女', '20201103054', NULL, 'zzz', NULL, 'xxx', '63');
INSERT INTO `studentinfo` VALUES (27, '白音', '男', '20201103055', NULL, 'zzz', NULL, 'xxx', '19');
INSERT INTO `studentinfo` VALUES (28, '敖达木', '男', '20201103056', NULL, 'zzz', NULL, 'xxx', '5');
INSERT INTO `studentinfo` VALUES (29, '阿思亚', '男', '20201103057', NULL, 'zzz', NULL, 'xxx', '68');
INSERT INTO `studentinfo` VALUES (30, '孟根珠拉', '女', '20201103058', NULL, 'zzz', NULL, 'xxx', '23');
INSERT INTO `studentinfo` VALUES (31, '阿拉坦干德尔', '男', '20201103059', NULL, 'zzz', NULL, 'xxx', '10');
INSERT INTO `studentinfo` VALUES (32, '勿日鲁格', '男', '20201103060', NULL, 'zzz', NULL, 'xxx', '81');
INSERT INTO `studentinfo` VALUES (33, '春燕', '女', '20201103061', NULL, 'zzz', NULL, 'xxx', '73');
INSERT INTO `studentinfo` VALUES (34, '乌友坛', '男', '20201103062', NULL, 'zzz', NULL, 'xxx', '24');
INSERT INTO `studentinfo` VALUES (35, '东升', '男', '20201103063', NULL, 'zzz', NULL, 'xxx', '98');
INSERT INTO `studentinfo` VALUES (36, '包苏敦', '男', '20201103064', NULL, 'zzz', NULL, 'xxx', '20');
INSERT INTO `studentinfo` VALUES (37, '柴力干', '男', '20192104117', NULL, 'zzz', NULL, 'xxx', '4');
INSERT INTO `studentinfo` VALUES (38, '草要乐', '男', '20192104151', NULL, 'zzz', NULL, 'xxx', '58');
INSERT INTO `studentinfo` VALUES (39, '宝巴雅苏拉', '男', '20192104154', NULL, 'zzz', NULL, 'xxx', '78');

-- ----------------------------
-- Table structure for teacherinfo
-- ----------------------------
DROP TABLE IF EXISTS `teacherinfo`;
CREATE TABLE `teacherinfo`  (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `TeacherNo` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Gender` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Birth` date NULL DEFAULT NULL,
  `PositionNo` int NULL DEFAULT NULL,
  `Salary` double NULL DEFAULT NULL,
  PRIMARY KEY (`Id`) USING BTREE,
  UNIQUE INDEX `TeacherNo`(`TeacherNo`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacherinfo
-- ----------------------------
INSERT INTO `teacherinfo` VALUES (1, 'chenglong', '20021', 'm', '1975-06-07', 2, 3000);
INSERT INTO `teacherinfo` VALUES (2, 'ss', '20022', 'm', '1999-09-09', 2, 3000);
INSERT INTO `teacherinfo` VALUES (3, 'wangwu', '20023', 'fm', '1989-11-30', 1, 5000);

SET FOREIGN_KEY_CHECKS = 1;
