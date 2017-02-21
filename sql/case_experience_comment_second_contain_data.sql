/*
Navicat MySQL Data Transfer

Source Server         : wla-xywy
Source Server Version : 50716
Source Host           : 192.168.139.100:3306
Source Database       : xywy

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-12-22 14:52:30
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

-- ----------------------------
-- Records of case_experience_comment_second
-- ----------------------------
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/44757', 'http://club.xywy.com/doc_card/65669976', '8个月前', '学习了', 'http://club.xywy.com/doc_card/65669976', 'http://club.xywy.com/doc_card/41907285', '8个月前', '共同学习', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/34054', 'http://club.xywy.com/doc_card/65669976', '2015-11-23', '赞', 'http://club.xywy.com/doc_card/65669976', 'http://club.xywy.com/doc_card/80490243', '2015-12-04', '赞', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/32441', 'http://club.xywy.com/doc_card/74436535', '2015-11-07', '对这位有机磷中毒患者的处理非常及时和正确。有机磷农药中毒，病情发展迅速，抢救必须是分秒必争。对这位患者处理的非常正确和及时。对这位患者要密切注意病情的观察，瞳孔、心率、呼吸、皮肤黏膜情况的变化及有无肌肉震颤的情况，阿托品、解磷定一定要按时应用。及时监测胆碱酯酶的活性。根据胆碱酯酶监测的结果调整胆碱酯酶复活剂药物的用量。', 'http://club.xywy.com/doc_card/74436535', 'http://club.xywy.com/doc_card/54496072', '2015-11-10', '分析的太好了', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/28932', 'http://club.xywy.com/doc_card/63526146', '2015-10-21', '我是十五楼，答对了，为什么没有我啊？', 'http://club.xywy.com/doc_card/63526146', 'http://club.xywy.com/doc_card/55959219', '2015-10-21', '亲，我们的规则是答对医生的第十五层哦，您是全部医生的第十五层，是答对医生的第十二层哦。', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/29164', 'http://club.xywy.com/doc_card/12378254', '2015-10-16', '前途是光明的，道路是曲折的，女住院医，总会有一个欣赏你的人把你娶回家去，然后当宝贝一样呵护的！', 'http://club.xywy.com/doc_card/12378254', 'http://club.xywy.com/doc_card/69527165', '2015-11-04', '是的', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/29164', 'http://club.xywy.com/doc_card/43328226', '2015-10-16', '分析的差不多', 'http://club.xywy.com/doc_card/43328226', 'http://club.xywy.com/doc_card/69527165', '2015-11-04', '肯定的', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/29164', 'http://club.xywy.com/doc_card/70072477', '2015-10-16', '脾气不好', 'http://club.xywy.com/doc_card/70072477', 'http://club.xywy.com/doc_card/69527165', '2015-11-04', '改改', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/29164', 'http://club.xywy.com/doc_card/56009193', '2015-10-15', '此事我不全同意', 'http://club.xywy.com/doc_card/56009193', 'http://club.xywy.com/doc_card/69527165', '2015-11-04', '还请不吝赐教', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/29164', 'http://club.xywy.com/doc_card/74116972', '2015-10-15', '医生本身就是个很辛苦的职业，女性由于在生活中的不同角色决定了女医生更加辛苦。', 'http://club.xywy.com/doc_card/74116972', 'http://club.xywy.com/doc_card/69527165', '2015-11-04', '是的啦', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/27581', 'http://club.xywy.com/doc_card/58104023', '2015-10-09', '什么时候开始的  都不知道', 'http://club.xywy.com/doc_card/58104023', 'http://club.xywy.com/doc_card/54490688', '2015-10-12', '每周三都会有', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/27581', 'http://club.xywy.com/doc_card/63153128', '2015-10-01', '白血病急性发展期、肺部感染、中度贫血。', 'http://club.xywy.com/doc_card/63153128', 'http://club.xywy.com/doc_card/55730299', '2015-10-01', '赞同你的诊断', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/26560', 'http://club.xywy.com/doc_card/53297598', '2015-09-18', '', 'http://club.xywy.com/doc_card/53297598', 'http://club.xywy.com/doc_card/54490688', '2015-09-22', '你没有做出诊断', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/26560', 'http://club.xywy.com/doc_card/53297598', '2015-09-18', '', 'http://club.xywy.com/doc_card/53297598', 'http://club.xywy.com/doc_card/54495400', '2015-09-22', '分析的好全', '2', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/26560', '匿名用户', '2015-09-16', '尿路狭窄   慢性肾盂肾炎急性发作', '匿名用户', 'http://club.xywy.com/doc_card/54490688', '2015-09-22', '为啥用匿名呢怎么颁奖？', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/23379', 'http://club.xywy.com/doc_card/54762926', '2015-08-05', '应该选，AC阑尾炎不可能血尿，排除，尿路感染，不可能有这么重的症状，排除。', 'http://club.xywy.com/doc_card/54762926', 'http://club.xywy.com/doc_card/53251468', '2015-08-05', '肿瘤会出现血尿啊', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/23504', '匿名用户', '2015-08-07', '学习', '匿名用户', 'http://club.xywy.com/doc_card/60624952', '2015-08-08', '', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/22315', 'http://club.xywy.com/doc_card/61253518', '2015-07-28', '胃溃疡', 'http://club.xywy.com/doc_card/61253518', 'http://club.xywy.com/doc_card/60661882', '2015-07-28', '胃窦小弯侧似见约2cm大小龛影，位于胃轮廓内？还有一个是龛影，位于胃轮廓外？一般是胃溃疡跟胃癌的鉴别', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/22315', 'http://club.xywy.com/doc_card/61253518', '2015-07-28', '胃溃疡', 'http://club.xywy.com/doc_card/61253518', 'http://club.xywy.com/doc_card/60661882', '2015-07-28', '胃窦小弯侧似见约2cm大小龛影，位于胃轮廓内？还有一个是龛影，位于胃轮廓外？一般是胃溃疡跟胃癌的鉴别', '2', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/21622', 'http://club.xywy.com/doc_card/54494065', '2015-07-15', '我是来学习的', '匿名用户', 'http://club.xywy.com/doc_card/54494065', '2015-07-15', '尝试诊断一下吧，不然怎么学习呢。。', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/22088', 'http://club.xywy.com/doc_card/53779188', '2015-07-20', '学习了', 'http://club.xywy.com/doc_card/53779188', 'http://club.xywy.com/doc_card/34271964', '2015-07-21', '谢谢。', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/22088', 'http://club.xywy.com/doc_card/12179455', '2015-07-20', '学习了', 'http://club.xywy.com/doc_card/12179455', 'http://club.xywy.com/doc_card/34271964', '2015-07-21', '相互学习。', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/21061', 'http://club.xywy.com/doc_card/13695948', '2015-07-08', '急性肺脓肿，不是结核，一般结核不是高烧', 'http://club.xywy.com/doc_card/13695948', 'http://club.xywy.com/doc_card/53251468', '2015-07-09', '粟粒性结核也会发烧，但是这个患者辅助检查，最有可能和肺脓肿鉴别。', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/20352', 'http://club.xywy.com/doc_card/50551412', '2015-07-01', '没看到治疗', 'http://club.xywy.com/doc_card/50551412', 'http://club.xywy.com/doc_card/60476674', '2015-07-01', '下次分享的', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/19817', 'http://club.xywy.com/doc_card/57385661', '2015-06-28', '腹膜后脂肪肉瘤', 'http://club.xywy.com/doc_card/57385661', 'http://club.xywy.com/doc_card/59087511', '2015-07-01', '佩服', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/19817', 'http://club.xywy.com/doc_card/53251468', '2015-06-28', '病人就是腹膜后肿瘤，累计周围器官，贫血可能考虑累计脾脏', 'http://club.xywy.com/doc_card/59087511', 'http://club.xywy.com/doc_card/53251468', '2015-07-08', '互相学习，其实我工作一直在内科，门诊，急症，外科都没有呆过。还是考职称时看过书。', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/19817', 'http://club.xywy.com/doc_card/53251468', '2015-06-28', '病人就是腹膜后肿瘤，累计周围器官，贫血可能考虑累计脾脏', 'http://club.xywy.com/doc_card/53251468', 'http://club.xywy.com/doc_card/59087511', '2015-07-01', '向老师学习', '2', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/19817', 'http://club.xywy.com/doc_card/53251468', '2015-06-28', '这个病例，病人轻度贫血，并有感染，胰腺良性肿瘤？嗜络细胞瘤？', 'http://club.xywy.com/doc_card/53251468', 'http://club.xywy.com/doc_card/59387916', '2015-06-28', '嗜络细胞瘤一般是长在肾上的吧？', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/15652', 'http://club.xywy.com/doc_card/57777202', '2015-06-04', '美美哒', 'http://club.xywy.com/doc_card/57777202', 'http://club.xywy.com/doc_card/58042412', '2015-06-04', '这是我一个小妹妹。做完漂亮了很多。谢谢评论。', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/15652', 'http://club.xywy.com/doc_card/57777202', '2015-06-04', '美美哒', 'http://club.xywy.com/doc_card/57777202', 'http://club.xywy.com/doc_card/58042412', '2015-06-04', '这是我一个小妹妹。做完漂亮了很多。谢谢评论。', '2', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/15127', 'http://club.xywy.com/doc_card/14480092', '2015-06-01', '根本不是属于腰椎间盘突出。', 'http://club.xywy.com/doc_card/14480092', 'http://club.xywy.com/doc_card/57638037', '2015-06-03', '那请问张老师您诊断为什么病', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/12686', 'http://club.xywy.com/doc_card/54495400', '2015-05-27', '这个比较专业，坐等眼科同仁来回答。', 'http://club.xywy.com/doc_card/54495400', 'http://club.xywy.com/doc_card/52637005', '2015-05-27', '嗯，希望眼科的专家们提供宝贵的意见。', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/10117', 'http://club.xywy.com/doc_card/56039519', '2015-05-20', '有可能是“椎动脉型颈椎病”，可以请康复科医生会诊。', 'http://club.xywy.com/doc_card/57128802', 'http://club.xywy.com/doc_card/56039519', '2015-05-21', '不同阶段的颈椎间盘突出，牵引的角度不同，而且有颈椎管狭窄，建议屈曲位牵引；神经性偏头痛，可以扎“头皮针”；再配合推拿、理疗（微波、磁疗、干扰电等）。个人意见。', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/10117', 'http://club.xywy.com/doc_card/56039519', '2015-05-20', '有可能是“椎动脉型颈椎病”，可以请康复科医生会诊。', 'http://club.xywy.com/doc_card/56039519', 'http://club.xywy.com/doc_card/57128802', '2015-05-21', '针灸，牵引症状加重，', '2', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/10117', 'http://club.xywy.com/doc_card/56039519', '2015-05-20', '有可能是“椎动脉型颈椎病”，可以请康复科医生会诊。', 'http://club.xywy.com/doc_card/53359874', 'http://club.xywy.com/doc_card/56039519', '2015-05-20', '谢谢老师', '3', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/10117', 'http://club.xywy.com/doc_card/56039519', '2015-05-20', '有可能是“椎动脉型颈椎病”，可以请康复科医生会诊。', 'http://club.xywy.com/doc_card/56039519', 'http://club.xywy.com/doc_card/53359874', '2015-05-20', '很专业', '4', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/10117', 'http://club.xywy.com/doc_card/56039519', '2015-05-20', '有可能是“椎动脉型颈椎病”，可以请康复科医生会诊。', 'http://club.xywy.com/doc_card/57128802', 'http://club.xywy.com/doc_card/56039519', '2015-05-20', '患者有颈椎间盘突出，椎管狭窄，而上肢没有任何症状，说明患者上肢神经没有受压迫，臂丛神经牵拉实验应该是阴性，不能考虑“神经根型颈椎病”。患者每次发作首先从颈部逐渐上行，而后向前逐渐发作阵发痉挛性疼痛难忍，家属手按压后略轻，头疼时肌肉僵硬，说明有颈部肌肉和血管痉挛的症状，还有头疼、恶心、呕吐，是“椎动脉型颈椎病”的症状。您已经用了药物治疗，患者同意的情况下，可以试试针灸、推拿、牵引、理疗。以上属个人意见。', '5', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/10117', 'http://club.xywy.com/doc_card/56039519', '2015-05-20', '有可能是“椎动脉型颈椎病”，可以请康复科医生会诊。', 'http://club.xywy.com/doc_card/56039519', 'http://club.xywy.com/doc_card/57128802', '2015-05-20', '颈椎病看似严重一点症状不明显，多年摸索感觉还是典型的神经性头疼，', '6', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/9601', 'http://club.xywy.com/doc_card/56367117', '2015-05-13', '给你点赞！', 'http://club.xywy.com/doc_card/56367117', 'http://club.xywy.com/doc_card/54493031', '2015-05-14', '也是在别的地方看的', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/9130', 'http://club.xywy.com/doc_card/55924883', '2015-05-08', '效果不错', 'http://club.xywy.com/doc_card/55924883', 'http://club.xywy.com/doc_card/24804272', '2015-05-08', '考虑股骨颈应该能够愈合', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/9130', 'http://club.xywy.com/doc_card/56296352', '2015-05-08', '这个不是头下型，且年龄不是很大，愈合的几率还是比较大的。', 'http://club.xywy.com/doc_card/56296352', 'http://club.xywy.com/doc_card/24804272', '2015-05-08', '第一张是伤后拍的，第二张是牵引后拍的！期间拍了3张，骨折对位对线良好与第二张一样', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/9088', 'http://club.xywy.com/doc_card/54041500', '2015-05-07', '可以，很值得。鼓掌！', 'http://club.xywy.com/doc_card/54041500', 'http://club.xywy.com/doc_card/19088510', '2015-05-07', '同样', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/8993', 'http://club.xywy.com/doc_card/53814895', '2015-05-06', '可以学习', 'http://club.xywy.com/doc_card/53814895', 'http://club.xywy.com/doc_card/53715554', '2015-05-06', '看了这篇文章我有了更深的了解学习', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/8991', 'http://club.xywy.com/doc_card/54494065', '2015-05-06', '学习了', 'http://club.xywy.com/doc_card/54494065', 'http://club.xywy.com/doc_card/4772658', '2015-05-06', '恩恩我们会继续努力', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/8286', 'http://club.xywy.com/doc_card/18732252', '2015-04-29', '学习了', '匿名用户', 'http://club.xywy.com/doc_card/18732252', '2015-04-29', '确实很不错', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/8252', 'http://club.xywy.com/doc_card/58124343', '2015-06-07', '这种情况，是不是手术治疗才能根治？', 'http://club.xywy.com/doc_card/58124343', 'http://club.xywy.com/doc_card/42891255', '2015-06-25', '手术治疗还没有达到这程度', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/8252', 'http://club.xywy.com/doc_card/57468866', '2015-06-05', '可以用20%甘露醇125ml快速滴入，再用一组活血改善脑循环的药物。', 'http://club.xywy.com/doc_card/57468866', 'http://club.xywy.com/doc_card/42891255', '2015-06-25', '谢谢指点', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/8252', 'http://club.xywy.com/doc_card/56344099', '2015-05-09', '典型基层处方，要是我还会加一组甲米和钾。', 'http://club.xywy.com/doc_card/56344099', 'http://club.xywy.com/doc_card/42891255', '2015-06-25', '说心里话这种病人我心里想的是尽快转不会给过多药物进行输液', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/8252', 'http://club.xywy.com/doc_card/24804272', '2015-05-01', '两个月前查的结果，不可盲目的相信，凌晨一点出现眩晕剧烈呕吐，家属电话求助出诊，晚上的最好让去大医院，晚上外出输液风险很大的。', 'http://club.xywy.com/doc_card/24804272', 'http://club.xywy.com/doc_card/42891255', '2015-05-01', '谢谢提醒，转院在山区不方便，只有先对症出来，和家属交代病情可能出现的并发症，尽快转诊', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/8252', 'http://club.xywy.com/doc_card/53872979', '2015-04-30', '基层医生不好干啊', 'http://club.xywy.com/doc_card/53872979', 'http://club.xywy.com/doc_card/42891255', '2015-04-30', '是啊 这种病人不是很熟的人是不会给输液的，剧烈的呕吐输个液都带着忐忑的心', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/7481', 'http://club.xywy.com/doc_card/55721340', '2015-05-01', '请问腹痛如何解释？谢谢', 'http://club.xywy.com/doc_card/55721340', 'http://club.xywy.com/doc_card/51938456', '2015-05-06', '1.急性心肌梗死的放射性疼痛，2.儿茶酚胺增多引起胃肠道蠕动减弱+淤血', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/7244', 'http://club.xywy.com/doc_card/54891919', '2015-04-16', '学习了', 'http://club.xywy.com/doc_card/54891919', 'http://club.xywy.com/doc_card/54496988', '2015-04-17', '写的真是不错', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/7053', 'http://club.xywy.com/doc_card/55721340', '2015-05-05', '在哪里妊娠了？', 'http://club.xywy.com/doc_card/55721340', 'http://club.xywy.com/doc_card/53969796', '2015-09-10', '宫内妊娠合并黄体破裂', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/1645', 'http://club.xywy.com/doc_card/58790067', '2015-06-13', '菌必治在早些年不是还有免皮试的么', 'http://club.xywy.com/doc_card/58790067', 'http://club.xywy.com/doc_card/24804272', '2015-06-13', '现在一直都在皮试，皮试就有过敏的，的确少见！', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/1645', 'http://club.xywy.com/doc_card/56348885', '2015-05-24', '我们这也发生一例，头孢曲松钠过敏蛮厉害的', 'http://club.xywy.com/doc_card/56348885', 'http://club.xywy.com/doc_card/24804272', '2015-07-02', '是的吧！真是惊魂未定啊！使我们心惊肉跳啊！', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/1645', 'http://club.xywy.com/doc_card/55721340', '2015-05-05', '学习了', 'http://club.xywy.com/doc_card/55721340', 'http://club.xywy.com/doc_card/24804272', '2015-05-13', '确实难得一见的过敏反应,不过非常吓人的', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/1645', 'http://club.xywy.com/doc_card/53465257', '2015-04-14', '常见难得的一例典型头孢菌素皮试过敏反应，处理及时准确，值得我们加强学习。', 'http://club.xywy.com/doc_card/53465257', 'http://club.xywy.com/doc_card/24804272', '2015-05-10', '过奖了，确实难得一见的过敏反应，使我今生受益', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/1645', 'http://club.xywy.com/doc_card/54762926', '2015-04-12', '曲松现在过敏的人比前几年增加了', 'http://club.xywy.com/doc_card/54762926', 'http://club.xywy.com/doc_card/24804272', '2015-07-02', '你说以前看到别的地方，不用做皮试，他们都是怎么干的，吓死我了', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/1645', 'http://club.xywy.com/doc_card/54424661', '2015-04-11', '处理的很好', 'http://club.xywy.com/doc_card/54424661', 'http://club.xywy.com/doc_card/24804272', '2015-07-02', '谢谢夸奖，其实内心里，非常担心受怕啊！惊魂未定啊', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/6766', 'http://club.xywy.com/doc_card/51058307', '2015-06-26', '请问一多年骨质增生的病人，为什么在吃了前几幅药时没反应，后来继续用药疼痛越来越厉害呢？是好转的情况吗？\n不知道怎么求助，只好发表到这里。\n请前辈指点。谢谢。', 'http://club.xywy.com/doc_card/51058307', 'http://club.xywy.com/doc_card/53946454', '2015-07-19', '这个不好判断，还是要看病人的情况以及具体的药物。主要是看你用药的意图。若是因为不通，采用通的药物，再通早期疼痛，之后就会病情痊愈。', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/6559', 'http://club.xywy.com/doc_card/54061881', '2015-04-07', '不错，得学', 'http://club.xywy.com/doc_card/54061881', 'http://club.xywy.com/doc_card/18732252', '2015-04-07', 'sdag', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/6559', 'http://club.xywy.com/doc_card/54061881', '2015-04-07', '不错，得学', 'http://club.xywy.com/doc_card/54061881', 'http://club.xywy.com/doc_card/18732252', '2015-04-07', 'sdag', '2', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/6475', 'http://club.xywy.com/doc_card/53278780', '2015-03-31', '家长是孩子的领路人', 'http://club.xywy.com/doc_card/53278780', 'http://club.xywy.com/doc_card/4772658', '2015-03-31', 'enheng', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/6475', 'http://club.xywy.com/doc_card/53278780', '2015-03-31', '家长是孩子的领路人', '匿名用户', 'http://club.xywy.com/doc_card/53278780', '2015-03-31', 'asdfasdfasdf', '2', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/5477', 'http://club.xywy.com/doc_card/51270356', '2015-03-06', '中药治疗就是好。', 'http://club.xywy.com/doc_card/51270356', 'http://club.xywy.com/doc_card/42891255', '2015-03-07', '祖国传统中医在医学领域中起着不可限量的功勋', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/5477', 'http://club.xywy.com/doc_card/22919012', '2015-03-05', '可以试用', 'http://club.xywy.com/doc_card/22919012', 'http://club.xywy.com/doc_card/42891255', '2015-03-07', '中医中药治疗往往能起到出乎意料的功效', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/5477', 'http://club.xywy.com/doc_card/22919012', '2015-03-05', '可以试用', 'http://club.xywy.com/doc_card/22919012', 'http://club.xywy.com/doc_card/42891255', '2015-03-07', '中医中药治疗往往能起到出乎意料的功效', '2', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/5477', 'http://club.xywy.com/doc_card/52653446', '2015-03-05', '这就是药方了吧', 'http://club.xywy.com/doc_card/52653446', 'http://club.xywy.com/doc_card/42891255', '2015-03-07', '药方应个体差异和症状随机加减，你懂的', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/4941', 'http://club.xywy.com/doc_card/23100801', '2015-02-04', '尿激酶的作用是什么呢', 'http://club.xywy.com/doc_card/23100801', 'http://club.xywy.com/doc_card/39356003', '2015-02-12', '客气啦  这药一般内科用的多', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/4941', 'http://club.xywy.com/doc_card/23100801', '2015-02-04', '尿激酶的作用是什么呢', 'http://club.xywy.com/doc_card/23100801', 'http://club.xywy.com/doc_card/39356003', '2015-02-11', '尿激酶、链激酶是溶栓药物', '2', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/3816', 'http://club.xywy.com/doc_card/25037115', '2015-01-13', '你的医术不错呀，想讨教青春豆，常是大的粉包了怎么治疗', 'http://club.xywy.com/doc_card/25037115', 'http://club.xywy.com/doc_card/44424588', '2015-01-13', '对于严重结节状的，要加入活血散结之品', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/3552', 'http://club.xywy.com/doc_card/25037115', '2014-12-31', '湿疹确实是一个复杂又反复的顽固的病，一个亲戚以前就是手背患湿疹，痒的难受，常皮疹难下。', 'http://club.xywy.com/doc_card/25037115', 'http://club.xywy.com/doc_card/50130575', '2015-01-04', '建议用中药泡洗，然后再涂药膏，很好的！', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/3552', 'http://club.xywy.com/doc_card/48341141', '2014-12-30', '湿疹的确是多发病，尤其是顽固性湿疹，这个方法值得推广。', 'http://club.xywy.com/doc_card/48341141', 'http://club.xywy.com/doc_card/50130575', '2014-12-30', '谢谢张老师的支持！', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/3196', 'http://club.xywy.com/doc_card/50686218', '2015-01-13', '肠系膜淋巴结炎只要是注意给孩子保暖就会见到效果', 'http://club.xywy.com/doc_card/50686218', 'http://club.xywy.com/doc_card/10164462', '2015-01-16', '谢谢！', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/3196', 'http://club.xywy.com/doc_card/48350943', '2014-12-17', '谢谢', 'http://club.xywy.com/doc_card/48350943', 'http://club.xywy.com/doc_card/10164462', '2014-12-16', '主要是温中止痛的中药，可以自己配制', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/3069', 'http://club.xywy.com/doc_card/48104726', '2014-12-12', '确实是奇迹！', 'http://club.xywy.com/doc_card/48104726', 'http://club.xywy.com/doc_card/38898392', '2014-12-12', '是啊，我们也没有想到，老太太心率经常不到30次/分，还能生存这么长时间。', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/3043', 'http://club.xywy.com/doc_card/45311503', '2014-12-16', '怎么认识呢，留下个QQ行不349411357', 'http://club.xywy.com/doc_card/45311503', 'http://club.xywy.com/doc_card/47318402', '2014-12-16', '当然可以认识了。', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/3043', 'http://club.xywy.com/doc_card/45441467', '2014-12-13', '我们都要积极乐观的经营自己的生活~', 'http://club.xywy.com/doc_card/45441467', 'http://club.xywy.com/doc_card/47318402', '2014-12-13', '自己活得精彩才是精彩！', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/2737', 'http://club.xywy.com/doc_card/45863837', '2014-11-25', '病人家属的犹豫，有时也是杀人啊。', 'http://club.xywy.com/doc_card/45863837', 'http://club.xywy.com/doc_card/44837032', '2014-12-01', '是啊', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/2309', 'http://club.xywy.com/doc_card/45228815', '2014-10-31', '找到自己不能接纳的特质，去接纳它，可采用的方法有，每天对着镜子中的自己，大声说：“这就是我，我就是_________(例如，偏心、虚伪、小气，每次直说一个特质)”。每次练习5分钟，直至练习到能接纳自己的这种特质为止。', '匿名用户', 'http://club.xywy.com/doc_card/45228815', '2014-10-31', '可以一试。', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/956', 'http://club.xywy.com/doc_card/56348885', '2015-06-27', '中医的优势', 'http://club.xywy.com/doc_card/56348885', 'http://club.xywy.com/doc_card/38894372', '2015-07-16', '中医博大精深，应该好好学习，继承与发扬', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/251', 'http://club.xywy.com/doc_card/33786927', '2015-06-25', '好危险啊！', 'http://club.xywy.com/doc_card/33786927', 'http://club.xywy.com/doc_card/18732252', '11个月前', 'en', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/251', 'http://club.xywy.com/doc_card/33786927', '2015-06-25', '长知识了!', 'http://club.xywy.com/doc_card/33786927', 'http://club.xywy.com/doc_card/18732252', '2015-09-02', '是的', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/251', 'http://club.xywy.com/doc_card/12179455', '2015-02-22', '赞成', 'http://club.xywy.com/doc_card/12179455', 'http://club.xywy.com/doc_card/4772658', '2015-03-31', '支持', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/251', 'http://club.xywy.com/doc_card/44069973', '2014-11-17', '学习', 'http://club.xywy.com/doc_card/44069973', 'http://club.xywy.com/doc_card/18732252', '2015-06-04', '赞一个！', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/251', 'http://club.xywy.com/doc_card/44069973', '2014-11-17', '学习', 'http://club.xywy.com/doc_card/44069973', 'http://club.xywy.com/doc_card/18732252', '2015-06-04', '写的很好！', '2', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/251', 'http://club.xywy.com/doc_card/44069973', '2014-11-17', '学习', 'http://club.xywy.com/doc_card/44069973', 'http://club.xywy.com/doc_card/18732252', '2015-06-04', '哈哈！', '3', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/251', 'http://club.xywy.com/doc_card/44069973', '2014-11-17', '学习', 'http://club.xywy.com/doc_card/44069973', 'http://club.xywy.com/doc_card/18732252', '2015-05-18', '值得学习', '4', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/251', 'http://club.xywy.com/doc_card/44069973', '2014-11-17', '学习', 'http://club.xywy.com/doc_card/44069973', 'http://club.xywy.com/doc_card/18732252', '2015-05-18', '一起学习了！', '5', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/251', 'http://club.xywy.com/doc_card/44069973', '2014-11-17', '学习', '匿名用户', 'http://club.xywy.com/doc_card/44069973', '2015-05-15', '恩，我也是', '6', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/264', 'http://club.xywy.com/doc_card/58372539', '2015-06-13', '很好的病例！', 'http://club.xywy.com/doc_card/58372539', 'http://club.xywy.com/doc_card/18732252', '2015-07-22', '很好的病例', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/8332', 'http://club.xywy.com/doc_card/44069973', '2015-05-18', '养成良好的睡眠，有助于提高免疫力，谢谢分享。', 'http://club.xywy.com/doc_card/44069973', 'http://club.xywy.com/doc_card/18732252', '2015-05-18', '过奖了', '1', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/8332', 'http://club.xywy.com/doc_card/44069973', '2015-05-18', '养成良好的睡眠，有助于提高免疫力，谢谢分享。', 'http://club.xywy.com/doc_card/18732252', 'http://club.xywy.com/doc_card/44069973', '2015-05-18', '谢谢', '2', '2016-12-15', '1');
INSERT INTO `case_experience_comment_second` VALUES ('http://club.xywy.com/doctorShare/detail/8332', 'http://club.xywy.com/doc_card/44069973', '2015-05-18', '养成良好的睡眠，有助于提高免疫力，谢谢分享。', 'http://club.xywy.com/doc_card/44069973', 'http://club.xywy.com/doc_card/18732252', '2015-05-18', '不用客气，应该的。', '3', '2016-12-15', '1');