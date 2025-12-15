<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get user input from the form

    $city = $_POST["City"];
    $X1 = $_POST["X1"];
    $X2 = $_POST["X2"];
    $X3 = $_POST["X3"];
    $X4 = $_POST["X4"];
    $X5 = $_POST["X5"];
    $X6 = $_POST["X6"];
    $X7 = $_POST["X7"];
    $X8 = $_POST["X8"];

    // Prepare the command to run the Python script with user inputs
    // $command = "python -u D:\\Projects\\Energy-Insight\\Dump\\heatCoolLoad.py";
    $command = "python -u heatCoolLoad.py";
        
    // Append user inputs to the command, including the city name
    $command .= " " . escapeshellarg($city) . " " . escapeshellarg($X1) . " " . escapeshellarg($X2) . " " . escapeshellarg($X3) . " " . escapeshellarg($X4) . " " . escapeshellarg($X5) . " " . escapeshellarg($X6) . " " . escapeshellarg($X7) . " " . escapeshellarg($X8);

    // Execute the command and capture the output
    $output = shell_exec($command);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heat Cool Load Prediction</title>
    <!-- <link rel="stylesheet" href="css/heatcoolLoad.css"> -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="css/results.css">
</head>
<body>
    <header>
        <h1>Heat Cool Load Prediction</h1>
    </header>

    <main>
        <div id="resultContainer" class="result-container">
            <?php if(isset($output)) echo "<p>$output</p>"; ?>
        </div>
    </main>

</body>
</html>
