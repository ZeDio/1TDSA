function Butao({texto}: {texto : string}){
    const estilo ={
        backgroundColor:"#131313",
        color: "#fff",
        padding: "0.5rem 1rem",
        boder: "none",
        cursor: "pointer"
    }

    return(
        <>
            <button style={estilo}>{texto}</button>
        </>
    )
} 
export default Butao;