<?php

require_once '/opt/bitnami/frameworks/symfony/vendor/autoload.php';
///Users/angelomartelli/vendor/swiftmailer/swiftmailer/lib
$config = parse_ini_file('/home/bitnami/reviewi/private/config.ini'); 

$emailusr = $config['emailusr'];
$emailpwd = $config['emailpwd'];

$transport = (new Swift_SmtpTransport('smtp.gmail.com', 465, "ssl"))
  ->setUsername($emailusr)
  ->setPassword($emailpwd);
  
$EmailFrom = "";
$EmailTo = "info.reviewi.me@gmail.com";
$Subject = "New Email from Contact Form";
$Name = Trim(stripslashes($_POST['fname'])); 
$Email = Trim(stripslashes($_POST['Email'])); 
$Message = Trim(stripslashes($_POST['Message'])); 

// validation
$validationOK=true;
if (!$validationOK) {
  print "<meta http-equiv=\"refresh\" content=\"0;URL=error.htm\">";
  exit;
}

// prepare email body text
$Body = "";
$Body .= "Name: ";
$Body .= $Name;
$Body .= "\n";
$Body .= "Email: ";
$Body .= $Email;
$Body .= "\n";
$Body .= "Message: ";
$Body .= $Message;
$Body .= "\n";


$mailer = new Swift_Mailer($transport);

$message = (new Swift_Message($Subject))
  ->setFrom([$Email => $Name])
  ->setTo([$EmailTo => 'Reviewi Support'])
  ->setBody($Body)	
  ;

// send email 
$result = $mailer->send($message);



// redirect to success page 
if ($result){
  print "<meta http-equiv=\"refresh\" content=\"0;URL=../html/MessageSent.html\">";
}
else{
  print "<meta http-equiv=\"refresh\" content=\"0;URL=error.htm\">";
}
?>
