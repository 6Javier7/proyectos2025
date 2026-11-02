#Mapas Resguardos2

#Elige EPSG:8857 si tu mapa se centra en Europa, África o el Atlántico.
#Elige EPSG:8858 si tu mapa se centra en América del Norte, Central o del Sur.
#Elige EPSG:8859 si tu mapa se centra en Asia, el Pacífico u Oceanía

#https://html-color.codes/olive


region = 'Latin America & Caribbean'
subregion = 'South America'
codigos_dep = ['27']
codigomdep = ['27']
codigos_muni = ['27250']
cpais = ['COL']
codigoc = ['153']
codigores = ['10345'] #Usar el caracter ID
codigoa = ['37'] #AZICATCH #por campo OBJECTID
ccomunidad1 = ['459'] #Santa Maria OBJECTID



# Lista de nombres de capas a procesar
nombres_capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'municipios_seleccionados', 'Ecosis 2024', 'Ecosis 2018', 'Cobertura 2020', 'Cobertura 2018', 'PAmoya', 'Pag', 'Pajorg', 'Pamoj', 'paramos', 'Pazap', 'RFAmazona1', 'RFAmazona2', 'RFCentral', 'RFMagda', 'RFMol', 'RFPacifico', 'RFSierra', 'ambitos', 'forestal', 'paz', 'zonip', 'autoridades', 'humedales', 'seco', 'ramsar', 'pomcas', 'manglares', 'parques', 'Áreas Prioritarias de Conservación CONPES 3680', 'zoniparques', 'Pacgsm', 'Cienagas', 'rios1', 'lagunas', 'pantanos', 'biosfera', 'hipso', 'vias', 'vias2', 'hidro', 'manzana', 'linea', 'nomenclatura', 'otrli', 'cultu', 'uacs', 'recuperacion_cortada', 'rehabilitacion_cortada', 'restauracion_cortada', 'marinos', 'coral', 'rocosoo', 'Sitios Prioritarios Conservación Caribe', 'Sitios Prioritarios Conservación Pacifico', 'campesinas', 'cienaga', 'cinturon', 'tuparro', 'sierra', 'seaflower', 'nsm']
oceano_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Mundo/ne_10m_ocean/ne_10m_ocean.shp'
region_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
pais_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
departamentos_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Colombia Dane/ADMINISTRATIVO/MGN_DPTO_POLITICO.shp'
municipios_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Municipios/Municipios2/MGN_MPIO_POLITICO.shp'
consejos_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Consejo_Comunitario_Titulado/Consejo_Comunitario_Titulado.gpkg'
resguardos_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Resguardos/Resguardo_Indigena_Formalizado/Resguardo_Indigena_Formalizado.shp'
campesinas_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/ZPRNRMA_1125_2021/ZPRNRMA_1125_2021.shp'
coberturas_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Coberturas Vegetales/Corregidas Coberturas.gpkg'
ecosistemas_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Ecositemas/corregidos.gpkg'
coberturas_path1 = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Coberturas Vegetales/Corregidas Coberturas1.gpkg'
ecosistemas_path1 = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Ecositemas/corregidos1.gpkg'

vias_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Colombia Dane/VIAS/VIAS.shp'
vias2_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/INVIAS/Invias_Vias.gpkg'
linea_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Colombia Dane/URBANO/MGN_URB_LINEA.shp'
manzana_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Colombia Dane/URBANO/MGN_URB_MANZANA.shp'
nomenclatura_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Colombia Dane/URBANO/MGN_URB_NOMENCLATURA_VIAL.shp'
cultu_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Colombia Dane/RURAL/CBD_RUR_CULTU_PUNTO.shp'
hidro_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Colombia Dane/RURAL/CBD_RUR_HIDRO_LINEA.shp'
hipso_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Colombia Dane/RURAL/CBD_RUR_HIPSO_PUNTO.shp'
otrli_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Colombia Dane/RURAL/CBD_RUR_OTRLI_LINEA.shp'
ambitos_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Ambitos_Territoriales_PDET/Ambitos_Territoriales_PDET.shp'
zonip_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Zonificacion_PDET_agosto_2021/Zonificacion_PDET_agosto_2021.shp'
autoridades_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Autoridades Ambientales/Lim_AA_25k_2019.shp'
marinos_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Ecosistemas Marinos/Mapa_de_Ecosistemas_MEC_100K/Mapa_de_Ecosistemas_MEC_100K.shp'
coral_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Ecosistemas Marinos/FormacionesCoralinas_Oceanico/FormacionesCoralinas_Oceanico.shp'
rocoso_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Ecosistemas Marinos/Litoral_Rocoso/litoralrocoso_litoralrocoso.shp'
prioc_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Ecosistemas Marinos/Sitios_Prioritarios_Conservación_Caribe/Sitios_Prioritarios_Conservación_Caribe.shp'
priop_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Ecosistemas Marinos/Sitios_Prioritarios_Conservación_Pacífico/Sitios_Prioritarios_Conservación_Pacífico.shp'
forestal_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Gobernanza_Forestal/Gobernanza_Forestal.shp'
humedales_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Humedal_version3/Humedal_version3.gpkg'
paramos_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Paramos_Delimitados_Junio_2020/Paramos_Delimitados_Junio_2020.shp'
seco_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/BosqueSecoTropical_100K/geo_export_1c851a13-97b1-4163-9ea1-d300bad45e9e.shp'
parques_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Parque Nacionales/runap_-_Registro_Unico_Nacional_AP/runap_-_Registro_Unico_Nacional_AP.shp'
priocon_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Prioridad_Conpes/PCN_CONPES.gpkg'
recu_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Recuperacion/Corregidos Recuperacion3a.gpkg'
reha_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Rehabilitacion/Corregidos Rehabilitacion3a.gpkg'
res_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Restauracion/Corregidos Restauracion3a.gpkg'

cienaga_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/AreasdeImportanciaEspecial_shp/Cienaga_grande_SM.shp'
cinturon_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/AreasdeImportanciaEspecial_shp/Cinturon_Andino.shp'
tuparro_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/AreasdeImportanciaEspecial_shp/El_Tuparro.shp'
ramsar_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/AreasdeImportanciaEspecial_shp/HumedalesRAMSAR.shp'
pomcas_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/AreasdeImportanciaEspecial_shp/POMCAS_MADS.shp'
zpomcas_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/POMCAS Zonificacion/zonificacion_POMCA_Octubre_2021/zonificacion_POMCA_Octubre_2021.shp'
ley2_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/AreasdeImportanciaEspecial_shp/ReservasForestalesLEY2.gpkg'
sierra_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/AreasdeImportanciaEspecial_shp/SCSierraNevadaSantaM.shp'
seaflower_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/AreasdeImportanciaEspecial_shp/Seaflower.shp'
nsm_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/AreasdeImportanciaEspecial_shp/SierraNSM.shp'

manglares_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/MANGLARES_COLOMBIA/MANGLARES_COLOMBIA.gpkg'
zoniparques_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Archivo_Zonificacion_PNNC_PM_Oficial_13122023/Corregidos Zonificacion1.gpkg'
biosfera_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/RESERVA_BIOSFERA_20240808/RESERVA_BIOSFERA_20240808.shp'
paz_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Bosques_Paz_septiembre_2022/Bosques_Paz_septiembre_2022.shp'
usos_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/usus_rurales/ZonificacionUsosRurales.shp'

rforestalp_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Reservas Forestales/res_1926_2013/res_1926_2013_info_cartografica/Zonificacion_PACIFICO_2014_2.shp'
rforestals_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Reservas Forestales/res_1276_2014/res_1276_2014_info_cartografica/Zonificacion_SNSM_2014.shp'
rforestalm1_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Reservas Forestales/res_1925_2013/res_1925_2013_info_cartografica/Zonificacion_AMAZONIA_2014_2.shp'
rforestalm2_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Reservas Forestales/Amazonia2 Resolucion-1277-de-2014/res_1277_2014_info_cartografica/Zonificacion_AMAZONIA_2014_2RESOLUCION1.gpkg'
rforestalc_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Reservas Forestales/res_1922_2013/res_1922_2013_info_cartografica/Zonificacion_CENTRAL_2014_2.shp'
rforestalmo_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Reservas Forestales/res_1923_2013/res_1923_2013_info_cartografica/Zonificacion_MOTILONES_2014_2.shp'
rforestalmag_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Reservas Forestales/Reserva Forestal Magdalena/res_1924_2013_info_cartografica/Zonificacion_MAGDALENA_2014_2.shp'
rforestalmag_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Reservas Forestales/Reserva Forestal Magdalena/res_1924_2013_info_cartografica/Zonificacion_MAGDALENA_2014_2.shp'

pomcamoya_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/POMCAS/Amoya/ZonificacionAmbiental1.shp'
pomcazap_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/POMCAS/Cienaga Zapatosa/ZonificacionAmbiental.shp'
pomcamoj_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/POMCAS/Mojana/Zonif_dissolve1.shp'
pomcag_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/POMCAS/Rio Tapias Guajira/ZonificacionAmbiental.shp'
pomcajorg_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/POMCAS/POMCA San Jorge/ZonificacionAmbiental1.gpkg'
pomcacgsm_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/POMCAS/Cienaga Grande/ZonificacionAmbiental_POMCAS1.gpkg'

cienaga2_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Hidrologia/Cienagas/Cienagas2.gpkg'
cuencas_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Hidrologia/Zonificación_Hidrográfica_Colombia_20260205.kml'
rios1_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Hidrologia/Rios/Principales Rios1.gpkg'
pantanos_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Hidrologia/Pantanos.gpkg'
lagunas_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Hidrologia/Lagunas/Lagunas.gpkg'


uacl_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Unidades Costeras/UACLLAS_-7168726867593121250/UACLLAS.shp'
uacs_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Unidades Costeras/Unidades Costeras/Limites UACs1.gpkg'

cabildos_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Resguardos/Estilo Asociaciones Indigenas/Comunidades Indigenas.gpkg'
asociaciones_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Resguardos/Estilo Asociaciones Indigenas/asociaciones Amazonia1.gpkg'

#veredas_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Veredas/CRVeredas_2020.shp'

# Lista de nombres de capas a procesar pc Andrey
#nombres_capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'municipios_seleccionados', 'Consejos2', 'veredas_en_consejos']
# Lista de nombres de capas a procesar
nombres_capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'municipios_seleccionados', 'Consejos2', 'Ecosis 2024', 'Ecosis 2018', 'Cobertura 2020', 'Cobertura 2018', 'hipso', 'hidro', 'otrli', 'vias2', 'parques', 'seco', 'humedales', 'paramos', 'forestal', 'zonip', 'ambitos', 'procon', 'autoridades', 'coral', 'priop', 'Sitios Prioritarios Conservación Pacifico', 'coral', 'marinos', 'rocoso']

#oceano_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Mundo/ne_10m_ocean/ne_10m_ocean.shp'
#region_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
#pais_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
#departamentos_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Colombia Dane/ADMINISTRATIVO/MGN_DPTO_POLITICO.shp'
#municipios_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Municipios/Municipios2/MGN_MPIO_POLITICO.shp'
#consejos_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Consejo_Comunitario_Titulado/Consejo_Comunitario_Titulado.shp'
#veredas_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Veredas/CRVeredas_2020.shp'

import time
from qgis import processing
from qgis.PyQt.QtCore import QVariant, QSizeF
from collections import defaultdict
from qgis.core import QgsProject, QgsVectorLayer, QgsRendererCategory, QgsCategorizedSymbolRenderer, QgsSymbol, QgsFeatureRequest, QgsFillSymbol, QgsSingleSymbolRenderer, QgsCoordinateReferenceSystem, QgsLegendPatchShape, QgsGeometry, QgsProject, QgsLayerTreeLayer, QgsSymbolLegendNode


#Eliminar Vacias
#######################

from qgis.core import QgsProject

def eliminar_capas_vacias():
    """
    Elimina del proyecto todas las capas vectoriales que tienen 0 features
    """
    
    proyecto = QgsProject.instance()
    capas_eliminadas = 0
    
    print("🔍 Buscando capas vacías...")
    
    for capa in proyecto.mapLayers().values():
        # Solo capas vectoriales
        if capa.type() == QgsMapLayer.VectorLayer:
            try:
                feature_count = capa.featureCount()
                
                if feature_count == 0:
                    nombre = capa.name()
                    proyecto.removeMapLayer(capa.id())
                    capas_eliminadas += 1
                    print(f"   🗑️ Eliminada: '{nombre}' (0 features)")
                    
            except Exception as e:
                print(f"   ⚠️ Error con capa '{capa.name()}': {e}")
    
    print(f"\n✅ {capas_eliminadas} capas vacías eliminadas")



#Areas
########################

def areas_por_etiqueta(nombre_capa, nombre_campo):
    """
    Calcula áreas por clase mostrando SOLO las etiquetas (sin códigos)
    
    Parámetros:
    - nombre_capa: str, nombre de la capa en QGIS
    - nombre_campo: str, nombre del campo que contiene las etiquetas
    """
    
    print("="*60)
    print("📊 CALCULANDO ÁREAS POR CLASE")
    print("="*60)
    
    # 1. Obtener capa
    capas = QgsProject.instance().mapLayersByName(nombre_capa)
    if not capas:
        print(f"❌ Capa '{nombre_capa}' no encontrada")
        return
    
    capa = capas[0]
    print(f"📋 Capa: {capa.name()}")
    print(f"🎯 Campo: '{nombre_campo}'")
    
    # 2. Verificar CRS y reproyectar si es necesario
    if capa.crs().isGeographic():
        print(f"🔄 CRS geográfico detectado. Reproyectando para cálculo preciso...")
        crs_utm = QgsCoordinateReferenceSystem("EPSG:9377")  # Ajusta según tu zona
        
        capa_trabajo = processing.run("native:reprojectlayer", {
            'INPUT': capa,
            'TARGET_CRS': crs_utm,
            'OUTPUT': 'memory:'
        })['OUTPUT']
        print(f"✅ Reproyección completada")
    else:
        capa_trabajo = capa
        print(f"✅ CRS proyectado detectado")
    
    # 3. Calcular áreas
    print(f"\n🔍 Procesando {capa.featureCount()} features...")
    
    areas = defaultdict(float)
    total_features = 0
    
    for feature in capa_trabajo.getFeatures():
        total_features += 1
        try:
            etiqueta = feature[nombre_campo]
            geom = feature.geometry()
            if geom and not geom.isEmpty():
                areas[etiqueta] += geom.area()
        except Exception as e:
            print(f"   ⚠️ Error en feature {feature.id()}: {e}")
    
    # 4. Mostrar resultados en el formato que te gusta
    print(f"\n📈 ÁREAS POR CLASE (en ha):")
    print("-" * 50)
    
    area_total = 0
    for etiqueta in sorted(areas.keys()):
        area_ha = areas[etiqueta] / 10000  # Convertir de m² a ha
        area_total += area_ha
        print(f"   {etiqueta}: {area_ha:,.2f} ha")
    
    print("-" * 50)
    print(f"\n📌 Resumen:")
    print(f"   • Total features: {total_features}")
    print(f"   • Clases distintas: {len(areas)}")
    print(f"   • ÁREA TOTAL: {area_total:,.2f} ha")
    
    return dict(areas)


#Areas totales
########################

def area_total_capa(nombre_capa, convertir_a_hectareas=True):
    """
    Calcula el área total de una capa vectorial
    
    Parámetros:
    - nombre_capa: str, nombre de la capa en QGIS
    - convertir_a_hectareas: bool, si True convierte de m² a hectáreas
    
    Retorna:
    - float: área total
    """
    
    print("="*60)
    print("📏 CALCULANDO ÁREA TOTAL DE LA CAPA")
    print("="*60)
    
    # 1. Obtener capa
    capas = QgsProject.instance().mapLayersByName(nombre_capa)
    if not capas:
        print(f"❌ Capa '{nombre_capa}' no encontrada")
        return None
    
    capa = capas[0]
    print(f"📋 Capa: {capa.name()}")
    print(f"   CRS original: {capa.crs().authid()}")
    print(f"   Features: {capa.featureCount():,}")
    
    # 2. Verificar CRS y reproyectar si es necesario
    if capa.crs().isGeographic():
        print(f"🔄 CRS geográfico detectado. Reproyectando para cálculo preciso...")
        crs_utm = QgsCoordinateReferenceSystem("EPSG:6686")  # Ajusta según tu zona
        
        capa_trabajo = processing.run("native:reprojectlayer", {
            'INPUT': capa,
            'TARGET_CRS': crs_utm,
            'OUTPUT': 'memory:'
        })['OUTPUT']
        print(f"✅ Reproyección completada")
    else:
        capa_trabajo = capa
        print(f"✅ CRS proyectado detectado")
    
    # 3. Calcular área total
    print(f"\n🔍 Calculando área...")
    
    area_total_m2 = 0
    features_procesadas = 0
    errores = 0
    
    for feature in capa_trabajo.getFeatures():
        features_procesadas += 1
        geom = feature.geometry()
        if geom and not geom.isEmpty():
            area_total_m2 += geom.area()
        else:
            errores += 1
    
    # 4. Convertir unidades
    if convertir_a_hectareas:
        area_total = area_total_m2 / 10000
        unidad = "hectáreas"
    else:
        area_total = area_total_m2
        unidad = "m²"
    
    # 5. Mostrar resultado
    print(f"\n📊 RESULTADO:")
    print("-" * 40)
    print(f"   ÁREA TOTAL: {area_total:,.2f} {unidad}")
    print("-" * 40)
    print(f"\n📌 Detalles:")
    print(f"   • Features procesadas: {features_procesadas}")
    print(f"   • Features con error: {errores}")
    
    return area_total




#Etiquetas
#########################



def actualizar_etiquetas_capa(nombre_capa, nombre_campo, mapeo_etiquetas):
    """
    Actualiza las etiquetas de una capa con simbología categorizada
    
    Parámetros:
    - nombre_capa: str, nombre de la capa en QGIS
    - nombre_campo: str, nombre del campo a categorizar
    - mapeo_etiquetas: dict, diccionario {valor: etiqueta_descriptiva}
    """
    
    print("="*60)
    print(f"🌍 ACTUALIZANDO LEYENDA DE {nombre_capa.upper()}")
    print("="*60)
    
    # 1. Obtener la capa
    capas = QgsProject.instance().mapLayersByName(nombre_capa)
    if not capas:
        print(f"❌ No se encontró la capa '{nombre_capa}'")
        return False
    
    capa = capas[0]
    
    if not capa.isValid():
        print(f"❌ La capa '{nombre_capa}' no es válida")
        return False
    
    print(f"📋 Capa: {capa.name()}")
    print(f"🎯 Campo objetivo: '{nombre_campo}'")
    
    # 2. Verificar que el campo existe
    idx_campo = capa.fields().indexFromName(nombre_campo)
    if idx_campo < 0:
        print(f"❌ El campo '{nombre_campo}' no existe en la capa")
        print("   Campos disponibles:")
        for field in capa.fields():
            print(f"   • {field.name()}")
        return False
    
    # 3. Obtener o crear renderizador categorizado
    renderer = capa.renderer()
    
    if not isinstance(renderer, QgsCategorizedSymbolRenderer):
        print("⚠️ Creando nueva simbología categorizada...")
        renderer = QgsCategorizedSymbolRenderer(nombre_campo, [])
        capa.setRenderer(renderer)
    else:
        print("✅ Usando simbología categorizada existente")
    
    renderer.setClassAttribute(nombre_campo)
    
    # 4. Obtener valores únicos del campo
    valores_unicos = capa.uniqueValues(idx_campo)
    print(f"\n📊 Valores únicos encontrados: {sorted(valores_unicos)}")
    
    # 5. Obtener categorías actuales
    categorias_actuales = renderer.categories()
    print(f"\n📊 Actualizando {len(categorias_actuales) if categorias_actuales else '0'} categorías:")
    
    # 6. Procesar según si hay categorías o no
    if not categorias_actuales:
        # Crear categorías desde cero
        print("   Creando categorías desde los datos...")
        nuevas_categorias = []
        
        for valor in sorted(valores_unicos):
            # Crear símbolo por defecto
            simbolo = QgsSymbol.defaultSymbol(capa.geometryType())
            
            # Buscar etiqueta (convertir valor a string para comparar)
            valor_str = str(valor)
            etiqueta = mapeo_etiquetas.get(valor_str, f"Valor {valor}")
            
            nuevas_categorias.append(QgsRendererCategory(valor, simbolo, etiqueta))
            print(f"   ➕ {valor} → '{etiqueta}'")
        
        # Crear nuevo renderizador
        renderer = QgsCategorizedSymbolRenderer(nombre_campo, nuevas_categorias)
        
    else:
        # Actualizar categorías existentes
        for i, cat in enumerate(categorias_actuales):
            valor = cat.value()
            etiqueta_actual = cat.label()
            
            # Convertir valor a string para buscar en el diccionario
            valor_str = str(valor)
            nueva_etiqueta = mapeo_etiquetas.get(valor_str, etiqueta_actual)
            
            # Actualizar etiqueta
            renderer.updateCategoryLabel(i, nueva_etiqueta)
            
            # Mostrar cambio
            if nueva_etiqueta != etiqueta_actual:
                print(f"   {i:2d}: {valor} → '{etiqueta_actual}' → '{nueva_etiqueta}'")
            else:
                print(f"   {i:2d}: {valor} → '{etiqueta_actual}' (sin cambios)")
    
    # 7. Aplicar cambios
    capa.setRenderer(renderer)
    capa.triggerRepaint()
    
    print(f"\n✅ Etiquetas actualizadas correctamente")
    return True



#estilos
#########################
def aplicar_estilo_comun_a_capas(capas, campo, colores_por_valor, borde_color='0, 0, 0', grosor_borde=0.2):
    """
    Aplica la misma simbología categorizada a múltiples capas de polígonos
    
    Parámetros:
    - capas: Lista de capas vectoriales (QgsVectorLayer) o nombres de capas
    - campo: Nombre del campo común para categorizar
    - colores_por_valor: Diccionario {valor: (R,G,B)} con los colores para cada categoría
    - borde_color: Color del borde en formato 'R,G,B' (opcional)
    - grosor_borde: Grosor del borde en mm (opcional)
    
    Retorna:
    - Número de capas a las que se aplicó el estilo correctamente
    """
    capas_estilizadas = 0
    
    # Convertir nombres de capas a objetos de capa si es necesario
    layers_to_style = []
    for item in capas:
        if isinstance(item, QgsVectorLayer):
            layers_to_style.append(item)
        elif isinstance(item, str):
            found_layers = QgsProject.instance().mapLayersByName(item)
            if found_layers:
                layers_to_style.extend(found_layers)
    
    for capa in layers_to_style:
        # Verificar que la capa sea válida y sea de polígonos
        if not capa.isValid():
            print(f"Advertencia: Capa '{capa.name()}' no es válida. Saltando...")
            continue
        
        if capa.geometryType() != QgsWkbTypes.PolygonGeometry:
            print(f"Advertencia: Capa '{capa.name()}' no es de polígonos. Saltando...")
            continue
            
        # Verificar que el campo exista
        if campo not in [field.name() for field in capa.fields()]:
            print(f"Advertencia: Campo '{campo}' no encontrado en capa '{capa.name()}'. Saltando...")
            continue

        # Obtener valores únicos que realmente existen en la capa
        valores_existentes = set()
        for feature in capa.getFeatures():
            valor = feature[campo]
            if valor is not None and valor != '':
                valores_existentes.add(valor)

        print(f"🔍 Valores existentes en {capa.name()}: {len(valores_existentes)}")
        print(f"🎨 Colores definidos: {len(colores_por_valor)}")

        # Filtrar colores para solo valores existentes
        colores_filtrados = {k: v for k, v in colores_por_valor.items() if k in valores_existentes}
        
        # Crear categorías SOLO para valores existentes
        categories = []
        for valor, color_rgb in colores_filtrados.items():  # ¡CAMBIADO! Usar colores_filtrados
            # Crear símbolo de relleno (siempre se ejecuta porque estamos usando colores_filtrados)
            symbol = QgsFillSymbol.createSimple({
                'color': f'{color_rgb[0]},{color_rgb[1]},{color_rgb[2]}',
                'color_border': borde_color,
                'width_border': str(grosor_borde)
            })
            
            # Crear categoría
            category = QgsRendererCategory(valor, symbol, str(valor))
            categories.append(category)
        
        # Crear y asignar renderizador
        renderer = QgsCategorizedSymbolRenderer(campo, categories)
        capa.setRenderer(renderer)

        # ¡ESTA ES LA CLAVE! Configurar para no mostrar categorías vacías
        #renderer.setShowAllSymbols(False)  # Oculta categorías sin features
        
        capa.setRenderer(renderer)

        # Forzar actualización
        capa.triggerRepaint()
        iface.layerTreeView().refreshLayerSymbology(capa.id())
        
        capas_estilizadas += 1
        print(f"Estilo aplicado a capa: {capa.name()}")
    
    # Actualizar vista del mapa
    if capas_estilizadas > 0:
        iface.mapCanvas().refreshAllLayers()
    
    return capas_estilizadas


def procesar_capa_rehabilitacion(capa, geometria_corte, capa_corte, salida_reha):
    """
    Función que procesa la capa de rehabilitación con manejo adecuado de casos vacíos
    """
    
    # 4. SELECCIÓN POR BOUNDING BOX
    print(f"\n📦 Seleccionando features por bounding box...")
    t_bbox = time.time()
    
    capa.selectByRect(geometria_corte.boundingBox())
    features_bbox = capa.selectedFeatureCount()
    print(f"   ✅ Features en bounding box: {features_bbox}")
    print(f"   ⏱️  Tiempo: {time.time()-t_bbox:.1f}s")
    
    # 5. EXTRAER SOLO LAS QUE REALMENTE INTERSECTAN
    print(f"\n🔍 Refinando con intersección real...")
    t_interseccion = time.time()
    
    selected_ids = [f.id() for f in capa.getSelectedFeatures()]
    
    if selected_ids:
        ids_str = ','.join(str(id) for id in selected_ids)
        expression = f"$id IN ({ids_str}) AND intersects($geometry, geom_from_wkt('{geometria_corte.asWkt()}'))"
        
        params_extract = {
            'INPUT': capa,
            'EXPRESSION': expression,
            'OUTPUT': 'memory:rehabilitacion_preseleccion'
        }
        
        capa1 = processing.run("qgis:extractbyexpression", params_extract)['OUTPUT']
        features_reales = capa1.featureCount()
        
        print(f"   ✅ Features que realmente intersectan: {features_reales}")
        print(f"   📊 Descartadas por bounding box: {features_bbox - features_reales}")
    else:
        print("   ⚠️ No hay features seleccionadas por bounding box")
        capa1 = None
        features_reales = 0
    
    print(f"   ⏱️  Tiempo: {time.time()-t_interseccion:.1f}s")
    
    # Limpiar selección
    capa.removeSelection()
    
    # 6. VERIFICAR QUE HAY FEATURES PARA PROCESAR
    if not capa1 or features_reales == 0:
        print("\n⚠️ ADVERTENCIA: No hay features para procesar.")
        print("   El área de corte no intersecta la capa de recuperación.")
        print("   Se creará una capa vacía para mantener el flujo del script.")
        
        # Crear una capa vacía para evitar errores posteriores
        resultado_reha = QgsVectorLayer("Polygon?crs=" + capa.crs().authid(), 
                                         salida_reha + "_sin_datos", "memory")
        QgsProject.instance().addMapLayer(resultado_reha)
        
        # Aplicar estilo a la capa vacía
        symbolreha = QgsFillSymbol.createSimple({
            'color': '157, 194, 9',
            'color_border': '139, 190, 27',
            'width_border': '0.3'
        })
        rendereha = QgsSingleSymbolRenderer(symbolreha)
        resultado_reha.setRenderer(rendereha)
        
        print("\n" + "="*60)
        print("⚠️ PROCESO COMPLETADO SIN DATOS (intersección vacía)")
        print("="*60)
        
        # EN VEZ DE sys.exit(), SIMPLEMENTE RETORNAMOS
        return False, resultado_reha
    
    # 7. CREAR ÍNDICE ESPACIAL PARA LA CAPA EXTRAÍDA
    print(f"\n📌 Creando índice espacial...")
    t_indice = time.time()
    processing.run("native:createspatialindex", {'INPUT': capa1})
    print(f"   ✅ Índice creado en {time.time()-t_indice:.1f}s")
    
    # 8. CLIP VECTORIAL
    print(f"\n✂️ Ejecutando clip vectorial...")
    t_clip = time.time()
    
    params_clip = {
        'INPUT': capa1,
        'OVERLAY': capa_corte,
        'OUTPUT': f'memory:{salida_reha}'
    }
    
    try:
        resultado_reha = processing.run("native:clip", params_clip)['OUTPUT']
        print(f"   ✅ Features resultantes: {resultado_reha.featureCount()}")
        print(f"   ⏱️  Tiempo: {time.time()-t_clip:.1f}s")
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(resultado_reha)
        print(f"   ✅ Capa '{salida_reha}' añadida al proyecto")
        
    except Exception as e:
        print(f"   ❌ Error en clip: {e}")
        print("   Intentando con algoritmo alternativo...")
        
        params_clip_alt = {
            'INPUT': capa1,
            'POLYGONS': capa_corte,
            'OUTPUT': f'memory:{salida_reha}'
        }
        resultado_reha = processing.run("native:clipvectorbypolygon", params_clip_alt)['OUTPUT']
        QgsProject.instance().addMapLayer(resultado_reha)
    
    # 9. APLICAR ESTILO
    print(f"\n🎨 Aplicando estilo...")
    t_estilo = time.time()
    
    symbolreha = QgsFillSymbol.createSimple({
        'color': '157, 194, 9',
        'color_border': '33, 66, 30',
        'width_border': '0.3'
    })
    
    rendereha = QgsSingleSymbolRenderer(symbolreha)
    resultado_reha.setRenderer(rendereha)
    resultado_reha.triggerRepaint()
    resultado_reha.updateExtents()
    
    print(f"   ✅ Estilo aplicado en {time.time()-t_estilo:.1f}s")
    
    return True, resultado_reha


#Colores
###################################

# Diccionario de mapeo: {valor_numerico: "etiqueta_descriptiva"}
mapeo_cov = {
            '111': '1.1.1 Tejido urbano continuo',
            '112': '1.1.2 Tejido urbano discontinuo',
            '121': '1.2.1 Zonas industriales o comerciales',
            '122': '1.2.2 Red vial, ferroviaria y terrenos asociados',
            '123': '1.2.3 Zonas portuarias',
            '124': '1.2.4 Aeropuertos',
            '125': '1.2.5 Obras hidráulicas',
            '131': '1.3.1 Zonas de extracción minera',
            '132': '1.3.2 Zona de disposición de residuos',
            '141': '1.4.1 Zonas verdes urbanas',
            '142': '1.4.2 Instalaciones recreativas',
            '211': '2.1.1 Otros cultivos transitorios',
            '212': '2.1.2 Cereales',
            '213': '2.1.3 Oleaginosas y leguminosas',
            '214': '2.1.4 Hortalizas',
            '215': '2.1.5 Tubérculos',
            '221': '2.2.1 Cultivos permanentes herbáceos',
            '222': '2.2.2 Cultivos permanentes arbustivos',
            '223': '2.2.3 Cultivos permanentes arbóreos',
            '224': '2.2.4 Cultivos agroforestales',
            '225': '2.2.5 Cultivos confinados',
            '231': '2.3.1 Pastos limpios',
            '232': '2.3.2 Pastos arbolados',
            '233': '2.3.3 Pastos enmalezados',
            '241': '2.4.1 Mosaico de cultivos',
            '242': '2.4.2 Mosaico de pastos y cultivos',
            '243': '2.4.3 Mosaico de cultivos, pastos y espacios naturales',
            '244': '2.4.4 Mosaico de pastos con espacios naturales',
            '245': '2.4.5 Mosaico de cultivos con espacios naturales',
            '311': '3.1.1 Bosque denso',
            '312': '3.1.2 Bosque abierto',
            '313': '3.1.3 Bosque fragmentado',
            '314': '3.1.4 Bosque de galería y ripario',
            '315': '3.1.5 Plantación forestal',
            '321': '3.2.1 Herbazal',
            '322': '3.2.2 Arbustal',
            '323': '3.2.3 Vegetación secundaria o en transición',
            '331': '3.3.1 Zonas arenosas naturales',
            '332': '3.3.2 Afloramientos rocosos',
            '333': '3.3.3 Tierras desnudas y degradadas',
            '334': '3.3.4 Zonas quemadas',
            '335': '3.3.5 Zonas glaciares y nivales',
            '411': '4.1.1 Zonas Pantanosas',
            '412': '4.1.2 Turberas',
            '413': '4.1.3 Vegetación acuática sobre cuerpos de agua',
            '421': '4.2.1 Pantanos costeros',
            '422': '4.2.2 Salitral',
            '423': '4.2.3 Sedimentos expuestos en bajamar',
            '511': '5.1.1 Ríos',
            '512': '5.1.2 Lagunas, lagos y ciénagas naturales',
            '513': '5.1.3 Canales',
            '514': '5.1.4 Cuerpos de agua artificiales',
            '521': '5.2.1 Lagunas costeras',
            '523': '5.2.3 Estanques para acuicultura marina'
        }

# Definir mapeo específico para POMCAS
mapeo_pomcas = {
    '01': 'Áreas del SINAP',
    '02': 'Áreas complementarias a la conservación',
    '03': 'Áreas de importancia ambiental',
    '04': 'Áreas con reglamentación especial',
    '05': 'Áreas de amenazas naturales',
    '06': 'Áreas de restauración ecológica',
    '07': 'Áreas de rehabilitación',
    '08': 'Áreas de recuperación para el uso múltiple',
    '09': 'Áreas agrícolas',
    '10': 'Áreas agrosilvopastoriles',
    '11': 'Áreas urbanas municipales y distritales',
    '12': 'Áreas objeto de ajuste cartográfico',
    '13': 'Otras subzonas de uso y manejo'
}

mapeo_priocon = {
            'a': 'Omisiones, Urgentes, Naturales Y Oportunas',
            'b': 'Omisiones, Urgentes,naturales Y Sin Oportunidad',
            'c': 'Omisiones, Urgentes Y Seminaturales',
            'd': 'Omisiones Sin Urgencia',
            'e': 'Alta Insuficiencia Y Urgente',
            'f': 'Alta Insuficiencia Sin Urgencia',
            'g': 'Baja Insuficiencia Y Urgente',
            'h': 'Baja Insuficiencia Y Sin Urgencia'
            }



colores_ambitos = {
            'AEIA': (42, 128, 0),
            'Franja Estabilización': (150, 111, 214),
            'Frontera Agrícola': (255, 215, 0),
       }

colores_cov = {
            '1.1.1. Tejido urbano continuo': (204, 0, 0),
            '1.1.2. Tejido urbano discontinuo': (248, 0, 0),
            '1.2.1. Zonas industriales o comerciales': (204, 77, 42),
            '1.2.2. Red vial, ferroviaria y terrenos asociados': (217, 101, 69),
            '1.2.3. Zonas portuarias': (225, 132, 107),
            '1.2.4. Aeropuertos': (231, 156, 135),
            '1.2.5. Obras hidráulicas': (238, 185, 170),
            '1.3.1. Zonas de extracción minera': (167, 0, 204),
            '1.3.2. Zona de disposición de residuos': (212, 23, 255),
            '1.4.1. Zonas verdes urbanas': (255, 128, 128),
            '1.4.2. Instalaciones recreativas': (255, 176, 176),
            '2.1.1. Otros cultivos transitorios': (255, 255, 166),
            '2.1.2. Cereales': (255, 255, 95),
            '2.1.3. Oleaginosas y leguminosas': (238, 232, 0),
            '2.1.4. Hortalizas': (209, 206, 0),
            '2.1.5. Tubérculos': (181, 178, 0),
            '2.2.1. Cultivos permanentes herbáceos': (242, 205, 167),
            '2.2.2. Cultivos permanentes arbustivos': (237, 183, 128),
            '2.2.3. Cultivos permanentes arbóreos': (232, 161, 90),
            '2.2.4. Cultivos agroforestales': (227, 141, 54),
            '2.2.5. Cultivos confinados': (214, 122, 30),
            '2.3.1. Pastos limpios': (204, 255, 204),
            '2.3.2. Pastos arbolados': (158, 255, 158),
            '2.3.3. Pastos enmalezados': (158, 255, 200),
            '2.4.1. Mosaico de cultivos': (255, 230, 166),
            '2.4.2. Mosaico de pastos y cultivos': (255, 216, 117),
            '2.4.3. Mosaico de cultivos, pastos y espacios naturales': (255, 201, 64),
            '2.4.4. Mosaico de pastos con espacios naturales': (255, 183, 0),
            '2.4.5. Mosaico de cultivos con espacios naturales': (214, 154, 0),
            '3.1.1. Bosque denso': (71, 143, 0),
            '3.1.2. Bosque abierto': (85, 171, 0),
            '3.1.3. Bosque fragmentado': (97, 194, 0),
            '3.1.4. Bosque de galería y ripario': (112, 224, 0),
            '3.1.5. Plantación forestal': (128, 255, 0),
            '3.2.1. Herbazal': (204, 242, 78),
            '3.2.2. Arbustal': (172, 219, 15),
            '3.2.3. Vegetación secundaria o en transición': (150, 191, 13),
            '3.3.1. Zonas arenosas naturales': (194, 194, 194),
            '3.3.2. Afloramientos rocosos': (179, 179, 179),
            '3.3.3. Tierras desnudas y degradadas': (158, 158, 158),
            '3.3.4. Zonas quemadas': (138, 138, 138),
            '3.3.5. Zonas glaciares y nivales': (101, 101, 181),
            '4.1.1. Zonas Pantanosas': (166, 166, 255),
            '4.1.2. Turberas': (145, 145, 255),
            '4.1.3. Vegetación acuática sobre cuerpos de agua': (115, 115, 255),
            '4.2.1. Pantanos costeros': (204, 204, 255),
            '4.2.2. Salitral': (184, 184, 255),
            '4.2.3. Sedimentos expuestos en bajamar': (166, 166, 255),
            '5.1.1. Ríos': (0, 0, 248),
            '5.1.2. Lagunas, lagos y ciénagas naturales': (0, 128, 255),
            '5.1.3. Canales': (0, 178, 255),
            '5.1.4. Cuerpos de agua artificiales': (0, 206, 242),
            '5.2.1. Lagunas costeras': (69, 224, 245),
            '5.2.3. Estanques para acuicultura marina': (204, 246, 255)
        }

colores_parques = {
    'Zona Primitiva': (80, 125, 42),
    'Zona Intangible': (116, 195, 101),
    'Zona de Recuperación Natural': (157, 194, 9),
    'Zona Amortiguadora': (232, 244, 140),
    'Zona de Alta Densidad de Uso': (206,200,239),
    'Zona de Recreación General Exterior': (136, 120, 195),
    'Zona Histórico Cultural': (114, 47, 55),
    'Otra Zonificación': (220, 220, 220)
    }

colores_cov1 = {
            '111': (204, 0, 0),
            '112': (248, 0, 0),
            '121': (204, 77, 42),
            '122': (217, 101, 69),
            '123': (225, 132, 107),
            '124': (231, 156, 135),
            '125': (238, 185, 170),
            '131': (167, 0, 204),
            '132': (212, 23, 255),
            '141': (255, 128, 128),
            '142': (255, 176, 176),
            '211': (255, 255, 166),
            '212': (255, 255, 95),
            '213': (238, 232, 0),
            '214': (209, 206, 0),
            '215': (181, 178, 0),
            '221': (242, 205, 167),
            '222': (237, 183, 128),
            '223': (232, 161, 90),
            '224': (227, 141, 54),
            '225': (214, 122, 30),
            '231': (204, 255, 204),
            '232': (158, 255, 158),
            '233': (158, 255, 200),
            '241': (255, 230, 166),
            '242': (255, 216, 117),
            '243': (255, 201, 64),
            '244': (255, 183, 0),
            '245': (214, 154, 0),
            '311': (71, 143, 0),
            '312': (85, 171, 0),
            '313': (97, 194, 0),
            '314': (112, 224, 0),
            '315': (128, 255, 0),
            '321': (204, 242, 78),
            '322': (172, 219, 15),
            '323': (150, 191, 13),
            '331': (194, 194, 194),
            '332': (179, 179, 179),
            '333': (158, 158, 158),
            '334': (138, 138, 138),
            '335': (101, 101, 181),
            '411': (166, 166, 255),
            '412': (145, 145, 255),
            '413': (115, 115, 255),
            '421': (204, 204, 255),
            '422': (184, 184, 255),
            '423': (166, 166, 255),
            '511': (0, 0, 248),
            '512': (0, 128, 255),
            '513': (0, 178, 255),
            '514': (0, 206, 242),
            '521': (69, 224, 245),
            '523': (204, 246, 255)
        }

colores_pomcas1 = {
    'Áreas del SINAP': (60,179,113),
    'Áreas complementarias a la conservación': (169,186,157),
    'Áreas de importancia ambiental': (86,130,3),
    'Áreas con reglamentación especial': (139,190,27),
    'Áreas de amenazas naturales': (255,140,105),
    'Áreas de restauración ecológica': (173,255,47),
    'Áreas de rehabilitación': (181,166,66),
    'Áreas de recuperación para el uso múltiple': (251,171,96),
    'Áreas agrícolas': (194,178,128),
    'Áreas agrosilvopastoriles': (210,105,30),
    'Áreas urbanas municipales y distritales': (250, 5, 21),
    'Áreas objeto de ajuste cartográfico': (194, 194, 194), #gris
    'Otras subzonas de uso y manejo': (212, 23, 255)
    }

colores_pomcas2 = {
    '01': (60,179,113),
    '02': (169,186,157),
    '03': (86,130,3),
    '04': (139,190,27),
    '05': (255,140,105),
    '06': (173,255,47),
    '07': (181,166,66),
    '08': (251,171,96),
    '09': (194,178,128),
    '10': (210,105,30),
    '11': (250, 5, 21),
    '12': (194, 194, 194), #gris
    '13': (212, 23, 255)
    }


colores_pomca = {
    '01': (60, 179, 113),
    '02': (169, 186, 157),
    '03': (86, 130, 3),
    '04': (139, 190, 27),
    '05': (255, 140, 105),
    '06': (173, 255, 47),
    '07': (181, 166, 66),
    '08': (251, 171, 96),
    '09': (194, 178, 128),
    '10': (210, 105, 30),
    '11': (250, 5, 21),
    '12': (194, 194, 194), #gris
    '13': (212, 23, 255)
    }

colores_forestal = {
'A': (197,227,132),
'B': (233,255,219),
'C': (227,218,201),
'ÁREAS CON PREVIA DECISIÓN DE ORDENAMIENTO': (255,200,124)
    }

colores_priocon = {
            'a': (255, 0, 40),
            'b': (255, 56, 0),
            'c': (255, 130, 67),
            'd': (255, 103, 0),
            'e': (237, 145, 33),
            'f': (255, 191, 0),
            'g': (255, 246, 0),
            'h': (255, 255, 0),
            }

colores_eco = {
            'Agroecosistema arrocero': (255, 245, 235),
            'Agroecosistema cafetero': (252, 239, 227),
            'Agroecosistema cañero': (250, 234, 220),
            'Agroecosistema de cultivos permanentes': (247, 224, 205),
            'Agroecosistema de cultivos transitorios': (247, 221, 200),
            'Agroecosistema de mosaico de cultivos y espacios naturales': (245, 211, 186),
            'Agroecosistema de mosaico de cultivos y pastos': (242, 204, 179),
            'Agroecosistema de mosaico de cultivos, pastos y espacios naturales': (240, 198, 173),
            'Agroecosistema de mosaico de pastos y espacios naturales': (240, 194, 165),
            'Agroecosistema forestal': (237, 188, 159),
            'Agroecosistema ganadero': (237, 183, 154),
            'Agroecosistema palmero': (235, 177, 145),
            'Agroecosistema papero': (235, 172, 141),
            'Agroecosistema platanero y bananero': (232, 165, 135),
            'Arbustal andino humedo': (162, 181, 65),
            'Arbustal basal humedo': (150, 168, 59),
            'Arbustal inundable andino': (131, 148, 46),
            'Arbustal inundable basal': (122, 138, 41),
            'Arbustal inundable costero': (125, 150, 36),
            'Arbustal inundable subandino': (112, 128, 36),
            'Arbustal subandino humedo': (103, 117, 30),
            'Bosque andino humedo': (42, 173, 42),
            'Bosque andino seco': (40, 163, 38),
            'Bosque basal humedo': (37, 158, 35),
            'Bosque basal seco': (35, 156, 33),
            'Bosque de galeria basal humedo': (32, 150, 30),
            'Bosque de galeria basal seco': (31, 145, 29),
            'Bosque de galeria inundable basal': (29, 143, 27),
            'Bosque de galeria inundable costero': (27, 138, 25),
            'Bosque fragmentado con pastos y cultivos': (21, 125, 19),
            'Bosque fragmentado con vegetacion secundaria': (22, 128, 20),
            'Bosque inundable andino': (20, 120, 18),
            'Bosque inundable basal': (19, 115, 16),
            'Bosque inundable costero': (18, 112, 15),
            'Bosque inundable subandino': (16, 107, 13),
            'Bosque mixto de guandal': (14, 102, 11),
            'Bosque ripario inundable subandino': (13, 97, 10),
            'Bosque subandino humedo': (12, 94, 9),
            'Bosque subandino seco': (11, 89, 8),
            'Complejos rocosos de los andes': (166, 66, 46),
            'Complejos rocosos de serranias': (138, 56, 36),
            'Coralino continental': (240, 98, 127),
            'Coralino oceanico': (122, 142, 245),
            'Cuerpo de agua artificial': (119, 150, 178),
            'Desierto': (252, 180, 10),
            'Fondos blandos': (237, 222, 50),
            'Fondos blandos con vegetacion no vascular': (190, 255, 232),
            'Fondos duros con vegetacion no vascular': (99, 209, 130),
            'Fondos duros no coralinos': (212, 157, 68),
            'Glaciares y nivales': (242, 241, 237),
            'Herbazal andino humedo': (204, 184, 55),
            'Herbazal basal humedo': (191, 173, 52),
            'Herbazal inundable andino': (179, 161, 48),
            'Herbazal inundable basal': (166, 150, 45),
            'Herbazal inundable costero': (153, 138, 41),
            'Herbazal inundable subandino': (140, 127, 38),
            'Herbazal subandino humedo': (128, 115, 34),
            'Lago Tectonico': (0, 183, 198),
            'Laguna Aluvial': (0, 181, 214),
            'Laguna costera': (0, 122, 165),
            'Laguna Glacial': (76, 206, 209),
            'Laguna Tectonica': (40, 196, 216),
            'Llanura mareal': (140, 224, 209),
            'Manglar': (9, 84, 7),
            'Manglar de aguas marinas': (8, 82, 6),
            'Manglar de aguas mixohalinas': (7, 77, 5),
            'Otras areas': (186, 186, 184),
            'Paramo': (132, 0, 168),
            'Playas costeras': (255, 255, 173),
            'Pradera de pastos marinos': (153, 235, 0),
            'Rio de Aguas Blancas': (0, 114, 198),
            'Rio de Aguas Claras': (0, 63, 119),
            'Rio de Aguas Negras': (0, 56, 107),
            'Sabana estacional': (250, 219, 20),
            'Sabana inundable': (84, 183, 198),
            'Sin informacion': (255, 255, 255),
            'Subxerofitia andina': (255, 0, 255),
            'Subxerofitia basal': (212, 110, 212),
            'Subxerofitia subandina': (255, 28, 206),
            'Territorio artificializado': (250, 5, 21),
            'Transicional transformado': (0, 96, 124),
            'Transicional transformado costero': (63, 96, 117),
            'Turbera andina': (94, 221, 161),
            'Turbera de paramo': (94, 221, 193),
            'Vegetacion secundaria': (96, 222, 64),
            'Xerofitia arida': (232, 88, 210),
            'Xerofitia desertica': (250, 95, 227),
            'Zona pantanosa andina': (58, 95, 158),
            'Zona pantanosa basal': (60, 88, 143),
            'Zona pantanosa subandina': (58, 73, 114),
            'Zonas arenosas naturales': (255, 255, 207),
            'Zonas pantanosas costeras': (59, 74, 115),
            'Zonas pantanosas salinas': (102, 147, 188)
        }


colores_eco1 = {
            'Agroecosistema Arrocero': (255, 248, 241),
            'Agroecosistema Cafetero': (253, 244, 235),
            'Agroecosistema Cañero': (252, 240, 231),
            'Agroecosistema Forestal': (242, 208, 188),
            'Agroecosistema Ganadero': (242, 205, 184),
            'Agroecosistema Palmero': (241, 200, 178),
            'Agroecosistema Papero': (241, 197, 175),
            'Agroecosistema Platanero y Bananero': (239, 192, 171),
            'Agroecosistema de Cultivos Permanentes': (249, 233, 220),
            'Agroecosistema de Cultivos Transitorios': (249, 231, 217),
            'Agroecosistema de Mosaico de Cultivos y Espacios Naturales': (248, 224, 207),
            'Agroecosistema de Mosaico de Cultivos y Pastos': (246, 219, 202),
            'Agroecosistema de Mosaico de Cultivos, Pastos y Espacios Naturales': (253, 215, 198),
            'Agroecosistema de Mosaico de Pastos y Espacios Naturales': (245, 212, 192),
            'Arbustal Andino Humedo': (190, 203, 122),
            'Arbustal Basal Humedo': (182, 194, 118),
            'Arbustal Inundable Andino': (168, 180, 109),
            'Arbustal Inundable Basal': (162, 173, 105),
            'Arbustal Inundable Costero': (159, 168, 103),
            'Arbustal Inundable Subandino': (155, 166, 102),
            'Arbustal Subandino Humedo': (149, 158, 98),
            'Bosque Andino Humedo': (106, 198, 106),
            'Bosque Andino Seco': (105, 191, 103),
            'Bosque Basal Humedo': (102, 187, 101),
            'Bosque Basal Seco': (101, 186, 100),
            'Bosque Fragmentado con Pastos y Cultivos': (91, 164, 90),
            'Bosque Fragmentado con Vegetacion Secundaria': (92, 166, 91),
            'Bosque Inundable Andino': (91, 161, 89),
            'Bosque Inundable Basal': (90, 157, 88),
            'Bosque Inundable Costero': (89, 155, 87),
            'Bosque Inundable Subandino': (88, 151, 86),
            'Bosque Ripario Inundable Subandino': (86, 144, 84),
            'Bosque Subandino Humedo': (85, 142, 83),
            'Bosque Subandino Seco': (84, 139, 82),
            'Bosque de Galeria Basal Humedo': (99, 182, 98),
            'Bosque de Galeria Basal Seco': (98, 178, 97),
            'Bosque de Galeria Inundable Basal': (97, 177, 95),
            'Bosque de Galeria Inundable Costero': (95, 173, 94),
            'Complejos Rocosos Andinos': (193, 123, 109),
            'Complejos Rocosos de Serranias': (173, 116, 102),
            'Coralino Continental': (245, 145, 165),
            'Coralino Oceanico': (162, 176, 248),
            'Cuerpo de Agua Artificial': (160, 182, 201),
            'Desierto': (253, 203, 84),
            'Fondos Blandos': (242, 232, 112),
            'Fondos Blandos con Vegetacion No Vascular': (210, 255, 239),
            'Fondos Duros No Coralinos': (225, 186, 124),
            'Fondos Duros con Vegetacion No Vascular': (146, 223, 168),
            'Glaciares y Nivales': (246, 245, 242),
            'Herbazal Andino Humedo': (219, 205, 115),
            'Herbazal Basal Humedo': (210, 198, 113),
            'Herbazal Inundable Andino': (202, 189, 110),
            'Herbazal Inundable Basal': (193, 182, 108),
            'Herbazal Inundable Costero': (184, 173, 105),
            'Herbazal Inundable Subandino': (175, 165, 103),
            'Herbazal Subandino Humedo': (166, 157, 100),
            'Laguna Aluvial': (77, 203, 226),
            'Laguna Costera': (77, 162, 192),
            'Laguna Glacial': (130, 221, 223),
            'Laguna Tectonica': (105, 214, 228),
            'Llanura Mareal': (175, 233, 223),
            'Manglar': (83, 135, 81),
            'Paramo': (169, 77, 194),
            'Playas Costeras': (255, 255, 198),
            'Pradera de Pastos Marinos': (184, 241, 77),
            'Rio de Aguas Blancas': (77, 156, 215),
            'Rio de Aguas Claras': (77, 121, 160),
            'Rio de Aguas Negras': (77, 116, 151),
            'Sabana Estacional': (252, 230, 91),
            'Sabana Inundable': (135, 205, 215),
            'Subxerofitia Andina': (255, 77, 255),
            'Subxerofitia Basal': (225, 154, 225),
            'Subxerofitia Subandina': (255, 96, 221),
            'Territorio Artificializado': (252, 80, 91),
            'Transicional Transformado': (77, 144, 163),
            'Transicional Transformado Costero': (121, 144, 158),
            'Turbera Andina': (142, 231, 189),
            'Turbera de Paramo': (142, 231, 212),
            'Vegetación Secundaria': (144, 232, 121),
            'Xerofitia Arida': (239, 138, 224),
            'Xerofitia Desertica': (252, 143, 235),
            'Zona Pantanosa Andina': (117, 143, 187),
            'Zona Pantanosa Basal': (119, 138, 177),
            'Zona Pantanosa Subandina': (118, 128, 157),
            'Zonas Arenosas Naturales': (255, 255, 221),
            'Zonas Pantanosas Costeras': (117, 128, 156),
            'Zonas Pantanosas Salinas': (148, 179, 208),
       }


colores_zonip = {
            'Preservación': (92, 194, 0),
            'Protección con uso sostenible': (158, 255, 200),
            'Protección por Alta Oferta de SSEE': (212, 23, 255),
            'Restauración': (94, 221, 193),
            'Uso productivo': (166, 66, 46),
            'Uso productivo con protección': (150, 168, 59),
            'Uso productivo con reconversión': (255, 255, 95),
            'Uso sostenible para el aprovechamiento de la biodiversidad': (243, 156, 18),
            'Uso sostenible para el desarrollo': (248, 196, 113),
            }




#Limpiar capas existentes
####################################

for nombre_capa in nombres_capas:
    # 1. Verificar si la capa ya existe
    capas_existentes = QgsProject.instance().mapLayersByName(nombre_capa)
    
    # 2. Eliminar todas las instancias (evita duplicados)
    if capas_existentes:
        for capa in capas_existentes:
            QgsProject.instance().removeMapLayer(capa)
        print(f"🗑️ Capa '{nombre_capa}' eliminada.")

QgsProject.instance().removeAllMapLayers()
print("✅ Todas las capas han sido eliminadas")


# Cargar OpenStreetMap
############################################

osm_layer = QgsRasterLayer(
    'type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png&zmax=19&zmin=0',
    'OpenStreetMap',
    'wms'
)

if osm_layer.isValid():
    QgsProject.instance().addMapLayer(osm_layer)
else:
    print("Error al cargar OpenStreetMap")


# 1a. Cargar la capa de Oceano
##################################################
# Método correcto para cargar una capa vectorial
olayer = QgsVectorLayer(oceano_path, 'oceano', 'ogr')

# Verificar si la capa se cargó correctamente
if olayer.isValid():
    # Crear un símbolo simple para el océano (azul claro)
    symbol = QgsFillSymbol.createSimple({
        'color': '147, 204, 234',  # '25, 100, 180' azul
        'color_border': '176, 208, 248',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
    })
    
    olayer.setOpacity(0.9)

    # Aplicar el símbolo a la capa
    olayer.renderer().setSymbol(symbol)
    
    # Añadir la capa al proyecto si no está ya añadida
    if not QgsProject.instance().mapLayersByName('oceano'):
        QgsProject.instance().addMapLayer(olayer)
    
    # Refrescar la visualización
    olayer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(olayer.id())
    
    print("Capa de océano cargada y estilizada correctamente")
else:
    print("¡Error al cargar la capa de océano!")


# 1a. Cargar la capa de Abya Yala(regiones)
##################################################

relayer = QgsVectorLayer(region_path, 'region', 'ogr')

# Verificar carga correcta
if not relayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # Construir expresión de selección (usando el campo REGION_WB)
    expression = f"REGION_WB = '{region}'"  # Buscar coincidencia exacta
        
    relayer.selectByExpression(expression)
    
    # Verificar selección y crear nueva capa
    if relayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(relayer.crs().authid()),
            "regiones_seleccionados",
            "memory"
        )

        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(relayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = relayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} país(es)!")
        
        # Aplicar estilo
        symbol = QgsFillSymbol.createSimple({
            'color': '250, 250, 250',  # Blanco hueso
            'color_border': '200, 200, 200',  # Gris
            'width_border': '0.3'
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        selection_layer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().setExtent(selection_layer.extent())
        iface.mapCanvas().refresh()

# 1a. Cargar la capa de Colombia (Pais)
#####################################################
palayer = QgsVectorLayer(pais_path, 'pais', 'ogr')



# Verificar carga correcta
if not palayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # 2. Seleccionar features por código DANE
    codigos_pais = cpais
    
    # Construir expresión de selección
    

    expression = "SOV_A3 IN ({})".format(','.join(["'{}'".format(c) for c in codigos_pais]))

    palayer.selectByExpression(expression)
    
    # 3. Verificar selección y crear nueva capa
    if palayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(palayer.crs().authid()),
            "paises_seleccionados",
            "memory"
        )

        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(palayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = palayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} departamento(s)!")
        
        # Aplicar estilo a la capa recién creada
        symbol = QgsFillSymbol.createSimple({
            'color': '230, 230, 230',  # Gris Claro
            'color_border': '180, 180, 180',  # 
            'width_border': '0.1'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        selection_layer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().zoomToSelected(palayer)
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron Paises con los códigos especificados")
        print("Nombres de campos disponibles:", [field.name() for field in palayer.fields()])


# 1a. Cargar la capa de Colombia con departamentos
#############################################
deplayer = iface.addVectorLayer(departamentos_path, 'departamentos', 'ogr')


if deplayer:
    # Crear un símbolo simple
    symbol = QgsFillSymbol.createSimple({
        'color': '230, 230, 230',  # Gris Claro
        'color_border': '180, 180, 180',  
        'width_border': '0.2'  # Grosor del borde en mm
    })

    deplayer.setOpacity(0.9)
    
    # Aplicar el símbolo a la capa
    deplayer.renderer().setSymbol(symbol)
    
    # Refrescar la capa para ver los cambios
    deplayer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(deplayer.id())

# Verificar carga correcta
if not deplayer.isValid():
    print("¡Error al cargar el shapefile!")
else:

# 2. Seleccionar departamento
#########################################################
    codigos_dane = codigos_dep
    
    # Construir expresión de selección
    

    expression = "DPTO_CCDGO IN ({})".format(','.join(["'{}'".format(c) for c in codigos_dane]))

    deplayer.selectByExpression(expression)
    
    # 3. Verificar selección y crear nueva capa
    if deplayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(deplayer.crs().authid()),
            "departamentos_seleccionados",
            "memory"
        )

        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(deplayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = deplayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} departamento(s)!")

        # Estilo diferenciado para selección
        highlight_symbol = QgsFillSymbol.createSimple({
            'color': '220, 208, 255',  # Vinotinto
            'outline_color': '75, 0, 130',  # Indigo
            'outline_width': '0.5'
        })
        selection_layer.renderer().setSymbol(highlight_symbol)
        selection_layer.setOpacity(0.9)


        # Zoom a la selección
        iface.mapCanvas().zoomToSelected(deplayer)
        iface.mapCanvas().refresh()

        deplayer.removeSelection()  # Elimina la selección actual

    else:
        print("No se encontraron Departamentos con los códigos especificados")
        print("Nombres de campos disponibles:", [field.name() for field in deplayer.fields()])



# 1b. Cargar la capa de municipios seleccionados
####################################################################
munlayer = QgsVectorLayer(municipios_path, 'municipios', 'ogr')


# Verificar carga correcta
if not munlayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # Definir códigos de departamento
    codigos_dep = codigomdep  # Reemplaza con tus códigos reales
    
    # Construir expresión de selección
    expression = "DPTO_CCDGO IN ({})".format(','.join(["'{}'".format(c) for c in codigos_dep]))
    munlayer.selectByExpression(expression)
    
    # Verificar selección y crear nueva capa
    if munlayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(munlayer.crs().authid()),
            "MunicipiosDep2",
            "memory"
        )

        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(munlayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = munlayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        selection_layer.setOpacity(0.9)
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} municipio(s) de los departamentos especificados!")

        # Aplicar estilo a la capa recién creada
        symbol = QgsFillSymbol.createSimple({
            'color': '220, 208, 255',  # Vinotinto
            'color_border': '75, 0, 130',  # Indigo
            'width_border': '0.3'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        munlayer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().setExtent(selection_layer.extent())
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron municipios con los códigos de departamento especificados")
        print("Nombres de campos disponibles:", [field.name() for field in munlayer.fields()])




# Verificar carga correcta
if not munlayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # 2. Seleccionar features por código DANE
    codigos_dane = codigos_muni
    
    # Construir expresión de selección
    expression = "MPIO_CDPMP IN ({})".format(','.join(["'{}'".format(c) for c in codigos_dane]))

    munlayer.selectByExpression(expression)
    
    # 3. Verificar selección y crear nueva capa
    if munlayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(munlayer.crs().authid()),
            "municipios_seleccionados",
            "memory"
        )
    
        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(munlayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = munlayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        selection_layer.setOpacity(0.9)
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} municipio(s)!")

        # Aplicar estilo a la capa recién creada
        symbol = QgsFillSymbol.createSimple({
            'color': '154, 185, 115',  # Oliva
            'color_border': '0, 100, 0',  # Dark green
            'width_border': '0.5'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        
        selection_layer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().zoomToSelected(munlayer)
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron municipios con los códigos especificados")
        print("Nombres de campos disponibles:", [field.name() for field in munlayer.fields()])


# 1b. Cargar la capa de resguardos
####################################################################

# Versión simplificada
resglayer = QgsVectorLayer(resguardos_path, 'resguardos', 'ogr')
#resglayer1 = iface.addVectorLayer(resguardos_path, 'resguardos', 'ogr')
#asociaciones = iface.addVectorLayer(asociaciones_path, 'asociaciones', 'ogr')

if resglayer.isValid():
    # Seleccionar por códigos de municipio
    expression = "MUNICIPIO IN ({})".format(','.join(["'{}'".format(c) for c in codigos_muni]))
    resglayer.selectByExpression(expression)
    
    if resglayer.selectedFeatureCount() > 0:
        # Crear nueva capa con la selección
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(resglayer.crs().authid()),
            "resguardos_seleccionados", 
            "memory"
        )
        
        # Copiar TODOS los campos y TODAS las features
        provider = selection_layer.dataProvider()
        provider.addAttributes(resglayer.fields())
        selection_layer.updateFields()
        provider.addFeatures(resglayer.selectedFeatures())
        selection_layer.updateExtents()
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"✅ Capa creada con {resglayer.selectedFeatureCount()} resguardos")
        
        # Estilo y zoom
        symbol = symbol = QgsFillSymbol.createSimple({
            'color': '253, 188, 180',  # Sunglow
            'color_border': '255, 135, 141',  # Indigo
            'width_border': '0.5'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        iface.mapCanvas().setExtent(selection_layer.extent())
        
    else:
        print("❌ No se encontraron resguardos")





# Construir expresión de selección
expression = "ID IN ({})".format(','.join(["'{}'".format(c) for c in codigores]))

resglayer.selectByExpression(expression)

# 3. Verificar selección y crear nueva capa
if resglayer.selectedFeatureCount() > 0:
    # Crear capa temporal
    selection_layer = QgsVectorLayer(
        "Polygon?crs={}".format(resglayer.crs().authid()),
        "resguardo_seleccionado",
        "memory"
    )

    # Copiar estructura de campos
    provider = selection_layer.dataProvider()
    provider.addAttributes(resglayer.fields())
    selection_layer.updateFields()
    
    # Copiar features seleccionadas
    features = resglayer.selectedFeatures()
    provider.addFeatures(features)
    selection_layer.updateExtents()
    selection_layer.setOpacity(0.9)
    
    # Añadir al proyecto
    QgsProject.instance().addMapLayer(selection_layer)
    print(f"¡Se seleccionaron {len(features)} municipio(s)!")

    # Aplicar estilo a la capa recién creada
    symbol = QgsFillSymbol.createSimple({
        'color': '#D59F0F',  # Oliva
        'color_border': '#FFED00',  # Dark green
        'width_border': '0.5'     # Grosor del borde
    })
    selection_layer.renderer().setSymbol(symbol)
    selection_layer.triggerRepaint()
    
    selection_layer.setOpacity(0.9)

    # Zoom a la selección
    iface.mapCanvas().zoomToSelected(resglayer)
    iface.mapCanvas().refresh()
else:
    print("No se encontraron resguardos con los códigos especificados")
    print("Nombres de campos disponibles:", [field.name() for field in resglayer.fields()])

# 1b. Cargar la capa de consejos
####################################################################

# Versión simplificada
conlayer = QgsVectorLayer(consejos_path, 'consejos', 'ogr')

if conlayer.isValid():
    # Seleccionar por códigos de municipio
    expression = "MUNICIPIO IN ({})".format(','.join(["'{}'".format(c) for c in codigos_muni]))
    conlayer.selectByExpression(expression)
    
    if conlayer.selectedFeatureCount() > 0:
        # Crear nueva capa con la selección
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(conlayer.crs().authid()),
            "consejos", 
            "memory"
        )
        
        # Copiar TODOS los campos y TODAS las features
        provider = selection_layer.dataProvider()
        provider.addAttributes(conlayer.fields())
        selection_layer.updateFields()
        provider.addFeatures(conlayer.selectedFeatures())
        selection_layer.updateExtents()
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"✅ Capa creada con {conlayer.selectedFeatureCount()} consejos")
        
        # Estilo y zoom
        symbol = symbol = QgsFillSymbol.createSimple({
            'color': '220, 220, 220',  # Sunglow
            'color_border': '128, 128, 128',  # Indigo
            'width_border': '0.5'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        iface.mapCanvas().setExtent(selection_layer.extent())
        
    else:
        print("❌ No se encontraron consejos")


#Asociaciones Amazonas
###################################

# Cargar la capa
asolayer = QgsVectorLayer(asociaciones_path, 'asociaciones', "ogr")


# 3. Configurar parámetros para el clip
params_asociaciones = {
        'INPUT': asolayer,    # Capa a cortar (ecosistemas)
        'OVERLAY': 'resguardos_seleccionados',  # Capa de corte (consejos)
        'OUTPUT': 'memory:asociaciones'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_asociaciones = processing.run("native:clip", params_asociaciones)
clipped_aso = result_asociaciones['OUTPUT']
clipped_aso.setName("asociaciones seleccionados")
QgsProject.instance().addMapLayer(clipped_aso)

symbolaso = QgsFillSymbol.createSimple({
        'color': '253, 188, 180, 70',  # '25, 100, 180' azul
        'color_border': '255, 135, 141',  # Color del borde
        'width_border': '0.5'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendereraso = QgsSingleSymbolRenderer(symbolaso)
clipped_aso.setRenderer(rendereraso)

# Refrescar la capa para ver los cambios
clipped_aso.triggerRepaint()


#asociacion seleccionada
###############################################################

# Cargar la capa
asolayer = QgsVectorLayer(asociaciones_path, 'asociaciones', "ogr")

# Construir expresión de selección
expression = "OBJECTID IN ({})".format(','.join(["'{}'".format(c) for c in codigoa]))


asolayer.selectByExpression(expression)

# 3. Verificar selección y crear nueva capa
if asolayer.selectedFeatureCount() > 0:
    # Crear capa temporal
    selection_layer = QgsVectorLayer(
        "Polygon?crs={}".format(asolayer.crs().authid()),
        "asociacion_seleccionada",
        "memory"
    )

    # Copiar estructura de campos
    provider = selection_layer.dataProvider()
    provider.addAttributes(asolayer.fields())
    selection_layer.updateFields()
    
    # Copiar features seleccionadas
    features = asolayer.selectedFeatures()
    provider.addFeatures(features)
    selection_layer.updateExtents()
    selection_layer.setOpacity(0.9)
    
    # Añadir al proyecto
    QgsProject.instance().addMapLayer(selection_layer)
    print(f"¡Se seleccionaron {len(features)} asociacion(es)!")

    # Aplicar estilo a la capa recién creada
    symbol = QgsFillSymbol.createSimple({
        'color': '252, 255, 164',  # Oliva
        'color_border': '238, 210, 2',  # Dark green
        'width_border': '0.6'     # Grosor del borde
    })
    selection_layer.renderer().setSymbol(symbol)
    selection_layer.triggerRepaint()
    
    selection_layer.setOpacity(0.9)

    # Zoom a la selección
    iface.mapCanvas().zoomToSelected(asolayer)
    iface.mapCanvas().refresh()
else:
    print("No se encontraron asociaciones con los códigos especificados")
    print("Nombres de campos disponibles:", [field.name() for field in asolayer.fields()])



#Forma
########################################

# PASO 1: Obtener la geometría de tu municipio
# Reemplaza 'nombre_de_tu_capa' con el nombre real de tu capa
capa_asociacion = QgsProject.instance().mapLayersByName('resguardos_seleccionados')[0]

# Obtener la primera feature (asumiendo que es tu municipio)
feature = next(capa_asociacion.getFeatures())
geometria = feature.geometry()

# PASO 2: SIMPLIFICAR la geometría (¡IMPORTANTE!)
geometria_simplificada = geometria.simplify(500)  # 500 metros de tolerancia
print(f"Vértices originales: {geometria.constGet().nCoordinates()}")
print(f"Vértices simplificados: {geometria_simplificada.constGet().nCoordinates()}")

# PASO 3: Crear el objeto QgsLegendPatchShape
patch_shape = QgsLegendPatchShape(
    Qgis.SymbolType.Fill,  # Es un polígono (relleno)
    geometria_simplificada,
    True  # Preservar aspecto
)

# PASO 4: Asignar la forma a la leyenda
root = QgsProject.instance().layerTreeRoot()
layer_node = root.findLayer(capa_asociacion.id())

if layer_node:
    # Asignar la forma al nodo de la capa
    layer_node.setPatchShape(patch_shape)
    print("✅ Forma asignada al nodo de la capa")
    
    # ACTUALIZACIÓN CORREGIDA: Forzar actualización de la leyenda
    iface.layerTreeView().refreshLayerSymbology(capa_asociacion.id())
    print("✅ Leyenda actualizada")
    
    # Verificar que se guardó
    if layer_node.patchShape() and not layer_node.patchShape().isNull():
        print("✅ Forma verificada y guardada")
    else:
        print("❌ La forma no se guardó correctamente")
else:
    print("❌ No se encontró el nodo de la capa")

# Obtener el primer feature de la capa de selección
first_feature = next(capa_asociacion.getFeatures())
geometry = first_feature.geometry()
wkt_string = geometry.asWkt()
#print(wkt_string)  # WKT de solo UN municipio
for feature in capa_asociacion.getFeatures():
    geometry = feature.geometry()
    wkt_string = geometry.asWkt()  # Convertir geometría a WKT
    #print(wkt_string)

# Guardar todas las geometrías WKT en un archivo de texto
with open('/Volumes/Disco A/Javier/mis_asociaciones.txt', 'w') as f:
    for i, feature in enumerate(capa_asociacion.getFeatures()):
        wkt = feature.geometry().asWkt()
        f.write(f"Asociacion {i+1}:\n{wkt}\n\n")
        print(f"✓ Guardado Asociacion {i+1}")
print("✅ Archivo guardado")




#Cabildos
########################################

# Cargar la capa
cablayer = QgsVectorLayer(cabildos_path, 'cabildos', "ogr")

# APLICAR ESTILO PARA PUNTOS - ¡CAMBIO A QgsMarkerSymbol!
symbolcab = QgsMarkerSymbol.createSimple({
    'name': 'circle',                    # Forma: circle, square, triangle, star, etc.
    'color': '10, 186, 181',        # Color (R,G,B,Alpha) - 255 opaco
    'color_border': '0, 109, 176',        # Color del borde
    'size': '1',                           # TAMAÑO del punto en mm
    'size_unit': 'MM',                     # Unidad: MM, Pixel, MapUnit
    'outline_width': '0.8',                 # Grosor del borde
    'outline_style': 'solid'                # Estilo del borde
    })

cablayer.renderer().setSymbol(symbolcab)
cablayer.triggerRepaint()
cablayer.setOpacity(0.9)

# 3. Configurar parámetros para el clip
params_cabildos = {
        'INPUT': cablayer,    # Capa a cortar (ecosistemas)
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte (consejos)
        'OUTPUT': 'memory:cabildos'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_cabildos = processing.run("native:clip", params_cabildos)
clipped_cabildos = result_cabildos['OUTPUT']

# Aplicar el mismo estilo a la capa recortada
clipped_cabildos.renderer().setSymbol(symbolcab)
clipped_cabildos.triggerRepaint()
clipped_cabildos.setName("cabildos")

QgsProject.instance().addMapLayer(clipped_cabildos)

#asociacion seleccionada
###############################################################

# Cargar la capa
cablayer = QgsVectorLayer(cabildos_path, 'cabildos', "ogr")

# Construir expresión de selección
expression = "OBJECTID IN ({})".format(','.join(["'{}'".format(c) for c in ccomunidad1]))


cablayer.selectByExpression(expression)

# 3. Verificar selección y crear nueva capa
if cablayer.selectedFeatureCount() > 0:
    # Crear capa temporal
    selection_layer = QgsVectorLayer(
        "Point?crs={}".format(cablayer.crs().authid()),
        "cabildo_seleccionado",
        "memory"
    )

    # Copiar estructura de campos
    provider = selection_layer.dataProvider()
    provider.addAttributes(cablayer.fields())
    selection_layer.updateFields()
    
    # Copiar features seleccionadas
    features = cablayer.selectedFeatures()
    provider.addFeatures(features)
    selection_layer.updateExtents()
    selection_layer.setOpacity(0.9)
    
    # Añadir al proyecto
    QgsProject.instance().addMapLayer(selection_layer)
    print(f"¡Se seleccionaron {len(features)} cabildo(s)!")

    # APLICAR ESTILO PARA PUNTOS - ¡CAMBIO A QgsMarkerSymbol!
    symbol = QgsMarkerSymbol.createSimple({
        'name': 'circle',                    # Forma: circle, square, triangle, star, etc.
        'color': '229,43,80',        # Color (R,G,B,Alpha) - 255 opaco
        'color_border': '96, 47, 107',        # Color del borde
        'size': '3',                           # TAMAÑO del punto en mm
        'size_unit': 'MM',                     # Unidad: MM, Pixel, MapUnit
        'outline_width': '0.8',                 # Grosor del borde
        'outline_style': 'solid'                # Estilo del borde
    })

    selection_layer.renderer().setSymbol(symbol)
    selection_layer.triggerRepaint()
    
    selection_layer.setOpacity(0.9)

    # Zoom a la selección
    iface.mapCanvas().zoomToSelected(cablayer)
    iface.mapCanvas().refresh()
else:
    print("No se encontraron asociaciones con los códigos especificados")
    print("Nombres de campos disponibles:", [field.name() for field in cablayer.fields()])


#Corporaciones
################

# Cargar la capa
autoridadeslayer = QgsVectorLayer(autoridades_path, 'autoridades', "ogr")


# 3. Configurar parámetros para el clip
params_autoridades = {
        'INPUT': autoridadeslayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:autoC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_autoridades = processing.run("native:clip", params_autoridades)
clipped_autoridades = result_autoridades['OUTPUT']
clipped_autoridades.setName("autoridades")
QgsProject.instance().addMapLayer(clipped_autoridades)

#Seco
################

# Cargar la capa
secolayer = QgsVectorLayer(seco_path, 'seco', "ogr")


# 3. Configurar parámetros para el clip
params_seco = {
        'INPUT': secolayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:secoC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_seco = processing.run("native:clip", params_seco)
clipped_seco = result_seco['OUTPUT']
clipped_seco.setName("seco")
QgsProject.instance().addMapLayer(clipped_seco)

symbols = QgsFillSymbol.createSimple({
        'color': '186, 135, 89, 60',  # '25, 100, 180' azul
        'color_border': '160, 120, 90',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
renderers = QgsSingleSymbolRenderer(symbols)
clipped_seco.setRenderer(renderers)

# Refrescar la capa para ver los cambios
clipped_seco.triggerRepaint()

#POMCAS
################

# Cargar la capa
pomcaslayer = QgsVectorLayer(pomcas_path, 'pomcas', "ogr")


# 3. Configurar parámetros para el clip
params_pomcas = {
        'INPUT': pomcaslayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:pomcasC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_pomcas = processing.run("native:clip", params_pomcas)
clipped_pomcas = result_pomcas['OUTPUT']
clipped_pomcas.setName("cuencas")
QgsProject.instance().addMapLayer(clipped_pomcas)

symbolpom = QgsFillSymbol.createSimple({
        'color': '0, 168, 107, 60',  # '25, 100, 180' azul
        'color_border': '0, 117, 94',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererpom = QgsSingleSymbolRenderer(symbolpom)
clipped_pomcas.setRenderer(rendererpom)

# Refrescar la capa para ver los cambios
clipped_pomcas.triggerRepaint()


#AmbitosPDET
################

# Cargar la capa
ambitoslayer = QgsVectorLayer(ambitos_path, 'ambitos', "ogr")


# 3. Configurar parámetros para el clip
params_ambitos = {
        'INPUT': ambitoslayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:ambitosC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_ambitos = processing.run("native:clip", params_ambitos)
clipped_ambitos = result_ambitos['OUTPUT']
clipped_ambitos.setName("ambitos")
QgsProject.instance().addMapLayer(clipped_ambitos)

# 1. Listar campos disponibles
print("📋 Campos disponibles:")
for field in clipped_ambitos.fields():
    print(f"   '{field.name()}'")
    
# 2. Verificar valores únicos en el campo de categoría
campo_buscado = 'categotia_'  # Ajusta este nombre si es necesario
valores_encontrados = set()


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_ambitos],
    campo = 'categoria_',  # Campo común en todas las capas
    colores_por_valor = colores_ambitos,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

#ZonificacionPDET
################

#asociacion_seleccionada

# Cargar la capa
zoniplayer = QgsVectorLayer(zonip_path, 'zonip', "ogr")


# 3. Configurar parámetros para el clip
params_zonip = {
        'INPUT': zoniplayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:zonipC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_zonip = processing.run("native:clip", params_zonip)
clipped_zonip = result_zonip['OUTPUT']
clipped_zonip.setName("zonip")
QgsProject.instance().addMapLayer(clipped_zonip)

# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_zonip],
    campo = 'categoria',  # Campo común en todas las capas
    colores_por_valor = colores_zonip,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)


#Reserva Magdalena
###########################

#iface.addVectorLayer

#Cargar capa
rforestalmag = QgsVectorLayer(rforestalmag_path, 'rforestalmag', 'ogr')

# 3. Configurar parámetros para el clip
params_rforestalmag = {
        'INPUT': rforestalmag,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:RFMagda'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_rforestalmag = processing.run("native:clip", params_rforestalmag)
clipped_rforestalmag = result_rforestalmag['OUTPUT']
clipped_rforestalmag.setName("RFMagda")
QgsProject.instance().addMapLayer(clipped_rforestalmag)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_rforestalmag],
    campo = 'Tipo_Zona_',  # Campo común en todas las capas
    colores_por_valor = colores_forestal,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

#Reserva Motilones
########################################

#iface.addVectorLayer
#QgsVectorLayer

#Cargar
rforestalmo = QgsVectorLayer(rforestalmo_path, 'rforestalmo', 'ogr')

# 3. Configurar parámetros para el clip
params_rforestalmo = {
        'INPUT': rforestalmo,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:RFMol'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_rforestalmo = processing.run("native:clip", params_rforestalmo)
clipped_rforestalmo = result_rforestalmo['OUTPUT']
clipped_rforestalmo.setName("RFMol")
QgsProject.instance().addMapLayer(clipped_rforestalmo)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_rforestalmo],
    campo = 'Tipo_Zona_',  # Campo común en todas las capas
    colores_por_valor = colores_forestal,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

#Reserva Central
############################

#Cargar 
rforestalc = QgsVectorLayer(rforestalc_path, 'rforestalc', 'ogr')


# 3. Configurar parámetros para el clip
params_rforestalc = {
        'INPUT': rforestalc,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:RFCentral'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_rforestalc = processing.run("native:clip", params_rforestalc)
clipped_rforestalc = result_rforestalc['OUTPUT']
clipped_rforestalc.setName("RFCentral")
QgsProject.instance().addMapLayer(clipped_rforestalc)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_rforestalc],
    campo = 'Tipo_Zona_',  # Campo común en todas las capas
    colores_por_valor = colores_forestal,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

#Reserva Amazonas2
###########################################

#Cargar
rforestalm2 = QgsVectorLayer(rforestalm2_path, 'rforestalm2', 'ogr')

# 3. Configurar parámetros para el clip
params_rforestalm2 = {
        'INPUT': rforestalm2,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:RFAmazona2'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_rforestalm2 = processing.run("native:clip", params_rforestalm2)
clipped_rforestalm2 = result_rforestalm2['OUTPUT']
clipped_rforestalm2.setName("RFAmazona2")
QgsProject.instance().addMapLayer(clipped_rforestalm2)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_rforestalm2],
    campo = 'ZONMADS',  # Campo común en todas las capas
    colores_por_valor = colores_forestal,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

#Reserva Amazonas1
###########################################

#Cargar capa
rforestalm1 = QgsVectorLayer(rforestalm1_path, 'rforestalm1', 'ogr')

# 3. Configurar parámetros para el clip
params_rforestalm1 = {
        'INPUT': rforestalm1,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:RFAmazona1'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_rforestalm1 = processing.run("native:clip", params_rforestalm1)
clipped_rforestalm1 = result_rforestalm1['OUTPUT']
clipped_rforestalm1.setName("RFAmazona1")
QgsProject.instance().addMapLayer(clipped_rforestalm1)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_rforestalm1],
    campo = 'Tipo_Zona_',  # Campo común en todas las capas
    colores_por_valor = colores_forestal,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

#Reserva Sierra
############################

#Cargar capa
rforestals = QgsVectorLayer(rforestals_path, 'rforestals', 'ogr')

# 3. Configurar parámetros para el clip
params_rforestals = {
        'INPUT': rforestals,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:RFSierra'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_rforestals = processing.run("native:clip", params_rforestals)
clipped_rforestals = result_rforestals['OUTPUT']
clipped_rforestals.setName("RFSierra")
QgsProject.instance().addMapLayer(clipped_rforestals)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_rforestals],
    campo = 'Tipo_zona',  # Campo común en todas las capas
    colores_por_valor = colores_forestal,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

#Reserva Pacifico
#######################################

# Cargar la capa
rforestalp = QgsVectorLayer(rforestalp_path, 'rforestalp', 'ogr')

# 3. Configurar parámetros para el clip
params_rforestalp = {
        'INPUT': rforestalp,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:RFPacifico'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_rforestalp = processing.run("native:clip", params_rforestalp)
clipped_rforestalp = result_rforestalp['OUTPUT']
clipped_rforestalp.setName("RFPacifico")
QgsProject.instance().addMapLayer(clipped_rforestalp)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_rforestalp],
    campo = 'Tipo_de_zo',  # Campo común en todas las capas
    colores_por_valor = colores_forestal,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

#POMCA Amoya
########################################

#Carga de capa
pomcamoya = QgsVectorLayer(pomcamoya_path, 'pomcamoya', 'ogr')

# 3. Configurar parámetros para el clip
params_pomcamoya = {
        'INPUT': pomcamoya,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:PAmoya'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_pomcamoya = processing.run("native:clip", params_pomcamoya)
clipped_pomcamoya = result_pomcamoya['OUTPUT']
clipped_pomcamoya.setName("PAmoya")
QgsProject.instance().addMapLayer(clipped_pomcamoya)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_pomcamoya],
    campo = 'SZO_US_M',  # Campo común en todas las capas
    colores_por_valor = colores_pomca,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

#POMCA Zapatosa
####################################

#Cargar capa
pomcazap = QgsVectorLayer(pomcazap_path, 'pomcazap', 'ogr')

# 3. Configurar parámetros para el clip
params_pomcazap = {
        'INPUT': pomcazap,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:Pazap'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_pomcazap = processing.run("native:clip", params_pomcazap)
clipped_pomcazap = result_pomcazap['OUTPUT']
clipped_pomcazap.setName("Pazap")
QgsProject.instance().addMapLayer(clipped_pomcazap)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_pomcazap],
    campo = 'SZO_US_M',  # Campo común en todas las capas
    colores_por_valor = colores_pomca,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)


#POMCA Mojana
####################################

#cargar capa
pomcamoj = QgsVectorLayer(pomcamoj_path, 'pomcamoj', 'ogr')


# 3. Configurar parámetros para el clip
params_pomcamoj = {
        'INPUT': pomcamoj,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:Pamoj'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_pomcamoj = processing.run("native:clip", params_pomcamoj)
clipped_pomcamoj = result_pomcamoj['OUTPUT']
clipped_pomcamoj.setName("Pamoj")
QgsProject.instance().addMapLayer(clipped_pomcamoj)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_pomcamoj],
    campo = 'SZO_US_M',  # Campo común en todas las capas
    colores_por_valor = colores_pomca,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)


#POMCA Guajira
####################################

#Cargar Capa
pomcag = QgsVectorLayer(pomcag_path, 'pomcag', 'ogr')

#Pomca
# 3. Configurar parámetros para el clip
params_pomcag = {
        'INPUT': pomcag,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:Pag'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_pomcag = processing.run("native:clip", params_pomcag)
clipped_pomcag = result_pomcag['OUTPUT']
clipped_pomcag.setName("Pag")
QgsProject.instance().addMapLayer(clipped_pomcag)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_pomcag],
    campo = 'SZO_US_M',  # Campo común en todas las capas
    colores_por_valor = colores_pomca,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)



#POMCA Bajo San Jorge
#####################################################

#iface.addVectorLayer
#QgsVectorLayer


#Cargar capa
pomcajorg = QgsVectorLayer(pomcajorg_path, 'pomcajorg', 'ogr')

#Pomca
# 3. Configurar parámetros para el clip
params_pomcajorg = {
        'INPUT': pomcajorg,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:Pajorg'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_pomcajorg = processing.run("native:clip", params_pomcajorg)
clipped_pomcajorg = result_pomcajorg['OUTPUT']
clipped_pomcajorg.setName("Pajorg")
QgsProject.instance().addMapLayer(clipped_pomcajorg)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_pomcajorg],
    campo = 'SZO_US_M',  # Campo común en todas las capas
    colores_por_valor = colores_pomca,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

#Coberturas y Ecosistemas
################

# Cargar la capa
coverlayer = QgsVectorLayer(coberturas_path, 'Coberturas', "ogr")



# 3. Configurar parámetros para el clip
params_coberturas = {
        'INPUT': coverlayer,    # Capa a cortar (ecosistemas)
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte (consejos)
        'OUTPUT': 'memory:cov2018'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_coberturas = processing.run("native:clip", params_coberturas)
clipped_coberturas = result_coberturas['OUTPUT']
clipped_coberturas.setName("Cobertura 2018")
QgsProject.instance().addMapLayer(clipped_coberturas)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_coberturas],
    campo = 'nivel_3',  # Campo común en todas las capas
    colores_por_valor = colores_cov,
    borde_color = '0,0,0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)


# Cargar la capa
ecolayer = QgsVectorLayer(ecosistemas_path, 'Ecosistemas', "ogr")

# 3. Configurar parámetros para el clip
params_ecosistemas = {
        'INPUT': ecolayer,    # Capa a cortar (ecosistemas)
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte (consejos)
        'OUTPUT': 'memory:eco2018'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_ecosistemas = processing.run("native:clip", params_ecosistemas)
clipped_ecosistemas = result_ecosistemas['OUTPUT']
clipped_ecosistemas.setName("Ecosis 2018")
QgsProject.instance().addMapLayer(clipped_ecosistemas)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_ecosistemas],
    campo = 'ECOS_GENER',  # Campo común en todas las capas
    colores_por_valor = colores_eco,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)


# Cargar la capa
coverlayer1 = QgsVectorLayer(coberturas_path1, 'Coberturas20', "ogr")

# 3. Configurar parámetros para el clip
params_coberturas1 = {
        'INPUT': coverlayer1,    # Capa a cortar (ecosistemas)
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte (consejos)
        'OUTPUT': 'memory:cov2020'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_coberturas1 = processing.run("native:clip", params_coberturas1)
clipped_coberturas2020 = result_coberturas1['OUTPUT']
clipped_coberturas2020.setName("Cobertura 2020")
QgsProject.instance().addMapLayer(clipped_coberturas2020)

# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_coberturas2020],
    campo = 'nivel_3',  # Campo común en todas las capas
    colores_por_valor = colores_cov1,
    borde_color = '0,0,0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

resultadocov = actualizar_etiquetas_capa(
    nombre_capa = 'Cobertura 2020',
    nombre_campo = 'nivel_3',
    mapeo_etiquetas = mapeo_cov
)

# Cargar la capa
ecolayer1 = QgsVectorLayer(ecosistemas_path1, 'Ecosistemas20', "ogr")


# 3. Configurar parámetros para el clip
params_ecosistemas1 = {
        'INPUT': ecolayer1,    # Capa a cortar (ecosistemas)
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte (consejos)
        'OUTPUT': 'memory:eco2024'   # Salida en memoria
    }


# Añadir resultado al proyecto
result_ecosistemas1 = processing.run("native:clip", params_ecosistemas1)
clipped_ecosistemas1 = result_ecosistemas1['OUTPUT']
clipped_ecosistemas1.setName("Ecosis 2024")
QgsProject.instance().addMapLayer(clipped_ecosistemas1)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_ecosistemas1],
    campo = 'ecos_gener',  # Campo común en todas las capas
    colores_por_valor = colores_eco1,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)


#Forestal
################

# Cargar la capa
forestalayer = QgsVectorLayer(forestal_path, 'forestal', "ogr")


# 3. Configurar parámetros para el clip
params_forestal = {
        'INPUT': forestalayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:forestalC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_forestal = processing.run("native:clip", params_forestal)
clipped_forestal = result_forestal['OUTPUT']
clipped_forestal.setName("forestal")
QgsProject.instance().addMapLayer(clipped_forestal)

symbolfore = QgsFillSymbol.createSimple({
        'color': '205, 133, 63',  # '25, 100, 180' azul
        'color_border': '210, 105, 30',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererfore = QgsSingleSymbolRenderer(symbolfore)
clipped_forestal.setRenderer(rendererfore)

# Refrescar la capa para ver los cambios
clipped_forestal.triggerRepaint()

#Humedales
################

# Cargar la capa
humedaleslayer = QgsVectorLayer(humedales_path, 'humedales', "ogr")


# 3. Configurar parámetros para el clip
params_humedales = {
        'INPUT': humedaleslayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:humedalesC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_humedales = processing.run("native:clip", params_humedales)
clipped_humedales = result_humedales['OUTPUT']
clipped_humedales.setName("humedales")
QgsProject.instance().addMapLayer(clipped_humedales)

symbolh = QgsFillSymbol.createSimple({
        'color': '188, 184, 138',  # '25, 100, 180' azul
        'color_border': '74, 93, 35',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererh = QgsSingleSymbolRenderer(symbolh)
clipped_humedales.setRenderer(rendererh)

# Refrescar la capa para ver los cambios
clipped_humedales.triggerRepaint()


#Paramos
################

# Cargar la capa
paramoslayer = QgsVectorLayer(paramos_path, 'paramos', "ogr")


# 3. Configurar parámetros para el clip
params_paramos = {
        'INPUT': paramoslayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:ParamosC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_paramos = processing.run("native:clip", params_paramos)
clipped_paramos = result_paramos['OUTPUT']
clipped_paramos.setName("paramos")
QgsProject.instance().addMapLayer(clipped_paramos)

symbolp = QgsFillSymbol.createSimple({
        'color': '200, 162, 200',  # '25, 100, 180' azul
        'color_border': '111, 45, 168',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererp = QgsSingleSymbolRenderer(symbolp)
clipped_paramos.setRenderer(rendererp)

# Refrescar la capa para ver los cambios
clipped_paramos.triggerRepaint()

#Pirorizados
################

# Cargar la capa
prioconlayer = QgsVectorLayer(priocon_path, 'priocon', "ogr")


# 3. Configurar parámetros para el clip
params_priocon = {
        'INPUT': prioconlayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:prioC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_priocon = processing.run("native:clip", params_priocon)
clipped_priocon = result_priocon['OUTPUT']
clipped_priocon.setName("Áreas Prioritarias de Conservación CONPES 3680")
QgsProject.instance().addMapLayer(clipped_priocon)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_priocon],
    campo = 'PRIORIDAD',  # Campo común en todas las capas
    colores_por_valor = colores_priocon,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

resultadopriocon = actualizar_etiquetas_capa(
    nombre_capa = 'Áreas Prioritarias de Conservación CONPES 3680',
    nombre_campo = 'PRIORIDAD',
    mapeo_etiquetas = mapeo_priocon
)

if resultadopriocon:
    print("\n✅ Proceso completado exitosamente")
else:
    print("\n❌ Hubo un error en el proceso")

print("\n" + "="*60)


#Parques
################

# Cargar la capa
parqueslayer = QgsVectorLayer(parques_path, 'parques', "ogr")


# 3. Configurar parámetros para el clip
params_parques = {
        'INPUT': parqueslayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:parquesC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_parques = processing.run("native:clip", params_parques)
clipped_parques = result_parques['OUTPUT']
clipped_parques.setName("parques")
QgsProject.instance().addMapLayer(clipped_parques)

symbolpar = QgsFillSymbol.createSimple({
        'color': '251, 236, 93',  # '25, 100, 180' azul
        'color_border': '232, 244, 140',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererpar = QgsSingleSymbolRenderer(symbolpar)
clipped_parques.setRenderer(rendererpar)

# Refrescar la capa para ver los cambios
clipped_parques.triggerRepaint()

#Zoniparques
################

# Cargar la capa
zoniparqueslayer = QgsVectorLayer(zoniparques_path, 'zoniparques', "ogr")


# 3. Configurar parámetros para el clip
params_zoniparques = {
        'INPUT': zoniparqueslayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:zoniparquesC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_zoniparques = processing.run("native:clip", params_zoniparques)
clipped_zoniparques = result_zoniparques['OUTPUT']
clipped_zoniparques.setName("zoniparques")
QgsProject.instance().addMapLayer(clipped_zoniparques)


# Aplicar el símbolo a la capa
# Refrescar la capa para ver los cambios
clipped_zoniparques.triggerRepaint()

# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_zoniparques],
    campo = 'nom_zopm',  # Campo común en todas las capas
    colores_por_valor = colores_parques,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

#Hipso
################

# Cargar la capa
hipsolayer = QgsVectorLayer(hipso_path, 'hipso', "ogr")


# 3. Configurar parámetros para el clip
params_hipso = {
        'INPUT': hipsolayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:hipsoC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_hipso = processing.run("native:clip", params_hipso)
clipped_hipso = result_hipso['OUTPUT']
clipped_hipso.setName("hipso")
QgsProject.instance().addMapLayer(clipped_hipso)


#Hidro
################

# Cargar la capa
hidrolayer = QgsVectorLayer(hidro_path, 'hidro', "ogr")


# 3. Configurar parámetros para el clip
params_hidro = {
        'INPUT': hidrolayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:hidroC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_hidro = processing.run("native:clip", params_hidro)
clipped_hidro = result_hidro['OUTPUT']
clipped_hidro.setName("hidro")
QgsProject.instance().addMapLayer(clipped_hidro)

symbol = QgsLineSymbol.createSimple({
    'color': '147, 204, 234',  # '25, 100, 180' azul
#   'color_border': '176, 208, 248',  # Color del borde
    'width': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
renderer = QgsSingleSymbolRenderer(symbol)
clipped_hidro.setRenderer(renderer)

# Refrescar la capa para ver los cambios
clipped_hidro.triggerRepaint()



#Cienagas
###########################


#Cargar capa
cienagas2 = QgsVectorLayer(cienaga2_path, 'cienagas', 'ogr')

# 3. Configurar parámetros para el clip
params_cienagas2 = {
        'INPUT': cienagas2,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:Cienagas'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_cienagas2 = processing.run("native:clip", params_cienagas2)
clipped_cienagas2 = result_cienagas2['OUTPUT']
clipped_cienagas2.setName("Cienagas")
QgsProject.instance().addMapLayer(clipped_cienagas2)

symbolciena2 = QgsFillSymbol.createSimple({
        'color': '0, 204, 153',  # '25, 100, 180' azul
        'color_border': '0, 153, 0',  # Color del borde
        'width_border': '0.2'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererciena2 = QgsSingleSymbolRenderer(symbolciena2)
clipped_cienagas2.setRenderer(rendererciena2)

# Refrescar la capa para ver los cambios
clipped_cienagas2.triggerRepaint()


#Rios1
###########################

from qgis.core import QgsProject, QgsSingleSymbolRenderer, QgsLineSymbol
from qgis.PyQt.QtGui import QColor

# Cargar capa

rios1 = QgsVectorLayer(rios1_path, 'rios1', 'ogr')

print(f"✅ Capa cargada: {rios1.name()}")
print(f"📌 Tipo de geometría: {rios1.geometryType()} (0 = Punto, 1 = Línea, 2 = Polígono)")

# Clip
params_rios1 = {
    'INPUT': rios1,
    'OVERLAY': 'resguardo_seleccionado',
    'OUTPUT': 'memory:rios1'
}

result_rios1 = processing.run("native:clip", params_rios1)
clipped_rios1 = result_rios1['OUTPUT']
clipped_rios1.setName("rios1")
QgsProject.instance().addMapLayer(clipped_rios1)

# ✅ CORRECCIÓN: Usar QgsLineSymbol en lugar de QgsFillSymbol
symbolrios = QgsLineSymbol.createSimple({
    'color': '0, 123, 167',        # Color de la línea (azul)
    'width': '1.7',                  # Ancho de la línea en mm
    'outline_width': '0.7',          # (opcional) alias para width
    'capstyle': 'round',             # Estilo de los extremos
    'joinstyle': 'round'             # Estilo de las uniones
})


# Aplicar el símbolo a la capa
clipped_rios1.setRenderer(QgsSingleSymbolRenderer(symbolrios))

# Refrescar
clipped_rios1.triggerRepaint()
iface.mapCanvas().refresh()

print("✅ Estilo de línea aplicado correctamente")
# Crear símbolo de relleno personalizado


#Lagunas
###########################

#iface.addVectorLayer

#Cargar capa
lagunas = QgsVectorLayer(lagunas_path, 'lagunas', 'ogr')

# 3. Configurar parámetros para el clip
params_lagunas = {
        'INPUT': lagunas,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:lagunas' # Salida en memoria
    }

# Añadir resultado al proyecto
result_lagunas = processing.run("native:clip", params_lagunas)
clipped_lagunas = result_lagunas['OUTPUT']
clipped_lagunas.setName("lagunas")
QgsProject.instance().addMapLayer(clipped_lagunas)


symbolla = QgsFillSymbol.createSimple({
        'color': '62, 180, 137',  # '25, 100, 180' azul
        'color_border': '0, 75, 73',  # Color del borde
        'width_border': '0.2'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererla = QgsSingleSymbolRenderer(symbolla)
clipped_lagunas.setRenderer(rendererla)

# Refrescar la capa para ver los cambios
clipped_lagunas.triggerRepaint()



#Pantanos
###########################

#iface.addVectorLayer

#Cargar capa
pantanos = QgsVectorLayer(pantanos_path, 'pantanos', 'ogr')

# 3. Configurar parámetros para el clip
params_pantanos = {
        'INPUT': pantanos,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:pantanos'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_pantanos = processing.run("native:clip", params_pantanos)
clipped_pantanos = result_pantanos['OUTPUT']
clipped_pantanos.setName("pantanos")
QgsProject.instance().addMapLayer(clipped_pantanos)

symbolpan = QgsFillSymbol.createSimple({
        'color': '227, 249, 136',  # '25, 100, 180' azul
        'color_border': '0, 51, 153',  # Color del borde
        'width_border': '0.2'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererpan = QgsSingleSymbolRenderer(symbolpan)
clipped_pantanos.setRenderer(rendererpan)

# Refrescar la capa para ver los cambios
clipped_pantanos.triggerRepaint()

#Vias
################

# Cargar la capa
viaslayer = QgsVectorLayer(vias_path, 'vias', "ogr")


# 3. Configurar parámetros para el clip
params_vias = {
        'INPUT': viaslayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:viasC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_vias = processing.run("native:clip", params_vias)
clipped_vias = result_vias['OUTPUT']
clipped_vias.setName("vias")
QgsProject.instance().addMapLayer(clipped_vias)

symbolv = QgsFillSymbol.createSimple({
        'color': '192, 192, 192',  # '25, 100, 180' azul
        'color_border': '128, 128, 128',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererv = QgsSingleSymbolRenderer(symbolv)
clipped_vias.setRenderer(rendererv)

# Refrescar la capa para ver los cambios
clipped_vias.triggerRepaint()

#Vias2
################

# Cargar la capa
viaslayer2 = QgsVectorLayer(vias2_path, 'vias2', "ogr")


# 3. Configurar parámetros para el clip
params_vias2 = {
        'INPUT': viaslayer2,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:vias2C'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_vias2 = processing.run("native:clip", params_vias2)
clipped_vias2 = result_vias2['OUTPUT']
clipped_vias2.setName("vias2")
QgsProject.instance().addMapLayer(clipped_vias2)

symbolv2 = QgsFillSymbol.createSimple({
        'color': '192, 192, 192',  # '25, 100, 180' azul
        'color_border': '128, 128, 128',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererv2 = QgsSingleSymbolRenderer(symbolv2)
clipped_vias2.setRenderer(rendererv2)

# Refrescar la capa para ver los cambios
clipped_vias2.triggerRepaint()


#Manzana
################

# Cargar la capa
manzanalayer = QgsVectorLayer(manzana_path, 'manzana', "ogr")


# 3. Configurar parámetros para el clip
params_manzana = {
        'INPUT': manzanalayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:manzanaC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_manzana = processing.run("native:clip", params_manzana)
clipped_manzana = result_manzana['OUTPUT']
clipped_manzana.setName("manzana")
QgsProject.instance().addMapLayer(clipped_manzana)

#Linea
################

# Cargar la capa
linealayer = QgsVectorLayer(linea_path, 'linea', "ogr")


# 3. Configurar parámetros para el clip
params_linea = {
        'INPUT': linealayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:lineaC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_linea = processing.run("native:clip", params_linea)
clipped_linea = result_linea['OUTPUT']
clipped_linea.setName("linea")
QgsProject.instance().addMapLayer(clipped_linea)

#Nomenclatura
################

# Cargar la capa
nomelayer = QgsVectorLayer(nomenclatura_path, 'nomenclatura', "ogr")


# 3. Configurar parámetros para el clip
params_nomenclatura = {
        'INPUT': nomelayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:nomeC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_nomenclatura = processing.run("native:clip", params_nomenclatura)
clipped_nomenclatura = result_nomenclatura['OUTPUT']
clipped_nomenclatura.setName("nomenclatura")
QgsProject.instance().addMapLayer(clipped_nomenclatura)

#OTRLI
################

# Cargar la capa
otrlilayer = QgsVectorLayer(otrli_path, 'otrli', "ogr")


# 3. Configurar parámetros para el clip
params_otrli = {
        'INPUT': otrlilayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:otrliC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_otrli = processing.run("native:clip", params_otrli)
clipped_otrli = result_otrli['OUTPUT']
clipped_otrli.setName("otrli")
QgsProject.instance().addMapLayer(clipped_otrli)



#Cultu
################

# Cargar la capa
cultulayer = QgsVectorLayer(cultu_path, 'cultu', "ogr")


# 3. Configurar parámetros para el clip
params_cultu = {
        'INPUT': cultulayer,    # Capa a cortar 
        'OVERLAY': 'resguardo_seleccionado',  # Capa de corte
        'OUTPUT': 'memory:cultuC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_cultu = processing.run("native:clip", params_cultu)
clipped_cultu = result_cultu['OUTPUT']
clipped_cultu.setName("cultu")
QgsProject.instance().addMapLayer(clipped_cultu)



# Cargar ecosistemas Marinos
############################################

#Cargar marinos

marinoslayer = iface.addVectorLayer(marinos_path, 'marinos', 'ogr')

symbolmarinos = QgsFillSymbol.createSimple({
        'color': '91, 146, 229, 70',  # '25, 100, 180' azul
        'color_border': '65, 102, 245',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
marinoslayer.renderer().setSymbol(symbolmarinos)

# Refrescar la visualización
marinoslayer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(marinoslayer.id())


corallayer = iface.addVectorLayer(coral_path, 'coral', 'ogr')

symbolcoral = QgsFillSymbol.createSimple({
        'color': '153, 186, 221',  # '25, 100, 180' azul
        'color_border': '124, 185, 232',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
corallayer.renderer().setSymbol(symbolcoral)

# Refrescar la visualización
corallayer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(corallayer.id())




rocosolayer = iface.addVectorLayer(rocoso_path, 'rocosoo', 'ogr')

symbolrocoso = QgsFillSymbol.createSimple({
        'color': '194, 178, 128, 70',  # '25, 100, 180' azul
        'color_border': '155, 118, 83',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rocosolayer.renderer().setSymbol(symbolrocoso)

# Refrescar la visualización
rocosolayer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(rocosolayer.id())


prioclayer = iface.addVectorLayer(prioc_path, 'Sitios Prioritarios Conservación Pacifico', 'ogr')

symbolprioc = QgsFillSymbol.createSimple({
        'color': '91, 146, 229, 70',  # '25, 100, 180' azul
        'color_border': '65, 102, 245',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
prioclayer.renderer().setSymbol(symbolprioc)

# Refrescar la visualización
prioclayer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(prioclayer.id())
    


prioplayer = iface.addVectorLayer(priop_path, 'Sitios Prioritarios Conservación Pacifico', 'ogr')

symbolpriop = QgsFillSymbol.createSimple({
        'color': '216, 228, 188, 70',  # '25, 100, 180' azul
        'color_border': '135, 169, 107',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
prioplayer.renderer().setSymbol(symbolpriop)

# Refrescar la visualización
prioplayer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(prioplayer.id())


campesinaslayer = iface.addVectorLayer(campesinas_path, 'campesinas', 'ogr')

symbolcampesinas = QgsFillSymbol.createSimple({
        'color': '91, 146, 229, 70',  # '25, 100, 180' azul
        'color_border': '65, 102, 245',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
campesinaslayer.renderer().setSymbol(symbolcampesinas)

# Refrescar la visualización
campesinaslayer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(campesinaslayer.id())

cienagalayer = iface.addVectorLayer(cienaga_path, 'cienaga', 'ogr')

symbolcienaga = QgsFillSymbol.createSimple({
        'color': '227, 171, 87, 70',  # '25, 100, 180' azul
        'color_border': '152, 118, 84',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
cienagalayer.renderer().setSymbol(symbolcienaga)

# Refrescar la visualización
cienagalayer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(cienagalayer.id())


cinturonlayer = iface.addVectorLayer(cinturon_path, 'cinturon', 'ogr')

symbolcinturon = QgsFillSymbol.createSimple({
        'color': '247, 231, 206, 70',  # '25, 100, 180' azul
        'color_border': '217, 144, 88',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
cinturonlayer.renderer().setSymbol(symbolcinturon)

# Refrescar la visualización
cinturonlayer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(cinturonlayer.id())

tuparrolayer = iface.addVectorLayer(tuparro_path, 'tuparro', 'ogr')

symboltuparro = QgsFillSymbol.createSimple({
        'color': '204, 119, 34, 70',  # '25, 100, 180' azul
        'color_border': '150, 90, 62',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
tuparrolayer.renderer().setSymbol(symboltuparro)

# Refrescar la visualización
tuparrolayer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(tuparrolayer.id())

sierralayer = iface.addVectorLayer(sierra_path, 'sierra', 'ogr')

symbolsierra = QgsFillSymbol.createSimple({
        'color': '68, 215, 168, 70',  # '25, 100, 180' azul
        'color_border': '58, 176, 158',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
sierralayer.renderer().setSymbol(symbolsierra)

# Refrescar la visualización
sierralayer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(sierralayer.id())

seaflowerlayer = iface.addVectorLayer(seaflower_path, 'seaflower', 'ogr')

symbolseaflower = QgsFillSymbol.createSimple({
        'color': '251, 236, 93, 70',  # '25, 100, 180' azul
        'color_border': '230, 226, 0',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
seaflowerlayer.renderer().setSymbol(symbolseaflower)

# Refrescar la visualización
seaflowerlayer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(seaflowerlayer.id())

nsmlayer = iface.addVectorLayer(nsm_path, 'nsm', 'ogr')

symbolnsm = QgsFillSymbol.createSimple({
        'color': '204, 204, 255, 70',  # '25, 100, 180' azul
        'color_border': '224, 176, 255',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
nsmlayer.renderer().setSymbol(symbolnsm)

# Refrescar la visualización
nsmlayer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(nsmlayer.id())




#Potencia de Restauracion en la zona
######################################

# Cargar capa de corte (municipios seleccionados)
capa_corte = QgsProject.instance().mapLayersByName('resguardo_seleccionado')

if not capa_corte:
    print("❌ No se encontró la capa 'municipios_seleccionados'")
    exit()
capa_corte = capa_corte[0]

print(f"✅ Capas cargadas correctamente")

if not capa_corte.hasSpatialIndex():
    print("   Creando índice para capa de corte...")
    processing.run("native:createspatialindex", {'INPUT': capa_corte})
    print("   ✅ Índice creado")
else:
    print("   ✅ Corte tiene índice")

# 3. OBTENER GEOMETRÍA DE CORTE
geometria_corte = next(capa_corte.getFeatures()).geometry()

#Recuperacion
#############################################

nombre_recu = 'Corregidos Recuperacion'
capa_recu = 'recuperacion'
salida_recu = 'Áreas Susceptibles A Recuperación'

# Cargar capa de recuperación
uri = f"{recu_path}|layername={nombre_recu}"
reclayer = QgsVectorLayer(uri, capa_recu, "ogr")

# Verificar y crear índices espaciales
print(f"\n📌 Índices espaciales:")
if not reclayer.hasSpatialIndex():
    print("   Creando índice para capa de recuperación...")
    processing.run("native:createspatialindex", {'INPUT': reclayer})
    print("   ✅ Índice creado")
else:
    print("   ✅ Capa tiene índice")

# 4. SELECCIÓN POR BOUNDING BOX
print(f"\n📦 Seleccionando features por bounding box...")
t_bbox = time.time()

reclayer.selectByRect(geometria_corte.boundingBox())
features_bbox = reclayer.selectedFeatureCount()
print(f"   ✅ Features en bounding box: {features_bbox}")
print(f"   ⏱️  Tiempo: {time.time()-t_bbox:.1f}s")

# 5. EXTRAER SOLO LAS QUE REALMENTE INTERSECTAN
print(f"\n🔍 Refinando con intersección real...")
t_interseccion = time.time()

# Guardamos los IDs de las features seleccionadas
selected_ids = [f.id() for f in reclayer.getSelectedFeatures()]

# Inicializar variables
skip_recu = False
reclayer1 = None
features_reales = 0

# Construir expresión con los IDs seleccionados
if selected_ids:
    ids_str = ','.join(str(id) for id in selected_ids)
    expression = f"$id IN ({ids_str}) AND intersects($geometry, geom_from_wkt('{geometria_corte.asWkt()}'))"
    
    params_extract = {
        'INPUT': reclayer,
        'EXPRESSION': expression,
        'OUTPUT': 'memory:recuperacion_preseleccion'
    }
    
    try:
        reclayer1 = processing.run("qgis:extractbyexpression", params_extract)['OUTPUT']
        features_reales = reclayer1.featureCount()
        
        print(f"   ✅ Features que realmente intersectan: {features_reales}")
        print(f"   📊 Descartadas por bounding box: {features_bbox - features_reales}")
    except Exception as e:
        print(f"   ⚠️ Error en extracción: {e}")
        features_reales = 0
        reclayer1 = None
else:
    print("   ⚠️ No hay features seleccionadas por bounding box")
    features_reales = 0
    reclayer1 = None

print(f"   ⏱️  Tiempo: {time.time()-t_interseccion:.1f}s")

# Limpiar selección
reclayer.removeSelection()

# 6. VERIFICAR QUE HAY FEATURES PARA PROCESAR
if not reclayer1 or features_reales == 0:
    print("\n⚠️ ADVERTENCIA: No hay features para procesar en RECUPERACIÓN.")
    print("   El área de corte no intersecta la capa de recuperación.")
    print("   Se creará una capa vacía para mantener el flujo del script.")
    
    # Crear una capa vacía para evitar errores posteriores
    resultado_recu = QgsVectorLayer("Polygon?crs=" + reclayer.crs().authid(), 
                                     salida_recu + "_sin_datos", "memory")
    QgsProject.instance().addMapLayer(resultado_recu)
    
    # Aplicar estilo a la capa vacía
    symbolrecu = QgsFillSymbol.createSimple({
        'color': '134, 126, 54',
        'color_border': '112, 28, 28',
        'width_border': '0.3'
    })
    renderecu = QgsSingleSymbolRenderer(symbolrecu)
    resultado_recu.setRenderer(renderecu)
    
    print("\n" + "="*60)
    print("⚠️ PROCESO DE RECUPERACIÓN COMPLETADO SIN DATOS")
    print("="*60)
    
    # EN VEZ DE sys.exit(), ESTABLECEMOS BANDERA PARA SALTAR PROCESAMIENTO
    skip_recu = True
else:
    skip_recu = False

# 7. CREAR ÍNDICE ESPACIAL (solo si hay features)
if not skip_recu:
    print(f"\n📌 Creando índice espacial...")
    t_indice = time.time()
    processing.run("native:createspatialindex", {'INPUT': reclayer1})
    print(f"   ✅ Índice creado en {time.time()-t_indice:.1f}s")

# 8. CLIP VECTORIAL (solo si hay features)
if not skip_recu:
    print(f"\n✂️ Ejecutando clip vectorial...")
    t_clip = time.time()

    params_clip = {
        'INPUT': reclayer1,
        'OVERLAY': capa_corte,
        'OUTPUT': f'memory:{salida_recu}'
    }

    try:
        resultado_recu = processing.run("native:clip", params_clip)['OUTPUT']
        print(f"   ✅ Features resultantes: {resultado_recu.featureCount()}")
        print(f"   ⏱️  Tiempo: {time.time()-t_clip:.1f}s")
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(resultado_recu)
        print(f"   ✅ Capa '{salida_recu}' añadida al proyecto")
        
    except Exception as e:
        print(f"   ❌ Error en clip: {e}")
        print("   Intentando con algoritmo alternativo...")
        
        params_clip_alt = {
            'INPUT': reclayer1,
            'POLYGONS': capa_corte,
            'OUTPUT': f'memory:{salida_recu}'
        }
        try:
            resultado_recu = processing.run("native:clipvectorbypolygon", params_clip_alt)['OUTPUT']
            QgsProject.instance().addMapLayer(resultado_recu)
        except Exception as e2:
            print(f"   ❌ También falló el alternativo: {e2}")
            # Crear capa vacía como fallback
            resultado_recu = QgsVectorLayer("Polygon?crs=" + reclayer.crs().authid(), 
                                             salida_recu + "_error", "memory")
            QgsProject.instance().addMapLayer(resultado_recu)
else:
    print("\n⏩ Procesamiento de RECUPERACIÓN omitido por falta de features.")
    # Asegurar que resultado_recu existe para los pasos siguientes
    if 'resultado_recu' not in locals():
        resultado_recu = QgsVectorLayer("Polygon?crs=" + reclayer.crs().authid(), 
                                         salida_recu + "_sin_datos", "memory")
        QgsProject.instance().addMapLayer(resultado_recu)

# 9. APLICAR ESTILO (siempre se ejecuta)
print(f"\n🎨 Aplicando estilo a RECUPERACIÓN...")
t_estilo = time.time()

symbolrecu = QgsFillSymbol.createSimple({
    'color': '134, 126, 54',
    'color_border': '112, 28, 28',
    'width_border': '0.3'
})

renderecu = QgsSingleSymbolRenderer(symbolrecu)
resultado_recu.setRenderer(renderecu)
resultado_recu.triggerRepaint()
resultado_recu.updateExtents()

print(f"   ✅ Estilo aplicado en {time.time()-t_estilo:.1f}s")

#Rehabilitacion
#############################################

nombre_reha = 'Corregidos Rehabilitacion'
capa_reha = 'rehabilitacion'
salida_reha = 'Áreas Susceptibles A Rehabilitación'

# Cargar capa de recuperación
uri = f"{reha_path}|layername={nombre_reha}"
rehlayer = QgsVectorLayer(uri, capa_reha, "ogr")

# Verificar y crear índices espaciales
print(f"\n📌 Índices espaciales:")
if not rehlayer.hasSpatialIndex():
    print("   Creando índice para capa de recuperación...")
    processing.run("native:createspatialindex", {'INPUT': rehlayer})
    print("   ✅ Índice creado")
else:
    print("   ✅ Capa tiene índice")

# 4. SELECCIÓN POR BOUNDING BOX
print(f"\n📦 Seleccionando features por bounding box...")
t_bbox = time.time()

rehlayer.selectByRect(geometria_corte.boundingBox())
features_bbox = rehlayer.selectedFeatureCount()
print(f"   ✅ Features en bounding box: {features_bbox}")
print(f"   ⏱️  Tiempo: {time.time()-t_bbox:.1f}s")

# 5. EXTRAER SOLO LAS QUE REALMENTE INTERSECTAN
print(f"\n🔍 Refinando con intersección real...")
t_interseccion = time.time()

# Guardamos los IDs de las features seleccionadas
selected_ids = [f.id() for f in rehlayer.getSelectedFeatures()]

# Inicializar variables
skip_reha = False
rehlayer1 = None
features_reales = 0

# Construir expresión con los IDs seleccionados
if selected_ids:
    ids_str = ','.join(str(id) for id in selected_ids)
    expression = f"$id IN ({ids_str}) AND intersects($geometry, geom_from_wkt('{geometria_corte.asWkt()}'))"
    
    params_extract = {
        'INPUT': rehlayer,
        'EXPRESSION': expression,
        'OUTPUT': 'memory:rehabilitacion_preseleccion'
    }
    
    try:
        rehlayer1 = processing.run("qgis:extractbyexpression", params_extract)['OUTPUT']
        features_reales = rehlayer1.featureCount()
        
        print(f"   ✅ Features que realmente intersectan: {features_reales}")
        print(f"   📊 Descartadas por bounding box: {features_bbox - features_reales}")
    except Exception as e:
        print(f"   ⚠️ Error en extracción: {e}")
        features_reales = 0
        rehlayer1 = None
else:
    print("   ⚠️ No hay features seleccionadas por bounding box")
    features_reales = 0
    rehlayer1 = None

print(f"   ⏱️  Tiempo: {time.time()-t_interseccion:.1f}s")

# Limpiar selección
rehlayer.removeSelection()

# 6. VERIFICAR QUE HAY FEATURES PARA PROCESAR
if not rehlayer1 or features_reales == 0:
    print("\n⚠️ ADVERTENCIA: No hay features para procesar en REHABILITACIÓN.")
    print("   El área de corte no intersecta la capa de recuperación.")
    print("   Se creará una capa vacía para mantener el flujo del script.")
    
    # Crear una capa vacía para evitar errores posteriores
    resultado_reha = QgsVectorLayer("Polygon?crs=" + rehlayer.crs().authid(), 
                                     salida_reha + "_sin_datos", "memory")
    QgsProject.instance().addMapLayer(resultado_reha)
    
    # Aplicar estilo a la capa vacía
    symbolreha = QgsFillSymbol.createSimple({
        'color': '157, 194, 9',
        'color_border': '139, 190, 27',
        'width_border': '0.3'
    })
    rendereha = QgsSingleSymbolRenderer(symbolreha)
    resultado_reha.setRenderer(rendereha)
    
    print("\n" + "="*60)
    print("⚠️ PROCESO DE REHABILITACIÓN COMPLETADO SIN DATOS")
    print("="*60)
    
    # EN VEZ DE sys.exit(), ESTABLECEMOS BANDERA PARA SALTAR PROCESAMIENTO
    skip_reha = True
else:
    skip_reha = False

# 7. CREAR ÍNDICE ESPACIAL (solo si hay features)
if not skip_reha:
    print(f"\n📌 Creando índice espacial...")
    t_indice = time.time()
    processing.run("native:createspatialindex", {'INPUT': rehlayer1})
    print(f"   ✅ Índice creado en {time.time()-t_indice:.1f}s")

# 8. CLIP VECTORIAL (solo si hay features)
if not skip_reha:
    print(f"\n✂️ Ejecutando clip vectorial...")
    t_clip = time.time()

    params_clip = {
        'INPUT': rehlayer1,
        'OVERLAY': capa_corte,
        'OUTPUT': f'memory:{salida_reha}'
    }

    try:
        resultado_reha = processing.run("native:clip", params_clip)['OUTPUT']
        print(f"   ✅ Features resultantes: {resultado_reha.featureCount()}")
        print(f"   ⏱️  Tiempo: {time.time()-t_clip:.1f}s")
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(resultado_reha)
        print(f"   ✅ Capa '{salida_reha}' añadida al proyecto")
        
    except Exception as e:
        print(f"   ❌ Error en clip: {e}")
        print("   Intentando con algoritmo alternativo...")
        
        params_clip_alt = {
            'INPUT': rehlayer1,
            'POLYGONS': capa_corte,
            'OUTPUT': f'memory:{salida_reha}'
        }
        try:
            resultado_reha = processing.run("native:clipvectorbypolygon", params_clip_alt)['OUTPUT']
            QgsProject.instance().addMapLayer(resultado_reha)
        except Exception as e2:
            print(f"   ❌ También falló el alternativo: {e2}")
            # Crear capa vacía como fallback
            resultado_reha = QgsVectorLayer("Polygon?crs=" + rehlayer.crs().authid(), 
                                             salida_reha + "_error", "memory")
            QgsProject.instance().addMapLayer(resultado_reha)
else:
    print("\n⏩ Procesamiento de REHABILITACIÓN omitido por falta de features.")
    # Asegurar que resultado_reha existe para los pasos siguientes
    if 'resultado_reha' not in locals():
        resultado_reha = QgsVectorLayer("Polygon?crs=" + rehlayer.crs().authid(), 
                                         salida_reha + "_sin_datos", "memory")
        QgsProject.instance().addMapLayer(resultado_reha)

# 9. APLICAR ESTILO (siempre se ejecuta)
print(f"\n🎨 Aplicando estilo a REHABILITACIÓN...")
t_estilo = time.time()

symbolreha = QgsFillSymbol.createSimple({
    'color': '157, 194, 9',
    'color_border': '33, 66, 30',
    'width_border': '0.3'
})

rendereha = QgsSingleSymbolRenderer(symbolreha)
resultado_reha.setRenderer(rendereha)
resultado_reha.triggerRepaint()
resultado_reha.updateExtents()

print(f"   ✅ Estilo aplicado en {time.time()-t_estilo:.1f}s")

# CONTINÚA CON RESTAURACIÓN (tu código existente)
...

#Restauracion
############################################

nombre_resta = 'Corregidos Restauracion2'
capa_reta = 'restauracion'
salida_resta = 'Áreas Susceptibles A Restauración'

# Cargar capa de restauración
uri = f"{res_path}|layername={nombre_resta}"
reslayer = QgsVectorLayer(uri, capa_reta, "ogr")
#reslayer1 = iface.addVectorLayer(uri, capa_reta, "ogr")

# Verificar y crear índices espaciales
print(f"\n📌 Índices espaciales:")
if not reslayer.hasSpatialIndex():
    print("   Creando índice para capa de restauración...")
    processing.run("native:createspatialindex", {'INPUT': reslayer})
    print("   ✅ Índice creado")
else:
    print("   ✅ Capa tiene índice")

# 4. SELECCIÓN POR BOUNDING BOX

print(f"\n📦 Seleccionando features por bounding box...")
t_bbox = time.time()

reslayer.selectByRect(geometria_corte.boundingBox())
features_bbox = reslayer.selectedFeatureCount()
print(f"   ✅ Features en bounding box: {features_bbox}")
print(f"   ⏱️  Tiempo: {time.time()-t_bbox:.1f}s")

# 5. EXTRAER SOLO LAS QUE REALMENTE INTERSECTAN

print(f"\n🔍 Refinando con intersección real...")
t_interseccion = time.time()

# Guardamos los IDs de las features seleccionadas
selected_ids = [f.id() for f in reslayer.getSelectedFeatures()]

# Inicializar variables
skip_processing = False
reslayer1 = None
features_reales = 0

# Construir expresión con los IDs seleccionados
if selected_ids:
    ids_str = ','.join(str(id) for id in selected_ids)
    expression = f"$id IN ({ids_str}) AND intersects($geometry, geom_from_wkt('{geometria_corte.asWkt()}'))"
    
    params_extract = {
        'INPUT': reslayer,
        'EXPRESSION': expression,
        'OUTPUT': 'memory:restauracion_preseleccion'
    }
    
    try:
        reslayer1 = processing.run("qgis:extractbyexpression", params_extract)['OUTPUT']
        features_reales = reslayer1.featureCount()
        
        print(f"   ✅ Features que realmente intersectan: {features_reales}")
        print(f"   📊 Descartadas por bounding box: {features_bbox - features_reales}")
    except Exception as e:
        print(f"   ⚠️ Error en extracción: {e}")
        features_reales = 0
        reslayer1 = None
else:
    print("   ⚠️ No hay features seleccionadas por bounding box")
    features_reales = 0
    reslayer1 = None

print(f"   ⏱️  Tiempo: {time.time()-t_interseccion:.1f}s")

# Limpiar selección
reslayer.removeSelection()

# 6. VERIFICAR QUE HAY FEATURES PARA PROCESAR

if not reslayer1 or features_reales == 0:
    print("\n⚠️ ADVERTENCIA: No hay features para procesar.")
    print("   Esto puede deberse a que el área de corte no intersecta la capa.")
    print("   El script continuará pero no generará capa de resultado.")
    
    # Crear una capa vacía para evitar errores posteriores
    from qgis.core import QgsVectorLayer
    resultado_resta = QgsVectorLayer("Polygon?crs=" + reslayer.crs().authid(), 
                                     salida_resta + "_vacia", "memory")
    QgsProject.instance().addMapLayer(resultado_resta)
    
    # Saltar los pasos que dependen de reslayer1
    skip_processing = True
else:
    skip_processing = False

# 7. CREAR ÍNDICE ESPACIAL (solo si hay features)

if not skip_processing:
    print(f"\n📌 Creando índice espacial...")
    t_indice = time.time()
    processing.run("native:createspatialindex", {'INPUT': reslayer1})
    print(f"   ✅ Índice creado en {time.time()-t_indice:.1f}s")
    
    # ============================================
    # 8. CLIP VECTORIAL (solo si hay features)
    # ============================================
    print(f"\n✂️ Ejecutando clip vectorial...")
    t_clip = time.time()
    
    params_clip = {
        'INPUT': reslayer1,
        'OVERLAY': capa_corte,
        'OUTPUT': f'memory:{salida_resta}'
    }
    
    try:
        resultado_resta = processing.run("native:clip", params_clip)['OUTPUT']
        print(f"   ✅ Features resultantes: {resultado_resta.featureCount()}")
        print(f"   ⏱️  Tiempo: {time.time()-t_clip:.1f}s")
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(resultado_resta)
        print(f"   ✅ Capa '{salida_resta}' añadida al proyecto")
        
    except Exception as e:
        print(f"   ❌ Error en clip: {e}")
        print("   Intentando con algoritmo alternativo...")
        
        params_clip_alt = {
            'INPUT': reslayer1,
            'POLYGONS': capa_corte,
            'OUTPUT': f'memory:{salida_resta}'
        }
        try:
            resultado_resta = processing.run("native:clipvectorbypolygon", params_clip_alt)['OUTPUT']
            QgsProject.instance().addMapLayer(resultado_resta)
        except Exception as e2:
            print(f"   ❌ También falló el alternativo: {e2}")
            # Crear capa vacía como fallback
            resultado_resta = QgsVectorLayer("Polygon?crs=" + reslayer.crs().authid(), 
                                             salida_resta + "_error", "memory")
            QgsProject.instance().addMapLayer(resultado_resta)
else:
    print("\n⏩ Procesamiento omitido por falta de features.")
    # Asegurar que resultado_resta existe para los pasos siguientes
    if 'resultado_resta' not in locals():
        from qgis.core import QgsVectorLayer
        resultado_resta = QgsVectorLayer("Polygon?crs=" + reslayer.crs().authid(), 
                                         salida_resta + "_sin_datos", "memory")
        QgsProject.instance().addMapLayer(resultado_resta)

# 9. APLICAR ESTILO (siempre se ejecuta)

print(f"\n🎨 Aplicando estilo...")
t_estilo = time.time()

symbolresta = QgsFillSymbol.createSimple({
    'color': '79, 121, 66',
    'color_border': '48, 96, 48',
    'width_border': '0.3'
})

renderesta = QgsSingleSymbolRenderer(symbolresta)
resultado_resta.setRenderer(renderesta)
resultado_resta.triggerRepaint()
resultado_resta.updateExtents()

print(f"   ✅ Estilo aplicado en {time.time()-t_estilo:.1f}s")



#Temas
####################################################################

project = QgsProject.instance()
theme_manager = project.mapThemeCollection()
root = project.layerTreeRoot()

###Pais

tema = 'Pais'
capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados']

# PASO 1: Guardar el estado actual de TODAS las capas
estado_original = {}
for layer in project.mapLayers().values():
    # Buscar el nodo en el árbol de capas
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        estado_original[layer.id()] = {
            'visible': layer_tree_node.isVisible(),
            'expanded': layer_tree_node.isExpanded() if hasattr(layer_tree_node, 'isExpanded') else True
        }

print(estado_original)

capas_procesadas = []
for layer in project.mapLayers().values():
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        # Verificar si esta capa está en nuestra lista
        if layer.name() in capas:
            # Mostrar esta capa
            layer_tree_node.setItemVisibilityChecked(True)
            if hasattr(layer_tree_node, 'setExpanded'):
                layer_tree_node.setExpanded(True)
            capas_procesadas.append(layer.name())
            print(f"   ✅ Mostrando: {layer.name()}")
        else:
            # Ocultar esta capa
            layer_tree_node.setItemVisibilityChecked(False)
            print(f"   🔘 Ocultando: {layer.name()}")


# PASO 3: Crear el tema desde el estado actual
theme_collection = project.mapThemeCollection()
#theme_collection.createThemeFromCurrentState(root, tema)

#Set themes for each group
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
QgsProject.instance().layerTreeRoot(),
iface.layerTreeView().layerTreeModel())

mapThemesCollection.insert(tema, mapThemeRecord)


###Departamento

tema = 'Departamento'
capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados']

# PASO 1: Guardar el estado actual de TODAS las capas
estado_original = {}
for layer in project.mapLayers().values():
    # Buscar el nodo en el árbol de capas
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        estado_original[layer.id()] = {
            'visible': layer_tree_node.isVisible(),
            'expanded': layer_tree_node.isExpanded() if hasattr(layer_tree_node, 'isExpanded') else True
        }

print(estado_original)

capas_procesadas = []
for layer in project.mapLayers().values():
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        # Verificar si esta capa está en nuestra lista
        if layer.name() in capas:
            # Mostrar esta capa
            layer_tree_node.setItemVisibilityChecked(True)
            if hasattr(layer_tree_node, 'setExpanded'):
                layer_tree_node.setExpanded(True)
            capas_procesadas.append(layer.name())
            print(f"   ✅ Mostrando: {layer.name()}")
        else:
            # Ocultar esta capa
            layer_tree_node.setItemVisibilityChecked(False)
            print(f"   🔘 Ocultando: {layer.name()}")


# PASO 3: Crear el tema desde el estado actual
theme_collection = project.mapThemeCollection()
#theme_collection.createThemeFromCurrentState(root, tema)

#Set themes for each group
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
QgsProject.instance().layerTreeRoot(),
iface.layerTreeView().layerTreeModel())

mapThemesCollection.insert(tema, mapThemeRecord)

##Municipios
tema = 'Municipio'
capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'municipios_seleccionados']

# PASO 1: Guardar el estado actual de TODAS las capas
estado_original = {}
for layer in project.mapLayers().values():
    # Buscar el nodo en el árbol de capas
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        estado_original[layer.id()] = {
            'visible': layer_tree_node.isVisible(),
            'expanded': layer_tree_node.isExpanded() if hasattr(layer_tree_node, 'isExpanded') else True
        }

print(estado_original)

capas_procesadas = []
for layer in project.mapLayers().values():
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        # Verificar si esta capa está en nuestra lista
        if layer.name() in capas:
            # Mostrar esta capa
            layer_tree_node.setItemVisibilityChecked(True)
            if hasattr(layer_tree_node, 'setExpanded'):
                layer_tree_node.setExpanded(True)
            capas_procesadas.append(layer.name())
            print(f"   ✅ Mostrando: {layer.name()}")
        else:
            # Ocultar esta capa
            layer_tree_node.setItemVisibilityChecked(False)
            print(f"   🔘 Ocultando: {layer.name()}")


# PASO 3: Crear el tema desde el estado actual
theme_collection = project.mapThemeCollection()
#theme_collection.createThemeFromCurrentState(root, tema)

#Set themes for each group
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
QgsProject.instance().layerTreeRoot(),
iface.layerTreeView().layerTreeModel())
mapThemesCollection.insert(tema, mapThemeRecord)

##Reservas
tema = 'Reservas'
capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'seco', 'parques', 'zoniparques', 'forestal', 'autoridades', 'paz', 'biosfera', 'zoniparques', 'parques']

# PASO 1: Guardar el estado actual de TODAS las capas
estado_original = {}
for layer in project.mapLayers().values():
    # Buscar el nodo en el árbol de capas
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        estado_original[layer.id()] = {
            'visible': layer_tree_node.isVisible(),
            'expanded': layer_tree_node.isExpanded() if hasattr(layer_tree_node, 'isExpanded') else True
        }

print(estado_original)

capas_procesadas = []
for layer in project.mapLayers().values():
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        # Verificar si esta capa está en nuestra lista
        if layer.name() in capas:
            # Mostrar esta capa
            layer_tree_node.setItemVisibilityChecked(True)
            if hasattr(layer_tree_node, 'setExpanded'):
                layer_tree_node.setExpanded(True)
            capas_procesadas.append(layer.name())
            print(f"   ✅ Mostrando: {layer.name()}")
        else:
            # Ocultar esta capa
            layer_tree_node.setItemVisibilityChecked(False)
            print(f"   🔘 Ocultando: {layer.name()}")


# PASO 3: Crear el tema desde el estado actual
theme_collection = project.mapThemeCollection()
#theme_collection.createThemeFromCurrentState(root, 'tema')

#Set themes for each group
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
QgsProject.instance().layerTreeRoot(),
iface.layerTreeView().layerTreeModel())

mapThemesCollection.insert(tema, mapThemeRecord)

##Ecosistemas
tema = 'Ecosistemas'
capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'Ecosis 2024']

# PASO 1: Guardar el estado actual de TODAS las capas
estado_original = {}
for layer in project.mapLayers().values():
    # Buscar el nodo en el árbol de capas
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        estado_original[layer.id()] = {
            'visible': layer_tree_node.isVisible(),
            'expanded': layer_tree_node.isExpanded() if hasattr(layer_tree_node, 'isExpanded') else True
        }

print(estado_original)

capas_procesadas = []
for layer in project.mapLayers().values():
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        # Verificar si esta capa está en nuestra lista
        if layer.name() in capas:
            # Mostrar esta capa
            layer_tree_node.setItemVisibilityChecked(True)
            if hasattr(layer_tree_node, 'setExpanded'):
                layer_tree_node.setExpanded(True)
            capas_procesadas.append(layer.name())
            print(f"   ✅ Mostrando: {layer.name()}")
        else:
            # Ocultar esta capa
            layer_tree_node.setItemVisibilityChecked(False)
            print(f"   🔘 Ocultando: {layer.name()}")


# PASO 3: Crear el tema desde el estado actual
theme_collection = project.mapThemeCollection()
#theme_collection.createThemeFromCurrentState(root, 'tema')

#Set themes for each group
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
QgsProject.instance().layerTreeRoot(),
iface.layerTreeView().layerTreeModel())

mapThemesCollection.insert(tema, mapThemeRecord)

##Coberturas
tema = 'Coberturas'
capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'Cobertura 2020']

# PASO 1: Guardar el estado actual de TODAS las capas
estado_original = {}
for layer in project.mapLayers().values():
    # Buscar el nodo en el árbol de capas
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        estado_original[layer.id()] = {
            'visible': layer_tree_node.isVisible(),
            'expanded': layer_tree_node.isExpanded() if hasattr(layer_tree_node, 'isExpanded') else True
        }

print(estado_original)

capas_procesadas = []
for layer in project.mapLayers().values():
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        # Verificar si esta capa está en nuestra lista
        if layer.name() in capas:
            # Mostrar esta capa
            layer_tree_node.setItemVisibilityChecked(True)
            if hasattr(layer_tree_node, 'setExpanded'):
                layer_tree_node.setExpanded(True)
            capas_procesadas.append(layer.name())
            print(f"   ✅ Mostrando: {layer.name()}")
        else:
            # Ocultar esta capa
            layer_tree_node.setItemVisibilityChecked(False)
            print(f"   🔘 Ocultando: {layer.name()}")


# PASO 3: Crear el tema desde el estado actual
theme_collection = project.mapThemeCollection()
#theme_collection.createThemeFromCurrentState(root, 'tema')

#Set themes for each group
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
QgsProject.instance().layerTreeRoot(),
iface.layerTreeView().layerTreeModel())

mapThemesCollection.insert(tema, mapThemeRecord)


tema = 'Ambitos'
capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'ambitos', 'municipios_seleccionados', 'autoridades']

# PASO 1: Guardar el estado actual de TODAS las capas
estado_original = {}
for layer in project.mapLayers().values():
    # Buscar el nodo en el árbol de capas
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        estado_original[layer.id()] = {
            'visible': layer_tree_node.isVisible(),
            'expanded': layer_tree_node.isExpanded() if hasattr(layer_tree_node, 'isExpanded') else True
        }

print(estado_original)

capas_procesadas = []
for layer in project.mapLayers().values():
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        # Verificar si esta capa está en nuestra lista
        if layer.name() in capas:
            # Mostrar esta capa
            layer_tree_node.setItemVisibilityChecked(True)
            if hasattr(layer_tree_node, 'setExpanded'):
                layer_tree_node.setExpanded(True)
            capas_procesadas.append(layer.name())
            print(f"   ✅ Mostrando: {layer.name()}")
        else:
            # Ocultar esta capa
            layer_tree_node.setItemVisibilityChecked(False)
            print(f"   🔘 Ocultando: {layer.name()}")


# PASO 3: Crear el tema desde el estado actual
theme_collection = project.mapThemeCollection()
#theme_collection.createThemeFromCurrentState(root, 'tema')

#Set themes for each group
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
QgsProject.instance().layerTreeRoot(),
iface.layerTreeView().layerTreeModel())

mapThemesCollection.insert(tema, mapThemeRecord)

###Zonificacion

tema = 'Zonificacion'
capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'zonip', 'municipios_seleccionados']

# PASO 1: Guardar el estado actual de TODAS las capas
estado_original = {}
for layer in project.mapLayers().values():
    # Buscar el nodo en el árbol de capas
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        estado_original[layer.id()] = {
            'visible': layer_tree_node.isVisible(),
            'expanded': layer_tree_node.isExpanded() if hasattr(layer_tree_node, 'isExpanded') else True
        }

print(estado_original)

capas_procesadas = []
for layer in project.mapLayers().values():
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        # Verificar si esta capa está en nuestra lista
        if layer.name() in capas:
            # Mostrar esta capa
            layer_tree_node.setItemVisibilityChecked(True)
            if hasattr(layer_tree_node, 'setExpanded'):
                layer_tree_node.setExpanded(True)
            capas_procesadas.append(layer.name())
            print(f"   ✅ Mostrando: {layer.name()}")
        else:
            # Ocultar esta capa
            layer_tree_node.setItemVisibilityChecked(False)
            print(f"   🔘 Ocultando: {layer.name()}")


# PASO 3: Crear el tema desde el estado actual
theme_collection = project.mapThemeCollection()
#theme_collection.createThemeFromCurrentState(root, 'tema')

#Set themes for each group
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
QgsProject.instance().layerTreeRoot(),
iface.layerTreeView().layerTreeModel())

mapThemesCollection.insert(tema, mapThemeRecord)


##Priorizados

tema = 'Priorizados'
capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'Áreas Prioritarias de Conservación CONPES 3680', 'Sitios Prioritarios Conservación Pacifico', 'Sitios Prioritarios Conservación Caribe', 'hidro', 'ramsar', 'cuencas', 'RFAmazona1', 'RFCentral', 'RFMagda', 'RFMol', 'RFPacifico', 'RFSierra', 'RFAmazona2', 'Áreas Susceptibles A Rehabilitación', 'Áreas Susceptibles A Restauración', 'Áreas Susceptibles A Recuperación', 'seco']

# PASO 1: Guardar el estado actual de TODAS las capas
estado_original = {}
for layer in project.mapLayers().values():
    # Buscar el nodo en el árbol de capas
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        estado_original[layer.id()] = {
            'visible': layer_tree_node.isVisible(),
            'expanded': layer_tree_node.isExpanded() if hasattr(layer_tree_node, 'isExpanded') else True
        }

print(estado_original)

capas_procesadas = []
for layer in project.mapLayers().values():
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        # Verificar si esta capa está en nuestra lista
        if layer.name() in capas:
            # Mostrar esta capa
            layer_tree_node.setItemVisibilityChecked(True)
            if hasattr(layer_tree_node, 'setExpanded'):
                layer_tree_node.setExpanded(True)
            capas_procesadas.append(layer.name())
            print(f"   ✅ Mostrando: {layer.name()}")
        else:
            # Ocultar esta capa
            layer_tree_node.setItemVisibilityChecked(False)
            print(f"   🔘 Ocultando: {layer.name()}")


# PASO 3: Crear el tema desde el estado actual
theme_collection = project.mapThemeCollection()
#theme_collection.createThemeFromCurrentState(root, 'tema')

#Set themes for each group
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
QgsProject.instance().layerTreeRoot(),
iface.layerTreeView().layerTreeModel())

mapThemesCollection.insert(tema, mapThemeRecord)


###Importancia

tema = 'Importancia'
capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'seco', 'humedales', 'manglares', 'cienaga', 'cinturon', 'tuparro', 'sierra', 'seaflower', 'nsm', 'coral', 'hidro', 'marinos', 'rocoso', 'ramsar', 'cuencas', 'rios1', 'humedales']

# PASO 1: Guardar el estado actual de TODAS las capas
estado_original = {}
for layer in project.mapLayers().values():
    # Buscar el nodo en el árbol de capas
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        estado_original[layer.id()] = {
            'visible': layer_tree_node.isVisible(),
            'expanded': layer_tree_node.isExpanded() if hasattr(layer_tree_node, 'isExpanded') else True
        }

print(estado_original)



capas_procesadas = []
for layer in project.mapLayers().values():
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        # Verificar si esta capa está en nuestra lista
        if layer.name() in capas:
            # Mostrar esta capa
            layer_tree_node.setItemVisibilityChecked(True)
            if hasattr(layer_tree_node, 'setExpanded'):
                layer_tree_node.setExpanded(True)
            capas_procesadas.append(layer.name())
            print(f"   ✅ Mostrando: {layer.name()}")
        else:
            # Ocultar esta capa
            layer_tree_node.setItemVisibilityChecked(False)
            print(f"   🔘 Ocultando: {layer.name()}")


# PASO 3: Crear el tema desde el estado actual
theme_collection = project.mapThemeCollection()
#theme_collection.createThemeFromCurrentState(root, 'tema')

#Set themes for each group
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
QgsProject.instance().layerTreeRoot(),
iface.layerTreeView().layerTreeModel())

mapThemesCollection.insert(tema, mapThemeRecord)

##Comunidades

tema = 'Comunidades'
capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'resguardos_seleccionados',  'consejos', 'consejos_seleccionados', 'campesinas', 'autoridades', 'cabildo_seleccionado', 'cabildos', 'asociacion_seleccionada', 'asociaciones seleccionados', 'resguardos_seleccionados']

# PASO 1: Guardar el estado actual de TODAS las capas
estado_original = {}
for layer in project.mapLayers().values():
    # Buscar el nodo en el árbol de capas
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        estado_original[layer.id()] = {
            'visible': layer_tree_node.isVisible(),
            'expanded': layer_tree_node.isExpanded() if hasattr(layer_tree_node, 'isExpanded') else True
        }

print(estado_original)

capas_procesadas = []
for layer in project.mapLayers().values():
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        # Verificar si esta capa está en nuestra lista
        if layer.name() in capas:
            # Mostrar esta capa
            layer_tree_node.setItemVisibilityChecked(True)
            if hasattr(layer_tree_node, 'setExpanded'):
                layer_tree_node.setExpanded(True)
            capas_procesadas.append(layer.name())
            print(f"   ✅ Mostrando: {layer.name()}")
        else:
            # Ocultar esta capa
            layer_tree_node.setItemVisibilityChecked(False)
            print(f"   🔘 Ocultando: {layer.name()}")


# PASO 3: Crear el tema desde el estado actual
theme_collection = project.mapThemeCollection()
#theme_collection.createThemeFromCurrentState(root, 'tema')

#Set themes for each group
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
QgsProject.instance().layerTreeRoot(),
iface.layerTreeView().layerTreeModel())

mapThemesCollection.insert(tema, mapThemeRecord)

###Urbano

tema = 'Urbano'
capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'municipios_seleccionados', 'nomenclatura', 'manzana', 'vias', 'vias2', 'linea', 'otrli', 'cultu']

# PASO 1: Guardar el estado actual de TODAS las capas
estado_original = {}
for layer in project.mapLayers().values():
    # Buscar el nodo en el árbol de capas
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        estado_original[layer.id()] = {
            'visible': layer_tree_node.isVisible(),
            'expanded': layer_tree_node.isExpanded() if hasattr(layer_tree_node, 'isExpanded') else True
        }

print(estado_original)

capas_procesadas = []
for layer in project.mapLayers().values():
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        # Verificar si esta capa está en nuestra lista
        if layer.name() in capas:
            # Mostrar esta capa
            layer_tree_node.setItemVisibilityChecked(True)
            if hasattr(layer_tree_node, 'setExpanded'):
                layer_tree_node.setExpanded(True)
            capas_procesadas.append(layer.name())
            print(f"   ✅ Mostrando: {layer.name()}")
        else:
            # Ocultar esta capa
            layer_tree_node.setItemVisibilityChecked(False)
            print(f"   🔘 Ocultando: {layer.name()}")


# PASO 3: Crear el tema desde el estado actual
theme_collection = project.mapThemeCollection()
#theme_collection.createThemeFromCurrentState(root, 'tema')

#Set themes for each group
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
QgsProject.instance().layerTreeRoot(),
iface.layerTreeView().layerTreeModel())

mapThemesCollection.insert(tema, mapThemeRecord)


##Pomcas
tema = 'Pomcas'
capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'cuencas', 'PAmoya', 'Pacgsm', 'Pag', 'Pamoj', 'Pajorg']

# PASO 1: Guardar el estado actual de TODAS las capas
estado_original = {}
for layer in project.mapLayers().values():
    # Buscar el nodo en el árbol de capas
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        estado_original[layer.id()] = {
            'visible': layer_tree_node.isVisible(),
            'expanded': layer_tree_node.isExpanded() if hasattr(layer_tree_node, 'isExpanded') else True
        }

print(estado_original)

capas_procesadas = []
for layer in project.mapLayers().values():
    layer_tree_node = root.findLayer(layer.id())
    if layer_tree_node:
        # Verificar si esta capa está en nuestra lista
        if layer.name() in capas:
            # Mostrar esta capa
            layer_tree_node.setItemVisibilityChecked(True)
            if hasattr(layer_tree_node, 'setExpanded'):
                layer_tree_node.setExpanded(True)
            capas_procesadas.append(layer.name())
            print(f"   ✅ Mostrando: {layer.name()}")
        else:
            # Ocultar esta capa
            layer_tree_node.setItemVisibilityChecked(False)
            print(f"   🔘 Ocultando: {layer.name()}")


# PASO 3: Crear el tema desde el estado actual
theme_collection = project.mapThemeCollection()
#theme_collection.createThemeFromCurrentState(root, 'tema')

#Set themes for each group
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemeRecord = QgsMapThemeCollection.createThemeFromCurrentState(
QgsProject.instance().layerTreeRoot(),
iface.layerTreeView().layerTreeModel())

mapThemesCollection.insert(tema, mapThemeRecord)



# Ejecutar
eliminar_capas_vacias()

 # 2. Cargar capa de veredas
#        vlayer = QgsVectorLayer(veredas_path, 'veredas', 'ogr')
        
#        if not vlayer.isValid():
#            print("¡Error al cargar las veredas!")
#        else:
#            # Crear índice espacial de los consejos seleccionados
#            index = QgsSpatialIndex(selection_layer.getFeatures())
#            
#            # Encontrar veredas que intersectan
#            features_seleccionados = []
#            for vereda in vlayer.getFeatures():
#                if index.intersects(vereda.geometry().boundingBox()):
#                    for consejo in selection_layer.getFeatures():
#                        if vereda.geometry().intersects(consejo.geometry()):
#                            features_seleccionados.append(vereda)
#                            break
#            
#            # Crear capa de resultados
#            if features_seleccionados:
#                result_layer = QgsVectorLayer(
#                    "Polygon?crs={}".format(vlayer.crs().authid()),
#                    "veredas_en_consejos",
#                    "memory"
#                )
                
#                provider = result_layer.dataProvider()
#                provider.addAttributes(vlayer.fields())
#                result_layer.updateFields()
#                provider.addFeatures(features_seleccionados)
#                
#                # Estilo para veredas
#                vereda_symbol = QgsFillSymbol.createSimple({
#                    'color': '70, 130, 180, 100',  # Azul acero transparente
#                    'outline_color': '0, 0, 139',
#                    'outline_width': '0.3'
#                })
#                result_layer.renderer().setSymbol(vereda_symbol)
#                
#                QgsProject.instance().addMapLayer(result_layer)
                
                # Zoom a la extensión combinada
#                extent = result_layer.extent()
#                extent.combineExtentWith(selection_layer.extent())
#                iface.mapCanvas().setExtent(extent)
#                iface.mapCanvas().refresh()
#                
#                print(f"✅ {len(features_seleccionados)} veredas intersectan con los consejos seleccionados")
#            else:
#                print("⚠️ No hay intersecciones entre veredas y consejos")
#
####################################################

#localidades_path = '/Volumes/Disco A/Compartido/Fami/Javier/Nico/localidades.csv'

## Crear la URI del CSV (ajusta estos parámetros)
#uri = (
#    f"file://{localidades_path}?encoding=UTF-8"
#    f"&delimiter=,"
#    f"&xField=Longitud"  # Columna con coordenadas X
#    f"&yField=Latitud"   # Columna con coordenadas Y
#    f"&crs=EPSG:4326"    # Sistema de referencia (WGS84 en este caso)
#)
#
## Crear la capa vectorial
#csv_layer = iface.addVectorLayer(uri, "Samples", "delimitedtext")

# 1. Cargar el archivo CSV como capa de puntos
#localidades_path = '/Volumes/Disco A/Compartido/Fami/Javier/Nico/localidades.csv'
#uri = (
#    f"file://{localidades_path}?encoding=UTF-8"
#    f"&delimiter=,"
#    f"&xField=Longitud"  # Asegúrate que estos nombres coincidan con tus columnas
#    f"&yField=Latitud"
#    f"&crs=EPSG:4326"
#)

#csv_layer = QgsVectorLayer(uri, "localidades", "delimitedtext")
#if not csv_layer.isValid():
#    print("Error al cargar el CSV!")
#else:
#    QgsProject.instance().addMapLayer(csv_layer, False)

# 2. Cargar la capa de veredas
#veredas_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Zonificacion Colombia/Veredas/CRVeredas_2020.shp'
#vlayer = QgsVectorLayer(veredas_path, 'veredas', 'ogr')
#if not vlayer.isValid():
#    print("Error al cargar las veredas!")
#else:
#    QgsProject.instance().addMapLayer(vlayer, False)

# Esperar un momento para que las capas se carguen
#import time
#time.sleep(2)

# 3. Verificar que las capas están cargadas
#vlayer = QgsProject.instance().mapLayersByName('veredas')[0]
#csv_layer = QgsProject.instance().mapLayersByName('localidades')[0]

# 4. Crear índice espacial para los puntos
#index = QgsSpatialIndex(csv_layer.getFeatures())

# 5. Seleccionar veredas que intersectan con puntos
#features_seleccionados = []
#for poligono in vlayer.getFeatures():
#    geom_poligono = poligono.geometry()
#    # Primero verificar por bounding box para eficiencia
#    ids_puntos = index.intersects(geom_poligono.boundingBox())
#    if ids_puntos:
#        # Luego verificar intersección exacta
#        for id_punto in ids_puntos:
#            punto = csv_layer.getFeature(id_punto)
#            if geom_poligono.intersects(punto.geometry()):
#                features_seleccionados.append(poligono)
#                break
#

# 6. Crear capa temporal con las veredas seleccionadas
#if features_seleccionados:
#    capa_temporal = QgsVectorLayer("Polygon?crs={}".format(vlayer.crs().authid()), 
#                                 "veredas_con_localidades", 
#                                 "memory")
#    
#    provider = capa_temporal.dataProvider()
#    provider.addAttributes(vlayer.fields())
#    capa_temporal.updateFields()
#    
#    provider.addFeatures(features_seleccionados)
#    
#    QgsProject.instance().addMapLayer(capa_temporal)
#    iface.mapCanvas().setExtent(capa_temporal.extent())
#    iface.mapCanvas().refresh()
    
#    print(f"Se creó capa temporal con {len(features_seleccionados)} veredas que contienen localidades")
#else:
#    print("No se encontraron veredas que intersecten con los puntos")


#Colores
##########################

#Amarillo
#d5b43c

#Verdes
#        # Aplicar estilo a la capa recién creada
#        symbol = QgsFillSymbol.createSimple({
#            'color': '107, 142, 35',  # Oliva
#            'color_border': '0, 100, 0',  # Dark green
#            'width_border': '0.5'     # Grosor del borde
#        })
#        selection_layer.renderer().setSymbol(symbol)

#    # Crear un símbolo simple
#    symbol = QgsFillSymbol.createSimple({
#        'color': '173, 216, 230',  # Azul claro
#        'color_border': '70, 130, 180',  # Azul acero
#        'width_border': '0.2'  # Grosor del borde en mm
#    })
#    
#    # Aplicar el símbolo a la capa
#    deplayer.renderer().setSymbol(symbol)

# Aplicar estilo a la capa recién creada
#        symbol = QgsFillSymbol.createSimple({
#            'color': '255, 165, 0',  # Dark ORange
#            'color_border': '205, 133, 63',  # Peru
#            'width_border': '0.5'     # Grosor del borde
#        })

#Areas
############################
area_total_capa('resguardo_seleccionado', convertir_a_hectareas = True)

# Para Ecosis 2024
areas_por_etiqueta(
    nombre_capa = 'Ecosis 2024',
    nombre_campo = 'ecos_gener'  # El campo que tiene las etiquetas
)

# Para Coberturas
areas_por_etiqueta(
    nombre_capa = 'Cobertura 2020',
    nombre_campo = 'nivel_3'  # El campo que tiene las etiquetas
)

# Para Reservas
areas_por_etiqueta(
    nombre_capa = 'RFAmazona2',
    nombre_campo = 'ZONMADS'  # El campo que tiene las etiquetas
)

# Para Cuencas
areas_por_etiqueta(
    nombre_capa = 'cuencas',
    nombre_campo = 'NOMSZH'  # El campo que tiene las etiquetas
)

