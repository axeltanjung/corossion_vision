import { GoogleMap, useJsApiLoader, Marker } from '@react-google-maps/api';

const containerStyle = { width: '100%', height: '400px' };

export default function GoogleAssetMap({ assets }) {
  const { isLoaded } = useJsApiLoader({
    googleMapsApiKey: process.env.NEXT_PUBLIC_GOOGLE_MAPS_KEY,
  });

  if (!isLoaded) return <div>Loading map…</div>;

  return (
    <GoogleMap
      mapContainerStyle={containerStyle}
      center={{ lat: -6.2, lng: 106.8 }}
      zoom={11}
      mapTypeId="satellite"
    >
      {assets.map(a => (
        <Marker
          key={a.asset_id}
          position={{ lat: a.lat, lng: a.lon }}
          label={`${a.asset_id}`}
        />
      ))}
    </GoogleMap>
  );
}
