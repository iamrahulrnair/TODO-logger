

          // Create a "close" button and append it to each list item
          var myNodelist = document.getElementsByTagName("LI");
          var i;
          for (i = 0; i < myNodelist.length; i++) {
            var span = document.createElement("SPAN");
            var txt = document.createTextNode("\u00D7");
            span.className = "close";
            span.appendChild(txt);
            myNodelist[i].appendChild(span);
          }
          
          // Click on a close button to hide the current list item
          var close = document.getElementsByClassName("close");
          var i;
          for (i = 0; i < close.length; i++) {
            close[i].onclick = function() {
              var div = this.parentElement;
              div.style.display = "none";
            }
          }
          
          // Add a "checked" symbol when clicking on a list item
          var list = document.querySelector('ul');
          list.addEventListener('click', function(ev) {
            if (ev.target.tagName === 'LI') {
              ev.target.classList.toggle('checked');
            }
          }, false);
          
          // Create a new list item when clicking on the "Add" button
          function newElement() {
            var li = document.createElement("li");
            var inputValue = document.getElementById("myInput").value;
            var t = document.createTextNode(inputValue);
            li.appendChild(t);
            if (inputValue === '') {
              alert("You must write something!");
            } else {
              document.getElementById("myUL").appendChild(li);
            }
            document.getElementById("myInput").value = "";
            var span = document.createElement("SPAN");
            var txt = document.createTextNode("\u00D7");
            span.className = "close";
            span.appendChild(txt);
            li.appendChild(span);
          
            for (i = 0; i < close.length; i++) {
              close[i].onclick = function() {
                var div = this.parentElement;
                div.style.display = "none";
              }
            }
          
          }
          // my code
          
          var listy=document.getElementsByTagName("li")
          
          
          
           var obj={
          
              }
          let queue= []
          let submit=document.querySelector(".submit")
          let save=document.querySelector(".save")
          var dataObjectBase64
          let objstring
          var hiddenfield=document.querySelector(".hiddenfield")
          var listlength=document.querySelector(".listlength")
          
          if(hiddenfield.value){

          
            let dataobjectfrombase64=atob(hiddenfield.value)
            objstring=JSON.parse(dataobjectfrombase64)
            console.log(objstring)
            let i=0
            while(i<objstring['user-data'].length){
          
              var li = document.createElement("li");
              var texty=objstring['user-data'][i]
              document.getElementById("myUL").appendChild(li);
              console.log(texty);
              if(texty.charAt(texty.length-1)=='x'){
                var updated_text=texty.slice(0,-1)
              }
  
              if(texty.charAt(texty.length-1)=='C'){
                li.classList.add('checked')
                 updated_text=texty.slice(0,-1)
                if(updated_text.charAt(updated_text.length-1)=='x'){
                  var updated_text=updated_text.slice(0,-1)
                }
                texty= updated_text
                li.textContent=texty
              }else{
                
                li.textContent=texty
              }
          
            i++
          }
          }
    save.addEventListener('click',function(e){
          let lengthy=document.getElementsByTagName("li")
             let queue= []
             hiddenfield.value=""
   
             for(let i=0;i<listy.length;i++){
               let element= listy[i].textContent
              //  console.log("element text:",element[element.length-1])
              //  console.log("element sliced:",element=element.slice(0,-1))

              element=element.slice(0,-1)

               if(listy[i].classList.contains("checked")){
                 
                 queue.push(element+'C')
                 console.log(queue);
                }else{
                queue.push(element)
                  console.log(queue);
  
               }
               listlength.value=lengthy.length.toString();
              
    
              
          }
          obj['user-data']=queue
          
          objstring=JSON.stringify(obj)
          dataObjectBase64=btoa(objstring)
          hiddenfield.value=dataObjectBase64
        })


   // call the function, so as to run the scripts again on the page
   
          
          


        var myNodelist = document.getElementsByTagName("LI");
        var i;
        for (i = 0; i < myNodelist.length; i++) {
          var span = document.createElement("SPAN");
          var txt = document.createTextNode("\u00D7");
          span.className = "close";
          span.appendChild(txt);
          myNodelist[i].appendChild(span);
        }
        
        // Click on a close button to hide the current list item
        var close = document.getElementsByClassName("close");
        var i;
        for (i = 0; i < close.length; i++) {
          close[i].addEventListener('click',function() {
            var div = this.parentElement
            div.style.display = "none";
            div.remove()
          })}
          