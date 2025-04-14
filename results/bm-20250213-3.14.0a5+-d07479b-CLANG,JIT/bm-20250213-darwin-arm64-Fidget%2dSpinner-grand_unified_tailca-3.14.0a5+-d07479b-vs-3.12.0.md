# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: grand_unified_tailca
- machine: darwin-arm64
- commit hash: d07479b
- commit date: 2025-02-13
- overall geometric mean: 1.128x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 156 ms: 1.08x faster                                                             |
| html5lib       | 33.4 ms                                                | 29.2 ms: 1.14x faster                                                            |
| sphinx         | 613 ms                                                 | 548 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io                    | 672 ms                                                 | 343 ms: 1.96x faster                                                             |
| async_tree_io_tg                 | 673 ms                                                 | 347 ms: 1.94x faster                                                             |
| async_tree_eager_io              | 666 ms                                                 | 347 ms: 1.92x faster                                                             |
| async_tree_eager_io_tg           | 617 ms                                                 | 348 ms: 1.77x faster                                                             |
| async_tree_none_tg               | 255 ms                                                 | 146 ms: 1.75x faster                                                             |
| async_tree_none                  | 263 ms                                                 | 152 ms: 1.74x faster                                                             |
| async_tree_memoization_tg        | 318 ms                                                 | 186 ms: 1.71x faster                                                             |
| async_tree_memoization           | 310 ms                                                 | 184 ms: 1.68x faster                                                             |
| coroutines                       | 19.7 ms                                                | 14.9 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 402 ms: 1.31x faster                                                             |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 404 ms: 1.31x faster                                                             |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.22x faster                                                             |
| async_generators                 | 299 ms                                                 | 263 ms: 1.14x faster                                                             |
| async_tree_eager                 | 65.8 ms                                                | 60.3 ms: 1.09x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 352 ms: 1.06x faster                                                             |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                             |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                             |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 166 ms: 1.17x slower                                                             |
| async_tree_eager_tg              | 46.9 ms                                                | 123 ms: 2.62x slower                                                             |
| Geometric mean                   | (ref)                                                  | 1.29x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 44.4 ms: 1.22x faster                                                            |
| nbody          | 67.6 ms                                                | 63.8 ms: 1.06x faster                                                            |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 63.4 ms: 1.20x faster                                                            |
| regex_effbot   | 2.44 ms                                                | 2.45 ms: 1.00x slower                                                            |
| regex_dna      | 143 ms                                                 | 149 ms: 1.04x slower                                                             |
| regex_v8       | 15.1 ms                                                | 18.3 ms: 1.21x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_process    | 38.9 ms                                                | 33.0 ms: 1.18x faster                                                            |
| tomli_loads          | 1.36 sec                                               | 1.17 sec: 1.16x faster                                                           |
| xml_etree_generate   | 55.4 ms                                                | 47.8 ms: 1.16x faster                                                            |
| unpickle_pure_python | 145 us                                                 | 127 us: 1.14x faster                                                             |
| xml_etree_parse      | 108 ms                                                 | 97.0 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 75.5 ms                                                | 68.8 ms: 1.10x faster                                                            |
| pickle_pure_python   | 197 us                                                 | 185 us: 1.06x faster                                                             |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                            |
| json_dumps           | 6.19 ms                                                | 7.24 ms: 1.17x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 12.7 ms: 1.04x faster                                                            |
| python_startup         | 17.8 ms                                                | 17.2 ms: 1.03x faster                                                            |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.7 ms: 1.16x faster                                                            |
| mako            | 7.44 ms                                                | 6.46 ms: 1.15x faster                                                            |
| genshi_xml      | 30.5 ms                                                | 27.0 ms: 1.13x faster                                                            |
| django_template | 19.7 ms                                                | 18.9 ms: 1.04x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                     |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.5 ms: 2.80x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 343 ms: 1.96x faster                                                             |
| async_tree_io_tg                 | 673 ms                                                 | 347 ms: 1.94x faster                                                             |
| async_tree_eager_io              | 666 ms                                                 | 347 ms: 1.92x faster                                                             |
| async_tree_eager_io_tg           | 617 ms                                                 | 348 ms: 1.77x faster                                                             |
| async_tree_none_tg               | 255 ms                                                 | 146 ms: 1.75x faster                                                             |
| async_tree_none                  | 263 ms                                                 | 152 ms: 1.74x faster                                                             |
| async_tree_memoization_tg        | 318 ms                                                 | 186 ms: 1.71x faster                                                             |
| async_tree_memoization           | 310 ms                                                 | 184 ms: 1.68x faster                                                             |
| deepcopy                         | 226 us                                                 | 138 us: 1.63x faster                                                             |
| generators                       | 29.4 ms                                                | 18.1 ms: 1.62x faster                                                            |
| deepcopy_memo                    | 26.0 us                                                | 16.6 us: 1.57x faster                                                            |
| go                               | 98.5 ms                                                | 72.6 ms: 1.36x faster                                                            |
| deepcopy_reduce                  | 2.01 us                                                | 1.48 us: 1.36x faster                                                            |
| coroutines                       | 19.7 ms                                                | 14.9 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 402 ms: 1.31x faster                                                             |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 404 ms: 1.31x faster                                                             |
| raytrace                         | 204 ms                                                 | 162 ms: 1.26x faster                                                             |
| logging_silent                   | 72.5 ns                                                | 58.1 ns: 1.25x faster                                                            |
| deltablue                        | 2.57 ms                                                | 2.06 ms: 1.24x faster                                                            |
| logging_simple                   | 3.60 us                                                | 2.93 us: 1.23x faster                                                            |
| comprehensions                   | 14.0 us                                                | 11.5 us: 1.22x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.22x faster                                                             |
| float                            | 54.1 ms                                                | 44.4 ms: 1.22x faster                                                            |
| logging_format                   | 3.90 us                                                | 3.22 us: 1.21x faster                                                            |
| pylint                           | 182 ms                                                 | 150 ms: 1.21x faster                                                             |
| regex_compile                    | 75.9 ms                                                | 63.4 ms: 1.20x faster                                                            |
| xml_etree_process                | 38.9 ms                                                | 33.0 ms: 1.18x faster                                                            |
| chaos                            | 41.6 ms                                                | 35.8 ms: 1.16x faster                                                            |
| genshi_text                      | 14.7 ms                                                | 12.7 ms: 1.16x faster                                                            |
| tomli_loads                      | 1.36 sec                                               | 1.17 sec: 1.16x faster                                                           |
| xml_etree_generate               | 55.4 ms                                                | 47.8 ms: 1.16x faster                                                            |
| scimark_sor                      | 85.8 ms                                                | 74.2 ms: 1.16x faster                                                            |
| mako                             | 7.44 ms                                                | 6.46 ms: 1.15x faster                                                            |
| html5lib                         | 33.4 ms                                                | 29.2 ms: 1.14x faster                                                            |
| unpickle_pure_python             | 145 us                                                 | 127 us: 1.14x faster                                                             |
| thrift                           | 468 us                                                 | 411 us: 1.14x faster                                                             |
| bpe_tokeniser                    | 3.28 sec                                               | 2.89 sec: 1.14x faster                                                           |
| async_generators                 | 299 ms                                                 | 263 ms: 1.14x faster                                                             |
| scimark_monte_carlo              | 44.5 ms                                                | 39.2 ms: 1.13x faster                                                            |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                           |
| genshi_xml                       | 30.5 ms                                                | 27.0 ms: 1.13x faster                                                            |
| nqueens                          | 59.5 ms                                                | 52.8 ms: 1.13x faster                                                            |
| spectral_norm                    | 76.5 ms                                                | 68.0 ms: 1.13x faster                                                            |
| sqlalchemy_declarative           | 61.9 ms                                                | 55.3 ms: 1.12x faster                                                            |
| hexiom                           | 4.38 ms                                                | 3.91 ms: 1.12x faster                                                            |
| sphinx                           | 613 ms                                                 | 548 ms: 1.12x faster                                                             |
| xml_etree_parse                  | 108 ms                                                 | 97.0 ms: 1.11x faster                                                            |
| richards_super                   | 34.6 ms                                                | 31.3 ms: 1.11x faster                                                            |
| richards                         | 30.6 ms                                                | 27.7 ms: 1.10x faster                                                            |
| sympy_str                        | 144 ms                                                 | 131 ms: 1.10x faster                                                             |
| xml_etree_iterparse              | 75.5 ms                                                | 68.8 ms: 1.10x faster                                                            |
| pathlib                          | 24.7 ms                                                | 22.5 ms: 1.10x faster                                                            |
| sympy_sum                        | 76.2 ms                                                | 69.5 ms: 1.10x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 60.3 ms: 1.09x faster                                                            |
| bench_mp_pool                    | 65.5 ms                                                | 60.2 ms: 1.09x faster                                                            |
| 2to3                             | 168 ms                                                 | 156 ms: 1.08x faster                                                             |
| dulwich_log                      | 29.2 ms                                                | 27.1 ms: 1.08x faster                                                            |
| sqlglot_optimize                 | 33.2 ms                                                | 31.0 ms: 1.07x faster                                                            |
| sympy_integrate                  | 11.1 ms                                                | 10.3 ms: 1.07x faster                                                            |
| sqlglot_normalize                | 180 ms                                                 | 168 ms: 1.07x faster                                                             |
| pickle_pure_python               | 197 us                                                 | 185 us: 1.06x faster                                                             |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 352 ms: 1.06x faster                                                             |
| scimark_fft                      | 194 ms                                                 | 183 ms: 1.06x faster                                                             |
| nbody                            | 67.6 ms                                                | 63.8 ms: 1.06x faster                                                            |
| bench_thread_pool                | 483 us                                                 | 457 us: 1.06x faster                                                             |
| sympy_expand                     | 233 ms                                                 | 221 ms: 1.05x faster                                                             |
| pyflate                          | 311 ms                                                 | 296 ms: 1.05x faster                                                             |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.01 ms: 1.04x faster                                                            |
| typing_runtime_protocols         | 91.5 us                                                | 87.9 us: 1.04x faster                                                            |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.34 ms: 1.04x faster                                                            |
| django_template                  | 19.7 ms                                                | 18.9 ms: 1.04x faster                                                            |
| mdp                              | 1.49 sec                                               | 1.43 sec: 1.04x faster                                                           |
| scimark_lu                       | 73.5 ms                                                | 70.7 ms: 1.04x faster                                                            |
| python_startup_no_site           | 13.2 ms                                                | 12.7 ms: 1.04x faster                                                            |
| python_startup                   | 17.8 ms                                                | 17.2 ms: 1.03x faster                                                            |
| pycparser                        | 673 ms                                                 | 654 ms: 1.03x faster                                                             |
| dask                             | 779 ms                                                 | 766 ms: 1.02x faster                                                             |
| shortest_path                    | 331 ms                                                 | 326 ms: 1.01x faster                                                             |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                             |
| sqlglot_transpile                | 973 us                                                 | 968 us: 1.01x faster                                                             |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                             |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.00x faster                                                            |
| connected_components             | 300 ms                                                 | 299 ms: 1.00x faster                                                             |
| regex_effbot                     | 2.44 ms                                                | 2.45 ms: 1.00x slower                                                            |
| crypto_pyaes                     | 51.4 ms                                                | 52.0 ms: 1.01x slower                                                            |
| pprint_pformat                   | 986 ms                                                 | 1.01 sec: 1.02x slower                                                           |
| pprint_safe_repr                 | 483 ms                                                 | 504 ms: 1.04x slower                                                             |
| regex_dna                        | 143 ms                                                 | 149 ms: 1.04x slower                                                             |
| gc_traversal                     | 2.95 ms                                                | 3.10 ms: 1.05x slower                                                            |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                            |
| many_optionals                   | 403 us                                                 | 427 us: 1.06x slower                                                             |
| meteor_contest                   | 69.1 ms                                                | 74.5 ms: 1.08x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                             |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.11x slower                                                            |
| fannkuch                         | 250 ms                                                 | 284 ms: 1.13x slower                                                             |
| telco                            | 3.92 ms                                                | 4.49 ms: 1.14x slower                                                            |
| coverage                         | 38.5 ms                                                | 44.7 ms: 1.16x slower                                                            |
| json_dumps                       | 6.19 ms                                                | 7.24 ms: 1.17x slower                                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 166 ms: 1.17x slower                                                             |
| regex_v8                         | 15.1 ms                                                | 18.3 ms: 1.21x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 123 ms: 2.62x slower                                                             |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                                     |

Benchmark hidden because not significant (3): docutils, sqlglot_parse, json
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.128x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x