class HtmlOutputer(object):
    
    def __init__(self):
        self._datas = [];
        
    
    def collect_data(self, new_data):
        if new_data is None:
            return 
        self._datas.append(new_data)
        
    
    def output_html(self):
        datas = self._datas

        tds = '''
            <html>
            <body>
            <table>
        '''
        for data in datas:
            tds += '''
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>    
            ''' % (data['url'], data['title'], data['summary'])

        tds = '''
            </table>
            </body>
            </html>
        '''
            
        fout = open('output.html', 'w')
        fout.write(tds.encode('utf-8'))
        fout.close()
    
    
    



