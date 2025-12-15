<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/appliances.css">
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
$command = "python -u D:/Projects/Energy-Insight/Dump/appliances.py";

// Append user inputs to the command
$command .= " " . escapeshellarg($lights) . " " . escapeshellarg($T1) . " " . escapeshellarg($RH_1) . " " . escapeshellarg($T2) . " " . escapeshellarg($RH_2) . " " . escapeshellarg($T3) . " " . escapeshellarg($RH_3) . " " . escapeshellarg($T4) . " " . escapeshellarg($RH_4) . " " . escapeshellarg($T5) . " " . escapeshellarg($RH_5) . " " . escapeshellarg($T6) . " " . escapeshellarg($RH_6) . " " . escapeshellarg($T7) . " " . escapeshellarg($RH_7) . " " . escapeshellarg($T8) . " " . escapeshellarg($RH_8) . " " . escapeshellarg($T9) . " " . escapeshellarg($RH_9) . " " . escapeshellarg($T_out) . " " . escapeshellarg($Press_mm_hg) . " " . escapeshellarg($RH_out) . " " . escapeshellarg($Windspeed) . " " . escapeshellarg($Visibility) . " " . escapeshellarg($Tdewpoint) . " " . escapeshellarg($NSM);

// Execute the command and capture the output
$output = shell_exec($command);

// Display the result
// echo "<p>The predicted Appliances value is: $output</p>";

}
?>


    <header>
        <h1>Appliance Energy Prediction</h1>
    </header>

    <main>
        <div class="container">
            <div class="form">
                <form action="result_a.php" method="post" id="predictionForm">

                    <div class="question" id="question1">
                        <div class="info-icon material-icons" title="">info</div>
                        <label for="lights">Lights:</label>
                        <input type="text" name="lights" step="0.01" min="0" required><br>
                        <button type="button" id="next-btn" class="next-btn">Next</button>


                    </div>
                    <div class="question hidden" id="question2">
                        <label for="T1">Temperature in kitchen area (T1):</label>
                        <input type="text" name="T1" required><br>

                        <label for="RH_1">Humidity in kitchen area (RH_1):</label>
                        <input type="text" name="RH_1" required><br>

                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                        

                    </div>
                    <div class="question hidden" id="question3">
                        <label for="T2">Temperature in living room area (T2):</label>
                        <input type="text" name="T2" required><br>

                        <label for="RH_2">Humidity in living room area (RH_2):</label>
                        <input type="text" name="RH_2" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question4">
                        <label for="T3">Temperature in laundry room area (T3):</label>
                        <input type="text" name="T3" required><br>

                        <label for="RH_3">Humidity in laundry room area (RH_3):</label>
                        <input type="text" name="RH_3" required><br>

                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question5">
                        <label for="T4">Temperature in office room (T4):</label>
                        <input type="text" name="T4" required><br>

                        <label for="RH_4">Humidity in office room (RH_4):</label>
                        <input type="text" name="RH_4" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question6">
                        <label for="T5">Temperature in bathroom (T5):</label>
                        <input type="text" name="T5" required><br>

                        <label for="RH_5">Humidity in bathroom (RH_5):</label>
                        <input type="text" name="RH_5" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question7">
                        <label for="T6">Temperature outside the building (north side) (T6):</label>
                        <input type="text" name="T6" required><br>

                        <label for="RH_6">Humidity outside the building (north side) (RH_6):</label>
                        <input type="text" name="RH_6" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question8">
                        <label for="T7">Temperature in ironing room (T7):</label>
                        <input type="text" name="T7" required><br>

                        <label for="RH_7">Humidity in ironing room (RH_7):</label>
                        <input type="text" name="RH_7" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question9">
                        <label for="T8">Temperature in teenager room 2 (T8):</label>
                        <input type="text" name="T8" required><br>

                        <label for="RH_8">Humidity in teenager room 2 (RH_8):</label>
                        <input type="text" name="RH_8" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question10">
                        <label for="T9">Temperature in parents' room (T9):</label>
                        <input type="text" name="T9" required><br>

                        <label for="RH_9">Humidity in parents' room (RH_9):</label>
                        <input type="text" name="RH_9" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question11">
                        <label for="T_out">Temperature outside (T_out):</label>
                        <input type="text" name="T_out" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question12">
                        <label for="Press_mm_hg">Pressure (Press_mm_hg):</label>
                        <input type="text" name="Press_mm_hg" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question13">
                        <label for="RH_out">Humidity outside (RH_out):</label>
                        <input type="text" name="RH_out" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question14">
                        <label for="Windspeed">Windspeed  (Windspeed):</label>
                        <input type="text" name="Windspeed" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question14">
                        <label for="Visibility">Visibility (Visibility):</label>
                        <input type="text" name="Visibility" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question15">
                        <label for="Tdewpoint">Dewpoint Temperature (Tdewpoint):</label>
                        <input type="text" name="Tdewpoint" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    
                    <div class="question hidden" id="question8">
                        <label for="NSM">NSM Value:</label>
                        <input type="text" name="NSM" required><br>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <!-- <button type="submit" id="predict-btn" class="hidden">Predict</button> -->
                    </div>
                    <button type="submit" id="predict-btn" class="pred-btn" disabled>Predict</button>
                </form>
            </div>

            <div class="data-representation">
                <div id="cube"></div>
            </div>
        </div>

        <div id="resultContainer" class="result-container">
            <?php if(isset($output)) echo "<p>$output</p>"; ?>
        </div>
    </main>

    <script src="js/heatload.js"></script>
</body>
</html>
