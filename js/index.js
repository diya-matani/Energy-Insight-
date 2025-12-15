function scrollToQuickLink() {
    const quickLinkSection = document.getElementById("quick-link");
    quickLinkSection.scrollIntoView({ behavior: 'smooth' });
}


window.addEventListener('scroll', function() {
    var header = document.querySelector('.navbar');
    var contactSection = document.querySelector('.contact');

    // Adjust the scroll position threshold as needed
    var scrollThreshold = contactSection.offsetTop - header.offsetHeight;

    if (window.scrollY >= scrollThreshold) {
        document.querySelectorAll('.right-nav a').forEach(function(link) {
            link.style.color = '#182527';
        });
    } else {
        header.style.backgroundColor = 'transparent';
        document.querySelectorAll('.right-nav a').forEach(function(link) {
            link.style.color = 'white';
        });
    }
});
