from categoria.models import Categoria
from produto.models import Produto

cat1 = Categoria(nome = 'Balas', slug = 'balas')
cat2 = Categoria(nome = 'Chocolate', slug = 'chocolate')
cat3 = Categoria(nome = 'Especiais', slug = 'especiais')

cat1.save()
cat2.save()
cat3.save()

p = []
p.append(Produto(nome = 'Confeito M&M chocolate ao leite', slug ='Confeito-MeM-chocolate-ao-leite', categoria = cat2, imagem = 'MEM.png',secao = 'maisVendidos'))
p.append(Produto(nome = 'Barra de chocolate lacta laka', slug = 'Barra-de-chocolate-lacta-laka', categoria = cat2, imagem = 'LAKA.png',secao = 'maisVendidos'))
p.append(Produto(nome = 'Chocolate KitKat ao leite', slug = 'Chocolate-KitKat-ao-leite', categoria = cat2, imagem = 'KITKATAOLEITE.png',secao = 'maisVendidos'))
p.append(Produto(nome = 'Bala de gelatina fini amoras', slug = 'Bala-de-gelatina-fini-amoras', categoria = cat1, imagem = 'FINIAMORAS.png',secao = 'maisVendidos'))
p.append(Produto(nome = 'Bala de gelatina fini dentaduras', slug = 'Bala-de-gelatina-fini-dentaduras', categoria = cat1, imagem = 'FINIDENTADURAS.png',secao = 'maisVendidos'))
p.append(Produto(nome = 'Bala de gelatina fini tubes', slug = 'Bala-de-gelatina-fini-tubes', categoria = cat1, imagem = 'FINIDENTADURAS.png',secao = 'maisVendidos'))

p.append(Produto(nome = 'Chocolate toblerone ao leite', slug = 'Chocolate-toblerone-ao-leite', categoria = cat2, imagem = 'toblerone1.png', secao = 'lancamentos'))
p.append(Produto(nome = 'Chocolate toblerone meio amargo', slug = 'Chocolate-toblerone-meio-amargo', categoria = cat2, imagem = 'toblerone2.png', secao = 'lancamentos'))
p.append(Produto(nome = 'Chocolate toblerone branco', slug = 'Chocolate-toblerone-branco',categoria = cat2, imagem = 'toblerone3.png', secao = 'lancamentos'))

p.append(Produto(nome = 'Feijõezinhos de todos os sabores harry potter', slug = 'Feijoezinhos-de-todos-os-sabores-harry-potter', categoria = cat3, imagem = 'hpfeijoes.png', secao = 'hp'))
p.append(Produto(nome = 'Cerveja amanteigada harry potter', slug = 'Cerveja-amanteigada-harry-potter', categoria = cat3, imagem = 'hpcerveja.png', secao = 'hp'))
p.append(Produto(nome = 'Chocolate sapos ao leite harry potter', slug = 'Chocolate-sapos-ao-leite-harry-potter', categoria = cat3, imagem = 'hpsapo.png', secao = 'hp'))

for i in p:
    i.save()