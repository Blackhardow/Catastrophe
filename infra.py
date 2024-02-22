

class Infrastructure:
    def __init__(self, infra_id, infra_type, longueur, nb_maisons):
        self.infra_id = infra_id
        self.infra_type = infra_type
        self.nb_maison = sum(nb_maisons)
        self.longueur = longueur
        self.diff_infra = 0

    def reparer(self):
        self.infra_type = "infra_intacte"

    def difficulte_infra(self):
        if  self.infra_type == "infra_intacte":
            self.diff = 0
        else:
            self.diff = self.longueur / self.nb_maison

