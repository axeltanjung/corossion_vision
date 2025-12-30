import { useEffect, useState } from "react";
import FleetHeatmap from "../components/FleetHeatmap";
import AssetMap from "../components/AssetMap";
import ExportPDF from "../components/ExportPDF";

export default function Dashboard(){
  const [assets,setAssets]=useState([]);

  useEffect(()=>{
    fetch("http://localhost:8000/assets")
      .then(r=>r.json()).then(setAssets)
  },[]);

  return (
    <div id="report">
      <h1>Corrosion Command Center</h1>

      <FleetHeatmap data={assets}/>
      <AssetMap assets={assets}/>
      <ExportPDF targetId="report"/>
    </div>
  );
}
