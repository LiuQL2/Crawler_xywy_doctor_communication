/*
Navicat MySQL Data Transfer

Source Server         : Qianlong
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : xywy_communication

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-12-13 12:11:06
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for case_experience_comment_first
-- ----------------------------
DROP TABLE IF EXISTS `case_experience_comment_first`;
CREATE TABLE `case_experience_comment_first` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `post_url` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '评论话题的URL',
  `doctor_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '评论医生链接',
  `comment_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '评论时间',
  `comment_content` text COLLATE utf8_bin COMMENT '评论内容',
  `crawl_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '抓取时间',
  PRIMARY KEY (`comment_id`),
  KEY `topic_url` (`post_url`),
  CONSTRAINT `topic_url` FOREIGN KEY (`post_url`) REFERENCES `case_experience_post` (`post_url`)
) ENGINE=InnoDB AUTO_INCREMENT=44389 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
