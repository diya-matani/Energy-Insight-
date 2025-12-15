<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/results.css">
    <title>Appliances Prediction</title>
</head>
<body>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get user inputs from the form
    $lights = $_POST['lights'];
    $T1 = $_POST['T1'];
    $RH_1 = $_POST['RH_1'];
    $T2 = $_POST['T2'];
    $RH_2 = $_POST['RH_2'];
    $T3 = $_POST['T3'];
    $RH_3 = $_POST['RH_3'];
    $T4 = $_POST['T4'];
    $RH_4 = $_POST['RH_4'];
    $T5 = $_POST['T5'];
    $RH_5 = $_POST['RH_5'];
    $T6 = $_POST['T6'];
    $RH_6 = $_POST['RH_6'];
    $T7 = $_POST['T7'];
    $RH_7 = $_POST['RH_7'];
    $T8 = $_POST['T8'];
    $RH_8 = $_POST['RH_8'];
    $T9 = $_POST['T9'];
    $RH_9 = $_POST['RH_9'];
    $T_out = $_POST['T_out'];
    $Press_mm_hg = $_POST['Press_mm_hg'];
    $RH_out = $_POST['RH_out'];
    $Windspeed = $_POST['Windspeed'];
    $Visibility = $_POST['Visibility'];
    $Tdewpoint = $_POST['Tdewpoint'];
    $NSM = $_POST['NSM'];

// Prepare the command to run the Python script with user inputs
$command = "python -u appliances.py";

// Append user inputs to the command
$command .= " " . escapeshellarg($lights) . " " . escapeshellarg($T1) . " " . escapeshellarg($RH_1) . " " . escapeshellarg($T2) . " " . escapeshellarg($RH_2) . " " . escapeshellarg($T3) . " " . escapeshellarg($RH_3) . " " . escapeshellarg($T4) . " " . escapeshellarg($RH_4) . " " . escapeshellarg($T5) . " " . escapeshellarg($RH_5) . " " . escapeshellarg($T6) . " " . escapeshellarg($RH_6) . " " . escapeshellarg($T7) . " " . escapeshellarg($RH_7) . " " . escapeshellarg($T8) . " " . escapeshellarg($RH_8) . " " . escapeshellarg($T9) . " " . escapeshellarg($RH_9) . " " . escapeshellarg($T_out) . " " . escapeshellarg($Press_mm_hg) . " " . escapeshellarg($RH_out) . " " . escapeshellarg($Windspeed) . " " . escapeshellarg($Visibility) . " " . escapeshellarg($Tdewpoint) . " " . escapeshellarg($NSM);

// Execute the command and capture the output
$output = shell_exec($command);

// Display the result
// echo "<p>The predicted Appliances value is: $output</p>";

}
?>

    <header>
        <h1>Appliances Energy Prediction</h1>
    </header>

    <main>
        <div id="resultContainer" class="result-container">
            <?php if(isset($output)) echo "<p>$output</p>"; ?>
        </div>
    </main>

</body>
</html>