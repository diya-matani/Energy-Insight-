<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heat Load Information</title>
    <link rel="stylesheet" href="css/appliancesinfo.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        /* Smooth scrolling */
        html {
            scroll-behavior: smooth;
        }
    </style>
</head>
<body>
    <header class="navbar">
        <div class="left-nav">EnergyInsight</div>
        <nav class="right-nav">
            <a href="index.php">Home</a>
        </nav>
    </header>
    <div class="container">
        <header>
            <h1>Heat Load Information</h1>
        </header>
        
        <section>
            <div class="intro-container">
                <div class="intro-content">
                    <p class="intro">Before filling out the form, let's understand how this predictive model can revolutionize the way you approach building design and energy consumption:</p>
                    <p>Our advanced predictive model leverages machine learning algorithms to accurately estimate the heating and cooling loads of buildings based on their architectural features. By analyzing key parameters such as relative compactness, surface area, wall area, roof area, overall height, orientation, glazing area, and glazing area distribution, the model provides invaluable insights into a building's energy performance.</p>
                    <p>By harnessing the power of data-driven predictions, architects, engineers, and building professionals can:</p>
                    <ul class="benefits-list">
                        <li>Design more sustainable and energy-efficient buildings from the ground up</li>
                        <li>Optimize the sizing and placement of heating, ventilation, and air conditioning (HVAC) systems</li>
                        <li>Reduce energy costs and environmental impact</li>
                        <li>Improve occupant comfort and well-being</li>
                    </ul>
                </div>

                <div class="intro-image-div">
                    <img class="intro-image"src="asset/common-hvac-questions-2.jpg" alt="Image">
                </div>
                <!-- Button to scroll to Prediction Info -->
                <a href="#prediction-info" class="scroll-btn">Learn More</a>
            </div>
            
            <div class="prediction-info-container" id="prediction-info">
                <h2>Predictions:</h2>
                <p class="prediction-info">The model estimates the heating load and cooling load of buildings. Heating load refers to the amount of heat energy required to maintain a comfortable indoor temperature during cold weather, while cooling load represents the amount of heat that must be removed to keep the indoor temperature comfortable during hot weather.</p>
                <!-- Button to scroll to Features -->
                <div class="pre-image-div">
                    <img class="prediction-image"src="asset/heatloadimage.png" alt="Image">
                </div>
                <a href="#features" class="scroll-btn">Explore Features</a>
            </div>
            
            <div class="features-container" id="features">
                <h2>Features:</h2>
                <ul class="feature-list">
                    <li><strong>Relative Compactness:</strong> Indicates how compact the building is relative to its footprint. Please provide a value between 0.0 and 1.0.</li>
                    <li><strong>Surface Area:</strong> Total surface area of the building envelope (in square meters).</li>
                    <li><strong>Wall Area:</strong> Total area of the external walls of the building (in square meters).</li>
                    <li><strong>Roof Area:</strong> Total area of the roof of the building (in square meters).</li>
                    <li><strong>Overall Height:</strong> Height of the building from the ground to the roof (in meters).</li>
                    <li><strong>Orientation:</strong> Direction the building faces relative to the north direction (in degrees, between 0 and 360).</li>
                    <li><strong>Glazing Area:</strong> Total area of windows (glazing) in the building (in square meters).</li>
                    <li><strong>Glazing Area Distribution:</strong> How the glazing area is distributed among different sides of the building. Please provide a value of 0 for uniform distribution or 1 for non-uniform distribution.</li>
                </ul>
                <!-- Button to fill out the form -->
                <a href="heatcoolload.php" class="fill-form-btn scroll-btn">Ready to optimize your building's energy consumption?</a>
            </div>
        </section>
    </div>
</body>
</html>
