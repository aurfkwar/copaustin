document.addEventListener("DOMContentLoaded", function(event) { 


  var acc = document.getElementsByClassName("accordion");
  var panel = document.getElementsByClassName('panel');
  
  for (var i = 0; i < acc.length; i++) {
      acc[i].onclick = function() {
          var setClasses = !this.classList.contains('active2');
          setClass(acc, 'active2', 'remove');
          setClass(panel, 'show', 'remove');
  
          if (setClasses) {
              this.classList.toggle("active2");
              this.nextElementSibling.classList.toggle("show");
          }
      }
  }
  
  function setClass(els, className, fnName) {
      for (var i = 0; i < els.length; i++) {
          els[i].classList[fnName](className);
      }
  }
  
  });

  