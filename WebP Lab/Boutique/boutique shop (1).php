<!DOCTYPE html>
<html>
<head>
  <title>Boutique Shop</title>
  <link rel="stylesheet" type="text/css" href="b.css">
</head>
<body>
  <center><h1>WELCOME TO BOUTIQUEEE....</h1></center>
  <marque><h4>Try it,Wear it,Love it</h4><marque>
  <div class="topnav">
  
  <div class="topnav-right">
    <a class="active" href="cart\ind.php">MATERIALS</a>
    
  </div>
  </div>
 <meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial;
  margin: 0;
}

* {
  box-sizing: border-box;
}

img {
  vertical-align: middle;
}

/* Position the image container (needed to position the left and right arrows) */
.container {
  position: relative;
}

/* Hide the images by default */
.mySlides {
  display: none;
}

/* Add a pointer when hovering over the thumbnail images */
.cursor {
  cursor: pointer;
}

/* Next & previous buttons */
.prev,
.next {
  cursor: pointer;
  position: absolute;
  top: 40%;
  width: auto;
  padding: 16px;
  margin-top: -50px;
  color: white;
  font-weight: bold;
  font-size: 20px;
  border-radius: 0 3px 3px 0;
  user-select: none;
  -webkit-user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover,
.next:hover {
  background-color: rgba(0, 0, 0, 0.8);
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* Container for image text */
.caption-container {
  text-align: center;
  background-color: #222;
  padding: 2px 16px;
  color: white;
}

.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Six columns side by side */
.column {
  float: left;
  width: 16.66%;
}

/* Add a transparency effect for thumnbail images */
.demo {
  opacity: 0.6;
}

.active,
.demo:hover {
  opacity: 1;
}
</style>
<body>

<h2 style="text-align:center">New</h2>

<div class="container">
  <div class="mySlides">
    <div class="numbertext">1 / 6</div>
    <img src="b5.jpg" style="width:25%",height="50%">
  </div>

  <div class="mySlides">
    <div class="numbertext">2 / 6</div>
    <img src="b6.jpg" style="width:25%",height="25%">
  </div>

  <div class="mySlides">
    <div class="numbertext">3 / 6</div>
    <img src="b12.jpg" style="width:50%",height="50%">
  </div>
    
  <div class="mySlides">
    <div class="numbertext">4 / 6</div>
    <img src="b13.jpg" style="width:50%",height="50%">
  </div>

  <div class="mySlides">
    <div class="numbertext">5 / 6</div>
    <img src="b8.jpg" style="width:25%",height="25%">
  </div>
    
  <div class="mySlides">
    <div class="numbertext">6 / 6</div>
    <img src="b10.jpg" style="width:25%",height="25%">
  </div>
    
  <a class="prev" onclick="plusSlides(-1)" >❮</a>
  <a class="next" onclick="plusSlides(1)">❯</a>
<br>
  <div class="caption-container">
    <p id="caption"></p>
  </div>
<h5>
  <div class="row" >
    <div class="column">
      <img class="demo cursor" src="b5.jpg" style="width:100%" onclick="currentSlide(1)" alt="">
    </div>
    <div class="column">
      <img class="demo cursor" src="b6.jpg" style="width:100%" onclick="currentSlide(2)" alt="">
    </div>
    <div class="column">
      <img class="demo cursor" src="b12.jpg" style="width:100%" onclick="currentSlide(3)" alt="">
    </div>
    <div class="column">
      <img class="demo cursor" src="b13.jpg" style="width:100%" onclick="currentSlide(4)" alt="">
    </div>
    <div class="column">
      <img class="demo cursor" src="b8.jpg" style="width:100%" onclick="currentSlide(5)" alt="">
    </div>    
    <div class="column">
      <img class="demo cursor" src="b10.jpg" style="width:100%" onclick="currentSlide(6)" alt="">
    </div>
  </div>
</div>
</h5>

<script>
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}
</script>
<br>
  <div class="caption-container">
    <p id="caption" ><b>Our Brand</b></p>
  </div>

<p><h3>Our Online Boutique offers a wide range of apparel to fit any woman’s unique sense of style. Our clothing and accessories are carefully curated to provide our customers the latest fashions. To keep our customers in style we post new arrivals daily, as well as offer stylist picks to help any indecisive shoppers. Impressions Online Boutique is a fashionista’s best place to create the perfect wardrobe.

Beyond helping you look your best, Impressions Online Boutique strives to make every purchase a positive experience. Our top priorities are excellent customer service, exceptionally quick order processing, ultra fast shipping times, and a hassle-free return policy. We value your feedback, whether positive or constructive and we are continuously working to improve your experience.

If you are a first-time visitor or long-standing customer, we hope you will be thrilled with every aspect of your Impressions Online Boutique shopping experience.

</h3></p>
<br>
  <div class="caption-container">
    <p id="caption" ><b><h4>We offers You the best customer services<h4></b></p>
  </div>





</body>
</html>