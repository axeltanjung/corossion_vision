import { useState } from 'react';

export default function MobileInspect(){
  const [img,setImg]=useState(null);
  const [res,setRes]=useState(null);

  const submit = async () => {
    const f = new FormData();
    f.append("image",img);
    const r = await fetch("http://localhost:8000/predict?asset_id=MOBILE-1",{method:"POST",body:f});
    setRes(await r.json());
  };

  return (
    <div>
      <h2>Field Inspection</h2>
      <input type="file" capture="environment" onChange={e=>setImg(e.target.files[0])}/>
      <button onClick={submit}>Analyze</button>
      {res && <pre>{JSON.stringify(res,null,2)}</pre>}
    </div>
  );
}
