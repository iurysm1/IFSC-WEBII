function deleteTask(taskId) {
    fetch("/delete-task", {
        method: "POST",
        body: JSON.stringify({ taskId: taskId}),
    }).then((_res) => {
        window.location.href = "/";
    });
}



$('#modalEdit').on('show.bs.modal', function (event) {
    

    const button = $(event.relatedTarget);
    console.log(event.relatedTarget)
    data = button.data();
    const idProduct = data.idproduct;
    const nameProduct = data.nameproduct;
    const precoProduct = data.priceproduct;
    const quantidadeProduct = data.estoqueproduct;
    const fornecedorId = data.productfornecedorid; //pega o id do fornecedor do data do mesmo
    $('#productIdEdit').val(idProduct);
    $('#productNameEdit').val(nameProduct);
    $('#productPriceEdit').val(precoProduct);
    $('#productEstoqueEdit').val(quantidadeProduct);
    $('#productFornecedorIdEdit').val(fornecedorId);

    const fornecedores = document.querySelectorAll('.inputFornecedor')

    fornecedores.forEach(function(fornecedorAtual){
        console.log(fornecedorAtual.id+" / "+fornecedorId)
        if(fornecedorAtual.id=="f"+fornecedorId){
            fornecedorAtual.checked = true;
        }else{
            fornecedorAtual.checked = false;
        }

        //passa por todos os elementos da lista comparando o id do fornecedor do produto com o id do input  (mesma logica usada no exemplo da ToDo list que fizemos em aula)
    })
    
  });