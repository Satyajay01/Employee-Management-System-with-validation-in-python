-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: mydata
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `Name` varchar(30) DEFAULT NULL,
  `DOB` varchar(10) DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Married_Status` varchar(15) DEFAULT NULL,
  `Phone_Number` varchar(10) DEFAULT NULL,
  `Email` varchar(30) DEFAULT NULL,
  `Country` varchar(15) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Joining_Date` varchar(30) DEFAULT NULL,
  `Department` varchar(40) DEFAULT NULL,
  `Combo_ID_Proof` varchar(20) DEFAULT NULL,
  `ID_Proof` varchar(20) NOT NULL,
  `Salary` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID_Proof`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('Reema','12/11/2002','Female','Married','1248579635','Reema@Gmail.com','Pakistan','Mew','16/28/2020','Principle WS Engineer','Passport','12457896587845','800000'),('Sunil','06/20/2000','Male','UnMarried','1456329874','Sunil@gmail.com','india','bhawtara','16/05/2021','Senior Manager','Passport','12458796321457','120000'),('Vijay','26/12/2001','Male','Married','1245987361','Vijay@gmail.com','USA','UK','20/08/2020','CR Project Manager','Passport','14587596324578','130000'),('Aarti','16/11/2001','Female','Married','1452145698','Aarti06@gmail.com','Pakistan','Bhawtara','16/06/2019','Security Engineer','Passport','14785236978945','150000'),('Tannu','22/03/2001','Female','UnMarried','1245963257','tanu@gmail.com','india','Bilashpur','11/11/2022','HR','Aadhar','456123987015','900000'),('Jyoti','12/19/1988','Female','UnMarried','3597845627','Jyoti.rani06@Gmail.com','india','Darri','26/12/2015','Back-end Developer','Aadhar','458796584524','130000'),('Rakesh','12/05/1988','Male','Married','8459658745','Rakesh48@gmail.com','india','Pangawo','24/09/2004','Data Scientist','PAN Card','ESYGD7854H','140000'),('Ravi','13/12/2001','Male','Married','1230458795','Ravi@gmail.com','USA','UK','11/11/2022','Asoosiate WS Engineer','PAN Card','GRDYP8572C','800000'),('Life','22/06/2001','Male','Married','1254963582','Life@gmail.com','india','PMG','11/11/2022','CO','PAN Card','KUOOD9661V','180000'),('Anjali','05/02/1978','Female','Married','2548697568','Anjali.ray45@gmail.com','india','Pendri','21/02/2010','Full-stack Developer','PAN Card','LKUFS9685B','160000'),('Bharti','24/09/2001','Female','Married','9985657568','Bhatri256@gmail.com','india','kosha','26/09/2021','Tester','PAN Card','LYDOD7549D','160000'),('Digamber','22/08/2001','Male','UnMarried','4578963218','Digamber@gmail.com','india','koshla','12/06/2020','Manager','PAN Card','LYIPS7825C','900000'),('Megha','16/07/2001','Female','Married','1459658749','Megha@gmail.com','Pakistan','Bargawo','18/12/2019','Graphics Developer','PAN Card','LYPFS5692B','700000'),('Pritee','16/01/1998','Female','UnMarried','1230125496','Pritee47@gmail.com','India','Bhawtara','12/08/2017','Front-end Developer','PAN Card','NJGTD4856G','150000'),('Suraj','06/23/1976','Male','UnMarried','3698546298','Suraj69@gmail.com','india','bhawtara','28/05/1990','Tester','PAN Card','UKGRD9725C','130000');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-17  2:24:58
