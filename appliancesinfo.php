<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Appliances Model Information</title>
    <link rel="stylesheet" href="css/appliancesinfo.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">

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
            <h1>Appliances Model Information</h1>
        </header>
        
        <section>
            <div class="intro-container">
                <div class="intro-content">
                    <p class="intro">Before Predicting, look about the feature and Prediction Model makes</p>
                    <p>Our advanced predictive model leverages machine learning algorithms to accurately estimate the energy usage of appliances in buildings based on various environmental and operational factors. By analyzing key parameters such as temperature, humidity, and weather conditions, the model provides invaluable insights into optimizing energy consumption.</p>
                    <br>
                    <p>By harnessing the power of data-driven predictions of this model, architects, engineers, and building professionals can:</p>
                    <ul class="benefits-list">
                        <li>Design more energy-efficient buildings by optimizing appliance usage</li>
                        <li>Identify opportunities for energy savings and cost reduction</li>
                        <li>Improve sustainability and reduce environmental impact</li>
                        <li>Enhance occupant comfort and well-being</li>
                    </ul>
                </div>
                <div class="intro-image-div">
                    <img class="intro-image"src="asset/bulb-glowing.png" alt="Image">
                </div>
                
                <!-- Button to scroll to Prediction Info -->
                <a href="#prediction-info" class="scroll-btn">Learn More</a>
            </div>
            
            <div class="prediction-info-container" id="prediction-info">
                <h2>Predictions:</h2>
                <div class="prediction-content">
                    <p class="prediction-info">The model estimates the energy usage of appliances in buildings. This includes the energy consumed by various appliances such as lights, kitchen appliances, electronics, etc. Understanding these predictions can help optimize energy usage and reduce overall consumption.</p>
                    <img class="prediction-image"src="asset/energy-effecient-home.png" alt="Image">
                </div>
                <div class="prediction-image">
                    
                </div>
                <!-- Button to scroll to Features -->
                <a href="#features" class="scroll-btn">Explore Features</a>
            </div>
            
            <div class="features-container" id="features">
                <h2>Features:</h2>
                <ul class="feature-list">
                    <li><strong class="feature-room">Lights:</strong> Energy use of light fixtures in the house (in Wh).</li>
                    <li><strong class="feature-room">Kitchen:</strong> 
                        <ul>
                            <li><strong>T1:</strong> Temperature in kitchen area (in Celsius).</li>
                            <li><strong>RH_1:</strong> Humidity in kitchen area (in %).</li>
                        </ul>
                    </li>
                    <li><strong class="feature-room">Living Room:</strong> 
                        <ul>
                            <li><strong>T2:</strong> Temperature in living room area (in Celsius).</li>
                            <li><strong>RH_2:</strong> Humidity in living room area (in %).</li>
                        </ul>
                    </li>
                    <li><strong class="feature-room">Laundry Room:</strong> 
                        <ul>
                            <li><strong>T3:</strong> Temperature in laundry room area (in Celsius).</li>
                            <li><strong>RH_3:</strong> Humidity in laundry room area (in %).</li>
                        </ul>
                    </li>
                    <li><strong class="feature-room">Office Room:</strong> 
                        <ul>
                            <li><strong>T4:</strong> Temperature in office room (in Celsius).</li>
                            <li><strong>RH_4:</strong> Humidity in office room (in %).</li>
                        </ul>
                    </li>
                    <li><strong class="feature-room">Bathroom:</strong> 
                        <ul>
                            <li><strong>T5:</strong> Temperature in bathroom (in Celsius).</li>
                            <li><strong>RH_5:</strong> Humidity in bathroom (in %).</li>
                        </ul>
                    </li>
                    <li><strong class="feature-room">Ironing Room:</strong> 
                        <ul>
                            <li><strong>T7:</strong> Temperature in ironing room (in Celsius).</li>
                            <li><strong>RH_7:</strong> Humidity in ironing room (in %).</li>
                        </ul>
                    </li>
                    <li><strong class="feature-room">Teenager Room 2:</strong> 
                        <ul>
                            <li><strong>T8:</strong> Temperature in teenager room 2 (in Celsius).</li>
                            <li><strong>RH_8:</strong> Humidity in teenager room 2 (in %).</li>
                        </ul>
                    </li>
                    <li><strong class="feature-room">Parents Room:</strong> 
                        <ul>
                            <li><strong>T9:</strong> Temperature in parents room (in Celsius).</li>
                            <li><strong>RH_9:</strong> Humidity in parents room (in %).</li>
                        </ul>
                    </li>
                    <li><strong class="feature-room">Outside:</strong> 
                        <ul>
                            <li><strong>T_out:</strong> Temperature outside the building (in Celsius).</li>
                            <li><strong>Press_mm_hg:</strong> Pressure outside the building (in mm Hg).</li>
                            <li><strong>RH_out:</strong> Humidity outside the building (in %).</li>
                            <li><strong>Windspeed:</strong> Windspeed outside the building (in m/s).</li>
                            <li><strong>Visibility:</strong> Visibility outside the building (in km).</li>
                            <li><strong>Tdewpoint:</strong> Dew point temperature outside the building (in Celsius).</li>
                        </ul>
                    </li>
                    <li><strong class="feature-room">Random Variables:</strong> 
                        <ul>
                            <li><strong>rv1, rv2:</strong> Random variables (nondimensional).</li>
                        </ul>
                    </li>
                </ul>
                <!-- Button to fill out the form -->
                <a href="appliances.php" class="fill-form-btn scroll-btn">Ready to optimize appliances energy consumption?</a>
            </div>

        </section>
    </div>
</body>
</html>
