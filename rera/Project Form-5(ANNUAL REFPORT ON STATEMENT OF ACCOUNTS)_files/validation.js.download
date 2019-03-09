var _validationOutput = true;

function validateForm(frm) {

	_validationOutput = true;
	$(frm).find('.requiredValFld').each(function() {

		if (!isDisabled(this)) {

			var msg = $(this).parent().find('.requiredValFldMsg').html();
			if ($(this).is('input')) {
				var typ = $(this).attr('type');
				if (typ == 'radio' || typ == 'RADIO') {
					if (!requiredradio(this, msg)) {
						_validationOutput = false;
						return _validationOutput;
					}

				} else if (typ == 'checkbox' || typ == 'CHECKBOX') {

					if (!requiredOption(this, msg)) {
						_validationOutput = false;
						return _validationOutput;
					}
				} else if (typ != 'hidden' && typ != 'HIDDEN') {

					if (!requiredValField(this, msg)) {
						_validationOutput = false;
						return _validationOutput;
					}

				}

			} else if ($(this).is('select')) {

				if (!requiredValSelect(this, msg)) {
					_validationOutput = false;
					return _validationOutput;
				}
			} else if ($(this).is('textarea')) {
				if (!requiredValField(this, msg)) {
					_validationOutput = false;
					return _validationOutput;
				}
			}

		}
	});
	if (_validationOutput) {
		$(frm).find('.requiredValSelctFld').each(function() {
			var msg = $(this).parent().find('.requiredValFldMsg').html();
			if (!isDisabled(this)) {
				if (!requiredValSelectWithBlank(this, msg)) {
					_validationOutput = false;
					return _validationOutput;
				}
			}

		});
	}
	if (_validationOutput) {
		$(frm).find('.numericValFld').each(function() {
			if (!isDisabled(this)) {
				if (!isNumber22(this)) {
					_validationOutput = false;
					return _validationOutput;
				}
			}

		});
	}
	if (_validationOutput) {
		$(frm).find('.mobileValFld').each(function() {
			if (!isDisabled(this)) {
				if (!checkMobile(this)) {
					_validationOutput = false;
					return _validationOutput;
				}
			}

		});
	}

	if (_validationOutput) {
		$(frm).find('.landlineValFld').each(function() {
			if (!isDisabled(this)) {
				if (!checkLandline(this)) {
					_validationOutput = false;
					return _validationOutput;
				}
			}

		});
	}

	if (_validationOutput) {
		$(frm).find('.panNoValFld').each(function() {
			if (!isDisabled(this)) {
				if (!checkPAN(this)) {
					_validationOutput = false;
					return _validationOutput;
				}
			}

		});
	}

	if (_validationOutput) {
		$(frm).find('.aadhaarNoValFld').each(function() {
			if (!isDisabled(this)) {
				if (!checkAadhaar(this)) {
					_validationOutput = false;
					return _validationOutput;
				}
			}

		});
	}

	if (_validationOutput) {
		$(frm).find('.pinCodeValFld').each(function() {
			if (!isDisabled(this)) {
				if (!checkPin(this)) {
					_validationOutput = false;
					return _validationOutput;
				}
			}

		});
	}

	

	if (_validationOutput) {
		$(frm).find('.decimalValFld').each(function() {
			// alert(".decimalValFld......................");
			if (!isDisabled(this)) {
				// alert(".decimalValFld...........1111111");
				if (!isDecimal(this)) {
					// alert(".decimalValFld........2222");
					_validationOutput = false;
					return _validationOutput;
				}
			}
		});
	}

	if (_validationOutput) {
		$(frm).find('.emailValFld').each(function() {
//			alert("in _validationOutput emailValFld");
			if (!isDisabled(this)) {

				if (!validateEmail(this)) {
//					alert("in _validationOutput emailValFld 11SSSS");
					_validationOutput = false;
					return _validationOutput;
				}
			}


		});
	}

	if (_validationOutput) {
		$(frm).find('.onlycharValFld').each(function() {
			if (!isDisabled(this)) {
				if (!isCharacterFun(this)) {
					_validationOutput = false;
					return _validationOutput;
				}
			}
		});
	}

	if (_validationOutput) {
		$(frm).find('.alphanumericValFld').each(function() {
			if (!isDisabled(this)) {
				if (!isAlphaNumeberFun(this)) {
					_validationOutput = false;
					return _validationOutput;
				}
			}
		});
	}
	
	if (_validationOutput) {
		$(frm).find('.specialCharValFld').each(function() {
			if (!isDisabled(this)) {
				if (!isSpecialCharacterFun(this)) {
					_validationOutput = false;
					return _validationOutput;
				}
			}
		});
	}
	if (_validationOutput) {
		$(frm).find('.ifscFldVal').each(function() {
			if (!isDisabled(this)) {
				if (!checkIfsc(this)) {
					_validationOutput = false;
					return _validationOutput;
				}
			}
		});
	}
//checkIfsc
	return _validationOutput;
}

function isDisabled(fld) {
	var flg = false;
	var part = fld;
	var dis = $(fld).css('display');
	var x = 0;
	while ($(part).parent() && x < 12 && !$(part).hasClass('Main_containner')) {
		if ( dis == 'none') {
			return true;
		}
		part = $(part).parent();
		dis = $(part).css('display');
		x = x + 1;
	}

	return flg;
}

function requiredValField(fld, msg) {
	var val = $(fld).val();
	if (val == '') {
		alert(msg);
		$(fld).focus();
		return false;
	}
	return true;
}


function requiredValSelectWithBlank(fld, msg) {
	var val = $(fld).val();
	if (val == '') {

		if($(fld).closest('form').hasClass("allowzero") && val == '0') {
			return true;
		} 
		alert(msg);
		$(fld).focus();
		return false;
	}
	return true;
}
function requiredValSelect(fld, msg) {
	var val = $(fld).val();
	if (val == '0' || val == '') {

		if($(fld).closest('form').hasClass("allowzero") && val == '0') {
			return true;
		} 
		alert(msg);
		$(fld).focus();
		return false;
	}
	return true;
}

function requiredradio(fld, msg) {
	var st = $(fld).attr('name');
	var flg = false;

	var fd = document.getElementsByName(st);
	if (fd && fd.length > 0) {

		for (var x = 0; x < fd.length; x = x + 1) {

			if (fd[x].checked) {
				flg = true;
			}
		}
	}
	if (!flg) {
		alert(msg);
		$(fld).focus();
		return false;
	}
	return true;
}

function requiredOption(fld, msg) {
	if (!$(fld).prop('checked')) {
		alert(msg);
		$(fld).focus();
		return false;
	}
	return true;
}

function checkLandline(fld) {
	var obj = $(fld).val();
	var char = /^\d{6,10}$/;
	if (obj != '') {
		if (!obj.match(char)) {
			alert("Please enter (6-10) digit Landline No.");
			$(fld).focus();
			return false;
		}
	}

	return true;
}

function checkYear(fld) {
	var obj = $(fld).val();
	var char = /^\d{4}$/;
	if (obj != '') {
		if (!obj.match(char)) {
			alert("Please enter 4 digit Year.");
			$(fld).focus();
			return false;
		}
	}
	return true;
}

function checkIfsc(fld) {
	var obj = $(fld).val();
	//var char = /^[A-Za-z]{4}[0-9]{6,7}$/;
//	var char = /^[A-Z]{4}[A-Z0-9]{7}$/;
	var char = /^[A-Z]{4}[0]{1}[A-Z0-9]{6}$/;
	if (obj != '') {
		if (!obj.match(char)) {
			alert("Please enter valid IFSC Code");
			$(fld).focus();
			return false;
		}
	}
	return true;
}

function checkAmount(fld) {
	var obj = $(fld).val();
	var char = /^([0-9]+.)*[0-9]+$/;
	if (obj != '') {
		if (!obj.match(char)) {
			alert("Plese enter amount in decimal.");
			$(fld).focus();
			return false;
		}
	}

	return true;
}

function checkMobile(fld) {
	var obj = $(fld).val();
	var char = /^\d{10}$/;
	if (obj != '') {
		if (!obj.match(char)) {
			alert("Please enter 10 digit Mobile No.");
			$(fld).focus();
			return false;
		}
	}
	return true;
}

function validateDate(stDate, endDate, msg) {
	var dt = $(stDate).val();
	var dt2 = $(endDate).val();


	var splitDt = dt.split('/');
	var splitDt2 = dt2.split('/');
	var DtDate = parseInt(splitDt[0]);
	var DtMo = parseInt(splitDt[1]);
	var DtYr = parseInt(splitDt[2]);
	var Dt2Date = parseInt(splitDt2[0]);
	var Dt2Mo = parseInt(splitDt2[1]);
	var Dt2Yr = parseInt(splitDt2[2]);
	
	//alert("endYr="+Dt2Yr+" startYr="+DtYr+ " DtMo="+DtMo+" Dt2Mo="+Dt2Mo+"  Dt2Date= "+Dt2Date+" DtDate="+DtDate);
	if (DtYr < Dt2Yr) {
		return true;
	}
	
	if (Dt2Yr == DtYr && DtMo < Dt2Mo) {
		return true;
	}
	if (Dt2Yr == DtYr && Dt2Mo == DtMo && DtDate <= Dt2Date) {
		return true;
	}
	alert(msg);
	endDate.focus();
	return false;
}

function checkPin(fld) {
	var obj = $(fld).val();
	var char = /^\d{6}$/;
	if (obj != '') {
		if (!obj.match(char)) {
			alert("Please enter 6 digit Pin Code");
			$(fld).focus();
			return false;
		}
	}
	return true;
}

function checkAadhaar(fld) {
	var obj = $(fld).val();
	var char = /^\d{12}$/;
	if (obj != '') {
		if (!obj.match(char)) {
			alert("Please enter 12 digit Aadhaar No.");
			$(fld).focus();
			return false;
		}
	}
	return true;
}

function checkPAN(fld) {
	obj = fld.value;
	var char = /[A-Z]{5}\d{4}[A-Z]{1}/;
	if (obj != '') {
		if (!obj.match(char)) {
			alert("Please enter valid PAN Number");
			$(fld).focus();
			return false;
		}
	}
	return true;
}

function validateEmail(obj) {
	/*var x = $(obj).val();
	var atpos = x.indexOf("@");
	var dotpos = x.lastIndexOf(".");
	if (atpos < 1 || dotpos < atpos + 2 || dotpos + 2 >= x.length) {
		$(obj).focus();// added by jagdish 12-09-2017
		alert('Please enter a valid Email ID');
		return false;
	}
	return true;*/
	var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;

    if (reg.test(obj.value) == false){
    	$(obj).focus();
    	alert('Please enter a valid Email Id.');
        return false;
    }else{
    	return true;
    }
}

function isNumber22(fld) {
	var obj = $(fld).val();
	var char = /^([0-9]+,)*[0-9]+$/;
	if (obj != '') {
		if (!obj.match(char)) {
			alert("Please enter numeric only.");
			$(fld).focus();
			return false;
		}
	}
	return true;
}

function isDecimal(fld) {
	// alert("isDecimal....."+fld);
	var obj = $(fld).val();
	// var char = /^[0-9]{1,14}\.[0-9]{0,2}$/;
	var char = /^[0-9]+([,.][0-9]+)?$/;//^\d{0,9}(\.\d{1,2})?$
	if (obj != '') {
		// alert("isDecimal..3333"+obj);
		if (!obj.match(char)) {
			// alert("isDecimal..444"+obj);
			alert("Please enter decimal value only.");
			$(fld).focus();
			return false;
		}
	}
	return true;
}

function isAlphaNumeberFun(fld) {
	var obj = $(fld).val();
	var letterNumber = /^[0-9a-zA-Z ]+$/;
	if (obj.match(letterNumber)) {
		return true;
	} else {
		alert("Please enter alphanumeric only");
		$(fld).focus();
		return false;
	}
}

function isSpecialCharacterFun(fld) {
	var obj = $(fld).val();
	var letterNumber = /^[a-zA-Z 0-9\n\r\^\)\(._-\d,+"]+$/g;
	if(obj!=''){
	if (obj.match(letterNumber)) {
		return true;
	} else {
		alert("Special characters are not allowed");
		$(fld).focus();
		return false;
	}
	}
	return true;
}

function isCharacterFun(fld) {
	var obj = $(fld).val();
	var letters = /^[A-Za-z ]+$/;
	if (obj.match(letters)) {
		return true;
	} else {
		alert("Please enter alphabet only.");
		$(fld).focus();
		return false;
	}
}


$(function() {

	$(".numericNotAllowedText").keydown(
			function(e) {
				-1 !== $.inArray(e.keyCode, [ 46, 8, 9, 27, 13 ])
						|| /65|67|86|88/.test(e.keyCode)
						&& (!0 === e.ctrlKey || !0 === e.metaKey)
						|| 35 <= e.keyCode && 40 >= e.keyCode
						|| (e.shiftKey || 48 > e.keyCode || 57 < e.keyCode)
						&& (96 > e.keyCode || 105 < e.keyCode)
						&& e.preventDefault()
			});
})


$(function() {

	$(".stringDescriptionValidate").keydown(
			function(e) {
				var k;
				document.all ? k = e.keyCode : k = e.which;
				return ((k > 64 && k < 91) || (k > 96 && k < 123) || k == 8
						|| k == 32 || k == 37 || k == 38 || k == 39 || k == 40 || k==13 || (k >= 48 && k <= 57));

			});
})

$(function() {
	$('#totalNoOfPlinth').on('change', function(){
        if ($('#totalNoOfPlinth').val() == 'NA') {
                $('#plinth').css("pointer-events","none");
                $('#plinth').prop('class', "form-control input-sm disableText");
                var select = document.getElementById("plinth");
                var options = ["NA"];
                var opt1 = options[0];
                var element = document.createElement("option");
                element.textContent = opt1;
	    		element.value = opt1;
	    		select.appendChild(element);
                $('#plinth').prop('value', 'NA');                
        }else{
        		$('#plinth').css("pointer-events","auto");
                $('#plinth').prop('class', "form-control input-sm requiredValFld disableText");
                $("#plinth option[value='NA']").remove();
        }
    });
	
	$('#totalNoOfPodiums').on('change', function(){
        if ($('#totalNoOfPodiums').val() == 'NA') {
                $('#podiums').css("pointer-events","none");
                $('#podiums').prop('class', "form-control input-sm disableText");
                var select = document.getElementById("podiums");
                var options = ["NA"];
                var opt1 = options[0];
                var element = document.createElement("option");
                element.textContent = opt1;
	    		element.value = opt1;
	    		select.appendChild(element);
                $('#podiums').prop('value', 'NA');
                
        }else{
        		$('#podiums').css("pointer-events","auto");
                $('#podiums').prop('class', "form-control input-sm requiredValFld disableText");
                $("#podiums option[value='NA']").remove();
        }
    });
	
	$('#totalNoOfSlabs').on('change', function(){
        if ($('#totalNoOfSlabs').val() == 'NA') {
                $('#slabs').css("pointer-events","none");
                $('#slabs').prop('class', "form-control input-sm disableText");
                var select = document.getElementById("slabs");
                var options = ["NA"];
                var opt1 = options[0];
                var element = document.createElement("option");
                element.textContent = opt1;
	    		element.value = opt1;
	    		select.appendChild(element);
                $('#slabs').prop('value', 'NA');
                
        }else{
        		$('#slabs').css("pointer-events","auto");
                $('#slabs').prop('class', "form-control input-sm requiredValFld disableText");
                $("#slabs option[value='NA']").remove();
        }
    });
	
});


$(function() {
	if($('#totalNoOfPlinth').val() == 'NA') {
        $('#plinth').css("pointer-events","none");
        $('#plinth').prop('class', "form-control input-sm disableText");
        var select = document.getElementById("plinth");
        var options = ["NA"];
        var opt1 = options[0];
        var element = document.createElement("option");
        element.textContent = opt1;
		element.value = opt1;
		select.appendChild(element);
        $('#plinth').prop('value', 'NA');                
	}else{
		$('#plinth').css("pointer-events","auto");
        $('#plinth').prop('class', "form-control input-sm requiredValFld disableText");
        $("#plinth option[value='NA']").remove();
	}
	
	if ($('#totalNoOfPodiums').val() == 'NA') {
        $('#podiums').css("pointer-events","none");
        $('#podiums').prop('class', "form-control input-sm disableText");
        var select = document.getElementById("podiums");
        var options = ["NA"];
        var opt1 = options[0];
        var element = document.createElement("option");
        element.textContent = opt1;
		element.value = opt1;
		select.appendChild(element);
        $('#podiums').prop('value', 'NA');        
	}else{
		$('#podiums').css("pointer-events","auto");
        $('#podiums').prop('class', "form-control input-sm requiredValFld disableText");
        $("#podiums option[value='NA']").remove();
	}
	
	if ($('#totalNoOfSlabs').val() == 'NA') {
        $('#slabs').css("pointer-events","none");
        $('#slabs').prop('class', "form-control input-sm disableText");
        var select = document.getElementById("slabs");
        var options = ["NA"];
        var opt1 = options[0];
        var element = document.createElement("option");
        element.textContent = opt1;
		element.value = opt1;
		select.appendChild(element);
        $('#slabs').prop('value', 'NA');        
	}else{
		$('#slabs').css("pointer-events","auto");
        $('#slabs').prop('class', "form-control input-sm requiredValFld disableText");
        $("#slabs option[value='NA']").remove();
	}
});


$(function() {
	$('#txtTotalPlinth').on('change', function(){
        if ($('#txtTotalPlinth').val() == 'NA') {
                $('#txtPlinth').css("pointer-events","none");
                $('#txtPlinth').prop('class', "form-control input-sm disableText");
                var select = document.getElementById("txtPlinth");
                var options = ["NA"];
                var opt1 = options[0];
                var element = document.createElement("option");
                element.textContent = opt1;
	    		element.value = opt1;
	    		select.appendChild(element);
                $('#txtPlinth').prop('value', 'NA');                
        }else{
        		$('#txtPlinth').css("pointer-events","auto");
                $('#txtPlinth').prop('class', "form-control input-sm requiredValFld disableText");
                $("#txtPlinth option[value='NA']").remove();
        }
    });
	
	$('#txtTotalPodiums').on('change', function(){
        if ($('#txtTotalPodiums').val() == 'NA') {
                $('#txtPodiums').css("pointer-events","none");
                $('#txtPodiums').prop('class', "form-control input-sm disableText");
                var select = document.getElementById("txtPodiums");
                var options = ["NA"];
                var opt1 = options[0];
                var element = document.createElement("option");
                element.textContent = opt1;
	    		element.value = opt1;
	    		select.appendChild(element);
                $('#txtPodiums').prop('value', 'NA');
                
        }else{
        		$('#txtPodiums').css("pointer-events","auto");
                $('#txtPodiums').prop('class', "form-control input-sm requiredValFld disableText");
                $("#txtPodiums option[value='NA']").remove();
        }
    });
	
	$('#txtTotalSlabs').on('change', function(){
        if ($('#txtTotalSlabs').val() == 'NA') {
                $('#txtSlabs').css("pointer-events","none");
                $('#txtSlabs').prop('class', "form-control input-sm disableText");
                var select = document.getElementById("txtSlabs");
                var options = ["NA"];
                var opt1 = options[0];
                var element = document.createElement("option");
                element.textContent = opt1;
	    		element.value = opt1;
	    		select.appendChild(element);
                $('#txtSlabs').prop('value', 'NA');
                
        }else{
        		$('#txtSlabs').css("pointer-events","auto");
                $('#txtSlabs').prop('class', "form-control input-sm requiredValFld disableText");
                $("#txtSlabs option[value='NA']").remove();
        }
    });
	
});

$(function() {
	
        if ($('#txtTotalPlinth').val() == 'NA') {
                $('#txtPlinth').css("pointer-events","none");
                $('#txtPlinth').prop('class', "form-control input-sm disableText");
                var select = document.getElementById("txtPlinth");
                var options = ["NA"];
                var opt1 = options[0];
                var element = document.createElement("option");
                element.textContent = opt1;
	    		element.value = opt1;
	    		select.appendChild(element);
                $('#txtPlinth').prop('value', 'NA');                
        }else{
        		$('#txtPlinth').css("pointer-events","auto");
                $('#txtPlinth').prop('class', "form-control input-sm requiredValFld disableText");
                $("#txtPlinth option[value='NA']").remove();
        }
	
        if ($('#txtTotalPodiums').val() == 'NA') {
                $('#txtPodiums').css("pointer-events","none");
                $('#txtPodiums').prop('class', "form-control input-sm disableText");
                var select = document.getElementById("txtPodiums");
                var options = ["NA"];
                var opt1 = options[0];
                var element = document.createElement("option");
                element.textContent = opt1;
	    		element.value = opt1;
	    		select.appendChild(element);
                $('#txtPodiums').prop('value', 'NA');
                
        }else{
        		$('#txtPodiums').css("pointer-events","auto");
                $('#txtPodiums').prop('class', "form-control input-sm requiredValFld disableText");
                $("#txtPodiums option[value='NA']").remove();
        }
	
        if ($('#txtTotalSlabs').val() == 'NA') {
                $('#txtSlabs').css("pointer-events","none");
                $('#txtSlabs').prop('class', "form-control input-sm disableText");
                var select = document.getElementById("txtSlabs");
                var options = ["NA"];
                var opt1 = options[0];
                var element = document.createElement("option");
                element.textContent = opt1;
	    		element.value = opt1;
	    		select.appendChild(element);
                $('#txtSlabs').prop('value', 'NA');
                
        }else{
        		$('#txtSlabs').css("pointer-events","auto");
                $('#txtSlabs').prop('class', "form-control input-sm requiredValFld disableText");
                $("#txtSlabs option[value='NA']").remove();
        }
	
});

/*function checkEmailId(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}*/
/*function checkEmailId(emailField){
    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;

    if (reg.test(emailField.value) == false) 
    {
        alert('Invalid Email Address');
        $(emailField).focus();
        return false;
    }
    
    return true;

}*/