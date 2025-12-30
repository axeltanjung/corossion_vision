import jsPDF from "jspdf";
import html2canvas from "html2canvas";

export default function ExportPDF({ targetId }) {
  const exportPDF = async () => {
    const el = document.getElementById(targetId);
    const canvas = await html2canvas(el);
    const img = canvas.toDataURL("image/png");

    const pdf = new jsPDF("p","mm","a4");
    pdf.addImage(img,"PNG",10,10,180,250);
    pdf.save("integrity-report.pdf");
  };

  return <button onClick={exportPDF}>Export PDF Report</button>;
}
