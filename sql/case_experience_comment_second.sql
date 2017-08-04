/*
Navicat MySQL Data Transfer

Source Server         : wla-xywy
Source Server Version : 50716
Source Host           : 192.168.139.100:3306
Source Database       : xywy

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-12-22 14:56:30
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for case_experience_comment_second
-- ----------------------------
DROP TABLE IF EXISTS `case_experience_comment_second`;
CREATE TABLE `case_experience_comment_second` (
  `post_url` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '对应的帖子的url',
  `parent_comment_doctor_url` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '对应父评论的评论时间',
  `parent_comment_comment_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '对应父评论的时间',
  `parent_comment_comment_content` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '对应付父评论的内容',
  `reply_to_doctor` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '被回复的医生链接',
  `reply_doctor` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '回复医生的链接',
  `reply_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '回复时间',
  `reply_content` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '回复的内容',
  `sequence` int(255) NOT NULL COMMENT '在上条评论下回复的顺序',
  `crawl_time` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '抓取时间',
  `crawl_number` int(11) NOT NULL COMMENT '第几次抓取'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
