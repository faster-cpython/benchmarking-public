# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: grand_unified_tailca
- machine: darwin-arm64
- commit hash: d07479b
- commit date: 2025-02-13
- overall geometric mean: 1.132x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 156 ms: 1.15x faster                                                             |
| html5lib       | 36.7 ms                                                | 29.2 ms: 1.26x faster                                                            |
| sphinx         | 602 ms                                                 | 548 ms: 1.10x faster                                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                     |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 186 ms: 1.55x faster                                                             |
| async_tree_io                    | 508 ms                                                 | 343 ms: 1.48x faster                                                             |
| async_tree_eager_io              | 511 ms                                                 | 347 ms: 1.47x faster                                                             |
| async_tree_memoization           | 268 ms                                                 | 184 ms: 1.45x faster                                                             |
| async_tree_io_tg                 | 500 ms                                                 | 347 ms: 1.44x faster                                                             |
| async_tree_none                  | 212 ms                                                 | 152 ms: 1.40x faster                                                             |
| async_tree_eager_io_tg           | 479 ms                                                 | 348 ms: 1.37x faster                                                             |
| async_tree_none_tg               | 198 ms                                                 | 146 ms: 1.36x faster                                                             |
| coroutines                       | 20.0 ms                                                | 14.9 ms: 1.34x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.23x faster                                                             |
| async_tree_eager                 | 69.9 ms                                                | 60.3 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 402 ms: 1.14x faster                                                             |
| async_generators                 | 294 ms                                                 | 263 ms: 1.12x faster                                                             |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 404 ms: 1.11x faster                                                             |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 352 ms: 1.06x faster                                                             |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                             |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                             |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 166 ms: 1.21x slower                                                             |
| async_tree_eager_tg              | 47.4 ms                                                | 123 ms: 2.60x slower                                                             |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 44.4 ms: 1.26x faster                                                            |
| nbody          | 73.6 ms                                                | 63.8 ms: 1.15x faster                                                            |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 63.4 ms: 1.23x faster                                                            |
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                            |
| regex_v8       | 17.0 ms                                                | 18.3 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.17 sec: 1.34x faster                                                           |
| unpickle_pure_python | 165 us                                                 | 127 us: 1.30x faster                                                             |
| xml_etree_process    | 41.3 ms                                                | 33.0 ms: 1.25x faster                                                            |
| xml_etree_generate   | 57.1 ms                                                | 47.8 ms: 1.19x faster                                                            |
| pickle_pure_python   | 215 us                                                 | 185 us: 1.16x faster                                                             |
| xml_etree_parse      | 108 ms                                                 | 97.0 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 74.2 ms                                                | 68.8 ms: 1.08x faster                                                            |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                            |
| json_dumps           | 6.47 ms                                                | 7.24 ms: 1.12x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.2 ms: 1.09x faster                                                            |
| python_startup_no_site | 13.7 ms                                                | 12.7 ms: 1.08x faster                                                            |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.7 ms: 1.34x faster                                                            |
| genshi_xml      | 34.1 ms                                                | 27.0 ms: 1.26x faster                                                            |
| mako            | 7.75 ms                                                | 6.46 ms: 1.20x faster                                                            |
| django_template | 20.5 ms                                                | 18.9 ms: 1.08x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.22x faster                                                                     |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators                       | 31.9 ms                                                | 18.1 ms: 1.76x faster                                                            |
| deepcopy                         | 236 us                                                 | 138 us: 1.71x faster                                                             |
| deepcopy_memo                    | 27.4 us                                                | 16.6 us: 1.65x faster                                                            |
| go                               | 117 ms                                                 | 72.6 ms: 1.61x faster                                                            |
| async_tree_memoization_tg        | 288 ms                                                 | 186 ms: 1.55x faster                                                             |
| async_tree_io                    | 508 ms                                                 | 343 ms: 1.48x faster                                                             |
| async_tree_eager_io              | 511 ms                                                 | 347 ms: 1.47x faster                                                             |
| async_tree_memoization           | 268 ms                                                 | 184 ms: 1.45x faster                                                             |
| async_tree_io_tg                 | 500 ms                                                 | 347 ms: 1.44x faster                                                             |
| scimark_sor                      | 106 ms                                                 | 74.2 ms: 1.43x faster                                                            |
| deepcopy_reduce                  | 2.09 us                                                | 1.48 us: 1.41x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 152 ms: 1.40x faster                                                             |
| async_tree_eager_io_tg           | 479 ms                                                 | 348 ms: 1.37x faster                                                             |
| async_tree_none_tg               | 198 ms                                                 | 146 ms: 1.36x faster                                                             |
| coroutines                       | 20.0 ms                                                | 14.9 ms: 1.34x faster                                                            |
| tomli_loads                      | 1.57 sec                                               | 1.17 sec: 1.34x faster                                                           |
| genshi_text                      | 16.9 ms                                                | 12.7 ms: 1.34x faster                                                            |
| richards                         | 36.2 ms                                                | 27.7 ms: 1.30x faster                                                            |
| unpickle_pure_python             | 165 us                                                 | 127 us: 1.30x faster                                                             |
| scimark_monte_carlo              | 50.4 ms                                                | 39.2 ms: 1.29x faster                                                            |
| deltablue                        | 2.65 ms                                                | 2.06 ms: 1.28x faster                                                            |
| genshi_xml                       | 34.1 ms                                                | 27.0 ms: 1.26x faster                                                            |
| float                            | 55.8 ms                                                | 44.4 ms: 1.26x faster                                                            |
| html5lib                         | 36.7 ms                                                | 29.2 ms: 1.26x faster                                                            |
| richards_super                   | 39.2 ms                                                | 31.3 ms: 1.25x faster                                                            |
| xml_etree_process                | 41.3 ms                                                | 33.0 ms: 1.25x faster                                                            |
| hexiom                           | 4.87 ms                                                | 3.91 ms: 1.24x faster                                                            |
| regex_compile                    | 78.3 ms                                                | 63.4 ms: 1.23x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.23x faster                                                             |
| logging_silent                   | 71.0 ns                                                | 58.1 ns: 1.22x faster                                                            |
| logging_simple                   | 3.56 us                                                | 2.93 us: 1.22x faster                                                            |
| mako                             | 7.75 ms                                                | 6.46 ms: 1.20x faster                                                            |
| pylint                           | 180 ms                                                 | 150 ms: 1.20x faster                                                             |
| logging_format                   | 3.85 us                                                | 3.22 us: 1.20x faster                                                            |
| xml_etree_generate               | 57.1 ms                                                | 47.8 ms: 1.19x faster                                                            |
| pyflate                          | 352 ms                                                 | 296 ms: 1.19x faster                                                             |
| nqueens                          | 61.8 ms                                                | 52.8 ms: 1.17x faster                                                            |
| async_tree_eager                 | 69.9 ms                                                | 60.3 ms: 1.16x faster                                                            |
| pickle_pure_python               | 215 us                                                 | 185 us: 1.16x faster                                                             |
| nbody                            | 73.6 ms                                                | 63.8 ms: 1.15x faster                                                            |
| chaos                            | 41.1 ms                                                | 35.8 ms: 1.15x faster                                                            |
| 2to3                             | 179 ms                                                 | 156 ms: 1.15x faster                                                             |
| typing_runtime_protocols         | 101 us                                                 | 87.9 us: 1.15x faster                                                            |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 402 ms: 1.14x faster                                                             |
| thrift                           | 466 us                                                 | 411 us: 1.13x faster                                                             |
| bpe_tokeniser                    | 3.26 sec                                               | 2.89 sec: 1.13x faster                                                           |
| spectral_norm                    | 76.5 ms                                                | 68.0 ms: 1.12x faster                                                            |
| sqlglot_normalize                | 188 ms                                                 | 168 ms: 1.12x faster                                                             |
| sqlglot_optimize                 | 34.7 ms                                                | 31.0 ms: 1.12x faster                                                            |
| sympy_expand                     | 248 ms                                                 | 221 ms: 1.12x faster                                                             |
| async_generators                 | 294 ms                                                 | 263 ms: 1.12x faster                                                             |
| raytrace                         | 181 ms                                                 | 162 ms: 1.12x faster                                                             |
| sympy_str                        | 146 ms                                                 | 131 ms: 1.11x faster                                                             |
| xml_etree_parse                  | 108 ms                                                 | 97.0 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 404 ms: 1.11x faster                                                             |
| bench_thread_pool                | 503 us                                                 | 457 us: 1.10x faster                                                             |
| sphinx                           | 602 ms                                                 | 548 ms: 1.10x faster                                                             |
| python_startup                   | 18.8 ms                                                | 17.2 ms: 1.09x faster                                                            |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.09x faster                                                            |
| scimark_fft                      | 200 ms                                                 | 183 ms: 1.09x faster                                                             |
| pprint_pformat                   | 1.10 sec                                               | 1.01 sec: 1.09x faster                                                           |
| django_template                  | 20.5 ms                                                | 18.9 ms: 1.08x faster                                                            |
| sympy_sum                        | 75.1 ms                                                | 69.5 ms: 1.08x faster                                                            |
| python_startup_no_site           | 13.7 ms                                                | 12.7 ms: 1.08x faster                                                            |
| xml_etree_iterparse              | 74.2 ms                                                | 68.8 ms: 1.08x faster                                                            |
| telco                            | 4.84 ms                                                | 4.49 ms: 1.08x faster                                                            |
| bench_mp_pool                    | 64.7 ms                                                | 60.2 ms: 1.08x faster                                                            |
| regex_effbot                     | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                            |
| scimark_lu                       | 75.9 ms                                                | 70.7 ms: 1.07x faster                                                            |
| pprint_safe_repr                 | 541 ms                                                 | 504 ms: 1.07x faster                                                             |
| sqlglot_transpile                | 1.04 ms                                                | 968 us: 1.07x faster                                                             |
| pycparser                        | 701 ms                                                 | 654 ms: 1.07x faster                                                             |
| sqlalchemy_declarative           | 59.0 ms                                                | 55.3 ms: 1.07x faster                                                            |
| connected_components             | 319 ms                                                 | 299 ms: 1.07x faster                                                             |
| crypto_pyaes                     | 55.3 ms                                                | 52.0 ms: 1.06x faster                                                            |
| dulwich_log                      | 28.7 ms                                                | 27.1 ms: 1.06x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 352 ms: 1.06x faster                                                             |
| shortest_path                    | 345 ms                                                 | 326 ms: 1.06x faster                                                             |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                                           |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.34 ms: 1.06x faster                                                            |
| sqlglot_parse                    | 852 us                                                 | 811 us: 1.05x faster                                                             |
| mdp                              | 1.50 sec                                               | 1.43 sec: 1.04x faster                                                           |
| comprehensions                   | 12.0 us                                                | 11.5 us: 1.04x faster                                                            |
| coverage                         | 46.2 ms                                                | 44.7 ms: 1.03x faster                                                            |
| pathlib                          | 23.2 ms                                                | 22.5 ms: 1.03x faster                                                            |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                             |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                            |
| dask                             | 771 ms                                                 | 766 ms: 1.01x faster                                                             |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                             |
| meteor_contest                   | 74.0 ms                                                | 74.5 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.01 ms: 1.01x slower                                                            |
| fannkuch                         | 279 ms                                                 | 284 ms: 1.02x slower                                                             |
| many_optionals                   | 409 us                                                 | 427 us: 1.04x slower                                                             |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                            |
| gc_traversal                     | 2.94 ms                                                | 3.10 ms: 1.05x slower                                                            |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.07x slower                                                            |
| regex_v8                         | 17.0 ms                                                | 18.3 ms: 1.08x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                             |
| json_dumps                       | 6.47 ms                                                | 7.24 ms: 1.12x slower                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 166 ms: 1.21x slower                                                             |
| subparsers                       | 9.44 ms                                                | 11.5 ms: 1.22x slower                                                            |
| async_tree_eager_tg              | 47.4 ms                                                | 123 ms: 2.60x slower                                                             |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                                     |

Benchmark hidden because not significant (3): json, regex_dna, docutils
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.132x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.08x