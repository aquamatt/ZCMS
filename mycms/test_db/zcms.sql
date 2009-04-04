-- MySQL dump 10.11
--
-- Host: localhost    Database: zcms
-- ------------------------------------------------------
-- Server version	5.0.67-0ubuntu6

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `zcms_channel`
--

DROP TABLE IF EXISTS `zcms_channel`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `zcms_channel` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(20) NOT NULL,
  `parent_id` int(11) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `zcms_channel_parent_id` (`parent_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `zcms_channel`
--

LOCK TABLES `zcms_channel` WRITE;
/*!40000 ALTER TABLE `zcms_channel` DISABLE KEYS */;
INSERT INTO `zcms_channel` VALUES (1,'MAIN',NULL),(2,'ALTERNATE',1);
/*!40000 ALTER TABLE `zcms_channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zcms_cmscomponent`
--

DROP TABLE IF EXISTS `zcms_cmscomponent`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `zcms_cmscomponent` (
  `id` int(11) NOT NULL auto_increment,
  `cid` varchar(20) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `zcms_cmscomponent`
--

LOCK TABLES `zcms_cmscomponent` WRITE;
/*!40000 ALTER TABLE `zcms_cmscomponent` DISABLE KEYS */;
INSERT INTO `zcms_cmscomponent` VALUES (1,'home'),(2,'loud_bit'),(3,'quiet_bit'),(6,'uberparent'),(5,'basecomponent'),(8,'help');
/*!40000 ALTER TABLE `zcms_cmscomponent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zcms_cmscomponentvalue`
--

DROP TABLE IF EXISTS `zcms_cmscomponentvalue`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `zcms_cmscomponentvalue` (
  `id` int(11) NOT NULL auto_increment,
  `component_id` int(11) NOT NULL,
  `channel_id` int(11) NOT NULL,
  `value` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `zcms_cmscomponentvalue_component_id` (`component_id`),
  KEY `zcms_cmscomponentvalue_channel_id` (`channel_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `zcms_cmscomponentvalue`
--

LOCK TABLES `zcms_cmscomponentvalue` WRITE;
/*!40000 ALTER TABLE `zcms_cmscomponentvalue` DISABLE KEYS */;
INSERT INTO `zcms_cmscomponentvalue` VALUES (1,1,1,'{% zextends \"basecomponent\" %}\r\n\r\n{% block content %}\r\n<p>This is the \'home\' template; it extends basecomponent with the zextends tag, a version of Django\'s extends tag which is able to pull templates from the CMS.</p>\r\n<p>\r\nA token from the CMS: [% tokenByName todo %]\r\n</p>\r\n{% endblock %}\r\n'),(2,2,1,'<span style=\'font-weight:bold\'>[% tokenByName baz %]</span>\r\n[% componentByName quiet_bit %]'),(3,3,1,'<span style=\'color:red\'>shhhh...</span>'),(4,6,1,'<html>\r\n<body>\r\n<span style=\'background-color:#ccccff\'>\r\n<a href=\'/zcms/setcontext?channel=MAIN\'>MAIN Channel</a> | \r\n<a href=\'/zcms/setcontext?channel=ALTERNATE\'>Alternate Channel</a>  |\r\n<a href=\'/zcms/setcontext?language=en_gb\'>English</a> | \r\n<a href=\'/zcms/setcontext?language=fr_fr\'>French</a>\r\n</span>\r\n<hr/>\r\nUber parent : This is the high level parent</br>\r\n{% block master %}\r\n{% endblock %}\r\n<p>\r\n<b>Slot test</b>\r\n<br/>\r\n[% slot testslot %]\r\n</p>\r\n<hr/>\r\nClick <a href=\'/zcms/help\'>here</a> for the help page\r\n</body>\r\n</html>'),(5,5,1,'{% zextends \"uberparent\" %}\r\n{% block master %}\r\n   <p>This is the base component, it extends the uberparent.</p>\r\n   <p>The best place to be \"[% tokenByName foobar %]\". The data in quotes is a CMS Token</p>\r\n  <p>\r\n  [% componentByName loud_bit %] (This is CMS component)\r\n  </p>\r\n\r\n{% block content %}{% endblock content%}\r\n\r\n{% endblock master%}'),(6,6,2,'<html>\r\n<body style=\'background-color:#ccc\'>\r\n<span style=\'background-color:#ccccff\'>\r\n<a href=\'/zcms/setcontext?channel=MAIN\'>MAIN Channel</a> | \r\n<a href=\'/zcms/setcontext?channel=ALTERNATE\'>Alternate Channel</a>  |\r\n<a href=\'/zcms/setcontext?language=en_gb\'>English</a> | \r\n<a href=\'/zcms/setcontext?language=fr_fr\'>French</a>\r\n</span>\r\n<hr/>\r\nUber parent : This is the high level parent</br>\r\n{% block master %}\r\n{% endblock %}\r\n<hr/>\r\nClick <a href=\'/zcms/help\'>here</a> for the help page\r\n</body>\r\n</html>'),(7,8,1,'{% zextends \"uberparent\" %}\r\n{% block master %}\r\n<p>\r\n  [% tokenByName helpText %]\r\n</p>\r\n{% block content %}{% endblock content%}\r\n\r\n{% endblock master%}');
/*!40000 ALTER TABLE `zcms_cmscomponentvalue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zcms_cmstoken`
--

DROP TABLE IF EXISTS `zcms_cmstoken`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `zcms_cmstoken` (
  `id` int(11) NOT NULL auto_increment,
  `cid` varchar(20) NOT NULL,
  `token_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `zcms_cmstoken`
--

LOCK TABLES `zcms_cmstoken` WRITE;
/*!40000 ALTER TABLE `zcms_cmstoken` DISABLE KEYS */;
INSERT INTO `zcms_cmstoken` VALUES (1,'foobar',0),(2,'baz',0),(5,'todo',0),(7,'helpText',0),(8,'slot_a',0),(9,'slot_b',0);
/*!40000 ALTER TABLE `zcms_cmstoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zcms_cmstokenvalue`
--

DROP TABLE IF EXISTS `zcms_cmstokenvalue`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `zcms_cmstokenvalue` (
  `id` int(11) NOT NULL auto_increment,
  `token_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `value` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `zcms_cmstokenvalue_token_id` (`token_id`),
  KEY `zcms_cmstokenvalue_language_id` (`language_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `zcms_cmstokenvalue`
--

LOCK TABLES `zcms_cmstokenvalue` WRITE;
/*!40000 ALTER TABLE `zcms_cmstokenvalue` DISABLE KEYS */;
INSERT INTO `zcms_cmstokenvalue` VALUES (1,8,1,'This is slot A'),(2,8,3,'Ceci est \'slot\' A'),(3,9,1,'This is slot B'),(4,9,3,'Ceci est \'slot\' B'),(5,7,1,'A bit of help - useful tidbits of information for you!'),(6,7,3,'Un peu de contenue statique  - on pourrait y mettre une page d\'aide.'),(7,5,1,'blah blah english blah'),(8,5,3,'Meh, meh meh!'),(9,2,1,'Whoopsy!'),(10,1,1,'Is really home.');
/*!40000 ALTER TABLE `zcms_cmstokenvalue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zcms_language`
--

DROP TABLE IF EXISTS `zcms_language`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `zcms_language` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(20) NOT NULL,
  `iso_code` varchar(5) NOT NULL,
  `fallback_id` int(11) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `iso_code` (`iso_code`),
  KEY `zcms_language_fallback_id` (`fallback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `zcms_language`
--

LOCK TABLES `zcms_language` WRITE;
/*!40000 ALTER TABLE `zcms_language` DISABLE KEYS */;
INSERT INTO `zcms_language` VALUES (1,'UK English','en_gb',NULL),(2,'US English','en_us',1),(3,'French','fr_fr',1);
/*!40000 ALTER TABLE `zcms_language` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zcms_url`
--

DROP TABLE IF EXISTS `zcms_url`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `zcms_url` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(20) NOT NULL,
  `url` varchar(255) NOT NULL,
  `enabled` tinyint(1) NOT NULL,
  `component_name` varchar(20) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `url` (`url`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `zcms_url`
--

LOCK TABLES `zcms_url` WRITE;
/*!40000 ALTER TABLE `zcms_url` DISABLE KEYS */;
INSERT INTO `zcms_url` VALUES (1,'Static page','/help',1,'help');
/*!40000 ALTER TABLE `zcms_url` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zcms_slot`
--

DROP TABLE IF EXISTS `zcms_slot`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `zcms_slot` (
  `id` int(11) NOT NULL auto_increment,
  `slot` varchar(20) NOT NULL,
  `summary` varchar(150) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `zcms_slot`
--

LOCK TABLES `zcms_slot` WRITE;
/*!40000 ALTER TABLE `zcms_slot` DISABLE KEYS */;
INSERT INTO `zcms_slot` VALUES (1,'testslot','A test slot for good things');
/*!40000 ALTER TABLE `zcms_slot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zcms_slotcontent`
--

DROP TABLE IF EXISTS `zcms_slotcontent`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `zcms_slotcontent` (
  `id` int(11) NOT NULL auto_increment,
  `slot_id` int(11) NOT NULL,
  `rank` int(11) NOT NULL,
  `enabled` tinyint(1) NOT NULL,
  `rules` longtext NOT NULL,
  `component` varchar(100) NOT NULL,
  `is_token` tinyint(1) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `zcms_slotcontent_slot_id` (`slot_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `zcms_slotcontent`
--

LOCK TABLES `zcms_slotcontent` WRITE;
/*!40000 ALTER TABLE `zcms_slotcontent` DISABLE KEYS */;
INSERT INTO `zcms_slotcontent` VALUES (1,1,1,1,'now.second%2','slot_a',1),(2,1,2,1,'True','slot_b',1);
/*!40000 ALTER TABLE `zcms_slotcontent` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2009-04-04 22:05:34
