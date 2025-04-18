// Create graph and canvas
const graph = new LGraph();
const canvas = new LGraphCanvas("#graph-container", graph);

// Add some basic controls
document.getElementById("run").addEventListener("click", () => {
    console.log("Running graph...");
    graph.start();
});

document.getElementById("add-node").addEventListener("click", () => {
    const nodeTypes = ["basic/const", "basic/console", "basic/watch"];
    const type = nodeTypes[Math.floor(Math.random() * nodeTypes.length)];
    const node = LiteGraph.createNode(type);
    
    // Position randomly in view
    const rect = canvas.canvas.getBoundingClientRect();
    node.pos = [
        100 + Math.random() * (rect.width - 200),
        100 + Math.random() * (rect.height - 200)
    ];
    
    // Set some default values for certain nodes
    if (type === "basic/const") {
        node.setValue(Math.floor(Math.random() * 100));
    }
    
    graph.add(node);
});

document.getElementById("clear").addEventListener("click", () => {
    if (confirm("Clear all nodes?")) {
        graph.clear();
    }
});

// Add initial nodes for demonstration
function setupInitialNodes() {
    // Create a constant number node
    const numberNode = LiteGraph.createNode("basic/const");
    numberNode.pos = [100, 200];
    numberNode.setValue(42);
    graph.add(numberNode);
    
    // Create a watch node to display values
    const watchNode = LiteGraph.createNode("basic/watch");
    watchNode.pos = [400, 200];
    graph.add(watchNode);
    
    // Create a console output node
    const consoleNode = LiteGraph.createNode("basic/console");
    consoleNode.pos = [400, 300];
    graph.add(consoleNode);
    
    // Connect them
    numberNode.connect(0, watchNode, 0);
    numberNode.connect(0, consoleNode, 0);
}

// Initialize the graph
setupInitialNodes();
graph.start();  // This makes the graph run automatically on load