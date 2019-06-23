Step Functions
===
![step_functions_how_it_works](./images/step_functions_how_it_works.png)
- is a web service that provides **serverless orchestration** for modern applications. It enables you to coordinate the components of distributed applications and microservices using visual workflows.
- Concepts
    - Step Functions is based on the concepts of **tasks** and **state machines**
        - A task performs work by using an activity or an AWS Lambda function, or by passing parameters to the API actions of other services.
        - A finite state machine can express an algorithm as a number of states, their relationships, and their input and output.
    - You define state machines using the **JSON-based Amazon States Languages**
    - A state is referred to by its *name*, which can be any string, but which must be unique within the scope of the entire state machine. An instance of a state exists until the end of its execution.
        - There are 6 types of states
            - Task state
            - Choice state
            - Fail or Succeed state
            - Pass state
            - Wait state
            - Parallel state
        - Common features between states
            - Each state must have a _Type_ field indicating what type of state it is.
            - Each state can have an optional _Comment_ field to hold a human-readable comment about, or description of, the state.
            - Each state (except a Succeed or Fail state) requires a _Next_ field or, alternatively, can become a terminal state by specifying an __End__ field
    - __Activities__ enables you to place a task in your state machine where the work is performed by an __activity worker__ that can be hosted on Amazon EC2, ECS, or mobile devices.

## Features
- Using Step Functions, you define your **workflow as state machine**, which transform complex code into easy to understand statements and diagrams.
- Step Functions provides ready-made steps for your workflow called __states__ taht implement basic service primitives for you, which means you can remove that logic from your application. States are able to:
    - pass data to other states and microservices,
    - handle expcetions,
    - add timeouts,
    - make decisions,
    - execute multiple paths in parallel,
    - and more
- Using Steps Functions __service tasks__, you can configure your Step Functions workflow to call other AWS services.
- can coordinate any application that can make an __HTTPS__ connection, regardless of where it is hosted - Amazon EC2 instances, mobile devices, or on-premises servers.
- coordinates your existing Lambda functions and microservices, and lets you modify them into new compositions. The tasks in your workflow can run anywhere, including on instances, containers, functions, and mobile devices.
- keeps the logic of your application strictly separated from the implementation of your application. You can add, move, swap, and reorder steps without having to make changes to your business logic.
- maintains the state of your application during execution, including tracking what step of execution it is in, and storing data that is moving between the steps of your workflow. You won't have to manage state yourself with data stores or by building complex state management into all of your tasks.
- automatically handles errors and exceptions with __built-in try/catch and retry__, whether the task takes seconds or months to complete. You can automatically retry failed or timed out tasks, respond differently to different types of errors, and recover gracefully by falling back to designated cleanup and recovery code.
- has __built-in fault tolerance and maintains service capacity across multiple AZ in each region__, ensuring high availablity for both the service itself and for the application workflow it operates.
-  __automcatically scales__ the operations and underlying compute to run the steps of your application for you in response to changing workloads.
- has a 99.9% SLA.
※ What is SLA : a commitment between a service provider and a client. Particular aspects of the service - quality, availability, responsibilities - are agreed between the service provider and the service user.

## How Step Functions Work
![step_funcitons](./images/step_funcitons.png)
- Orchestration centrally manages a workflow by breaking it into multiple steps, adding flow logic, and tracking the inputs and outputs between the steps.
- As your applications execute, Step Functions maintains application state, tacking exactly which workflow step your application is in, and stores an event log of data that is passed between application components. __That means that if network fail or compoenens hang, your application can pick up right where it left off__.