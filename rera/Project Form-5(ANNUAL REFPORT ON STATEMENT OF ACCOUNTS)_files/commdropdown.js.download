var _ctxpath='';
 
    //stateID

function reloadChildDropdown(sl){
	
	if(sl.value!='' && sl.value!='0' ){
		
		
	   var cid='District-'+$(sl).attr("id");
	  
		$('#'+cid+' option').each(function() {
		    if ( $(this).val() != '0' && $(this).val() != '') {
		        $(this).remove();
		    }
		});
		
		new reloadChildDropdownFun(sl.value,cid);
	}
}


 reloadChildDropdownFun =function (v,c){
	

this.param='stateID='+v+'&CID='+c;
this.callbackfun=function(xml){

	$(xml).find('DISTRICT').each(function(){
		var cd=$(this).attr("CID");
		
		$('#'+cd).append('<option value="'+$(this).attr("ID")+'" >'+$(this).attr("NAME")+'</option>');
		
	});
};
$.ajax({  
    type: "POST",  
    url: _ctxpath+"getDistrictByStateID",  
    data: this.param,
    dataType: "xml",
    async: false,
    success:this.callbackfun,
    error: function(){alert("Error Found.");}
});




};


function reloadSubDistrict(sl){
	if(sl.value!='' && sl.value!='0' ){
		

	   var cid='SubDistrict-'+$(sl).attr("id");
		$('#'+cid+' option').each(function() {
		    if ( $(this).val() != '0' && $(this).val() != '') {
		        $(this).remove();
		    }
		});
		
		
		new reloadSubDistFun(sl.value,cid);
	}
}


reloadSubDistFun =function (v,c){
	

this.param='DSTID='+v+'&CID='+c;
this.callbackfun2=function(xml){

	$(xml).find('SUBDISTRICT').each(function(){
		var cd=$(this).attr("CID");
		$('#'+cd).append('<option value="'+$(this).attr("ID")+'" >'+$(this).attr("NAME")+'</option>');
		
	});
};
$.ajax({  
   type: "POST",  
   url: _ctxpath+"getSubDistrictByDstID",  
   data: this.param,
   dataType: "xml",
   async: false,
   success:this.callbackfun2,
   error: function(){alert("Error Found.");}
});




};






