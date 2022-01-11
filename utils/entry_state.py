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
        obj.entry_product_img.config(state= "normal", disabledbackground=self.background)
        obj.entry_qr_img.config(state= "normal", disabledbackground=self.background)
        obj.entry_jewellery_name.config(state= "normal", disabledbackground=self.background)
        obj.entry_adress.config(state= "normal", disabledbackground=self.background)
        obj.entry_customer_name.config(state= "normal", disabledbackground=self.background)
        obj.entry_date.config(state= "normal", disabledbackground=self.background)
        obj.entry_product_name.config(state= "normal", disabledbackground=self.background)
        obj.entry_product_weight.config(state= "normal", disabledbackground=self.background)
        obj.entry_product_karate.config(state= "normal", disabledbackground=self.background)
        obj.entry_gold_value.config(state= self.state_gold, disabledbackground=self.background)

        # state as per card condition (gold and diamond)
        # have to pass "normal" or "disabled"
        obj.entry_silver_value.config(state= self.state_gold, disabledbackground=self.background)
        obj.entry_coper_value.config(state= self.state_gold, disabledbackground=self.background)
        obj.entry_other_value.config(state= self.state_gold, disabledbackground=self.background)
        obj.entry_color.config(state= self.state_diamond, disabledbackground=self.background)
        obj.entry_clarity.config(state= self.state_diamond, disabledbackground=self.background)
        obj.entry_cut.config(state= self.state_diamond, disabledbackground=self.background)
        obj.entry_finish.config(state= self.state_diamond, disabledbackground=self.background)