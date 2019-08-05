<?
/*
 * Parameters:
 * 
 *   - bigtext: The text to replace the @handle
 *   - smalltext: The text to replace the words below
 *   - user: The user to parse
 *   - duration: The time in seconds to show
 *   - loop: Whether to loop the show or just stop 
 *
 *   Future:
 *     assetlist: Assets to show instead of "detecting" them
 */
function get($what) {
  global $contents;
  preg_match_all('/"' . $what . '...([^"]*)/', $contents, $matchList);
  return $matchList[1][0];
}
function check($x) {
  global $sizes;
  return $sizes[$x] > 1080 ? 'class=fill' : '';
}
$handle = trim($_GET['user']);
$contents = file_get_contents("https://instagram.com/$handle");
$name = $_GET['smalltext'] ?: json_decode('"' . get('full_name') . '"');
$bigtext = $_GET['bigtext'] ?: $handle;
$logo = get('profile_pic_url_hd');

preg_match_all('/.height.:(\d*),.width.:1080},.display_url...([^"]*)/', $contents, $matchList);
$sizes = $matchList[1];
$images = $matchList[2];
$iy = 0;
for($ix = count($images); $ix < 6; $ix ++) {
  $images[] = $images[$iy];
  $sizes[] = $sizes[$iy];
  $iy++;
}

$dur = $_GET['duration'] ?: 16;

if(!empty($_GET['loop'])) {
  echo "<meta http-equiv=refresh content=" . $dur - 1.75 . ">";
}

?>
<link href="https://fonts.googleapis.com/css?family=Roboto:300,400&display=swap" rel=stylesheet>
<style>
* {
  animation-duration: <?= $dur ?>s;
  animation-fill-mode: forwards;
}
body.dark { 
  color: #fff;
  background: #000 
}
h2,h3,body { 
  margin: 0 ;
  font-family: 'Roboto', sans-serif;
}
h2 { 
  font-size: 2.85vw;
  font-weight: 400;
  margin-top: 2vw;
}
h3 {
  font-size: 1.75vw;
  font-weight: 300;
  text-transform: lowercase;
}
#container {
  height: 35.1vw;
  position: relative;
  overflow: hidden;
}
#container > div {
  width: calc(100%/3);
  text-align: center;
}
.row {
  position: absolute;
  display: flex;
  justify-content: center;
  flex-flow: row wrap;
  opacity: 0;
}
.row img {
  object-fit: cover;
  max-height: calc(100vw/3 - 2vw);
}
img.fill {
  min-width: calc(100vw/3 - 2vw);
}
.row div {
  display: flex;
  justify-content: space-around;
  align-items: center;
  border-radius: 2vw;
  margin: 2vw 0;
  height: calc(100vw/3 - 2vw);
  width: calc(100vw/3 - 2vw);
  overflow: hidden
}
#brand {
  display: flex;
  align-items: center;
  justify-content: space-around;
  height: 35.1vw;
  transition-timing-function: ease;
  animation-name: logo;
}
#logo-container {
  display: inline-flex;
  justify-content: space-around;
  align-items: center;
  width: 16.5vw;
  height: 16.5vw;
}
#copy { 
  animation-name: brandslide;
}
#brand img {
  border-radius: 50vw;
  padding: 0.2vw;
  border: 1px solid #e4e4e4;
  width: 100%;
  animation-name: zoomout;
}
.row.down {
  bottom: 0;
  animation-name: slidedown;
}
.row.up {
  top: 0;
  animation-name: slideup;
}
@keyframes zoomout {
  90% { 
    opacity: 1;
    width: 100%; 
  }
  to { 
    opacity: 0;
    width: 0 
  }
}
@keyframes brandslide {
  90% { 
    opacity: 1;
    transform: translateY(0); 
  }
  to { 
    opacity: 0;
    transform: translateY(12vw); 
  }
}
@keyframes logo {
  from { margin-left: 33%; opacity: 0 }
  5% { opacity: 1 }
  10% { margin-left: 0 }
  77% { margin-left: 0 }
  90% { margin-left: 33%; }
  to { margin-left: 33%; }
}
@keyframes slideup {
  from {
    transform: translateY(35.1vw);
    opacity: 0;
  }
  10% { transform: translateY(0); opacity: 1; }
  23% { transform: translateY(0) }
  36% { transform: translateY(-35.3vw) }
  50% { transform: translateY(-35.3vw) }
  63% { transform: translateY(calc(-35.3vw * 2)) }
  77% { transform: translateY(calc(-35.3vw * 2)); opacity: 1 }
  90% { transform: translateY(calc(-35.3vw * 3)); opacity: 0; }
  to { transform: translateY(calc(-35.3vw * 3)); opacity: 0; }
}
@keyframes slidedown {
  from {
    transform: translateY(-35.1vw);
    opacity: 0;
  }
  10% { transform: translateY(0); opacity: 1; }
  23% { transform: translateY(0) }
  36% { transform: translateY(35.3vw) }
  50% { transform: translateY(35.3vw) }
  63% { transform: translateY(calc(35.3vw * 2)) }
  77% { transform: translateY(calc(35.3vw * 2)); opacity: 1 }
  90% { transform: translateY(calc(35.3vw * 3)); opacity: 0; }
  to { transform: translateY(calc(35.3vw * 3)); opacity: 0; }
}
</style>
</head>
<body class=dark>
<div id=container>
  <div id=brand>
    <div>
      <div id=logo-container>
        <img src=<?= $logo ?>>
      </div>
      <div id=copy>
        <h2>@<?= $bigtext ?></h2>
        <h3><?= $smalltext ?></h3>
      </div>
    </div>
  </div>
  <div class='row up' style='left:33.3%'>
    <? foreach([0,1,2] as $i){ ?>
    <div><img <?=check($i);?> src=<?= $images[$i] ?>></div>
    <? } ?>
  </div>
  <div class='row down' style='left:66.6%'>
    <? foreach([5,4,3] as $i){ ?>
    <div><img <?=check($i);?> src=<?= $images[$i] ?>></div>
    <? } ?>
  </div>
</div>
</body>
</html>
