
# 新建zhihu数据库
CREATE DATABASE zhihu DEFAULT CHARSET utf8 COLLATE utf8_bin;

use zhihu;
CREATE TABLE `zhihu_topic_square` (
  `id`  INT(13) NOT NULL AUTO_INCREMENT ,
  `topic_id`  VARCHAR(100) COLLATE utf8_bin NOT NULL DEFAULT '',
  `title` VARCHAR(100) COLLATE utf8_bin NOT NULL DEFAULT '',
  `add_time`  INT(11) NULL ,
  `update_time`  INT(11) NULL ,
  `is_deleted`  TINYINT(3) NULL DEFAULT 0 ,
  PRIMARY KEY (`id`),
  UNIQUE KEY(`topic_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT '话题广场';

CREATE TABLE `zhihu_topic` (
  `id`  INT(13) NOT NULL AUTO_INCREMENT ,
  `parent_topic_id`  VARCHAR(100) COLLATE utf8_bin NOT NULL DEFAULT '',
  `topic_id`  VARCHAR(100) COLLATE utf8_bin NOT NULL DEFAULT '',
  `title` VARCHAR(100) COLLATE utf8_bin NOT NULL DEFAULT '',
  `add_time`  INT(11) NULL ,
  `update_time`  INT(11) NULL ,
  `is_deleted`  TINYINT(3) NULL DEFAULT 0 ,
  PRIMARY KEY (`id`),
  UNIQUE KEY(`topic_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT '知乎话题';

CREATE TABLE `zhihu_question_1` (
  `id`  INT(13) NOT NULL AUTO_INCREMENT ,
  `topic_id`  VARCHAR(100) COLLATE utf8_bin NOT NULL DEFAULT '',
  `attached_info` VARCHAR(150) COLLATE utf8_bin NOT NULL DEFAULT '',
  `title` VARCHAR(150) COLLATE utf8_bin NOT NULL DEFAULT '',
  `type` VARCHAR(20) NOT NULL DEFAULT '',
  `comment_count` VARCHAR(20) NOT NULL DEFAULT '',
  `voteup_count` VARCHAR(20) NOT NULL DEFAULT '',
  `common_json` LONGTEXT,
  `content` LONGTEXT,
  `add_time`  INT(11) NULL ,
  `update_time`  INT(11) NULL ,
  `is_deleted`  TINYINT(3) NULL DEFAULT 0 ,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT '知乎问题';
CREATE TABLE zhihu_question_2 like zhihu_question_1;
CREATE TABLE zhihu_question_3 like zhihu_question_1;
CREATE TABLE zhihu_question_4 like zhihu_question_1;
CREATE TABLE zhihu_question_5 like zhihu_question_1;
CREATE TABLE zhihu_question_6 like zhihu_question_1;
CREATE TABLE zhihu_question_7 like zhihu_question_1;
CREATE TABLE zhihu_question_8 like zhihu_question_1;
CREATE TABLE zhihu_question_9 like zhihu_question_1;
CREATE TABLE zhihu_question_10 like zhihu_question_1;
CREATE TABLE zhihu_question_11 like zhihu_question_1;
CREATE TABLE zhihu_question_12 like zhihu_question_1;
CREATE TABLE zhihu_question_13 like zhihu_question_1;
CREATE TABLE zhihu_question_14 like zhihu_question_1;
CREATE TABLE zhihu_question_15 like zhihu_question_1;
CREATE TABLE zhihu_question_16 like zhihu_question_1;
CREATE TABLE zhihu_question_17 like zhihu_question_1;
CREATE TABLE zhihu_question_18 like zhihu_question_1;
CREATE TABLE zhihu_question_19 like zhihu_question_1;
CREATE TABLE zhihu_question_20 like zhihu_question_1;
CREATE TABLE zhihu_question_21 like zhihu_question_1;
CREATE TABLE zhihu_question_22 like zhihu_question_1;
CREATE TABLE zhihu_question_23 like zhihu_question_1;
CREATE TABLE zhihu_question_24 like zhihu_question_1;
CREATE TABLE zhihu_question_25 like zhihu_question_1;
CREATE TABLE zhihu_question_26 like zhihu_question_1;
CREATE TABLE zhihu_question_27 like zhihu_question_1;
CREATE TABLE zhihu_question_28 like zhihu_question_1;
CREATE TABLE zhihu_question_29 like zhihu_question_1;
CREATE TABLE zhihu_question_30 like zhihu_question_1;
CREATE TABLE zhihu_question_31 like zhihu_question_1;
CREATE TABLE zhihu_question_32 like zhihu_question_1;
CREATE TABLE zhihu_question_33 like zhihu_question_1;
CREATE TABLE zhihu_question_34 like zhihu_question_1;
CREATE TABLE zhihu_question_35 like zhihu_question_1;
CREATE TABLE zhihu_question_36 like zhihu_question_1;
CREATE TABLE zhihu_question_37 like zhihu_question_1;
CREATE TABLE zhihu_question_38 like zhihu_question_1;
CREATE TABLE zhihu_question_39 like zhihu_question_1;
CREATE TABLE zhihu_question_40 like zhihu_question_1;
CREATE TABLE zhihu_question_41 like zhihu_question_1;
CREATE TABLE zhihu_question_42 like zhihu_question_1;
CREATE TABLE zhihu_question_43 like zhihu_question_1;
CREATE TABLE zhihu_question_44 like zhihu_question_1;
CREATE TABLE zhihu_question_45 like zhihu_question_1;
CREATE TABLE zhihu_question_46 like zhihu_question_1;
CREATE TABLE zhihu_question_47 like zhihu_question_1;
CREATE TABLE zhihu_question_48 like zhihu_question_1;
CREATE TABLE zhihu_question_49 like zhihu_question_1;
CREATE TABLE zhihu_question_50 like zhihu_question_1;
CREATE TABLE zhihu_question_51 like zhihu_question_1;
CREATE TABLE zhihu_question_52 like zhihu_question_1;
CREATE TABLE zhihu_question_53 like zhihu_question_1;
CREATE TABLE zhihu_question_54 like zhihu_question_1;
CREATE TABLE zhihu_question_55 like zhihu_question_1;
CREATE TABLE zhihu_question_56 like zhihu_question_1;
CREATE TABLE zhihu_question_57 like zhihu_question_1;
CREATE TABLE zhihu_question_58 like zhihu_question_1;
CREATE TABLE zhihu_question_59 like zhihu_question_1;
CREATE TABLE zhihu_question_60 like zhihu_question_1;
CREATE TABLE zhihu_question_61 like zhihu_question_1;
CREATE TABLE zhihu_question_62 like zhihu_question_1;
CREATE TABLE zhihu_question_63 like zhihu_question_1;
CREATE TABLE zhihu_question_64 like zhihu_question_1;
CREATE TABLE zhihu_question_65 like zhihu_question_1;
CREATE TABLE zhihu_question_66 like zhihu_question_1;
CREATE TABLE zhihu_question_67 like zhihu_question_1;
CREATE TABLE zhihu_question_68 like zhihu_question_1;
CREATE TABLE zhihu_question_69 like zhihu_question_1;
CREATE TABLE zhihu_question_70 like zhihu_question_1;
CREATE TABLE zhihu_question_71 like zhihu_question_1;
CREATE TABLE zhihu_question_72 like zhihu_question_1;
CREATE TABLE zhihu_question_73 like zhihu_question_1;
CREATE TABLE zhihu_question_74 like zhihu_question_1;
CREATE TABLE zhihu_question_75 like zhihu_question_1;
CREATE TABLE zhihu_question_76 like zhihu_question_1;
CREATE TABLE zhihu_question_77 like zhihu_question_1;
CREATE TABLE zhihu_question_78 like zhihu_question_1;
CREATE TABLE zhihu_question_79 like zhihu_question_1;
CREATE TABLE zhihu_question_80 like zhihu_question_1;
CREATE TABLE zhihu_question_81 like zhihu_question_1;
CREATE TABLE zhihu_question_82 like zhihu_question_1;
CREATE TABLE zhihu_question_83 like zhihu_question_1;
CREATE TABLE zhihu_question_84 like zhihu_question_1;
CREATE TABLE zhihu_question_85 like zhihu_question_1;
CREATE TABLE zhihu_question_86 like zhihu_question_1;
CREATE TABLE zhihu_question_87 like zhihu_question_1;
CREATE TABLE zhihu_question_88 like zhihu_question_1;
CREATE TABLE zhihu_question_89 like zhihu_question_1;
CREATE TABLE zhihu_question_90 like zhihu_question_1;
CREATE TABLE zhihu_question_91 like zhihu_question_1;
CREATE TABLE zhihu_question_92 like zhihu_question_1;
CREATE TABLE zhihu_question_93 like zhihu_question_1;
CREATE TABLE zhihu_question_94 like zhihu_question_1;
CREATE TABLE zhihu_question_95 like zhihu_question_1;
CREATE TABLE zhihu_question_96 like zhihu_question_1;
CREATE TABLE zhihu_question_97 like zhihu_question_1;
CREATE TABLE zhihu_question_98 like zhihu_question_1;
CREATE TABLE zhihu_question_99 like zhihu_question_1;
CREATE TABLE zhihu_question_100 like zhihu_question_1;

CREATE TABLE `zhihu_user_1` (
  `id`  INT(13) NOT NULL AUTO_INCREMENT ,
  `userId`  VARCHAR(100) COLLATE utf8_bin NOT NULL DEFAULT '',
  `name` VARCHAR(100) NOT NULL DEFAULT '',
  `avatar_url` VARCHAR(200) NOT NULL DEFAULT '',
  `avatar_url_template` VARCHAR(200) NOT NULL  DEFAULT '',
  `gender` TINYINT(2) NOT NULL DEFAULT 0 COMMENT '0->男,1->女',
  `headline` VARCHAR(255) NOT NULL DEFAULT '',
  `is_advertiser` TINYINT(2) NOT NULL DEFAULT 0 COMMENT '0->不是，1->是',
  `is_org` TINYINT(2) NOT NULL DEFAULT 0 COMMENT '0->不是，1->是',
  `url_token` VARCHAR(100) NOT NULL DEFAULT '',
  `type` VARCHAR(50) NOT NULL DEFAULT '',
  `url` VARCHAR(150) NOT NULL DEFAULT '',
  `user_type` VARCHAR(50) NOT NULL DEFAULT '',
  `badge` TEXT,
  `edu_member_tag` TEXT,
  `add_time`  INT(11) NULL ,
  `update_time`  INT(11) NULL ,
  `is_deleted`  TINYINT(3) NULL DEFAULT 0 ,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT '知乎用户表';
CREATE TABLE zhihu_user_2 like zhihu_user_1;
CREATE TABLE zhihu_user_3 like zhihu_user_1;
CREATE TABLE zhihu_user_4 like zhihu_user_1;
CREATE TABLE zhihu_user_5 like zhihu_user_1;
CREATE TABLE zhihu_user_6 like zhihu_user_1;
CREATE TABLE zhihu_user_7 like zhihu_user_1;
CREATE TABLE zhihu_user_8 like zhihu_user_1;
CREATE TABLE zhihu_user_9 like zhihu_user_1;
CREATE TABLE zhihu_user_10 like zhihu_user_1;
CREATE TABLE zhihu_user_11 like zhihu_user_1;
CREATE TABLE zhihu_user_12 like zhihu_user_1;
CREATE TABLE zhihu_user_13 like zhihu_user_1;
CREATE TABLE zhihu_user_14 like zhihu_user_1;
CREATE TABLE zhihu_user_15 like zhihu_user_1;
CREATE TABLE zhihu_user_16 like zhihu_user_1;
CREATE TABLE zhihu_user_17 like zhihu_user_1;
CREATE TABLE zhihu_user_18 like zhihu_user_1;
CREATE TABLE zhihu_user_19 like zhihu_user_1;
CREATE TABLE zhihu_user_20 like zhihu_user_1;
CREATE TABLE zhihu_user_21 like zhihu_user_1;
CREATE TABLE zhihu_user_22 like zhihu_user_1;
CREATE TABLE zhihu_user_23 like zhihu_user_1;
CREATE TABLE zhihu_user_24 like zhihu_user_1;
CREATE TABLE zhihu_user_25 like zhihu_user_1;
CREATE TABLE zhihu_user_26 like zhihu_user_1;
CREATE TABLE zhihu_user_27 like zhihu_user_1;
CREATE TABLE zhihu_user_28 like zhihu_user_1;
CREATE TABLE zhihu_user_29 like zhihu_user_1;
CREATE TABLE zhihu_user_30 like zhihu_user_1;
CREATE TABLE zhihu_user_31 like zhihu_user_1;
CREATE TABLE zhihu_user_32 like zhihu_user_1;
CREATE TABLE zhihu_user_33 like zhihu_user_1;
CREATE TABLE zhihu_user_34 like zhihu_user_1;
CREATE TABLE zhihu_user_35 like zhihu_user_1;
CREATE TABLE zhihu_user_36 like zhihu_user_1;
CREATE TABLE zhihu_user_37 like zhihu_user_1;
CREATE TABLE zhihu_user_38 like zhihu_user_1;
CREATE TABLE zhihu_user_39 like zhihu_user_1;
CREATE TABLE zhihu_user_40 like zhihu_user_1;
CREATE TABLE zhihu_user_41 like zhihu_user_1;
CREATE TABLE zhihu_user_42 like zhihu_user_1;
CREATE TABLE zhihu_user_43 like zhihu_user_1;
CREATE TABLE zhihu_user_44 like zhihu_user_1;
CREATE TABLE zhihu_user_45 like zhihu_user_1;
CREATE TABLE zhihu_user_46 like zhihu_user_1;
CREATE TABLE zhihu_user_47 like zhihu_user_1;
CREATE TABLE zhihu_user_48 like zhihu_user_1;
CREATE TABLE zhihu_user_49 like zhihu_user_1;
CREATE TABLE zhihu_user_50 like zhihu_user_1;
CREATE TABLE zhihu_user_51 like zhihu_user_1;
CREATE TABLE zhihu_user_52 like zhihu_user_1;
CREATE TABLE zhihu_user_53 like zhihu_user_1;
CREATE TABLE zhihu_user_54 like zhihu_user_1;
CREATE TABLE zhihu_user_55 like zhihu_user_1;
CREATE TABLE zhihu_user_56 like zhihu_user_1;
CREATE TABLE zhihu_user_57 like zhihu_user_1;
CREATE TABLE zhihu_user_58 like zhihu_user_1;
CREATE TABLE zhihu_user_59 like zhihu_user_1;
CREATE TABLE zhihu_user_60 like zhihu_user_1;
CREATE TABLE zhihu_user_61 like zhihu_user_1;
CREATE TABLE zhihu_user_62 like zhihu_user_1;
CREATE TABLE zhihu_user_63 like zhihu_user_1;
CREATE TABLE zhihu_user_64 like zhihu_user_1;
CREATE TABLE zhihu_user_65 like zhihu_user_1;
CREATE TABLE zhihu_user_66 like zhihu_user_1;
CREATE TABLE zhihu_user_67 like zhihu_user_1;
CREATE TABLE zhihu_user_68 like zhihu_user_1;
CREATE TABLE zhihu_user_69 like zhihu_user_1;
CREATE TABLE zhihu_user_70 like zhihu_user_1;
CREATE TABLE zhihu_user_71 like zhihu_user_1;
CREATE TABLE zhihu_user_72 like zhihu_user_1;
CREATE TABLE zhihu_user_73 like zhihu_user_1;
CREATE TABLE zhihu_user_74 like zhihu_user_1;
CREATE TABLE zhihu_user_75 like zhihu_user_1;
CREATE TABLE zhihu_user_76 like zhihu_user_1;
CREATE TABLE zhihu_user_77 like zhihu_user_1;
CREATE TABLE zhihu_user_78 like zhihu_user_1;
CREATE TABLE zhihu_user_79 like zhihu_user_1;
CREATE TABLE zhihu_user_80 like zhihu_user_1;
CREATE TABLE zhihu_user_81 like zhihu_user_1;
CREATE TABLE zhihu_user_82 like zhihu_user_1;
CREATE TABLE zhihu_user_83 like zhihu_user_1;
CREATE TABLE zhihu_user_84 like zhihu_user_1;
CREATE TABLE zhihu_user_85 like zhihu_user_1;
CREATE TABLE zhihu_user_86 like zhihu_user_1;
CREATE TABLE zhihu_user_87 like zhihu_user_1;
CREATE TABLE zhihu_user_88 like zhihu_user_1;
CREATE TABLE zhihu_user_89 like zhihu_user_1;
CREATE TABLE zhihu_user_90 like zhihu_user_1;
CREATE TABLE zhihu_user_91 like zhihu_user_1;
CREATE TABLE zhihu_user_92 like zhihu_user_1;
CREATE TABLE zhihu_user_93 like zhihu_user_1;
CREATE TABLE zhihu_user_94 like zhihu_user_1;
CREATE TABLE zhihu_user_95 like zhihu_user_1;
CREATE TABLE zhihu_user_96 like zhihu_user_1;
CREATE TABLE zhihu_user_97 like zhihu_user_1;
CREATE TABLE zhihu_user_98 like zhihu_user_1;
CREATE TABLE zhihu_user_99 like zhihu_user_1;
CREATE TABLE zhihu_user_100 like zhihu_user_1;

