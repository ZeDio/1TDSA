import estilos from'./Mensagem.module.css'

const Mensagem =() =>{
    return(
        <>
            <p className={estilos.paragrafo}>Olá, esse é um componente com CSS Module!</p>
            <p className="paragrafo">Olá, esse é um componente com CSS Global!</p>
        </>
    )
} 
export default Mensagem;