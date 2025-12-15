
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
    <link rel="stylesheet" href="css/heatcoolLoad.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>
<body>
    <header>
        <h1>Heat Cool Load Prediction</h1>
    </header>

    <main>
        <div class="container">
            <div class="form">
                <!-- <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post" id="predictionForm"> -->
                <form action="results_hcl.php" method="post" id="predictionForm">



                    <div class="question" id="question1">
                        <!-- Info icon -->
                        <div class="info-icon material-icons" title="Indicates how compact the building is relative to its footprint. Please provide a value between 0.0 and 1.0.">info</div>
                        <label for="X1">X1 Relative Compactness:</label>
                        <input type="number" name="X1" step="0.01" min="0" required>
                        <button type="button" class="next-btn">Next</button>
                    </div>
                    
                    <div class="question hidden" id="question2">
                        <div class="info-icon material-icons" title="Total surface area of the building envelope (in square meters)">info</div>
                        <label for="X2">X2 Surface Area:</label>
                        <input type="number" name="X2" step="0.02" min="0" required>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question3">
                        <div class="info-icon material-icons" title="Total area of the external walls of the building (in square meters).">info</div>
                        <label for="X3">X3 Wall Area:</label>
                        <input type="number" name="X3" step="0.01" min="0" required>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question4">
                        <div class="info-icon material-icons" title="Total area of the roof of the building (in square meters).">info</div>
                        <label for="X4">X4 Roof Area:</label>
                        <input type="number" name="X4" step="0.01" min="0" required>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question5">
                        <div class="info-icon material-icons" title=" Height of the building from the ground to the roof (in meters)">info</div>
                        <label for="X5">X5 Overall Height:</label>
                        <input type="number" name="X5" step="0.01" min="0" required>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question6">
                        <div class="info-icon material-icons" title="Direction the building faces relative to the north direction (in degrees, between 0 and 360).">info</div>
                        <label for="X6">X6 Orientation:</label>
                        <input type="number" name="X6" step="0.01" min="0" required>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question7">
                        <div class="info-icon material-icons" title="Total area of windows (glazing) in the building (in square meters).">info</div>
                        <label for="X7">X7 Glazing Area:</label>
                        <input type="number" name="X7" step="0.01" min="0" required>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                    </div>
                    <div class="question hidden" id="question8">
                        <div class="info-icon material-icons" title=" How the glazing area is distributed among different sides of the building. Please provide a value of 0 for uniform distribution or 1 for non-uniform distribution.">info</div>
                        <label for="X8">X8 Glazing Area Distribution:</label>
                        <input type="number" name="X8" step="0.01" min="0" required>
                        <button type="button" id="prev-btn" class="prev-btn hidden">Previous</button>
                        <button type="button" id="next-btn" class="next-btn">Next</button>
                        <!-- <button type="submit" id="predict-btn" class="hidden">Predict</button> -->
                    </div>
                    <div class="question hidden" id="question9">
                        <label for="City">Enter Your City</label>
                        <input type="text" name="City" step="0.01" min="0" required>
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

