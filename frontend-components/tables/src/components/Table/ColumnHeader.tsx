import { flexRender } from "@tanstack/react-table";
import clsx from "clsx";
import { FC } from "react";
import { useDrag, useDrop } from "react-dnd";

function Filter({
  column,
  table,
  numberOfColumns,
}: {
  column: any;
  table: any;
  numberOfColumns: number;
}) {
  const firstValue = table
    .getPreFilteredRowModel()
    .flatRows[0]?.getValue(column.id);

  const columnFilterValue = column.getFilterValue();

  const isProbablyDate =
    column.id.toLowerCase().includes("date") ||
    column.id.toLowerCase() === "index";

  if (isProbablyDate) {
    function getTime(value) {
      if (!value) return null;
      const date = new Date(value);
      const year = date.getFullYear();
      const month =
        date.getMonth() + 1 > 9
          ? date.getMonth() + 1
          : `0${date.getMonth() + 1}`;
      const day = date.getDate() > 9 ? date.getDate() : `0${date.getDate()}`;
      return `${year}-${month}-${day}`;
    }

    return (
      <div className="flex space-x-2">
        <input
          type="date"
          value={getTime((columnFilterValue as [string, string])?.[0]) ?? ""}
          onChange={(e) => {
            const value = new Date(e.target.value).getTime();
            column.setFilterValue((old: [string, string]) => [value, old?.[1]]);
          }}
          placeholder={`Start date`}
          className="_input"
        />
        <input
          type="date"
          value={getTime((columnFilterValue as [string, string])?.[1]) ?? ""}
          onChange={(e) => {
            const value = new Date(e.target.value).getTime();
            column.setFilterValue((old: [string, string]) => [old?.[0], value]);
          }}
          placeholder={`End date`}
          className="_input"
        />
      </div>
    );
  }

  return typeof firstValue === "number" ? (
    <div
      className={clsx("flex space-x-2", {
        "flex-col": numberOfColumns > 4,
        "flex-row": numberOfColumns <= 4,
      })}
    >
      <input
        type="number"
        value={(columnFilterValue as [number, number])?.[0] ?? ""}
        onChange={(e) =>
          column.setFilterValue((old: [number, number]) => [
            e.target.value,
            old?.[1],
          ])
        }
        placeholder={`Min`}
        className="_input"
      />
      <input
        type="number"
        value={(columnFilterValue as [number, number])?.[1] ?? ""}
        onChange={(e) =>
          column.setFilterValue((old: [number, number]) => [
            old?.[0],
            e.target.value,
          ])
        }
        placeholder={`Max`}
        className="_input"
      />
    </div>
  ) : (
    <input
      type="text"
      value={(columnFilterValue ?? "") as string}
      onChange={(e) => column.setFilterValue(e.target.value)}
      placeholder={`Search...`}
      className="_input"
    />
  );
}

const reorderColumn = (
  draggedColumnId: string,
  targetColumnId: string,
  columnOrder: string[]
) => {
  columnOrder.splice(
    columnOrder.indexOf(targetColumnId),
    0,
    columnOrder.splice(columnOrder.indexOf(draggedColumnId), 1)[0] as string
  );
  return [...columnOrder];
};

const DraggableColumnHeader: FC<{
  header: any;
  table: any;
  advanced: boolean;
}> = ({ header, table, advanced }) => {
  const { getState, setColumnOrder } = table;
  const { columnOrder } = getState();
  const { column } = header;

  const [, dropRef] = useDrop({
    accept: "column",
    drop: (draggedColumn: any) => {
      const newColumnOrder = reorderColumn(
        draggedColumn.id,
        column.id,
        columnOrder
      );
      setColumnOrder(newColumnOrder);
    },
  });

  const [{ isDragging }, dragRef, previewRef] = useDrag({
    collect: (monitor) => ({
      isDragging: monitor.isDragging(),
    }),
    item: () => column,
    type: "column",
  });

  return (
    <th
      className="h-[70px] relative"
      colSpan={header.colSpan}
      style={{ /* width: header.getSize(),*/ opacity: isDragging ? 0.5 : 1 }}
      ref={dropRef}
    >
      <div ref={previewRef} className="space-y-2">
        {header.isPlaceholder ? null : (
          <>
            <div
              {...{
                className: clsx(
                  "font-bold uppercase text-white tracking-widest tracking-normal flex gap-2 whitespace-nowrap justify-between",
                  {
                    "cursor-pointer select-none": header.column.getCanSort(),
                  }
                ),
                onClick: header.column.getToggleSortingHandler(),
              }}
            >
              <div className="flex gap-2">
                {flexRender(
                  header.column.columnDef.header,
                  header.getContext()
                )}
                {header.column.getCanSort() && (
                  <div className="flex flex-col gap-1 items-center justify-center">
                    <button
                      className={clsx({
                        "text-[#669DCB]": header.column.getIsSorted() === "asc",
                        "text-grey-600": header.column.getIsSorted() !== "asc",
                      })}
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="11"
                        height="5"
                        fill="none"
                        viewBox="0 0 11 5"
                      >
                        <path fill="currentColor" d="M10.333 5l-5-5-5 5"></path>
                      </svg>
                    </button>
                    <button
                      className={clsx({
                        "text-[#669DCB]":
                          header.column.getIsSorted() === "desc",
                        "text-grey-600": header.column.getIsSorted() !== "desc",
                      })}
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="11"
                        height="5"
                        fill="none"
                        viewBox="0 0 11 5"
                      >
                        <path fill="currentColor" d="M.333 0l5 5 5-5"></path>
                      </svg>
                    </button>
                  </div>
                )}
              </div>
              {advanced && column.id !== "select" && (
                <button ref={dragRef}>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="17"
                    height="16"
                    fill="none"
                    viewBox="0 0 17 16"
                  >
                    <path
                      stroke="#fff"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M3.667 6l-2 2 2 2M6.333 3.333l2-2 2 2M10.333 12.667l-2 2-2-2M13 6l2 2-2 2M1.667 8H15M8.333 1.333v13.334"
                    ></path>
                  </svg>
                </button>
              )}
            </div>
            {advanced && header.column.getCanFilter() ? (
              <div>
                <Filter
                  column={header.column}
                  table={table}
                  numberOfColumns={columnOrder.length}
                />
              </div>
            ) : null}
          </>
        )}
      </div>
      {/* <div
          className="absolute right-0 top-0 h-full w-1 bg-blue-300 select-none touch-none hover:bg-blue-500 cursor-col-resize"
          onMouseDown={header.getResizeHandler()}
          onTouchStart={header.getResizeHandler()}
              />*/}
    </th>
  );
};

export default DraggableColumnHeader;
