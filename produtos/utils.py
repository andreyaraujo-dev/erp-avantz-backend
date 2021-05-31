from .models import Produtos


def generate_product_code(id_matriz):
    last_product = Produtos.objects.filter(
        id_matriz=id_matriz).order_by('id').last()
    return last_product.codprod + 1
