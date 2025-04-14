# Results vs. 3.12.0

- fork: python
- ref: v3.13.2
- machine: darwin-arm64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.014x slower
- HPT reliability: 97.30%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 180 ms: 1.07x slower                                   |
| chameleon      | 4.55 ms                                                | 4.95 ms: 1.09x slower                                  |
| docutils       | 1.45 sec                                               | 1.44 sec: 1.01x faster                                 |
| html5lib       | 33.4 ms                                                | 36.2 ms: 1.09x slower                                  |
| sphinx         | 613 ms                                                 | 599 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io                    | 672 ms                                                 | 511 ms: 1.31x faster                                   |
| async_tree_none_tg               | 255 ms                                                 | 196 ms: 1.30x faster                                   |
| async_tree_io_tg                 | 673 ms                                                 | 516 ms: 1.30x faster                                   |
| async_tree_eager_io              | 666 ms                                                 | 515 ms: 1.29x faster                                   |
| async_tree_none                  | 263 ms                                                 | 213 ms: 1.23x faster                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 510 ms: 1.21x faster                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 278 ms: 1.14x faster                                   |
| async_tree_memoization           | 310 ms                                                 | 272 ms: 1.14x faster                                   |
| async_generators                 | 299 ms                                                 | 262 ms: 1.14x faster                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 462 ms: 1.14x faster                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 479 ms: 1.10x faster                                   |
| coroutines                       | 19.7 ms                                                | 19.8 ms: 1.00x slower                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 170 ms: 1.01x slower                                   |
| async_tree_eager                 | 65.8 ms                                                | 70.6 ms: 1.07x slower                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 425 ms: 1.22x slower                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 211 ms: 1.49x slower                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 159 ms: 3.38x slower                                   |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                   |
| float          | 54.1 ms                                                | 55.9 ms: 1.03x slower                                  |
| nbody          | 67.6 ms                                                | 74.4 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.28 ms: 1.07x faster                                  |
| regex_dna      | 143 ms                                                 | 141 ms: 1.02x faster                                   |
| regex_compile  | 75.9 ms                                                | 78.9 ms: 1.04x slower                                  |
| regex_v8       | 15.1 ms                                                | 17.0 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 74.1 ms: 1.02x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.01x faster                                   |
| xml_etree_generate   | 55.4 ms                                                | 56.8 ms: 1.02x slower                                  |
| json_dumps           | 6.19 ms                                                | 6.50 ms: 1.05x slower                                  |
| xml_etree_process    | 38.9 ms                                                | 41.5 ms: 1.07x slower                                  |
| pickle_pure_python   | 197 us                                                 | 216 us: 1.10x slower                                   |
| unpickle_pure_python | 145 us                                                 | 164 us: 1.13x slower                                   |
| tomli_loads          | 1.36 sec                                               | 1.57 sec: 1.16x slower                                 |
| Geometric mean       | (ref)                                                  | 1.05x slower                                           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.4 ms: 1.02x slower                                  |
| python_startup         | 17.8 ms                                                | 18.4 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 7.44 ms                                                | 7.72 ms: 1.04x slower                                  |
| django_template | 19.7 ms                                                | 20.6 ms: 1.05x slower                                  |
| genshi_xml      | 30.5 ms                                                | 34.1 ms: 1.12x slower                                  |
| genshi_text     | 14.7 ms                                                | 16.9 ms: 1.15x slower                                  |
| Geometric mean  | (ref)                                                  | 1.09x slower                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 9.48 ms: 3.39x faster                                  |
| gunicorn                         | 1.71 ms                                                | 1.19 ms: 1.43x faster                                  |
| djangocms                        | 9.55 us                                                | 6.87 us: 1.39x faster                                  |
| async_tree_io                    | 672 ms                                                 | 511 ms: 1.31x faster                                   |
| async_tree_none_tg               | 255 ms                                                 | 196 ms: 1.30x faster                                   |
| async_tree_io_tg                 | 673 ms                                                 | 516 ms: 1.30x faster                                   |
| async_tree_eager_io              | 666 ms                                                 | 515 ms: 1.29x faster                                   |
| async_tree_none                  | 263 ms                                                 | 213 ms: 1.23x faster                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 510 ms: 1.21x faster                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 278 ms: 1.14x faster                                   |
| async_tree_memoization           | 310 ms                                                 | 272 ms: 1.14x faster                                   |
| async_generators                 | 299 ms                                                 | 262 ms: 1.14x faster                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 462 ms: 1.14x faster                                   |
| comprehensions                   | 14.0 us                                                | 12.3 us: 1.14x faster                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 479 ms: 1.10x faster                                   |
| raytrace                         | 204 ms                                                 | 185 ms: 1.10x faster                                   |
| regex_effbot                     | 2.44 ms                                                | 2.28 ms: 1.07x faster                                  |
| bench_mp_pool                    | 65.5 ms                                                | 61.5 ms: 1.06x faster                                  |
| k_core                           | 1.72 sec                                               | 1.62 sec: 1.06x faster                                 |
| gevent_hub                       | 0.72 ns                                                | 0.68 ns: 1.06x faster                                  |
| pathlib                          | 24.7 ms                                                | 23.4 ms: 1.06x faster                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 58.9 ms: 1.05x faster                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.02 ms: 1.04x faster                                  |
| logging_silent                   | 72.5 ns                                                | 70.3 ns: 1.03x faster                                  |
| sphinx                           | 613 ms                                                 | 599 ms: 1.02x faster                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 74.1 ms: 1.02x faster                                  |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.02x faster                                   |
| xml_etree_parse                  | 108 ms                                                 | 106 ms: 1.01x faster                                   |
| docutils                         | 1.45 sec                                               | 1.44 sec: 1.01x faster                                 |
| dask                             | 779 ms                                                 | 772 ms: 1.01x faster                                   |
| dulwich_log                      | 29.2 ms                                                | 29.0 ms: 1.01x faster                                  |
| gc_traversal                     | 2.95 ms                                                | 2.93 ms: 1.01x faster                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.26 sec: 1.01x faster                                 |
| thrift                           | 468 us                                                 | 465 us: 1.01x faster                                   |
| sympy_sum                        | 76.2 ms                                                | 75.8 ms: 1.01x faster                                  |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                  |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                   |
| coroutines                       | 19.7 ms                                                | 19.8 ms: 1.00x slower                                  |
| spectral_norm                    | 76.5 ms                                                | 76.8 ms: 1.00x slower                                  |
| logging_simple                   | 3.60 us                                                | 3.62 us: 1.01x slower                                  |
| mdp                              | 1.49 sec                                               | 1.51 sec: 1.01x slower                                 |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.68 ms: 1.01x slower                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 170 ms: 1.01x slower                                   |
| sympy_str                        | 144 ms                                                 | 146 ms: 1.02x slower                                   |
| python_startup_no_site           | 13.2 ms                                                | 13.4 ms: 1.02x slower                                  |
| chaos                            | 41.6 ms                                                | 42.5 ms: 1.02x slower                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.3 ms: 1.02x slower                                  |
| many_optionals                   | 403 us                                                 | 412 us: 1.02x slower                                   |
| xml_etree_generate               | 55.4 ms                                                | 56.8 ms: 1.02x slower                                  |
| deepcopy_reduce                  | 2.01 us                                                | 2.07 us: 1.03x slower                                  |
| float                            | 54.1 ms                                                | 55.9 ms: 1.03x slower                                  |
| nqueens                          | 59.5 ms                                                | 61.5 ms: 1.03x slower                                  |
| python_startup                   | 17.8 ms                                                | 18.4 ms: 1.04x slower                                  |
| mako                             | 7.44 ms                                                | 7.72 ms: 1.04x slower                                  |
| pycparser                        | 673 ms                                                 | 698 ms: 1.04x slower                                   |
| deltablue                        | 2.57 ms                                                | 2.66 ms: 1.04x slower                                  |
| regex_compile                    | 75.9 ms                                                | 78.9 ms: 1.04x slower                                  |
| deepcopy                         | 226 us                                                 | 235 us: 1.04x slower                                   |
| scimark_fft                      | 194 ms                                                 | 202 ms: 1.04x slower                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.20 ms: 1.04x slower                                  |
| bench_thread_pool                | 483 us                                                 | 504 us: 1.04x slower                                   |
| scimark_lu                       | 73.5 ms                                                | 76.7 ms: 1.04x slower                                  |
| django_template                  | 19.7 ms                                                | 20.6 ms: 1.05x slower                                  |
| shortest_path                    | 331 ms                                                 | 347 ms: 1.05x slower                                   |
| json_dumps                       | 6.19 ms                                                | 6.50 ms: 1.05x slower                                  |
| sqlglot_optimize                 | 33.2 ms                                                | 35.0 ms: 1.05x slower                                  |
| sqlglot_parse                    | 808 us                                                 | 851 us: 1.05x slower                                   |
| deepcopy_memo                    | 26.0 us                                                | 27.4 us: 1.05x slower                                  |
| sqlglot_transpile                | 973 us                                                 | 1.03 ms: 1.06x slower                                  |
| crypto_pyaes                     | 51.4 ms                                                | 54.4 ms: 1.06x slower                                  |
| sympy_expand                     | 233 ms                                                 | 247 ms: 1.06x slower                                   |
| sqlglot_normalize                | 180 ms                                                 | 191 ms: 1.06x slower                                   |
| connected_components             | 300 ms                                                 | 319 ms: 1.06x slower                                   |
| xml_etree_process                | 38.9 ms                                                | 41.5 ms: 1.07x slower                                  |
| 2to3                             | 168 ms                                                 | 180 ms: 1.07x slower                                   |
| meteor_contest                   | 69.1 ms                                                | 73.9 ms: 1.07x slower                                  |
| generators                       | 29.4 ms                                                | 31.5 ms: 1.07x slower                                  |
| async_tree_eager                 | 65.8 ms                                                | 70.6 ms: 1.07x slower                                  |
| html5lib                         | 33.4 ms                                                | 36.2 ms: 1.09x slower                                  |
| chameleon                        | 4.55 ms                                                | 4.95 ms: 1.09x slower                                  |
| pickle_pure_python               | 197 us                                                 | 216 us: 1.10x slower                                   |
| pprint_pformat                   | 986 ms                                                 | 1.08 sec: 1.10x slower                                 |
| nbody                            | 67.6 ms                                                | 74.4 ms: 1.10x slower                                  |
| pprint_safe_repr                 | 483 ms                                                 | 535 ms: 1.11x slower                                   |
| typing_runtime_protocols         | 91.5 us                                                | 101 us: 1.11x slower                                   |
| hexiom                           | 4.38 ms                                                | 4.87 ms: 1.11x slower                                  |
| genshi_xml                       | 30.5 ms                                                | 34.1 ms: 1.12x slower                                  |
| fannkuch                         | 250 ms                                                 | 280 ms: 1.12x slower                                   |
| regex_v8                         | 15.1 ms                                                | 17.0 ms: 1.13x slower                                  |
| unpickle_pure_python             | 145 us                                                 | 164 us: 1.13x slower                                   |
| richards_super                   | 34.6 ms                                                | 39.2 ms: 1.13x slower                                  |
| pyflate                          | 311 ms                                                 | 352 ms: 1.13x slower                                   |
| scimark_monte_carlo              | 44.5 ms                                                | 50.8 ms: 1.14x slower                                  |
| genshi_text                      | 14.7 ms                                                | 16.9 ms: 1.15x slower                                  |
| tomli_loads                      | 1.36 sec                                               | 1.57 sec: 1.16x slower                                 |
| richards                         | 30.6 ms                                                | 35.3 ms: 1.16x slower                                  |
| go                               | 98.5 ms                                                | 115 ms: 1.17x slower                                   |
| coverage                         | 38.5 ms                                                | 46.2 ms: 1.20x slower                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 425 ms: 1.22x slower                                   |
| telco                            | 3.92 ms                                                | 4.81 ms: 1.23x slower                                  |
| scimark_sor                      | 85.8 ms                                                | 106 ms: 1.24x slower                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 211 ms: 1.49x slower                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 159 ms: 3.38x slower                                   |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (7): tornado_http, pylint, json, asyncio_websockets, json_loads, async_tree_eager_cpu_io_mixed, logging_format

- Geometric mean (including insignificant results): 1.014x slower

# HPT report

- Reliability score: 97.30% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x