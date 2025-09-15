import Butao from "./components/Butao/Butao"
import Mensagem from "./components/Mensagem/Mensagem"

function App() {
  return (
    <>
      <Mensagem></Mensagem>
      <Butao texto="Cancelar"></Butao>
      <Butao texto="Atualizar"></Butao>
      <Butao texto="Excluir"></Butao>
      <Butao texto="Gravar"></Butao>
    </>
  )
}
export default App