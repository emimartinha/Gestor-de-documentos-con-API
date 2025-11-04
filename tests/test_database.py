
import csv
import copy
import config
import helpers
import unittest
import database as db


class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('32.390.404', 'Marta', 'Perez'),
            db.Cliente('30.200.300', 'Manolo', 'Lopez'),
            db.Cliente('42.819.032', 'Emiliano', 'Martinha')
        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('32.390.404')
        cliente_inexistente = db.Clientes.buscar('99X')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('39.909.800', 'Héctor', 'Costa')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39.909.800')
        self.assertEqual(nuevo_cliente.nombre, 'Héctor')
        self.assertEqual(nuevo_cliente.apellido, 'Costa')

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('30.200.300'))
        cliente_modificado = db.Clientes.modificar('30.200.300', 'Mariana', 'Garcia')
        self.assertEqual(cliente_a_modificar.nombre, 'Manolo')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('42.819.032')
        cliente_rebuscado = db.Clientes.buscar('42.819.032')
        self.assertEqual(cliente_borrado.dni, '42.819.032')
        self.assertIsNone(cliente_rebuscado)

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('99.999.999', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('232323S', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar('42.819.032')
        db.Clientes.borrar('30.200.300')
        db.Clientes.modificar('32.390.404', 'Mariana', 'García')

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)

        self.assertEqual(dni, '32.390.404')
        self.assertEqual(nombre, 'Mariana')
        self.assertEqual(apellido, 'García')


