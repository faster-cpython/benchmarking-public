# Results vs. 3.12.0

- fork: JelleZijlstra
- ref: sunder_io
- machine: darwin-arm64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.103x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 160 ms: 1.05x faster                                               |
| docutils       | 1.45 sec                                               | 1.42 sec: 1.03x faster                                             |
| html5lib       | 33.4 ms                                                | 29.2 ms: 1.14x faster                                              |
| sphinx         | 613 ms                                                 | 574 ms: 1.07x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 351 ms: 1.92x faster                                               |
| async_tree_io                    | 672 ms                                                 | 354 ms: 1.90x faster                                               |
| async_tree_eager_io              | 666 ms                                                 | 359 ms: 1.85x faster                                               |
| async_tree_memoization_tg        | 318 ms                                                 | 184 ms: 1.73x faster                                               |
| async_tree_eager_io_tg           | 617 ms                                                 | 360 ms: 1.72x faster                                               |
| async_tree_none_tg               | 255 ms                                                 | 151 ms: 1.69x faster                                               |
| async_tree_none                  | 263 ms                                                 | 159 ms: 1.66x faster                                               |
| async_tree_memoization           | 310 ms                                                 | 190 ms: 1.64x faster                                               |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 399 ms: 1.32x faster                                               |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 402 ms: 1.31x faster                                               |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.24x faster                                               |
| async_generators                 | 299 ms                                                 | 246 ms: 1.22x faster                                               |
| coroutines                       | 19.7 ms                                                | 16.3 ms: 1.21x faster                                              |
| async_tree_eager                 | 65.8 ms                                                | 59.9 ms: 1.10x faster                                              |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 347 ms: 1.08x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                               |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 167 ms: 1.18x slower                                               |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.76x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.27x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 45.7 ms: 1.18x faster                                              |
| nbody          | 67.6 ms                                                | 70.7 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 66.1 ms: 1.15x faster                                              |
| regex_effbot   | 2.44 ms                                                | 2.26 ms: 1.08x faster                                              |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                               |
| regex_v8       | 15.1 ms                                                | 15.7 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.21 sec: 1.12x faster                                             |
| xml_etree_iterparse  | 75.5 ms                                                | 71.6 ms: 1.05x faster                                              |
| xml_etree_generate   | 55.4 ms                                                | 53.5 ms: 1.04x faster                                              |
| xml_etree_process    | 38.9 ms                                                | 38.1 ms: 1.02x faster                                              |
| unpickle_pure_python | 145 us                                                 | 143 us: 1.02x faster                                               |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.01x slower                                               |
| pickle_pure_python   | 197 us                                                 | 201 us: 1.02x slower                                               |
| json_loads           | 17.0 us                                                | 17.6 us: 1.03x slower                                              |
| json_dumps           | 6.19 ms                                                | 7.37 ms: 1.19x slower                                              |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 14.7 ms: 1.12x slower                                              |
| python_startup         | 17.8 ms                                                | 19.9 ms: 1.12x slower                                              |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 13.6 ms: 1.08x faster                                              |
| genshi_xml      | 30.5 ms                                                | 28.4 ms: 1.08x faster                                              |
| mako            | 7.44 ms                                                | 7.62 ms: 1.02x slower                                              |
| django_template | 19.7 ms                                                | 20.5 ms: 1.04x slower                                              |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                       |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.0 ms: 2.68x faster                                              |
| mdp                              | 1.49 sec                                               | 742 ms: 2.01x faster                                               |
| async_tree_io_tg                 | 673 ms                                                 | 351 ms: 1.92x faster                                               |
| async_tree_io                    | 672 ms                                                 | 354 ms: 1.90x faster                                               |
| async_tree_eager_io              | 666 ms                                                 | 359 ms: 1.85x faster                                               |
| async_tree_memoization_tg        | 318 ms                                                 | 184 ms: 1.73x faster                                               |
| async_tree_eager_io_tg           | 617 ms                                                 | 360 ms: 1.72x faster                                               |
| async_tree_none_tg               | 255 ms                                                 | 151 ms: 1.69x faster                                               |
| async_tree_none                  | 263 ms                                                 | 159 ms: 1.66x faster                                               |
| async_tree_memoization           | 310 ms                                                 | 190 ms: 1.64x faster                                               |
| deepcopy                         | 226 us                                                 | 147 us: 1.53x faster                                               |
| deepcopy_memo                    | 26.0 us                                                | 18.1 us: 1.44x faster                                              |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 399 ms: 1.32x faster                                               |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 402 ms: 1.31x faster                                               |
| deepcopy_reduce                  | 2.01 us                                                | 1.59 us: 1.27x faster                                              |
| generators                       | 29.4 ms                                                | 23.2 ms: 1.26x faster                                              |
| comprehensions                   | 14.0 us                                                | 11.2 us: 1.26x faster                                              |
| go                               | 98.5 ms                                                | 78.6 ms: 1.25x faster                                              |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.24x faster                                               |
| dulwich_log                      | 29.2 ms                                                | 24.0 ms: 1.22x faster                                              |
| async_generators                 | 299 ms                                                 | 246 ms: 1.22x faster                                               |
| raytrace                         | 204 ms                                                 | 168 ms: 1.22x faster                                               |
| coroutines                       | 19.7 ms                                                | 16.3 ms: 1.21x faster                                              |
| float                            | 54.1 ms                                                | 45.7 ms: 1.18x faster                                              |
| regex_compile                    | 75.9 ms                                                | 66.1 ms: 1.15x faster                                              |
| html5lib                         | 33.4 ms                                                | 29.2 ms: 1.14x faster                                              |
| pylint                           | 182 ms                                                 | 159 ms: 1.14x faster                                               |
| k_core                           | 1.72 sec                                               | 1.51 sec: 1.14x faster                                             |
| spectral_norm                    | 76.5 ms                                                | 68.2 ms: 1.12x faster                                              |
| bpe_tokeniser                    | 3.28 sec                                               | 2.93 sec: 1.12x faster                                             |
| tomli_loads                      | 1.36 sec                                               | 1.21 sec: 1.12x faster                                             |
| logging_silent                   | 72.5 ns                                                | 64.8 ns: 1.12x faster                                              |
| chaos                            | 41.6 ms                                                | 37.3 ms: 1.12x faster                                              |
| deltablue                        | 2.57 ms                                                | 2.30 ms: 1.11x faster                                              |
| scimark_sor                      | 85.8 ms                                                | 77.6 ms: 1.11x faster                                              |
| logging_simple                   | 3.60 us                                                | 3.28 us: 1.10x faster                                              |
| async_tree_eager                 | 65.8 ms                                                | 59.9 ms: 1.10x faster                                              |
| logging_format                   | 3.90 us                                                | 3.58 us: 1.09x faster                                              |
| pyflate                          | 311 ms                                                 | 286 ms: 1.09x faster                                               |
| genshi_text                      | 14.7 ms                                                | 13.6 ms: 1.08x faster                                              |
| regex_effbot                     | 2.44 ms                                                | 2.26 ms: 1.08x faster                                              |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 347 ms: 1.08x faster                                               |
| genshi_xml                       | 30.5 ms                                                | 28.4 ms: 1.08x faster                                              |
| sphinx                           | 613 ms                                                 | 574 ms: 1.07x faster                                               |
| scimark_fft                      | 194 ms                                                 | 183 ms: 1.06x faster                                               |
| sqlalchemy_declarative           | 61.9 ms                                                | 58.4 ms: 1.06x faster                                              |
| scimark_monte_carlo              | 44.5 ms                                                | 42.0 ms: 1.06x faster                                              |
| pathlib                          | 24.7 ms                                                | 23.3 ms: 1.06x faster                                              |
| sympy_str                        | 144 ms                                                 | 136 ms: 1.05x faster                                               |
| xml_etree_iterparse              | 75.5 ms                                                | 71.6 ms: 1.05x faster                                              |
| sympy_integrate                  | 11.1 ms                                                | 10.5 ms: 1.05x faster                                              |
| 2to3                             | 168 ms                                                 | 160 ms: 1.05x faster                                               |
| sympy_sum                        | 76.2 ms                                                | 72.8 ms: 1.05x faster                                              |
| pycparser                        | 673 ms                                                 | 646 ms: 1.04x faster                                               |
| nqueens                          | 59.5 ms                                                | 57.2 ms: 1.04x faster                                              |
| xml_etree_generate               | 55.4 ms                                                | 53.5 ms: 1.04x faster                                              |
| hexiom                           | 4.38 ms                                                | 4.23 ms: 1.03x faster                                              |
| docutils                         | 1.45 sec                                               | 1.42 sec: 1.03x faster                                             |
| pprint_pformat                   | 986 ms                                                 | 964 ms: 1.02x faster                                               |
| xml_etree_process                | 38.9 ms                                                | 38.1 ms: 1.02x faster                                              |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.09 ms: 1.02x faster                                              |
| unpickle_pure_python             | 145 us                                                 | 143 us: 1.02x faster                                               |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                               |
| sympy_expand                     | 233 ms                                                 | 230 ms: 1.01x faster                                               |
| pprint_safe_repr                 | 483 ms                                                 | 477 ms: 1.01x faster                                               |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.52 ms: 1.01x faster                                              |
| scimark_lu                       | 73.5 ms                                                | 74.1 ms: 1.01x slower                                              |
| connected_components             | 300 ms                                                 | 303 ms: 1.01x slower                                               |
| xml_etree_parse                  | 108 ms                                                 | 109 ms: 1.01x slower                                               |
| typing_runtime_protocols         | 91.5 us                                                | 93.1 us: 1.02x slower                                              |
| pickle_pure_python               | 197 us                                                 | 201 us: 1.02x slower                                               |
| mako                             | 7.44 ms                                                | 7.62 ms: 1.02x slower                                              |
| bench_thread_pool                | 483 us                                                 | 497 us: 1.03x slower                                               |
| json_loads                       | 17.0 us                                                | 17.6 us: 1.03x slower                                              |
| fannkuch                         | 250 ms                                                 | 260 ms: 1.04x slower                                               |
| regex_v8                         | 15.1 ms                                                | 15.7 ms: 1.04x slower                                              |
| django_template                  | 19.7 ms                                                | 20.5 ms: 1.04x slower                                              |
| meteor_contest                   | 69.1 ms                                                | 71.9 ms: 1.04x slower                                              |
| nbody                            | 67.6 ms                                                | 70.7 ms: 1.05x slower                                              |
| richards_super                   | 34.6 ms                                                | 36.3 ms: 1.05x slower                                              |
| gc_traversal                     | 2.95 ms                                                | 3.10 ms: 1.05x slower                                              |
| richards                         | 30.6 ms                                                | 32.3 ms: 1.06x slower                                              |
| crypto_pyaes                     | 51.4 ms                                                | 54.8 ms: 1.07x slower                                              |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                               |
| many_optionals                   | 403 us                                                 | 439 us: 1.09x slower                                               |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.11x slower                                              |
| python_startup_no_site           | 13.2 ms                                                | 14.7 ms: 1.12x slower                                              |
| python_startup                   | 17.8 ms                                                | 19.9 ms: 1.12x slower                                              |
| telco                            | 3.92 ms                                                | 4.54 ms: 1.16x slower                                              |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 167 ms: 1.18x slower                                               |
| json_dumps                       | 6.19 ms                                                | 7.37 ms: 1.19x slower                                              |
| coverage                         | 38.5 ms                                                | 47.6 ms: 1.24x slower                                              |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.76x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                       |

Benchmark hidden because not significant (6): shortest_path, asyncio_websockets, pidigits, sqlite_synth, bench_mp_pool, json
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250425-3.14.0a7+-dac50cc/bm-20250425-darwin-arm64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.11x