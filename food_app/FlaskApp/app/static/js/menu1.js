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

let items=[
{Name:"dal-rise",Category:"Veg_cas",Price:"80/-"},
{name:"Fried-rise",cat:"Veg_cas",Price:"70/-"},
{name:"Veg-biryani",cat:"Veg_spcl",Price:"120/-"},
{name:"Shahi-paneer",cat:"Veg_spcl",Price:"110/-"},
{name:"Chikan-biryani",cat:"Non-veg",Price:"90/-"},
]

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

let table = document.querySelector("table");
let data = Object.keys(items[0]);
generateTableHead(table, data);
generateTable(table, items);
cur_day(table,n);