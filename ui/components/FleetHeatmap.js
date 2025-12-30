import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip } from "recharts";

export default function FleetHeatmap({ data }) {
  return (
    <ResponsiveContainer width="100%" height={250}>
      <BarChart data={data}>
        <XAxis dataKey="asset_id"/>
        <YAxis/>
        <Tooltip/>
        <Bar dataKey="corrosion_index" />
      </BarChart>
    </ResponsiveContainer>
  );
}
