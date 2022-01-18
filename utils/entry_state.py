class EntryStates():
    '''
        state_gold: [normal - user can insert text into entry
                    disabled - user can't insert text into entry]
        state_diamond: [normal - user can insert text into entry
                       disabled - user can't insert text into entry]
        background: [disable entry background image]
    '''
    def __init__(self, state_gold: str, state_diamond: str, background: str):
        self.state_gold = state_gold
        self.state_diamond = state_diamond
        self.background = background

    def state(self, obj):
        # state normal for both condition (gold and diamond)
        obj.entry0.config(state= "normal", disabledbackground=self.background)
        obj.entry1.config(state= "normal", disabledbackground=self.background)
        obj.entry2.config(state= "normal", disabledbackground=self.background)
        obj.entry3.config(state= "normal", disabledbackground=self.background)
        obj.entry4.config(state= "normal", disabledbackground=self.background)
        obj.entry5.config(state= "normal", disabledbackground=self.background)
        obj.entry6.config(state= "normal", disabledbackground=self.background)
        obj.entry7.config(state= "normal", disabledbackground=self.background)
        obj.entry8.config(state= "normal", disabledbackground=self.background)
        obj.entry9.config(state= "normal", disabledbackground=self.background)
        obj.entry10.config(state= self.state_gold, disabledbackground=self.background)

        # state as per card condition (gold and diamond)
        # have to pass "normal" or "disabled"
        obj.entry11.config(state= self.state_gold, disabledbackground=self.background)
        obj.entry12.config(state= self.state_gold, disabledbackground=self.background)
        obj.entry13.config(state= self.state_gold, disabledbackground=self.background)
        obj.entry14.config(state= self.state_diamond, disabledbackground=self.background)
        obj.entry15.config(state= self.state_diamond, disabledbackground=self.background)
        obj.entry16.config(state= self.state_diamond, disabledbackground=self.background)
        obj.entry17.config(state= self.state_diamond, disabledbackground=self.background)