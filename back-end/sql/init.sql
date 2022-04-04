CREATE TABLE `tb_users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'user id',
  `username` varchar(20) NOT NULL COMMENT '用户名',
  `password` varchar(100) NOT NULL COMMENT '密码',
  `is_deleted` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '删除标识',
  `role_id` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '权限id',
  `email` varchar(50) NOT NULL DEFAULT '' COMMENT '用户email',
  `phone` varchar(20) NOT NULL DEFAULT '' COMMENT '手机号',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_idx_username_is_deleted` (`username`,`is_deleted`) USING BTREE COMMENT '用户名唯一索引'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户信息表';


CREATE TABLE `tb_roles` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'role id',
  `name` varchar(20) NOT NULL COMMENT '角色名称',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `auth_time` datetime NOT NULL COMMENT '授权时间',
  `auth_name` varchar(20) NOT NULL DEFAULT '' COMMENT '授权人',
  `menus` varchar(255) NOT NULL DEFAULT '' COMMENT '授权目录',
  `is_deleted` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '删除标识',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_idx_name_is_deleted` (`name`,`is_deleted`) USING BTREE COMMENT '角色名称唯一索引'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='角色表';


CREATE TABLE `tb_categories` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'category id',
  `name` varchar(20) NOT NULL COMMENT '品类名称',
  `parent_id` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '父品类ID',
  `is_deleted` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '删除标识',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_idx_name_is_deleted` (`name`,`is_deleted`) USING BTREE COMMENT '品类名称唯一索引'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='品类表';


CREATE TABLE `tb_products` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'product id',
  `name` varchar(20) NOT NULL COMMENT '商品名称',
  `desc` varchar(255) NOT NULL DEFAULT '' COMMENT '商品描述',
  `price` decimal(10,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '商品价格',
  `parent_category_id` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '一级类别ID',
  `category_id` bigint(20) unsigned NOT NULL COMMENT '二级类别ID',
  `on_sale` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '上架状态',
  `is_deleted` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '删除标识',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_idx_name_is_deleted` (`name`,`is_deleted`) USING BTREE COMMENT '商品名称唯一索引'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='商品信息表';
