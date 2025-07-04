## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005

from CvPythonExtensions import *
import CvUtil
import Popup as PyPopup
import PyHelpers
import CvScreenEnums
import CvCameraControls
import cPickle
import math

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer
CyGameInstance = gc.getGame()

class CustomFunctions:

  def nameUnit(self,unit):
    names = ['Ham','Shem','Japheth','Magog','Madai','Gomer','Javan','Tubal','Meshech','Tiras','Ashkenaz','Riphath','Togarmah','Elishah','Tarshish','Kittim','Dodanim','Cush','Egypt','Put','Canaan','Seba','Havilah','Sabtah','Raamah','Sabteca','Sheba','Dedan','Nimrod','Babel','Erech','Accad','Calneh','Rehoboth-Ir','Calah','Ludim','Anamim','Lehabim','Naphtuhim','Pathrusim','Casluhim','Caphtorim','Sidon','Heth','Gerar','Admah','Zeboiim','Lasha','Eber','Asshur','Arpachshad','Lud','Aram','Uz','Hul','Gether','Mash','Shelah','Peleg','Joktan','Almodad','Sheleph','Hazarmaveth','Jerah','Hadoram','Uzal','Diklah','Obal','Abimael','Ophir','Jobab','Sephar','Mesha','Reu','Serug','Nahor','Terah','Abram','Haran','Lot']
    curName = self.getObjectInt(CyGameInstance,'curName')
    if curName < len(names):
      unit.setName( names[curName] )
      self.setObjectInt( CyGameInstance, 'curName', curName + 1 )
      
  def nearPeak(self,x,y,r):
    for iiX in range(x-r, x+r+1, 1):
      for iiY in range(y-r, y+r+1, 1):
        pPlot = CyMap().plot(iiX,iiY)
        if pPlot.isPeak():
          return True
    
    return False

  def tough(self,unit):
    
    if self.getObjectInt(unit,'tough') == 0:
      self.setObjectInt(unit,'tough',1)
      pPlayer = gc.getPlayer(unit.getOwner())
      iPlayer = unit.getOwner()

      if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_TOUGH1')) == False and unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WIMPY1')) == False:
        iTough = CyGame().getSorenRandNum(100, "Toughness")
        if iTough < 2:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_TOUGH5'), True)
        if iTough < 6:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_TOUGH4'), True)
        if iTough < 13:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_TOUGH3'), True)
        if iTough < 22:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_TOUGH2'), True)
        if iTough < 40:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_TOUGH1'), True)
        if iTough > 98:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WIMPY5'), True)
        if iTough > 94:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WIMPY4'), True)
        if iTough > 87:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WIMPY3'), True)
        if iTough > 78:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WIMPY2'), True)
        if iTough > 60:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WIMPY1'), True)

      if CyGame().getSorenRandNum(20, "RandomHero") == 1:
        if unit.baseCombatStr() > 1:
          self.unitAptitude(unit)
          sMsg = 'An unusally skilled ' + str( unit.getName() ) + ' has become apparent!'
          CyInterface().addMessage(unit.getOwner(),false,25,sMsg,'AS3D_SPELL_CHARM_PERSON',1,unit.getButton(),ColorTypes(8),unit.getX(),unit.getY(),True,True)

      if unit.baseCombatStr() > 1:
        iSpecialChance = 200
        
        if CyGame().getSorenRandNum(iSpecialChance, "RandomSinister") == 1:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SINISTER'), True)

        if CyGame().getSorenRandNum(iSpecialChance, "RandomHealer") == 2:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BASIC_HEALING'), True)

        if CyGame().getSorenRandNum(iSpecialChance, "RandomDexterous") == 3:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEXTEROUS'), True)

        if CyGame().getSorenRandNum(iSpecialChance, "RandomBlessed") == 4:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BLESSED'), True)

        if CyGame().getSorenRandNum(iSpecialChance, "RandomCourage") == 5:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COURAGE'), True)

        if CyGame().getSorenRandNum(iSpecialChance, "RandomHeavy") == 6:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HEAVY'), True)

        if CyGame().getSorenRandNum(iSpecialChance, "RandomLight") == 7:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LIGHT'), True)

        if CyGame().getSorenRandNum(iSpecialChance, "RandomLoyalty") == 8:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LOYALTY'), True)

        if CyGame().getSorenRandNum(iSpecialChance, "RandomPotency") == 9:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POTENCY'), True)

        if CyGame().getSorenRandNum(iSpecialChance, "RandomProphecyMark") == 10:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PROPHECY_MARK'), True)

        if CyGame().getSorenRandNum(iSpecialChance, "RandomSpiritGuide") == 11:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE'), True)

        if CyGame().getSorenRandNum(iSpecialChance, "RandomValor") == 12:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_VALOR'), True)

        if CyGame().getSorenRandNum(iSpecialChance, "RandomStigmata") == 13:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STIGMATA'), True)
            
      ## Dire beasts and dragons add a chance that new living units will start with the Cult of the Dragon promotion...
      if unit.isAlive():
        iDireChance = 0
        iDireChance += pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_WYRMLING')) * 3
        iDireChance += pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_YOUNG_DRAGON')) * 6
        iDireChance += pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_DRAGON')) * 9
        iDireChance += pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_ACHERON')) * 10
        iDireChance += pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_ABASHI')) * 10
        iDireChance += pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_EURABATRES')) * 10
        if CyGame().getSorenRandNum(100, "RandomDragonCult") < iDireChance:
          unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CULT_OF_THE_DRAGON'), True)
          sMsg = unit.getName() + ' is born fearing dragons and beasts...'
          CyInterface().addMessage(iPlayer,false,25,sMsg,'',1,'Art/Interface/Buttons/Units/Acheron.dds',ColorTypes(8),unit.getX(),unit.getY(),True,True)
          CyInterface().addCombatMessage(iPlayer,sMsg)

  def reqMageArmor(self,caster):
    pPlot = caster.plot()
    for i in range(pPlot.getNumUnits()):
      pUnit = pPlot.getUnit(i)
      if not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MAGE_ARMOR')):
        return True
    return False
    
  def spellMageArmor(self,caster,mode):
    if mode == 'caster':
      iNumArmored = caster.getLevel() / 3
      caster.changeDamage(10,0)
    else:
      iNumArmored = caster.getLevel() / 2 + self.retCombat(caster)
    if iNumArmored < 1:
      iNumArmored = 1
    pPlot = caster.plot()
    for i in range(pPlot.getNumUnits()):
      pUnit = pPlot.getUnit(i)
      if not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MAGE_ARMOR')):
        pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MAGE_ARMOR'),True)
        iNumArmored = iNumArmored - 1
        if ( iNumArmored < 1 ):
          return
  
  def reqJudge(self,caster):
    if caster.plot().isCity():
      pCity = caster.plot().getPlotCity()

      sInfo = cPickle.loads(pCity.getScriptData())

      if 'JUDGE' not in sInfo:
        sInfo['JUDGE'] = 0

      if sInfo['JUDGE'] > 0:
        return True

    return False
    
  def upgradeWeapons(self,pUnit,iPercent,tier):
    pCity = pUnit.plot().getPlotCity()
    pPlayer = gc.getPlayer(pUnit.getOwner())
    maxstock = pPlayer.getNumCities() * 200 + 500  ## * 100 + 200
    autostock = ( maxstock * iPercent ) / 100
    weaponcost = ( pUnit.baseCombatStr() + pUnit.baseCombatStrDefense() ) * 10
    if weaponcost < 50:
      weaponcost = 50
    if gc.getUnitInfo(pUnit.getUnitType()).getWeaponTier() > 2 and tier > 2 and self.getObjectInt(pPlayer,'t3') >= autostock:
      if not pPlayer.isHuman() or self.getObjectInt(pPlayer,'t3') >= weaponcost:
        # Trade in Iron Weapons
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS')):
          weaponcost -= 40
          self.changeObjectInt(pPlayer,'t2',weaponcost/2)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), False)
        # Trade in Bronze Weapons  
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS')):
          weaponcost -= 20
          self.changeObjectInt(pPlayer,'t1',weaponcost/2)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), False)
        # Upgrade to Mithril Weapons!
        self.changeObjectInt(pPlayer,'t3',weaponcost*-1)
        pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MITHRIL_WEAPONS'), True)
        CyInterface().addMessage(pUnit.getOwner(),False,25,pUnit.getName()+' upgrades to mithril weapons! ' + ' Remaining stock: ' + str( self.getObjectInt(pPlayer,'t3') ) + 'm,' + str( self.getObjectInt(pPlayer,'t2') ) + 'i,' + str( self.getObjectInt(pPlayer,'t1') ) + 'c','AS2D_REPAIR',1,pUnit.getButton(),ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)
        CyInterface().addCombatMessage(pUnit.getOwner(),pUnit.getName()+' upgrades to mithril weapons!' + ' Remaining stock: ' + str( self.getObjectInt(pPlayer,'t3') ) + 'm,' + str( self.getObjectInt(pPlayer,'t2') ) + 'i,' + str( self.getObjectInt(pPlayer,'t1') ) + 'c')
    elif gc.getUnitInfo(pUnit.getUnitType()).getWeaponTier() > 1 and tier > 1 and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS')) and self.getObjectInt(pPlayer,'t2') >= autostock:
      if not pPlayer.isHuman() or self.getObjectInt(pPlayer,'t2') >= weaponcost:
        # Trade in Bronze Weapons  
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS')):
          weaponcost -= 20
          self.changeObjectInt(pPlayer,'t1',weaponcost/2)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), False)
        # Upgrade to Iron Weapons!
        self.changeObjectInt(pPlayer,'t2',weaponcost*-1)
        pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), True)
        CyInterface().addMessage(pUnit.getOwner(),False,25,pUnit.getName()+' upgrades to iron weapons!' + ' Remaining stock: ' + str( self.getObjectInt(pPlayer,'t3') ) + 'm,' + str( self.getObjectInt(pPlayer,'t2') ) + 'i,' + str( self.getObjectInt(pPlayer,'t1') ) + 'c','AS2D_REPAIR',1,pUnit.getButton(),ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)
        CyInterface().addCombatMessage(pUnit.getOwner(),pUnit.getName()+' upgrades to iron weapons!' + ' Remaining stock: ' + str( self.getObjectInt(pPlayer,'t3') ) + 'm,' + str( self.getObjectInt(pPlayer,'t2') ) + 'i,' + str( self.getObjectInt(pPlayer,'t1') ) + 'c')
    elif gc.getUnitInfo(pUnit.getUnitType()).getWeaponTier() > 0 and tier > 0 and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS')) and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS')) and self.getObjectInt(pPlayer,'t1') >= autostock:
      if not pPlayer.isHuman() or self.getObjectInt(pPlayer,'t1') >= weaponcost:
        # Upgrade to Bronze Weapons!
        self.changeObjectInt(pPlayer,'t1',weaponcost*-1)
        pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), True)
        CyInterface().addMessage(pUnit.getOwner(),False,25,pUnit.getName()+' upgrades to bronze weapons!' + ' Remaining stock: ' + str( self.getObjectInt(pPlayer,'t3') ) + 'm,' + str( self.getObjectInt(pPlayer,'t2') ) + 'i,' + str( self.getObjectInt(pPlayer,'t1') ) + 'c','AS2D_REPAIR',1,pUnit.getButton(),ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)
        CyInterface().addCombatMessage(pUnit.getOwner(),pUnit.getName()+' upgrades to bronze weapons!' + ' Remaining stock: ' + str( self.getObjectInt(pPlayer,'t3') ) + 'm,' + str( self.getObjectInt(pPlayer,'t2') ) + 'i,' + str( self.getObjectInt(pPlayer,'t1') ) + 'c')
  
  def spellJudge(self,caster):
    pCity = caster.plot().getPlotCity()
    pPlayer = gc.getPlayer(caster.getOwner())
    cPlayer = gc.getPlayer(pCity.getOwner())

    sInfo = cPickle.loads(pCity.getScriptData())
    
    iDiv = ( self.iNoble(caster,1) + 1 + sInfo['JUDGE'] )
    if iDiv < 1:
      iDiv = 1
    iChance = ( ( self.iNoble(caster,1) + 1 ) * 100 ) / iDiv
    if CyGame().getSorenRandNum(self.iNoble(caster,1)+1, "Judge") >= CyGame().getSorenRandNum(sInfo['JUDGE']+1, "Problem"):
      ## Success!
      iGain = sInfo['JUDGE'] * 3 + 5
      if caster.getOwner() == pCity.getOwner():
        iGain = iGain * 2
      iXP = sInfo['JUDGE'] / 2 + 1
      caster.changeExperience( iXP , -1, False, False, False )
      CyInterface().addMessage(caster.getOwner(),False,25,'Success! ('+str(iChance)+'% chance) '+caster.getName() + ' resolved a ' + self.sDisputeLevel(sInfo['JUDGE']) + ' dispute in ' + pCity.getName() + '!  You gain '+str(iGain)+' gold pieces and '+str(iXP)+'xp!','AS2D_GOODY_GOLD',1,'Art/Interface/Buttons/Units/Commander.dds',ColorTypes(8),caster.getX(),caster.getY(),True,True)
      CyInterface().addCombatMessage(caster.getOwner(),caster.getName() + ' resolved a ' + self.sDisputeLevel(sInfo['JUDGE']) + ' dispute in ' + pCity.getName() + '!  You gain '+str(iGain)+' gold pieces and '+str(iXP)+'xp!' )
      pPlayer.setGold( pPlayer.getGold() + sInfo['JUDGE'] * 3 + 5 )
      cPlayer.setGold( cPlayer.getGold() + sInfo['JUDGE'] * 3 + 5 )
      sInfo['JUDGE'] = 0
      pCity.setScriptData(cPickle.dumps(sInfo))
    else:
      ## Failure, this turn...
      CyInterface().addMessage(caster.getOwner(),False,25,'Failure. ('+str(iChance)+'% chance) '+caster.getName() + ' failed to resolve a ' + self.sDisputeLevel(sInfo['JUDGE']) + ' dispute in ' + pCity.getName() + '!','AS2D_PILLAGE',1,'Art/Interface/Buttons/Units/Commander.dds',ColorTypes(8),caster.getX(),caster.getY(),True,True)
      CyInterface().addCombatMessage(caster.getOwner(),caster.getName() + ' failed to resolve a ' + self.sDisputeLevel(sInfo['JUDGE']) + ' dispute in ' + pCity.getName() + '!' )
  
  def young(self,pUnit,newUnit):
    newUnit.finishMoves()
    newUnit.setHasCasted(True)
    if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT1')):
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER1'),True)
    if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT2')):
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER2'),True)
    if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT3')):
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER3'),True)
    if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT4')):
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER4'),True)
    if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT5')):
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER5'),True)
      
    if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DIRE')):
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MOBILITY1'),True)
    if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BLITZ')):
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MOBILITY2'),True)
    if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ANCIENT')):
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT1'),True)
    if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_PERFECT_SIGHT')):
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SENTRY'),True)
    
    pUnit.changeExperience(1, -1, False, False, False)
    pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FATIGUED'), True)
    sMsg = str( pUnit.getName() ) + ' has young...'
    if len(pUnit.getNameNoDesc()) > 2:
      if pUnit.getName().find('Offspring') == -1:
        newUnit.setName('Offspring of ' + pUnit.getNameNoDesc())
      else: 
        newUnit.setName('Grand-' + pUnit.getNameNoDesc())
    CyInterface().addMessage(pUnit.getOwner(),False,25,sMsg,'AS3D_SPELL_CHARM_PERSON',1,pUnit.getButton(),ColorTypes(8),newUnit.getX(),newUnit.getY(),True,True)
    CyInterface().addCombatMessage(pUnit.getOwner(),sMsg)

  def retSpellDamageMod(self, unit):
    i = 0
    # Aptitude
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WIMPY1')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WIMPY2')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WIMPY3')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WIMPY4')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WIMPY5')):
      i += 1
      
    # Training  
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT1')):
      i += 2
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT2')):
      i += 2
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT3')):
      i += 2
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT4')):
      i += 3
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT5')):
      i += 4
      
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_METAMAGIC1')):
      i += 5
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_METAMAGIC2')):
      i += 5
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_METAMAGIC3')):
      i += 5

    # States of being
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_UNHOLY_TAINT')):
      i += 5
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_PATRIARCH')):
      i += 5
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_READY_TO_GIFT')):
      i += 5
      
    # Equipment  
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ROD_OF_WINDS')):
      i += 5
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SCORCHED_STAFF')):
      i += 5
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SPELLSTAFF')):
      i += 5
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_STAFF_OF_SOULS')):
      i += 5
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MASTER_CRAFTED_WEAPONS')):
      i += 5
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BATTLE_ROBE')):
      i += 5
      
    return i  

  def retCombat(self,unit):
    i = 0
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT1')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT2')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT3')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT4')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT5')):
      i += 1

    return i

  def iDrill(self,unit):
    i = 0
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL1')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL2')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL3')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL4')):
      i += 1

    return i

  def retRange(self,unit1,unit2):
    iRange = int( math.fabs(unit1.getX()-unit2.getX()) )
    if iRange < int( math.fabs(unit1.getY()-unit2.getY()) ):
      iRange = int( math.fabs(unit1.getY()-unit2.getY()) )

    return iRange 

  def retDistance(self,x1,y1,x2,y2):
    iRange = int( math.fabs(x1-x2) )
    if iRange < int( math.fabs(y1-y2) ):
      iRange = int( math.fabs(y1-y2) )

    return iRange 

  def retDir(self,x,y,tx,ty):
    sDirection = ''
    ry = int( math.fabs(ty - y) )
    rx = int( math.fabs(tx - x) )
    
    if ty > y:
      if ry > rx * 2 and rx > 0:
        sDirection = 'north-'
    if ty < y:
      if ry > rx * 2 and rx > 0:
        sDirection = 'south-'
    if tx < x:
      if rx > ry * 2 and ry > 0:
        sDirection = 'west-'
    if tx > x:
      if rx > ry * 2 and ry > 0:
        sDirection = 'east-'

    if ty > y:
      sDirection = sDirection + 'north'
    if ty < y:
      sDirection = sDirection + 'south'
    if tx < x:
      sDirection = sDirection + 'west'
    if tx > x:
      sDirection = sDirection + 'east'

    return sDirection
    
  def iMorale(self,unit): 
    morale = 0
    iX = unit.getX()
    iY = unit.getY()
    pPlayer = gc.getPlayer(unit.getOwner())
    iImprovement = unit.plot().getImprovementType()
    iR = 1
    pX = 0
    pY = 0
    iFear = 0
    iNobility = 0
    iDamage = unit.getDamage() / 25
    iFort = 0
    iEnemyStr = 0
    iAlliedStr = 0
    
    if unit.plot().isCity():
      iFort = unit.plot().getPlotCity().getDefenseModifier(False) / 10
    if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_TOWER'):
      iFort = 2
    if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_FORT'):
      iFort = 3
    if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_CASTLE'):
      iFort = 5
    if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_CITADEL'):
      iFort = 7
    
    for iiX in range(iX-iR, iX+iR+1, 1):
      for iiY in range(iY-iR, iY+iR+1, 1):
        pPlot = CyMap().plot(iiX,iiY)
        for i in range(pPlot.getNumUnits()):
          pUnit = pPlot.getUnit(i)
          if gc.getTeam(pUnit.getTeam()).isAtWar(pPlayer.getTeam()) and not pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_HIDDEN_CACHE'):
            if (iiX != pX or iiY != pY): 
              morale -= 1
              pX = iiX
              pY = iiY
              
            # Fear  
            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FEAR')) or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_TIMOR_MASK')) or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRAGON')) and not unit.isImmuneToFear():
              iFear = 3
              
            iEnemyStr += ( ( pUnit.baseCombatStr() + pUnit.baseCombatStrDefense() ) * ( 100 - pUnit.getDamage() ) ) / 100
              
          if pUnit.getTeam() == pPlayer.getTeam():
            if iiX != pX or iiY != pY:
              morale += 1
              pX = iiX
              pY = iiY
            
            iAlliedStr += ( ( pUnit.baseCombatStr() + pUnit.baseCombatStrDefense() ) * ( 100 - pUnit.getDamage() ) ) / 100
            
            # Leadership
            thisNobility = self.iNoble(pUnit,0)
            if thisNobility > iNobility:
              iNobility = thisNobility
    
    if iEnemyStr > 0:
      if iAlliedStr > iEnemyStr * 8:
        morale += 3
      elif iAlliedStr > iEnemyStr * 4:
        morale += 2
      elif iAlliedStr > iEnemyStr * 2:
        morale += 1
      elif iAlliedStr < iEnemyStr / 8:  
        morale -= 3
      elif iAlliedStr < iEnemyStr / 4:  
        morale -= 2
      elif iAlliedStr < iEnemyStr / 2:  
        morale -= 1
    
    morale += iFort
    morale -= iFear
    morale += iNobility
    morale += self.iDrill(unit)
    if unit.isImmuneToFear():
      morale += 1
    morale -= iDamage 
    
    return morale

  def reqInteractCache(self,caster,mode):
    iX = caster.getX()
    iY = caster.getY()
    pPlayer = gc.getPlayer(caster.getOwner())
    iMult = 0

    iSearch = self.retSearch(caster)

    if caster.plot().isCity():
      pCity = caster.plot().getPlotCity()
      iMult = int( pCity.getPopulation() / 3 )
      if iMult > caster.getFortifyTurns()*2:
        iMult = caster.getFortifyTurns()*2
      if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_TAVERN')) != 0:
        iMult += iSearch
    else:
      if mode == 9:
        if caster.getFortifyTurns() < 1:
          return False
    
    # Learn about caches worldwide
    if mode == 8 or mode == 9:
      # Learn about caches
      py = PyPlayer( gc.getBARBARIAN_PLAYER() )
      for pUnit in py.getUnitList():
        if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_HIDDEN_CACHE'):
          iRange = self.retRange(caster,pUnit)
          if pUnit.getLevel() <= iSearch and iRange <= iSearch + iMult and mode == 9:
            if iRange > -1 and iRange < 99:
              return True
          if pUnit.getLevel() <= iSearch and iRange > iSearch + iMult and mode == 8:
            if iRange > -1 and iRange < 99:
              return True
      return False


    iR = int( iSearch / 4 )
    for iiX in range(iX-iR, iX+iR+1, 1):
      for iiY in range(iY-iR, iY+iR+1, 1):
        pPlot = CyMap().plot(iiX,iiY)
        for i in range(pPlot.getNumUnits()):
          iRange = int( math.fabs(iiX-iX) )
          if iRange < int( math.fabs(iiY-iY) ):
            iRange = int( math.fabs(iiY-iY) )

          pUnit = pPlot.getUnit(i)
          if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_HIDDEN_CACHE') and pUnit.getLevel() + iRange * 2 <= iSearch:
            if mode == 3 and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT1')):
              return False
            return True
    return False  

    
  def spellExamineCache(self,caster,mode):
    iX = caster.getX()
    iY = caster.getY()
    pPlayer = gc.getPlayer(caster.getOwner())
    bPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
    iMult = 0

    iSearch = self.retSearch(caster)

    sName = 'here'
    sPref = ''
    if caster.plot().isCity():
      pCity = caster.plot().getPlotCity()
      sName = pCity.getName()
      iMult = int( pCity.getPopulation() / 3 )
      if iMult > caster.getFortifyTurns()*2:
        iMult = caster.getFortifyTurns()*2
      if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_TAVERN')) != 0:
        iMult += iSearch

    bCreep = True
    bKill = False

    iR = int( iSearch / 4 )

    # Learn about caches worldwide
    if mode == 8 or mode == 9:
      # Learn about caches
      py = PyPlayer( gc.getBARBARIAN_PLAYER() )
      iCaches = 0
      iCachesLev = 0
      iBestRange = 999
      iNextBestRange = 999
      iNextBestPower = 999
      iFarRange = 999
      for pUnit in py.getUnitList():
        if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_HIDDEN_CACHE'):
          iCaches += 1
          iRange = self.retRange(caster,pUnit)
          if iRange > -1 and iRange < iFarRange and iRange > iSearch + iMult:
            iFarRange = iRange
            fx = pUnit.getX()
            fy = pUnit.getY()
          if iRange > -1 and iRange < iNextBestRange and iRange <= iSearch + iMult and pUnit.getLevel() <= iSearch:
            iNextBestRange = iRange
            tx = pUnit.getX()
            ty = pUnit.getY()
          if pUnit.getLevel() <= iSearch:
            iCachesLev += 1
            if iRange > -1 and iRange < iBestRange and iRange <= iSearch + iMult:
              iBestRange = iRange

      if iBestRange == 999:
        iBestRange = iNextBestRange
        sPref = ', though it is above your experience level (there are no caches within your level within range)'

      if iBestRange < 999:
        sDirection = ' to the ' + self.retDir(iX,iY,tx,ty)
        if sDirection == ' to the ':
          sDirection = ' in the tile'

        if caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BURGLAR3')):
          sDip = 'Your sources say that there are around '+str(iCaches)+' hidden caches in the world, '+str(iCachesLev)+' that are within your experience level, and the closest one is ' + str(iBestRange) + ' tiles' + sDirection + ' of ' + sName + sPref + '...'
        elif caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BURGLAR2')) and iBestRange <= caster.getFortifyTurns():
          sDip = 'Your sources say there is a hidden cache ' + str(iBestRange) + ' tiles' + sDirection + ' of ' + sName + sPref + '...'
        else:
          sDip = 'Your sources say there is a hidden cache' + sDirection + ' of ' + sName + sPref + '...'
      else:
        sDirection = ' to the ' + self.retDir(caster.getX(),caster.getY(),fx,fy)
        if sDirection == ' to the ':
          sDirection = ''

        if iFarRange < 999:
          sDip = 'Your sources say that there is a hidden cache far' + sDirection + ' of ' + sName + sPref + '...'
        else:
          sDip = 'Your sources do not know of any hidden caches within range of ' + sName + '...'

      ## Additional Information
      ## Serpent Report
      iSerpentCount = bPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_SEA_SERPENT'))
      iGreatSerpentCount = bPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_GIANT_SEA_SERPENT'))
      if CyGame().getSorenRandNum(100, "Serpent Report") < iSerpentCount + iGreatSerpentCount and iMult > 0:
        sDip = sDip + '  Sailors tell tales of giant beasts in the sea.  The population of greater serpents is estimated at ' + str(iGreatSerpentCount) + '.  The population of smaller serpents is estimated at ' + str(iSerpentCount) + '.'

      CyInterface().addMessage(caster.getOwner(),False,25,sDip,'',1,'Art/Interface/Buttons/Promotions/Hidden.dds',ColorTypes(8),caster.getX(),caster.getY(),True,True)
      CyInterface().addCombatMessage(caster.getOwner(),sDip)

      return

    pBestUnit = -1
    iClosest = 999
    iR = int( iSearch / 4 )
    for iiX in range(iX-iR, iX+iR+1, 1):
      for iiY in range(iY-iR, iY+iR+1, 1):
        pPlot = CyMap().plot(iiX,iiY)
        for i in range(pPlot.getNumUnits()):
          iRange = int( math.fabs(iiX-iX) )
          if iRange < int( math.fabs(iiY-iY) ):
            iRange = int( math.fabs(iiY-iY) )

          pUnit = pPlot.getUnit(i)
          if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_HIDDEN_CACHE') and pUnit.getLevel() + iRange * 2 <= iSearch:
            if iClosest > iRange:
              iBX = iiX
              iBY = iiY
              iClosest = iRange
              pBestUnit = pUnit

    if pBestUnit != -1: 
      pUnit = pBestUnit 
      iRange = iClosest
      iiX = iBX
      iiY = iBY
      # Found Cache
      if caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MASTER_CRAFTED_WEAPONS')):
        iSearch += 1
      if caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MASTER_CRAFTED_ARMOR')):
        iSearch += 1
      iDiv = ( pUnit.baseCombatStrDefense() + iRange * 3 + iSearch + 1 )
      if iDiv < 1:
        iDiv = 1
      iChance = int( ( iSearch * 100 + 50 ) / iDiv )
      sSpec = ''
      sGuard = ' barbarian'
      if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL1')):
        sGuard = ' undead'
      if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL2')):
        sGuard = ' infernal'
      if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL3')):
        sGuard = ''
      if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER1')):
        sSpec += ', poison'
      if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER2')):
        sSpec += ', disease'
      if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER3')):
        sSpec += ', plague'
      if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT1')):
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL4')):
          iPower = self.retCombat(pUnit)
          sGuard = ' dragon'
          if iPower < 4 or CyGame().getGameTurn() < 300:
            sSpec += ', a wyrmling'
          elif iPower == 4 or CyGame().getGameTurn() < 400:
            sSpec += ', a young dragon'
          else:
            sSpec += ', a dragon!'
        else:
          sSpec += ', ' + str( self.retCombat(pUnit) ) + sGuard + ' guards'

      # Examine Cache
      if mode == 1:
        if caster.getFortifyTurns() == 5 and iRange < 2 and CyGame().getSorenRandNum(100, "Search Cache") < ( iChance / 2 ):
          sDip = caster.getName() + ' is coming up with a plan to loot the cache!  Difficulty reduced by 1!'
          CyInterface().addMessage(caster.getOwner(),False,25,sDip,'',1,'Art/Interface/Buttons/Promotions/Hidden.dds',ColorTypes(8),caster.getX(),caster.getY(),True,True)
          CyInterface().addCombatMessage(caster.getOwner(),sDip)
          if pUnit.baseCombatStr() > 1:
            pUnit.setBaseCombatStr(pUnit.baseCombatStr() - 1)
          else:
            pUnit.setBaseCombatStr(1)

          if pUnit.baseCombatStrDefense() > 1:
            pUnit.setBaseCombatStrDefense(pUnit.baseCombatStrDefense() - 1)
          else:
            pUnit.setBaseCombatStrDefense(1)

        sDir = self.retDir(iX,iY,iiX,iiY)
        sDip = caster.getName() + ' is examining a hidden cache... Distance: '+str(iRange)+' '+sDir+' Skill: '+str(iSearch)+' Dif: ' + str(pUnit.baseCombatStrDefense()+iRange*3) + ' Chance: ' + str( iChance ) + ' Danger: ' + str(pUnit.baseCombatStr()) + sSpec
        CyInterface().addMessage(caster.getOwner(),False,25,sDip,'',1,'Art/Interface/Buttons/Promotions/Hidden.dds',ColorTypes(8),caster.getX(),caster.getY(),True,True)
        CyInterface().addCombatMessage(caster.getOwner(),sDip)

        return

      # Loot Cache
      if mode == 2:
        sDip = caster.getName() + ' is attempting to loot a hidden cache... Skill: '+str(iSearch)+' Dif: ' + str(pUnit.baseCombatStrDefense()+iRange*3) + ' Chance: ' + str( iChance ) + ' Danger: ' + str(pUnit.baseCombatStr()) + sSpec
        CyInterface().addMessage(caster.getOwner(),true,25,sDip,'',1,'Art/Interface/Buttons/Promotions/Hidden.dds',ColorTypes(8),caster.getX(),caster.getY(),True,True)
        CyInterface().addCombatMessage(caster.getOwner(),sDip)
        iRoll = CyGame().getSorenRandNum(100, "Roll It")
        if iRoll <= iChance:
          # Success!
  #       pUnit.setXY(iX, iY, true, true, false)
          iXP = (100 - iChance) / 20 + pUnit.baseCombatStr() / 2 + pUnit.getLevel() / 2
          caster.changeExperience( iXP , -1, False, False, False)
          bKill = True
          iGold = CyGame().getSorenRandNum( pUnit.baseCombatStr() * 25, "Find Gold") + pUnit.baseCombatStr() * 10
          sDip = caster.getName() + ' has success!  You find '+str(iGold)+' gold pieces and gain '+str(iXP)+'xp!'
          pPlayer.setGold( pPlayer.getGold() + iGold )
          CyInterface().addMessage(caster.getOwner(),true,25,sDip,'',1,'Art/Interface/Buttons/Promotions/Hidden.dds',ColorTypes(11),caster.getX(),caster.getY(),True,True)
          CyInterface().addCombatMessage(caster.getOwner(),sDip)

        elif iRoll > iChance and iRoll < iChance + 25 and iRoll < 95:
          # Failure
          sDip = 'Failure'
          if CyGame().getSorenRandNum(100, "Roll It2") < 35:
            bCreep = False
          CyInterface().addMessage(caster.getOwner(),true,25,sDip,'',1,'Art/Interface/Buttons/Promotions/Hidden.dds',ColorTypes(7),caster.getX(),caster.getY(),True,True)
          CyInterface().addCombatMessage(caster.getOwner(),sDip)

        else:
          # Detonation
          sDip = 'Critical Failure'
          bCreep = False
          CyInterface().addMessage(caster.getOwner(),true,25,sDip,'',1,'Art/Interface/Buttons/Promotions/Hidden.dds',ColorTypes(7),caster.getX(),caster.getY(),True,True)
          CyInterface().addCombatMessage(caster.getOwner(),sDip)

          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER1')):
            caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED'),True)
          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER2')):
            caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DISEASED'),True)
          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER3')):
            caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED'),True)
    
          bcs = caster.baseCombatStr()
          if bcs < 1:
            bcs = 1
          iDamage = CyGame().getSorenRandNum(pUnit.baseCombatStr()*100, "Damage") / bcs
          caster.doDamageNoCaster(iDamage, 100, gc.getInfoTypeForString('DAMAGE_PHYSICAL'), false)            

      # Draw Guards Away
      if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT1')):
        iPow = self.retCombat( pUnit )
        iNum = iPow
        bPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
        pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT1'),False)
        iii = 0
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL4')):
          iNum = 1
          if iPow < 4 or CyGame().getGameTurn() < 300:
            sEnemy = 'UNIT_WYRMLING'
          elif iPow == 4 or CyGame().getGameTurn() < 400:
            sEnemy = 'UNIT_YOUNG_DRAGON'
          elif iPow == 5:
            sEnemy = 'UNIT_DRAGON'

        for iEnemy in range( iNum ):
          if sGuard == '':
            sEnemy = self.sComputerUnit()
          elif sGuard == ' barbarian':
            sEnemy = self.sBarbUnit()
          elif sGuard == ' undead':
            sEnemy = self.sUndeadUnit()
          elif sGuard == ' infernal':
            sEnemy = self.sEvilUnit()

          iPX = iX
          if iMult > 0:
            iPX += 1
          newUnit = bPlayer.initUnit(gc.getInfoTypeForString(sEnemy), iPX, iY, UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_NORTH)
          self.equip(newUnit)
          if sEnemy == 'UNIT_WYRMLING' or sEnemy == 'UNIT_YOUNG_DRAGON' or sEnemy == 'UNIT_DRAGON':
            # newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LOYALTY'),True)
            newUnit.setDuration( 30 + CyGame().getSorenRandNum(70, "Dragon Duration") )
          if bCreep:
            newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CREEP'),True)

        if mode == 3:
          if pUnit.baseCombatStr() > 2:
            pUnit.setBaseCombatStr(pUnit.baseCombatStr() - 2)
          else:
            pUnit.setBaseCombatStr(1)

          if pUnit.baseCombatStrDefense() > 2:
            pUnit.setBaseCombatStrDefense(pUnit.baseCombatStrDefense() - 2)
          else:
            pUnit.setBaseCombatStrDefense(1)

      if bKill:
        if iMult > 0:
          pUnit.setXY(iX + 1, iY, true, true, false)
          
        # if pUnit.plot().isOwned():  
          # oPlayer = gc.getPlayer(pUnit.plot().getOwner())
          # newUnit = oPlayer.initUnit(pUnit.getUnitType(), pUnit.getX(), pUnit.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
          # newUnit.convert(pUnit)
          # newUnit.kill(False,0)
        # else:

          # pUnit.kill(False,0)
        pUnit.kill(False,0)
            
      caster.setFortifyTurns(0)
    
    
  def iCrowdingDamage(self, pUnit):
    roomFor = 1
    pPlot = pUnit.plot()
    if pPlot.isCity():
      roomFor = roomFor + pPlot.getPlotCity().getPopulation()
    if pPlot.getNumUnits() <= roomFor:
      return 0
      
    nobLevel = 0
    for ii in range(pPlot.getNumUnits()):
      oUnit = pPlot.getUnit(ii)
      # The strongest noble adds room for units
      if self.iNoble(oUnit,1) > nobLevel:
        nobLevel = self.iNoble(oUnit,1)
      # Computer units add room for themselves    
      if not gc.getPlayer(oUnit.getOwner()).isHuman() or oUnit.getDomainType() == gc.getInfoTypeForString('DOMAIN_IMMOBILE'):
        roomFor += 1
      # Carried units don't count
      if oUnit.isCargo():
        roomFor += 1
    if nobLevel > 0:
      roomFor += nobLevel
      
    iDam = pPlot.getNumUnits() - roomFor

    iImprovement = pPlot.getImprovementType()
    if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_TOWER'):
      iDam -= 1
    if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_FORT'):
      iDam -= 2
    if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_CASTLE'):
      iDam -= 4
    if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_CITADEL'):
      iDam -= 8
    
    if iDam < 0:
      iDam = 0
    
    return iDam
  
  def reqHeal(self, caster):
    pPlot = caster.plot()
    iPoisoned = gc.getInfoTypeForString('PROMOTION_POISONED')
    for i in range(pPlot.getNumUnits()):
      pUnit = pPlot.getUnit(i)
      if (pUnit.isAlive() and pUnit.getDamage() > 0):
        return True
      if pUnit.isHasPromotion(iPoisoned):
        return True
    return False
    
  def spellHealingTouch(self,caster):
    iL = caster.getLevel()
    iNumHealed = 0
    pPlot = caster.plot()
    sMsg = caster.getName() + ' tends wounds for '
    for i in range(pPlot.getNumUnits()):
      pUnit = pPlot.getUnit(i)
      if (pUnit.isAlive() and pUnit.getDamage() > 0):
        iDefStr = pUnit.baseCombatStr()
        if iDefStr < 1:
          iDefStr = 1
        iMod = ( iL * caster.baseCombatStr() ) / iDefStr + 1
        iHealAmount = CyGame().getSorenRandNum(iMod, "Healing Touch Amount") + iMod
        pUnit.changeDamage(-iHealAmount,0) #player doesn't matter - it won't kill
        sMsg = sMsg + pUnit.getName() + ' (' + str(iHealAmount) + '), '
        iNumHealed = iNumHealed + 1
        if ( iNumHealed + 1 > 0 ):
          break

    CyInterface().addMessage(caster.getOwner(),False,25,sMsg,'AS3D_SPELL_BLESS',1,caster.getButton(),ColorTypes(12),caster.getX(),caster.getY(),True,True)

  def spellFieldMedic(self,caster):
    iL = caster.getLevel()
    iNumHealed = 1
    if iNumHealed < 1:
      iNumHealed = 1
    pPlot = caster.plot()
    lUnit = -1
    
    sMsg = caster.getName() + ' tends wounds for '

    for ii in range(iNumHealed):
      iBestDamage = 0
      for i in range(pPlot.getNumUnits()):
        pUnit = pPlot.getUnit(i)
        if (pUnit.isAlive() and pUnit.getDamage() > 0 and not i == lUnit):
          if pUnit.getDamage() > iBestDamage:
            iBestDamage = pUnit.getDamage()
            iBestUnit = pUnit
            lUnit = i
            
      if iBestDamage > 0:
        pUnit = iBestUnit
        iDefStr = pUnit.baseCombatStr()
        if iDefStr < 1:
          iDefStr = 1
        iMod = ( iL * caster.baseCombatStr() ) / iDefStr + 1
        iHealAmount = CyGame().getSorenRandNum(iMod, "Healing Touch Amount") + iMod
        pUnit.changeDamage(-iHealAmount,0) #player doesn't matter - it won't kill
        sMsg = sMsg + pUnit.getName() + ' (' + str(iHealAmount) + '), '
    
    CyInterface().addMessage(caster.getOwner(),False,25,sMsg,'AS3D_SPELL_BLESS',1,caster.getButton(),ColorTypes(12),caster.getX(),caster.getY(),True,True)
    

  def reqSustain(self, caster):
    pPlot = caster.plot()
    if caster.getDuration() > 0:
      return False
    for i in range(pPlot.getNumUnits()):
      pUnit = pPlot.getUnit(i)
      bUnit = True
      if ( pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_MAGIC_MISSILE') or pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_FIREBALL') or pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_METEOR') ):
        bUnit = False
      if ( pUnit.getDuration() > 0 and pUnit.baseCombatStr() <= caster.baseCombatStr() * 2 and bUnit and pUnit.getUnitType() != gc.getInfoTypeForString('UNIT_PUPPET')  ):
        return True

    return False

  def spellSustain(self, caster):
    iSustain = 1
    bPlayer = gc.getPlayer(caster.getOwner())
    if bPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_SUMMONER')):
      iSustain = 2
    iDuration = 99
    pBestUnit = -1
    pPlot = caster.plot()
    for i in range(pPlot.getNumUnits()):
      pUnit = pPlot.getUnit(i)
      bUnit = True
      if ( pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_MAGIC_MISSILE') or pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_FIREBALL') or pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_METEOR') ):
        bUnit = False
      if ( pUnit.getDuration() > 0 and pUnit.baseCombatStr() <= caster.baseCombatStr() * 2 and bUnit and pUnit.getUnitType() != gc.getInfoTypeForString('UNIT_PUPPET') ):
        if ( pUnit.getDuration() < iDuration ):
          pBestUnit = pUnit
          iDuration = pUnit.getDuration()

    if pBestUnit != -1:
      pBestUnit.setDuration( iDuration + iSustain )
    
  def spellUnsummon(self, caster):
    bPlayer = gc.getPlayer(caster.getOwner())
    pBestUnit = -1
    iDuration = 99
    pPlot = caster.plot()
    for i in range(pPlot.getNumUnits()):
      pUnit = pPlot.getUnit(i)
      bUnit = True
      if ( pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_MAGIC_MISSILE') or pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_FIREBALL') or pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_METEOR') ):
        bUnit = False
      if ( pUnit.getDuration() > 0 and pUnit.baseCombatStr() <= caster.baseCombatStr() * 2 and bUnit and pUnit.getUnitType() != gc.getInfoTypeForString('UNIT_PUPPET') ):
        if ( pUnit.getDuration() < iDuration ):
          pBestUnit = pUnit
          iDuration = pUnit.getDuration()

    if pBestUnit != -1:
      iXP = int( pBestUnit.getExperience() / 2 )
      if caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DIMENSIONAL3')):
        iXP = pBestUnit.getExperience()
      caster.changeExperience(iXP, -1, false, false, false)
      pBestUnit.kill(True, 0)
    
  def pay(self, pCity, sBuilding, iCost, iPlayer, sDesc):
    ## Load City Stock
    strSetData = cPickle.loads(pCity.getScriptData())
    if sBuilding not in strSetData:
      strSetData[sBuilding] = 0
      
    ## Set Max City Stock 
    if strSetData[sBuilding] < CyGame().getGameTurn() - pCity.getPopulation() * 12:
      strSetData[sBuilding] = CyGame().getGameTurn() - pCity.getPopulation() * 12

    iCostMod = ( iCost * 15 ) / pCity.getPopulation() 
    
    strSetData[sBuilding] = strSetData[sBuilding] + iCostMod
    pCity.setScriptData(cPickle.dumps(strSetData))

    iStock = ( ( CyGame().getGameTurn() - strSetData[sBuilding] ) * pCity.getPopulation() ) / 15
    iMaxStock = ( pCity.getPopulation() * 12 * pCity.getPopulation() ) / 15
    if iMaxStock < 1:
      iMaxStock = 1
    iPercent = ( iStock * 100 ) / iMaxStock
    if iStock < 0:
      iPercent = 0
    sMsg = 'The ' + pCity.getName() + ' ' + sDesc + ' has ' + str(iStock) + ' stock remaining (' + str(iPercent) + '%)...'
    CyInterface().addMessage(iPlayer,True,25,sMsg,'AS2D_GOODY_GOLD',1,'Art/Interface/Buttons/Equipment/DragonsHorde.dds',ColorTypes(8),pCity.getX(),pCity.getY(),True,True)
    CyInterface().addCombatMessage(iPlayer,sMsg)

  def retSearch(self, unit):
    i = 0
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BURGLAR1')):
      i += 1
    if i == 0:
      return 0
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BURGLAR2')):
      i += 2
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BURGLAR3')):
      i += 3
      
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MOBILITY1')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MOBILITY2')):
      i += 1
      
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SENTRY')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SENTRY2')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_PERFECT_SIGHT')):
      i += 2
      
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL1')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL2')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL3')):
      i += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL4')):
      i += 1

    if unit.getFortifyTurns() < 5:
      ii = i / 2 + unit.getFortifyTurns()
      if ii > i:
        ii = i
      i = ii

    iExtendedSearch = unit.getFortifyTurns()
    if iExtendedSearch > int( i / 2 ):
      iExtendedSearch = int( i / 2 )
    if iExtendedSearch > 5:
      iExtendedSearch = 5

    i += iExtendedSearch  

    return i

  def bTechExist(self, sTech):
    bFoundValid = false
    iTech = CvUtil.findInfoTypeNum(gc.getTechInfo, gc.getNumTechInfos(), sTech)
    for iPlayer in range(gc.getMAX_CIV_PLAYERS()):      
      loopPlayer = gc.getPlayer(iPlayer)
      if loopPlayer.isAlive():
        if gc.getTeam(loopPlayer.getTeam()).isHasTech(iTech):
          bFoundValid = true
          break
    return bFoundValid

  def initCityVars(self, city):
    try:
      strSetData = cPickle.loads(city.getScriptData())
    except EOFError:
      strSetData = {}
    strSetData['BUILDING_LIBRARY'] = CyGame().getGameTurn()
    strSetData['BUILDING_CRAFTSMEN_GUILD'] = CyGame().getGameTurn()
    strSetData['BUILDING_HERBALIST'] = CyGame().getGameTurn()
    strSetData['BUILDING_ALCHEMY_LAB'] = CyGame().getGameTurn()
    strSetData['BUILDING_MAGE_GUILD'] = CyGame().getGameTurn()
    strSetData['TrainMage'] = 0
    strSetData['TrainingYard'] = 0
    strSetData['OBELISK'] = 0
    strSetData['COUNCIL'] = 0
    strSetData['TEMPLE'] = 0 
    strSetData['PLUNDER'] = 0 
    strSetData['ECON'] = 0 
    city.setScriptData(cPickle.dumps(strSetData))

  def msgAll(self, sMsg, x, y, sendingPlayer, pic):
    for iPlayer in range(gc.getMAX_PLAYERS()):
      mPlayer = gc.getPlayer(iPlayer)
      if mPlayer.isAlive() and sendingPlayer > -1 and (mPlayer.canContact(sendingPlayer) or iPlayer == sendingPlayer or gc.getPlayer(sendingPlayer).isBarbarian()):
        py = PyPlayer(iPlayer)
        CyInterface().addMessage(iPlayer,false,25,sMsg,'',1,pic,ColorTypes(8),x,y,True,True)
        CyInterface().addCombatMessage(iPlayer,sMsg)

  def generateLoot(self, iUnit, iHaveScrolls):
    if iHaveScrolls < 1:
      iHaveScrolls = iUnit.baseCombatStr()

    iWeapons = 0
    iArmor = 0
    iTreasure = 0
    iPotions = 0
    iScrolls = 0
    iItems = 0
    iMessage = 0

    if CyGame().getSorenRandNum(100, "ItemSelect1") < iHaveScrolls:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IMPROVED_WEAPONS'), True)
      iWeapons = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ItemSelect2") < iHaveScrolls - 3:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HEAVY_WEAPONS'), True)
      iWeapons = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ItemSelect3") < iHaveScrolls - 6:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MASTER_CRAFTED_WEAPONS'), True)
      iWeapons = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ItemSelect4") < iHaveScrolls:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IMPROVED_ARMOR'), True)
      iArmor = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ItemSelect5") < iHaveScrolls - 3:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HEAVY_ARMOR'), True)
      iArmor = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ItemSelect6") < iHaveScrolls - 6:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MASTER_CRAFTED_ARMOR'), True)
      iArmor = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ItemSelect9") < iHaveScrolls - 3:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_TREASURE1'), True)
      iTreasure = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ItemSelect10") < iHaveScrolls - 6:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_TREASURE2'), True)
      iTreasure = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ItemSelect11") < iHaveScrolls - 9:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_TREASURE3'), True)
      iTreasure = 1
      iMessage = 1

    ## Adept Units have a higher chance of having magical items
    if iUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ADEPT'):
      iHaveScrolls = iHaveScrolls * 4

    if CyGame().getSorenRandNum(100, "PotionSelect1") < iHaveScrolls + 4:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POTION_HEALING_MINOR'), True)
      iPotions = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "PotionSelect1a") < iHaveScrolls + 2:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POTION_HEALING_MODERATE'), True)
      iPotions = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "PotionSelect3") < iHaveScrolls + 2:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POTION_HASTE'), True)
      iPotions = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "PotionSelect2") < iHaveScrolls + 2:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POTION_STRENGTH'), True)
      iPotions = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "PotionSelect0") < iHaveScrolls:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POTION_XP_MINOR'), True)
      iPotions = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "PotionSelect1c") < iHaveScrolls:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POTION_REGENERATION'), True)
      iPotions = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "PotionSelect1b") < iHaveScrolls - 2:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POTION_HEALING_GREATER'), True)
      iPotions = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ScrollSelect1") < iHaveScrolls - 2:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SCROLL_MM'), True)
      iScrolls = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ScrollSelect2") < iHaveScrolls - 2:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SCROLL_MA'), True)
      iScrolls = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ScrollSelect3") < iHaveScrolls - 2:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SCROLL_SB'), True)
      iScrolls = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ScrollSelect4") < iHaveScrolls - 2:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SCROLL_MR'), True)
      iScrolls = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "PotionSelect2a") < iHaveScrolls - 4:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POTION_STRENGTH_ENDURING'), True)
      iPotions = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "PotionSelect2b") < iHaveScrolls - 4:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POTION_VAMPIRISM'), True)
      iPotions = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "PotionSelect0a") < iHaveScrolls - 4:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POTION_XP'), True)
      iPotions = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ScrollSelect5") < iHaveScrolls - 4:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SCROLL_SK'), True)
      iScrolls = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ScrollSelect6") < iHaveScrolls - 4:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SCROLL_FB'), True)
      iScrolls = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ItemSelect8") < iHaveScrolls - 6:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BOOTS_OF_HASTE'), True)
      iItems = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "PotionSelect4") < iHaveScrolls - 6:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HEALING_SALVE'), True)
      iPotions = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ScrollSelect7") < iHaveScrolls - 6:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SCROLL_SE'), True)
      iScrolls = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ScrollSelect8") < iHaveScrolls - 8:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SCROLL_CR'), True)
      iScrolls = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ScrollSelect9") < iHaveScrolls - 8:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SCROLL_MS'), True)
      iScrolls = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ItemSelect7") < iHaveScrolls - 10:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BATTLE_ROBE'), True)
      iItems = 1
      iMessage = 1

    if CyGame().getSorenRandNum(100, "ItemSelect9") < iHaveScrolls - 8:
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POTION_OF_RESTORATION'), True)
      iItems = 1
      iMessage = 1

    if iUnit.getUnitType() == gc.getInfoTypeForString('UNIT_MERCHANT_SHIP') and iMessage > 0:
      sMsg = ''
      if iWeapons > 0:
        sMsg = sMsg + 'weapons, '
      if iArmor > 0:
        sMsg = sMsg + 'armor, '
      if iTreasure > 0:
        sMsg = sMsg + 'treasure, '
      if iPotions > 0:
        sMsg = sMsg + 'potions, '
      if iScrolls > 0:
        sMsg = sMsg + 'scrolls, '
      if iItems > 0:
        sMsg = sMsg + 'magical items, '

      CyInterface().addMessage(iUnit.getOwner(),false,25,'Your '+iUnit.getName()+' has gained '+sMsg+'gold and experience in recent trades!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),iUnit.getX(),iUnit.getY(),True,True)
      CyInterface().addCombatMessage(iUnit.getOwner(),'Your '+iUnit.getName()+' has gained '+sMsg+'gold and experience in recent trades!')


  def equip(self, iUnit):
    if iUnit.baseCombatStr() < 1:
      return
    if iUnit.getDuration() > 0:
      return

    iGameTurn = CyGame().getGameTurn()
    iHaveScrolls = 0
    iBigCache = 0
    iExtraLev = 0
    # Initiate Hidden Caches
    if iUnit.getUnitType() == gc.getInfoTypeForString('UNIT_HIDDEN_CACHE') and not iUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FEAR')):
      if iGameTurn < 4:
        iBigCache = iGameTurn 
        iExtraLev = 10
    
      iSkl = CyGame().getSorenRandNum(12, "Cache") - 2 + iBigCache * 2 + iExtraLev + iGameTurn / 50
      if iSkl < 1:
        iSkl = 1
      if iSkl > 18:
        iSkl = 18
      
      iUnit.setLevel( iSkl )

      iStr = CyGame().getSorenRandNum(10, "CacheStr") + iGameTurn / 50 - 2 + iBigCache * 2
      if iStr < 1:
        iStr = 1
      iUnit.setBaseCombatStr(iStr)

      iDef = CyGame().getSorenRandNum(12, "CacheDef") + iGameTurn / 50 + iBigCache * 10
      if iDef < 1:
        iDef = 1
      iUnit.setBaseCombatStrDefense(iDef)

      iHaveScrolls = int( iSkl + iStr + iDef ) + 5

      # Mark this cache as having been processed
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FEAR'),True)
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_THROWING_AXES'), True)

      iRoll = CyGame().getSorenRandNum(20, "Guards")
      if iRoll > 10:
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT1'),True)
      if iRoll > 12:
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT2'),True)
      if iRoll > 14:
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT3'),True)
      if iRoll > 16:
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT4'),True)
      if iRoll > 18:
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT5'),True)
      if iRoll > 10:
        iRoll = CyGame().getSorenRandNum(5, "GuardType")
        if iRoll == 1:
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL1'),True)
        if iRoll == 2:
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL2'),True)
        if iRoll == 3:
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL3'),True)
        if iRoll == 4:
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL4'),True)

      if CyGame().getSorenRandNum(20+iStr/2, "Trap1") > 12:
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER1'),True)
      if CyGame().getSorenRandNum(20+iStr/2, "Trap2") > 15:
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER2'),True)
      if CyGame().getSorenRandNum(20+iStr/2, "Trap3") > 18:
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER3'),True)

      if iDef > 8:
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_TREASURE2'),True)
      if iDef > 12:
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_TREASURE3'),True)

    iMod = 0
    iFix = 0

    if self.bTechExist('TECH_BRONZE_WORKING'):
      iFix += 15
    if self.bTechExist('TECH_IRON_WORKING'):
      iFix += 15
    if self.bTechExist('TECH_MITHRIL_WORKING'):
      iFix += 30

    iCreep = CyGame().getSorenRandNum(4, "IsCreep")
    if (iUnit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_BEAST') and iCreep == 1 and iUnit.baseCombatStr() > 0 and iUnit.baseCombatStr() < 12 and CyGame().getSorenRandNum(150, "FewEarlyCreeps") < CyGame().getGameTurn() ) and not iUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO')):
      iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CREEP'), True)

    if iUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CREEP')):
      iMod = 60

    if (iUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_MELEE') or iUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_NAVAL')):
      i = CyGame().getSorenRandNum(100+iMod, "EquipmentSelect") + iFix
      if(i>100 and i<125):
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), True)
      elif(i>124):
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), True)
      elif(i>149):
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MITHRIL_WEAPONS'), True)

    if iUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_RECON'):
      i = CyGame().getSorenRandNum(400+iMod, "EquipmentSelect") + iFix
      if(i>250 and i<375):
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONOUS'), True)
      elif(i>374):
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED_BLADE'), True)

    if iUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ARCHER'):
      i = CyGame().getSorenRandNum(400+iMod, "EquipmentSelect") + iFix
      if(i>300):
        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONOUS'), True)

    if ( iUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ANIMAL') and self.bTechExist('TECH_FERAL_BOND') ):
      iUnit.setHasPromotion( gc.getInfoTypeForString('PROMOTION_DIRE'), True )

    if (iUnit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_ANIMAL') and iUnit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_NAVAL') and iUnit.getUnitType() != gc.getInfoTypeForString('UNIT_SEA_SERPENT') and iUnit.getUnitType() != gc.getInfoTypeForString('UNIT_GIANT_SEA_SERPENT')):
      if iUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ADEPT'):
        iSphere = CyGame().getSorenRandNum(9, "SphereSelect")       
        if iSphere == 0:
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FIRE1'), True)
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FIRE2'), True)
        elif iSphere == 1:
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WATER1'), True)
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WATER2'), True)
        elif iSphere == 2:
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EARTH1'), True)
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EARTH2'), True)
        elif iSphere == 3:
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_AIR1'), True)
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_AIR2'), True)
        elif iSphere == 4:
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEATH1'), True)
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEATH2'), True)
        elif iSphere == 5:
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENTROPY1'), True)
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENTROPY2'), True)
        elif iSphere == 6:
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LIFE1'), True)
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LIFE2'), True)
        elif iSphere == 7:
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CHAOS1'), True)
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CHAOS2'), True)
        elif iSphere == 8:
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SHADOW1'), True)
          iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SHADOW2'), True)

        iUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CREEP'), True)
        if self.bTechExist('TECH_KNOWLEDGE_OF_THE_ETHER'):
          iUnit.setExperience(CyGame().getSorenRandNum(iGameTurn/20, "Conjurer Experience")+iGameTurn/20, -1)

      self.generateLoot(iUnit,iHaveScrolls)


  def sBarbUnit(self):
    i = CyGame().getSorenRandNum(100, "BarbUnitSelect")

    if self.bTechExist('TECH_BRONZE_WORKING'):
      i += 30
    if self.bTechExist('TECH_IRON_WORKING'):
      i += 30
    if self.bTechExist('TECH_MITHRIL_WORKING'):
      i += 60

    if(i<50):
      return 'UNIT_GOBLIN'
    elif(i<100):
      return 'UNIT_WARRIOR'
    elif(i<150):
      ii = CyGame().getSorenRandNum(6, "BarbUnitSelectTier")
      if( ii < 3 ):
        return 'UNIT_AXEMAN'
      elif( ii < 5 ):
        return 'UNIT_ARCHER'
      elif( ii == 5 ):
        return 'UNIT_ADEPT'
    elif(i<200):
      ii = CyGame().getSorenRandNum(6, "BarbUnitSelectTier")
      if( ii < 3 ):
        return 'UNIT_CHAMPION'
      elif( ii < 4 ):
        return 'UNIT_MAGE'
      elif( ii < 5 ):
        return 'UNIT_WOLF_RIDER'
      elif( ii == 5 ):
        return 'UNIT_LIZARDMAN'
    elif(i>200):
      return 'UNIT_OGRE'
    return 'UNIT_WARRIOR'

  def sComputerUnit(self):
    i = CyGame().getSorenRandNum(100, "CompUnitSelect")

    if self.bTechExist('TECH_BRONZE_WORKING'):
      i += 30
    if self.bTechExist('TECH_IRON_WORKING'):
      i += 30
    if self.bTechExist('TECH_MITHRIL_WORKING'):
      i += 60

    if(i<50):
      return 'UNIT_SCOUT'
    elif(i<100):
      return 'UNIT_WARRIOR'
    elif(i<150):
      ii = CyGame().getSorenRandNum(6, "CompUnitSelectTier")
      if( ii == 0 ):
        return 'UNIT_HORSEMAN'
      if( ii < 3 ):
        return 'UNIT_AXEMAN'
      elif( ii < 5 ):
        return 'UNIT_ARCHER'
      elif( ii == 5 ):
        return 'UNIT_ADEPT'
    elif(i>149):
      ii = CyGame().getSorenRandNum(6, "CompUnitSelectTier")
      if( ii < 3 ):
        return 'UNIT_CHAMPION'
      elif( ii < 4 ):
        return 'UNIT_MAGE'
      elif( ii < 5 ):
        return 'UNIT_LONGBOWMAN'
      elif( ii == 5 ):
        return 'UNIT_RANGER'

    return 'UNIT_WARRIOR'

  def sUndeadUnit(self):
    i = CyGame().getSorenRandNum(100, "BarbUnitSelect")

    if self.bTechExist('TECH_BRONZE_WORKING'):
      i += 30
    if self.bTechExist('TECH_IRON_WORKING'):
      i += 30
    if self.bTechExist('TECH_MITHRIL_WORKING'):
      i += 60

    if(i<50):
      return 'UNIT_ZOMBIE_1'
    elif(i<100):
      ii = CyGame().getSorenRandNum(6, "BarbUnitSelectTier")
      if( ii < 2 ):
        return 'UNIT_SKELETON'
      elif( ii < 4 ):
        return 'UNIT_ZOMBIE_2'
      elif( ii < 5 ):
        return 'UNIT_ZOMBIE'
      elif( ii == 5 ):
        return 'UNIT_DROWN'
    elif(i<150):
      ii = CyGame().getSorenRandNum(6, "BarbUnitSelectTier")
      if( ii < 3 ):
        return 'UNIT_SPECTRE'
      elif( ii < 5 ):
        return 'UNIT_PYRE_ZOMBIE'
      elif( ii == 5 ):
        return 'UNIT_DISEASED_CORPSE'
    elif(i<200):
      ii = CyGame().getSorenRandNum(6, "BarbUnitSelectTier")
      if( ii < 3 ):
        return 'UNIT_SKELETON_WARRIOR'
      elif( ii == 3 ):
        return 'UNIT_LICH'
      elif( ii == 4 ):
        return 'UNIT_WRAITH'
      elif( ii == 5 ):
        return 'UNIT_DEATH_KNIGHT'
    elif(i>200):
      return 'UNIT_DEATH_KNIGHT'
    return 'UNIT_SKELETON'

  def sEvilUnit(self):
    i = CyGame().getSorenRandNum(100, "BarbUnitSelect")

    if self.bTechExist('TECH_BRONZE_WORKING'):
      i += 30
    if self.bTechExist('TECH_IRON_WORKING'):
      i += 30
    if self.bTechExist('TECH_MITHRIL_WORKING'):
      i += 60

    if(i<100):
      ii = CyGame().getSorenRandNum(6, "BarbUnitSelectTier")
      if( ii < 5 ):
        return 'UNIT_IMP'
      elif( ii == 5 ):
        return 'UNIT_CHAOS_MARAUDER'
    elif(i<150):
      ii = CyGame().getSorenRandNum(6, "BarbUnitSelectTier")
      if( ii < 1 ):
        return 'UNIT_CHAOS_MARAUDER'
      elif( ii < 3 ):
        return 'UNIT_SUCCUBUS'
      elif( ii < 5 ):
        return 'UNIT_STYGIAN_GUARD'
      elif( ii == 5 ):
        return 'UNIT_TAR_DEMON_MED'
    elif(i<200):
      ii = CyGame().getSorenRandNum(6, "BarbUnitSelectTier")
      if( ii < 3 ):
        return 'UNIT_STYGIAN_GUARD'
      elif( ii < 5 ):
        return 'UNIT_PIT_BEAST'
      elif( ii == 5 ):
        return 'UNIT_TAR_DEMON'
    elif(i>200):
      return 'UNIT_BALOR'
    return 'UNIT_IMP'

  def sAnimalUnit(self):
    i = CyGame().getSorenRandNum(10, "AnimalUnitSelect") + 1
    if(i==1):
      return 'UNIT_BABY_SPIDER'
    elif(i==2):
      return 'UNIT_BEAR'
    elif(i==3):
      return 'UNIT_ELEPHANT'
    elif(i==4):
      return 'UNIT_GIANT_SPIDER'
    elif(i==5):
      return 'UNIT_GORILLA'
    elif(i==6):
      return 'UNIT_LION'
    elif(i==7):
      return 'UNIT_TIGER'
    elif(i==8):
      return 'UNIT_WOLF'
    elif(i==9):
      return 'UNIT_GRIFFON'
    elif(i==10):
      return 'UNIT_SCORPION'

    return 'UNIT_GIANT_SPIDER'

  def cantake(self,pUnit,iProm):
    if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_MELEE'):
      return True
    if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_MOUNTED'):
      return True
    if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_BEAST'):
      return True
    if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_NAVAL'):
      return True
    if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_SIEGE'):
      return True

    if iProm == gc.getInfoTypeForString('PROMOTION_IMPROVED_WEAPONS'):
      if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ANIMAL'):
        return True
      if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ARCHER'):
        return True
      if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_DISCIPLE'):
        return True
      if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_RECON'):
        return True
      if pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_WORKER'):
        return True

    if iProm == gc.getInfoTypeForString('PROMOTION_IMPROVED_ARMOR'):
      if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ANIMAL'):
        return True
      if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_DISCIPLE'):
        return True
      if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_RECON'):
        return True
      if pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_WORKER'):
        return True

    if iProm == gc.getInfoTypeForString('PROMOTION_HEAVY_ARMOR'):
      if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_DISCIPLE'):
        return True

    return False

  def addUnit(self, iUnit):
    biPlayer = gc.getBARBARIAN_PLAYER()
    pBestPlot = -1
    iBestPlot = -1
    for i in range (CyMap().numPlots()):
      pPlot = CyMap().plotByIndex(i)
      iPlot = -1
      if pPlot.isWater() == False:
        if pPlot.getNumUnits() == 0:
          if pPlot.isCity() == False:
            if pPlot.isImpassable() == False:
              iPlot = CyGame().getSorenRandNum(500, "Add Unit")
              iPlot = iPlot + (pPlot.area().getNumTiles() * 10)
              if pPlot.isBarbarian():
                iPlot = iPlot + 200
              if (pPlot.isOwned() and pPlot.isBarbarian() != True):
                iPlot = iPlot / 2
              if pPlot.isVisibleEnemyUnit(biPlayer):
                iPlot = iPlot / 2
              if iPlot > iBestPlot:
                iBestPlot = iPlot
                pBestPlot = pPlot
    if iBestPlot != -1:
      bPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
      newUnit = bPlayer.initUnit(iUnit, pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
      newUnit.finishMoves()
      self.equip(newUnit)
      if iUnit == gc.getInfoTypeForString('UNIT_STEPHANOS') or iUnit == gc.getInfoTypeForString('UNIT_YERSINIA') or iUnit == gc.getInfoTypeForString('UNIT_BUBOES') or iUnit == gc.getInfoTypeForString('UNIT_ARS'):
        newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_SUCCUBUS'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), True)
        newUnit.finishMoves()
        self.equip(newUnit)
        newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_SUCCUBUS'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), True)
        newUnit.finishMoves()
        self.equip(newUnit)
        newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_RANGER'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
        newUnit.finishMoves()
        self.equip(newUnit)
        newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_RANGER'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
        newUnit.finishMoves()
        self.equip(newUnit)
        newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_RANGER'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
        newUnit.finishMoves()
        self.equip(newUnit)
        newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_RANGER'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
        newUnit.finishMoves()
        self.equip(newUnit)
        newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_RANGER'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
        newUnit.finishMoves()
        self.equip(newUnit)
        newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_CHAMPION'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), True)
        newUnit.finishMoves()
        self.equip(newUnit)
        newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_CHAMPION'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), True)
        newUnit.finishMoves()
        self.equip(newUnit)
        newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_CHAMPION'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), True)
        newUnit.finishMoves()
        self.equip(newUnit)
        newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_CHAMPION'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), True)
        newUnit.finishMoves()
        self.equip(newUnit)
        newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_CHAMPION'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), True)
        newUnit.finishMoves()
        self.equip(newUnit)
        newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_CHAMPION'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), True)
        newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
        newUnit.finishMoves()
        self.equip(newUnit)
      return newUnit
      
    return -1  

  def addBarbUnit(self, iUnit):
    biPlayer = gc.getBARBARIAN_PLAYER()
    pBestPlot = -1
    iBestPlot = -1
    iJungle = gc.getInfoTypeForString('FEATURE_JUNGLE')
    iJungleUnit = CyGame().getSorenRandNum(3, "Jungle Unit")
    for i in range (CyMap().numPlots()):
      pPlot = CyMap().plotByIndex(i)
      iPlot = -1
      if pPlot.isWater() == False:
        if pPlot.isImpassable() == False:
          if pPlot.getNumUnits() == 0:
            iPlot = CyGame().getSorenRandNum(1000, "Add Unit")
            if (pPlot.getFeatureType() == iJungle and iJungleUnit == 1):
              iPlot = iPlot + 100
            if (pPlot.isOwned() and pPlot.isBarbarian() != True):
              iPlot = iPlot / 2
            if pPlot.isVisibleEnemyUnit(biPlayer):
              iPlot = iPlot / 2
            if iPlot > iBestPlot:
              iBestPlot = iPlot
              pBestPlot = pPlot
    if iBestPlot != -1:
      bPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
      newUnit = bPlayer.initUnit(iUnit, pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
      newUnit.finishMoves()
      self.equip(newUnit)
      return newUnit


  def addBarbUnitA(self, iUnit):
    biPlayer = gc.getBARBARIAN_PLAYER()
    pBestPlot = -1
    iBestPlot = -1
    for i in range (CyMap().numPlots()):
      pPlot = CyMap().plotByIndex(i)
      iPlot = -1
      if pPlot.isWater() == False:
        if pPlot.isImpassable() == False:
          if pPlot.getNumUnits() == 0:
            iPlot = CyGame().getSorenRandNum(500, "Add Unit")
            if iPlot > iBestPlot:
              iBestPlot = iPlot
              pBestPlot = pPlot
    if iBestPlot != -1:
      bPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
      newUnit = bPlayer.initUnit(iUnit, pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
      newUnit.finishMoves()
      self.equip(newUnit)

  def unitAptitude(self, newUnit):
    iAptitude = CyGame().getSorenRandNum(6, "Aptitude") + 1
    iStrong = CyGame().getSorenRandNum(3, "Strong") + 1
    iImmortal = CyGame().getSorenRandNum(3, "Immortal") + 1
    iHero =  CyGame().getSorenRandNum(6, "Noble") + 1
    iBurglar =  CyGame().getSorenRandNum(8, "Burglar") + 1

    if iAptitude > 1:
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER1'), True)
    if iAptitude > 2:
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER2'), True)
    if iAptitude > 3:
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER3'), True)
    if iAptitude > 4:
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER4'), True)
    if iAptitude > 5:
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_EMPOWER5'), True)

    if iStrong == 1:
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG'), True)

    if iImmortal > 0 and newUnit.getOwner() != gc.getBARBARIAN_PLAYER():
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IMMORTAL'), True)

    if CyGame().getSorenRandNum(3, "Mobile") == 1:
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MOBILITY1'), True)

    if iHero == 1:
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_NOBILITY'), True)

    if iBurglar == 1:
      newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BURGLAR1'), True)

  def sDisputeLevel(self, i):
    if i < 3:
      return 'minor'
    if i < 6:
      return 'small'
    if i < 9:
      return ''
    if i < 12:
      return 'troubling'
    if i < 15:
      return 'large'
    if i < 20:
      return 'citywide'
    if i < 30:
      return 'regional'
    if i < 50:
      return 'nationwide'

    return 'global'

  def iAutoBuffRange(self,pUnit):
    iABR = pUnit.getLevel() + pUnit.getFortifyTurns()
    if iABR > pUnit.getLevel() * 2:
      iABR = pUnit.getLevel() * 2
    if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_EXTENSION1')):
      iABR = iABR * 2
    if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_EXTENSION2')):
      iABR = iABR * 2
    return iABR

  def finalWar(self):
    iPlayer = CyGame().getRankPlayer(0)
    pPlayer = gc.getPlayer(iPlayer)
    iLead = CyGame().getPlayerScore(iPlayer) - CyGame().getPlayerScore(CyGame().getRankPlayer(1))
    if (CyGame().getPlayerScore(iPlayer) >= 650 + CyGame().getPlayerScore(CyGame().getRankPlayer(1)) and (CyGame().getSorenRandNum(6, "Warn Leading Player") == 1 or CyGame().getPlayerScore(iPlayer) >= 2 * CyGame().getPlayerScore(CyGame().getRankPlayer(1)) )):
      sMsg = pPlayer.getName() + ' is pulling ahead.  There is talk of war in the taverns of the world...'
      self.msgAll(sMsg,pPlayer.getCapitalCity().getX(), pPlayer.getCapitalCity().getY(),iPlayer,'Art/Interface/Buttons/Units/Commander.dds')

      # Final War started no more often than every 15 turns
      strSetData = cPickle.loads(CyGameInstance.getScriptData())
      if strSetData['FinalWar'] > CyGame().getGameTurn() - 15:
        return

      # Computer players will declare war if a player gets too far ahead
      if (CyGame().getPlayerScore(iPlayer) >= 1000 and CyGame().getSorenRandNum(iLead, "Go To War") > 750):
        strSetData['FinalWar'] = CyGame().getGameTurn()
        CyGameInstance.setScriptData(cPickle.dumps(strSetData))
        pTeam = pPlayer.getTeam()
        for iTeam in range(gc.getMAX_CIV_TEAMS()):
          eTeam = gc.getTeam(iTeam)
          if iTeam != pPlayer.getTeam() and eTeam.isAlive() and not eTeam.isHuman() and eTeam.isAVassal() == False:
            eTeam.declareWar(pTeam, false, WarPlanTypes.WARPLAN_TOTAL)

      # Kill all enemies if a player scores over 2,000 and is twice the score of the nearest competitor
      if CyGame().getPlayerScore(iPlayer) >= 2000 and iLead > CyGame().getPlayerScore(CyGame().getRankPlayer(1)) * 2:
        pTeam = pPlayer.getTeam()
        for iTeam in range(gc.getMAX_CIV_TEAMS()):
          eTeam = gc.getTeam(iTeam)
          if iTeam != pPlayer.getTeam() and eTeam.isAlive() and not eTeam.isHuman() and eTeam.isAVassal() == False:
            for kPlayer in range(gc.getMAX_PLAYERS()):
              dPlayer = gc.getPlayer(kPlayer)
              dPlayer.killCities()
              dPlayer.killUnits()

  def iNoble(self, unit, includeArmy):
    iNob = 0
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_NOBILITY')):
      iNob += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GREAT_COMMANDER')):
      iNob += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMMANDER1')):
      iNob += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMMANDER2')):
      iNob += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMMANDER3')):
      iNob += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ESTATES1')):
      iNob += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ESTATES2')):
      iNob += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ESTATES3')):
      iNob += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GOVERNOR1')):
      iNob += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GOVERNOR2')):
      iNob += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GOVERNOR3')):
      iNob += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHIEF')):
      iNob += 1
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GRAND_MASTER')):
      iNob += 1
    if iNob > 0:
      iNob += ( unit.getLevel() / 3 )

    if includeArmy > 0:
      iArmy = 0
      pPlot = CyMap().plot(unit.getX(),unit.getY())
      for i in range(pPlot.getNumUnits()):
        pUnit = pPlot.getUnit(i)
        if pUnit.getOwner() == unit.getOwner():
          iArmy += pUnit.baseCombatStr()

      iBonus = 0
      iBonus = ( iArmy / 7 )    
      iBonus += ( unit.baseCombatStr() / 2 )
      if iBonus > iNob:
        iBonus = iNob
      
      iNob += iBonus

    return iNob

  def iValidCity(self,pPlayer):
    for i in range (pPlayer.getNumCities()):
      pCity = pPlayer.getCity(i)
      if pCity.getPopulation() > 0:
        return i
    return -1

  def setObjectInt(self,city,svar,ival):
    sSet = {}
    try:
      sSet = cPickle.loads(city.getScriptData())
    except:
      sSet = {}
    
    sSet[svar] =  ival
    city.setScriptData(cPickle.dumps(sSet))

  def changeObjectInt(self,city,svar,ival):
    sSet = {}
    try:
      sSet = cPickle.loads(city.getScriptData())
    except:
      sSet = {}
      sSet[svar] = 0
    
    if svar not in sSet:
      sSet[svar] = 0
      
    sSet[svar] = int(sSet[svar]) + ival
    city.setScriptData(cPickle.dumps(sSet))

  def getObjectInt(self,city,svar):
    try:
      iGet = cPickle.loads(city.getScriptData())
    except:
      return 0
      
    if svar not in iGet:
      return 0
      
    return iGet[svar]

  def setObjectStr(self,city,svar,sval):
    try:
      sSet = cPickle.loads(city.getScriptData())
    except:
      sSet = {}
    
    sSet[svar] = sval
    city.setScriptData(cPickle.dumps(sSet))

  def getObjectStr(self,city,svar):
    try:
      sGet = cPickle.loads(city.getScriptData())
    except:
      return ''
      
    if svar not in sGet:
      return ''
      
    return sGet[svar]

  def setGameVar(self,svar,sval):
    try:
      sSet = cPickle.loads(CyGameInstance.getScriptData())
    except:
      sSet = {}
      
    sSet[svar] =  sval
    CyGameInstance.setScriptData(cPickle.dumps(sSet))

  def getGameVar(self,svar):
    try:
      sGet = cPickle.loads(CyGameInstance.getScriptData())
    except:
      return ''
      
    if svar not in sGet:
      return ''
      
    return sGet[svar]
    
  ### FW Changes above

  def addBonus(self, iBonus, iNum, sIcon):
    listPlots = []
    for i in range (CyMap().numPlots()):
      pPlot = CyMap().plotByIndex(i)
      if (pPlot.canHaveBonus(gc.getInfoTypeForString(iBonus),True) and pPlot.getBonusType(-1) == -1 and pPlot.isCity() == False):
        listPlots.append(i)
    if len(listPlots) > 0:
      for i in range (iNum):
        iRnd = CyGame().getSorenRandNum(len(listPlots), "Add Bonus")
        pPlot = CyMap().plotByIndex(listPlots[iRnd])
        pPlot.setBonusType(gc.getInfoTypeForString(iBonus))
        if sIcon != -1:
          iActivePlayer = CyGame().getActivePlayer()
          CyInterface().addMessage(iActivePlayer,True,25,CyTranslator().getText("TXT_KEY_MESSAGE_RESOURCE_DISCOVERED",()),'AS2D_DISCOVERBONUS',1,sIcon,ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)

  def addPopup(self, szText, sDDS):
    szTitle = CyGameTextMgr().getTimeStr(CyGame().getGameTurn(), false)
    popup = PyPopup.PyPopup(-1)
    popup.addDDS(sDDS, 0, 0, 128, 384)
    popup.addSeparator()
    popup.setHeaderString(szTitle)
    popup.setBodyString(szText)
    popup.launch(true, PopupStates.POPUPSTATE_IMMEDIATE)

  def addPlayerPopup(self, szText, iPlayer):
    popupInfo = CyPopupInfo()
    popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
    popupInfo.setText(szText)
    popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_CLOSE", ()), "")
    popupInfo.addPopup(iPlayer)

  # def addUnit(self, iUnit):
    # pBestPlot = -1
    # iBestPlot = -1
    # for i in range (CyMap().numPlots()):
      # pPlot = CyMap().plotByIndex(i)
      # iPlot = -1
      # if pPlot.isWater() == False:
        # if pPlot.getNumUnits() == 0:
          # if pPlot.isCity() == False:
            # if pPlot.isImpassable() == False:
              # iPlot = CyGame().getSorenRandNum(500, "Add Unit")
              # iPlot = iPlot + (pPlot.area().getNumTiles() * 10)
              # if pPlot.isBarbarian():
                # iPlot = iPlot + 200
              # if pPlot.isOwned():
                # iPlot = iPlot / 2
              # if iPlot > iBestPlot:
                # iBestPlot = iPlot
                # pBestPlot = pPlot
    if iBestPlot != -1:
      bPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
      newUnit = bPlayer.initUnit(iUnit, pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)

  def addUnitFixed(self, caster, iUnit):
    pPlot = caster.plot()
    pNewPlot = self.findClearPlot(-1, pPlot)
    if pNewPlot != -1:
      pPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
      newUnit = pPlayer.initUnit(iUnit, pNewPlot.getX(), pNewPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
      return newUnit
    return -1

  def doCrusade(self, iPlayer):
    iCrusadeChance = gc.getDefineINT('CRUSADE_SPAWN_CHANCE')
    iDemagog = gc.getInfoTypeForString('UNIT_DEMAGOG')
    iTown = gc.getInfoTypeForString('IMPROVEMENT_TOWN')
    iVillage = gc.getInfoTypeForString('IMPROVEMENT_VILLAGE')
    pPlayer = gc.getPlayer(iPlayer)
    for i in range (CyMap().numPlots()):
      pPlot = CyMap().plotByIndex(i)
      if pPlot.getImprovementType() == iTown:
        if pPlot.getOwner() == iPlayer:
          if CyGame().getSorenRandNum(100, "Crusade") < iCrusadeChance:
            newUnit = pPlayer.initUnit(iDemagog, pPlot.getX(), pPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
            pPlot.setImprovementType(iVillage)

  def doFear(self, pVictim, pPlot, pCaster, bResistable):
    #mtk
    return False
    if pVictim.isImmuneToFear():
      return False
    if bResistable:
      if CyGame().getSorenRandNum(100, "Crusade") < pVictim.getResistChance(pCaster, gc.getInfoTypeForString('SPELL_ROAR')):
        return False
    iX = pVictim.getX()
    iY = pVictim.getY()
    pBestPlot = -1
    iBestPlot = 0
    for iiX in range(iX-1, iX+2, 1):
      for iiY in range(iY-1, iY+2, 1):
        pLoopPlot = CyMap().plot(iiX,iiY)
        if not pLoopPlot.isNone():
          if not pLoopPlot.isVisibleEnemyUnit(pVictim.getOwner()):
            if pVictim.canMoveOrAttackInto(pLoopPlot, False):
              if (abs(pLoopPlot.getX() - pPlot.getX())>1) or (abs(pLoopPlot.getY() - pPlot.getY())>1):
                iRnd = CyGame().getSorenRandNum(500, "Fear")
                if iRnd > iBestPlot:
                  iBestPlot = iRnd
                  pBestPlot = pLoopPlot
    if pBestPlot != -1:
      pVictim.setXY(pBestPlot.getX(), pBestPlot.getY(), false, true, true)
      return True
    return False

  def exploreLairBigBad(self, caster):
    iPlayer = caster.getOwner()
    pPlot = caster.plot()
    pPlayer = gc.getPlayer(caster.getOwner())

    lList = ['UNIT_AZER']
    lPromoList = ['PROMOTION_MUTATED', 'PROMOTION_CANNIBALIZE', 'PROMOTION_MOBILITY1', 'PROMOTION_STRONG', 'PROMOTION_BLITZ', 'PROMOTION_COMMAND1', 'PROMOTION_HEROIC_STRENGTH', 'PROMOTION_HEROIC_DEFENSE', 'PROMOTION_MAGIC_IMMUNE', 'PROMOTION_STONESKIN', 'PROMOTION_VALOR', 'PROMOTION_VILE_TOUCH']
    lHenchmanList = ['UNIT_AZER', 'UNIT_GRIFFON']
    if self.grace() == False:
      lList = lList + ['UNIT_AIR_ELEMENTAL']
    if not pPlot.isWater():
      lList = lList + ['UNIT_ASSASSIN', 'UNIT_OGRE', 'UNIT_GIANT_SPIDER', 'UNIT_HILL_GIANT', 'UNIT_SPECTRE', 'UNIT_SCORPION']
      lHenchmanList = lHenchmanList + ['UNIT_AXEMAN', 'UNIT_WOLF', 'UNIT_CHAOS_MARAUDER', 'UNIT_WOLF_RIDER', 'UNIT_MISTFORM', 'UNIT_LION', 'UNIT_TIGER', 'UNIT_BABY_SPIDER', 'UNIT_FAWN', 'UNIT_SCORPION']
      if self.grace() == False:
        lList = lList + ['UNIT_EARTH_ELEMENTAL', 'UNIT_FIRE_ELEMENTAL', 'UNIT_GARGOYLE', 'UNIT_VAMPIRE', 'UNIT_MYCONID', 'UNIT_EIDOLON', 'UNIT_LICH', 'UNIT_OGRE_WARCHIEF', 'UNIT_SATYR', 'UNIT_WEREWOLF']
        lPromoList = lPromoList + ['PROMOTION_FIRE2', 'PROMOTION_AIR2', 'PROMOTION_HERO', 'PROMOTION_MARKSMAN', 'PROMOTION_SHADOWWALK']
        lHenchmanList = lHenchmanList + ['UNIT_OGRE']
        if pPlot.getFeatureType() == gc.getInfoTypeForString('FEATURE_FOREST'):
          lList = lList + ['UNIT_TREANT']
      if pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_SNOW'):
        lHenchmanList = lHenchmanList + ['UNIT_FROSTLING_ARCHER', 'UNIT_FROSTLING_WOLF_RIDER', 'UNIT_POLAR_BEAR']
      if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_BARROW'):
        lPromoList = lPromoList + ['PROMOTION_DEATH2']
        lHenchmanList = lHenchmanList + ['UNIT_SKELETON', 'UNIT_PYRE_ZOMBIE']
        if self.grace() == False:
          lList = lList + ['UNIT_WRAITH']
      if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_RUINS'):
        lPromoList = lPromoList + ['PROMOTION_POISONED_BLADE']
        lHenchmanList = lHenchmanList + ['UNIT_LIZARDMAN', 'UNIT_GORILLA']
        if self.grace() == False:
          lList = lList + ['UNIT_MANTICORE']
      if CyGame().getGlobalCounter() > 40:
        lList = lList + ['UNIT_PIT_BEAST', 'UNIT_DEATH_KNIGHT', 'UNIT_BALOR']
        lPromoList = lPromoList + ['PROMOTION_FEAR']
        lHenchmanList = lHenchmanList + ['UNIT_IMP', 'UNIT_HELLHOUND']
    if pPlot.isWater():
      lList = lList + ['UNIT_SEA_SERPENT', 'UNIT_STYGIAN_GUARD', 'UNIT_PIRATE']
      lHenchmanList = lHenchmanList + ['UNIT_DROWN']
      if self.grace() == False:
        lList = lList + ['UNIT_WATER_ELEMENTAL', 'UNIT_KRAKEN']

    sMonster = lList[CyGame().getSorenRandNum(len(lList), "Pick Monster")-1]
    sHenchman = lHenchmanList[CyGame().getSorenRandNum(len(lHenchmanList), "Pick Henchman")-1]
    sPromo = lPromoList[CyGame().getSorenRandNum(len(lPromoList), "Pick Promotion")-1]
    iUnit = gc.getInfoTypeForString(sMonster)
    iHenchman = gc.getInfoTypeForString(sHenchman)
    newUnit = self.addUnitFixed(caster,iUnit)
    if newUnit != -1:
      newUnit.setHasPromotion(gc.getInfoTypeForString(sPromo), True)
      newUnit.setName(self.MarnokNameGenerator(newUnit))
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BIGBAD",()),'',1,gc.getUnitInfo(iUnit).getButton(),ColorTypes(7),newUnit.getX(),newUnit.getY(),True,True)
      bPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
      for i in range (CyGame().getSorenRandNum(5, "Pick Henchmen")):
        bPlayer.initUnit(iHenchman, newUnit.getX(), newUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
    return 0

  def exploreLairBad(self, caster):
    iPlayer = caster.getOwner()
    pPlot = caster.plot()
    pPlayer = gc.getPlayer(caster.getOwner())

    lList = ['COLLAPSE']
    if caster.getLevel() == 1:
      lList = lList + ['DEATH']
    if caster.isAlive():
      lList = lList + ['CRAZED', 'DEMONIC_POSSESSION', 'DISEASED', 'ENRAGED', 'PLAGUED', 'POISONED', 'WITHERED']
    if caster.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_MELEE'):
      lList = lList + ['RUSTED']
    if pPlot.isWater():
      lList = lList + ['SPAWN_DROWN', 'SPAWN_SEA_SERPENT']
    if not pPlot.isWater():
      lList = lList + ['SPAWN_SPIDER', 'SPAWN_SPECTRE']
    if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_GOBLIN_FORT'):
      lList = lList + ['SPAWN_SCORPION_BAD', 'SPAWN_SCORPION_BAD', 'SPAWN_SCORPION_BAD']

    sGoody = lList[CyGame().getSorenRandNum(len(lList), "Pick Goody")-1]
    if sGoody == 'DEATH':
      caster.kill(True,0)
      CyInterface().addMessage(caster.getOwner(),False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_DEATH", ()),'',1,'Art/Interface/Buttons/Spells/Explore Lair.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
      return 0
    if sGoody == 'COLLAPSE':
      caster.doDamageNoCaster(50, 90, gc.getInfoTypeForString('DAMAGE_PHYSICAL'), false)
      CyInterface().addMessage(caster.getOwner(),False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_COLLAPSE", ()),'',1,'Art/Interface/Buttons/Spells/Explore Lair.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'CRAZED':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CRAZED'), True)
      CyInterface().addMessage(caster.getOwner(),False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_CRAZED", ()),'',1,'Art/Interface/Buttons/Promotions/Crazed.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
      return 80
    if sGoody == 'DEMONIC_POSSESSION':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENRAGED'), True)
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CRAZED'), True)
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
      CyInterface().addMessage(caster.getOwner(),False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_POSSESSED", ()),'',1,'Art/Interface/Buttons/Units/UCDemon.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
      return 80
    if sGoody == 'DISEASED':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DISEASED'), True)
      CyInterface().addMessage(caster.getOwner(),False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_DISEASED", ()),'',1,'Art/Interface/Buttons/Promotions/Diseased.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
      return 80
    if sGoody == 'ENRAGED':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENRAGED'), True)
      CyInterface().addMessage(caster.getOwner(),False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_ENRAGED", ()),'',1,'Art/Interface/Buttons/Promotions/Enraged.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
      return 80   
    if sGoody == 'PLAGUED':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED'), True)
      CyInterface().addMessage(caster.getOwner(),False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_PLAGUED", ()),'',1,'Art/Interface/Buttons/Promotions/Plagued.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
      return 80
    if sGoody == 'POISONED':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED'), True)
      caster.doDamageNoCaster(25, 90, gc.getInfoTypeForString('DAMAGE_POISON'), false)
      CyInterface().addMessage(caster.getOwner(),False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_POISONED", ()),'',1,'Art/Interface/Buttons/Promotions/Poisoned.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
      return 80
    if sGoody == 'WITHERED':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WITHERED'), True)
      CyInterface().addMessage(caster.getOwner(),False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_WITHERED", ()),'',1,'Art/Interface/Buttons/Promotions/Withered.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
      return 80
    if sGoody == 'RUSTED':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RUSTED'), True)
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), False)
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), False)
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MITHRIL_WEAPONS'), False)
      CyInterface().addMessage(caster.getOwner(),False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_RUSTED", ()),'',1,'Art/Interface/Buttons/Promotions/Rusted.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
      return 80
    if sGoody == 'SPAWN_DROWN':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_DROWN'), caster)
      return 50
    if sGoody == 'SPAWN_SCORPION_BAD':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SCORPION_BAD'), caster)
      return 50
    if sGoody == 'SPAWN_SEA_SERPENT':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SEA_SERPENT'), caster)
      return 50
    if sGoody == 'SPAWN_SPECTRE':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_GRAVE_SPECTRE'), caster)
      return 50
    if sGoody == 'SPAWN_SPIDER':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SPIDER'), caster)
      return 50
    return 100

  def exploreLairNeutral(self, caster):
    iPlayer = caster.getOwner()
    pPlot = caster.plot()
    pPlayer = gc.getPlayer(caster.getOwner())
    lList = ['NOTHING']
    if not pPlot.isWater():
      lList = lList + ['SPAWN_SKELETON', 'SPAWN_LIZARDMAN', 'SPAWN_SPIDER', 'PORTAL', 'DEPTHS', 'DWARF_VS_LIZARDMEN', 'CAGE']
      if pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_SNOW'):
        lList = lList + ['SPAWN_FROSTLING']
      if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_BARROW'):
        lList = lList + ['SPAWN_SKELETON', 'SPAWN_SKELETON']
      if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_RUINS'):
        lList = lList + ['SPAWN_LIZARDMAN', 'SPAWN_LIZARDMAN']
      if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_GOBLIN_FORT'):
        lList = lList + ['SPAWN_SCORPION', 'SPAWN_SCORPION', 'SPAWN_SCORPION']
    if pPlot.isWater():
      lList = lList + ['SPAWN_DROWN']
    if caster.isAlive():
      if not caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MUTATED')):
        lList = lList + ['MUTATED']
    
    sGoody = lList[CyGame().getSorenRandNum(len(lList), "Pick Goody")-1]
    if sGoody == 'CAGE':
      pPlot.setImprovementType(gc.getInfoTypeForString('IMPROVEMENT_CAGE'))
      for i in range(pPlot.getNumUnits(), -1, -1):
        pUnit = pPlot.getUnit(i)
        pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HELD'), True)
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_CAGE",()),'',1,'Art/Interface/Buttons/Improvements/Cage.dds',ColorTypes(7),caster.getX(),caster.getY(),True,True)
      return 0
    if sGoody == 'DEPTHS':
      iUnitID = self.getUnitPlayerID(caster)
      if iUnitID != -1:
        iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(),'EVENTTRIGGER_EXPLORE_LAIR_DEPTHS')
        triggerData = pPlayer.initTriggeredData(iEvent, true, -1, caster.getX(), caster.getY(), caster.getOwner(), -1, -1, -1, iUnitID, -1)
      return 100
    if sGoody == 'DWARF_VS_LIZARDMEN':
      iUnitID = self.getUnitPlayerID(caster)
      if iUnitID != -1:
        iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(),'EVENTTRIGGER_EXPLORE_LAIR_DWARF_VS_LIZARDMEN')
        triggerData = pPlayer.initTriggeredData(iEvent, true, -1, caster.getX(), caster.getY(), caster.getOwner(), -1, -1, -1, iUnitID, -1)
      return 100
    if sGoody == 'MUTATED':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MUTATED'), True)
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_MUTATED",()),'',1,'Art/Interface/Buttons/Promotions/Mutated.dds',ColorTypes(7),caster.getX(),caster.getY(),True,True)
      return 50
    if sGoody == 'NOTHING':
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_NOTHING",()),'',1,'Art/Interface/Buttons/Spells/Explore Lair.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'PORTAL':
      iUnitID = self.getUnitPlayerID(caster)
      if iUnitID != -1:
        iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(),'EVENTTRIGGER_EXPLORE_LAIR_PORTAL')
        triggerData = pPlayer.initTriggeredData(iEvent, true, -1, caster.getX(), caster.getY(), caster.getOwner(), -1, -1, -1, iUnitID, -1)
      return 0
    if sGoody == 'SPAWN_DROWN':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_DROWN'), caster)
      return 50
    if sGoody == 'SPAWN_FROSTLING':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_FROSTLING'), caster)
      return 50
    if sGoody == 'SPAWN_LIZARDMAN':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_LIZARDMAN'), caster)
      return 50
    if sGoody == 'SPAWN_SCORPION':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SCORPION'), caster)
      return 50
    if sGoody == 'SPAWN_SKELETON':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SKELETON'), caster)
      return 50
    if sGoody == 'SPAWN_SPIDER':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SPIDER'), caster)
      return 50
    return 100

  def exploreLairGood(self, caster):
    iPlayer = caster.getOwner()
    pPlot = caster.plot()
    pPlayer = gc.getPlayer(caster.getOwner())
    lList = ['HIGH_GOLD', 'TREASURE', 'EXPERIENCE']
    if caster.isAlive():
      if not caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE')):
        lList = lList + ['SPIRIT_GUIDE']
    if not pPlot.isWater():
      lList = lList + ['ITEM_HEALING_SALVE', 'SUPPLIES']
      if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_MYSTICISM')):
        lList = lList + ['PRISONER_DISCIPLE_ASHEN', 'PRISONER_DISCIPLE_EMPYREAN', 'PRISONER_DISCIPLE_LEAVES', 'PRISONER_DISCIPLE_OVERLORDS', 'PRISONER_DISCIPLE_RUNES', 'PRISONER_DISCIPLE_ORDER']
    if caster.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_MELEE'):
      if not caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ENCHANTED_BLADE')):
        lList = lList + ['ENCHANTED_BLADE']
    if caster.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ADEPT'):
      if not caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SPELLSTAFF')):
        lList = lList + ['SPELLSTAFF']
    if caster.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_RECON'):
      if not caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED_BLADE')):
        lList = lList + ['POISONED_BLADE']
    if caster.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ARCHER'):
      if not caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FLAMING_ARROWS')):
        lList = lList + ['FLAMING_ARROWS']
    if caster.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_DISCIPLE'):
      if not caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SHIELD_OF_FAITH')):
        lList = lList + ['SHIELD_OF_FAITH']
    if gc.getUnitInfo(caster.getUnitType()).getWeaponTier() >= 1:
      if not caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MITHRIL_WEAPONS')):
        if (gc.getUnitInfo(caster.getUnitType()).getWeaponTier() >= 3 and pPlayer.isHasTech(gc.getInfoTypeForString('TECH_IRON_WORKING'))):
          lList = lList + ['MITHRIL_WEAPONS']
        if not caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS')):
          if (gc.getUnitInfo(caster.getUnitType()).getWeaponTier() >= 2 and pPlayer.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING'))):
            lList = lList + ['IRON_WEAPONS']
          if not caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS')):
            lList = lList + ['BRONZE_WEAPONS']

    sGoody = lList[CyGame().getSorenRandNum(len(lList), "Pick Goody")-1]
    if sGoody == 'HIGH_GOLD':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_HIGH_GOLD'), caster)
      return 90
    if sGoody == 'SUPPLIES':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SUPPLIES'), caster)
      return 100
    if sGoody == 'TREASURE':
      self.placeTreasure(iPlayer, gc.getInfoTypeForString('EQUIPMENT_TREASURE'))
      return 80
    if sGoody == 'EXPERIENCE':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_EXPERIENCE'), caster)
      return 100
    if sGoody == 'SPIRIT_GUIDE':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE'), True)
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_SPIRIT_GUIDE",()),'AS2D_POSITIVE_DINK',1,'Art/Interface/Buttons/Promotions/SpiritGuide.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 80
    if sGoody == 'ITEM_HEALING_SALVE':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_HEALING_SALVE'), caster)
      return 100
    if sGoody == 'ITEM_POTION_OF_INVISIBILITY':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_POTION_OF_INVISIBILITY'), caster)
      return 100
    if sGoody == 'ITEM_POTION_OF_RESTORATION':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_POTION_OF_RESTORATION'), caster)
      return 100
    if sGoody == 'ENCHANTED_BLADE':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENCHANTED_BLADE'), True)
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_ENCHANTED_BLADE",()),'',1,'Art/Interface/Buttons/Promotions/EnchantedBlade.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'SPELLSTAFF':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SPELLSTAFF'), True)
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_SPELLSTAFF",()),'',1,'Art/Interface/Buttons/Promotions/Spellstaff.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'POISONED_BLADE':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED_BLADE'), True)
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_POISONED_BLADE",()),'',1,'Art/Interface/Buttons/Promotions/PoisonedBlade.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'FLAMING_ARROWS':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FLAMING_ARROWS'), True)
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_FLAMING_ARROWS",()),'AS2D_POSITIVE_DINK',1,'Art/Interface/Buttons/Promotions/FlamingArrows.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'PRISONER_DISCIPLE_ASHEN':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_DISCIPLE_ASHEN'), caster)
      return 100      
    if sGoody == 'PRISONER_DISCIPLE_EMPYREAN':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_DISCIPLE_EMPYREAN'), caster)
      return 100      
    if sGoody == 'PRISONER_DISCIPLE_LEAVES':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_DISCIPLE_LEAVES'), caster)
      return 100      
    if sGoody == 'PRISONER_DISCIPLE_OVERLORDS':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_DISCIPLE_OVERLORDS'), caster)
      return 100      
    if sGoody == 'PRISONER_DISCIPLE_RUNES':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_DISCIPLE_RUNES'), caster)
      return 100      
    if sGoody == 'PRISONER_DISCIPLE_ORDER':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_DISCIPLE_ORDER'), caster)
      return 100      
    if sGoody == 'SHIELD_OF_FAITH':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SHIELD_OF_FAITH'), True)
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_SHIELD_OF_FAITH",()),'',1,'Art/Interface/Buttons/Promotions/ShieldOfFaith.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'BRONZE_WEAPONS':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), True)
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BRONZE_WEAPONS",()),'',1,'Art/Interface/Buttons/Promotions/BronzeWeapons.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      if caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_RUSTED')) == True:
        caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RUSTED'),False)
      return 100
    if sGoody == 'IRON_WEAPONS':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), True)
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), False)
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_IRON_WEAPONS",()),'',1,'Art/Interface/Buttons/Promotions/IronWeapons.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      if caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_RUSTED')) == True:
        caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RUSTED'),False)
      return 100
    if sGoody == 'MITHRIL_WEAPONS':
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MITHRIL_WEAPONS'), True)
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), False)
      caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), False)
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_MITHRIL_WEAPONS",()),'',1,'Art/Interface/Buttons/Promotions/MithrilWeapons.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      if caster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_RUSTED')) == True:
        caster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RUSTED'),False)
      return 100
    return 100

  def exploreLairBigGood(self, caster):
    iPlayer = caster.getOwner()
    pPlot = caster.plot()
    pPlayer = gc.getPlayer(caster.getOwner())

    lList = ['TREASURE_VAULT', 'GOLDEN_AGE']
    if pPlayer.canReceiveGoody(pPlot, gc.getInfoTypeForString('GOODY_GRAVE_TECH'), caster):
      lList = lList + ['TECH']
    if not pPlot.isWater():
      lList = lList + ['ITEM_JADE_TORC', 'ITEM_ROD_OF_WINDS', 'ITEM_TIMOR_MASK', 'PRISONER_ADVENTURER', 'PRISONER_ARTIST', 'PRISONER_COMMANDER', 'PRISONER_ENGINEER', 'PRISONER_MERCHANT', 'PRISONER_PROPHET', 'PRISONER_SCIENTIST']
      if pPlot.getBonusType(-1) == -1:
        lList = lList + ['BONUS_MANA']
        if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_MINING')):
          lList = lList + ['BONUS_COPPER', 'BONUS_GEMS', 'BONUS_GOLD']
        if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_SMELTING')):
          lList = lList + ['BONUS_IRON']
    if pPlot.isWater():
      lList = lList + ['PRISONER_SEA_SERPENT']
      if pPlot.getBonusType(-1) == -1:
        lList = lList + ['BONUS_CLAM', 'BONUS_CRAB', 'BONUS_FISH']
    if self.grace() == False:
      lList = lList + ['PRISONER_ANGEL', 'PRISONER_MONK', 'PRISONER_ASSASSIN', 'PRISONER_CHAMPION', 'PRISONER_MAGE']
    sGoody = lList[CyGame().getSorenRandNum(len(lList), "Pick Goody")-1]

    if sGoody == 'TREASURE_VAULT':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_TREASURE_VAULT'), caster)
      return 100  
    if sGoody == 'BONUS_CLAM':
      pPlot.setBonusType(gc.getInfoTypeForString('BONUS_CLAM'))
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_CLAM",()),'',1,'Art/Interface/Buttons/WorldBuilder/Clam.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'BONUS_COPPER':
      pPlot.setBonusType(gc.getInfoTypeForString('BONUS_COPPER'))
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_COPPER",()),'',1,'Art/Interface/Buttons/WorldBuilder/Copper.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'BONUS_CRAB':
      pPlot.setBonusType(gc.getInfoTypeForString('BONUS_CRAB'))
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_CRAB",()),'',1,'Art/Interface/Buttons/WorldBuilder/Crab.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'BONUS_FISH':
      pPlot.setBonusType(gc.getInfoTypeForString('BONUS_FISH'))
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_FISH",()),'',1,'Art/Interface/Buttons/WorldBuilder/Fish.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'BONUS_GOLD':
      pPlot.setBonusType(gc.getInfoTypeForString('BONUS_GOLD'))
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_GOLD",()),'',1,'Art/Interface/Buttons/WorldBuilder/Gold.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'BONUS_GEMS':
      pPlot.setBonusType(gc.getInfoTypeForString('BONUS_GEMS'))
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_GEMS",()),'',1,'Art/Interface/Buttons/WorldBuilder/Gems.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'BONUS_IRON':
      pPlot.setBonusType(gc.getInfoTypeForString('BONUS_IRON'))
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_IRON",()),'',1,'Art/Interface/Buttons/WorldBuilder/Iron.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'BONUS_MANA':
      pPlot.setBonusType(gc.getInfoTypeForString('BONUS_MANA'))
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_MANA",()),'',1,'Art/Interface/Buttons/WorldBuilder/mana_button.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'GOLDEN_AGE':
      pPlayer.changeGoldenAgeTurns(CyGame().goldenAgeLength())
      CyInterface().addMessage(iPlayer,False,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_GOLDEN_AGE",()),'',1,'Art/Interface/Buttons/Spells/Explore Lair.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)
      return 100
    if sGoody == 'ITEM_JADE_TORC':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_JADE_TORC'), caster)
      return 100
    if sGoody == 'ITEM_ROD_OF_WINDS':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_ROD_OF_WINDS'), caster)
      return 100
    if sGoody == 'ITEM_TIMOR_MASK':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_TIMOR_MASK'), caster)
      return 100
    if sGoody == 'PRISONER_ADVENTURER':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_ADVENTURER'), caster)
      return 100      
    if sGoody == 'PRISONER_ANGEL':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_ANGEL'), caster)
      return 100      
    if sGoody == 'PRISONER_ARTIST':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_ARTIST'), caster)
      return 100
    if sGoody == 'PRISONER_ASSASSIN':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_ASSASSIN'), caster)
      return 100
    if sGoody == 'PRISONER_CHAMPION':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_CHAMPION'), caster)
      return 100
    if sGoody == 'PRISONER_COMMANDER':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_COMMANDER'), caster)
      return 100  
    if sGoody == 'PRISONER_ENGINEER':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_ENGINEER'), caster)
      return 100  
    if sGoody == 'PRISONER_MAGE':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_MAGE'), caster)
      return 100
    if sGoody == 'PRISONER_MERCHANT':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_MERCHANT'), caster)
      return 100  
    if sGoody == 'PRISONER_MONK':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_MONK'), caster)
      return 100      
    if sGoody == 'PRISONER_PROPHET':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_PROPHET'), caster)
      return 100  
    if sGoody == 'PRISONER_SEA_SERPENT':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_SEA_SERPENT'), caster)
      return 100  
    if sGoody == 'PRISONER_SCIENTIST':
      pPlayer.receiveGoody(pPlot,gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_SCIENTIST'), caster)
      return 100
    if sGoody == 'TECH':
      pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_GRAVE_TECH'), caster)
      return 100
    return 100    

  def formEmpire(self, iCiv, iLeader, iTeam, pCity, iAlignment, pFromPlayer):
    iPlayer = self.getOpenPlayer()
    pPlot = pCity.plot()
    pPlot2 = self.findClearPlot(-1, pCity.plot())
    if (iPlayer != -1 and pPlot2 != -1):
      for i in range(pPlot.getNumUnits(), -1, -1):
        pUnit = pPlot.getUnit(i)
        pUnit.setXY(pPlot2.getX(), pPlot2.getY(), true, true, true)
      CyGame().addPlayerAdvanced(iPlayer, iTeam, iLeader, iCiv)
      pPlayer = gc.getPlayer(iPlayer)
      pPlayer.acquireCity(pCity, False, False)
      pCity = pPlot.getPlotCity()
      pCity.changeCulture(iPlayer, 100, True)
      pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ARCHER'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
      pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ARCHER'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
      pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ARCHER'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
      pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ARCHER'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
      pPlayer.initUnit(gc.getInfoTypeForString('UNIT_WORKER'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
      if iAlignment != -1:
        pPlayer.setAlignment(iAlignment)
      if pFromPlayer != -1:
        eFromTeam = gc.getTeam(pFromPlayer.getTeam())
        eTeam = gc.getTeam(pPlayer.getTeam())
        for iTech in range(gc.getNumTechInfos()):
          if eFromTeam.isHasTech(iTech):
            eTeam.setHasTech(iTech, true, iPlayer, true, false)

  def grace(self):
    iGrace = 20 * (int(CyGame().getGameSpeedType()) + 1)
    iDiff = gc.getNumHandicapInfos() + 1 - int(gc.getGame().getHandicapType())
    iGrace = iGrace * iDiff
    iGrace = CyGame().getSorenRandNum(iGrace, "grace") + iGrace
    if iGrace > CyGame().getGameTurn():
      return True
    return False

  def doCityFire(self, pCity):
    iCount = 0
    iDemon = gc.getInfoTypeForString('BUILDING_DEMONIC_CITIZENS')
    for iBuilding in range(gc.getNumBuildingInfos()):
      if iBuilding != iDemon:
        if pCity.getNumRealBuilding(iBuilding) > 0:
          if gc.getBuildingInfo(iBuilding).getConquestProbability() != 100:
            if CyGame().getSorenRandNum(100, "City Fire") <= 10:
              pCity.setNumRealBuilding(iBuilding, 0)
              CyInterface().addMessage(pCity.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_CITY_FIRE",(gc.getBuildingInfo(iBuilding).getDescription(), )),'',1,gc.getBuildingInfo(iBuilding).getButton(),ColorTypes(8),pCity.getX(),pCity.getY(),True,True)
              iCount += 1
    if iCount == 0:
      CyInterface().addMessage(pCity.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_CITY_FIRE_NO_DAMAGE",()),'AS2D_SPELL_FIRE_ELEMENTAL',1,'Art/Interface/Buttons/Fire.dds',ColorTypes(8),pCity.getX(),pCity.getY(),True,True)

  def doHellTerrain(self):
    iCount = CyGame().getGlobalCounter()
    iGameTurn = CyGame().getGameTurn()
    iAshenVeil = gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL')
    iBurningSands = gc.getInfoTypeForString('TERRAIN_BURNING_SANDS')
    iSnow = gc.getInfoTypeForString('TERRAIN_SNOW')
    iBanana = gc.getInfoTypeForString('BONUS_BANANA')
    iCotton = gc.getInfoTypeForString('BONUS_COTTON')
    iCorn = gc.getInfoTypeForString('BONUS_CORN')
    iCow = gc.getInfoTypeForString('BONUS_COW')
    iEvil = gc.getInfoTypeForString('ALIGNMENT_EVIL')
    iFarm = gc.getInfoTypeForString('IMPROVEMENT_FARM')
    iFlames = gc.getInfoTypeForString('FEATURE_FLAMES')
    iFlamesSpreadChance = gc.getDefineINT('FLAMES_SPREAD_CHANCE')
    iGulagarm = gc.getInfoTypeForString('BONUS_GULAGARM')
    iHorse = gc.getInfoTypeForString('BONUS_HORSE')
    iInfernal = gc.getInfoTypeForString('CIVILIZATION_INFERNAL')
    iMarble = gc.getInfoTypeForString('BONUS_MARBLE')
    iNeutral = gc.getInfoTypeForString('ALIGNMENT_NEUTRAL')
    iNightmare = gc.getInfoTypeForString('BONUS_NIGHTMARE')
    iPig = gc.getInfoTypeForString('BONUS_PIG')
    iRazorweed = gc.getInfoTypeForString('BONUS_RAZORWEED')
    iRice = gc.getInfoTypeForString('BONUS_RICE')
    iSheep = gc.getInfoTypeForString('BONUS_SHEEP')
    iSheutStone = gc.getInfoTypeForString('BONUS_SHEUT_STONE')
    iSilk = gc.getInfoTypeForString('BONUS_SILK')
    iSnakePillar = gc.getInfoTypeForString('IMPROVEMENT_SNAKE_PILLAR')
    iSugar = gc.getInfoTypeForString('BONUS_SUGAR')
    iToad = gc.getInfoTypeForString('BONUS_TOAD')
    iWheat = gc.getInfoTypeForString('BONUS_WHEAT')
    iJungle = gc.getInfoTypeForString('FEATURE_JUNGLE')
    iForestBurnt = gc.getInfoTypeForString('FEATURE_FOREST_BURNT')
    iReagents = gc.getInfoTypeForString('BONUS_REAGENTS')
    iGunPowder = gc.getInfoTypeForString('BONUS_GUNPOWDER')
    iAncientForest = gc.getInfoTypeForString('FEATURE_FOREST_ANCIENT')
    iAncientForestChance = gc.getDefineINT('ANCIENT_FOREST_CHANCE')
    iDesert = gc.getInfoTypeForString('TERRAIN_DESERT')
    iOcean = gc.getInfoTypeForString('TERRAIN_OCEAN')
    iGrass = gc.getInfoTypeForString('TERRAIN_GRASS')
    
    ### FW Changes
    iAdj = 0
    iCache = 20

    if CyMap().getWorldSize() == gc.getInfoTypeForString('WORLDSIZE_DUEL'):
      iAdj = 6
      iCache = 8
    if CyMap().getWorldSize() == gc.getInfoTypeForString('WORLDSIZE_TINY'):
      iAdj = 4
      iCache = 12
    if CyMap().getWorldSize() == gc.getInfoTypeForString('WORLDSIZE_SMALL'):
      iAdj = 2
      iCache = 16
    if CyMap().getWorldSize() == gc.getInfoTypeForString('WORLDSIZE_LARGE'):
      iAdj = -1
      iCache = 24
    if CyMap().getWorldSize() == gc.getInfoTypeForString('WORLDSIZE_HUGE'):
      iAdj = -2
      iCache = 36

    if CyGame().getGameSpeedType() == gc.getInfoTypeForString('GAMESPEED_NORMAL'):
      iAdj = iAdj + 4
    if CyGame().getGameSpeedType() == gc.getInfoTypeForString('GAMESPEED_EPIC'):
      iAdj = iAdj + 8
    if CyGame().getGameSpeedType() == gc.getInfoTypeForString('GAMESPEED_MARATHON'):
      iAdj = iAdj + 12
      
    if self.bTechExist('TECH_INFERNAL_PACT') == False and CyGame().getSorenRandNum(6+iAdj, "AnimalStuff") == 1:
      self.addUnit(gc.getInfoTypeForString(self.sAnimalUnit()))
    if CyGame().getSorenRandNum(4+iAdj, "BarbarianStuff") == 1:
      self.addBarbUnit(gc.getInfoTypeForString(self.sBarbUnit()))
    if iGameTurn < iCache:
      self.addBarbUnitA(gc.getInfoTypeForString('UNIT_HIDDEN_CACHE'))
    if self.bTechExist('TECH_NECROMANCY') and CyGame().getSorenRandNum(4+iAdj, "UndeadStuff") == 1:
      self.addBarbUnit(gc.getInfoTypeForString(self.sUndeadUnit()))
    if self.bTechExist('TECH_CORRUPTION_OF_SPIRIT') and CyGame().getSorenRandNum(4+iAdj, "EvilStuff") == 1:
      self.addBarbUnit(gc.getInfoTypeForString(self.sEvilUnit()))

    # Nobility Building Support
    iEst1 = {}
    iEst2 = {}
    iEst3 = {}
    iGov1 = {}
    iGov2 = {}
    iGov3 = {}
    iCom1 = {}
    iMil1 = {}
      
    # Crowded squares are crowded - FW
    for i in range (CyMap().numPlots()):
      crowdMessage = True
      checkRoom = True
      roomFor = 1
      pPlot = CyMap().plotByIndex(i)
      if pPlot.isCity():
        roomFor = roomFor + pPlot.getPlotCity().getPopulation()
      for i in range(pPlot.getNumUnits()):
        pUnit = pPlot.getUnit(i)
        pPlayer = gc.getPlayer(pUnit.getOwner())
        if i < pPlot.getNumUnits() and pPlayer.isHuman():
          # Count Nobility Building Promotions
          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ESTATES1')):
            if pUnit.getOwner() not in iEst1:
              iEst1[pUnit.getOwner()] = 0
            iEst1[pUnit.getOwner()] += 1
          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ESTATES2')):
            if pUnit.getOwner() not in iEst2:
              iEst2[pUnit.getOwner()] = 0
            iEst2[pUnit.getOwner()] += 1
          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ESTATES3')):
            if pUnit.getOwner() not in iEst3:
              iEst3[pUnit.getOwner()] = 0
            iEst3[pUnit.getOwner()] += 1
          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GOVERNOR1')):
            if pUnit.getOwner() not in iGov1:
              iGov1[pUnit.getOwner()] = 0
            iGov1[pUnit.getOwner()] += 1
          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GOVERNOR2')):
            if pUnit.getOwner() not in iGov2:
              iGov2[pUnit.getOwner()] = 0
            iGov2[pUnit.getOwner()] += 1
          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GOVERNOR3')):
            if pUnit.getOwner() not in iGov3:
              iGov3[pUnit.getOwner()] = 0
            iGov3[pUnit.getOwner()] += 1
          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMMANDER2')):
            if pUnit.getOwner() not in iCom1:
              iCom1[pUnit.getOwner()] = 0
            iCom1[pUnit.getOwner()] += 1
          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMMANDER3')):
            if pUnit.getOwner() not in iMil1:
              iMil1[pUnit.getOwner()] = 0
            iMil1[pUnit.getOwner()] += 1
          
          # Crowding damage
          if pPlot.getNumUnits() > roomFor:
            # Check for nobility and computer units
            if checkRoom:
              checkRoom = False
              nobLevel = 0
              for ii in range(pPlot.getNumUnits()):
                oUnit = pPlot.getUnit(ii)
                # The strongest noble adds room for units
                if self.iNoble(oUnit,1) > nobLevel:
                  nobLevel = self.iNoble(oUnit,1)
                # Computer units add room for themselves    
                if not gc.getPlayer(oUnit.getOwner()).isHuman() or oUnit.getDomainType() == gc.getInfoTypeForString('DOMAIN_IMMOBILE'):
                  roomFor += 1
                # Carried units don't count
                if oUnit.isCargo():
                  roomFor += 1
              if nobLevel > 0:
                roomFor += nobLevel
            iDam = pPlot.getNumUnits() - roomFor
            iImprovement = pPlot.getImprovementType()
            if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_TOWER'):
              iDam -= 1
            if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_FORT'):
              iDam -= 2
            if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_CASTLE'):
              iDam -= 4
            if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_CITADEL'):
              iDam -= 8
            
            if iDam > 4:
              pUnit.doDamageNoCaster( iDam, 50, gc.getInfoTypeForString('DAMAGE_PHYSICAL'), false)
              if crowdMessage:
                CyInterface().addMessage(pUnit.getOwner(),False,25,str( iDam ) + " overcrowding damage!",'',1,'Art/Interface/Buttons/Promotions/Demon.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
                crowdMessage = False
          # Injury damage
          if pUnit.getDamage() > 0 and pUnit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_SIEGE') and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GOLEM')) and not pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_LOKI'):
            iDam = CyGame().getSorenRandNum( pUnit.getDamage(), "Injury Damage") / 5 - pUnit.getLevel()
            if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ANIMAL') or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ORC')) or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_LIZARDMAN')):
              iDam = iDam / 2
            if iDam > 12:
              iDam = 12
            if iDam > 0:  
              pUnit.changeDamage( iDam, pUnit.getOwner() ) 
            if pUnit.getDamage() > 99:
              sMess = pUnit.getName() + " dies from injuries..."
              CyInterface().addMessage(pUnit.getOwner(),False,25,sMess,'AS2D_UNIT_FALLS',1,pUnit.getButton(),ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
            else: 
              if iDam > 3:
                sMess = pUnit.getName() + " suffers " + str( iDam ) + " damage from injuries..."
                CyInterface().addMessage(pUnit.getOwner(),False,25,sMess,'',1,pUnit.getButton(),ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
              
    
    # Player Processing
    for iPlayer in range(gc.getMAX_PLAYERS()):
      pPlayer = gc.getPlayer(iPlayer)
      pTeam = gc.getTeam(pPlayer.getTeam())
      if pPlayer.isHuman():
        pCity = pPlayer.getCity(self.iValidCity(pPlayer))
        try:
          sPD = cPickle.loads(pPlayer.getScriptData())
        except EOFError:
          sPD = {}
          
        sPD['CUSTOM_INCOME'] = 0
        if 't3' not in sPD:
          sPD['t3'] = 0
        if 't2' not in sPD:
          sPD['t2'] = 0
        if 't1' not in sPD:
          sPD['t1'] = 0
        sPD['forges'] = pPlayer.getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_FORGE'))
        if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KURIOTATES'):
          if sPD['forges'] < int( pPlayer.getNumCities() / 2 ):
            sPD['forges'] = int( pPlayer.getNumCities() / 2 )
          
        iExtraResources = 0
        sExtraResources = 'Income from excess resources: '

        if pPlayer.isHuman():
          if iPlayer in iEst1:
            sPD['Est1'] = iEst1[iPlayer]
          if iPlayer in iEst2:
            sPD['Est2'] = iEst2[iPlayer]
          if iPlayer in iEst3:
            sPD['Est3'] = iEst3[iPlayer]
          if iPlayer in iGov1:
            sPD['Gov1'] = iGov1[iPlayer]
          if iPlayer in iGov2:
            sPD['Gov2'] = iGov2[iPlayer]
          if iPlayer in iGov3:
            sPD['Gov3'] = iGov3[iPlayer]
          if iPlayer in iCom1:
            sPD['Com1'] = iCom1[iPlayer]
          if iPlayer in iMil1:
            sPD['Mil1'] = iMil1[iPlayer]

        ## Process Strategic Resources
        iProcessMult = 1
        if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KURIOTATES'):
          iProcessMult = 4
        
        # Mithril
        if sPD['t3'] < pPlayer.getNumCities() * 200 + 500:
          i = gc.getInfoTypeForString('BONUS_MITHRIL')
          raw = pPlayer.getNumAvailableBonuses(i) * 8
          neededforges = pPlayer.getNumAvailableBonuses(i) * 4
          iprocess = neededforges
          if iprocess > sPD['forges'] * iProcessMult:
            iprocess = sPD['forges'] * iProcessMult
          if iprocess > int( raw / 2 ):  
            iprocess = int( raw / 2 )
          if iprocess > 0:
            sPD['t3'] += int( iprocess * 12 ) ## You get 48 if you have enough forges, 8 if you don't
            sPD['forges'] -= int( iprocess / iProcessMult )
            raw -= int( iprocess * 2 )
          if raw > 0:
            sPD['t3'] += raw
          if sPD['t3'] > pPlayer.getNumCities() * 200 + 500:
            sPD['t3'] = pPlayer.getNumCities() * 200 + 500

        # Iron
        if sPD['t2'] < pPlayer.getNumCities() * 200 + 500:
          i = gc.getInfoTypeForString('BONUS_IRON')
          raw = pPlayer.getNumAvailableBonuses(i) * 12
          neededforges = pPlayer.getNumAvailableBonuses(i) * 3
          iprocess = neededforges
          if iprocess > sPD['forges'] * iProcessMult:
            iprocess = sPD['forges'] * iProcessMult
          if iprocess > int( raw / 4 ):  
            iprocess = int( raw / 4 )
          if iprocess > 0:
            sPD['t2'] += int( iprocess * 12 ) ## You get 36 if you have enough forges, 12 if you don't
            sPD['forges'] -= int( iprocess / iProcessMult )
            raw -= int( iprocess * 4 )
          if raw > 0:
            sPD['t2'] += raw
          if sPD['t2'] > pPlayer.getNumCities() * 200 + 500:
            sPD['t2'] = pPlayer.getNumCities() * 200 + 500

        # Copper
        if sPD['t1'] < pPlayer.getNumCities() * 200 + 500:
          i = gc.getInfoTypeForString('BONUS_COPPER')
          raw = pPlayer.getNumAvailableBonuses(i) * 16
          neededforges = pPlayer.getNumAvailableBonuses(i) * 2
          iprocess = neededforges
          if iprocess > sPD['forges'] * iProcessMult:
            iprocess = sPD['forges'] * iProcessMult
          if iprocess > int( raw / 8 ):  
            iprocess = int( raw / 8 )
          if iprocess > 0:
            sPD['t1'] += int( iprocess * 20 ) ## You get 40 if you have enough forges, 16 if you don't
            sPD['forges'] -= int( iprocess / iProcessMult )
            raw -= int( iprocess * 8 )
          if raw > 0:
            sPD['t1'] += raw
          if sPD['t1'] > pPlayer.getNumCities() * 200 + 500:
            sPD['t1'] = pPlayer.getNumCities() * 200 + 500

  #     Sell Extra Resources
        if pPlayer.isAlive() and pPlayer.getNumCities() > 0:
          for i in range(gc.getNumBonusInfos()):
            bonus = gc.getBonusInfo(i)

            iNum = pPlayer.getNumAvailableBonuses(i) - 1
            if iNum > 0 :
              iDiv = 1
              if bonus.getHappiness() > 0:
                iNum += 1
                iDiv = 1
              if bonus.getDescription() == 'Horse':
                iNum += 1
                iDiv = 1
              if bonus.getDescription() == 'Copper':
                iNum += 1
                iDiv = 1
              if bonus.getDescription() == 'Iron':
                iNum += 1
                iDiv = 2
              if bonus.getDescription() == 'Mithril':
                iNum += 1
                iDiv = 4
              iTotal = iNum * iDiv
              if iTotal < iNum:
                iTotal = iNum
              pPlayer.setGold( pPlayer.getGold() + iTotal )
              iExtraResources += iTotal
              sExtraResources += bonus.getDescription() + ' ' + str( iTotal ) + ', '
          
          if iExtraResources > 0 and pPlayer.isHuman() == True:
            sExtraResources = sExtraResources[:-2]
            sPD['CUSTOM_INCOME'] += iExtraResources
            ## Give message when resource income changes
            if 'RESOURCE_INCOME' not in sPD:
              sPD['RESOURCE_INCOME'] = 0
            if iExtraResources != sPD['RESOURCE_INCOME']:
              CyInterface().addMessage(iPlayer,false,25,sExtraResources,'',1,'Art/Interface/Buttons/Equipment/DragonsHorde.dds',ColorTypes(11),pCity.getX(),pCity.getY(),True,True)
              CyInterface().addCombatMessage(iPlayer,sExtraResources)
              sPD['RESOURCE_INCOME'] = iExtraResources
            pPlayer.setScriptData(cPickle.dumps(sPD))

  #     Plunder from Barbarians
        if pPlayer.isHuman() and pPlayer.isAlive() and pPlayer.getNumCities() > 0:
          if 'PLUNDER' not in sPD:
            sPD['PLUNDER'] = 0
          if sPD['PLUNDER'] > 0 and sPD['PLUNDER'] < 2500:
            sMsg = 'You gain ' + str(sPD['PLUNDER']) + ' gold pieces from looting barbarians...'
            CyInterface().addMessage(iPlayer,false,25,sMsg,'AS2D_GOODY_GOLD',1,'Art/Interface/Buttons/Equipment/DragonsHorde.dds',ColorTypes(11),pCity.getX(),pCity.getY(),True,True)
            CyInterface().addCombatMessage(iPlayer,sMsg)
            pPlayer.setGold( pPlayer.getGold() + sPD['PLUNDER'] )
          sPD['PLUNDER'] = 0

          ## Commerce Sliders - Changing reduces bonus income
          if 'ECON' in sPD:
            sPD['ECON'] += 1
          else:
            sPD['ECON'] = 0

          if sPD['ECON'] < 0:
            sPD['ECON'] = 0

          if 'COMMERCE' not in sPD:
            sPD['COMMERCE'] = pPlayer.getCommercePercent(0)

          if 'RESEARCH' not in sPD:
            sPD['RESEARCH'] = pPlayer.getCommercePercent(1)

          if 'COMMERCE_INCOME' not in sPD:
            sPD['COMMERCE_INCOME'] = 0

          iChange = int( math.fabs( sPD['COMMERCE'] - pPlayer.getCommercePercent(0) ) / 2 ) - 1
          if int( math.fabs( sPD['RESEARCH'] - pPlayer.getCommercePercent(1) ) / 2 ) - 1 > iChange:
            iChange = int( math.fabs( sPD['RESEARCH'] - pPlayer.getCommercePercent(1) ) / 2 ) - 1
          if iChange > 0:
            iChange = iChange * ( ( iChange / 2 ) + 1 )
            sPD['ECON'] = sPD['ECON'] - iChange
            sPD['COMMERCE'] = pPlayer.getCommercePercent(0)
            sPD['RESEARCH'] = pPlayer.getCommercePercent(1)

          if sPD['ECON'] > 0:
            iIncome = int(math.sqrt(sPD['ECON']) * pPlayer.getTotalPopulation() / 50)
            iPotentialIncome = int(math.sqrt(iGameTurn) * pPlayer.getTotalPopulation() / 50)
            iIncome -= int( iPotentialIncome / 2 )
            if iIncome != 0:
              pPlayer.setGold( pPlayer.getGold() + iIncome )
              sPD['CUSTOM_INCOME'] += iIncome
            ## Give message when commerce priority income changes
            if iIncome != sPD['COMMERCE_INCOME']:
              sMsg = 'You are gaining ' + str(iIncome) + ' gold pieces per turn from stable commerce priorities... '
              CyInterface().addMessage(iPlayer,false,25,sMsg,'',1,'Art/Interface/Buttons/Equipment/DragonsHorde.dds',ColorTypes(11),pCity.getX(),pCity.getY(),True,True)
              CyInterface().addCombatMessage(iPlayer,sMsg)
              sPD['COMMERCE_INCOME'] = iIncome

          pPlayer.setScriptData(cPickle.dumps(sPD))

#     City Processing
      iDisputes = 1
      if pPlayer.isAlive() and pPlayer.getNumCities() > 0:  
        for i in range (pPlayer.getNumCities()):
          pCity = pPlayer.getCity(i)
          try:
            sCityInfo = cPickle.loads(pCity.getScriptData())
          except EOFError:
            self.initCityVars(pCity)

          ## Barbarian City Defense
          if iGameTurn == 0 and pPlayer.isBarbarian():
            iCityGarrison1 = gc.getInfoTypeForString('PROMOTION_CITY_GARRISON1')
            iCityGarrison2 = gc.getInfoTypeForString('PROMOTION_CITY_GARRISON2')
            newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_WARRIOR'), pCity.getX(), pCity.getY(), UnitAITypes.UNITAI_CITY_DEFENSE, DirectionTypes.DIRECTION_SOUTH)
            newUnit.setHasPromotion(iCityGarrison1, True)
            newUnit.setHasPromotion(iCityGarrison2, True)
            if CyGame().getUnitCreatedCount(gc.getInfoTypeForString('UNIT_AXEMAN')) > 5:
              newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ARCHER'), pCity.getX(), pCity.getY(), UnitAITypes.UNITAI_CITY_DEFENSE, DirectionTypes.DIRECTION_SOUTH)
              
          ## Barbarian City Menace    
          iForceChance = 100 - pCity.getPopulation() * 3 + pPlayer.getNumCities()
          if iForceChance < 10:
            iForceChance = 10
          if(CyGame().getSorenRandNum(iForceChance, "BarbStuff") == 1) and pPlayer.isBarbarian():
            iForceSize = int( CyGame().getSorenRandNum(6, "ForceSize") + ( pCity.getPopulation() / 2 ))
            pCity.changeCulture(pCity.getOwner(), iForceSize, True)
            if(pCity.getX() > 0 and pCity.getY() > 0 and pCity.getPopulation() > 0 and iForceSize > 0):
              for ii in range ( iForceSize ):
                oNewUnit = gc.getInfoTypeForString(self.sBarbUnit())
                newUnit = pPlayer.initUnit(oNewUnit, pCity.getX(), pCity.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
                newUnit.finishMoves()
                self.equip(newUnit)
                newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CREEP'), False)
                if ii == 0:
                  newUnit.setName(self.MarnokNameGenerator(newUnit))
                  newUnit.setBaseCombatStr(int(newUnit.baseCombatStr() * 1.5) + 1)
                  newUnit.setBaseCombatStrDefense(int(newUnit.baseCombatStrDefense() * 1.5) + 1)
                  self.generateLoot(newUnit,newUnit.baseCombatStr())
                  self.generateLoot(newUnit,newUnit.baseCombatStr())
                  newUnit.changeExperience(iForceSize+1, -1, False, False, False)
                  newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CITY_RAIDER1'), True)
                  newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO'), True)
                  newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LOYALTY'), True)
                  sMsg = newUnit.getName() + ' rises to lead the barbarians!'
                  self.msgAll(sMsg,pCity.getX(),pCity.getY(),pCity.getOwner(),newUnit.getButton())
            
          ## Island Resort Vacations
          if pCity.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_ISLAND_RESORT')) > 0:
            py = PyPlayer(iPlayer)
            for pUnit in py.getUnitList():
              if pUnit.getFortifyTurns() > 4 and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BLESSED')) and pUnit.isAlive() and pUnit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_BEAST') and pUnit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_ANIMAL'):
                pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BLESSED'), True)
                sMsg = pUnit.getName() + ' visits the ' + pCity.getName() + ' Island Resort for a little rest and relaxation!'
                CyInterface().addMessage(iPlayer,false,25,sMsg,'AS3D_SPELL_BLESS',1,pUnit.getButton(),ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)
                CyInterface().addCombatMessage(iPlayer,sMsg)
                break

          ## Automatic Military Academy Training
          if pCity.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_MILITARY_ACADEMY')) > 0:
            tUnit = -1
            tXP = -1
            pPlot = pCity.plot()
            for ii in range(pPlot.getNumUnits()):
              pUnit = pPlot.getUnit(ii)
              if pUnit.getOwner() == pCity.getOwner() and pUnit.getExperience() < pCity.getPopulation() and pUnit.getExperience() > tXP:
                tUnit = pUnit
                tXP = pUnit.getExperience()

            if tUnit != -1:
              tUnit.changeExperience(1, -1, False, False, False)
              sMsg = tUnit.getName() + ' studies at the ' + pCity.getName() + ' Academy... '
              CyInterface().addMessage(iPlayer,false,25,sMsg,'AS3D_SPELL_TRAIN',1,tUnit.getButton(),ColorTypes(8),pCity.getX(),pCity.getY(),True,True)
              CyInterface().addCombatMessage(iPlayer,sMsg)
            else:
              sMsg = 'The ' + pCity.getName() + ' Military Academy has an opening for a new student... '
              CyInterface().addMessage(iPlayer,false,25,sMsg,'',1,'Art/Interface/Buttons/Buildings/Academy.dds',ColorTypes(8),pCity.getX(),pCity.getY(),True,True)
              CyInterface().addCombatMessage(iPlayer,sMsg)

          ## Treasure and Noble Building Expiration
          if pCity.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_TREASURE1')) > 0:
            if 'TR1' not in sCityInfo:
              sCityInfo['TR1'] = CyGame().getGameTurn() + 18
            if sCityInfo['TR1'] < CyGame().getGameTurn() - 5: 
              sCityInfo['TR1'] = CyGame().getGameTurn() + 18
            if CyGame().getGameTurn() > sCityInfo['TR1']:
              pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_TREASURE1'), 0)
              sMsg = 'A treasure runs out in ' + pCity.getName() + '... '
              CyInterface().addMessage(iPlayer,false,25,sMsg,'',1,'Art/Interface/Buttons/Equipment/DragonsHorde.dds',ColorTypes(11),pCity.getX(),pCity.getY(),True,True)
              CyInterface().addCombatMessage(iPlayer,sMsg)
              sCityInfo['TR1'] = 0
          else:
            sCityInfo['TR1'] = 0

          if pCity.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_TREASURE2')) > 0:
            if 'TR2' not in sCityInfo:
              sCityInfo['TR2'] = CyGame().getGameTurn() + 18
            if sCityInfo['TR2'] < CyGame().getGameTurn() - 5: 
              sCityInfo['TR2'] = CyGame().getGameTurn() + 18
            if CyGame().getGameTurn() > sCityInfo['TR2']:
              pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_TREASURE2'), 0)
              sMsg = 'A large treasure runs out in ' + pCity.getName() + '... '
              CyInterface().addMessage(iPlayer,false,25,sMsg,'',1,'Art/Interface/Buttons/Equipment/DragonsHorde.dds',ColorTypes(11),pCity.getX(),pCity.getY(),True,True)
              CyInterface().addCombatMessage(iPlayer,sMsg)
              sCityInfo['TR2'] = 0
          else:
            sCityInfo['TR2'] = 0

          if pCity.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_TREASURE3')) > 0:
            if 'TR3' not in sCityInfo:
              sCityInfo['TR3'] = CyGame().getGameTurn() + 18
            if sCityInfo['TR3'] < CyGame().getGameTurn() - 5: 
              sCityInfo['TR3'] = CyGame().getGameTurn() + 18
            if CyGame().getGameTurn() > sCityInfo['TR3']:
              pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_TREASURE3'), 0)
              sMsg = 'A grand treasure runs out in ' + pCity.getName() + '... '
              CyInterface().addMessage(iPlayer,false,25,sMsg,'',1,'Art/Interface/Buttons/Equipment/DragonsHorde.dds',ColorTypes(11),pCity.getX(),pCity.getY(),True,True)
              CyInterface().addCombatMessage(iPlayer,sMsg)
              sCityInfo['TR3'] = 0
          else:
            sCityInfo['TR3'] = 0
            
          ## Process disputes for nobles to solve
          if pPlayer.isHuman():
            if 'JUDGE' not in sCityInfo:
              sCityInfo['JUDGE'] = 0
            if sCityInfo['JUDGE'] > 0:
              if CyGame().getSorenRandNum(100, "ReportDispute") < sCityInfo['JUDGE']:
                if CyGame().getSorenRandNum(sCityInfo['JUDGE'], "Dispute Self Resolved") < 2:
                  sMsg = 'The people of ' + pCity.getName() + ' have resolved their ' + self.sDisputeLevel(sCityInfo['JUDGE']) + ' dispute without a noble!  It caused somewhat of a mess, but it is now resolved...'
                  self.msgAll(sMsg,pCity.getX(),pCity.getY(),pCity.getOwner(),'Art/Interface/Buttons/Units/Commander.dds')
                  pCity.changeHurryAngerTimer(sCityInfo['JUDGE']+1)
                  iFeud = int( sCityInfo['JUDGE'] / 8 )
                  if iFeud > 0:
                    iFeud = iFeud * -1
                    pCity.changePopulation(iFeud)
                  sCityInfo['JUDGE'] = 0
                else:
                  sMsg = 'The people of ' + pCity.getName() + ' owned by ' + pPlayer.getName() + ' still await a noble to help them resolve a ' + self.sDisputeLevel(sCityInfo['JUDGE']) + ' dispute...'
                  self.msgAll(sMsg,pCity.getX(),pCity.getY(),pCity.getOwner(),'Art/Interface/Buttons/Units/Commander.dds')
            else:
              if iDisputes > 0 and CyGame().getSorenRandNum(3000, "Dispute") < pCity.getPopulation():
                iSize = CyGame().getSorenRandNum(pCity.getPopulation()*3 + 1, "DisputeSize")
                sMsg = 'A ' + self.sDisputeLevel(iSize) + ' dispute has broken out in ' + pCity.getName() + ' owned by ' + pPlayer.getName() + '.  They seek a noble to help resolve the situation...'
                self.msgAll(sMsg,pCity.getX(),pCity.getY(),pCity.getOwner(),'Art/Interface/Buttons/Units/Commander.dds')
                sCityInfo['JUDGE'] = iSize
                iDisputes -= 1
  
          ## Give computer players monoliths to help them out a little
          if pCity.getPopulation() > 2 and pPlayer.isHuman() == False:
            pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_MONOLITH'), 1)
          else:
            pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_MONOLITH'), 0)

          ## Computer vassal states occasionally give their masters units
          if not pPlayer.isHuman() and pTeam.isAVassal() and pCity.getPopulation() > CyGame().getSorenRandNum(100, "Vassal Gift Unit") and pPlayer.getNumMilitaryUnits() > pPlayer.getNumCities() * 3:
            py = PyPlayer(pCity.getOwner())
            imPlayer = pTeam.getLeaderID()
            mPlayer = gc.getPlayer(imPlayer)
            sMsg = pPlayer.getName() + ' wants to send a unit to serve their master...'
            CyInterface().addCombatMessage(imPlayer,sMsg)
            CyInterface().addMessage(imPlayer,false,25,sMsg,'AS2D_GOODY_GOLD',1,pUnit.getButton(),ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)
            for pUnit in py.getUnitList():
              if isWorldUnitClass(pUnit.getUnitClassType()) == False:
                sMsg = pPlayer.getName() + ' sends ' + pUnit.getName() + 's from ' + pCity.getName() + ' to serve the great ' + mPlayer.getName() + '...'
                CyInterface().addCombatMessage(imPlayer,sMsg)
                CyInterface().addMessage(imPlayer,false,25,sMsg,'AS2D_GOODY_GOLD',1,pUnit.getButton(),ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)
                newUnit = mPlayer.initUnit(pUnit.getUnitType(), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
                newUnit.convert(pUnit)
                break

          pCity.setScriptData(cPickle.dumps(sCityInfo))
              
    ### End FW Changes
            
    iRoadTax = {}
    for i in range (CyMap().numPlots()):
      pPlot = CyMap().plotByIndex(i)
      iFeature = pPlot.getFeatureType()
      iTerrain = pPlot.getTerrainType()
      iBonus = pPlot.getBonusType(-1)
      iImprovement = pPlot.getImprovementType()
      bUntouched = True
      
      # Add computer defenders for dungeons
      if iGameTurn == 0:
        sDefender = 'NONE'
        if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_DUNGEON'):
          sDefender = 'UNIT_WARRIOR'
        if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_BARROW'):
          sDefender = 'UNIT_SKELETON'
        if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_RUINS'):
          sDefender = 'UNIT_LIZARDMAN'
        if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_GOODY_HUT'):
          sDefender = 'UNIT_GOBLIN'
        if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_SHIP_WRECK'):
          sDefender = 'UNIT_STYGIAN_GUARD'
        if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_SERPENT_LAIR'):
          sDefender = 'UNIT_GIANT_SEA_SERPENT'
      
        if sDefender != 'NONE':
          bPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
          newUnit = bPlayer.initUnit(gc.getInfoTypeForString(sDefender), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
          self.equip(newUnit)
          newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CREEP'), True)
      
      iThisPlotTrain = 0
      iThisPlotTrainAnimal = 0
      if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_TOWER'):
        iThisPlotTrain = 1
      if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_FORT'):
        iThisPlotTrain = 2
      if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_CASTLE'):
        iThisPlotTrain = 4
      if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_CITADEL'):
        iThisPlotTrain = 8
      if pPlot.getFeatureType() == iJungle:
        iThisPlotTrainAnimal = 1
      iShelter = iThisPlotTrain 
      iDiseaseInPlot = 0
      iPlagueInPlot = 0
      iTreat = 0
      iDisMult = 2
      pCity = pPlot.getPlotCity()
      if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_HERBALIST')) > 0:
        iTreat += 1
      if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_INFIRMARY')) > 0:
        iTreat += 3

      ## Set Up Player and Team Variables for the Plot
      plotPlayer = gc.getPlayer(pPlot.getOwner())
      py = PyPlayer(pPlot.getOwner())
      if pPlot.isOwned() == False:
        plotPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
        py = PyPlayer(gc.getBARBARIAN_PLAYER())
      iPlotTeam = plotPlayer.getTeam()
      plotTeam = gc.getTeam(iPlotTeam)

      iEntropyMessage = 0
      bCanCreateUnit = True
      for ii in range(pPlot.getNumUnits()):
        if ii > pPlot.getNumUnits():
          break
        pUnit = pPlot.getUnit(ii)
        pPlayer = gc.getPlayer(pUnit.getOwner())
        iUnitTeam = pPlayer.getTeam()
        unitTeam = gc.getTeam(iUnitTeam)
        
        ## Wall of Stone
        if pUnit.isHasPromotion( gc.getInfoTypeForString('PROMOTION_WALL_OF_STONE') ):
          if pPlot.getX() != self.getObjectInt( pUnit, 'lx' ) or pPlot.getY() != self.getObjectInt( pUnit, 'ly' ):
            pUnit.setHasPromotion( gc.getInfoTypeForString('PROMOTION_WALL_OF_STONE'), False )
          
        ## Drowning
        if pUnit.isHasPromotion( gc.getInfoTypeForString('PROMOTION_DROWNING') ):
          if pUnit.isCargo() or not pPlot.isWater() or pUnit.isFlying() or pUnit.getDomainType() == gc.getInfoTypeForString('DOMAIN_SEA'):
            pUnit.setHasPromotion( gc.getInfoTypeForString('PROMOTION_DROWNING'), False )
          else:
            iDam = 100 - pUnit.getLevel() * 10
            if iDam > 0:
              pUnit.changeDamage( iDam, pUnit.getOwner() ) 
              if iDam > 0:
                CyInterface().addMessage(pUnit.getOwner(),false,25,'Your '+pUnit.getName()+' takes '+str(iDam)+' damage from drowning...','',1,'Art/Interface/Buttons/Promotions/flying.dds',ColorTypes(7),pUnit.getX(),pUnit.getY(),True,True)
                CyInterface().addCombatMessage(pUnit.getOwner(),'Your '+pUnit.getName()+' takes '+str(iDam)+' damage from drowning...')
          
        ## Water Walking with a Water Walker
        if pUnit.isHasPromotion( gc.getInfoTypeForString('PROMOTION_WALK_WITH_WATER_WALKER') ):
          if pUnit.isCargo() or not pPlot.isWater() or pUnit.isFlying() or pUnit.getDomainType() == gc.getInfoTypeForString('DOMAIN_SEA'):
            pUnit.setHasPromotion( gc.getInfoTypeForString('PROMOTION_WALK_WITH_WATER_WALKER'), False )
          else:
            pUnit.setHasPromotion( gc.getInfoTypeForString('PROMOTION_DROWNING'), True )
          
        ## Record Previous Unit Location  
        self.setObjectInt( pUnit, 'lx', pPlot.getX() )
        self.setObjectInt( pUnit, 'ly', pPlot.getY() )

        ## Unit Morale
        if pPlayer.isHuman():
          if pUnit.getNameNoDesc() == '.':
            self.nameUnit(pUnit)
        
          if pUnit.getGameTurnCreated() > iGameTurn - 1:
            self.tough(pUnit)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RAVAGER'), False)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WORKER_SHIELD'), False)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_1'), False)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_2'), False)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_3'), False)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_4'), False)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_5'), False)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_6'), False)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_7'), False)
          iMorale = self.iMorale(pUnit)
          if iMorale > 4:
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_1'), True)
          elif iMorale > 2: 
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_2'), True)
          elif iMorale == -1: 
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_3'), True)
          elif iMorale == -2: 
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_4'), True)
          elif iMorale == -3: 
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_5'), True)
          elif iMorale == -4: 
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_6'), True)
          elif iMorale < -4:  
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE_7'), True)
        else:
          # Computer Units get Ravager Bonus
          if iGameTurn > 50:
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RAVAGER'), True)
          if pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_WORKER') or pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_SETTLER'):
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WORKER_SHIELD'), False )
          else:
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WORKER_SHIELD'), False )
          if CyGame().getSorenRandNum(3, "UnitGuard") == 1 and pUnit.getDamage() < 50 and pUnit.baseMoves() > 0:
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_GUARDING'), True)
          else:
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_GUARDING'), False)
          if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ADEPT') and pPlot.isOwned() and not plotPlayer.isBarbarian() and pPlayer.isBarbarian():
            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG')):
              pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CREEP'), True)
            else:
              pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG'), True)
          if pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_MITHRIL')) and gc.getUnitInfo(pUnit.getUnitType()).getWeaponTier() > 2 and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MITHRIL_WEAPONS')):
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MITHRIL_WEAPONS'), True)
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), False)
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), False)
          elif pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_IRON')) and gc.getUnitInfo(pUnit.getUnitType()).getWeaponTier() > 1 and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS')):
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), True)
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), False)
          elif pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_COPPER')) and gc.getUnitInfo(pUnit.getUnitType()).getWeaponTier() > 0 and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS')):
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), True)
        
        ## Unit Weapon Upgrades
        if pPlot.isCity() and pPlot.getOwner() == pUnit.getOwner() and gc.getUnitInfo(pUnit.getUnitType()).getWeaponTier() > 0 and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MITHRIL_WEAPONS')):
          self.upgradeWeapons(pUnit,75,3)
        
        ## Fix an AI spinlock problem...
        if pUnit.getUnitAIType() == UnitAITypes.UNITAI_WORKER and pUnit.getUnitClassType() != gc.getInfoTypeForString('UNITCLASS_WORKER') and not pPlayer.isHuman():
          pUnit.setUnitAIType(UnitAITypes.UNITAI_ATTACK)
          
        ## Recruits become permanent (from temporary workers)
        if pUnit.getDuration() > 0 and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ILLUSION')) and ( pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_RECRUIT') or pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_WARRIOR') or pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_AXEMAN') or pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_CHAMPION') or pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_BERSERKER') or pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_PHALANX') or pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_IMMORTAL') ):
          pUnit.setDuration(0)

        ## If enemy occupied, do not create units here automatically
        if plotTeam.isAtWar(iUnitTeam):
          bCanCreateUnit = False

        ## Entropy Mana does damage to enemy human players
        if pPlot.isOwned() and plotPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_MANA_ENTROPY')) > 0 and pUnit.isAlive() and plotTeam.isAtWar(iUnitTeam):
          iMaxDam = 25
          if pPlayer.isHuman():
            iMaxDam = 100
          pUnit.doDamageNoCaster((plotPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_MANA_ENTROPY')) * 3 + 3), iMaxDam, gc.getInfoTypeForString('DAMAGE_UNHOLY'), False)
          if iEntropyMessage == 0:
            point = pPlot.getPoint()
            CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SACRIFICE'),point)
            iEntropyMessage = 1
            CyInterface().addMessage(pUnit.getOwner(),False,25,'Your army is suffering from poisonous fumes caused by enemy entropy mana!','',1,'Art/Interface/Buttons/Improvements/Maelstrom.dds',ColorTypes(7),pUnit.getX(),pUnit.getY(),True,True)
            CyInterface().addCombatMessage(pUnit.getOwner(),'Your army is suffering from poisonous fumes caused by enemy entropy mana!')

        ## Grant barbarian units to the player that owns a city they reside in.
        if (pPlot.isCity() and pPlayer.isBarbarian() and not plotPlayer.isBarbarian() and not plotPlayer.isHuman() and not pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_HIDDEN_CACHE')):
          pCity = pPlot.getPlotCity()
          newUnit = plotPlayer.initUnit(pUnit.getUnitType(), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
          newUnit.convert(pUnit)
          
        ## Grant barbarian zombie units to the evil player that owns the land they are in.
        if pPlayer.isBarbarian() and not plotPlayer.isBarbarian() and plotPlayer.isHuman() and plotPlayer.getAlignment() == iEvil and plotPlayer.isHasTech(gc.getInfoTypeForString('TECH_NECROMANCY')) and ( pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_ZOMBIE') or pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_ZOMBIE_1') or pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_ZOMBIE_2') ):
          CyInterface().addMessage(pUnit.getOwner(),false,25,pUnit.getName()+' rallies to you...','',1,'Art/Interface/Buttons/Units/Diseased Corpse.dds',ColorTypes(13),pUnit.getX(),pUnit.getY(),True,True)
          CyInterface().addCombatMessage(pUnit.getOwner(),pUnit.getName()+' rallies to you...')
          newUnit = plotPlayer.initUnit(pUnit.getUnitType(), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
          newUnit.convert(pUnit)
          
        # Computer Players gain creeps within their borders
        # if (pPlot.isOwned() and pPlayer.isBarbarian() and not plotPlayer.isBarbarian() and not plotPlayer.isHuman() and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CREEP')) and not pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_HIDDEN_CACHE') and not pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_ORTHUS')):
          # pCity = plotPlayer.getCity(self.iValidCity(plotPlayer))
          # pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CREEP'), False)
          # pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SLEEPING'), True)
          # newUnit = plotPlayer.initUnit(pUnit.getUnitType(), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
          # newUnit.convert(pUnit)

        ## Hidden Caches Stay Invisible
        if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_HIDDEN_CACHE'):
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INVISIBLE'), True)
          
        ## Damaged Creeps Can wake up and if they do, wake up all creeps on the stack
        if (pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CREEP')) and pUnit.getDamage() > 5 and CyGame().getSorenRandNum(3, "Wake Creep") == 1):
          for iii in range(pPlot.getNumUnits()):
            if iii > pPlot.getNumUnits():
              break
            pPlot.getUnit(ii).setHasPromotion(gc.getInfoTypeForString('PROMOTION_CREEP'), False)
            pPlot.getUnit(ii).finishMoves()

        ## Sell scrolls and potions owned by computers
        if CyGame().getSorenRandNum(20, "SellEquipment") == 1:
          if (pPlayer.isBarbarian() == False and pPlayer.isHuman() == False):
            SellIt = 0
            if ( pUnit.getUnitType() == gc.getInfoTypeForString('EQUIPMENT_POTION_HEALING_MINOR') ):
              SellIt = 1
            if ( pUnit.getUnitType() == gc.getInfoTypeForString('EQUIPMENT_POTION_STRENGTH') ):
              SellIt = 1
            if ( pUnit.getUnitType() == gc.getInfoTypeForString('EQUIPMENT_POTION_HASTE') ):
              SellIt = 1
            if ( pUnit.getUnitType() == gc.getInfoTypeForString('EQUIPMENT_SCROLL_MM') ):
              SellIt = 1
            if ( pUnit.getUnitType() == gc.getInfoTypeForString('EQUIPMENT_SCROLL_MA') ):
              SellIt = 1
            if ( pUnit.getUnitType() == gc.getInfoTypeForString('EQUIPMENT_SCROLL_SB') ):
              SellIt = 1
            if ( pUnit.getUnitType() == gc.getInfoTypeForString('EQUIPMENT_SCROLL_FB') ):
              SellIt = 1
            if ( pUnit.getUnitType() == gc.getInfoTypeForString('EQUIPMENT_SCROLL_SK') ):
              SellIt = 1
            if ( pUnit.getUnitType() == gc.getInfoTypeForString('EQUIPMENT_SCROLL_MR') ):
              SellIt = 1
            if ( pUnit.getUnitType() == gc.getInfoTypeForString('EQUIPMENT_SCROLL_MS') ):
              SellIt = 3
            if SellIt > 0:
              pUnit.kill(True,0)
              pPlayer.changeGold(35 * SellIt)
              
        ## Send Heralded Units On
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HERALDS_CALL')):
          pUnit.kill(True,0)

        ## Infernal Units Heal at Infernal Altars 
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON')) and pUnit.getDamage() > 0 and pCity.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_DEMONS_ALTAR')) > 0:
          pUnit.changeDamage(-13, 0)
          
        ## Equip barbarian units
        if (pPlayer.isBarbarian() and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_THROWING_AXES'))):
          self.equip(pUnit)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_THROWING_AXES'), False)

        ## Vampires become hungry and possibly ready to gift vampirism
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_VAMPIRE')):
          if CyGame().getSorenRandNum(100, "Ready to Hunt") < 10 - pUnit.getLevel() / 2 and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HUNGER')): 
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HUNGER'), True)
            CyInterface().addMessage(pUnit.getOwner(),false,25,pUnit.getName()+' hungers...','',1,'Art/Interface/Buttons/Units/vampire.dds',ColorTypes(7),pUnit.getX(),pUnit.getY(),True,True)
            CyInterface().addCombatMessage(pUnit.getOwner(),pUnit.getName()+' hungers...')
            point = pUnit.plot().getPoint()
            CyAudioGame().Play3DSound('AS3D_VAMPIRE_SELECT',point.x,point.y,point.z)
            CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SACRIFICE'),point)
          if CyGame().getSorenRandNum(100, "Ready to Gift") < pUnit.getLevel() - 10 and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_READY_TO_GIFT')):  
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_READY_TO_GIFT'), True)
            CyInterface().addMessage(pUnit.getOwner(),false,25,'Your '+pUnit.getName()+' is ready to gift vampirism...','',1,'Art/Interface/Buttons/Units/vampire.dds',ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)
            CyInterface().addCombatMessage(pUnit.getOwner(),'Your '+pUnit.getName()+' is ready to gift vampirism...')
            point = pUnit.plot().getPoint()
            CyAudioGame().Play3DSound('AS3D_SPELL_GIFT_VAMPIRISM',point.x,point.y,point.z)
            CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SACRIFICE'),point)

        ## Nobles who can judge disputes try if they have done nothing else this turn.  
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_NOBILITY')) and not pUnit.isHasCasted() and self.reqJudge(pUnit):
          self.spellJudge(pUnit)
          pUnit.setHasCasted(True)

        ## Units which can sustain units try if they have done nothing else this turn.  
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SUMMONER')) and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DIMENSIONAL1')) and not pUnit.isHasCasted() and self.reqSustain(pUnit):
          self.spellSustain(pUnit)
          pUnit.setHasCasted(True)

        ## Burglars fortified on a Hidden Cache continue to search for a way to loot it.
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BURGLAR1')) and not pUnit.isHasCasted() and pUnit.getFortifyTurns() > 4: ## and self.reqInteractCache(pUnit,1):
          self.spellExamineCache(pUnit,1)
          pUnit.setHasCasted(True)
          
        ## Fortified Units Cost Less Maintenance
        if pUnit.getFortifyTurns() > 4:
          if pUnit.getOwner() in iRoadTax:
            iRoadTax[pUnit.getOwner()] -= 1
          else:
            iRoadTax[pUnit.getOwner()] = -1

        ## Units with healing touch auto-use it if they can.
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CAST_HEALING_TOUCH')) and not pUnit.isHasCasted() and self.reqHeal(pUnit):
          self.spellFieldMedic(pUnit)
          pUnit.setHasCasted(True)

        ## Fortified Priests Auto-Buff if they can
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DIVINE')) and pUnit.getFortifyTurns() > 1 and not pUnit.isHasCasted():
          py = PyPlayer(pUnit.getOwner())
          iABR = self.iAutoBuffRange(pUnit)
          iBuffs = pUnit.getLevel()
          for iBuff in range( ( pUnit.getLevel() + 2 ) / 3 ):
            iNoTargets = iBuffs
            if iBuffs < 1:
              break
            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING2')) and iBuffs > 0 and pUnit.getReligion() == gc.getInfoTypeForString('RELIGION_THE_ORDER'):
              pBestUnit = -1
              iBestRange = iABR
              for tUnit in py.getUnitList():
                if tUnit.isAlive() and tUnit.isPromotionValid(gc.getInfoTypeForString('PROMOTION_BLESSED')) and not tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BLESSED')):
                  iRange = int( math.fabs(pUnit.getX()-tUnit.getX()) )
                  if iRange < int( math.fabs(pUnit.getY()-tUnit.getY()) ):
                    iRange = int( math.fabs(pUnit.getY()-tUnit.getY()) )
                  if iRange < iBestRange:
                    iBestRange = iRange
                    pBestUnit = tUnit
              if pBestUnit != -1:
                iBuffs -= 1
                if iABR > iBestRange:
                  pBestUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BLESSED'), True)
                  if pPlayer.isHuman():
                    CyInterface().addMessage(pBestUnit.getOwner(),false,25,'Your '+pBestUnit.getName()+' gains a blessing from your '+pUnit.getName()+'!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),pBestUnit.getX(),pBestUnit.getY(),True,True)
                    CyInterface().addCombatMessage(pBestUnit.getOwner(),'Your '+pBestUnit.getName()+' gains a blessing from your '+pUnit.getName()+'!')
                    point = pBestUnit.plot().getPoint()
                    CyAudioGame().Play3DSound('AS3D_SPELL_BLESS',point.x,point.y,point.z)
                    CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_CREATION'),point)

            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING2')) and iBuffs > 0 and  pUnit.getReligion() == gc.getInfoTypeForString('RELIGION_RUNES_OF_KILMORPH'):
              pBestUnit = -1
              iBestRange = iABR
              for tUnit in py.getUnitList():
                if tUnit.isPromotionValid(gc.getInfoTypeForString('PROMOTION_SHIELD_OF_FAITH')) and not tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SHIELD_OF_FAITH')):
                  iRange = int( math.fabs(pUnit.getX()-tUnit.getX()) )
                  if iRange < int( math.fabs(pUnit.getY()-tUnit.getY()) ):
                    iRange = int( math.fabs(pUnit.getY()-tUnit.getY()) )
                  if iRange < iBestRange:
                    iBestRange = iRange
                    pBestUnit = tUnit
              if pBestUnit != -1:
                iBuffs -= 1
                if iABR > iBestRange:
                  pBestUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SHIELD_OF_FAITH'), True)
                  if pPlayer.isHuman():
                    CyInterface().addMessage(pBestUnit.getOwner(),false,25,'Your '+pBestUnit.getName()+' gains a shield of faith from your '+pUnit.getName()+'!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),pBestUnit.getX(),pBestUnit.getY(),True,True)
                    CyInterface().addCombatMessage(pBestUnit.getOwner(),'Your '+pBestUnit.getName()+' gains a shield of faith from your '+pUnit.getName()+'!')
                    point = pBestUnit.plot().getPoint()
                    CyAudioGame().Play3DSound('AS3D_SPELL_ENCHANTMENT',point.x,point.y,point.z)
                    CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SWORDS_SPARKS'),point)

            if iNoTargets == iBuffs:
              break
              
        ## Fortified Mages Auto-Buff if they can
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING1')) and pUnit.getFortifyTurns() > 0 and not pUnit.isHasCasted():
          py = PyPlayer(pUnit.getOwner())
          iABR = self.iAutoBuffRange(pUnit)
          iBuffs = CyGame().getSorenRandNum( pUnit.getLevel(), "Autobuff" ) + 1
          for iBuff in range( ( pUnit.getLevel() + 2 ) / 3 ):
            iNoTargets = iBuffs
            if iBuffs < 1:
              break
            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ENCHANTMENT1')) and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING1')) and iBuffs > 0:
              pBestUnit = -1
              iBestRange = iABR
              for tUnit in py.getUnitList():
                if tUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_MELEE') and not tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ENCHANTED_BLADE')):
                  iRange = int( math.fabs(pUnit.getX()-tUnit.getX()) )
                  if iRange < int( math.fabs(pUnit.getY()-tUnit.getY()) ):
                    iRange = int( math.fabs(pUnit.getY()-tUnit.getY()) )
                  if iRange < iBestRange:
                    iBestRange = iRange
                    pBestUnit = tUnit
              if pBestUnit != -1:
                iBuffs -= 3
                if iABR > iBestRange:
                  pBestUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENCHANTED_BLADE'), True)
                  if pPlayer.isHuman():
                    CyInterface().addMessage(pBestUnit.getOwner(),false,25,'Your '+pBestUnit.getName()+' gains an enchanted blade from your '+pUnit.getName()+'!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),pBestUnit.getX(),pBestUnit.getY(),True,True)
                    CyInterface().addCombatMessage(pBestUnit.getOwner(),'Your '+pBestUnit.getName()+' gains an enchanted blade from your '+pUnit.getName()+'!')
                    point = pBestUnit.plot().getPoint()
                    CyAudioGame().Play3DSound('AS3D_SPELL_ENCHANTMENT',point.x,point.y,point.z)
                    CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_ENCHANTED_BLADE'),point)

            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SPIRIT1')) and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING1')) and iBuffs > 0:
              pBestUnit = -1
              iBestRange = iABR
              for tUnit in py.getUnitList():
                if tUnit.isAlive() and tUnit.isPromotionValid(gc.getInfoTypeForString('PROMOTION_COURAGE')) and not tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COURAGE')):
                  iRange = int( math.fabs(pUnit.getX()-tUnit.getX()) )
                  if iRange < int( math.fabs(pUnit.getY()-tUnit.getY()) ):
                    iRange = int( math.fabs(pUnit.getY()-tUnit.getY()) )
                  if iRange < iBestRange:
                    iBestRange = iRange
                    pBestUnit = tUnit
              if pBestUnit != -1:
                iBuffs -= 2
                if iABR > iBestRange:
                  pBestUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COURAGE'), True)
                  if pPlayer.isHuman():
                    CyInterface().addMessage(pBestUnit.getOwner(),false,25,'Your '+pBestUnit.getName()+' gains courage from your '+pUnit.getName()+'!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),pBestUnit.getX(),pBestUnit.getY(),True,True)
                    CyInterface().addCombatMessage(pBestUnit.getOwner(),'Your '+pBestUnit.getName()+' gains courage from your '+pUnit.getName()+'!')
                    point = pBestUnit.plot().getPoint()
                    CyAudioGame().Play3DSound('AS3D_SPELL_BLESS',point.x,point.y,point.z)
                    CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_CREATION'),point)

            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_LAW1')) and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING1')) and iBuffs > 0:
              pBestUnit = -1
              iBestRange = iABR
              for tUnit in py.getUnitList():
                if tUnit.isAlive() and tUnit.isPromotionValid(gc.getInfoTypeForString('PROMOTION_LOYALTY')) and not tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_LOYALTY')):
                  iRange = int( math.fabs(pUnit.getX()-tUnit.getX()) )
                  if iRange < int( math.fabs(pUnit.getY()-tUnit.getY()) ):
                    iRange = int( math.fabs(pUnit.getY()-tUnit.getY()) )
                  if iRange < iBestRange:
                    iBestRange = iRange
                    pBestUnit = tUnit
              if pBestUnit != -1:
                iBuffs -= 2
                if iABR > iBestRange:
                  pBestUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LOYALTY'), True)
                  if pPlayer.isHuman():
                    CyInterface().addMessage(pBestUnit.getOwner(),false,25,'Your '+pBestUnit.getName()+' gains loyalty from your '+pUnit.getName()+'!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),pBestUnit.getX(),pBestUnit.getY(),True,True)
                    CyInterface().addCombatMessage(pBestUnit.getOwner(),'Your '+pBestUnit.getName()+' gains loyalty from your '+pUnit.getName()+'!')
                    point = pBestUnit.plot().getPoint()
                    CyAudioGame().Play3DSound('AS3D_SPELL_BLESS',point.x,point.y,point.z)
                    CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_CREATION'),point)

            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_LAW3')) and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING3')) and iBuffs > 0:
              pBestUnit = -1
              iBestRange = iABR
              for tUnit in py.getUnitList():
                if tUnit.isAlive() and tUnit.isPromotionValid(gc.getInfoTypeForString('PROMOTION_VALOR')) and not tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_VALOR')):
                  iRange = int( math.fabs(pUnit.getX()-tUnit.getX()) )
                  if iRange < int( math.fabs(pUnit.getY()-tUnit.getY()) ):
                    iRange = int( math.fabs(pUnit.getY()-tUnit.getY()) )
                  if iRange < iBestRange:
                    iBestRange = iRange
                    pBestUnit = tUnit
              if pBestUnit != -1:
                iBuffs -= 1
                if iABR > iBestRange:
                  pBestUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_VALOR'), True)
                  if pPlayer.isHuman():
                    CyInterface().addMessage(pBestUnit.getOwner(),false,25,'Your '+pBestUnit.getName()+' gains valor from your '+pUnit.getName()+'!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),pBestUnit.getX(),pBestUnit.getY(),True,True)
                    CyInterface().addCombatMessage(pBestUnit.getOwner(),'Your '+pBestUnit.getName()+' gains valor from your '+pUnit.getName()+'!')
                    point = pBestUnit.plot().getPoint()
                    CyAudioGame().Play3DSound('AS3D_SPELL_BLESS',point.x,point.y,point.z)
                    CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_CREATION'),point)

            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SPIRIT3')) and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING3')) and iBuffs > 6:
              pBestUnit = -1
              iBestRange = iABR
              for tUnit in py.getUnitList():
                if tUnit.isAlive() and tUnit.getDuration() == 0 and tUnit.isPromotionValid(gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE')) and not tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE')):
                  iRange = int( math.fabs(pUnit.getX()-tUnit.getX()) )
                  if iRange < int( math.fabs(pUnit.getY()-tUnit.getY()) ):
                    iRange = int( math.fabs(pUnit.getY()-tUnit.getY()) )
                  if iRange < iBestRange:
                    iBestRange = iRange
                    pBestUnit = tUnit
              if pBestUnit != -1:
                iBuffs -= 7
                if iABR > iBestRange:
                  pBestUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE'), True)
                  if pPlayer.isHuman():
                    CyInterface().addMessage(pBestUnit.getOwner(),false,25,'Your '+pBestUnit.getName()+' gains help from your '+pUnit.getName()+'!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),pBestUnit.getX(),pBestUnit.getY(),True,True)
                    CyInterface().addCombatMessage(pBestUnit.getOwner(),'Your '+pBestUnit.getName()+' gains help from your '+pUnit.getName()+'!')
                    point = pBestUnit.plot().getPoint()
                    CyAudioGame().Play3DSound('AS3D_SPELL_BLESS',point.x,point.y,point.z)
                    CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPIRITUAL_HAMMER'),point)

            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ENCHANTMENT3')) and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING3')) and iBuffs > 9:
              pBestUnit = -1
              iBestRange = iABR
              for tUnit in py.getUnitList():
                if tUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ADEPT') and tUnit.getDuration() == 0 and not tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SPELLSTAFF')):
                  iRange = int( math.fabs(pUnit.getX()-tUnit.getX()) )
                  if iRange < int( math.fabs(pUnit.getY()-tUnit.getY()) ):
                    iRange = int( math.fabs(pUnit.getY()-tUnit.getY()) )
                  if iRange < iBestRange:
                    iBestRange = iRange
                    pBestUnit = tUnit
              if pBestUnit != -1:
                iBuffs -= 10
                if iABR > iBestRange:
                  pBestUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SPELLSTAFF'), True)
                  if pPlayer.isHuman():
                    CyInterface().addMessage(pBestUnit.getOwner(),false,25,'Your '+pBestUnit.getName()+' gains an enchanted staff from your '+pUnit.getName()+'!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),pBestUnit.getX(),pBestUnit.getY(),True,True)
                    CyInterface().addCombatMessage(pBestUnit.getOwner(),'Your '+pBestUnit.getName()+' gains an enchanted staff from your '+pUnit.getName()+'!')
                    point = pBestUnit.plot().getPoint()
                    CyAudioGame().Play3DSound('AS3D_SPELL_BLESS',point.x,point.y,point.z)
                    CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPIRITUAL_HAMMER'),point)

            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ENCHANTMENT2')) and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING2')) and iBuffs > 0:
              pBestUnit = -1
              iBestRange = iABR
              for tUnit in py.getUnitList():
                if tUnit.isAlive() and tUnit.isPromotionValid(gc.getInfoTypeForString('PROMOTION_FLAMING_ARROWS')) and not tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FLAMING_ARROWS')):
                  iRange = int( math.fabs(pUnit.getX()-tUnit.getX()) )
                  if iRange < int( math.fabs(pUnit.getY()-tUnit.getY()) ):
                    iRange = int( math.fabs(pUnit.getY()-tUnit.getY()) )
                  if iRange < iBestRange:
                    iBestRange = iRange
                    pBestUnit = tUnit
              if pBestUnit != -1:
                iBuffs -= 1
                if iABR > iBestRange:
                  pBestUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FLAMING_ARROWS'), True)
                  if pPlayer.isHuman():
                    CyInterface().addMessage(pBestUnit.getOwner(),false,25,'Your '+pBestUnit.getName()+' gains flaming arrows from your '+pUnit.getName()+'!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),pBestUnit.getX(),pBestUnit.getY(),True,True)
                    CyInterface().addCombatMessage(pBestUnit.getOwner(),'Your '+pBestUnit.getName()+' gains flaming arrows from your '+pUnit.getName()+'!')
                    point = pBestUnit.plot().getPoint()
                    CyAudioGame().Play3DSound('AS3D_SPELL_BLESS',point.x,point.y,point.z)
                    CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_CREATION'),point)

            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_EARTH3')) and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING3')) and iBuffs > 0:
              pBestUnit = -1
              iBestRange = iABR
              for tUnit in py.getUnitList():
                if tUnit.isPromotionValid(gc.getInfoTypeForString('PROMOTION_STONESKIN')) and not tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_STONESKIN')):
                  iRange = int( math.fabs(pUnit.getX()-tUnit.getX()) )
                  if iRange < int( math.fabs(pUnit.getY()-tUnit.getY()) ):
                    iRange = int( math.fabs(pUnit.getY()-tUnit.getY()) )
                  if iRange < iBestRange:
                    iBestRange = iRange
                    pBestUnit = tUnit
              if pBestUnit != -1:
                iBuffs -= 1
                if iABR > iBestRange:
                  pBestUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STONESKIN'), True)
                  if pPlayer.isHuman():
                    CyInterface().addMessage(pBestUnit.getOwner(),false,25,'Your '+pBestUnit.getName()+' gains stoneskin from your '+pUnit.getName()+'!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),pBestUnit.getX(),pBestUnit.getY(),True,True)
                    CyInterface().addCombatMessage(pBestUnit.getOwner(),'Your '+pBestUnit.getName()+' gains stoneskin from your '+pUnit.getName()+'!')
                    point = pBestUnit.plot().getPoint()
                    CyAudioGame().Play3DSound('AS3D_SPELL_STONESKIN',point.x,point.y,point.z)
                    CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_STONESKIN'),point)

            # if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_LAW3')) and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING3')) and iBuffs > 0:
              # pBestUnit = -1
              # iBestRange = iABR
              # for tUnit in py.getUnitList():
                # if tUnit.isPromotionValid(gc.getInfoTypeForString('PROMOTION_VALOR')) and not tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_VALOR')):
                  # iRange = int( math.fabs(pUnit.getX()-tUnit.getX()) )
                  # if iRange < int( math.fabs(pUnit.getY()-tUnit.getY()) ):
                    # iRange = int( math.fabs(pUnit.getY()-tUnit.getY()) )
                  # if iRange < iBestRange:
                    # iBestRange = iRange
                    # pBestUnit = tUnit
              # if pBestUnit != -1:
                # iBuffs -= 1
                # if iABR > iBestRange:
                  # pBestUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_VALOR'), True)
                  # if pPlayer.isHuman():
                    # CyInterface().addMessage(pBestUnit.getOwner(),False,25,'Your '+pBestUnit.getName()+' gains valor from your '+pUnit.getName()+'!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),pBestUnit.getX(),pBestUnit.getY(),True,True)
                    # CyInterface().addCombatMessage(pBestUnit.getOwner(),'Your '+pBestUnit.getName()+' gains valor from your '+pUnit.getName()+'!')
                    # point = pBestUnit.plot().getPoint()
                    # CyAudioGame().Play3DSound('AS3D_SPELL_BLESS',point.x,point.y,point.z)
                    # CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_STONESKIN'),point)

            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_NATURE2')) and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING2')) and iBuffs > 0:
              pBestUnit = -1
              iBestRange = iABR
              for tUnit in py.getUnitList():
                if tUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_RECON') and not tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED_BLADE')):
                  iRange = int( math.fabs(pUnit.getX()-tUnit.getX()) )
                  if iRange < int( math.fabs(pUnit.getY()-tUnit.getY()) ):
                    iRange = int( math.fabs(pUnit.getY()-tUnit.getY()) )
                  if iRange < iBestRange:
                    iBestRange = iRange
                    pBestUnit = tUnit
              if pBestUnit != -1:
                iBuffs -= 1
                if iABR > iBestRange:
                  pBestUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED_BLADE'), True)
                  if pPlayer.isHuman():
                    CyInterface().addMessage(pBestUnit.getOwner(),false,25,'Your '+pBestUnit.getName()+' gains a poisoned blade from your '+pUnit.getName()+'!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),pBestUnit.getX(),pBestUnit.getY(),True,True)
                    CyInterface().addCombatMessage(pBestUnit.getOwner(),'Your '+pBestUnit.getName()+' gains a poisoned blade from your '+pUnit.getName()+'!')
                    point = pBestUnit.plot().getPoint()
                    CyAudioGame().Play3DSound('AS3D_SPELL_ENCHANTMENT',point.x,point.y,point.z)
                    CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPELL1'),point)

            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_AIR1')) and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING1')) and iBuffs > 0:
              pBestUnit = -1
              iBestRange = iABR
              for tUnit in py.getUnitList():
                if (tUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_NAVAL') or tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FLYING'))) and not tUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FAIR_WINDS')):
                  iRange = int( math.fabs(pUnit.getX()-tUnit.getX()) )
                  if iRange < int( math.fabs(pUnit.getY()-tUnit.getY()) ):
                    iRange = int( math.fabs(pUnit.getY()-tUnit.getY()) )
                  if iRange < iBestRange:
                    iBestRange = iRange
                    pBestUnit = tUnit
              if pBestUnit != -1:
                iBuffs -= 1
                if iABR > iBestRange:
                  pBestUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FAIR_WINDS'), True)
                  if pPlayer.isHuman():
                    CyInterface().addMessage(pBestUnit.getOwner(),false,25,'Your '+pBestUnit.getName()+' experiences fair winds because of '+pUnit.getName()+'!','',1,'Art/Interface/Buttons/Units/mage.dds',ColorTypes(8),pBestUnit.getX(),pBestUnit.getY(),True,True)
                    CyInterface().addCombatMessage(pBestUnit.getOwner(),'Your '+pBestUnit.getName()+' experiences fair winds because of '+pUnit.getName()+'!')
                    point = pBestUnit.plot().getPoint()
                    CyAudioGame().Play3DSound('AS3D_SPELL_HASTE',point.x,point.y,point.z)
                    CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_WIND_SWIRL'),point)

            if iNoTargets == iBuffs:
              break

        # Units with mage armor, buff if they can
        # if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CAST_MAGE_ARMOR')) and not pUnit.isHasCasted() and self.reqMageArmor(pUnit):
          # self.spellMageArmor(pUnit)
          # pUnit.setHasCasted(True)
          
        ## Living units that fly take endurance damage
        if pPlayer.isHuman() and (pUnit.isAlive() or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ANGEL'))) and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FLYING')):
          iDam = CyGame().getSorenRandNum(16, "Flying Fatigue") + 3 - pUnit.getLevel()
          if iDam > 0:
            CyInterface().addMessage(pUnit.getOwner(),false,25,'Your '+pUnit.getName()+' is flying and taking ' + str(iDam) + ' endurance damage... (3d6-level)','',1,'Art/Interface/Buttons/Promotions/flying.dds',ColorTypes(7),pUnit.getX(),pUnit.getY(),True,True)
            CyInterface().addCombatMessage(pUnit.getOwner(),'Your '+pUnit.getName()+' is flying and taking ' + str(iDam) + ' endurance damage... (3d6-level)')
            pUnit.changeDamage( iDam, pUnit.getOwner() ) 
              
        ## Vessels can take damage from dangerous seas
        if pPlayer.isHuman() and iTerrain == iOcean and ( not pPlot.isOwned() or pPlot.getOwner() != pUnit.getOwner()):
          if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_NAVAL'):
            iMov = pUnit.movesLeft() / 60
            if iMov > pUnit.baseMoves():
              iMov = pUnit.baseMoves()
            iDam = CyGame().getSorenRandNum(50, "Dangerous Seas") - iMov * 5 - pUnit.getLevel() * 3 - pUnit.baseCombatStr()
            if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_SEAFARING')):
              iDam = iDam - 10
            if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_OPTICS')):
              iDam = iDam - 10
            if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_ASTRONOMY')):
              iDam = iDam - 10
            if iDam > 0:
              pUnit.changeDamage( iDam, pUnit.getOwner() ) 
              if iDam > 4:
                CyInterface().addMessage(pUnit.getOwner(),false,25,'Your '+pUnit.getName()+' takes '+str(iDam)+' damage from dangerous seas...','',1,'Art/Interface/Buttons/Promotions/flying.dds',ColorTypes(7),pUnit.getX(),pUnit.getY(),True,True)
                CyInterface().addCombatMessage(pUnit.getOwner(),'Your '+pUnit.getName()+' takes '+str(iDam)+' damage from dangerous seas...')
                # CyCamera().JustLookAtPlot(pPlot)
              
        ## Merchant Ships give income every 25 turns or so, more with speed and experience
        if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_MERCHANT_SHIP') and pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_OCEAN') and CyGame().getSorenRandNum(100, "Merchant") < pUnit.getLevel() + pUnit.baseMoves():
          iRange = 15
          iX = pUnit.getX()
          iY = pUnit.getY()
          sBlock = ''

          ## Cut down range close to map borders, frozen waters make merchanteering more difficult
          if iY < iRange:
            iRange = iY
            sBlock = ' limited by frozen waters...'
          if iY > CyMap().getGridHeight() - iRange:
            iRange = ( CyMap().getGridHeight() - iY )
            sBlock = ' limited by frozen waters...'
            
          for iiX in range(iX-iRange, iX+iRange+1, 1):
            for iiY in range(iY-iRange, iY+iRange+1, 1):
              xPlot = CyMap().plot(iiX,iiY)
              # For now, don't worry about cities - remove False if desired
              if False and xPlot.isCity() and xPlot.getOwner() == pUnit.getOwner():
                xCity = xPlot.getPlotCity()
                iRangeToCity = -1
                if iRangeToCity < int( math.fabs( xPlot.getX() - pUnit.getX() ) ):
                  iRangeToCity = int( math.fabs( xPlot.getX() - pUnit.getX() ) )
                if iRangeToCity < int( math.fabs( xPlot.getY() - pUnit.getY() ) ):
                  iRangeToCity = int( math.fabs( xPlot.getY() - pUnit.getY() ) )
                if iRangeToCity > -1 and iRange > iRangeToCity:
                  iRange = iRangeToCity
                  sBlock = ' limited by your city ' + xCity.getName() + '...'
              for xi in range(xPlot.getNumUnits()):
                if CyMap().isPlot(iiX,iiY):
                  xUnit = xPlot.getUnit(xi)
                  if ( xUnit.getUnitType() == gc.getInfoTypeForString('UNIT_MERCHANT_SHIP') or ( unitTeam.isAtWar( xUnit.getTeam() ) and ( xUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_NAVAL') or xUnit.plot().getTerrainType() == gc.getInfoTypeForString('TERRAIN_OCEAN') ) ) ) and xUnit.getID() != pUnit.getID():
                    iRangeToShip = -1
                    if iRangeToShip < int( math.fabs( xUnit.getX() - pUnit.getX() ) ):
                      iRangeToShip = int( math.fabs( xUnit.getX() - pUnit.getX() ) )
                    if iRangeToShip < int( math.fabs( xUnit.getY() - pUnit.getY() ) ):
                      iRangeToShip = int( math.fabs( xUnit.getY() - pUnit.getY() ) )
                    if iRangeToShip > -1 and iRange > iRangeToShip:
                      iRange = iRangeToShip
                      sBlock = ' limited by ' + gc.getPlayer(xUnit.getOwner()).getCivilizationAdjective(0) + ' ' + xUnit.getName() + ' actions...'
                      
          iModRange = iRange + pUnit.getLevel()
          
          iMerchantIncome = CyGame().getSorenRandNum(6*iModRange, "Merchant Mission") + iModRange * 1
          if iMerchantIncome > 0:
            CyInterface().addMessage(pUnit.getOwner(),false,25,'Your '+pUnit.getName()+' completes a merchant mission and gains '+str(iMerchantIncome)+'gp!  Merchanteering range '+str(iModRange-pUnit.getLevel())+'/15'+sBlock,'',1,pUnit.getButton(),ColorTypes(11),pUnit.getX(),pUnit.getY(),True,True)
            CyInterface().addCombatMessage(pUnit.getOwner(),'Your '+pUnit.getName()+' completes a merchant mission and gains '+str(iMerchantIncome)+'gp!  Merchanteering range '+str(iModRange-pUnit.getLevel())+'/15'+sBlock)
            pPlayer.setGold( pPlayer.getGold() + iMerchantIncome )
            pUnit.changeExperience( iModRange / 4, -1, False, False, False)
            self.generateLoot( pUnit, iModRange / 2 )

        ## Dragons change to the dragon race when fully promoted (from the orcish race...)
        if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_DRAGON'):
          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ORC')):
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ORC'), False)
            pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DRAGON'), True)

        ## Give Random XP to all Units
        iGiveXP = 15
        if pPlayer.isHuman():
          iGiveXP = 25
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO')):
          iGiveXP = 2
          if CyGame().getGameSpeedType() == gc.getInfoTypeForString('GAMESPEED_EPIC'):
            iGiveXP = 3
          if CyGame().getGameSpeedType() == gc.getInfoTypeForString('GAMESPEED_MARATHON'):
            iGiveXP = 4
        if iThisPlotTrainAnimal > 0 and iGiveXP > 5 and (pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ANIMAL') or pUnit.getRace() == gc.getInfoTypeForString('PROMOTION_ORC') or pUnit.getRace() == gc.getInfoTypeForString('PROMOTION_LIZARDMAN')):
          iThisPlotTrainAnimal -= 1
          iGiveXP = 5
        if iThisPlotTrain > 0 and iGiveXP > 10:
          iThisPlotTrain -= 1
          iGiveXP = 10
          if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ADEPT') and iImprovement == gc.getInfoTypeForString('IMPROVEMENT_TOWER'):
            iGiveXP = 4
        if pUnit.getUnitType() != gc.getInfoTypeForString('UNIT_HIDDEN_CACHE') and CyGame().getSorenRandNum(iGiveXP, "UnitExperience"+str(pUnit.getID())) == 1:
          pUnit.changeExperience(1, -1, False, False, False)

        ## Giant Sea Serpents can have young
        if ( pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_GIANT_SEA_SERPENT') and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FATIGUED')) and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CREEP')) ):
          iCountS = pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_GIANT_SEA_SERPENT'))
          iCountS += pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_SEA_SERPENT'))
          if ( CyGame().getSorenRandNum(30+iCountS, "NewSerpents") == 1 and iCountS < 60 ):
            oNewUnit = gc.getInfoTypeForString('UNIT_SEA_SERPENT')
            newUnit = pPlayer.initUnit(oNewUnit, pUnit.getX(), pUnit.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
            self.young(pUnit,newUnit)
            ## Serpent variation in the world
            if CyGame().getSorenRandNum(10, "NewSerpentWeak") < 4:
              newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'),True)
            else:
              if CyGame().getSorenRandNum(10, "NewSerpentStrong") > 7:
                newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG'),True)
            if CyGame().getSorenRandNum(10, "NewSerpentLight") < 4:
              newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LIGHT'),True)
            else:
              if CyGame().getSorenRandNum(10, "NewSerpentHeavy") > 7:
                newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HEAVY'),True)

        ## Giant Sea Serpents can die of old age (if over populated - shouldn't happen now, but fixes a current bug after-effect)
        if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_GIANT_SEA_SERPENT') and pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_GIANT_SEA_SERPENT')) > 60 and pUnit.getLevel() < 5:
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_TREASURE1'), False)
          pUnit.kill(True,0)
          
        ## Sea Serpents and Giant Sea Serpents have random strength  
        if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_SEA_SERPENT') and self.getObjectInt(pUnit,'ss') == 0:
          self.setObjectInt(pUnit,'ss',1)
          pUnit.setBaseCombatStr( CyGame().getSorenRandNum(4, "NewSerpentStr") + 6 )
          pUnit.setBaseCombatStrDefense( CyGame().getSorenRandNum(4, "NewSerpentDef") + 6 )
        if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_GIANT_SEA_SERPENT') and self.getObjectInt(pUnit,'gss') == 0:
          self.setObjectInt(pUnit,'gss',1)
          pUnit.setBaseCombatStr( CyGame().getSorenRandNum(5, "NewSerpentStr") + 9 )
          pUnit.setBaseCombatStrDefense( CyGame().getSorenRandNum(5, "NewSerpentDef") + 9 )

        ## Angels become evil if owned by an evil player...
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ANGEL')) and pPlayer.getAlignment() == iEvil and not pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_BRIGIT_HELD') and pUnit.getDuration() < 1:
          iRoll = CyGame().getSorenRandNum(6, "Fallen Angel")
          if iRoll == 1:
            oNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_TAR_DEMON'), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
          elif iRoll == 2:
            oNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_SUCCUBUS'), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
          elif iRoll == 3:
            oNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_PIT_BEAST'), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
          elif iRoll == 4:
            oNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_IMP'), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
          elif iRoll == 5:
            oNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_STYGIAN_GUARD'), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
          else:
            oNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_CHAOS_MARAUDER'), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
          sMsg = 'An ' + pUnit.getName() + ' turns evil!'
          CyInterface().addMessage(pUnit.getOwner(),false,25,sMsg,'AS3D_SPELL_BLESS',1,pUnit.getButton(),ColorTypes(7),pUnit.getX(),pUnit.getY(),True,True)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ANGEL'), False)
          oNewUnit.convert(pUnit)

        ## Barbarian Baby Serpents grow up
        if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_SEA_SERPENT') and pUnit.getLevel() > 3 and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FATIGUED')) and pPlayer.isBarbarian():
          oNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_GIANT_SEA_SERPENT'), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FATIGUED'), True)
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CREEP'), True)
          oNewUnit.convert(pUnit)

        ## Animals can have young
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_PROLIFIC3')):
          iBirth = 7
        elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_PROLIFIC2')):  
          iBirth = 4
        elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_PROLIFIC')): 
          iBirth = 2
        else:
          if pPlayer.isHuman():
            iBirth = 0
            if pUnit.getLevel() > 4:
              iBirth = 1
          else:
            iBirth = pUnit.getLevel() - 5
            
        if (bCanCreateUnit and CyGame().getSorenRandNum(100, "NewAnimal") < iBirth and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FATIGUED')) and (pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ANIMAL'))):
          pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FATIGUED'), True)
          if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_GIANT_SPIDER'):
            oNewUnit = gc.getInfoTypeForString('UNIT_BABY_SPIDER')
          else:
            oNewUnit = pUnit.getUnitType()
          newUnit = pPlayer.initUnit(oNewUnit, pUnit.getX(), pUnit.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
          self.young(pUnit,newUnit)

        ## Baby Spiders can grow up
        if (CyGame().getSorenRandNum(50, "NewSpiders") == 1 and pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_BABY_SPIDER')):
          oNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_GIANT_SPIDER'), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
          oNewUnit.convert(pUnit)
          oNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FATIGUED'), False)
          
        ## Plagues may spread from a plague carrier
        if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUE_CARRIER')):
          iPlagueSpread = CyGame().getSorenRandNum(100, "PlagueSpread")
          iPlagueSpreadChance = ( pUnit.getLevel() + pUnit.baseCombatStr() ) / 2
          if iPlagueSpread < iPlagueSpreadChance:
            lUnits = []
            iX = pUnit.getX()
            iY = pUnit.getY()
            iR = iPlagueSpreadChance
            for iiX in range(iX-iR, iX+iR+1, 1):
              for iiY in range(iY-iR, iY+iR+1, 1):
                plpPlot = CyMap().plot(iiX,iiY)
                for i in range(plpPlot.getNumUnits()):
                  plpUnit = plpPlot.getUnit(i)
                  if gc.getTeam(pUnit.getTeam()).isAtWar(pPlayer.getTeam()) and not plpUnit.getUnitType() == gc.getInfoTypeForString('UNIT_HIDDEN_CACHE'):
                    if plpUnit.isAlive() and not plpUnit.isDelayedDeath() and not plpUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_IMMUNE_DISEASE')):
                      lUnits.append(pLoopUnit)
            if len(lUnits) > 0:
              plpUnit = lUnits[CyGame().getSorenRandNum(len(lUnits), "The Plague!")-1]
              plpUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED'), True)
              sMsg = plpUnit.getName() + ' contracts the plague from ' + pUnit.getName() + '!'
              CyInterface().addMessage(plpUnit.getOwner(),False,25,sMsg,'AS2D_FEATUREGROWTH',1,'Art/Interface/Buttons/Promotions/plagued.dds',ColorTypes(7),plpUnit.getX(),plpUnit.getY(),True,True)
              CyInterface().addCombatMessage(plpUnit.getOwner(),sMsg)
              CyInterface().addMessage(pUnit.getOwner(),False,25,sMsg,'AS2D_FEATUREGROWTH',1,'Art/Interface/Buttons/Promotions/plagued.dds',ColorTypes(14),pUnit.getX(),pUnit.getY(),True,True)
              CyInterface().addCombatMessage(pUnit.getOwner(),sMsg)

        ## Disease and Plague causes damage over time and can be recovered from
        if (pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DISEASED')) or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED')) or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED'))):
          iRecover = 3 - int( pUnit.getDamage() / 10 )
          if not pPlayer.isHuman():
            iRecover += 10
          if pPlot.isCity() == True:
            iRecover += 2
            pCity = pUnit.plot().getPlotCity()
            if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_HERBALIST')) > 0:
              iRecover += 2
            if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_INFIRMARY')) > 0:
              iRecover += 4
          if iRecover < 1:
            iRecover = CyGame().getSorenRandNum(3, "MiracleRecovery")

          iDamage = 10 + int( pUnit.getDamage() / 10 )
          iHalfDamage = int( iDamage / 2 )

          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED')):
            if pUnit.getDamage() < 3 or not pUnit.isAlive():
              pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED'), False)
            else:
              pUnit.doDamageNoCaster(iHalfDamage, 100, gc.getInfoTypeForString('DAMAGE_POISON'), False)

          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DISEASED')):
            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_IMMUNE_DISEASE')) or not pUnit.isAlive():
              pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DISEASED'), False)
            else:
              iDiseaseInPlot += 1
              pUnit.doDamageNoCaster(iDamage, 100, gc.getInfoTypeForString('DAMAGE_POISON'), False)
              if CyGame().getSorenRandNum(100, "RecoverDisease") < iRecover:
                pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DISEASED'), False)
                pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IMMUNE_DISEASE'), True)
                sMsg = pUnit.getName() + ' recovers from a disease!'
                CyInterface().addMessage(pUnit.getOwner(),false,25,sMsg,'AS2D_FEATUREGROWTH',1,pUnit.getButton(),ColorTypes(7),pUnit.getX(),pUnit.getY(),True,True)
            
          if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED')):
            if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_IMMUNE_DISEASE')) or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUE_CARRIER')) or not pUnit.isAlive():
              pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED'), False)
            else:
              iPlagueInPlot += 1
              pUnit.doDamageNoCaster(iDamage, 100, gc.getInfoTypeForString('DAMAGE_POISON'), False)
              if CyGame().getSorenRandNum(100, "RecoverPlague") < iRecover / 2:
                pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED'), False)
                pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IMMUNE_DISEASE'), True)
                sMsg = pUnit.getName() + ' recovers from the plague!'
                CyInterface().addMessage(pUnit.getOwner(),false,25,sMsg,'AS2D_FEATUREGROWTH',1,pUnit.getButton(),ColorTypes(7),pUnit.getX(),pUnit.getY(),True,True)

        ## Jungles can cause disease and Disease and Plague can spread
        if pPlot.getFeatureType() == iJungle:
          iJunglePlot = 2
        else:
          iJunglePlot = 0
        if pPlot.getFeatureType() == iJungle or iDiseaseInPlot > 0 or iPlagueInPlot > 0:
          if pUnit.isAlive():
            if not pUnit.getRace() == gc.getInfoTypeForString('PROMOTION_ORC') and not pUnit.getRace() == gc.getInfoTypeForString('PROMOTION_LIZARDMAN'):
              if (pUnit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_ANIMAL') and pUnit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_BEAST')):
                if not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_IMMUNE_DISEASE')):
                  if not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DISEASED')) and CyGame().getSorenRandNum(100, "JungleFever") < iJunglePlot + iDiseaseInPlot * iDisMult + pUnit.getDamage() / 10 - iTreat * iDisMult:
                    pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DISEASED'), True)
                    sMsg = pUnit.getName() + ' contracts a disease!'
                    CyInterface().addMessage(pUnit.getOwner(),false,25,sMsg,'AS2D_FEATUREGROWTH',1,'Art/Interface/Buttons/Promotions/diseased.dds',ColorTypes(7),pUnit.getX(),pUnit.getY(),True,True)
                  if not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED')) and CyGame().getSorenRandNum(100, "ThePlague") < iPlagueInPlot * iDisMult * 2 + pUnit.getDamage() / 5 - iTreat * iDisMult and iPlagueInPlot > 0:
                    pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED'), True)
                    sMsg = pUnit.getName() + ' contracts the plague!'
                    CyInterface().addMessage(pUnit.getOwner(),false,25,sMsg,'AS2D_FEATUREGROWTH',1,'Art/Interface/Buttons/Promotions/plagued.dds',ColorTypes(7),pUnit.getX(),pUnit.getY(),True,True)
                    
        ## Flames damage living units
        if pPlot.getFeatureType() == iFlames:
          if (pUnit.isAlive() or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_UNDEAD'))) and pPlayer.isHuman():
            pUnit.doDamageNoCaster(35, 100, gc.getInfoTypeForString('DAMAGE_FIRE'), False)

        ## Snow tiles can damage living units
        if pPlot.getTerrainType() == iSnow and pUnit.isAlive() and pPlayer.isHuman() and not (pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ARCTIC_WARFARE')) or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WINTERBORN')) or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COLD_RESISTANCE'))):
          ## Do I have shelter?
          if not (pPlot.isCity() or iShelter > 0):
            iDam = CyGame().getSorenRandNum(25, "IceDamage") - pUnit.getLevel()
            if iDam > 0:
              pUnit.doDamageNoCaster(iDam, 100, gc.getInfoTypeForString('DAMAGE_COLD'), False)
              if iDam > 7:
                pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SLOW'), True)
              sMsg = 'Blistering wind, ice and cold inflicts ' + str(iDam) + ' damage on ' + pUnit.getName() + '...  (Seek shelter in a city, defensive structure or a warmer climate.)'
              CyInterface().addMessage(pUnit.getOwner(),false,25,sMsg,'AS3D_SPELL_CONTAGION',1,pUnit.getButton(),ColorTypes(7),pUnit.getX(),pUnit.getY(),True,True)
            
        if pUnit.getGameTurnCreated() == iGameTurn:
          self.tough(pUnit)
      
      if pPlot.isOwned():
        pPlayer = gc.getPlayer(pPlot.getOwner())
        iAlignment = pPlayer.getAlignment()

        ## Road Tax
        if pPlot.isRoute() and not pPlot.isRiver() and pPlayer.isHuman():
          if pPlot.getOwner() in iRoadTax:
            iRoadTax[pPlot.getOwner()] += 1
          else:
            iRoadTax[pPlot.getOwner()] = 1
            
        ## Desert Trading Income for the Malakim
        if pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_DESERT') and pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MALAKIM'):
          if pPlot.getOwner() in iRoadTax:
            iRoadTax[pPlot.getOwner()] -= 2
          else:
            iRoadTax[pPlot.getOwner()] = -2

        ## Check for Jungle Haunt Expiration
        if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_JUNGLE_FARM'): 
          bValidCiv = False
          bValidTerrain = False  
          if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CLAN_OF_EMBERS') or pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ILLIANS') or pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DOVIELLO'):
            bValidCiv = True
          if pPlot.getFeatureType() == iJungle or pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_SNOW') or pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_TUNDRA'):
            bValidTerrain = True
          if bValidCiv == False or bValidTerrain == False:  
            if CyGame().getSorenRandNum(100, "Haunt Expiration") < 5 or bValidTerrain == False:
              pPlot.setImprovementType(-1)
              CyInterface().addMessage(pPlot.getOwner(),false,25,'Hunting grounds fall into ruin...','AS2D_CHARM_PERSON',1,'Art/Interface/Buttons/Spells/Ressurection.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)

        if pPlayer.getCivilizationType() == iInfernal:
          pPlot.changePlotCounter(100)
          bUntouched = false
        if (bUntouched and pPlayer.getStateReligion() == iAshenVeil or (iCount >= 50 and iAlignment == iEvil) or (iCount >= 75 and iAlignment == iNeutral)):
          iX = pPlot.getX()
          iY = pPlot.getY()
          for iiX in range(iX-1, iX+2, 1):
            for iiY in range(iY-1, iY+2, 1):
              pAdjacentPlot = CyMap().plot(iiX,iiY)
              if pAdjacentPlot.isNone() == False:
                if pAdjacentPlot.getPlotCounter() > 10:
                  pPlot.changePlotCounter(1)
                  bUntouched = False
      if (bUntouched and pPlot.isOwned() == false and iCount > 25):
        iX = pPlot.getX()
        iY = pPlot.getY()
        for iiX in range(iX-1, iX+2, 1):
          for iiY in range(iY-1, iY+2, 1):
            pAdjacentPlot = CyMap().plot(iiX,iiY)
            if pAdjacentPlot.isNone() == False:
              if pAdjacentPlot.getPlotCounter() > 10:
                pPlot.changePlotCounter(1)
                bUntouched = False
      iPlotCount = pPlot.getPlotCounter()
      if (bUntouched and iPlotCount > 0):
        pPlot.changePlotCounter(-1)
      if iPlotCount > 9:
        if (iBonus == iSheep or iBonus == iPig):
          pPlot.setBonusType(iToad)
        if (iBonus == iHorse or iBonus == iCow):
          pPlot.setBonusType(iNightmare)
        if (iBonus == iCotton or iBonus == iSilk):
          pPlot.setBonusType(iRazorweed)
        if (iBonus == iBanana or iBonus == iSugar):
          pPlot.setBonusType(iGulagarm)
        if (iBonus == iMarble):
          pPlot.setBonusType(iSheutStone)
        if (iBonus == iCorn or iBonus == iRice or iBonus == iWheat):
          pPlot.setBonusType(-1)
          pPlot.setImprovementType(iSnakePillar)
      if iPlotCount < 10:
        if iBonus == iToad:
          if CyGame().getSorenRandNum(100, "Hell Convert") < 50:
            pPlot.setBonusType(iSheep)
          else:
            pPlot.setBonusType(iPig)
        if iBonus == iNightmare:
          if CyGame().getSorenRandNum(100, "Hell Convert 2") < 50:
            pPlot.setBonusType(iHorse)
          else:
            pPlot.setBonusType(iCow)
        if iBonus == iRazorweed:
          if CyGame().getSorenRandNum(100, "Hell Convert 3") < 50:
            pPlot.setBonusType(iCotton)
          else:
            pPlot.setBonusType(iSilk)
        if iBonus == iGulagarm:
          if CyGame().getSorenRandNum(100, "Hell Convert 4") < 50:
            pPlot.setBonusType(iBanana)
          else:
            pPlot.setBonusType(iSugar)
        if (iBonus == iSheutStone):
          pPlot.setBonusType(iMarble)
        if iImprovement == iSnakePillar:
          pPlot.setImprovementType(iFarm)
          iCount = CyGame().getSorenRandNum(100, "Hell Convert")
          if  iCount < 33:
            pPlot.setBonusType(iCorn)
          else:
            if iCount < 66:
              pPlot.setBonusType(iRice)
            else:
              pPlot.setBonusType(iWheat)
      if iTerrain == iBurningSands:
        if pPlot.isCity() == False:
          if pPlot.isPeak() == False:
            if CyGame().getSorenRandNum(100, "Flames") <= iFlamesSpreadChance:
              pPlot.setFeatureType(iFlames, 0)

      ## Recovering Forest will come back as jungle if adjacent to jungle and on grassland
      if iFeature == iForestBurnt and iTerrain == iGrass and CyGame().getSorenRandNum(100, "Jungle Grow") < 15:
        iX = pPlot.getX()
        iY = pPlot.getY()
        for iiX in range(iX-1, iX+2, 1):
          for iiY in range(iY-1, iY+2, 1):
            pAdjacentPlot = CyMap().plot(iiX,iiY)
            if pAdjacentPlot.getFeatureType() == iJungle:
              pPlot.setFeatureType(iJungle, 0)
              
    ## Road Taxes Assessed to Human Players
    for iPlayer in range(gc.getMAX_PLAYERS()):
      mPlayer = gc.getPlayer(iPlayer)
      pCity = mPlayer.getCity(self.iValidCity(mPlayer))
      if mPlayer.isAlive() and mPlayer.isHuman():
        if iPlayer not in iRoadTax:
          iRoadTax[iPlayer] = 0
        iTax = iRoadTax[iPlayer] / 4
        if iTax != 0:
          py = PyPlayer(iPlayer)
          sPD = cPickle.loads(mPlayer.getScriptData())
          mPlayer.setGold( mPlayer.getGold() - iTax )         
          sPD['CUSTOM_INCOME'] -= iTax

          ## Message Road Taxes when they change
          if 'ROAD_TAX' not in sPD:
            sPD['ROAD_TAX'] = 0
          if iTax != sPD['ROAD_TAX']:
            sPD['ROAD_TAX'] = iTax
            if iTax > 0:
              sMsg = 'Road Taxes Change: ' + str(iTax) + ' per turn'
            else:
              if mPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MALAKIM'):
                sMsg = 'Desert Trading and '
              else:  
                sMsg = ''
              sMsg = sMsg + 'Unit Fortification Income (1/4 fully fortified units): ' + str(iTax * -1) + ' per turn'
            CyInterface().addMessage(iPlayer,false,25,sMsg,'',1,'Art/Interface/Buttons/Units/Commander.dds',ColorTypes(8),pCity.getX(),pCity.getY(),True,True)
            CyInterface().addCombatMessage(iPlayer,sMsg)

          mPlayer.setScriptData(cPickle.dumps(sPD))
          
    ## Score Victory?
    self.finalWar()
        

  def doTurnKhazad(self, iPlayer):
    pPlayer = gc.getPlayer(iPlayer)
    if pPlayer.getNumCities() > 0:
      iVault1 = gc.getInfoTypeForString('BUILDING_DWARVEN_VAULT_EMPTY')
      iVault2 = gc.getInfoTypeForString('BUILDING_DWARVEN_VAULT_LOW')
      iVault3 = gc.getInfoTypeForString('BUILDING_DWARVEN_VAULT')
      iVault4 = gc.getInfoTypeForString('BUILDING_DWARVEN_VAULT_STOCKED')
      iVault5 = gc.getInfoTypeForString('BUILDING_DWARVEN_VAULT_ABUNDANT')
      iVault6 = gc.getInfoTypeForString('BUILDING_DWARVEN_VAULT_FULL')
      iVault7 = gc.getInfoTypeForString('BUILDING_DWARVEN_VAULT_OVERFLOWING')
      iGold = pPlayer.getGold() / pPlayer.getNumCities()
      if iGold <= 49:
        iNewVault = iVault1
      if (iGold >= 50 and iGold <= 99):
        iNewVault = iVault2
      if (iGold >= 100 and iGold <= 149):
        iNewVault = iVault3
      if (iGold >= 150 and iGold <= 199):
        iNewVault = iVault4
      if (iGold >= 200 and iGold <= 299):
        iNewVault = iVault5
      if (iGold >= 300 and iGold <= 499):
        iNewVault = iVault6
      if iGold >= 500:
        iNewVault = iVault7
      for pyCity in PyPlayer(iPlayer).getCityList():
        pCity = pyCity.GetCy()
        pCity.setNumRealBuilding(iVault1, 0)
        pCity.setNumRealBuilding(iVault2, 0)
        pCity.setNumRealBuilding(iVault3, 0)
        pCity.setNumRealBuilding(iVault4, 0)
        pCity.setNumRealBuilding(iVault5, 0)
        pCity.setNumRealBuilding(iVault6, 0)
        pCity.setNumRealBuilding(iVault7, 0)
        pCity.setNumRealBuilding(iNewVault, 1)

  def doTurnLuchuirp(self, iPlayer):
    if gc.getPlayer(iPlayer).getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_BARNAXUS')) > 0:
      py = PyPlayer(iPlayer)
      pBarnaxus = -1
      bEmp1 = False
      bEmp2 = False
      bEmp3 = False
      bEmp4 = False
      bEmp5 = False
      iBarnaxus = gc.getInfoTypeForString('UNITCLASS_BARNAXUS')
      iCombat1 = gc.getInfoTypeForString('PROMOTION_COMBAT1')
      iCombat2 = gc.getInfoTypeForString('PROMOTION_COMBAT2')
      iCombat3 = gc.getInfoTypeForString('PROMOTION_COMBAT3')
      iCombat4 = gc.getInfoTypeForString('PROMOTION_COMBAT4')
      iCombat5 = gc.getInfoTypeForString('PROMOTION_COMBAT5')
      iEmpower1 = gc.getInfoTypeForString('PROMOTION_EMPOWER1')
      iEmpower2 = gc.getInfoTypeForString('PROMOTION_EMPOWER2')
      iEmpower3 = gc.getInfoTypeForString('PROMOTION_EMPOWER3')
      iEmpower4 = gc.getInfoTypeForString('PROMOTION_EMPOWER4')
      iEmpower5 = gc.getInfoTypeForString('PROMOTION_EMPOWER5')
      iGolem = gc.getInfoTypeForString('PROMOTION_GOLEM')

      lGolems = []
      for pUnit in py.getUnitList():
        if pUnit.getUnitClassType() == iBarnaxus :
          pBarnaxus = pUnit
        elif pUnit.isHasPromotion(iGolem) :
          lGolems.append(pUnit)
      if pBarnaxus != -1 :
        bEmp1 = bool(pBarnaxus.isHasPromotion(iCombat1))
        bEmp2 = bool(pBarnaxus.isHasPromotion(iCombat2))
        bEmp3 = bool(pBarnaxus.isHasPromotion(iCombat3))
        bEmp4 = bool(pBarnaxus.isHasPromotion(iCombat4))
        bEmp5 = bool(pBarnaxus.isHasPromotion(iCombat5))
      for pUnit in lGolems :
        pUnit.setHasPromotion(iEmpower1, False)
        pUnit.setHasPromotion(iEmpower2, False)
        pUnit.setHasPromotion(iEmpower3, False)
        pUnit.setHasPromotion(iEmpower4, False)
        pUnit.setHasPromotion(iEmpower5, False)
        if bEmp1:
          pUnit.setHasPromotion(iEmpower1, True)
        if bEmp2:
          pUnit.setHasPromotion(iEmpower2, True)
        if bEmp3:
          pUnit.setHasPromotion(iEmpower3, True)
        if bEmp4:
          pUnit.setHasPromotion(iEmpower4, True)
        if bEmp5:
          pUnit.setHasPromotion(iEmpower5, True)

  def findClearPlot(self, pUnit, plot):
    BestPlot = -1
    iBestPlot = 0
    if pUnit == -1:
      iX = plot.getX()
      iY = plot.getY()
      for iiX in range(iX-1, iX+2, 1):
        for iiY in range(iY-1, iY+2, 1):
          iCurrentPlot = 0
          pPlot = CyMap().plot(iiX,iiY)
          if pPlot.isNone() == False:
            if pPlot.getNumUnits() == 0:
              if (pPlot.isWater() == plot.isWater() and pPlot.isPeak() == False and pPlot.isCity() == False):
                iCurrentPlot = iCurrentPlot + 5
            if iCurrentPlot >= 1:
              iCurrentPlot = iCurrentPlot + CyGame().getSorenRandNum(5, "FindClearPlot")
              if iCurrentPlot >= iBestPlot:
                BestPlot = pPlot
                iBestPlot = iCurrentPlot
      return BestPlot
    iX = pUnit.getX()
    iY = pUnit.getY()
    for iiX in range(iX-1, iX+2, 1):
      for iiY in range(iY-1, iY+2, 1):
        iCurrentPlot = 0
        pPlot = CyMap().plot(iiX,iiY)
        if pPlot.isNone() == False:
          if pPlot.getNumUnits() == 0:
            if pUnit.canMoveOrAttackInto(pPlot, False):
              iCurrentPlot = iCurrentPlot + 5
          for i in range(pPlot.getNumUnits()):
            if pPlot.getUnit(i).getOwner() == pUnit.getOwner():
              if pUnit.canMoveOrAttackInto(pPlot, False):
                iCurrentPlot = iCurrentPlot + 15
          if pPlot.isCity():
            if pPlot.getPlotCity().getOwner() == pUnit.getOwner():
              iCurrentPlot = iCurrentPlot + 50
          if (iX == iiX and iY == iiY):
            iCurrentPlot = 0
          if iCurrentPlot >= 1:
            iCurrentPlot = iCurrentPlot + CyGame().getSorenRandNum(5, "FindClearPlot")
            if iCurrentPlot >= iBestPlot:
              BestPlot = pPlot
              iBestPlot = iCurrentPlot
    return BestPlot

  def genesis(self, iPlayer):
    iBrokenLands = gc.getInfoTypeForString('TERRAIN_BROKEN_LANDS')
    iBurningSands = gc.getInfoTypeForString('TERRAIN_BURNING_SANDS')
    iDesert = gc.getInfoTypeForString('TERRAIN_DESERT')
    iFields = gc.getInfoTypeForString('TERRAIN_FIELDS_OF_PERDITION')
    iGrass = gc.getInfoTypeForString('TERRAIN_GRASS')
    iSnow = gc.getInfoTypeForString('TERRAIN_SNOW')
    iTundra = gc.getInfoTypeForString('TERRAIN_TUNDRA')
    iPlains = gc.getInfoTypeForString('TERRAIN_PLAINS')
    iForestAncient = gc.getInfoTypeForString('FEATURE_FOREST_ANCIENT')
    iForest = gc.getInfoTypeForString('FEATURE_FOREST')
    for i in range (CyMap().numPlots()):
      pPlot = CyMap().plotByIndex(i)
      if pPlot.getOwner() == iPlayer:
        iTerrain = pPlot.getTerrainType()
        if iTerrain == iSnow:
          pPlot.setTerrainType(iTundra,True,True)
        if iTerrain == iTundra:
          pPlot.setTerrainType(iPlains,True,True)
        if (iTerrain == iDesert or iTerrain == iBurningSands):
          pPlot.setTerrainType(iPlains,True,True)
        if (iTerrain == iPlains or iTerrain == iFields or iTerrain == iBrokenLands):
          pPlot.setTerrainType(iGrass,True,True)
        if (iTerrain == iGrass and pPlot.getImprovementType() == -1 and pPlot.getFeatureType() != iForestAncient and pPlot.isPeak() == False and pPlot.isCity() == False):
          pPlot.setFeatureType(iForest, 0)
        pPlot.changePlotCounter(-100)

  def getAshenVeilCity(self, iNum):
    iInfernal = gc.getInfoTypeForString('CIVILIZATION_INFERNAL')
    iVeil = gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL')
    iBestValue1 = 0
    iBestValue2 = 0
    iBestValue3 = 0
    pBestCity1 = -1
    pBestCity2 = -1
    pBestCity3 = -1
    for iPlayer in range(gc.getMAX_PLAYERS()):
      pPlayer = gc.getPlayer(iPlayer)
      pTeam = gc.getTeam(pPlayer.getTeam())
      if ( pPlayer.isAlive() and pPlayer.getCivilizationType() != iInfernal and iPlayer != pTeam.getLeaderID() ):
        for pyCity in PyPlayer(iPlayer).getCityList():
          pCity = pyCity.GetCy()
          if (pCity.isHasReligion(iVeil) and pCity.isCapital() == False):
            bValid = True
            iValue = pCity.getPopulation() * 100
            iValue += pCity.getCulture(iPlayer) / 3
            iValue += pCity.getNumBuildings() * 10
            iValue += pCity.getNumWorldWonders() * 100
            iValue += pCity.countNumImprovedPlots()
            if iValue > iBestValue1:
              iBestValue3 = iBestValue2
              pBestCity3 = pBestCity2
              iBestValue2 = iBestValue1
              pBestCity2 = pBestCity1
              iBestValue1 = iValue
              pBestCity1 = pCity
              bValid = False
            if (bValid and iValue > iBestValue2):
              iBestValue3 = iBestValue2
              pBestCity3 = pBestCity2
              iBestValue2 = iValue
              pBestCity2 = pCity
              bValid = False
            if (bValid and iValue > iBestValue3):
              iBestValue3 = iValue
              pBestCity3 = pCity
    if iNum == 1:
      return pBestCity1
    if iNum == 2:
      return pBestCity2
    if iNum == 3:
      return pBestCity3
    return -1

  def getCivilization(self, iCiv):
    i = -1
    for iPlayer in range(gc.getMAX_PLAYERS()):
      pPlayer = gc.getPlayer(iPlayer)
      if pPlayer.getCivilizationType() == iCiv:
        i = iPlayer
    return i

  def getHero(self, pPlayer):
    iHero = -1
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BANNOR'):
      iHero = gc.getInfoTypeForString('UNITCLASS_DONAL')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MALAKIM'):
      iHero = gc.getInfoTypeForString('UNITCLASS_TEUTORIX')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ELOHIM'):
      iHero = gc.getInfoTypeForString('UNITCLASS_CORLINDALE')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MERCURIANS'):
      iHero = gc.getInfoTypeForString('UNITCLASS_BASIUM')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LANUN'):
      iHero = gc.getInfoTypeForString('UNITCLASS_GUYBRUSH')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KURIOTATES'):
      iHero = gc.getInfoTypeForString('UNITCLASS_EURABATRES')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'):
      iHero = gc.getInfoTypeForString('UNITCLASS_GILDEN')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KHAZAD'):
      iHero = gc.getInfoTypeForString('UNITCLASS_MAROS')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_HIPPUS'):
      iHero = gc.getInfoTypeForString('UNITCLASS_MAGNADINE')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_AMURITES'):
      iHero = gc.getInfoTypeForString('UNITCLASS_GOVANNON')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BALSERAPHS'):
      iHero = gc.getInfoTypeForString('UNITCLASS_LOKI')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CLAN_OF_EMBERS'):
      iHero = gc.getInfoTypeForString('UNITCLASS_RANTINE')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SVARTALFAR'):
      iHero = gc.getInfoTypeForString('UNITCLASS_ALAZKAN')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CALABIM'):
      iHero = gc.getInfoTypeForString('UNITCLASS_LOSHA')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SHEAIM'):
      iHero = gc.getInfoTypeForString('UNITCLASS_ABASHI')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SIDAR'):
      iHero = gc.getInfoTypeForString('UNITCLASS_RATHUS')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ILLIANS'):
      iHero = gc.getInfoTypeForString('UNITCLASS_WILBOMAN')
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_INFERNAL'):
      iHero = gc.getInfoTypeForString('UNITCLASS_HYBOREM')
    return iHero

  def getLeader(self, iLeader):
    i = -1
    for iPlayer in range(gc.getMAX_PLAYERS()):
      pPlayer = gc.getPlayer(iPlayer)
      if pPlayer.getLeaderType() == iLeader:
        i = iPlayer
    return i

  def getOpenPlayer(self):
    i = -1
    for iPlayer in range(gc.getMAX_PLAYERS()):
      pPlayer = gc.getPlayer(iPlayer)
      if (pPlayer.isEverAlive() == False and i == -1):
        i = iPlayer
    return i

  def getUnholyVersion(self, pUnit):
    iUnit = -1
    if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ADEPT'):
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
        iUnit = gc.getInfoTypeForString('UNIT_IMP')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
        iUnit = gc.getInfoTypeForString('UNIT_MAGE')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
        iUnit = gc.getInfoTypeForString('UNIT_LICH')
    if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ANIMAL') or pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_BEAST'):
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 1:
        iUnit = gc.getInfoTypeForString('UNIT_SCOUT')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
        iUnit = gc.getInfoTypeForString('UNIT_HELLHOUND')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
        iUnit = gc.getInfoTypeForString('UNIT_ASSASSIN')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
        iUnit = gc.getInfoTypeForString('UNIT_BEAST_OF_AGARES')
    if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ARCHER'):
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
        iUnit = gc.getInfoTypeForString('UNIT_ARCHER')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
        iUnit = gc.getInfoTypeForString('UNIT_LONGBOWMAN')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
        iUnit = gc.getInfoTypeForString('UNIT_CROSSBOWMAN')
    if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_DISCIPLE'):
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
        iUnit = gc.getInfoTypeForString('UNIT_DISCIPLE_THE_ASHEN_VEIL')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
        iUnit = gc.getInfoTypeForString('UNIT_PRIEST_OF_THE_VEIL')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
        iUnit = gc.getInfoTypeForString('UNIT_EIDOLON')
    if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_MELEE'):
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 1:
        iUnit = gc.getInfoTypeForString('UNIT_SKELETON')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
        iUnit = gc.getInfoTypeForString('UNIT_DISEASED_CORPSE')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
        iUnit = gc.getInfoTypeForString('UNIT_CHAMPION')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
        iUnit = gc.getInfoTypeForString('UNIT_BALOR')
    if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_MOUNTED'):
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
        iUnit = gc.getInfoTypeForString('UNIT_HORSEMAN')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
        iUnit = gc.getInfoTypeForString('UNIT_CHARIOT')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
        iUnit = gc.getInfoTypeForString('UNIT_DEATH_KNIGHT')
    if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_RECON'):
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 1:
        iUnit = gc.getInfoTypeForString('UNIT_SCOUT')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
        iUnit = gc.getInfoTypeForString('UNIT_HELLHOUND')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
        iUnit = gc.getInfoTypeForString('UNIT_ASSASSIN')
      if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
        iUnit = gc.getInfoTypeForString('UNIT_BEASTMASTER')
    return iUnit

  def getUnitPlayerID(self, pUnit):
    pPlayer = gc.getPlayer(pUnit.getOwner())
    iID = pUnit.getID()
    iUnitID = -1
    for iUnit in range(pPlayer.getNumUnits()):
      pLoopUnit = pPlayer.getUnit(iUnit)
      if pLoopUnit.getID() == iID:
        iUnitID = iUnit
    return iUnitID

  def giftUnit(self, iUnit, iCivilization, iXP, pFromPlot, iFromPlayer):
    iAngel = gc.getInfoTypeForString('UNIT_ANGEL')
    iManes = gc.getInfoTypeForString('UNIT_MANES')
    if (iUnit == iAngel or iUnit == iManes):
      iChance = 100 - (CyGame().countCivPlayersAlive() * 3)
      iChance = iChance + iXP
      if iChance < 5:
        iChance = 5
      if iChance > 95:
        iChance = 95
      if CyGame().getSorenRandNum(100, "Gift Unit") > iChance:
        iUnit = -1
    if iUnit != -1:
      bValid = False
      for iPlayer in range(gc.getMAX_PLAYERS()):
        pPlayer = gc.getPlayer(iPlayer)
        if (pPlayer.isAlive()):
          if pPlayer.getCivilizationType() == iCivilization:
            py = PyPlayer(iPlayer)
            if pPlayer.getNumCities() > 0:
              iRnd = CyGame().getSorenRandNum(py.getNumCities(), "Gift Unit")
              pCity = py.getCityList()[iRnd]
              pPlot = pCity.plot()
              newUnit = pPlayer.initUnit(iUnit, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
              newUnit.changeExperience(iXP, -1, false, false, false)
              newUnit.setWeapons()
              if (pFromPlot != -1 and gc.getPlayer(iFromPlayer).isHuman()):
                bValid = True
              if pPlayer.isHuman():
                if iUnit == iManes:
                  CyInterface().addMessage(iPlayer,True,25,CyTranslator().getText("TXT_KEY_MESSAGE_ADD_MANES",()),'AS2D_UNIT_FALLS',1,'Art/Interface/Buttons/Promotions/Demon.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
                if iUnit == iAngel:
                  CyInterface().addMessage(iPlayer,True,25,CyTranslator().getText("TXT_KEY_MESSAGE_ADD_ANGEL",()),'AS2D_UNIT_FALLS',1,'Art/Interface/Buttons/Promotions/Angel.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
              if (pPlayer.isHuman() == False and iUnit == iManes and pCity != -1):
                if CyGame().getSorenRandNum(100, "Manes") < (100 - (pCity.getPopulation() * 5)):
                  pCity.changePopulation(1)
                  newUnit.kill(True, PlayerTypes.NO_PLAYER)
      if bValid:
        if iUnit == iManes:
          CyInterface().addMessage(iFromPlayer,True,25,CyTranslator().getText("TXT_KEY_MESSAGE_UNIT_FALLS",()),'AS2D_UNIT_FALLS',1,'Art/Interface/Buttons/Promotions/Demon.dds',ColorTypes(7),pFromPlot.getX(),pFromPlot.getY(),True,True)
        if iUnit == iAngel:
          CyInterface().addMessage(iFromPlayer,True,25,CyTranslator().getText("TXT_KEY_MESSAGE_UNIT_RISES",()),'AS2D_UNIT_FALLS',1,'Art/Interface/Buttons/Promotions/Angel.dds',ColorTypes(7),pFromPlot.getX(),pFromPlot.getY(),True,True)

  def placeTreasure(self, iPlayer, iUnit):
    pPlayer = gc.getPlayer(iPlayer)
    pBestPlot = -1
    iBestPlot = -1
    for i in range (CyMap().numPlots()):
      pPlot = CyMap().plotByIndex(i)
      iPlot = -1
      if not pPlot.isWater():
        if pPlot.getNumUnits() == 0:
          if not pPlot.isCity():
            if not pPlot.isImpassable():
              iPlot = CyGame().getSorenRandNum(1000, "Add Unit")
              if pPlot.area().getNumTiles() < 8:
                iPlot += 1000
              if not pPlot.isOwned():
                iPlot += 1000
              if iPlot > iBestPlot:
                iBestPlot = iPlot
                pBestPlot = pPlot
    if iBestPlot != -1:
      newUnit = pPlayer.initUnit(iUnit, pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
      CyInterface().addMessage(iPlayer,True,25,CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_TREASURE",()),'',1,'Art/Interface/Buttons/Equipment/Treasure.dds',ColorTypes(8),newUnit.getX(),newUnit.getY(),True,True)
      CyCamera().JustLookAtPlot(pBestPlot)

  def showUniqueImprovements(self, iPlayer):
    pPlayer = gc.getPlayer(iPlayer)
    iTeam = pPlayer.getTeam()
    for i in range (CyMap().numPlots()):
      pPlot = CyMap().plotByIndex(i)
      if pPlot.getImprovementType() != -1:
        if gc.getImprovementInfo(pPlot.getImprovementType()).isUnique():
          pPlot.setRevealed(iTeam, True, False, TeamTypes.NO_TEAM)

  def startWar(self, iPlayer, i2Player, iWarPlan):
    iTeam = gc.getPlayer(iPlayer).getTeam()
    i2Team = gc.getPlayer(i2Player).getTeam()
    eTeam = gc.getTeam(iTeam)
    e2Team = gc.getTeam(i2Team)
    if eTeam.isAlive():
      if e2Team.isAlive():
        if not eTeam.isAtWar(i2Team):
          if iTeam != i2Team:
            if eTeam.isHasMet(i2Team):
              if not eTeam.isPermanentWarPeace(i2Team):
                eTeam.declareWar(i2Team, false, iWarPlan)

  def warScript(self, iPlayer):
    pPlayer = gc.getPlayer(iPlayer)
    iEnemy = -1
    for iPlayer2 in range(gc.getMAX_PLAYERS()):
      pPlayer2 = gc.getPlayer(iPlayer2)
      if pPlayer2.isAlive():
        iTeam = gc.getPlayer(iPlayer).getTeam()
        iTeam2 = gc.getPlayer(iPlayer2).getTeam()
        eTeam = gc.getTeam(iTeam)
        if eTeam.isAVassal() == False:
          if eTeam.isAtWar(iTeam2):
            if CyGame().getSorenRandNum(100, "War Script") < 5:
              self.dogpile(iPlayer, iPlayer2)
          if self.warScriptAllow(iPlayer, iPlayer2):
            if pPlayer2.getBuildingClassMaking(gc.getInfoTypeForString('BUILDINGCLASS_TOWER_OF_MASTERY')) > 0:
              if eTeam.getAtWarCount(True) == 0:
                self.startWar(iPlayer, iPlayer2, WarPlanTypes.WARPLAN_TOTAL)
            if (pPlayer2.getNumBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_DIVINE')) > 0 or pPlayer2.getNumBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_EXALTED')) > 0):
              if pPlayer.getAlignment() == gc.getInfoTypeForString('ALIGNMENT_EVIL'):
                if eTeam.getAtWarCount(True) == 0:
                  self.startWar(iPlayer, iPlayer2, WarPlanTypes.WARPLAN_TOTAL)
            if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MERCURIANS'):
              if pPlayer2.getStateReligion() == gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL'):
                self.startWar(iPlayer, iPlayer2, WarPlanTypes.WARPLAN_TOTAL)
            if CyGame().getGlobalCounter() > 20:
              if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SVARTALFAR'):
                if (pPlayer2.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR') and CyGame().getPlayerRank(iPlayer) > CyGame().getPlayerRank(iPlayer2)):
                  self.startWar(iPlayer, iPlayer2, WarPlanTypes.WARPLAN_TOTAL)
              if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'):
                if (pPlayer2.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SVARTALFAR') and CyGame().getPlayerRank(iPlayer) > CyGame().getPlayerRank(iPlayer2)):
                  self.startWar(iPlayer, iPlayer2, WarPlanTypes.WARPLAN_TOTAL)
            if (CyGame().getGlobalCounter() > 40 or pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_INFERNAL') or pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DOVIELLO')):
              if pPlayer.getAlignment() == gc.getInfoTypeForString('ALIGNMENT_EVIL'):
                if (eTeam.getAtWarCount(True) == 0 and CyGame().getPlayerRank(iPlayer2) > CyGame().getPlayerRank(iPlayer)):
                  if (iEnemy == -1 or CyGame().getPlayerRank(iPlayer2) > CyGame().getPlayerRank(iEnemy)):
                    iEnemy = iPlayer2
    if iEnemy != -1:
      if CyGame().getPlayerRank(iPlayer) > CyGame().getPlayerRank(iEnemy):
        self.startWar(iPlayer, iEnemy, WarPlanTypes.WARPLAN_TOTAL)

  def warScriptAllow(self, iPlayer, iPlayer2):
    pPlayer = gc.getPlayer(iPlayer)
    pPlayer2 = gc.getPlayer(iPlayer2)
    iTeam = gc.getPlayer(iPlayer).getTeam()
    iTeam2 = gc.getPlayer(iPlayer2).getTeam()
    eTeam = gc.getTeam(iTeam)
    if iPlayer == gc.getBARBARIAN_PLAYER():
      return False
    if eTeam.isHasMet(iTeam2) == False:
      return False
    if eTeam.AI_getAtPeaceCounter(iTeam2) < 20:
      return False
#   if pPlayer.AI_getAttitude(iPlayer2) <= gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getDeclareWarRefuseAttitudeThreshold():
#     return False
    if eTeam.isAtWar(iTeam2):
      return False
    if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_INFERNAL'):
      if pPlayer2.getStateReligion() == gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL'):
        return False
    return True

  def dogpile(self, iPlayer, iVictim):
    pPlayer = gc.getPlayer(iPlayer)
    for iPlayer2 in range(gc.getMAX_PLAYERS()):
      pPlayer2 = gc.getPlayer(iPlayer2)
      iChance = -1
      if pPlayer2.isAlive():
        if (self.dogPileAllow(iPlayer, iPlayer2) and self.warScriptAllow(iPlayer2, iVictim)):
          iChance = pPlayer2.AI_getAttitude(iPlayer) * 5
          if iChance > 0:
            iChance = iChance - (pPlayer2.AI_getAttitude(iVictim) * 5) - 10
            if CyGame().isOption(gc.getInfoTypeForString('GAMEOPTION_AGGRESSIVE_AI')) == False:
              iChance = iChance - 10
            if iChance > 0:
              iChance = iChance + (CyGame().getGlobalCounter() / 3)
              if pPlayer2.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BALSERAPHS'):
                iChance = CyGame().getSorenRandNum(50, "Dogpile")
              if CyGame().getSorenRandNum(100, "Dogpile") < iChance:
                self.startWar(iPlayer2, iVictim, WarPlanTypes.WARPLAN_DOGPILE)

  def dogPileAllow(self, iPlayer, iPlayer2):
    pPlayer = gc.getPlayer(iPlayer)
    pPlayer2 = gc.getPlayer(iPlayer2)
    iTeam = gc.getPlayer(iPlayer).getTeam()
    iTeam2 = gc.getPlayer(iPlayer2).getTeam()
    if iPlayer == iPlayer2:
      return False
    if iTeam == iTeam2:
      return False
    if pPlayer2.isHuman():
      return False
    if pPlayer2.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ELOHIM'):
      return False
    if gc.getTeam(iTeam2).isAVassal():
      return False
    return True

  def warn(self, iPlayer, szText, pPlot):
    pPlayer = gc.getPlayer(iPlayer)
    for iPlayer2 in range(gc.getMAX_PLAYERS()):
      pPlayer2 = gc.getPlayer(iPlayer2)
      if (pPlayer2.isAlive() and iPlayer != iPlayer2):
        if pPlayer2.isHuman():
          popupInfo = CyPopupInfo()
          popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
          popupInfo.setText(szText)
          popupInfo.setOnClickedPythonCallback("selectWarn")
          popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_MAIN_MENU_OK",()), "")
          popupInfo.addPopup(iPlayer2)
        if pPlot != -1:
          CyInterface().addMessage(iPlayer2,True,25,CyTranslator().getText("TXT_KEY_MESSAGE_ALTAR_OF_THE_LUONNOTAR",()),'AS2D_DISCOVERBONUS',1,'Art/Interface/Buttons/Buildings/AltaroftheLuonnotar.dds',ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)

  def MarnokNameGenerator(self, unit):
    pPlayer = gc.getPlayer(unit.getOwner()) 
    pCiv = pPlayer.getCivilizationType() 
    pReligion = pPlayer.getStateReligion()
    pAlign = pPlayer.getAlignment() 

    lPre=["ta","go","da","bar","arc","ken","an","ad","mi","kon","kar","mar","wal","he", "ha", "re", "ar", "bal", "bel", "bo", "bri", "car","dag","dan","ma","ja","co","be","ga","qui","sa"]
    lMid=["ad","z","the","and","tha","ent","ion","tio","for","tis","oft","che","gan","an","en","wen","on","d","n","g","t","ow","dal"]
    lEnd=["ar","sta","na","is","el","es","ie","us","un","th", "er","on","an","re","in","ed","nd","at","en","le","man","ck","ton","nok","git","us","or","a","da","u","cha","ir"]
  
    lEpithet=["red","blue","black","grey","white","strong","brave","old","young","great","slayer","hunter","seeker"]
    lNoun=["spirit","soul","boon","born","staff","rod","shield","autumn","winter","spring","summer","wit","horn","tusk","glory","claw","tooth","head","heart", "blood","breath", "blade", "hand", "lover","bringer","maker","taker","river","stream","moon","star","face","foot","half","one","hundred","thousand"]
    lSchema=["CPME","CPMESCPME","CPESCPE","CPE","CPMME","CPMDCME","CPMAME","KCPMESCUM","CPMME[ the ]CX", "CPMESCXN", "CPMME[ of ]CPMME", "CNNSCXN"]

    if pAlign == gc.getInfoTypeForString('ALIGNMENT_EVIL'):
      lNoun = lNoun + ["fear","terror","reign","brood","snare","war","strife","pain","hate","evil","hell","misery","murder","anger","fury","rage","spawn","sly","blood","bone","scythe","slave","bound","ooze","scum"]
      lEpithet=["dark","black","white","cruel","foul"]    
  
    if pReligion == gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL'):
      lEpithet = lEpithet + ["fallen","diseased","infernal","profane","corrupt"]
      lSchema = lSchema + ["CPME[ the ]CX"]
    if pReligion == gc.getInfoTypeForString('RELIGION_OCTOPUS_OVERLORDS'):
      lPre = lPre + ["cth","cht","shu","az","ts","dag","hy","gla","gh","rh","x","ll"]   
      lMid = lMid + ["ul","tha","on","ug","st","oi"]  
      lEnd = lEnd + ["hu","on", "ha","ua","oa","uth","oth","ath","thua", "thoa","ur","ll","og","hua"]
      lEpithet = lEpithet + ["nameless","webbed","deep","watery"]
      lNoun = lNoun + ["tentacle","wind","wave","sea","ocean","dark","crab","abyss","island"]
      lSchema = lSchema + ["CPMME","CPDMME","CPAMAME","CPMAME","CPAMAMEDCPAMAE"]
    if pReligion == gc.getInfoTypeForString('RELIGION_THE_ORDER'):
      lPre = lPre + ["ph","v","j"]    
      lMid = lMid + ["an","al","un"]  
      lEnd = lEnd + ["uel","in","il"]
      lEpithet = lEpithet + ["confessor","crusader", "faithful","obedient","good"]
      lNoun = lNoun + ["order", "faith", "heaven","law"]
      lSchema = lSchema + ["CPESCPME","CPMESCPE","CPMESCPME", "CPESCPE"]
    if pReligion == gc.getInfoTypeForString('RELIGION_FELLOWSHIP_OF_LEAVES'):
      lPre = lPre + ["ki","ky","yv"]    
      lMid = lMid + ["th","ri"] 
      lEnd = lEnd + ["ra","el","ain"]
      lEpithet = lEpithet + ["green"]
      lNoun = lNoun + ["tree","bush","wood","berry","elm","willow","oak","leaf","flower","blossom"]
      lSchema = lSchema + ["CPESCN","CPMESCNN","CPMESCXN"]    
    if pReligion == gc.getInfoTypeForString('RELIGION_RUNES_OF_KILMORPH'):
      lPre = lPre + ["bam","ar","khel","ki"]    
      lMid = lMid + ["th","b","en"] 
      lEnd = lEnd + ["ur","dain","ain","don"]
      lEpithet = lEpithet + ["deep","guard","miner"]
      lNoun = lNoun + ["rune","flint","slate","stone","rock","iron","copper","mithril","thane","umber"]
      lSchema = lSchema + ["CPME","CPMME"]  
    if pReligion == gc.getInfoTypeForString('RELIGION_THE_EMPYREAN'):
      lEpithet = lEpithet + ["radiant","holy"]
      lNoun = lNoun + ["honor"]
    if pReligion == gc.getInfoTypeForString('RELIGION_COUNCIL_OF_ESUS'):
      lEpithet = lEpithet + ["hidden","dark"]
      lNoun = lNoun + ["cloak","shadow","mask"]
      lSchema = lSchema + ["CPME","CPMME"]  

    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ENRAGED')) == True:
      # I have left this as a copy of the Barbarian, see how it goes, this might do the trick. I plan to use it when there is a chance a unit will go Barbarian anyway.
      lPre = lPre + ["gru","bra","no","os","dir","ka","z"]
      lMid = lMid + ["g","ck","gg","sh","b","bh","aa"]
      lEnd = lEnd + ["al","e","ek","esh","ol","olg","alg"]
      lNoun = lNoun + ["death", "hate", "rage", "mad","insane","berserk"]   
      lEpithet = lEpithet + ["smasher", "breaker", "mangle","monger"]

    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CRAZED')) == True:
      # might want to tone this down, because I plan to use it as possession/driven to madness, less than madcap zaniness.
      lPre = lPre + ["mad","pim","zi","zo","fli","mum","dum","odd","slur"]
      lMid = lMid + ["bl","pl","gg","ug","bl","b","zz","abb","odd"]
      lEnd = lEnd + ["ad","ap","izzle","onk","ing","er","po","eep","oggle","y"] 
    
    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_VAMPIRE')) == True:
      lPre = lPre + ["dra","al","nos","vam","vla","tep","bat","bar","cor","lil","ray","zar","stra","le"]
      lMid = lMid + ["cul","u","car","fer","pir","or","na","ov","sta"]
      lEnd = lEnd + ["a","d","u","e","es","y","bas","vin","ith","ne","ak","ich","hd","t"] 

    if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON')) == True:
      lPre = lPre + ["aa","ab","adr","ah","al","de","ba","cro","da","be","eu","el","ha","ib","me","she","sth","z"]
      lMid = lMid + ["rax","lia","ri","al","as","b","bh","aa","al","ze","phi","sto","phe","cc","ee"]
      lEnd = lEnd + ["tor","tan","ept","lu","res","ah","mon","gon","bul","gul","lis","les","uz"]
      lSchema = ["CPMMME","CPMACME", "CPKMAUAPUE", "CPMMME[ the ]CNX"]        
    
    if unit.getUnitType() == gc.getInfoTypeForString('UNIT_HILL_GIANT'):
      lPre = lPre + ["gor","gra","gar","gi","gol"]
      lMid = lMid + ["gan","li","ri","go"]
      lEnd = lEnd + ["tus","tan","ath","tha"]
      lSchema = lSchema +["CXNSCNN","CPESCNE", "CPMME[ the ]CX"]    
      lEpithet = lEpithet + ["large","huge","collossal","brutal","basher","smasher","crasher","crusher"]    
      lNoun = lNoun + ["fist","tor","hill","brute","stomp"]

    if unit.getUnitType() == gc.getInfoTypeForString('UNIT_LIZARDMAN'):
      lPre = lPre + ["ss","s","th","sth","hss"]
      lEnd = lEnd + ["ess","iss","ath","tha"]
      lEpithet = lEpithet + ["cold"]      
      lNoun = lNoun + ["hiss","tongue","slither","scale","tail","ruin"]
      lSchema = lSchema + ["CPAECPAE","CPAKECPAU","CPAMMAE"]    
    if unit.getUnitType() == gc.getInfoTypeForString('UNIT_FIRE_ELEMENTAL') or unit.getUnitType() == gc.getInfoTypeForString('UNIT_AZER'):
      lPre = lPre + ["ss","cra","th","sth","hss","roa"]
      lMid = lMid + ["ss","ck","rr","oa","iss","tt"]    
      lEnd = lEnd + ["le","iss","st","r","er"]
      lNoun = lNoun + ["hot", "burn","scald","roast","flame","scorch","char","sear","singe","fire","spit"]      
      lSchema = ["CNN","CNX","CPME","CPME[ the ]CNX","CPMME","CNNSCPME"]
    if unit.getUnitType() == gc.getInfoTypeForString('UNIT_WATER_ELEMENTAL'):
      lPre = lPre + ["who","spl","dr","sl","spr","sw","b"]
      lMid = lMid + ["o","a","i","ub","ib"]   
      lEnd = lEnd + ["sh","p","ter","ble"]
      lNoun = lNoun + ["wave","lap","sea","lake","water","tide","surf","spray","wet","damp","soak","gurgle","bubble"]     
      lSchema = ["CNN","CNX","CPME","CPME[ the ]CNX","CPMME","CNNSCPME"]  
    if unit.getUnitType() == gc.getInfoTypeForString('UNIT_AIR_ELEMENTAL'):
      lPre = lPre + ["ff","ph","th","ff","ph","th"]
      lMid = lMid + ["oo","aa","ee","ah","oh"]    
      lEnd = lEnd + ["ff","ph","th","ff","ph","th"]
      lNoun = lNoun + ["wind","air","zephyr","breeze","gust","blast","blow"]      
      lSchema = ["CNN","CNX","CPME","CPME[ the ]CNX","CPMME","CNNSCPME"]  
    if unit.getUnitType() == gc.getInfoTypeForString('UNIT_EARTH_ELEMENTAL'):
      lPre = lPre + ["gra","gro","kro","ff","ph","th"]
      lMid = lMid + ["o","a","u"]   
      lEnd = lEnd + ["ck","g","k"]
      lNoun = lNoun + ["rock","stone","boulder","slate","granite","rumble","quake"]     
      lSchema = ["CNN","CNX","CPME","CPME[ the ]CNX","CPMME","CNNSCPME"]  
  
    # SEA BASED
    # Check for ships - special schemas
    if unit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_NAVAL'):
      lEnd = lEnd + ["ton","town","port"]
      lNoun = lNoun + ["lady","jolly","keel","bow","stern", "mast","sail","deck","hull","reef","wave"]
      lEpithet = lEpithet + ["sea", "red", "blue","grand","barnacle","gull"]
      lSchema = ["[The ]CNN", "[The ]CXN", "[The ]CNX","[The ]CNSCN", "[The ]CNSCX","CPME['s ]CN","[The ]CPME", "[The ]CNX","CNX","CN['s ]CN"]
  
    # # #
    # Pick a Schema
    sSchema = lSchema[CyGame().getSorenRandNum(len(lSchema), "Name Gen")-1]
    sFull = ""
    sKeep = ""
    iUpper = 0
    iKeep = 0
    iSkip = 0
  
    # Run through each character in schema to generate name
    for iCount in range (0,len(sSchema)):
      sAdd=""
      iDone = 0
      sAction = sSchema[iCount]
      if iSkip == 1:
        if sAction == "]":
          iSkip = 0
        else:
          sAdd = sAction
          iDone = 1   
      else:         # MAIN SECTION
        if sAction == "P":  # Pre   : beginnings of names
          sAdd = lPre[CyGame().getSorenRandNum(len(lPre), "Name Gen")-1]
          iDone = 1
        if sAction == "M":  # Mid   : middle syllables
          sAdd = lMid[CyGame().getSorenRandNum(len(lMid), "Name Gen")-1]  
          iDone = 1 
        if sAction == "E":  # End : end of names
          sAdd = lEnd[CyGame().getSorenRandNum(len(lEnd), "Name Gen")-1]
          iDone = 1
        if sAction == "X":  # Epithet : epithet word part
          #epithets ("e" was taken!)
          sAdd = lEpithet[CyGame().getSorenRandNum(len(lEpithet), "Name Gen")-1]
          iDone = 1
        if sAction == "N":  # Noun  : noun word part
          #noun
          sAdd = lNoun[CyGame().getSorenRandNum(len(lNoun), "Name Gen")-1]  
          iDone = 1
        if sAction == "S":  # Space : a space character. (Introduced before [ ] was possible )
          sAdd =  " "
          iDone = 1
        if sAction == "D":  # Dash  : a - character. Thought to be common and useful enough to warrant inclusion : Introduced before [-] was possible 
          sAdd =  "-"
          iDone = 1
        if sAction == "A":  # '   : a ' character - as for -, introduced early
          sAdd = "'" 
          iDone = 1
        if sAction == "C":  # Caps  : capitalizes first letter of next phrase generated. No effect on non-letters.
          iUpper = 1
        if sAction == "K":  # Keep  : stores the next phrase generated for re-use with U
          iKeep = 1
        if sAction == "U":  # Use : re-uses a stored phrase.
          sAdd = sKeep
          iDone = 1
        if sAction == "[":  # Print : anything between [] is added to the final phrase "as is". Useful for [ the ] and [ of ] among others.
          iSkip = 1
      # capitalizes phrase once.  
      if iUpper == 1 and iDone == 1:
        sAdd = sAdd.capitalize()
        iUpper = 0
      # stores the next phrase generated. 
      if iKeep == 1 and iDone == 1:
        sKeep = sAdd
        iKeep = 0
      # only adds the phrase if a new bit was actally created.
      if iDone == 1:
        sFull = sFull + sAdd

    # trim name length      
    if len(sFull) > 25:
      sFull = sFull[:25]    
    #CyInterface().addMessage(caster.getOwner(),True,25,"NAME : "+sFull,'AS2D_POSITIVE_DINK',1,'Art/Interface/Buttons/Spells/Rob Grave.dds',ColorTypes(8),pPlot.getX(),pPlot.getY(),True,True)

    return sFull

  def BarbCityProduction(self, pCity):

    ePlayer = pCity.getOwner()
    pPlayer = gc.getPlayer(ePlayer)
    player = PyPlayer(ePlayer)
    civtype = pPlayer.getCivilizationType()
    infoCiv = gc.getCivilizationInfo(civtype)
    eTeam = gc.getTeam(pPlayer.getTeam())
    pPlot = pCity.plot()
    
    if pPlayer.isHuman():
      return False
          
    sProd = ['UNITCLASS_WARRIOR']
    sProd = sProd + ['UNITCLASS_ADEPT','UNITCLASS_AXEMAN','UNITCLASS_HUNTER','UNITCLASS_ARCHER','UNITCLASS_HORSEMAN']
    sProd = sProd + ['UNITCLASS_CHAMPION','UNITCLASS_CHARIOT','UNITCLASS_RANGER','UNITCLASS_LONGBOWMAN','UNITCLASS_ASSASSIN']
    sProd = sProd + ['UNITCLASS_ACHERON','UNITCLASS_TUMTUM']

    iValue=[0]
    for i in range (len(sProd)):
      iValue+=[0]
            
    iValue[sProd.index('UNITCLASS_AXEMAN')]=19500
    iValue[sProd.index('UNITCLASS_ARCHER')]=19000+CyGame().getSorenRandNum(650, "Archer Scores")
    iValue[sProd.index('UNITCLASS_HUNTER')]=19400+CyGame().getSorenRandNum(200, "Lizard Scores")
    iValue[sProd.index('UNITCLASS_HORSEMAN')]=19400+CyGame().getSorenRandNum(200, "Horseman Scores")
    iValue[sProd.index('UNITCLASS_WARRIOR')]=19002
      
    if pPlayer.getUnitClassCountPlusMaking(gc.getInfoTypeForString('UNITCLASS_TUMTUM'))==0:     
      if gc.getGame().getUnitClassCreatedCount(gc.getInfoTypeForString('UNITCLASS_TUMTUM'))==0:       
        iValue[sProd.index('UNITCLASS_TUMTUM')]=100000  

    if not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_ACHERON) and CyGame().getGameTurn() > 100:   
      if gc.getGame().getUnitClassCreatedCount(gc.getInfoTypeForString('UNITCLASS_ACHERON'))==0:    
        if pPlayer.getUnitClassCountPlusMaking(gc.getInfoTypeForString('UNITCLASS_ACHERON'))==0:          
          iValue[sProd.index('UNITCLASS_ACHERON')]=150000     
#Value higher Tier units more

    if (iValue[sProd.index('UNITCLASS_WARRIOR')]>iValue[sProd.index('UNITCLASS_AXEMAN')]):
      iValue[sProd.index('UNITCLASS_AXEMAN')]=iValue[sProd.index('UNITCLASS_WARRIOR')]+1000   
    if (iValue[sProd.index('UNITCLASS_WARRIOR')]>iValue[sProd.index('UNITCLASS_ARCHER')]):
      iValue[sProd.index('UNITCLASS_ARCHER')]=iValue[sProd.index('UNITCLASS_WARRIOR')]+1000   
    if (iValue[sProd.index('UNITCLASS_WARRIOR')]>iValue[sProd.index('UNITCLASS_HUNTER')]):
      iValue[sProd.index('UNITCLASS_HUNTER')]=iValue[sProd.index('UNITCLASS_WARRIOR')]+1000   

    if (iValue[sProd.index('UNITCLASS_AXEMAN')]>0):             
      iValue[sProd.index('UNITCLASS_CHAMPION')]+=iValue[sProd.index('UNITCLASS_AXEMAN')]+1000

    if iValue[sProd.index('UNITCLASS_ARCHER')]>0:             
      iValue[sProd.index('UNITCLASS_LONGBOWMAN')]+=iValue[sProd.index('UNITCLASS_ARCHER')]+1000

    if iValue[sProd.index('UNITCLASS_HUNTER')]>0:             
      iValue[sProd.index('UNITCLASS_RANGER')]+=iValue[sProd.index('UNITCLASS_HUNTER')]+1000
      iValue[sProd.index('UNITCLASS_ASSASSIN')]+=iValue[sProd.index('UNITCLASS_HUNTER')]+1000

    if iValue[sProd.index('UNITCLASS_HORSEMAN')]>0:             
      iValue[sProd.index('UNITCLASS_CHARIOT')]+=iValue[sProd.index('UNITCLASS_HORSEMAN')]+1000
      
      
    infoCiv = gc.getCivilizationInfo(civtype)   
    iBestBuilding=-1
    iBestBuildingValue=0
    for i in range(len(sProd)):
      if iValue[i]>iBestBuildingValue:
        iUnit = infoCiv.getCivilizationUnits(gc.getInfoTypeForString(sProd[i]))
        if iUnit != -1:
          if pCity.canTrain(iUnit,True,False):
            iBestBuildingValue=iValue[i]
            iBestBuilding=i

    if iUnit==gc.getInfoTypeForString('UNIT_ACHERON'):          
##--------  BUGFfH: Modified by Denev 2009/10/12
#     CyInterface().addMessage(0,true,25,"Travellers from far away speak of a mighty Dragon, who wants to make %s his lair." %(pCity.getName()),'',0,'',ColorTypes(11), pPlot.getX(), pPlot.getY(), True,True)
      CyInterface().addMessage(0, true, 25, CyTranslator().getText("TXT_KEY_MESSAGE_START_PRODUCTION_ACHERON", (pCity.getName(), )), '', 0, '', ColorTypes(11), pPlot.getX(), pPlot.getY(), True, True)
##--------  BUGFfH: End Modify

    if iBestBuilding!=-1:
      iUnit = infoCiv.getCivilizationUnits(gc.getInfoTypeForString(sProd[iBestBuilding]))
      if (gc.getUnitInfo(iUnit).getUnitCombatType()==gc.getInfoTypeForString('UNITCOMBAT_ARCHER')):
        pCity.pushOrder(OrderTypes.ORDER_TRAIN,iUnit,gc.getInfoTypeForString('UNITAI_CITY_DEFENSE'), False, False, False, False)
      else:
        pCity.pushOrder(OrderTypes.ORDER_TRAIN,iUnit,gc.getInfoTypeForString('UNITAI_ATTACK_CITY'), False, False, False, False)     
      return 1      
  
    return False