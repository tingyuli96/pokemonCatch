// URL: https://beta.observablehq.com/@steven13737/d3-sortable-bar-chart
// Title: D3 Sortable Bar Chart
// Author: steven13737 (@steven13737)
// Version: 225
// Runtime version: 1

const m0 = {
  id: "adc43881cd41cfce@225",
  variables: [
    {
      inputs: ["md"],
      value: (function(md){return(
md`# D3 Sortable Bar Chart

Use the dropdown menu to change the sort order.`
)})
    },
    {
      name: "viewof order",
      inputs: ["html","Promises"],
      value: (function(html,Promises)
{
  const select = html`<select>
  <option selected value=name-ascending>Alphabetical
  <option value=value-descending>Frequency, descending
  <option value=value-ascending>Frequency, ascending
</select>`;
  Promises.delay(2000).then(() => {
    select.selectedIndex = 1;
    select.dispatchEvent(new CustomEvent("input"));
  });
  return select;
}
)
    },
    {
      name: "order",
      inputs: ["Generators","viewof order"],
      value: (G, _) => G.input(_)
    },
    {
      name: "chart",
      inputs: ["d3","DOM","width","height","data","x","y","xAxis","yAxis"],
      value: (function(d3,DOM,width,height,data,x,y,xAxis,yAxis)
{
  const svg = d3.select(DOM.svg(width, height));

  const bar = svg.append("g")
      .attr("fill", "steelblue")
    .selectAll("rect")
    .data(data)
    .enter().append("rect")
      .style("mix-blend-mode", "multiply")
      .attr("x", d => x(d.name))
      .attr("y", d => y(d.value))
      .attr("height", d => y(0) - y(d.value))
      .attr("width", x.bandwidth());

  const gx = svg.append("g")
      .call(xAxis);

  const gy = svg.append("g")
      .call(yAxis);

  svg.node().update = () => {
    const t = svg.transition()
        .duration(750);

    bar.data(data, d => d.name)
        .order()
      .transition(t)
        .delay((d, i) => i * 20)
        .attr("x", d => x(d.name));

    gx.transition(t)
        .call(xAxis)
      .selectAll(".tick")
        .delay((d, i) => i * 20);
  };

  return svg.node();
}
)
    },
    {
      inputs: ["order","data","x","chart"],
      value: (function(order,data,x,chart)
{
  switch (order) {
    case "name-ascending": data.sort((a, b) => a.name.localeCompare(b.name)); break;
    case "value-ascending": data.sort((a, b) => a.value - b.value); break;
    case "value-descending": data.sort((a, b) => b.value - a.value); break;
  }
  x.domain(data.map(d => d.name));
  chart.update();
  return order;
}
)
    },
    {
      name: "data",
      inputs: ["require"],
      value: (async function(require){return(
(await require("../static/pikachu_city"))
  .map(({x, y}) => ({name: x, value: y}))
)})
    },
    {
      name: "x",
      inputs: ["d3","data","margin","width"],
      value: (function(d3,data,margin,width){return(
d3.scaleBand()
    .domain(data.map(d => d.name))
    .range([margin.left, width - margin.right])
    .padding(0.1)
)})
    },
    {
      name: "y",
      inputs: ["d3","data","height","margin"],
      value: (function(d3,data,height,margin){return(
d3.scaleLinear()
    .domain([0, d3.max(data, d => d.value)]).nice()
    .range([height - margin.bottom, margin.top])
)})
    },
    {
      name: "xAxis",
      inputs: ["height","margin","d3","x"],
      value: (function(height,margin,d3,x){return(
g => g
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x)
        .tickSizeOuter(0))
)})
    },
    {
      name: "yAxis",
      inputs: ["margin","d3","y"],
      value: (function(margin,d3,y){return(
g => g
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y))
    .call(g => g.select(".domain").remove())
)})
    },
    {
      name: "height",
      value: (function(){return(
500
)})
    },
    {
      name: "margin",
      value: (function(){return(
{top: 20, right: 0, bottom: 30, left: 40}
)})
    },
    {
      name: "d3",
      inputs: ["require"],
      value: (function(require){return(
require("d3@5")
)})
    }
  ]
};

const notebook = {
  id: "adc43881cd41cfce@225",
  modules: [m0]
};
