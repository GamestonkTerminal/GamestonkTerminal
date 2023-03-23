//@ts-nocheck
import { useEffect, useState } from "react";
import Table from "./components/Table";
import { DndProvider } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";
import {
  cryptoData,
  incomeData,
  longIncomeData,
  performanceData,
} from "./data/mockup";

declare global {
  interface Window {
    json_data: any;
    title: string;
  }
}

function App() {
  const [data, setData] = useState(
    process.env.NODE_ENV === "production" ? null : JSON.parse(longIncomeData)
  );
  const [title, setTitle] = useState("Interactive Table");

  if (process.env.NODE_ENV === "production") {
    useEffect(() => {
      const interval = setInterval(() => {
        if (window.json_data) {
          const data = JSON.parse(window.json_data);
          console.log(data);
          setData(data);
          if (data.title) {
            setTitle(data.title);
          }
          clearInterval(interval);
        }
      }, 100);
      return () => clearInterval(interval);
    }, []);
  }

  const transformData = (data: any) => {
    if (!data) return null;

    let filename = data.title?.replace(/<b>|<\/b>/g, "").replace(/ /g, "_");
    let date = new Date().toISOString().slice(0, 10).replace(/-/g, "");
    let time = new Date().toISOString().slice(11, 19).replace(/:/g, "");
    window.title = `openbb_${filename}_${date}_${time}`;

    const columns = data.columns;
    const index = data.index;
    const newData = data.data;
    const transformedData = newData.map((row: any, index: number) => {
      const transformedRow = {};
      row.forEach((value: any, index: number) => {
        //@ts-ignore
        transformedRow[columns[index]] = value;
      });
      return transformedRow;
    });
    return {
      columns,
      data: transformedData,
    };
  };

  const transformedData = transformData(data);

  return (
    <div className="relative h-full bg-black">
      <DndProvider backend={HTML5Backend}>
        {transformedData && (
          <Table
            title={title}
            data={transformedData.data}
            columns={transformedData.columns}
          />
        )}
      </DndProvider>
    </div>
  );
}

export default App;
