"use strict";(self.webpackChunktradingview=self.webpackChunktradingview||[]).push([[93659],{293659:(e,t,i)=>{i.d(t,{MiniChartPlotBase:()=>M,isTimePointIndex:()=>V});var s=i(259332),o=i(431057),r=i(998034),a=i(283873),n=i(650151),l=i(724377),h=i(444372),u=i(120984),d=i(432059),_=i(621239),c=i(643322),m=i(124829),p=i(375397),g=i(942634),f=i(957365),S=i(501571),C=i(338619),y=i(882782),v=i(975179),b=i(566238);const w=(0,C.getLogger)("Chart.MiniChart"),I=new f.VolumeFormatter;function O(e,t,i){return{time:e,color:i,value:t[4]}}function D(e,t){return{time:e,open:t[1],high:t[2],low:t[3],close:t[4]}}function L(e,t,i,s,o){return{time:e,topColor:s,bottomColor:o,lineColor:i,value:t[4]}}function T(e){const t=new Date(e);return Date.UTC(t.getFullYear(),t.getMonth(),t.getDate(),t.getHours(),t.getMinutes(),t.getSeconds())/1e3}function V(e){return(0,m.isInteger)(e)}const B=(0,s.default)(d.resetTransparency);const x={leftLogical:-.5,rightLogical:-.5,leftPx:0,rightPx:4};class M{constructor(e,t,i,s){this._symbolChanged=new g.Delegate,this._seriesChanged=new g.Delegate,this._whitespaces=null,this._symbolResolved=new g.Delegate,this._originalScaleMode=null,this._customPriceFormatter=null,this._isDestroyed=new p.WatchedValue(!1),this._status=new p.WatchedValue(0),this._noData=new p.WatchedValue(null),this._directionBasedColor=new p.WatchedValue(null),this._dataLengthInfo=null,this._sessionId=new p.WatchedValue,this._barBuilderLoader=null,this._symbolInfo=null,this._symbol={symbol:""},this._timeFrameInvalidated=new g.Delegate,this._firstValueCache=null,this._historyUpdateReceived=!1,this._miniChart=e,this._originalSeriesOptions=t,this._currentSeriesOptions=(0,r.default)({},t),this._options=s,this._horzMargins=(0,r.default)({},x,t.horzMargins),this._series=this._createSeries(),this._originalVolumeOptions=i,this._volume=this._createVolume(),this._timeFrame=e.timeframe().spawn(),this._timeFrame.subscribe(this._updateSessionId.bind(this)),this._currentlyShownDataDescription=new b.WatchedObject({timeframe:this._timeFrame.value(),symbol:this.symbol()}),this._isLastSessionInterval=(0,c.combine)((e=>"LASTSESSION"===e.value),this._miniChart.timeframe().weakReference()),this._isLastSessionInterval.subscribe(this._updateSessionId.bind(this)),this._miniChart.timeScaleSizeChanged().subscribe(null,this._timeScaleSizeChanged.bind(this))}destroy(){this._status.unsubscribe(),this._timeFrame.destroy(),this._isDestroyed.setValue(!0),this._isLastSessionInterval.destroy(),this._barBuilderLoader?.destroy()}status(){return this._status.readonly()}noData(){return this._noData.readonly()}symbolInfo(){return this._symbolInfo}symbol(){return this._symbol.symbol}subSession(){return this._sessionId.value()}setSymbol(e,t){(0,a.default)(e)&&(e={...this._symbol,symbol:e}),void 0!==t&&this._updateSeriesOptions(t),(0,y.compareSymbols)(this._symbol,e)||(this._symbol=e,this._updateSessionId(),this._symbolChanged.fire())}extendedSymbol(){return{...this._symbol,session:this._sessionId.value()}}updateSeriesOptions(e){
const t=void 0!==e.chartType&&this._originalSeriesOptions.chartType!==e.chartType;this._updateSeriesOptions(e),t?this._onChartStyleChanged():this._series.applyOptions(e)}applyOptions(e){(0,r.default)(this._options,e)}updateHorzMargins(e){this._horzMargins=(0,r.default)(this._horzMargins,e),this.fitContent()}symbolResolved(){return this._symbolResolved}symbolChanged(){return this._symbolChanged}seriesChanged(){return this._seriesChanged}timeFrameInvalidated(){return this._timeFrameInvalidated}restoreOriginalScaleMode(){null!==this._originalScaleMode&&this._series.priceScale().applyOptions({mode:this._originalScaleMode})}switchToPercentageScaleMode(){null===this._originalScaleMode&&(this._originalScaleMode=this._series.priceScale().options().mode),this._series.priceScale().applyOptions({mode:o.PriceScaleMode.Percentage})}chartSession(){return this._miniChart.chartSession()}currentSeriesOptions(){return this._currentSeriesOptions}volumeOptions(){return this._originalVolumeOptions}series(){return this._series}volume(){return this._originalVolumeOptions.visible?this._volume:null}updateData(e,t,i){e&&this.clearSourceData();const s=this._originalSeriesOptions,o=this._buildViewData(i),r=o.series.length;if(this._historyUpdateReceived=this._historyUpdateReceived||void 0===i,0===r)return void(void 0===i&&(this._dataLengthInfo=null,this._firstValueCache=null));void 0!==i||"area"!==s.chartType&&"line"!==s.chartType||(this._firstValueCache=o.series[0].value);const a=this._historyUpdateReceived&&null===this._dataLengthInfo;if(void 0!==i&&!a){const e=this._dataLengthInfo;if(null===e)return;const t={...e};e.lastBarSession=o.lastBarSession;let i=!1;for(const t of o.series)this._series.update(t),e.lastBarTime<t.time&&(e.lastBarTime=t.time,e.realtime+=1,e.lastBarIndex+=1,i=!0);if(o.additionalSeries&&this._updateAdditionalSeriesData(o.additionalSeries),o.volume)for(const e of o.volume)this._volume.update(e);if(void 0!==this._whitespacesData&&i){const t=this._whitespacesData.findIndex((t=>t.time>e.lastBarTime));-1===t?(e.whitespaces=0,this._updateWhitespaces([])):0!==t&&(e.whitespaces-=t,this._updateWhitespaces(this._whitespacesData.slice(t)))}return i&&(void 0!==e.fixLeftEdgeUntil?(this._isMainPlot()&&e.fixLeftEdgeUntil>=e.lastBarTime&&this.fitContent(),e.lastBarTime>e.fixLeftEdgeUntil&&(e.history+=e.realtime-1,e.realtime=0,e.fixLeftEdgeUntil=void 0,e.timeFrameInvalidated=!0,this._timeFrameInvalidated.fire())):e.timeFrameInvalidated||(e.timeFrameInvalidated=!0,this._timeFrameInvalidated.fire())),this._updateSeriesColor(o.series[o.series.length-1]),void this._dataUpdated(o,e,t)}const n=o.whitespaces,l=n?.length??0;this._dataLengthInfo={history:r,realtime:0,lastBarIndex:r-1,lastBarTime:o.series[o.series.length-1].time,whitespaces:l,fixLeftEdgeUntil:o.fixLeftEdgeUntil,timeFrameInvalidated:!1,lastBarSession:o.lastBarSession},this._updateSeriesColor(o.series[o.series.length-1]),this._series.applyOptions(this._currentSeriesOptions),this._applyPriceScaleFormatter(),t||this._beforeDataReady(),this._series.setData(o.series),
o.additionalSeries&&this._setAdditionalSeriesData(o.additionalSeries),o.volume&&this._volume.setData(o.volume),this._updateWhitespaces(o.whitespaces),this._dataUpdated(o,this._dataLengthInfo)}fitContent(){if(null===this._dataLengthInfo||0===this._dataLengthInfo.history)return;const{history:e,realtime:t,whitespaces:i,lastBarTime:s,fixLeftEdgeUntil:o=0}=this._dataLengthInfo,r=this._miniChart.widget(),a=r.paneSize().width;if(0===a)return;const{leftLogical:n,rightLogical:l,leftPx:h,rightPx:u}=this._horzMargins;let d=-n-(o>=s?0:t),_=e+l+i+t;if(0!==h){d-=h/((a-h)/(_-d+1))}if(0!==u){_+=u/((a-u)/(_-d+1))}_=Math.max(d,_),r.timeScale().setVisibleLogicalRange({from:d,to:_}),r.timeScale().applyOptions({lockVisibleTimeRangeOnResize:!0})}titles(){return this._currentSeriesOptions.title?[this._currentSeriesOptions.title]:[]}deleteView(){this._series.setData([]),this._whitespaces?.setData([]),this._volume.setData([])}clearData(){this._symbolInfo=null,this._historyUpdateReceived=!1,this._dataLengthInfo=null,this._firstValueCache=null,this._customPriceFormatter=null,this._status.setValue(0),this._noData.setValue(null),this._directionBasedColor.setValue(null)}resolution(){return this._miniChart.resolution()}forcePercentageMode(){return!1}lastBarTime(){return this._dataLengthInfo?.lastBarTime}getViewData(e){return this._buildViewData(e)}getLegendData(e){const{point:t,time:s,seriesData:o}=e,r=this.series(),a=this.volume();if(void 0===t||void 0===s)return[];const l=o.get(r);if(void 0===l)return[];const u=[],c=r.priceFormatter(),m=this.currentSeriesOptions();if(!1===m.visible)return[];if("Area"===r.seriesType()||"Line"===r.seriesType()||"Baseline"===r.seriesType()||"legend"===m.tooltipType||"line"===m.tooltipType){const{value:e,color:t}=l;let i;i="area"===m.chartType?void 0:t;const s=this.symbolInfo();u.push({title:m.tooltipTitle||s?.name||"",value:c.format(e),color:i||m.color,unit:m.showUnit?(0,_.prepareCurrencyValue)({currency_code:s?.currency_code,unit_id:s?.unit_id,value_unit_id:s?.value_unit_id,measure:s?.measure}):void 0})}else{const{open:e,high:t,low:s,close:o}=l,a=function(e,t){const i=e?t.up:t.down;return B(i)}(o>=e,(0,n.ensureDefined)(this._miniChart.upDownColors()[r.seriesType()]));[[h.t(null,{context:"in_legend"},i(746728)),c.format(e)],[h.t(null,{context:"in_legend"},i(943253)),c.format(t)],[h.t(null,{context:"in_legend"},i(389923)),c.format(s)],[h.t(null,{context:"in_legend"},i(102696)),c.format(o)]].forEach((([e,t])=>{u.push({value:t,title:e,color:a})}))}const p=a&&o.get(a),g=this.volumeOptions();if(p){const{value:e,color:t}=p;u.push({title:g.tooltipTitle??h.t(null,{context:"in_legend"},i(971060)),value:I.format(e),color:g.ignoreColor?void 0:t&&(0,d.resetTransparency)(t),unit:g.showUnit?this.symbolInfo()?.currency_code:void 0})}return u}isDestroyed(){return this._isDestroyed.readonly()}_isMainPlot(){return!1}_onChartStyleChanged(){this._recreateSeries(),3===this._status.value()&&this.updateData(!1,!0)}_beforeDataReady(){this._currentlyShownDataDescription.setValue({timeframe:this._timeFrame.value(),symbol:this.symbol()})}
_dataUpdated(e,t,i){}_onSymbolResolved(e){this._barBuilderLoader?.destroy(),this._barBuilderLoader=null,this._symbolInfo=e,this._symbolResolved.fire(this._symbolInfo)}_getViewData(e,t){const i=[],s={series:[],volume:i};let o=-1/0;const r=this._bars();if(r.isEmpty())return s;const a=this.minBarIndex(),n=this.maxBarIndex();if(null===a||null===n)return s;const l=t??(V(a)?a:r.firstIndex()),h=r.lastIndex();if(null===l||null===h)return s;let u;const{premarketLineColor:d,postmarketLineColor:_,premarketTopColor:c,premarketBottomColor:m,postmarketTopColor:p,postmarketBottomColor:g}=this._getPrePostMarketColors(),f=e=>{switch(e){case 0:return[d,c,m];case 1:return[_,p,g];default:return[]}};for(const t of r.rangeIterator(l,h)){const{value:r,index:a}=t;if(a<=S.UNPLOTTABLE_TIME_POINT_INDEX)continue;const n=this._miniChart.indexToTime(a);if(null===n){w.logWarn(`Couldn't find time for index ${a}`);continue}const l=T(1e3*n);if(l<=o)continue;o=l,u=l;const h=this._barIndexSession(a);s.lastBarSession=h,s.series.push(e(l,r,...f(h)));const d=r[4]>=r[1]?this._originalVolumeOptions.upColor:this._originalVolumeOptions.downColor;i.push({time:l,value:r[5],color:d})}if(this._isMainPlot()&&void 0===t&&void 0!==u)switch(this._timeFrame.value().value){case"1D":s.fixLeftEdgeUntil=u+86400-1;break;case"LASTSESSION":{let e=[],t=u+87840-1;const i=this._generateBarsToSessionEnd();i?.length&&null!==n&&n>h&&(e=i,t=i[i.length-1].time),s.fixLeftEdgeUntil=t,s.whitespaces=e}}return s}_buildViewData(e){switch(this._originalSeriesOptions.chartType){case"histogram":{const e=this._currentSeriesOptions;return this._getViewData(((t,i)=>function(e,t,i,s){const o=t[4];return{time:e,color:o>0?i:s,value:o}}(t,i,e.upColor,e.downColor)))}case"line":return this._getViewData(O,e);case"area":case"baseline":return this._getViewData(L,e);case"bars":case"candlesticks":return this._getViewData(D,e)}}_setAdditionalSeriesData(e){}_updateAdditionalSeriesData(e){}_barIndexSession(e){}_onSymbolError(e){w.logWarn((0,y.encodeExtendedSymbolOrGetSimpleSymbolString)(this._symbol)+" symbol resolving error: "+e),this.updateData(!0),this._status.setValue(1)}_onSymbolNotPermitted(){this._noData.setValue(1)}_onIntradaySpreadNotPermitted(){this._status.setValue(2),this._noData.setValue(4),this._isMainPlot()&&this._miniChart.showMessage(h.t(null,void 0,i(753434)))}_onSymbolGroupNotPermitted(){this._noData.setValue(1)}_onSymbolInvalid(){this._noData.setValue(0)}_onResolutionOrExchangeNotPermittedError(){w.logError((0,y.encodeExtendedSymbolOrGetSimpleSymbolString)(this._symbol)+" resolution or exchange permission error"),this.updateData(!0),this._isMainPlot()&&this._miniChart.showMessage(h.t(null,void 0,i(284259))),setTimeout((()=>this._miniChart.updateAvailableTimeframes()),1e3)}_onDataError(){1!==this._status.value()&&this._status.setValue(2),this._noData.setValue(3)}_onDataCompleted(){this._status.setValue(3),this._noData.setValue(0===this._bars().size()?2:null),2===this._noData.value()&&this._isMainPlot()&&this._miniChart.showMessage(h.t(null,void 0,i(212938)))}async _onData(e,t){
null!==this.minBarIndex()&&null!==this.maxBarIndex()&&this.updateData(!1,void 0,e)}_updateSeriesOptions(e){this._originalSeriesOptions=(0,r.default)(this._originalSeriesOptions,e),this._currentSeriesOptions=(0,r.default)(this._currentSeriesOptions,this._originalSeriesOptions),this._updateSeriesColor(),e.horzMargins&&this.updateHorzMargins(e.horzMargins)}_recreateSeries(){const e=this._miniChart.widget();e.removeSeries(this._series),e.removeSeries(this._volume),this._whitespaces&&(e.removeSeries(this._whitespaces),this._whitespaces=null),this._series=this._createSeries(),this._volume=this._createVolume(),this._seriesChanged.fire()}_initBarBuilder(e){return null===this._barBuilderLoader&&(this._barBuilderLoader=new u.AsyncResourceWrapper(Promise.all([i.e(97525),i.e(65414),i.e(42095),i.e(96003)]).then(i.bind(i,397796)).then((t=>new t.LightweightMiniChartBarBuilder(e))))),this._barBuilderLoader.promise()}_firstAndLastValuesForSeriesColor(e,t){if(null===this._firstValueCache||!this._dataLengthInfo)return null;if("line"!==e&&"area"!==e)return null;const i=this._series.dataByIndex(this._dataLengthInfo.lastBarIndex);return null!==i||t?(t=t??i,[this._firstValueCache,t.value]):null}_updateSeriesColor(e){const t=this._originalSeriesOptions,i=t.chartType,s=this._firstAndLastValuesForSeriesColor(i,e);if(null===s)return;const[o,r]=s;if("line"===i||"area"===i){const e="line"===i?r>=o:r>o;if("area"===i){const i=this._currentSeriesOptions;e?(i.lineColor=t.growingLineColor||t.lineColor,i.topColor=t.growingTopColor||t.topColor,i.bottomColor=t.growingBottomColor||t.bottomColor):(i.lineColor=t.fallingLineColor||t.lineColor,i.topColor=t.fallingTopColor||t.topColor,i.bottomColor=t.fallingBottomColor||t.bottomColor),i.lineColor||(i.lineColor=this._series.options().lineColor),this._series.applyOptions({topColor:i.topColor,bottomColor:i.bottomColor,lineColor:i.lineColor}),this._directionBasedColor.setValue(i.lineColor)}else if("line"===i){const{color:i,growingColor:s=i,fallingColor:o=i}=t,r=this._currentSeriesOptions;r.color=e?s:o,r.color||(r.color=this._series.options().color),this._series.applyOptions({color:r.color}),this._directionBasedColor.setValue(r.color)}}}_createSeries(){const e=this._miniChart.widget();let t;switch(this._currentSeriesOptions.chartType){case"line":t=e.addLineSeries(this._currentSeriesOptions);break;case"histogram":t=e.addHistogramSeries(this._currentSeriesOptions);break;case"area":t=e.addAreaSeries(this._currentSeriesOptions);break;case"bars":t=e.addBarSeries(this._currentSeriesOptions);break;case"candlesticks":t=e.addCandlestickSeries(this._currentSeriesOptions);break;case"baseline":t=e.addBaselineSeries(this._currentSeriesOptions)}return null===this._originalScaleMode&&(this._originalScaleMode=t.priceScale().options().mode),t.priceScale().applyOptions({scaleMargins:this._currentSeriesOptions.scaleMargins}),t}_createVolume(){const e=this._miniChart.widget().addHistogramSeries(this._originalVolumeOptions);return e.priceScale().applyOptions({scaleMargins:this._originalVolumeOptions.scaleMargins}),e}
_applyPriceScaleFormatter(){if("priceFormat"in this._originalSeriesOptions)return;const e=(0,n.ensureNotNull)(this._symbolInfo??this._miniChart.mainPlot().symbolInfo());this._currentSeriesOptions.priceFormat={type:"custom",minMove:e.minmov/e.pricescale,formatter:t=>(0,v.createSeriesFormatter)(e,"default").format(t)},this._series.applyOptions(this._currentSeriesOptions)}_updateSessionId(){this._sessionId.setValue(this._isLastSessionInterval.value()?"extended":this._symbol.session)}_updateWhitespaces(e){void 0===e||0===e.length?null!==this._whitespaces&&(this._miniChart.widget().removeSeries(this._whitespaces),this._whitespaces=null):(null===this._whitespaces&&(this._whitespaces=this._miniChart.widget().addLineSeries()),this._whitespacesData=null===this._whitespaces?void 0:e,this._whitespaces.setData(e))}_generateBarsToSessionEnd(){const e=this.symbolInfo(),t=this._bars().lastIndex(),i=this.maxBarIndex();if(e&&t&&i&&this._isLastSessionInterval.value()){let e=this._miniChart.indexToTime(t);if(null===e)return;const s=[];for(let o=t+1;o<=i;o+=1){const t=this._miniChart.indexToTime(o)??e+60;s.push({time:T(1e3*t)}),e=t}return s}}_getPrePostMarketColors(){if(!this._isMainPlot())return{};let e,t,i,s;const o=this._originalSeriesOptions.premarketLineColor,r=this._originalSeriesOptions.postmarketLineColor;if("area"===this._originalSeriesOptions.chartType&&o&&r){const a=this._currentSeriesOptions,n=a.growingTopColor||a.fallingTopColor||a.topColor;if(void 0!==n){const t=(0,l.tryParseRgba)(n);if(null!==t){const s=t[3];e=(0,d.applyAlpha)(o,s),i=(0,d.applyAlpha)(r,s)}}const h=a.growingBottomColor||a.fallingBottomColor||a.bottomColor;if(void 0!==h){const e=(0,l.tryParseRgba)(h);if(null!==e){const i=e[3];t=(0,d.applyAlpha)(o,i),s=(0,d.applyAlpha)(r,i)}}}return{premarketLineColor:o,postmarketLineColor:r,premarketTopColor:e,postmarketTopColor:i,premarketBottomColor:t,postmarketBottomColor:s}}_timeScaleSizeChanged(){this._isMainPlot()&&Promise.resolve().then((()=>this.fitContent()))}}}}]);