/*
Navicat MySQL Data Transfer

Source Server         : Qianlong
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : xywy_communication

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-12-04 23:03:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for help_topic_comment_second
-- ----------------------------
DROP TABLE IF EXISTS `help_topic_comment_second`;
CREATE TABLE `help_topic_comment_second` (
  `post_url` varchar(255) COLLATE utf8_bin NOT NULL,
  `parent_comment_comment_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '父评论的评论时间',
  `parent_comment_crawl_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '父评论的抓取时间',
  `parent_comment_doctor_url` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '父评论的医生链接',
  `parent_comment_content` text COLLATE utf8_bin COMMENT '父评论的内容',
  `reply_to_doctor` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '被回复的医生链接',
  `reply_doctor` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '回复医生的链接',
  `reply_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '回复时间',
  `reply_content` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `sequence` int(255) NOT NULL COMMENT '在上条评论下回复的顺序',
  `crawl_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '抓取时间',
  PRIMARY KEY (`post_url`,`parent_comment_comment_time`,`parent_comment_doctor_url`,`parent_comment_crawl_time`,`sequence`),
  KEY `parent_comment_id` (`parent_comment_doctor_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
