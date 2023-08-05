from Domain.review import Review


class ReviewValidator:
    def valideazaReview(self,review:Review):
        erori = []
        if review.numeClient == '':
            erori.append("numele trebe sa fie nenul")
        if erori:
            raise ValueError(erori)
