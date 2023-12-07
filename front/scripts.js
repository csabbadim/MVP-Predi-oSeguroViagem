
/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/clientes';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.clientes.forEach(item => insertList(item.age,
        item.employment_type,
        item.graduate_or_not,
        item.annual_income,
        item.family_members,
        item.chronic_diseases,
        item.frequent_flyer,
        item.ever_travelled_abroad,
        item.travel_insurance))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()

/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/

const postItem = async (age, employment_type, graduate_or_not,
                        annual_income, family_members, chronic_diseases, 
                        frequent_flyer, ever_travelled_abroad) => {
    
  const formData = new FormData();
  formData.append('age', age);
  formData.append('employment_type', employment_type);
  formData.append('graduate_or_not', graduate_or_not);
  formData.append('annual_income', annual_income);
  formData.append('family_members', family_members);
  formData.append('chronic_diseases', chronic_diseases);
  formData.append('frequent_flyer', frequent_flyer);
  formData.append('ever_travelled_abroad', ever_travelled_abroad);

  console.log('Dados enviados para o backend:', formData);
  let url = 'http://127.0.0.1:5000/cliente';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      if (confirm("Você tem certeza?")) {
        div.remove();
        deleteItem(div);
        alert("Removido!");
      }
    }
  }
}


/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/

const deleteItem = (nomeItem) => {
  console.log(nomeItem)
  age = nomeItem.getElementsByTagName('td')[0].innerHTML
  employment_type = nomeItem.getElementsByTagName('td')[1].innerHTML
  graduate_or_not = nomeItem.getElementsByTagName('td')[2].innerHTML 
  annual_income = nomeItem.getElementsByTagName('td')[3].innerHTML
  family_members = nomeItem.getElementsByTagName('td')[4].innerHTML
  chronic_diseases = nomeItem.getElementsByTagName('td')[5].innerHTML 
  frequent_flyer = nomeItem.getElementsByTagName('td')[6].innerHTML
  ever_travelled_abroad = nomeItem.getElementsByTagName('td')[7].innerHTML
  travel_insurance = nomeItem.getElementsByTagName('td')[8].innerHTML

  //let url = 'http://127.0.0.1:5000/cliente?age=' + age + '&employment_type=' + employment_type + '&graduate_or_not=' + graduate_or_not + '&annual_income=' + annual_income + '&family_members=' + family_members + '&chronic_diseases=' + chronic_diseases + '&frequent_flyer=' + frequent_flyer + '&ever_travelled_abroad=' + ever_travelled_abroad + '&travel_insurance=' + travel_insurance;
  let url = 'http://127.0.0.1:5000/cliente?' +
   'age=' + encodeURIComponent(age) +
   '&employment_type=' + encodeURIComponent(employment_type) +
   '&graduate_or_not=' + encodeURIComponent(graduate_or_not) +
   '&annual_income=' + encodeURIComponent(annual_income) +
   '&family_members=' + encodeURIComponent(family_members) +
   '&chronic_diseases=' + encodeURIComponent(chronic_diseases) +
   '&frequent_flyer=' + encodeURIComponent(frequent_flyer) +
   '&ever_travelled_abroad=' + encodeURIComponent(ever_travelled_abroad) +
   '&travel_insurance=' + encodeURIComponent(travel_insurance);
   console.log(url)
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputAge = document.getElementById("age").value;
  let inputEmploymentType = document.getElementById("employment_type").value;
  let inputGraduateOr0t = document.getElementById("graduate_or_not").value;
  let inputAnnualIncome = document.getElementById("annual_income").value;
  let inputFamilyMembers = document.getElementById("family_members").value;
  let inputChronicDiseases = document.getElementById("chronic_diseases").value;
  let inputFrequentFlyer = document.getElementById("frequent_flyer").value;
  let inputEverTravelledAbroad = document.getElementById("ever_travelled_abroad").value;

      if (
          age === inputAge &&
          employment_type === inputEmploymentType &&
          graduate_or_not === inputGraduateOr0t &&
          annual_income === inputAnnualIncome &&
          family_members === inputFamilyMembers &&
          chronic_diseases === inputChronicDiseases &&
          frequent_flyer === inputFrequentFlyer &&
          ever_travelled_abroad === inputEverTravelledAbroad
      ) {
        alert("Já existe um cliente com o mesmo cadastro.\nCadastre o cliente com informações diferentes.");
      } else if (inputAge === '') { 
        alert("Favor preencher o campo Idade.");
      } else if (inputEmploymentType === '') { 
        alert("Favor preencher o campo Tipo de Emprego.");
      } else if (inputGraduateOr0t === '') { 
        alert("Favor preencher o campo Graduado.");
      } else if (inputAnnualIncome === '') { 
        alert("Favor preencher o campo Salário anual.");
      } else if (inputFamilyMembers === '') { 
        alert("Favor preencher o campo Nº de membros da família.");
      } else if (inputChronicDiseases === '') { 
        alert("Favor preencher o campo doenças crônicas.");
      } else if (inputFrequentFlyer === '') { 
        alert("Favor preencher se viaja frequentemente.");
      } else if (inputEverTravelledAbroad === '') { 
        alert("Favor preencher se já viajou para o exterior.");
      } else if ((inputGraduateOr0t.toLowerCase() !== 'sim' && inputGraduateOr0t.toLowerCase() !== 'não') && inputGraduateOr0t.toLowerCase() !== '') {
        alert('Você precisa preencher se pretende ler com os valores "sim" ou "não"');
            if (sim) {
              sim = 1;
            } else if (não) {
              não = 0;
            }
      } else if ((inputChronicDiseases.toLowerCase() !== 'sim' && inputChronicDiseases.toLowerCase() !== 'não') && inputChronicDiseases.toLowerCase() !== '') {
        alert('Você precisa preencher se pretende ler com os valores "sim" ou "não"');
            if (sim) {
              sim = 1;
            } else if (não) {
              não = 0;
            }
      } else if ((inputFrequentFlyer.toLowerCase() !== 'sim' && inputFrequentFlyer.toLowerCase() !== 'não') && inputFrequentFlyer.toLowerCase() !== '') {
        alert('Você precisa preencher se pretende ler com os valores "sim" ou "não"');
            if (sim) {
              sim = 1;
            } else if (não) {
              não = 0;
            }
      } else if ((inputEverTravelledAbroad.toLowerCase() !== 'sim' && inputEverTravelledAbroad.toLowerCase() !== 'não') && inputEverTravelledAbroad.toLowerCase() !== '') {
        alert('Você precisa preencher se pretende ler com os valores "sim" ou "não"');
            if (sim) {
              sim = 1;
            } else if (não) {
              não = 0;
            }
      } //else if (isNaN(inputPreg) || isNaN(inputPlas) || isNaN(inputPres) || isNaN(inputSkin) || isNaN(inputTest) || isNaN(inputMass) || isNaN(inputPedi) || isNaN(inputAge)) {
        //alert("Esse(s) campo(s) precisam ser números!");} 
        else {
        insertList(inputAge, inputEmploymentType, inputGraduateOr0t, inputAnnualIncome, inputFamilyMembers, inputChronicDiseases, inputFrequentFlyer, inputEverTravelledAbroad);
        postItem(inputAge, inputEmploymentType, inputGraduateOr0t, inputAnnualIncome, inputFamilyMembers, inputChronicDiseases, inputFrequentFlyer, inputEverTravelledAbroad);
        alert("Cliente adicionado!");
      }
    }


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
  
const insertList = (age, employment_type, graduate_or_not, annual_income, family_members, chronic_diseases, frequent_flyer, ever_travelled_abroad, TravelInsurance) => {
  var item = [age, employment_type, graduate_or_not, annual_income, family_members, chronic_diseases, frequent_flyer, ever_travelled_abroad, TravelInsurance];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);


  document.getElementById("age").value = "";
  document.getElementById("employment_type").value = "";
  document.getElementById("graduate_or_not").value = "";
  document.getElementById("annual_income").value = "";
  document.getElementById("family_members").value = "";
  document.getElementById("chronic_diseases").value = "";
  document.getElementById("frequent_flyer").value = "";
  document.getElementById("ever_travelled_abroad").value = "";

  removeElement();
}