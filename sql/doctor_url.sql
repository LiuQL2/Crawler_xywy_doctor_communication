/*
Navicat MySQL Data Transfer

Source Server         : wla-xywy
Source Server Version : 50716
Source Host           : 192.168.139.100:3306
Source Database       : xywy

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-12-22 14:56:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for doctor_url
-- ----------------------------
DROP TABLE IF EXISTS `doctor_url`;
CREATE TABLE `doctor_url` (
  `doctor_url` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '医生的网址链接',
  `crawl_number` int(11) NOT NULL,
  `crawl_time` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`doctor_url`,`crawl_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
