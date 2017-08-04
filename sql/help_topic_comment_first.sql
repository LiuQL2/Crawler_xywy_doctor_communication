/*
Navicat MySQL Data Transfer

Source Server         : wla-xywy
Source Server Version : 50716
Source Host           : 192.168.139.100:3306
Source Database       : xywy

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-12-22 14:57:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for help_topic_comment_first
-- ----------------------------
DROP TABLE IF EXISTS `help_topic_comment_first`;
CREATE TABLE `help_topic_comment_first` (
  `post_url` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '评论话题的URL',
  `doctor_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '评论医生链接',
  `comment_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '评论时间',
  `comment_content` text COLLATE utf8_bin COMMENT '评论内容',
  `crawl_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '抓取时间',
  `crawl_number` int(11) NOT NULL COMMENT '抓取次数',
  KEY `post_url` (`post_url`),
  CONSTRAINT `help_topic_comment_first_ibfk_1` FOREIGN KEY (`post_url`) REFERENCES `help_topic_post` (`post_url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
