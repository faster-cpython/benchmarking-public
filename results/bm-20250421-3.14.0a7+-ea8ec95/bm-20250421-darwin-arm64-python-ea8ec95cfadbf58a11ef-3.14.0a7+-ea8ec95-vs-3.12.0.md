# Results vs. 3.12.0

- fork: python
- ref: ea8ec95cfadbf58a11ef
- machine: darwin-arm64
- commit hash: ea8ec95
- commit date: 2025-04-21
- overall geometric mean: 1.045x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 187 ms: 1.11x slower                                                   |
| docutils       | 1.45 sec                                               | 1.55 sec: 1.07x slower                                                 |
| html5lib       | 33.4 ms                                                | 35.0 ms: 1.05x slower                                                  |
| sphinx         | 613 ms                                                 | 629 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 411 ms: 1.64x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 410 ms: 1.63x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 426 ms: 1.58x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 211 ms: 1.51x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 416 ms: 1.49x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 178 ms: 1.43x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 186 ms: 1.41x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 227 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 424 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 441 ms: 1.20x faster                                                   |
| async_generators                 | 299 ms                                                 | 273 ms: 1.10x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| coroutines                       | 19.7 ms                                                | 19.7 ms: 1.00x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.15x slower                                                   |
| async_tree_eager                 | 65.8 ms                                                | 76.8 ms: 1.17x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 188 ms: 1.33x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 150 ms: 3.19x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (2): async_tree_eager_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                   |
| float          | 54.1 ms                                                | 57.5 ms: 1.06x slower                                                  |
| nbody          | 67.6 ms                                                | 97.3 ms: 1.44x slower                                                  |
| Geometric mean | (ref)                                                  | 1.15x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                  |
| regex_dna      | 143 ms                                                 | 145 ms: 1.02x slower                                                   |
| regex_v8       | 15.1 ms                                                | 16.2 ms: 1.07x slower                                                  |
| regex_compile  | 75.9 ms                                                | 85.5 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 76.4 ms: 1.01x slower                                                  |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| xml_etree_generate   | 55.4 ms                                                | 61.7 ms: 1.11x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.51 sec: 1.12x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 45.8 ms: 1.18x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.76 ms: 1.25x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 183 us: 1.26x slower                                                   |
| pickle_pure_python   | 197 us                                                 | 250 us: 1.27x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 20.1 ms: 1.13x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 15.5 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.15x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 9.14 ms: 1.23x slower                                                  |
| genshi_xml      | 30.5 ms                                                | 37.5 ms: 1.23x slower                                                  |
| genshi_text     | 14.7 ms                                                | 18.5 ms: 1.26x slower                                                  |
| django_template | 19.7 ms                                                | 26.3 ms: 1.34x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.26x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.8 ms: 2.33x faster                                                  |
| mdp                              | 1.49 sec                                               | 878 ms: 1.70x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 411 ms: 1.64x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 410 ms: 1.63x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 426 ms: 1.58x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 211 ms: 1.51x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 416 ms: 1.49x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 178 ms: 1.43x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 186 ms: 1.41x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 227 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 424 ms: 1.24x faster                                                   |
| deepcopy                         | 226 us                                                 | 182 us: 1.24x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 441 ms: 1.20x faster                                                   |
| k_core                           | 1.72 sec                                               | 1.54 sec: 1.11x faster                                                 |
| deepcopy_memo                    | 26.0 us                                                | 23.4 us: 1.11x faster                                                  |
| async_generators                 | 299 ms                                                 | 273 ms: 1.10x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.93 us: 1.05x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 28.0 ms: 1.04x faster                                                  |
| pathlib                          | 24.7 ms                                                | 24.0 ms: 1.03x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| coroutines                       | 19.7 ms                                                | 19.7 ms: 1.00x faster                                                  |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 3.30 sec: 1.01x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 77.1 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.18 ms: 1.01x slower                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 76.4 ms: 1.01x slower                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 66.5 ms: 1.02x slower                                                  |
| regex_dna                        | 143 ms                                                 | 145 ms: 1.02x slower                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.58 us: 1.02x slower                                                  |
| comprehensions                   | 14.0 us                                                | 14.3 us: 1.02x slower                                                  |
| shortest_path                    | 331 ms                                                 | 339 ms: 1.02x slower                                                   |
| sphinx                           | 613 ms                                                 | 629 ms: 1.03x slower                                                   |
| json                             | 3.00 ms                                                | 3.10 ms: 1.03x slower                                                  |
| connected_components             | 300 ms                                                 | 310 ms: 1.04x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| html5lib                         | 33.4 ms                                                | 35.0 ms: 1.05x slower                                                  |
| raytrace                         | 204 ms                                                 | 215 ms: 1.05x slower                                                   |
| sympy_integrate                  | 11.1 ms                                                | 11.7 ms: 1.05x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.06x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 206 ms: 1.06x slower                                                   |
| float                            | 54.1 ms                                                | 57.5 ms: 1.06x slower                                                  |
| go                               | 98.5 ms                                                | 105 ms: 1.07x slower                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 66.1 ms: 1.07x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.55 sec: 1.07x slower                                                 |
| generators                       | 29.4 ms                                                | 31.5 ms: 1.07x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 16.2 ms: 1.07x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 78.4 ns: 1.08x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 82.6 ms: 1.08x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 94.5 ms: 1.10x slower                                                  |
| 2to3                             | 168 ms                                                 | 187 ms: 1.11x slower                                                   |
| sympy_str                        | 144 ms                                                 | 160 ms: 1.11x slower                                                   |
| xml_etree_generate               | 55.4 ms                                                | 61.7 ms: 1.11x slower                                                  |
| chaos                            | 41.6 ms                                                | 46.5 ms: 1.12x slower                                                  |
| pyflate                          | 311 ms                                                 | 347 ms: 1.12x slower                                                   |
| tomli_loads                      | 1.36 sec                                               | 1.51 sec: 1.12x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 77.3 ms: 1.12x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.12x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.88 ms: 1.12x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.38 us: 1.12x slower                                                  |
| pycparser                        | 673 ms                                                 | 757 ms: 1.12x slower                                                   |
| logging_simple                   | 3.60 us                                                | 4.06 us: 1.13x slower                                                  |
| regex_compile                    | 75.9 ms                                                | 85.5 ms: 1.13x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 83.0 ms: 1.13x slower                                                  |
| python_startup                   | 17.8 ms                                                | 20.1 ms: 1.13x slower                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.53 ms: 1.14x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 553 us: 1.15x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.15x slower                                                   |
| sympy_expand                     | 233 ms                                                 | 271 ms: 1.16x slower                                                   |
| async_tree_eager                 | 65.8 ms                                                | 76.8 ms: 1.17x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 15.5 ms: 1.17x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 45.8 ms: 1.18x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 61.0 ms: 1.19x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 52.9 ms: 1.19x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 110 us: 1.21x slower                                                   |
| many_optionals                   | 403 us                                                 | 494 us: 1.23x slower                                                   |
| mako                             | 7.44 ms                                                | 9.14 ms: 1.23x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 37.5 ms: 1.23x slower                                                  |
| telco                            | 3.92 ms                                                | 4.84 ms: 1.23x slower                                                  |
| hexiom                           | 4.38 ms                                                | 5.48 ms: 1.25x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.76 ms: 1.25x slower                                                  |
| unpickle_pure_python             | 145 us                                                 | 183 us: 1.26x slower                                                   |
| nqueens                          | 59.5 ms                                                | 75.2 ms: 1.26x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 18.5 ms: 1.26x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 250 us: 1.27x slower                                                   |
| richards_super                   | 34.6 ms                                                | 44.1 ms: 1.27x slower                                                  |
| fannkuch                         | 250 ms                                                 | 321 ms: 1.28x slower                                                   |
| coverage                         | 38.5 ms                                                | 49.4 ms: 1.28x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.28 sec: 1.30x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 635 ms: 1.31x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 188 ms: 1.33x slower                                                   |
| django_template                  | 19.7 ms                                                | 26.3 ms: 1.34x slower                                                  |
| richards                         | 30.6 ms                                                | 41.6 ms: 1.36x slower                                                  |
| nbody                            | 67.6 ms                                                | 97.3 ms: 1.44x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 150 ms: 3.19x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (3): pylint, async_tree_eager_cpu_io_mixed, asyncio_websockets
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250421-3.14.0a7+-ea8ec95/bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.045x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.10x