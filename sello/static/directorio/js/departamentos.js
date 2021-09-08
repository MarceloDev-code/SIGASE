const ID_MODAL_DIRECTORIO_CONTENIDO = '#modalAgregarDirectorioContenido';
const ID_MODAL_DIRECTORIO = '#modalAgregarDirectorio';
const URL_AGREGAR_DIRECTORIO = '/app/departamentos/(id_departamento)/agregar/directorio/';
const ID_FORMULARIO_AGREGAR_DIRECTORIO = '#id-DirectorioDepartamentoForm';

function modalAgregarDirectorio(data){
    let idModal = ID_MODAL_DIRECTORIO.split("#")[1];
    let contenidoModal = `<div class="modal fade show" id="${idModal}" tabindex="-1" role="dialog" aria-hidden="true">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">Agregar Directorio al departamento 
                    <small> ${data.departamento} </small></h4>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    ${data.form_html}
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
                </div>
            </div>
        </div>
    </div>`;
    $(ID_MODAL_DIRECTORIO_CONTENIDO).html(contenidoModal);
    $(ID_MODAL_DIRECTORIO).modal('show');
}


function submitForm(form){
    let id_departamento = form.find('input[name="departamento"]').val();
    let url = URL_AGREGAR_DIRECTORIO.replace(
        '(id_departamento)',
        id_departamento
    );
    $.ajax({
        type: form.attr('method'),
        url: url,
        data: form.serialize(),
        success: function(data) {
            if (!(data['success'])) {
                if(data['form_html'] !== null){
                    $(form).replaceWith(data['form_html']);
                }
            }
            else {
                alert("Todo se guardo bien..");
                document.location.reload();
            }
        },
        error: function () {
           console.log("Error en la solicitud post");
        }
    });
}


$(function() {

    $(document).on('click', `button[name="agregar-directorio"]`, function () {
        let id_departamento = $(this).parent().find('input[name="id_departamento"]').val();

        let urlAgregarDirectorio = URL_AGREGAR_DIRECTORIO.replace(
            '(id_departamento)',
            id_departamento
        );

        //generar formulario desde servidor (ajax)
        $.get(urlAgregarDirectorio, function (data) {
            if(data['form_html']){
                // crear modal
                modalAgregarDirectorio(data);
            }
        });
    });

    /* Escuchar submit para guardar iniciativa */
    $(document).on('submit', ID_FORMULARIO_AGREGAR_DIRECTORIO, function (e){
        e.preventDefault();
        submitForm($(this));
    });


});
