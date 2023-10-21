MARS:=java -jar ./Mars4_5.jar
#MARS:=mars
# max number of instructions allowed 305900 (10 x 30590)
JTIMEOUT:=305900

## CSS to decorate HTML
CSS="<style> .my-pre{\
line-height:1.2em;\
background:linear-gradient(180deg,\#ccc 0,\#ccc 1.2em,\#eee 0);\
background-size:2.4em 2.4em;\
background-origin:content-box;\
padding:0 20px;\
text-align:justify;\
font-family:calibri,arial,sans-serif;} </style>"

TESTS=$(wildcard test-*.in)
PASSEDFN:=$(TESTS:.in=.pass)

all: $(PASSEDFN) test_results.html


test_results.html: clean program01.asm Makefile
	@echo $(CSS) > $@
	@echo "<H1>[AE] Test results</H1>" >> $@
	make $(PASSEDFN) | tee -a $@

program01.comp: program01.asm
	@echo "> Compile test</br>"
	@echo
	@rm -f program01.*comp ; \
	$(MARS) a ae1 me nc program01.asm > program01.comp 2> program01.noncomp ; \
	if [ -s program01.noncomp ] ; then  \
		rm -f program01.comp ; \
	else \
		rm -f program01.noncomp ; \
	fi

test-%.out: program01.comp  test-%.in
	@echo "> Running"
	@echo $@ for at most $(JTIMEOUT) instructions
	@F=$(basename $@ .out) ; \
	$(MARS) $(JTIMEOUT) se1 me nc sm ic program01.asm < $$F.in > $@ 2> $$F.err

test-%.pass: test-%.out test-%.expt
	@echo '<pre class="my-pre">'
	@echo Checking $^
	@F=$(basename $@ .pass) ; \
	rm -f $$F*pass ; \
	if (diff -yabBw $^ > $$F.diff ) ; then \
		echo "<span style=\"color:green\">PASSED</span>" ; \
		touch $$F.pass ; \
	else \
		echo "" >> $$F.diff ; \
		echo "<span style=\"color:red\">NOT PASSED</span><code>" ; \
		touch $$F.nopass ; \
		echo "=== Risultato ottenuto a sinistra ===    ==== Risultato atteso a destra =====" ; \
		cat $$F.diff ; \
		echo ============================================================================= ; \
		echo ============================================================================= ; \
		echo "</code>" ; \
	fi
	@echo '</pre>'

printerr:
	cat *err

clean:
	rm -f *.out *.diff *.pass *.nopass *.comp *.nocomp *.err test_results.html


.PRECIOUS: test-%.out *.out *.err *.diff
