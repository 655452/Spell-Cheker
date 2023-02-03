
    function gfg_Run(){
            let text=document.getElementById("editor")
            
            let data=text.value
            let new1=data.replace(/[&\/[\\#, +()$~%.'-_":*?<>{}]/g," ");
            text.value=new1

        }
// for live reloading
// let text=document.getElementById("editor")
let editor=document.getElementById("editor")
        let show=document.getElementById('show')
        
        editor.addEventListener('keyup',(e)=>{
            let variable=e.target.value
            let newvariable=" "
            
            let myArray=variable.split(" ")
            // console.log(text.selectionStart)
         
         
          let result= myArray.filter(word=>word.trim().length>0);
            // show.innerHTML=myArray[myArray.length-1]
            // console.log(result[result.length-1])
           

            
          let predicted=Word_predict(result[result.length-1])
          
        })
        async function Word_predict(Word){
            
           let url=`http://127.0.0.1:5000/new/${Word}`;
           const resp=await fetch(url,
           ).then(response=>response.json())
           .then(json=>{
            // console.log("this is from word predict",json)
            let data=json
            show.innerHTML=`<label style="font-weight: 800;color: rgb(53, 87, 2);" for="">Suggested words</label>`
            
            for (let i=0;i<data.length;i++)
            {
                show.innerHTML+=`<li onclick="EnterText(event)" >${data[i]}</li>`
            }
            
           
           })
           
        
            
            
         }
         function EnterText(event){
            console.log(event.target.innerText)
            editor.value=editor.value+"  "+event.target.innerText
         }

        //  live reloading end

        
    // for Rules section rember it in predict box
    function For_Rules(){
      let  Rules_options=document.getElementById("Rules_options")
      let Rules=document.getElementById("Rules")
      
      Rules.value=Rules_options.value

    }
    function selecting() {
      let text1 = document.getElementById("text1")
      let text2 = document.getElementById("text2")
      text2.innerHTML = ""
      text2.innerHTML = text1.innerHTML
      console.log(text1.innerHTML, text2.innerHTML)
    }

    // x and y axis 
    function showCoordinates(event) {
      let x = event.clientX;
      let y = event.clientY;
      console.log(x, y)
      let predict = document.getElementById("predict")

      predict.style.transform = `translate(${x - 700}%,${y + 600}%)`;
      console.log(predict.style.transform)

    }

    let Add_d = document.getElementById("Add_D")
    Add_d.addEventListener("mouseout", () => {
      let editor = document.getElementById("editor");

      Add_d.value = editor.value
    })

    function copyText() {
      let editor = document.getElementById("text2");
      // editor.select();
      // editor.select();
      navigator.clipboard.writeText(editor.value);
        console.log(editor.innerText)
      // alert("Copied text is "+editor.value)
      // document.execCommand("copy");
    }

    //  async function pasteText() {

    //     let editor = document.getElementById("editor");
    //     // editor.focus();
    //     const text=await navigator.clipboard.readText()
    //     editor.value+=text
    //     // console.log(text)
    //     // document.execCommand("paste");
    //   }

    function uploadFile() {
      let input = document.getElementById("file-input");
      let file = input.files[0];
      let reader = new FileReader();


      reader.onloadend = function () {
        let editor = document.getElementById("editor");
        editor.innerText = reader.result;
      }
      if (file) {
        reader.readAsText(file);
      }

    }

    function changeText() {
      let select = document.getElementById('predict')
      let obj = document.getElementById('editor')
      obj.value = select.value
    }
    function upadate() {
      let text = document.getElementById('text')
      let obj = document.getElementById('editor')
      obj.value = text.innerText
    }
 