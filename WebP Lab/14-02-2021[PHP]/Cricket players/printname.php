<?php
$name1 = $_POST['pname1'];
$name2 = $_POST['pname2'];
$name3 = $_POST['pname3'];
$name4 = $_POST['pname4'];
$name5 = $_POST['pname5'];

    $myArray = Array($name1, $name2, $name3, $name4,$name5)?>
    <table border='1'>
    <tr>
    <th>Id</th>
    <th>Name</th>
    </tr><?php
    $x=1;
    for($i=0;$i<5;$i++)
{
    ?>
        <tr>
       <td><?php echo $x;?></td>
        <td><?php echo $myArray[$i];?></td>
        </tr>;
      <?php $x++; }?>
        </table>
    

