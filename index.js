const express = require("express");
const app = express();
const path = require('path');
const port = 3001;

app.use(express.static(__dirname));

app.get("/", async (req, res) => {
  res.sendFile(path.join(__dirname+'/index.html'));
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
