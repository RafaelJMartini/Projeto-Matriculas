window.onload = function(e){
    jsonElements = document.querySelectorAll(".jsonHidden");
    for (let i = 0; i < jsonElements.length; ++i) {
        try {
            jsonText = jsonElements[i].textContent.replace(/'/g, '"');
            jsonText = jsonText.replace(/None/g, "-1");
            obj = JSON.parse(jsonText);

            tabela = document.createElement("table");
            tabela.className = "table table-bordered tabelaMini";

            console.log(obj);
            if("num_matriculados" in obj[0]){
                const linhaHeader = tabela.insertRow();
                linhaHeader.insertCell().appendChild(document.createTextNode("ANO"));
                linhaHeader.insertCell().appendChild(document.createTextNode("MATRICULADOS"));
                for (const cell of obj) {
                    const linhaTabela = tabela.insertRow();
                    const celulaLinhaAno = linhaTabela.insertCell();
                    celulaLinhaAno.appendChild(document.createTextNode(cell.ano));
                    const celulaLinhaMatriculados = linhaTabela.insertCell();
                    celulaLinhaMatriculados.appendChild(document.createTextNode(cell.num_matriculados));
                }
                jsonElements[i].parentElement.appendChild(tabela);
                console.log(linhaTabela);
                console.log(linhaHeader);
            }
        } catch (error) {
            // pass
        }
    }
}