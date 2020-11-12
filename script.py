from categoria.models import Categoria
from produto.models import Produto
from loja.models import Loja

cat1 = Categoria(nome = 'Balas', slug = 'balas')
cat2 = Categoria(nome = 'Chocolate', slug = 'chocolate')
cat3 = Categoria(nome = 'Especiais', slug = 'especiais')
cat4 = Categoria(nome = 'Bebidas', slug = 'bebidas')

cat1.save()
cat2.save()
cat3.save()
cat4.save()

Loja(nome="Candy Store", logo="candyStoreLogo4.png").save()


p = []
p.append(Produto(nome = 'Confeito M&M chocolate ao leite', imagem = 'MEM.png',secao = 'maisVendidos', loja = l))
p.append(Produto(nome = 'Barra de chocolate lacta laka', imagem = 'LAKA.png',secao = 'maisVendidos', loja = l))
p.append(Produto(nome = 'Chocolate KitKat ao leite', imagem = 'KITKATAOLEITE.png',secao = 'maisVendidos', loja = l))
p.append(Produto(nome = 'Bala de gelatina fini amoras', imagem = 'FINIAMORAS.png',secao = 'maisVendidos', loja = l))
p.append(Produto(nome = 'Bala de gelatina fini dentaduras', imagem = 'FINIDENTADURAS.png',secao = 'maisVendidos', loja = l))
p.append(Produto(nome = 'Bala de gelatina fini tubes', imagem = 'FINITUBES.png',secao = 'maisVendidos', loja = l))

p.append(Produto(nome = 'Chocolate toblerone ao leite', imagem = 'toblerone1.png', secao = 'lancamentos', loja = l))
p.append(Produto(nome = 'Chocolate toblerone meio amargo', imagem = 'toblerone2.png', secao = 'lancamentos', loja = l))
p.append(Produto(nome = 'Chocolate toblerone branco', imagem = 'toblerone3.png', secao = 'lancamentos', loja = l))

p.append(Produto(nome = 'Feijõezinhos de todos os sabores harry potter', imagem = 'hpfeijoes.png', secao = 'hp', loja = l))
p.append(Produto(nome = 'Cerveja amanteigada harry potter', imagem = 'hpcerveja.png', secao = 'hp', loja = l))
p.append(Produto(nome = 'Chocolate sapos ao leite harry potter', imagem = 'hpsapo.png', secao = 'hp', loja = l))

for i in p:
    i.save()