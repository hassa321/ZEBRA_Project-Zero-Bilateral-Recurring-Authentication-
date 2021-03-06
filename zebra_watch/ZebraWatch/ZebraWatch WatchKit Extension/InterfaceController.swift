//
//  InterfaceController.swift
//  ZebraWatch WatchKit Extension
//
//  Created by Vladyslava Diachenko on 2020-02-01.
//  Copyright © 2020 Vladyslava Diachenko. All rights reserved.
//

import WatchKit
import Foundation
import CoreMotion
import os.log

extension Date {
    var millisecondsSince1970:Int64 {
        return Int64((self.timeIntervalSince1970 * 1000.0).rounded())
    }
}

class InterfaceController: WKInterfaceController {
    
   struct WatchData: Codable {
        var Ax: Double
        var Ay: Double
        var Az: Double
        var TimeStamp: Int64
    
    }
   
    
    @IBOutlet weak var accelerationLbl: WKInterfaceLabel!
    
    @IBOutlet weak var gyroscopeLbl: WKInterfaceLabel!
    
    var accelerationString = "Not Active"
    var gyroscopeString = "Not Active"
    
    var accelerationStr = ""
    var gyroscopeStr = ""
    
    var activityStr = ""
    

    
    
    let motionManager = CMMotionManager()
    let sampleInterval = 1.0 / 50 //replace for 50 later
    let queue = OperationQueue()
    let queueact = OperationQueue()
    
    
    var motionActivityManager = CMMotionActivityManager()
    
    /*
    func startActUpdates() {
        if CMMotionActivityManager.isActivityAvailable() {
            motionActivityManager.startActivityUpdates(to: queue, withHandler: {
                activityData
                in
                if activityData!.walking == true {
                    self.activityStr = "Walking"
                } else if activityData!.running == true {
                    self.activityStr = "Running"
                } else if activityData!.automotive == true {
                    self.activityStr = "Automotive"
                } else if activityData!.stationary == true {
                     self.activityStr = "Stationary"
                }
                //print("\n\n\nActivity Data: ", activityData!)
            })
        }
    }
    
*/
    
    func updateLabels() {
        accelerationLbl.setText(accelerationString)
        gyroscopeLbl.setText(gyroscopeString)
    }
    
    func startUpdates() {

           if !motionManager.isDeviceMotionAvailable {
               print("Device Motion is not available.")
               //return
           }
           
           os_log("Start Updates");

           motionManager.deviceMotionUpdateInterval = sampleInterval
           motionManager.startDeviceMotionUpdates(to: queue) { (deviceMotion: CMDeviceMotion?, error: Error?) in
               if error != nil {
                   print("Encountered error: \(error!)")
               }

               if deviceMotion != nil {
                   self.processDeviceMotion(deviceMotion!)
                   self.accelerationString = "Collecting data"
                   self.gyroscopeString = "Collecting data"
               }
           }
        
       }

       func stopUpdates() {
           if motionManager.isDeviceMotionAvailable {
               motionManager.stopDeviceMotionUpdates()
               accelerationString = "Not Active"
               gyroscopeString = "Not Active"
           }
       }
    
    func processDeviceMotion(_ deviceMotion: CMDeviceMotion) {
         /*
         accelerationStr = String(format: "X: %.1f Y: %.1f Z: %.1f" ,
                             deviceMotion.userAcceleration.x,
                             deviceMotion.userAcceleration.y,
                             deviceMotion.userAcceleration.z)
          gyroscopeStr = String(format: "X: %.1f Y: %.1f Z: %.1f" ,
                                deviceMotion.rotationRate.x,
                                deviceMotion.rotationRate.y,
                                deviceMotion.rotationRate.z)
         
          */
            let timestamp = Date().millisecondsSince1970
            
           //PLEASE WORK I NEED A BREAK
            
            //let json = ["user":"admin"]
        
            let newTodoItem = WatchData(Ax: deviceMotion.userAcceleration.x, Ay: deviceMotion.userAcceleration.y, Az: deviceMotion.userAcceleration.z, TimeStamp: timestamp)
            
            var request = URLRequest(url: URL(string: "http://dev3.horizon.tom.srl/watch")!)
            request.setValue("application/json", forHTTPHeaderField: "Content-Type")

            request.httpMethod = "POST"
    
            let jsonData = try? JSONEncoder().encode(newTodoItem)
            
            request.httpBody = jsonData
            
            // Perform HTTP Request
            let task = URLSession.shared.dataTask(with: request) { (data, response, error) in
                    
                    // Check for Error
                    if let error = error {
                        print("Error took place \(error)")
                        return
                    }
             
                    // Convert HTTP Response Data to a String
                    if let data = data, let dataString = String(data: data, encoding: .utf8) {
                        print("Response data string:\n \(dataString)")
                    }
            }
            task.resume()
            
            
                 os_log("Motion: %@, %@, %@, %@",
                 String(timestamp),
                 String(deviceMotion.userAcceleration.x),
                 String(deviceMotion.userAcceleration.y),
                 String(deviceMotion.userAcceleration.z))
         
        
          updateLabels();
        
      }


    
    
    func postData() {
      //
    }
    
    override func willActivate() {
        // This method is called when watch view controller is about to be visible to user
        super.willActivate()
        startUpdates()
        //startActUpdates()
        postData()
    }
    
    override func didDeactivate() {
        // This method is called when watch view controller is no longer visible
        super.didDeactivate()
    }

}
