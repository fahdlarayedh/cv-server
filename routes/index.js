var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function (req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/script', async (req, res) => {
  try {
    console.log('script:');
    //const python = spawn('python',['--version']); 
    const spawn = require("child_process").spawn;
    //const python = spawn('python', [`${process.cwd()}\\routes\\script.py`]); // windows
    const python = spawn('python', [`${process.cwd()}/routes/script.py`]); //mac ou bien linux

    python.stdin.write(JSON.stringify(req.body));
    python.stdin.end();

    var buffers = [];

    python.stdout.on('data', (data) => {
      buffers.push(data);
      //console.log(`stdout: ${data}`);
      //pyRespData = data.toString();
      //pyJsonRespData = JSON.parse(pyRespData);
      //console.log('Tf2v:'+pyJsonRespData.Tf2v);
      //console.log('Detection:'+pyJsonRespData.Detection);
      //console.log('RednessPerc:'+pyJsonRespData.RednessPerc);
      //console.log('Image1:'+pyJsonRespData.Image1);
      //console.log('Image2:'+pyJsonRespData.Image2);
      //res.status(200).json({ message: "All Done", Detection: pyJsonRespData.Detection, RednessPerc: pyJsonRespData.RednessPerc, Image1: pyJsonRespData.Image1 });
    }).on('end', function () {
      pyJsonRespData = JSON.parse(Buffer.concat(buffers).toString());
      //pyRespData = data.toString();
      //pyJsonRespData = JSON.parse(buffers.toString());
      //console.log(buffers.toString());
      //res.status(200).json({ message: "All Done", Detection: pyJsonRespData.Detection, RednessPerc: pyJsonRespData.RednessPerc, Image1: pyJsonRespData.Image1 });
      res.status(200).json({ message: "All Done", test: pyJsonRespData.test, detection: pyJsonRespData.detection, evaxData: pyJsonRespData.evaxData , qrCodeData: pyJsonRespData.qrCodeData });

    });

    python.stderr.on('data', (data) => {
      console.log(`stderr: ${data}`);
    });

    /*python.on('close', (code) => {
      console.log(`child process exited with code: ${code}`);
    });*/

  } catch (e) {
    console.log(e);
    return res.status(404).json({ msg: e });
  }
});

module.exports = router;
