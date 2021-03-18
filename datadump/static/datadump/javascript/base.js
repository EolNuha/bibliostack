function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("content").style.marginRight = "250px";
  document.getElementById("openbtn").style.display = "none";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("openbtn").style.display = "block";
  document.getElementById("content").style.marginRight= "0";
}