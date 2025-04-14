# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: darwin-arm64
- commit hash: d270553
- commit date: 2025-02-20
- overall geometric mean: 1.005x faster
- HPT reliability: 92.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 200 ms: 1.19x slower                                                      |
| docutils       | 1.45 sec                                               | 1.49 sec: 1.03x slower                                                    |
| html5lib       | 33.4 ms                                                | 32.2 ms: 1.04x faster                                                     |
| sphinx         | 613 ms                                                 | 605 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 388 ms: 1.73x faster                                                      |
| async_tree_eager_io              | 666 ms                                                 | 389 ms: 1.71x faster                                                      |
| async_tree_io                    | 672 ms                                                 | 408 ms: 1.65x faster                                                      |
| async_tree_eager_io_tg           | 617 ms                                                 | 400 ms: 1.54x faster                                                      |
| async_tree_none_tg               | 255 ms                                                 | 166 ms: 1.53x faster                                                      |
| async_tree_memoization_tg        | 318 ms                                                 | 208 ms: 1.53x faster                                                      |
| async_tree_none                  | 263 ms                                                 | 177 ms: 1.49x faster                                                      |
| async_tree_memoization           | 310 ms                                                 | 211 ms: 1.47x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 426 ms: 1.24x faster                                                      |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 429 ms: 1.23x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                      |
| async_generators                 | 299 ms                                                 | 270 ms: 1.11x faster                                                      |
| coroutines                       | 19.7 ms                                                | 17.9 ms: 1.10x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 367 ms: 1.02x faster                                                      |
| async_tree_eager                 | 65.8 ms                                                | 69.2 ms: 1.05x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 407 ms: 1.17x slower                                                      |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 189 ms: 1.34x slower                                                      |
| async_tree_eager_tg              | 46.9 ms                                                | 144 ms: 3.07x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 53.2 ms: 1.02x faster                                                     |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                      |
| nbody          | 67.6 ms                                                | 80.7 ms: 1.20x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.30 ms: 1.06x faster                                                     |
| regex_compile  | 75.9 ms                                                | 74.4 ms: 1.02x faster                                                     |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                      |
| regex_v8       | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 75.5 ms                                                | 73.7 ms: 1.03x faster                                                     |
| tomli_loads          | 1.36 sec                                               | 1.39 sec: 1.03x slower                                                    |
| xml_etree_generate   | 55.4 ms                                                | 57.4 ms: 1.04x slower                                                     |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                                     |
| xml_etree_process    | 38.9 ms                                                | 41.8 ms: 1.07x slower                                                     |
| pickle_pure_python   | 197 us                                                 | 225 us: 1.14x slower                                                      |
| unpickle_pure_python | 145 us                                                 | 167 us: 1.15x slower                                                      |
| json_dumps           | 6.19 ms                                                | 7.49 ms: 1.21x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 12.3 ms: 1.07x faster                                                     |
| python_startup         | 17.8 ms                                                | 17.1 ms: 1.04x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 32.2 ms: 1.06x slower                                                     |
| genshi_text     | 14.7 ms                                                | 15.5 ms: 1.06x slower                                                     |
| mako            | 7.44 ms                                                | 7.97 ms: 1.07x slower                                                     |
| django_template | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.09x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.8 ms: 2.52x faster                                                     |
| async_tree_io_tg                 | 673 ms                                                 | 388 ms: 1.73x faster                                                      |
| async_tree_eager_io              | 666 ms                                                 | 389 ms: 1.71x faster                                                      |
| async_tree_io                    | 672 ms                                                 | 408 ms: 1.65x faster                                                      |
| async_tree_eager_io_tg           | 617 ms                                                 | 400 ms: 1.54x faster                                                      |
| async_tree_none_tg               | 255 ms                                                 | 166 ms: 1.53x faster                                                      |
| async_tree_memoization_tg        | 318 ms                                                 | 208 ms: 1.53x faster                                                      |
| async_tree_none                  | 263 ms                                                 | 177 ms: 1.49x faster                                                      |
| async_tree_memoization           | 310 ms                                                 | 211 ms: 1.47x faster                                                      |
| deepcopy                         | 226 us                                                 | 165 us: 1.37x faster                                                      |
| deepcopy_memo                    | 26.0 us                                                | 20.6 us: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 426 ms: 1.24x faster                                                      |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 429 ms: 1.23x faster                                                      |
| generators                       | 29.4 ms                                                | 25.0 ms: 1.17x faster                                                     |
| deepcopy_reduce                  | 2.01 us                                                | 1.72 us: 1.17x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                      |
| async_generators                 | 299 ms                                                 | 270 ms: 1.11x faster                                                      |
| coroutines                       | 19.7 ms                                                | 17.9 ms: 1.10x faster                                                     |
| bench_mp_pool                    | 65.5 ms                                                | 59.9 ms: 1.09x faster                                                     |
| k_core                           | 1.72 sec                                               | 1.59 sec: 1.08x faster                                                    |
| comprehensions                   | 14.0 us                                                | 13.0 us: 1.08x faster                                                     |
| python_startup_no_site           | 13.2 ms                                                | 12.3 ms: 1.07x faster                                                     |
| pylint                           | 182 ms                                                 | 170 ms: 1.07x faster                                                      |
| regex_effbot                     | 2.44 ms                                                | 2.30 ms: 1.06x faster                                                     |
| go                               | 98.5 ms                                                | 92.9 ms: 1.06x faster                                                     |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.05x faster                                                      |
| raytrace                         | 204 ms                                                 | 194 ms: 1.05x faster                                                      |
| pathlib                          | 24.7 ms                                                | 23.5 ms: 1.05x faster                                                     |
| python_startup                   | 17.8 ms                                                | 17.1 ms: 1.04x faster                                                     |
| html5lib                         | 33.4 ms                                                | 32.2 ms: 1.04x faster                                                     |
| logging_silent                   | 72.5 ns                                                | 70.6 ns: 1.03x faster                                                     |
| xml_etree_iterparse              | 75.5 ms                                                | 73.7 ms: 1.03x faster                                                     |
| regex_compile                    | 75.9 ms                                                | 74.4 ms: 1.02x faster                                                     |
| thrift                           | 468 us                                                 | 459 us: 1.02x faster                                                      |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.09 ms: 1.02x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 367 ms: 1.02x faster                                                      |
| float                            | 54.1 ms                                                | 53.2 ms: 1.02x faster                                                     |
| sphinx                           | 613 ms                                                 | 605 ms: 1.01x faster                                                      |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                      |
| dulwich_log                      | 29.2 ms                                                | 29.0 ms: 1.01x faster                                                     |
| dask                             | 779 ms                                                 | 772 ms: 1.01x faster                                                      |
| logging_simple                   | 3.60 us                                                | 3.59 us: 1.01x faster                                                     |
| scimark_fft                      | 194 ms                                                 | 195 ms: 1.00x slower                                                      |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.00x slower                                                     |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                      |
| bpe_tokeniser                    | 3.28 sec                                               | 3.32 sec: 1.01x slower                                                    |
| mdp                              | 1.49 sec                                               | 1.52 sec: 1.02x slower                                                    |
| sympy_sum                        | 76.2 ms                                                | 78.1 ms: 1.02x slower                                                     |
| json                             | 3.00 ms                                                | 3.08 ms: 1.03x slower                                                     |
| docutils                         | 1.45 sec                                               | 1.49 sec: 1.03x slower                                                    |
| tomli_loads                      | 1.36 sec                                               | 1.39 sec: 1.03x slower                                                    |
| pprint_pformat                   | 986 ms                                                 | 1.02 sec: 1.03x slower                                                    |
| xml_etree_generate               | 55.4 ms                                                | 57.4 ms: 1.04x slower                                                     |
| scimark_sor                      | 85.8 ms                                                | 89.0 ms: 1.04x slower                                                     |
| pycparser                        | 673 ms                                                 | 701 ms: 1.04x slower                                                      |
| deltablue                        | 2.57 ms                                                | 2.67 ms: 1.04x slower                                                     |
| sympy_str                        | 144 ms                                                 | 150 ms: 1.04x slower                                                      |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                                     |
| shortest_path                    | 331 ms                                                 | 346 ms: 1.05x slower                                                      |
| pprint_safe_repr                 | 483 ms                                                 | 506 ms: 1.05x slower                                                      |
| sqlglot_optimize                 | 33.2 ms                                                | 34.8 ms: 1.05x slower                                                     |
| spectral_norm                    | 76.5 ms                                                | 80.2 ms: 1.05x slower                                                     |
| async_tree_eager                 | 65.8 ms                                                | 69.2 ms: 1.05x slower                                                     |
| bench_thread_pool                | 483 us                                                 | 507 us: 1.05x slower                                                      |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.94 ms: 1.05x slower                                                     |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.05x slower                                                     |
| sqlglot_normalize                | 180 ms                                                 | 190 ms: 1.06x slower                                                      |
| genshi_xml                       | 30.5 ms                                                | 32.2 ms: 1.06x slower                                                     |
| connected_components             | 300 ms                                                 | 317 ms: 1.06x slower                                                      |
| genshi_text                      | 14.7 ms                                                | 15.5 ms: 1.06x slower                                                     |
| scimark_monte_carlo              | 44.5 ms                                                | 47.2 ms: 1.06x slower                                                     |
| chaos                            | 41.6 ms                                                | 44.2 ms: 1.06x slower                                                     |
| sqlglot_parse                    | 808 us                                                 | 864 us: 1.07x slower                                                      |
| sympy_expand                     | 233 ms                                                 | 250 ms: 1.07x slower                                                      |
| sqlglot_transpile                | 973 us                                                 | 1.04 ms: 1.07x slower                                                     |
| mako                             | 7.44 ms                                                | 7.97 ms: 1.07x slower                                                     |
| xml_etree_process                | 38.9 ms                                                | 41.8 ms: 1.07x slower                                                     |
| sympy_integrate                  | 11.1 ms                                                | 12.1 ms: 1.09x slower                                                     |
| typing_runtime_protocols         | 91.5 us                                                | 101 us: 1.10x slower                                                      |
| scimark_lu                       | 73.5 ms                                                | 81.1 ms: 1.10x slower                                                     |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.12x slower                                                     |
| meteor_contest                   | 69.1 ms                                                | 77.5 ms: 1.12x slower                                                     |
| regex_v8                         | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                     |
| hexiom                           | 4.38 ms                                                | 4.97 ms: 1.14x slower                                                     |
| pyflate                          | 311 ms                                                 | 354 ms: 1.14x slower                                                      |
| pickle_pure_python               | 197 us                                                 | 225 us: 1.14x slower                                                      |
| unpickle_pure_python             | 145 us                                                 | 167 us: 1.15x slower                                                      |
| many_optionals                   | 403 us                                                 | 468 us: 1.16x slower                                                      |
| django_template                  | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 407 ms: 1.17x slower                                                      |
| nqueens                          | 59.5 ms                                                | 70.1 ms: 1.18x slower                                                     |
| 2to3                             | 168 ms                                                 | 200 ms: 1.19x slower                                                      |
| nbody                            | 67.6 ms                                                | 80.7 ms: 1.20x slower                                                     |
| crypto_pyaes                     | 51.4 ms                                                | 61.7 ms: 1.20x slower                                                     |
| telco                            | 3.92 ms                                                | 4.72 ms: 1.20x slower                                                     |
| json_dumps                       | 6.19 ms                                                | 7.49 ms: 1.21x slower                                                     |
| fannkuch                         | 250 ms                                                 | 306 ms: 1.22x slower                                                      |
| coverage                         | 38.5 ms                                                | 47.3 ms: 1.23x slower                                                     |
| richards_super                   | 34.6 ms                                                | 42.5 ms: 1.23x slower                                                     |
| richards                         | 30.6 ms                                                | 37.7 ms: 1.23x slower                                                     |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 189 ms: 1.34x slower                                                      |
| async_tree_eager_tg              | 46.9 ms                                                | 144 ms: 3.07x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (3): sqlalchemy_declarative, asyncio_websockets, logging_format
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 92.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x