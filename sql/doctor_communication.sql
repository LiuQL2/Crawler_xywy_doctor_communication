/*
Navicat MySQL Data Transfer

Source Server         : Qianlong
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : xywy_communication

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-12-13 12:28:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for doctor_communication
-- ----------------------------
DROP TABLE IF EXISTS `doctor_communication`;
CREATE TABLE `doctor_communication` (
  `doctor_url` varchar(255) COLLATE utf8_bin NOT NULL,
  `attention_number` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `fans_number` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `web_number` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `crawl_time` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`doctor_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
