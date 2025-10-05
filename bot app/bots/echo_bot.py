# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount


class EchoBot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    async def on_message_activity(self, turn_context: TurnContext):
        incoming = (turn_context.activity.text or "").strip()

        # Handle empty / malformed input
        if not incoming:
            await turn_context.send_activity("I didn’t get any text. Type 'help' to see options.")
            return

        # Handle a 'help' command
        if incoming.lower() == "help":
            help_text = (
                "I can:\n"
                "- Reverse your text.\n"
                "- Show this help message if you type 'help'."
            )
            await turn_context.send_activity(help_text)
            return

        # Default: reverse the input text
        reversed_text = incoming[::-1]
        await turn_context.send_activity(MessageFactory.text(reversed_text))
