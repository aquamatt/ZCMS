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
INSERT INTO `zcms_channel` VALUES (1,'UK',NULL),(3,'FRANCE',1);
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
  `channel_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `value` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `zcms_cmscomponent_channel_id` (`channel_id`),
  KEY `zcms_cmscomponent_language_id` (`language_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `zcms_cmscomponent`
--

LOCK TABLES `zcms_cmscomponent` WRITE;
/*!40000 ALTER TABLE `zcms_cmscomponent` DISABLE KEYS */;
INSERT INTO `zcms_cmscomponent` VALUES (1,'home',1,1,'{% zextends \"basecomponent\" %}\r\n\r\n{% block content %}\r\n<p>This is the \'home\' template; it extends basecomponent with the zextends tag, a version of Django\'s extends tag which is able to pull templates from the CMS.</p>\r\n<p>\r\nA token from the CMS: [% tokenByName todo %]\r\n</p>\r\n{% endblock %}\r\n'),(2,'loud_bit',1,1,'<span style=\'font-weight:bold\'>[% tokenByName baz %]</span>\r\n[% componentByName quiet_bit %]'),(3,'quiet_bit',1,1,'<span style=\'color:red\'>shhhh...</span>'),(6,'uberparent',1,1,'<html>\r\n<body>\r\n<span style=\'background-color:#ccccff\'>\r\n<a href=\'/zcms/setcontext?language=en_gb&channel=UK\'>UK Channel</a> | <a href=\'/zcms/setcontext?channel=FRANCE\'>French Channel</a>\r\n</span>\r\n<hr/>\r\nUber parent : This is the high level parent</br>\r\n{% block master %}\r\n{% endblock %}\r\n<hr/>\r\nClick <a href=\'/zcms/help\'>here</a> for the help page\r\n</body>\r\n</html>'),(5,'basecomponent',1,1,'{% zextends \"uberparent\" %}\r\n{% block master %}\r\n   <p>This is the base component, it extends the uberparent.</p>\r\n   <p>The best place to be \"[% tokenByName foobar %]\". The data in quotes is a CMS Token</p>\r\n  <p>\r\n  [% componentByName loud_bit %] (This is CMS component)\r\n  </p>\r\n\r\n{% block content %}{% endblock content%}\r\n\r\n{% endblock master%}'),(7,'home',3,1,'{% zextends \"basecomponent\" %}\r\n\r\n{% block content %}\r\n<p>Voici le cadre \'maison\' qui tien de le cadre \'basecomponent\'. Pas mal, n\'est-ce pas?\r\n</p>\r\nUn \'token\' du CMS: [% tokenByName todo %]\r\n</p>\r\n{% endblock %}'),(8,'help',1,1,'{% zextends \"uberparent\" %}\r\n{% block master %}\r\n<p>\r\n  A little bit of static content. This could be the help page!\r\n</p>\r\n{% block content %}{% endblock content%}\r\n\r\n{% endblock master%}'),(9,'help',3,1,'{% zextends \"uberparent\" %}\r\n{% block master %}\r\n<p>\r\n Voici une page statique qui pourrait, par example, donner des explications.\r\n</p>\r\n{% block content %}{% endblock content%}\r\n\r\n{% endblock master%}');
/*!40000 ALTER TABLE `zcms_cmscomponent` ENABLE KEYS */;
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
  `channel_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `value` varchar(200) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `zcms_cmstoken_channel_id` (`channel_id`),
  KEY `zcms_cmstoken_language_id` (`language_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `zcms_cmstoken`
--

LOCK TABLES `zcms_cmstoken` WRITE;
/*!40000 ALTER TABLE `zcms_cmstoken` DISABLE KEYS */;
INSERT INTO `zcms_cmstoken` VALUES (1,'foobar',1,1,'Is really home.'),(2,'baz',1,1,'Whoopsy!'),(4,'todo',1,1,'Blah blah blah'),(5,'todo',3,1,'Meh, meh meh!');
/*!40000 ALTER TABLE `zcms_cmstoken` ENABLE KEYS */;
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
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `zcms_language`
--

LOCK TABLES `zcms_language` WRITE;
/*!40000 ALTER TABLE `zcms_language` DISABLE KEYS */;
INSERT INTO `zcms_language` VALUES (1,'UK English','en_gb'),(2,'US English','en_us'),(3,'French','fr_fr');
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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2009-03-25 21:53:35
