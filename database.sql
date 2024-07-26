/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3306
 Source Schema         : 数据库大作业

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 15/12/2023 16:30:37
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin_login_k
-- ----------------------------
DROP TABLE IF EXISTS `admin_login_k`;
CREATE TABLE `admin_login_k` (
  `admin_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `admin_pass` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`admin_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of admin_login_k
-- ----------------------------
BEGIN;
INSERT INTO `admin_login_k` VALUES ('admin', 'admin');
COMMIT;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `CNO` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `CNAME` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `CCREDIT` smallint DEFAULT NULL,
  `CTEACHER` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`CNO`) USING BTREE,
  KEY `CTEACHER` (`CTEACHER`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of course
-- ----------------------------
BEGIN;
INSERT INTO `course` VALUES ('1', '数据库', 4, '徐志强');
INSERT INTO `course` VALUES ('2', '数学', 2, '张浩');
INSERT INTO `course` VALUES ('3', '信息系统', 4, '汤姆');
INSERT INTO `course` VALUES ('4', '操作系统', 3, '徐志强');
INSERT INTO `course` VALUES ('5', '数据结构', 4, '山姆');
INSERT INTO `course` VALUES ('6', '数据处理', 2, '汤姆');
INSERT INTO `course` VALUES ('7', 'PASCAL语言', 4, '山姆');
COMMIT;

-- ----------------------------
-- Table structure for s_course
-- ----------------------------
DROP TABLE IF EXISTS `s_course`;
CREATE TABLE `s_course` (
  `SNO` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `CNO` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `GRADE` smallint DEFAULT NULL,
  KEY `SNO` (`SNO`) USING BTREE,
  KEY `CNO` (`CNO`) USING BTREE,
  CONSTRAINT `s_course_ibfk_1` FOREIGN KEY (`SNO`) REFERENCES `student_k` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `s_course_ibfk_2` FOREIGN KEY (`CNO`) REFERENCES `course` (`CNO`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of s_course
-- ----------------------------
BEGIN;
INSERT INTO `s_course` VALUES ('201215121', '1', 99);
INSERT INTO `s_course` VALUES ('201215121', '2', 99);
INSERT INTO `s_course` VALUES ('201215121', '3', 88);
INSERT INTO `s_course` VALUES ('201215122', '1', 90);
COMMIT;

-- ----------------------------
-- Table structure for stu_login_k
-- ----------------------------
DROP TABLE IF EXISTS `stu_login_k`;
CREATE TABLE `stu_login_k` (
  `stu_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stu_pass` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`stu_id`) USING BTREE,
  CONSTRAINT `stu_login_k_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `student_k` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of stu_login_k
-- ----------------------------
BEGIN;
INSERT INTO `stu_login_k` VALUES ('201215120', '123456');
INSERT INTO `stu_login_k` VALUES ('201215121', '123456');
INSERT INTO `stu_login_k` VALUES ('201215122', '123456');
INSERT INTO `stu_login_k` VALUES ('201215123', '123456');
INSERT INTO `stu_login_k` VALUES ('201215124', '123456');
COMMIT;

-- ----------------------------
-- Table structure for student_k
-- ----------------------------
DROP TABLE IF EXISTS `student_k`;
CREATE TABLE `student_k` (
  `id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `gender` char(5) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `age` smallint DEFAULT NULL,
  `dept` char(5) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of student_k
-- ----------------------------
BEGIN;
INSERT INTO `student_k` VALUES ('201215120', '李勇f', '男', 20, 'CS');
INSERT INTO `student_k` VALUES ('201215121', '李勇', '男', 20, 'CS');
INSERT INTO `student_k` VALUES ('201215122', '刘晨', '女', 19, 'CS');
INSERT INTO `student_k` VALUES ('201215123', '王敏', '女', 18, 'MA');
INSERT INTO `student_k` VALUES ('201215124', '张立', '男', 19, 'IS');
COMMIT;

-- ----------------------------
-- Table structure for tea_login_k
-- ----------------------------
DROP TABLE IF EXISTS `tea_login_k`;
CREATE TABLE `tea_login_k` (
  `tea_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tea_pass` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`tea_id`) USING BTREE,
  CONSTRAINT `tea_login_k_ibfk_1` FOREIGN KEY (`tea_id`) REFERENCES `teacher_k` (`tea_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of tea_login_k
-- ----------------------------
BEGIN;
INSERT INTO `tea_login_k` VALUES ('19001', '123456');
INSERT INTO `tea_login_k` VALUES ('19002', '123456');
INSERT INTO `tea_login_k` VALUES ('19003', '123456');
INSERT INTO `tea_login_k` VALUES ('19004', '123456');
COMMIT;

-- ----------------------------
-- Table structure for teacher_k
-- ----------------------------
DROP TABLE IF EXISTS `teacher_k`;
CREATE TABLE `teacher_k` (
  `tea_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tea_name` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `tea_gender` char(5) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `tea_age` smallint DEFAULT NULL,
  `tea_dept` char(5) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`tea_id`) USING BTREE,
  KEY `tea_name` (`tea_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teacher_k
-- ----------------------------
BEGIN;
INSERT INTO `teacher_k` VALUES ('19001', '徐志强', '男', 41, 'CS');
INSERT INTO `teacher_k` VALUES ('19002', '张浩', '男', 51, 'MA');
INSERT INTO `teacher_k` VALUES ('19003', '汤姆', '男', 33, 'CS');
INSERT INTO `teacher_k` VALUES ('19004', '山姆', '女', 43, 'IS');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
