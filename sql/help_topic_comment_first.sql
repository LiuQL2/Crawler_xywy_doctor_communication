/*
Navicat MySQL Data Transfer

Source Server         : Qianlong
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : xywy_communication

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-12-04 23:03:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for help_topic_comment_first
-- ----------------------------
DROP TABLE IF EXISTS `help_topic_comment_first`;
CREATE TABLE `help_topic_comment_first` (
  `post_url` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '评论话题的URL',
  `doctor_url` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '评论医生链接',
  `comment_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '评论时间',
  `comment_content` text COLLATE utf8_bin COMMENT '评论内容',
  `crawl_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '抓取时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
