function deleteObject(objectId, typeOfObject) {
    fetch("/delete-object", {
        method: "POST",
        body: JSON.stringify({ objectId: objectId, typeObject: typeOfObject}),
    }).then((_res) => {
        if(typeOfObject=="produto"){
            window.location.href = "/";
        }else if(typeOfObject=="fornecedor"){
            window.location.href = "/fornecedores";
        }
    });
}

$('#modalEditFornecedor').on('show.bs.modal', function (event) {

    const button = $(event.relatedTarget);
    console.log(event.relatedTarget)
    data = button.data();
    const idFornecedor = data.idfornecedor;
    const nameFornecedor = data.namefornecedor;
    const emailFornecedor = data.emailfornecedor;
    const phoneFornecedor = data.phonefornecedor;
    const siteFornecedor = data.sitefornecedor;

    $('#idEdit').val(idFornecedor);
    $('#razao_socialEdit').val(nameFornecedor);
    $('#emailEdit').val(emailFornecedor);
    $('#telefoneEdit').val(phoneFornecedor);
    $('#siteEdit').val(siteFornecedor);
});

$('#modalEdit').on('show.bs.modal', function (event) {
    

    const button = $(event.relatedTarget);
    console.log(event.relatedTarget)
    data = button.data();
    const idProduct = data.idproduct;
    const nameProduct = data.nameproduct;
    const precoProduct = data.priceproduct;
    const quantidadeProduct = data.estoqueproduct;
    const fornecedorId = data.productfornecedorid; //pega o id do fornecedor do data do botão
    $('#productIdEdit').val(idProduct);
    $('#productNameEdit').val(nameProduct);
    $('#productPriceEdit').val(precoProduct);
    $('#productEstoqueEdit').val(quantidadeProduct);
    $('#productFornecedorIdEdit').val(fornecedorId);

    const fornecedores = document.querySelectorAll('.inputFornecedor')

    fornecedores.forEach(function(fornecedorAtual){
        console.log(fornecedorAtual.id+" / "+fornecedorId)
        if(fornecedorAtual.id=="fe"+fornecedorId){
            fornecedorAtual.checked = true;
        }else{
            fornecedorAtual.checked = false;
        }

        //passa por todos os elementos da lista comparando o id do fornecedor do produto com o id do input  (mesma logica usada no exemplo da ToDo list que fizemos em aula)
    })
    
  });