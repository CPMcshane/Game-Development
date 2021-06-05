from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

class MyApp(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)
        
        # Load the environment model
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8,42,0)
        
        # Add a spin camera task procedure to the task manager
        # self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        
        # Load and transform the panda actor
        self.pandaActor1 = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor1.setScale(0.005, 0.005, 0.005)
        self.pandaActor1.reparentTo(self.render)
        self.pandaActor1.loop("walk")
        
        # walk back and forth.
        posInterval1 = self.pandaActor1.posInterval(13,
                                                   Point3(0, -10, 0),
                                                   startPos=Point3(0, 10, 0))
        posInterval2 = self.pandaActor1.posInterval(13,
                                                   Point3(0, 10, 0),
                                                   startPos=Point3(0, -10, 0))
        hprInterval1 = self.pandaActor1.hprInterval(3,
                                                   Point3(180, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor1.hprInterval(3,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(180, 0, 0))
        
        # Create and play the sequence that coordinates the intervals.
        self.pandaPace1 = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace1")
        self.pandaPace1.loop()
        
        
        # Load and transform the panda actor
        self.pandaActor2 = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor2.setScale(0.005, 0.005, 0.005)
        self.pandaActor2.reparentTo(self.render)
        self.pandaActor2.loop("walk")
        
        # walk back and forth.
        posInterval1 = self.pandaActor2.posInterval(5,
                                                   Point3(-20, -70, 0),
                                                   startPos=Point3(20, 70, 0))
        posInterval2 = self.pandaActor2.posInterval(5,
                                                   Point3(-20, 70, 0),
                                                   startPos=Point3(0, -70, 0))
        hprInterval1 = self.pandaActor2.hprInterval(8,
                                                   Point3(180, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor2.hprInterval(8,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(180, 0, 0))
        
        # Create and play the sequence that coordinates the intervals.
        self.pandaPace2 = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace2")
        self.pandaPace2.loop()
        
        
        # Load and transform the panda actor
        self.pandaActor3 = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor3.setScale(0.015, 0.015, 0.015)
        self.pandaActor3.reparentTo(self.render)
        self.pandaActor3.loop("walk")
        
        # walk back and forth.
        posInterval1 = self.pandaActor3.posInterval(10,
                                                   Point3(30, -50, 0),
                                                   startPos=Point3(30, 50, 0))
        posInterval2 = self.pandaActor3.posInterval(10,
                                                   Point3(30, 50, 0),
                                                   startPos=Point3(30, -50, 0))
        hprInterval1 = self.pandaActor3.hprInterval(1,
                                                   Point3(180, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor3.hprInterval(1,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(180, 0, 0))
        
        # Create and play the sequence that coordinates the intervals.
        self.pandaPace3 = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace3")
        self.pandaPace3.loop()
        
        
    """    
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi/180)
        self.camera.setPos(40* sin(angleRadians), -40 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, -20, 30)
        return Task.cont
    """
app = MyApp()
app.run()
