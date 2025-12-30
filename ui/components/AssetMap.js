import { MapContainer, TileLayer, CircleMarker, Popup } from "react-leaflet";

export default function AssetMap({ assets }) {
  return (
    <MapContainer center={[-6.2,106.8]} zoom={10} style={{height:400}}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>
      {assets.map(a=>(
        <CircleMarker
          key={a.asset_id}
          center={[a.lat,a.lon]}
          radius={10}
          color={a.corrosion_index>0.7?"red":"green"}>
          <Popup>
            <b>{a.asset_id}</b><br/>
            CI: {a.corrosion_index}<br/>
            RUL: {a.rul_days} days
          </Popup>
        </CircleMarker>
      ))}
    </MapContainer>
  );
}
