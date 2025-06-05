document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.form')
    const btn = document.querySelector('.btn')
    const warning = document.querySelector('#warning')

    if(form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault()

            if(this.nome.value != '' && this.email.value != ''){
                console.log('Enviado!')
                console.log('Nome enviado:', this.nome.value)
                console.log('Email enviado:', this.email.value)
                
                warning.textContent = 'Dados enviados com sucesso!'
                warning.style.color = '#22c55e';
                
                btn.textContent = 'Enviado!';
                btn.style.backgroundColor = '#22c55e';  
            } else {
                warning.textContent = 'Digite nome e email válidos'
            }

            setTimeout(() => {
                this.reset();
                btn.textContent = 'Enviar';
                btn.style.backgroundColor = '';
            }, 900)

            setTimeout(() => {
                warning.textContent = '';
              }, 2000);
        })
    }
})