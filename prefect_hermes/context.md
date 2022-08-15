## What is General Availability (GA)?

General Availability is when a stable release of a product is made available to the general public. Upon the GA release:

- Prefect 2.0.0 will become the default version of the the open source framework provided [upon installation](https://orion-docs.prefect.io/getting-started/installation/)
- The [Prefect Cloud 2.0 platform](https://www.prefect.io/cloud/v2/) will no longer have a “beta” label and the Starter tier will be available for purchase to the general public

## Will Prefect Cloud 2.0 be ready for Enterprise customers upon the GA release?

No, the GA release is for the Free/Starter tier of the [Cloud 2.0 Tiers: Pricing / Features](https://www.notion.so/Cloud-2-0-Tiers-Pricing-Features-2ee95ddb890f406294b8c71dc99597e1). Release dates for the features associated with the Growth and Enterprise tiers are TBD, but will most likely be delivered by October 2022.

<aside>
💡 Messaging for Enterprise customers below who we won’t be ready to migrate

</aside>

> Thank you for being a valued partner of Prefect! We recently brought Prefect 2 and Prefect Cloud 2 out of beta, and announced Generally Availability (GA). Right now this covers our Starter tier, and we’ll be making our Enterprise tier features available over the next few months. These include SSO, custom roles, audit trail and more.

We are committed to helping you upgrade to Prefect Cloud 2 as soon as it is possible, and we will reach out proactively when the features that support your enterprise use cases are available.
> 

## Will there be changes to our public websites, if so when?

Yes there will be changes. They will go live on the day of the release, 7/27.

On the [Prefect.io](http://Prefect.io) home page:

- The “Get Started” button will direct to Prefect Cloud 2.0 registration instead of Prefect Cloud 1.0 registration
- The “Log In” button will direct to a landing page in which the user selects either Prefect Cloud 1.0 or Prefect Cloud 2.0
- Pricing page will have a new design and copy to reflect 2.0 pricing

On the docs sites:

- The content at [docs.prefect.io](https://docs.prefect.io/) will be accessible at to [docs.prefect.io](https://docs.prefect.io/)/v1/
- The content at [orion-docs.prefect.io](https://orion-docs.prefect.io/) will be accessible at [docs.prefect.io](https://docs.prefect.io/)/v2/
    - [docs.prefect.io](https://docs.prefect.io/) will redirect there
    - [orion-docs.prefect.io](https://orion-docs.prefect.io/) will redirect there

For the applications:

- Prefect Cloud 1.0 will remain at [cloud.prefect.io](https://cloud.prefect.io/prefect)
- Prefect Cloud 2.0 will be available at [app.prefect.cloud](https://prefect.cloud/). The current URL, [beta.prefect.io](https://beta.prefect.io/dashboard), will redirect there

Read more about it in [2.0 GA URL Changes](https://www.notion.so/2-0-GA-URL-Changes-8202023a2686433bad6b6ad6888f1de6).

## Can a flow written with Prefect 1.0 be orchestrated with Prefect 2.0 and vice versa?

No. Flows written with the Prefect 1.0 client must be rewritten with the Prefect 2.0 client. For most flows, this should take just a few minutes. 

## What are the differences between orchestrating a flow with Prefect 1.0 & Prefect 2.0?

Flows written with Prefect 2.0 are more dynamic, do not require registration, and are asynchronous by default. There are several simple but important syntax changes. 

## Does Prefect Cloud 2.0 adhere to the [hybrid model](https://www.prefect.io/why-prefect/hybrid-model/), and generally, does Prefect Cloud 2.0 make the same set of guarantees as Prefect Cloud 1.0 regarding data sharing and security?

Yes, Prefect Cloud 2.0 adhere’s to the hybrid model. However, the hybrid model is not a specific, immutable set of guarantees, but rather an *architecture* that enables the user to choose how much and what kind of information to send to Prefect Cloud.

Prefect’s hybrid model begins with one foundational principle: *from the perspective of a customer network, API traffic is always outgoing, never incoming.* This means that Prefect will never send information of any kind to the customer’s network without first being explicitly requested to do so. Users can use Prefect without providing Prefect first-class access to either workflow defining code or data exchanged between tasks. Note that configuration, secrets, and other sensitive information may still be stored in Prefect Cloud 2.0.

## What will the version of the open source prefect library be when Prefect enters GA?

The version will be 2.0.0. The “b” preceding the final number will be removed from all future versions.

## How long will Prefect Cloud 1.0 be supported after the 2.0 GA release?

At least one full year. Currently, the GTM team tells customers we will support Prefect Cloud 1.0 “for as long as needed, but we will be proactive in supporting your migration effort.” in order to ensure we don’t create undue anxiety in our existing users. There is no need to give customers greater precision than this at this time.

## What are the differences between Prefect Cloud 1.0 & Prefect Cloud 2.0?

Cloud 2.0 is simpler and faster, but less feature rich (for now). See the following resources for more information:

- @George Coyne’s [Upgrade to Prefect 2](https://www.prefect.io/guide/blog/upgrade-to-prefect-2/) post
- [Differences between Cloud 1.0 and Cloud 2.0](https://www.notion.so/Differences-between-Cloud-1-0-and-Cloud-2-0-9152ce7733ac4a7395d199dfd69440e4)
- @Anna Geller’s [Migration Guide](https://orion-docs.prefect.io/migration_guide/)

## What is “Orion”?

Orion is a branded, open source orchestration engine that powers both Prefect 2.0 and Prefect Cloud 2.0. Read more about it in [Prefect Orion: Our Second-Generation Workflow Engine](https://www.prefect.io/guide/blog/announcing-prefect-orion/).

![Screen Shot 2022-06-24 at 1.57.27 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/048986f6-57f0-473e-b6c3-7371f965b34f/Screen_Shot_2022-06-24_at_1.57.27_PM.png)

## If I’m using Prefect Cloud 2.0, do I still need to run Orion locally?

No, Prefect Cloud 2.0 hosts an instance of Orion for you. In fact, each workspace in Prefect Could 2.0 corresponds directly to a single instance of Orion.

## What is a “Block”?

Blocks provide shared, secure configuration and functionality for common connections. They give you a straightforward way to access and use external systems like S3 buckets, dbt DAGs, GitHub repos, Slack channels, Postgres tables, and more. A block loaded to an Orion Server (or Prefect Cloud Workspace) can be use in any flows run with that Server. 

Blocks replace both Secrets and the Key Value store in Prefect Cloud 1. Instead of generic, independent key-values, blocks offer schema validation with strong typing, such that related configuration values can be stored and used together.

Blocks are modular. Each block has “capabilities” - standardized methods such as read, write, and store. Blocks with the same capabilities can be used interchangeably.

## What is a “Workspace”?

A workspace is an isolated environment within Prefect Cloud 2.0 for collections of people, blocks, flows, and their related concepts like deployments and flow runs. Workspaces could be used in any way you like to organize or compartmentalize your workflows. For example, you could use separate workspaces to isolate dev, staging, and prod environments, or to provide separation between different teams. Access is controlled at the workspace level - users and service accounts have access to everything or nothing in a workspace - though the permissions associated with that access can be controlled via RBAC (See “What is RBAC?” for more information.)

Technically, each workspace corresponds to a single Orion instance.

For a comparison to tenants and projects, see [Differences between Cloud 1.0 and Cloud 2.0](https://www.notion.so/Differences-between-Cloud-1-0-and-Cloud-2-0-9152ce7733ac4a7395d199dfd69440e4).

## What is an “Organization”?

An Organization is the highest-level grouping of workspaces and users in Prefect Cloud 2.0. Often representing a company, organizations come with an allotment of members and workspaces according to their account’s annual plan. Organizations enable new features, including Service Accounts and Workspace Access Roles, and will be the natural home of several other features planned for the growth tier and above. 

## What is a “Team”?

A team is a group of users. Users in a group must be members of the same organization. Users can belong to more that one team. Teams are usually a subset of the complete set of organization members. Teams can be assigned Workspace Access Roles. All of the members of that team inherit the Roles assigned to that team.

## What happens to existing customer contracts upon the GA release?

Customers that have signed contracts with Prefect in the past few months are usually part of Prefect’s [Lighthouse program](https://www.notion.so/2022-Q2-Product-Offerings-47d72047f80047fb82944e4c6373cb8a), so their contracts will not need to be changed for them to transition to Prefect Cloud 2.0. Exceptions are handled on a case by case basis with approval from sales leadership as appropriate.

## What is the pricing model for Prefect Cloud 2.0?

At the lower tiers, the pricing model is driven by users and workspaces. At higher tiers, pricing will be driven by security and performance. See[Cloud 2.0 Tiers: Pricing / Features](https://www.notion.so/Cloud-2-0-Tiers-Pricing-Features-2ee95ddb890f406294b8c71dc99597e1) for more information.

## What are the “Performance Capabilities” referenced in the tiers/pricing table and how do they relate to a rate limit?

<aside>
🔒 This answer for internal purposes only

</aside>

In Prefect Cloud 1.0, all code needed to be included in a task to be orchestrated. This made task runs a very good proxy for how much usage each account made of Prefect, so we priced on task runs.

Given our plans for Prefect Cloud 2.0, we know that task runs alone will not be a good proxy for usage. We know that we’ll need a different metric that is a good proxy for usage, but we don’t know what it is yet.

Upon GA Prefect Cloud 2.0 will have a single, standard, per account rate limit for all REST API requests, like most web services. This rate limit will not impact performance for most use cases, so it will not be a focus of our pricing model.

## What is RBAC and how will permission controls differ between the tiers of Prefect Cloud 2.0?

[Role Based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) is a way of restricting the access of certain users to a system through roles, which are groups of access permissions that can be assigned to users. *All* of Prefect Cloud 2.0’s tiers leverage RBAC, but higher tiers give users more control over roles and their assignment to users. On all tiers, access is controlled on a *per workspace* basis.

On the starter tier, roles are not exposed to users at all. All workspaces that belong to starter accounts must extend Administrator permissions to any user that has access.

On the Growth tier, there are three, and only three, workspace roles:

- Administrator (all permissions)
- Collaborator (just read and write permissions), and
- Read-Only Collaborator (just read permissions)

On the Enterprise tier, in addition to these roles, users can create custom roles that are composed of any set of permissions.

Plans for permission management are subject to change upon release.

## I found a bug or have an idea to improve Prefect Cloud 2.0 - how can I let the right person know?

<aside>
🔒 This answer for internal purposes only

</aside>

Please share or pass along feedback about Prefect 2.0 and Cloud 2.0 just as you always can. See [Sharing Feedback](https://www.notion.so/Sharing-Feedback-55d4b58a34b646609a65aed75a04f343) for more information.

## Is there a public roadmap for Prefect & Prefect Cloud beyond the GA release?

<aside>
🔒 This answer for internal purposes only

</aside>

No, see the [Roadmap & Backlog](https://www.notion.so/Roadmap-Backlog-ac24bb8b364f46c5be4bb3adc873161a) page for more information.

## How will the repositories for our open source product be organized upon the GA release?

The `orion` branch of the `prefect` repository will become the `main` branch. The default branch will change from `master` to the new `main` brach. Development will transition from the internal `orion` repository to the new, public `main` branch of the `prefect` repo.

## I heard that Prefect 2.0 will return results instead of states - why change?

When we first designed Prefect 2, we designed for common use cases with Prefect 1. In particular, we valued the ability to seamlessly transition between local execution and execution with distributed compute frameworks, like [Dask](https://www.dask.org/). As Prefect 2 usage has grown, we've observed a pattern among first time users of Prefect 2 that were not previously users of Prefect 1 - they were often surprised that their tasks returned futures and [states](https://orion-docs.prefect.io/concepts/states/), Prefect objects, rather than [results](https://orion-docs.prefect.io/concepts/tasks/#using-results-from-tasks), the data that the Python functions were handling. Additionally, these users were often unfamiliar with the concurrent execution concepts like [futures](https://docs.python.org/3/library/asyncio-future.html). This led to unfamiliar, potentially intimidating errors in some cases.

States are a very important part of Prefect. They are integral to how we [define orchestration](https://www.moderndatastack.xyz/category/workflow-orchestration). Seamlessly supporting concurrent execution is similarly important. Some users, however, may not need either of these things. Consistent with our principle of *incremental adoption*, we only want to require users to learn something new when they need that knowledge to solve the problem at hand.

**Tasks now return results and run sequentially by default.** This means that users can truly take most native Python scripts, add the relevant `@flow` and `@task` decorators, and start running that script as a flow, benefitting from the observability and resilience that Prefect provides, without learning about states or concurrency until they need to.

States remain an import concept in dictating and understanding the behavior of flows. Users will still be able to access and use them. Similarly, users will be able to run their flows concurrently with modifications.

## Prefect 2.0 broke my flows! What do I do?

With the release of Prefect 2.0 on July 27th, the latest version that is used by pip and docker will now point to the latest Prefect 2.0 release.

Pip errors: To fix this, please specify the correct version in your pip install command: pip install prefect==1.2.4

Docker errors: To fix this, please specify the correct version through an image tag: prefecthq/prefect:1.2.4-python3.9

## Who is Marvin?

Marvin has many forms. Our favorite, although probably not his, is as a blue rubber duck. That is how he is depicted as Prefect's beloved mascot.