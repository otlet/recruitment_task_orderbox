from pprint import pprint

from generator_order_box import GeneratorOrderBox


def display(asd: int) -> str:
    return asd if asd != 0 else ""


if __name__ == '__main__':
    generator = GeneratorOrderBox()
    print(f'Liczba\tMały\tŚredni\tDuży\tZbiorczy')
    for i in range(37):
        varka = generator.get_box_quantity(i)
        multiple = generator.get_box_multiply()
        print(
            f'{i}\t'
            f'{display(varka["small_box"])}\t'
            f'{display(varka["average_box"])}\t'
            f'{display(varka["large_box"])}\t'
            f'{display(multiple)}'
        )
