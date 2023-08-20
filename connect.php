<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "stylesheet" type = "text/css" href = "style.css" />
    <title>Currency</title>
</head>
<body>
    <h1>Currency</h1>
    <?php
    $connection=pg_connect("host=localhost port=5432 dbname=web user=postgres password=admin");
    if(!$connection){
        echo "Connection failed";
        exit;
    }
    $result=pg_query($connection,"select * from currency");
    if(!$result){
        echo "Query failed";
        exit;
    }
    ?>
    <table>

        <tr>
            <th>id</th>
            <th>Currency</th>
            <th>Rate</th>
        </tr>

        <?php

            while($row=pg_fetch_row($result)){
                echo "<tr>";
                echo "<td>$row[0]</td>";
                echo "<td>$row[1]</td>";
                echo "<td>$row[2]</td>";
                echo "</tr>";
            }

        ?>
    </table>
    
</body>
</html>