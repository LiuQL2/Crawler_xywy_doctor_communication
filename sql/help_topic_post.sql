/*
Navicat MySQL Data Transfer

Source Server         : wla-xywy
Source Server Version : 50716
Source Host           : 192.168.139.100:3306
Source Database       : xywy

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-12-22 14:57:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for help_topic_post
-- ----------------------------
DROP TABLE IF EXISTS `help_topic_post`;
CREATE TABLE `help_topic_post` (
  `post_url` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '话题的主页链接',
  `post_title` text COLLATE utf8_bin,
  `post_review_number` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '话题浏览人数',
  `post_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '话题发表时间',
  `post_content` longtext COLLATE utf8_bin COMMENT '帖子正文',
  `post_like_number` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '点赞人数',
  `post_comment_number` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '评论人数',
  `post_like_doctor_url` text COLLATE utf8_bin COMMENT '点赞医生的链接，不确保全部',
  `post_comment_doctor_url` text COLLATE utf8_bin COMMENT '评论医生的链接',
  `post_doctor_url` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '发帖医生链接',
  `post_follower_number` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '该帖子的关注人数',
  `post_type` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '帖子类别',
  `crawl_time` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '抓取时间',
  `crawl_number` int(11) NOT NULL COMMENT '抓取次数',
  PRIMARY KEY (`post_url`,`crawl_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
