# Results vs. 3.12.0

- fork: python
- ref: d7bb7c781771650a4edc
- machine: darwin-arm64
- commit hash: d7bb7c7
- commit date: 2025-03-05
- overall geometric mean: 1.011x slower
- HPT reliability: 98.92%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 175 ms: 1.04x slower                                                   |
| docutils       | 1.45 sec                                               | 1.50 sec: 1.03x slower                                                 |
| sphinx         | 613 ms                                                 | 607 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 393 ms: 1.69x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 397 ms: 1.69x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 402 ms: 1.67x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 404 ms: 1.53x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 212 ms: 1.50x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 171 ms: 1.49x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 178 ms: 1.48x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 222 ms: 1.40x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 428 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 437 ms: 1.21x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.11x faster                                                   |
| async_generators                 | 299 ms                                                 | 269 ms: 1.11x faster                                                   |
| coroutines                       | 19.7 ms                                                | 18.5 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 366 ms: 1.02x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 68.2 ms: 1.04x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 189 ms: 1.34x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 142 ms: 3.02x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                   |
| nbody          | 67.6 ms                                                | 92.5 ms: 1.37x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                  |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| regex_compile  | 75.9 ms                                                | 78.1 ms: 1.03x slower                                                  |
| regex_v8       | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 74.6 ms: 1.01x faster                                                  |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                                  |
| xml_etree_generate   | 55.4 ms                                                | 58.1 ms: 1.05x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.44 sec: 1.06x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 42.8 ms: 1.10x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 170 us: 1.17x slower                                                   |
| pickle_pure_python   | 197 us                                                 | 231 us: 1.17x slower                                                   |
| json_dumps           | 6.19 ms                                                | 7.52 ms: 1.22x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 14.1 ms: 1.07x slower                                                  |
| python_startup         | 17.8 ms                                                | 19.1 ms: 1.07x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 33.6 ms: 1.10x slower                                                  |
| genshi_text     | 14.7 ms                                                | 16.2 ms: 1.11x slower                                                  |
| mako            | 7.44 ms                                                | 8.39 ms: 1.13x slower                                                  |
| django_template | 19.7 ms                                                | 24.3 ms: 1.23x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.0 ms: 2.47x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 393 ms: 1.69x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 397 ms: 1.69x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 402 ms: 1.67x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 404 ms: 1.53x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 212 ms: 1.50x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 171 ms: 1.49x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 178 ms: 1.48x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 222 ms: 1.40x faster                                                   |
| deepcopy                         | 226 us                                                 | 168 us: 1.35x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 20.9 us: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 428 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 437 ms: 1.21x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.76 us: 1.15x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.54 sec: 1.12x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.11x faster                                                   |
| async_generators                 | 299 ms                                                 | 269 ms: 1.11x faster                                                   |
| regex_effbot                     | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                  |
| comprehensions                   | 14.0 us                                                | 13.1 us: 1.07x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 61.3 ms: 1.07x faster                                                  |
| pylint                           | 182 ms                                                 | 171 ms: 1.06x faster                                                   |
| coroutines                       | 19.7 ms                                                | 18.5 ms: 1.06x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.7 ms: 1.04x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| go                               | 98.5 ms                                                | 95.1 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.06 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 366 ms: 1.02x faster                                                   |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 3.24 sec: 1.01x faster                                                 |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                   |
| generators                       | 29.4 ms                                                | 29.0 ms: 1.01x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 74.6 ms: 1.01x faster                                                  |
| thrift                           | 468 us                                                 | 463 us: 1.01x faster                                                   |
| sphinx                           | 613 ms                                                 | 607 ms: 1.01x faster                                                   |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                   |
| scimark_fft                      | 194 ms                                                 | 196 ms: 1.01x slower                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 62.7 ms: 1.01x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 73.6 ns: 1.01x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 77.8 ms: 1.02x slower                                                  |
| dulwich_log                      | 29.2 ms                                                | 30.0 ms: 1.03x slower                                                  |
| shortest_path                    | 331 ms                                                 | 340 ms: 1.03x slower                                                   |
| regex_compile                    | 75.9 ms                                                | 78.1 ms: 1.03x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.50 sec: 1.03x slower                                                 |
| logging_simple                   | 3.60 us                                                | 3.72 us: 1.03x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 68.2 ms: 1.04x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.04 us: 1.04x slower                                                  |
| raytrace                         | 204 ms                                                 | 212 ms: 1.04x slower                                                   |
| 2to3                             | 168 ms                                                 | 175 ms: 1.04x slower                                                   |
| mdp                              | 1.49 sec                                               | 1.55 sec: 1.04x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                                  |
| pycparser                        | 673 ms                                                 | 704 ms: 1.04x slower                                                   |
| xml_etree_generate               | 55.4 ms                                                | 58.1 ms: 1.05x slower                                                  |
| connected_components             | 300 ms                                                 | 315 ms: 1.05x slower                                                   |
| sympy_sum                        | 76.2 ms                                                | 80.1 ms: 1.05x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.10 ms: 1.05x slower                                                  |
| chaos                            | 41.6 ms                                                | 44.1 ms: 1.06x slower                                                  |
| sympy_str                        | 144 ms                                                 | 152 ms: 1.06x slower                                                   |
| tomli_loads                      | 1.36 sec                                               | 1.44 sec: 1.06x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 14.1 ms: 1.07x slower                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.07 ms: 1.07x slower                                                  |
| python_startup                   | 17.8 ms                                                | 19.1 ms: 1.07x slower                                                  |
| sqlglot_optimize                 | 33.2 ms                                                | 35.7 ms: 1.08x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 92.7 ms: 1.08x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.78 ms: 1.08x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 523 us: 1.08x slower                                                   |
| sqlglot_normalize                | 180 ms                                                 | 196 ms: 1.09x slower                                                   |
| nqueens                          | 59.5 ms                                                | 65.0 ms: 1.09x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 255 ms: 1.09x slower                                                   |
| sqlglot_parse                    | 808 us                                                 | 888 us: 1.10x slower                                                   |
| xml_etree_process                | 38.9 ms                                                | 42.8 ms: 1.10x slower                                                  |
| sqlglot_transpile                | 973 us                                                 | 1.07 ms: 1.10x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 33.6 ms: 1.10x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.11x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 16.2 ms: 1.11x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 101 us: 1.11x slower                                                   |
| sympy_integrate                  | 11.1 ms                                                | 12.3 ms: 1.11x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 49.8 ms: 1.12x slower                                                  |
| mako                             | 7.44 ms                                                | 8.39 ms: 1.13x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.11 sec: 1.13x slower                                                 |
| pyflate                          | 311 ms                                                 | 351 ms: 1.13x slower                                                   |
| pprint_safe_repr                 | 483 ms                                                 | 546 ms: 1.13x slower                                                   |
| scimark_lu                       | 73.5 ms                                                | 83.2 ms: 1.13x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 78.3 ms: 1.13x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 59.0 ms: 1.15x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                   |
| many_optionals                   | 403 us                                                 | 468 us: 1.16x slower                                                   |
| unpickle_pure_python             | 145 us                                                 | 170 us: 1.17x slower                                                   |
| fannkuch                         | 250 ms                                                 | 292 ms: 1.17x slower                                                   |
| pickle_pure_python               | 197 us                                                 | 231 us: 1.17x slower                                                   |
| hexiom                           | 4.38 ms                                                | 5.26 ms: 1.20x slower                                                  |
| telco                            | 3.92 ms                                                | 4.76 ms: 1.21x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.52 ms: 1.22x slower                                                  |
| coverage                         | 38.5 ms                                                | 47.2 ms: 1.23x slower                                                  |
| django_template                  | 19.7 ms                                                | 24.3 ms: 1.23x slower                                                  |
| richards_super                   | 34.6 ms                                                | 42.8 ms: 1.24x slower                                                  |
| richards                         | 30.6 ms                                                | 39.9 ms: 1.30x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 189 ms: 1.34x slower                                                   |
| nbody                            | 67.6 ms                                                | 92.5 ms: 1.37x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 142 ms: 3.02x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (5): html5lib, asyncio_websockets, sqlite_synth, float, json
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 98.92% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x