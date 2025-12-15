<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/index.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&display=swap" rel="stylesheet">
    <script src="js/index.js"></script>
    <title>EnergyInsight</title>
</head>

<body>
    <header class="navbar">
        <div class="left-nav">EnergyInsight</div>
        <nav class="right-nav">
            <a href="#main-content">Home</a>
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <!-- Add more navigation links as needed -->
        </nav>
    </header>

    <div class="main-content" id="main-content">
        <span class="prj-name">EnergyInsight</span>
        <div class="main-heading">
            Sustainability Plans
        </div>
        <div class="subheading">
            You Make, We Save.
        </div>
        <button class="btn-learn-more">Learn More</button>
        <div class="arrow-icon" onclick="scrollToQuickLink()">↓</div>
    </div>

    <div class="quick-link" id="quick-link">
        <span class="ql-heading">Quick Links</span>

        <div class="quick-links">
            <a href="#intro" class="links">Quick Introduction</a>
            


            <a href="appliancesinfo.php" class="links">Appliances</a>
            <a href="heatloadinfo.php" class="links">Heat & Cool Load</a>
            <a href="#goal" class="links">Goal</a>
            <!-- <a href="#contact" class="links">Contact</a> -->
        </div>
    </div>
    <div class="intro" id="intro">
        <span class="ql-heading">Problem Statement</span>
        
        <div class="about-us">
            <p>Heating and cooling loads significantly impact the energy efficiency of buildings, presenting a critical challenge in sustainable construction and operation. Addressing the optimal management of these loads is essential to minimize energy consumption, reduce greenhouse gas emissions, and enhance overall building performance.</p>
            <img src="asset\load-calculation-factors-cooling-2.jpg" alt="">
        </div>
    </div>

    <div class="goal" id="goal">
        <span class="ql-heading">Our Goal</span>

    <div class="our-goal">
        <ul>
            <li>To develop a predictive model capable of accurately forecasting the heating and cooling loads of buildings</li>
            <li>The model will leverage historical data, building characteristics, weather information, and other relevant variables to make predictions</li>
            <li>Additionally, the project aims to provide actionable suggestions for optimizing heating and cooling systems based on the predicted loads, thereby improving energy efficiency, reducing operational costs, and enhancing environmental sustainability in buildings.</li>
            <li>Also, we will be able to find the power consumption that would take place due to the appliances that would be used</li>
        </ul>
    </div>

    </div>

    <div class="contact" id="contact">
        <span class="contact-heading">Contact Details</span>
        <div class="contact-content">
            <div>
                <img class="contact-image" src="asset/contact-index.jpg" alt="contact image" srcset="">
            </div>
            <div class="contact-options">
                
                <span class="items">87379767XX</span>
                <span class="items">VIT Bhopal University</span>
                <span class="items">EnergyInsight@gmail.com</span>
                <span class="items">EnergyInsight.com</span>
            </div>
        </div>

    </div>
  
</body>
</html>
