import rblk.scanner.txt as txtscaner
import rblk.tag.txt as tgtg
import elist.elist as elel

class Parser():
    def __init__(self,txt,tag_pairs):
        self.txt = txt
        if(isinstance(tag_pairs,dict)):
            pass
        else:
            tag_pairs = tgtg.str2pairs(tag_pairs)
        self.descmat = txtscaner.get_descmat(txti,tag_pairs=tag_pairs)
        self.depth = len(descmat)
        self.breadths = elel.mapv(self.descmat,lambda layer:len(layer))
        self.text_mat = elel.matrix_map(self.descmat,lambda v,r,c:txt[v['si']:v['ei']])
    def srch4loc(self,tag):
        rslt = []
        for i in range(self.depth):
            for j in range(self.breadths[i]):
                ele_tag = self.descmat[i][j]['tag']
                if(tag == ele_tag):
                    loc = [i][j]
                    rslt.append(loc)
        return(rslt)
    def srch4txt(self,tag):
        rslt = []
        for i in range(self.depth):
            for j in range(self.breadths[i]):
                ele_tag = self.descmat[i][j]['tag']
                if(tag == ele_tag):
                    txt = self.text_mat[i][j]
                    rslt.append(txt)
        return(rslt)
    def lvsrch4txt_fromto(self,tag,from_lv,to_lv):
        from_lv = elel.uniform_index(from_lv,self.depth)
        to_lv = elel.uniform_index(to_lv,self.depth)
        rslt = []
        for i in range(from_lv,self.depth):
            for j in range(self.breadths[i]):
                ele_tag = self.descmat[i][j]['tag']
                if(tag == ele_tag):
                    txt = self.text_mat[i][j]
        return(rslt)
    def lvsrch4txt_from(self,tag,from_lv):
        to_lv = self.depth
        rslt = self.lvsrch4txt_fromto(tag,from_lv,to_lv)
        return(rslt)
    def lvsrch4txt_to(self,tag,to_lv):
        from_lv = 0
        rslt = self.lvsrch4txt_fromto(tag,from_lv,to_lv)
        return(rslt)






    
    
        

