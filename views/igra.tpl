<!DOCTYPE html>
<html>

<body>
<h1>{{igra.pravilni_del_gesla()}}</h1>

Nepravilne črke: {{igra.nepravilni_del_gesla()}} <br>
Stopnja obešenosti: {{igra.stevilo_napak()}}

% if igra.zmaga():
<h1>Čestitke, uganil/a si geslo: {{igra.geslo}}</h1>
% elif igra.poraz():
<h1>Geslo je bilo {{igra.geslo}}. Več sreče drugič.</h1>
% else:
<form method="post" action="">
Ugibaj: <input name="crka" /> <input type="submit" value="Ugibaj">
</form>
% end

</body>

</html>