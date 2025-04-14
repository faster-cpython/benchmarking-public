# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_20250304
- machine: darwin-arm64
- commit hash: 7c58692
- commit date: 2025-03-04
- overall geometric mean: 1.016x slower
- HPT reliability: 99.56%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 178 ms: 1.06x slower                                               |
| docutils       | 1.45 sec                                               | 1.51 sec: 1.04x slower                                             |
| html5lib       | 33.4 ms                                                | 34.9 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                  | 1.03x slower                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 395 ms: 1.69x faster                                               |
| async_tree_io_tg                 | 673 ms                                                 | 402 ms: 1.67x faster                                               |
| async_tree_io                    | 672 ms                                                 | 415 ms: 1.62x faster                                               |
| async_tree_eager_io_tg           | 617 ms                                                 | 406 ms: 1.52x faster                                               |
| async_tree_memoization_tg        | 318 ms                                                 | 212 ms: 1.50x faster                                               |
| async_tree_none_tg               | 255 ms                                                 | 173 ms: 1.48x faster                                               |
| async_tree_none                  | 263 ms                                                 | 180 ms: 1.47x faster                                               |
| async_tree_memoization           | 310 ms                                                 | 223 ms: 1.39x faster                                               |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 429 ms: 1.23x faster                                               |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 438 ms: 1.20x faster                                               |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                               |
| async_generators                 | 299 ms                                                 | 271 ms: 1.10x faster                                               |
| coroutines                       | 19.7 ms                                                | 18.7 ms: 1.05x faster                                              |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                               |
| async_tree_eager                 | 65.8 ms                                                | 69.4 ms: 1.05x slower                                              |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                               |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 190 ms: 1.34x slower                                               |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.04x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                               |
| float          | 54.1 ms                                                | 54.6 ms: 1.01x slower                                              |
| nbody          | 67.6 ms                                                | 91.8 ms: 1.36x slower                                              |
| Geometric mean | (ref)                                                  | 1.11x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                              |
| regex_dna      | 143 ms                                                 | 144 ms: 1.01x slower                                               |
| regex_compile  | 75.9 ms                                                | 78.1 ms: 1.03x slower                                              |
| regex_v8       | 15.1 ms                                                | 16.9 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                  | 1.03x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                               |
| xml_etree_iterparse  | 75.5 ms                                                | 74.3 ms: 1.02x faster                                              |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                              |
| xml_etree_generate   | 55.4 ms                                                | 58.3 ms: 1.05x slower                                              |
| tomli_loads          | 1.36 sec                                               | 1.44 sec: 1.06x slower                                             |
| xml_etree_process    | 38.9 ms                                                | 42.9 ms: 1.10x slower                                              |
| unpickle_pure_python | 145 us                                                 | 170 us: 1.17x slower                                               |
| pickle_pure_python   | 197 us                                                 | 230 us: 1.17x slower                                               |
| json_dumps           | 6.19 ms                                                | 7.51 ms: 1.21x slower                                              |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 14.0 ms: 1.07x slower                                              |
| python_startup         | 17.8 ms                                                | 18.9 ms: 1.07x slower                                              |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 33.8 ms: 1.11x slower                                              |
| genshi_text     | 14.7 ms                                                | 16.2 ms: 1.11x slower                                              |
| mako            | 7.44 ms                                                | 8.44 ms: 1.13x slower                                              |
| django_template | 19.7 ms                                                | 24.2 ms: 1.23x slower                                              |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                       |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-darwin-arm64-mdboom-aa_test_20250304-3.14.0a5+-7c58692 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.9 ms: 2.49x faster                                              |
| async_tree_eager_io              | 666 ms                                                 | 395 ms: 1.69x faster                                               |
| async_tree_io_tg                 | 673 ms                                                 | 402 ms: 1.67x faster                                               |
| async_tree_io                    | 672 ms                                                 | 415 ms: 1.62x faster                                               |
| async_tree_eager_io_tg           | 617 ms                                                 | 406 ms: 1.52x faster                                               |
| async_tree_memoization_tg        | 318 ms                                                 | 212 ms: 1.50x faster                                               |
| async_tree_none_tg               | 255 ms                                                 | 173 ms: 1.48x faster                                               |
| async_tree_none                  | 263 ms                                                 | 180 ms: 1.47x faster                                               |
| async_tree_memoization           | 310 ms                                                 | 223 ms: 1.39x faster                                               |
| deepcopy                         | 226 us                                                 | 170 us: 1.33x faster                                               |
| deepcopy_memo                    | 26.0 us                                                | 21.0 us: 1.24x faster                                              |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 429 ms: 1.23x faster                                               |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 438 ms: 1.20x faster                                               |
| deepcopy_reduce                  | 2.01 us                                                | 1.77 us: 1.14x faster                                              |
| k_core                           | 1.72 sec                                               | 1.53 sec: 1.12x faster                                             |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                               |
| async_generators                 | 299 ms                                                 | 271 ms: 1.10x faster                                               |
| comprehensions                   | 14.0 us                                                | 13.1 us: 1.07x faster                                              |
| bench_mp_pool                    | 65.5 ms                                                | 61.2 ms: 1.07x faster                                              |
| pylint                           | 182 ms                                                 | 171 ms: 1.06x faster                                               |
| coroutines                       | 19.7 ms                                                | 18.7 ms: 1.05x faster                                              |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                              |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                               |
| go                               | 98.5 ms                                                | 95.1 ms: 1.04x faster                                              |
| pathlib                          | 24.7 ms                                                | 23.9 ms: 1.03x faster                                              |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.08 ms: 1.02x faster                                              |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                               |
| xml_etree_iterparse              | 75.5 ms                                                | 74.3 ms: 1.02x faster                                              |
| bpe_tokeniser                    | 3.28 sec                                               | 3.24 sec: 1.01x faster                                             |
| generators                       | 29.4 ms                                                | 29.0 ms: 1.01x faster                                              |
| dask                             | 779 ms                                                 | 770 ms: 1.01x faster                                               |
| thrift                           | 468 us                                                 | 463 us: 1.01x faster                                               |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.01x faster                                              |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                               |
| float                            | 54.1 ms                                                | 54.6 ms: 1.01x slower                                              |
| regex_dna                        | 143 ms                                                 | 144 ms: 1.01x slower                                               |
| json                             | 3.00 ms                                                | 3.04 ms: 1.01x slower                                              |
| sqlalchemy_declarative           | 61.9 ms                                                | 62.8 ms: 1.01x slower                                              |
| logging_silent                   | 72.5 ns                                                | 73.6 ns: 1.01x slower                                              |
| scimark_fft                      | 194 ms                                                 | 197 ms: 1.01x slower                                               |
| spectral_norm                    | 76.5 ms                                                | 78.5 ms: 1.03x slower                                              |
| dulwich_log                      | 29.2 ms                                                | 30.0 ms: 1.03x slower                                              |
| regex_compile                    | 75.9 ms                                                | 78.1 ms: 1.03x slower                                              |
| docutils                         | 1.45 sec                                               | 1.51 sec: 1.04x slower                                             |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                              |
| raytrace                         | 204 ms                                                 | 212 ms: 1.04x slower                                               |
| sympy_sum                        | 76.2 ms                                                | 79.5 ms: 1.04x slower                                              |
| logging_simple                   | 3.60 us                                                | 3.76 us: 1.04x slower                                              |
| logging_format                   | 3.90 us                                                | 4.07 us: 1.04x slower                                              |
| shortest_path                    | 331 ms                                                 | 345 ms: 1.04x slower                                               |
| html5lib                         | 33.4 ms                                                | 34.9 ms: 1.05x slower                                              |
| gc_traversal                     | 2.95 ms                                                | 3.08 ms: 1.05x slower                                              |
| pycparser                        | 673 ms                                                 | 707 ms: 1.05x slower                                               |
| xml_etree_generate               | 55.4 ms                                                | 58.3 ms: 1.05x slower                                              |
| async_tree_eager                 | 65.8 ms                                                | 69.4 ms: 1.05x slower                                              |
| 2to3                             | 168 ms                                                 | 178 ms: 1.06x slower                                               |
| connected_components             | 300 ms                                                 | 317 ms: 1.06x slower                                               |
| chaos                            | 41.6 ms                                                | 44.1 ms: 1.06x slower                                              |
| tomli_loads                      | 1.36 sec                                               | 1.44 sec: 1.06x slower                                             |
| sympy_str                        | 144 ms                                                 | 153 ms: 1.06x slower                                               |
| python_startup_no_site           | 13.2 ms                                                | 14.0 ms: 1.07x slower                                              |
| python_startup                   | 17.8 ms                                                | 18.9 ms: 1.07x slower                                              |
| sqlglot_optimize                 | 33.2 ms                                                | 35.6 ms: 1.07x slower                                              |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.10 ms: 1.08x slower                                              |
| deltablue                        | 2.57 ms                                                | 2.76 ms: 1.08x slower                                              |
| scimark_sor                      | 85.8 ms                                                | 93.0 ms: 1.08x slower                                              |
| bench_thread_pool                | 483 us                                                 | 523 us: 1.08x slower                                               |
| sqlglot_normalize                | 180 ms                                                 | 196 ms: 1.09x slower                                               |
| nqueens                          | 59.5 ms                                                | 65.0 ms: 1.09x slower                                              |
| sympy_expand                     | 233 ms                                                 | 255 ms: 1.09x slower                                               |
| sqlglot_parse                    | 808 us                                                 | 890 us: 1.10x slower                                               |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.10x slower                                              |
| xml_etree_process                | 38.9 ms                                                | 42.9 ms: 1.10x slower                                              |
| sqlglot_transpile                | 973 us                                                 | 1.08 ms: 1.11x slower                                              |
| sympy_integrate                  | 11.1 ms                                                | 12.3 ms: 1.11x slower                                              |
| genshi_xml                       | 30.5 ms                                                | 33.8 ms: 1.11x slower                                              |
| genshi_text                      | 14.7 ms                                                | 16.2 ms: 1.11x slower                                              |
| typing_runtime_protocols         | 91.5 us                                                | 102 us: 1.11x slower                                               |
| regex_v8                         | 15.1 ms                                                | 16.9 ms: 1.12x slower                                              |
| scimark_monte_carlo              | 44.5 ms                                                | 49.8 ms: 1.12x slower                                              |
| pprint_pformat                   | 986 ms                                                 | 1.11 sec: 1.12x slower                                             |
| pprint_safe_repr                 | 483 ms                                                 | 545 ms: 1.13x slower                                               |
| pyflate                          | 311 ms                                                 | 352 ms: 1.13x slower                                               |
| scimark_lu                       | 73.5 ms                                                | 83.3 ms: 1.13x slower                                              |
| mako                             | 7.44 ms                                                | 8.44 ms: 1.13x slower                                              |
| meteor_contest                   | 69.1 ms                                                | 78.5 ms: 1.14x slower                                              |
| mdp                              | 1.49 sec                                               | 1.71 sec: 1.15x slower                                             |
| crypto_pyaes                     | 51.4 ms                                                | 59.2 ms: 1.15x slower                                              |
| many_optionals                   | 403 us                                                 | 468 us: 1.16x slower                                               |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                               |
| unpickle_pure_python             | 145 us                                                 | 170 us: 1.17x slower                                               |
| pickle_pure_python               | 197 us                                                 | 230 us: 1.17x slower                                               |
| fannkuch                         | 250 ms                                                 | 293 ms: 1.17x slower                                               |
| hexiom                           | 4.38 ms                                                | 5.28 ms: 1.21x slower                                              |
| telco                            | 3.92 ms                                                | 4.76 ms: 1.21x slower                                              |
| json_dumps                       | 6.19 ms                                                | 7.51 ms: 1.21x slower                                              |
| django_template                  | 19.7 ms                                                | 24.2 ms: 1.23x slower                                              |
| richards_super                   | 34.6 ms                                                | 42.9 ms: 1.24x slower                                              |
| coverage                         | 38.5 ms                                                | 47.9 ms: 1.24x slower                                              |
| richards                         | 30.6 ms                                                | 39.9 ms: 1.31x slower                                              |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 190 ms: 1.34x slower                                               |
| nbody                            | 67.6 ms                                                | 91.8 ms: 1.36x slower                                              |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.04x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (2): asyncio_websockets, sphinx
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.016x slower

# HPT report

- Reliability score: 99.56% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x