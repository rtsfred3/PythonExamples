window.onload = function () {
  var temp = JSON.parse(document.getElementById('d').innerHTML.toString().replace(/'/g,'"'));
  var total = 0;
  for(var i = 0; i < temp.length; i++){
    total += temp[i]['y'];
  }

  for(var i = 0; i < temp.length; i++){
    temp[i]['y'] = Math.floor((temp[i]['y']/total)*10000)/100;
  }

  var options = {
    title: { text: "Customers and number of new leads" },
    animationEnabled: true,
    data: [{
      type: "pie",
      startAngle: 40,
      toolTipContent: "<b>{label}</b>: {y}%",
      showInLegend: "true",
      legendText: "{label}",
      indexLabelFontSize: 16,
      indexLabel: "{label} - {y}%",
      dataPoints: temp
    }]
  };
  $("#chartContainer").CanvasJSChart(options);
}
