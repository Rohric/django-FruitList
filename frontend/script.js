const fetchGetUrl = "http://127.0.0.1:8000/fruits/";

async function fetchTestGet() {
  let result = await fetch(fetchGetUrl);
  let resultToText = await result.text();
  console.log(resultToText);
}

async function showFruitList() {
  const response = await fetch(fetchGetUrl);
  const fruits = await response.json();
  const fruitList = document.getElementById("fruitList");
  fruitList.innerHTML = ""; // Clear existing list

  fruits.forEach((fruit) => {
    const listItem = document.createElement("li");
    listItem.textContent = `Name: ${fruit.name}, Gewicht: ${fruit.gewicht}, Farbe: ${fruit.farbe}`;
    fruitList.appendChild(listItem);
  });
}
