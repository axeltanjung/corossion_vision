import {useState} from 'react'

export default function Home(){
  const [res,setRes]=useState(null)

  async function send(e){
    e.preventDefault()
    const f=new FormData(e.target)
    const r=await fetch("http://localhost:8000/predict?asset_id=A1",{method:"POST",body:f})
    setRes(await r.json())
  }

  return (
    <form onSubmit={send}>
      <input type="file" name="image"/>
      <button>Analyze</button>
      {res && <pre>{JSON.stringify(res,null,2)}</pre>}
    </form>
  )
}
