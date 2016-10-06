//Converter Class 
var Converter = require("csvtojson").Converter;
var converter = new Converter({});
var haversine = require('haversine')
 
//end_parsed will be emitted once parsing finished 
converter.on("end_parsed", function (jsonArray) {
   //console.log(jsonArray); //here is your result jsonarray 
   processFile([jsonArray[0]]);
   processFile(jsonArray);
});
 
 
 
//read from file 
require("fs").createReadStream("../datos/eventosAnonimosConLocacion.csv").pipe(converter);
var writeStream=require("fs").createWriteStream("outpuData.json");

var processed = [];
var startsWithNumber = [];
var emptyOnes = [];

function processFile(jsonArray){
   console.log("Total initial records:" + jsonArray.length); 
   
   for(var i=jsonArray.length;i>0;i--){
       var currentAddress = jsonArray[i-1]["Dirección"];
       
       if(currentAddress.length == 0){
           emptyOnes[emptyOnes.length] = jsonArray.splice(i-1,1);
           continue;
       };
        
       if(currentAddress[0].match(/\d/)){
           startsWithNumber[startsWithNumber.length] = jsonArray.splice(i-1,1);
           continue;
       };

       start = {
         latitude: jsonArray[i-1]["Latitud"],
         longitude: jsonArray[i-1]["Longitud"]
       }
        end = { // CLUB FERRO 
          latitude: -34.6200996,
          longitude: -58.4477692
        }   
        
    
       var distance = haversine(start,end); 
       console.log(distance);
       jsonArray[i-1]["Distancia"] = distance;
       
   }
   
   console.log("startsWithNumber length:" );
   console.log(startsWithNumber.length);

   console.log("jsonArray length:" );
   console.log(jsonArray.length);

   console.log("emptyOnes length:" );
   console.log(emptyOnes.length);
   
   writeToFile(jsonArray);
}

var json2csv = require('json2csv');
var fs = require('fs');


function writeToFile(jsonArray){
    
    var fields = ['id','Dirección','Localidad','Provincia','Apellido','Nombre','Sexo','Longitud','Latitud','Distancia']
    var csv = json2csv({ data: jsonArray, fields: fields });
     
    fs.writeFile('file.csv', csv, function(err) {
      if (err) throw err;
      console.log('file saved');
    });
}

/*
1. Posibles excepciones
11 DE SEPTIEMBRE
14 DE JULIO
11 DE NOVIEMBRE
12 DE FEBRERO
15 DE NOVIEMBRE
17 DE AGOSTO
33 DE ORIENTALES
3 DE FEBRERO
*/



