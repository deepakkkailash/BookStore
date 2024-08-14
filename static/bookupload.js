const perstagequery = (stage,jsonObj)=>{
    let space = document.getElementById('ForTheUploadQuestion')
    console.log(stage,'da');
    if(stage==4){
        let children = document.body.children;
        let bookuploadform = document.getElementById('bookuploadform')
        for(var i of children){
            if(i==bookuploadform){
                i.classList.remove('z-50');
                i.classList.remove('opacity-100');
                i.classList.add('opacity-0')
                i.classList.add('z-0')
            }
            i.style.removeProperty('filter');
             i.classList.remove('z-0');
             i.classList.add('z-50')
        }

        return None


    }
    switch(stage){
        case 0:
            var label = document.createElement('label')
            label.innerText = 'Hello. Lets Upload Your book';
            space.appendChild(label)
            setTimeout(()=>{
                console.log('ashdaidh');
                space.removeChild(label)
                return perstagequery(stage+1,jsonObj)

            },3000)
            break;
        case 1:
            var label = document.createElement('label');
            label.innerText = 'Enter the name of your book'
            let temp = document.createElement('input');
            temp.setAttribute('type','text');
            space.appendChild(label)
            space.appendChild(temp)
            temp.addEventListener('change',()=>{
                jsonObj['bookname']=temp.value;
                space.removeChild(label);
                space.removeChild(temp);
                return perstagequery(stage+1,jsonObj)

            })
            break;

        case 2:
            var label = document.createElement('label')
            label.innerText = 'Upload the PDF file of your book!';
            let file = document.createElement('input');
            file.setAttribute('type','file')
            let submitbtn=  document.createElement('input');
            submitbtn.setAttribute('type','submit')
            space.appendChild(label)
            space.appendChild(file)
            space.appendChild(submitbtn)
            submitbtn.addEventListener('click',()=>{
                jsonObj['bookcontent']=file.files[0]
                  space.removeChild(label)
                  space.removeChild(file)
                  space.removeChild(submitbtn)
                return perstagequery(stage+1,jsonObj)

            })
            break;
        case 3:
            var label = document.createElement('label')
            label.innerText = 'Enter the name as You would like to be called?'
            let nameinp = document.createElement('input');
            nameinp.setAttribute('type','text')
            nameinp.value = window.shareddata;
            space.appendChild(label)
            space.appendChild(nameinp)
            nameinp.addEventListener('change',()=>{
                jsonObj['bookname']=nameinp.value;
                space.removeChild(label);
                space.removeChild(nameinp);
                return perstagequery(stage+1,jsonObj)

            })
            break;


    }


}
document.getElementById('BeaAuthorofyourownStory').addEventListener('click',()=>{
        console.log("click")
         let children = document.body.children;
         let bookuploadform = document.getElementById('bookuploadform')
         for(const i of children){
            if(i==bookuploadform){
                continue
            }
            else{
                i.classList.add('z-0');
                i.style.filter = 'blur(8px)'
            }
         }
         bookuploadform.classList.remove('z-0')
         bookuploadform.classList.remove('opacity-0')
         bookuploadform.classList.add('opacity-100')
         bookuploadform.classList.add('z-50');
         let stage = 0;
         let tobeuploaded = await perstagequery(stage,{});

         for (var i in tobeuploaded){
            console.log(i,tobeuploaded[i]);
         }
})



