/*
Navicat MySQL Data Transfer

Source Server         : Qianlong
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : xywy_communication

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-12-13 12:11:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for case_experience_comment_second
-- ----------------------------
DROP TABLE IF EXISTS `case_experience_comment_second`;
CREATE TABLE `case_experience_comment_second` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_comment_id` int(11) NOT NULL COMMENT '该二级评论对应的一级评论id',
  `post_url` varchar(255) COLLATE utf8_bin NOT NULL,
  `reply_to_doctor` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '被回复的医生链接',
  `reply_doctor` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '回复医生的链接',
  `reply_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '回复时间',
  `reply_content` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `sequence` int(255) NOT NULL COMMENT '在上条评论下回复的顺序',
  `crawl_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '抓取时间',
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=779 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
