

function adiciona_dias(dias, dataini) {
   var data = new Date();

   data.setDate(dataini.substr(0,dataini.indexOf("-",0)));
   data.setMonth(dataini.substr(dataini.indexOf("-",1)+1,(dataini.lastIndexOf("-")-dataini.indexOf("-",1) )-1));
   data.setFullYear(dataini.substr(dataini.lastIndexOf("-")+1,4));
   var dataVenc = new Date(data.getTime() + (dias * 24 * 60 * 60 * 1000));
  return dataVenc.getDate() + "-" + (dataVenc.getMonth() ) + "-" + dataVenc.getFullYear();
}

function trocaClasseIcone(icone, antiga, nova) {
   var x = document.getElementsByClassName(antiga); 
   var t = x.length;
   for (var i = 0 ; i < t ; i++) {
   	if(x[i].children[0].className.indexOf(icone) > 0){
   		x[i].className  = nova;
   		i = i-1;
   		t = x.length;
   	}   	
   }
   return;    
}
function calcDias(data_inicio,data_fim){

  var sDate = new Date();
  var eDate = new Date();
  sDate.setDate(data_inicio.substr(0,data_inicio.indexOf("-",0)));
  sDate.setMonth(data_inicio.substr(data_inicio.indexOf("-",1)+1,(data_inicio.lastIndexOf("-")-data_inicio.indexOf("-",1) )-1));
  sDate.setFullYear(data_inicio.substr(data_inicio.lastIndexOf("-")+1,4));

  eDate.setDate(data_fim.substr(0,data_fim.indexOf("-",0)));
  eDate.setMonth(data_fim.substr(data_fim.indexOf("-",1)+1,(data_fim.lastIndexOf("-")-data_fim.indexOf("-",1) )-1));
  eDate.setFullYear(data_fim.substr(data_fim.lastIndexOf("-")+1,4));
  var daysApart = 0
  if(eDate < sDate)
  {
     daysApart = 0;
  }
   else{
      daysApart = Math.round((eDate-sDate)/86400000);
   }
  
  
 return daysApart;
}
function ajustaCSS(){

   trocaClasseIcone('zoom','button btn btn-default btn-secondary','button btn btn-default btn-outline-primary' );

   trocaClasseIcone('trash','button btn btn-default btn-secondary','button btn btn-default btn-outline-danger' );
   trocaClasseIcone('arrow','button btn btn-default btn-secondary','button btn btn-default btn-outline-danger' );
}