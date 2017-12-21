(function(json) { 

	var otdata = JSON.parse(json); 
	return new Date(otdata.tst * 1000).toISOString(); 
})(input)