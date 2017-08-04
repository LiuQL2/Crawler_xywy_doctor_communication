/*
Navicat MySQL Data Transfer

Source Server         : wla-xywy
Source Server Version : 50716
Source Host           : 192.168.139.100:3306
Source Database       : xywy

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-12-22 14:56:20
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for case_experience_comment_first
-- ----------------------------
DROP TABLE IF EXISTS `case_experience_comment_first`;
CREATE TABLE `case_experience_comment_first` (
  `post_url` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '评论话题的URL',
  `doctor_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '评论医生链接',
  `comment_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '评论时间',
  `comment_content` text COLLATE utf8_bin COMMENT '评论内容',
  `crawl_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '抓取时间',
  `crawl_number` int(11) NOT NULL COMMENT '第几次抓取',
  KEY `topic_url` (`post_url`),
  CONSTRAINT `topic_url` FOREIGN KEY (`post_url`) REFERENCES `case_experience_post` (`post_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
