import os

def get_base_svg(title, width=800, height=420):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n'
    svg += '  <defs>\n'
    svg += '    <style>\n'
    svg += '      .bg { fill: #f8f9fa; rx: 10px; }\n'
    svg += '      .text-val { font-family: sans-serif; font-size: 14px; fill: #333; text-anchor: middle; font-weight: bold; }\n'
    svg += '      .text-label { font-family: sans-serif; font-size: 16px; fill: #333; text-anchor: middle; font-weight: bold; }\n'
    svg += '      .axis { stroke: #333; stroke-width: 2; }\n'
    svg += '      .title { font-family: sans-serif; font-size: 24px; fill: #333; text-anchor: middle; font-weight: bold; }\n'
    svg += '      .bracket-line { stroke-width: 2; fill: none; }\n'
    svg += '      .bracket-text { font-family: sans-serif; font-size: 16px; text-anchor: middle; font-weight: bold; }\n'
    svg += '    </style>\n'
    svg += '  </defs>\n'
    svg += f'  <rect width="100%" height="100%" class="bg" />\n'
    svg += f'  <text x="{width/2}" y="40" class="title">{title}</text>\n'
    return svg

def save_svg(name, content):
    path = f'y:/Libraries/Projects/Claude/Table Top Role Playing Game/Rules/images/{name}'
    with open(path, 'w') as f:
        f.write(content + '</svg>')

def get_bracket_type(s, attr, anchor_offset):
    # Rule: Natural extremes always override
    if s == 2: return "disaster"
    if s == 20: return "perfect"
    
    total = s + attr
    standard_anchor = attr + anchor_offset
    
    if total >= standard_anchor + 5: return "perfect"
    if total >= standard_anchor: return "standard"
    if total >= standard_anchor - 5: return "fumble"
    return "disaster"

def gen_anchored_bracket_variant(name, title, anchor_offset):
    svg = get_base_svg(title)
    colors = {"disaster": "#d9534f", "fumble": "#f0ad4e", "standard": "#5cb85c", "perfect": "#5bc0de"}
    
    margin = 60
    chart_w = 680
    chart_h = 220
    bar_w = chart_w / 19
    attr = 4
    
    probs_list = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]
    
    # Determine ranges for brackets
    bracket_ranges = {"disaster": [], "fumble": [], "standard": [], "perfect": []}
    for s in range(2, 21):
        b_type = get_bracket_type(s, attr, anchor_offset)
        bracket_ranges[b_type].append(s)
        
    bracket_y = 90
    
    def get_x_range(s_list):
        if not s_list: return None, None
        x1 = margin + (min(s_list) - 2) * bar_w + 5
        x2 = margin + (max(s_list) - 2) * bar_w + bar_w - 5
        return x1, x2

    # Draw brackets
    for b_type, label in [("disaster", "Disaster"), ("fumble", "Fumble"), ("standard", "Standard"), ("perfect", "Perfect")]:
        s_list = bracket_ranges[b_type]
        if not s_list: continue
        
        x1, x2 = get_x_range(s_list)
        count = sum(probs_list[s-2] for s in s_list)
        
        svg += f'  <path d="M {x1} 105 L {x1} {bracket_y} L {x2} {bracket_y} L {x2} 105" stroke="{colors[b_type]}" class="bracket-line" />\n'
        text_label = label if (x2 - x1) > 70 else label[0]
        svg += f'  <text x="{(x1+x2)/2}" y="{bracket_y-10}" fill="{colors[b_type]}" class="bracket-text">{text_label} ({count}%)</text>\n'

    # Draw bars
    svg += f'  <line x1="{margin}" y1="360" x2="{margin+chart_w}" y2="360" class="axis" />\n'
    
    # Reference is ALWAYS at Roll 11
    ref_total = attr + 11
    # Anchor point for Target label
    anchor_total = attr + anchor_offset
    
    for i, s in enumerate(range(2, 21)):
        total = s + attr
        p = probs_list[i]
        h = (p / 10) * chart_h
        x = margin + i * bar_w + 5
        y = 360 - h
        
        b_type = get_bracket_type(s, attr, anchor_offset)
        color = colors[b_type]
        
        svg += f'  <rect x="{x}" y="{y}" width="{bar_w-10}" height="{h}" fill="{color}" rx="3" />\n'
        svg += f'  <text x="{x + (bar_w-10)/2}" y="{y-8}" class="text-val" style="font-size:10px">{p}%</text>\n'
        
        diff = total - ref_total
        label = f"{diff:+}"
        color_style = ''
        
        if total == ref_total and total == anchor_total:
            label = "Ref/Target"
            color_style = 'fill: #d0021b;'
        elif total == ref_total:
            label = "Ref"
            color_style = 'fill: #d0021b;'
        elif total == anchor_total:
            label = "Target"
            color_style = 'fill: #007bff;'
            
        svg += f'  <text x="{x + (bar_w-10)/2}" y="385" class="text-label" style="font-size:10px;{color_style}">{label}</text>\n'
    save_svg(name, svg)

if __name__ == "__main__":
    gen_anchored_bracket_variant("custom_brackets_easy.svg", "+6 Attribute-Anchored Brackets", 6)
    gen_anchored_bracket_variant("custom_brackets_standard.svg", "+11 Attribute-Anchored Brackets", 11)
    gen_anchored_bracket_variant("custom_brackets_expert.svg", "+16 Attribute-Anchored Brackets", 16)
