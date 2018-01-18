tab = 3
for i in range(21):
    print("<div id=\"inner_tab" + str(tab) + "_" + str(i) + "\" style=\"display: none\">\n\
    <div class=\"large-24 columns section_header\">\n\
        <h2><span id=\"tab_" + str(tab) + "_" + str(i)  + "\" runat=\"server\"></span></h2>\n\
    </div>\n\
    <div class=\"row\">\n\
        <div class=\"large-24 medium-24 small-24 columns\">\n\
            <span id=\"documents_" + str(tab) + "_" + str(i)  + "\" runat=\"server\" />\n\
        </div>\n\
    </div>\n\
    <div class=\"row\">\n\
        <div class=\"large-24 medium-24 small-24 columns\">\n\
            <span id=\"span_tab_" + str(tab) + "_" + str(i)  + "_section\" runat=\"server\" />\n\
        </div>\n\
    </div>\n\
</div>")