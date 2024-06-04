var d = new Date();
var weekday = new Array(7);
weekday[0] = "Sunday";
weekday[1] = "Monday";
weekday[2] = "Tuesday";
weekday[3] = "Wednesday";
weekday[4] = "Thursday";
weekday[5] = "Friday";
weekday[6] = "Saturday";

var n = weekday[d.getDay()];

function cur_day(table,n) {
  var table = table.createCaption();
  table.innerHTML ="<b>"+ n+"'s menu</b>";
}

let items_mon=[
{Name:"chhole bhature",Category:"Veg",Price:"40/-"},
{name:"aalu parantha",Category:"Veg",Price:"25/-"},
{name:"jalebi rabri",Category:"Veg",Price:"40/-"},
{name:"biryani",Category:"Non-Veg Special",Price:"80/-"},
{name:"Malai kofte",Category:"Veg",Price:"50/-"}]

let items_tue=[
{name:"gazar ka halwa",Category:"Veg",Price:"75/-"},
{name:"masala Dosa",Category:"Veg",Price:"30/-"},
{name:"Upma",Category:"Veg",Price:"55/-"},
{name:"Idali",Category:"Veg",Price:"25/-"},
{name:"wada",Category:"Veg",Price:"30/-"}]

let items_wed=[
{name:"Aloo Gobi",Category:"Veg",Price:"40/-"},
{name:"bhindi masala",Category:"Veg",Price:"35/-"},
{name:"Rajma masala curry",Category:"Veg",Price:"55/-"},
{name:"kachori",Category:"Veg",Price:"25/-"},
{name:"dum aloo",Category:"Veg",Price:"40/-"}]

let items_thu=[
{name:"dal bhati",Category:"Veg",Price:"90/-"},
{name:"dhokla",Category:"Veg",Price:"80/-"},
{name:"dal makhani",Category:"Veg",Price:"60/-"},
{name:"aaloo tikki chat",Category:"Veg",Price:"45/-"},
{name:"chiken tikka masla",Category:"Non-Veg",Price:"90/-"}]

let items_fri=[
{name:"chilli chiken",Category:"Non-Veg",Price:"95/-"},
{name:"butter chiken",Category:"Non-Veg",Price:"110/-"},
{name:"pav bhaji",Category:"Veg",Price:"35/-"},
{name:"kadai paneer",Category:"Veg",Price:"60/-"},
{name:"tandoori chiken",Category:"Non-Veg",Price:"80/-"}]

let items_sat=[
{name:"kakori kabab",Category:"Non-Veg",Price:"40/-"},
{name:"vada pav",Category:"Veg",Price:"40/-"},
{name:"omellet",Category:"Non-Veg",Price:"20/-"},
{name:"Rogan josh",Category:"Veg",Price:"80/-"},
{name:"Palak paneer",Category:"Veg",Price:"55/-"}]

function generateTableHead(table, data) {
  let thead = table.createTHead();
  let row = thead.insertRow();
  for (let key of data) {
    let th = document.createElement("th");
    let text = document.createTextNode(key);
    th.appendChild(text);
    row.appendChild(th);
  }
}

function generateTable(table, data) {
  for (let element of data) {
    let row = table.insertRow();
    for (key in element) {
      let cell = row.insertCell();
      let text = document.createTextNode(element[key]);
      cell.appendChild(text);
    }
  }
}

let table = document.getElementById("main_course");
let data = Object.keys(items_mon[0]);
if(n=="Monday"){
  generateTableHead(table, data);
  generateTable(table, items_mon);
}
if(n=="Tuesday"){
  generateTableHead(table, data);
  generateTable(table, items_tue);
}
if(n=="Wednesday"){
  generateTableHead(table, data);
  generateTable(table, items_wed);
}
if(n=="Thursday"){
  generateTableHead(table, data);
  generateTable(table, items_thu);
}
if(n=="Friday"){
  generateTableHead(table, data);
  generateTable(table, items_fri);
}
if(n=="Saturday"){
  generateTableHead(table, data);
  generateTable(table, items_sat);
}
cur_day(table,n);

$("table tr").hide();
$("table tr").each(function(index){
  $(this).delay(index*500).show(700);
});