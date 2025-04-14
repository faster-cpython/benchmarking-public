# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: darwin-arm64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.018x faster
- HPT reliability: 77.67%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 203 ms: 1.20x slower                                                   |
| docutils       | 1.45 sec                                               | 1.48 sec: 1.01x slower                                                 |
| html5lib       | 33.4 ms                                                | 32.6 ms: 1.02x faster                                                  |
| sphinx         | 613 ms                                                 | 596 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 383 ms: 1.76x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 392 ms: 1.70x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 397 ms: 1.69x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 391 ms: 1.58x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 204 ms: 1.56x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 164 ms: 1.56x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 171 ms: 1.54x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 205 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 419 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 143 ms: 1.17x faster                                                   |
| coroutines                       | 19.7 ms                                                | 17.3 ms: 1.14x faster                                                  |
| async_generators                 | 299 ms                                                 | 264 ms: 1.13x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 395 ms: 1.14x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 180 ms: 1.27x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 135 ms: 2.89x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (2): async_tree_eager, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 52.7 ms: 1.03x faster                                                  |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| nbody          | 67.6 ms                                                | 81.1 ms: 1.20x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                  |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| regex_compile  | 75.9 ms                                                | 74.9 ms: 1.01x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.7 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 73.5 ms: 1.03x faster                                                  |
| xml_etree_generate   | 55.4 ms                                                | 56.2 ms: 1.01x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.40 sec: 1.03x slower                                                 |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| xml_etree_process    | 38.9 ms                                                | 40.9 ms: 1.05x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 221 us: 1.12x slower                                                   |
| unpickle_pure_python | 145 us                                                 | 165 us: 1.13x slower                                                   |
| json_dumps           | 6.19 ms                                                | 7.48 ms: 1.21x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 17.9 ms: 1.01x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 7.83 ms: 1.05x slower                                                  |
| genshi_xml      | 30.5 ms                                                | 32.2 ms: 1.06x slower                                                  |
| genshi_text     | 14.7 ms                                                | 15.6 ms: 1.06x slower                                                  |
| django_template | 19.7 ms                                                | 22.8 ms: 1.16x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.7 ms: 2.53x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 383 ms: 1.76x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 392 ms: 1.70x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 397 ms: 1.69x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 391 ms: 1.58x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 204 ms: 1.56x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 164 ms: 1.56x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 171 ms: 1.54x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 205 ms: 1.51x faster                                                   |
| deepcopy                         | 226 us                                                 | 162 us: 1.39x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 20.4 us: 1.27x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 419 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                                   |
| generators                       | 29.4 ms                                                | 25.1 ms: 1.17x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 143 ms: 1.17x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.73 us: 1.17x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 25.6 ms: 1.14x faster                                                  |
| coroutines                       | 19.7 ms                                                | 17.3 ms: 1.14x faster                                                  |
| async_generators                 | 299 ms                                                 | 264 ms: 1.13x faster                                                   |
| regex_effbot                     | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                  |
| pylint                           | 182 ms                                                 | 167 ms: 1.09x faster                                                   |
| comprehensions                   | 14.0 us                                                | 12.9 us: 1.09x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.60 sec: 1.08x faster                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 60.7 ms: 1.08x faster                                                  |
| go                               | 98.5 ms                                                | 92.7 ms: 1.06x faster                                                  |
| raytrace                         | 204 ms                                                 | 192 ms: 1.06x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                   |
| logging_silent                   | 72.5 ns                                                | 70.4 ns: 1.03x faster                                                  |
| sphinx                           | 613 ms                                                 | 596 ms: 1.03x faster                                                   |
| thrift                           | 468 us                                                 | 455 us: 1.03x faster                                                   |
| float                            | 54.1 ms                                                | 52.7 ms: 1.03x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 73.5 ms: 1.03x faster                                                  |
| pathlib                          | 24.7 ms                                                | 24.1 ms: 1.02x faster                                                  |
| html5lib                         | 33.4 ms                                                | 32.6 ms: 1.02x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.10 ms: 1.01x faster                                                  |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| regex_compile                    | 75.9 ms                                                | 74.9 ms: 1.01x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 61.1 ms: 1.01x faster                                                  |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.59 us: 1.00x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 194 ms: 1.00x faster                                                   |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 3.30 sec: 1.01x slower                                                 |
| python_startup                   | 17.8 ms                                                | 17.9 ms: 1.01x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 77.3 ms: 1.01x slower                                                  |
| xml_etree_generate               | 55.4 ms                                                | 56.2 ms: 1.01x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.48 sec: 1.01x slower                                                 |
| mdp                              | 1.49 sec                                               | 1.52 sec: 1.02x slower                                                 |
| scimark_sor                      | 85.8 ms                                                | 87.8 ms: 1.02x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.63 ms: 1.03x slower                                                  |
| sympy_str                        | 144 ms                                                 | 148 ms: 1.03x slower                                                   |
| tomli_loads                      | 1.36 sec                                               | 1.40 sec: 1.03x slower                                                 |
| pycparser                        | 673 ms                                                 | 696 ms: 1.03x slower                                                   |
| shortest_path                    | 331 ms                                                 | 342 ms: 1.04x slower                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.84 ms: 1.04x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.02 sec: 1.04x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 79.5 ms: 1.04x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 15.7 ms: 1.04x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 506 ms: 1.05x slower                                                   |
| json                             | 3.00 ms                                                | 3.14 ms: 1.05x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 506 us: 1.05x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                  |
| mako                             | 7.44 ms                                                | 7.83 ms: 1.05x slower                                                  |
| chaos                            | 41.6 ms                                                | 43.8 ms: 1.05x slower                                                  |
| connected_components             | 300 ms                                                 | 316 ms: 1.05x slower                                                   |
| xml_etree_process                | 38.9 ms                                                | 40.9 ms: 1.05x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 47.0 ms: 1.06x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 32.2 ms: 1.06x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.12 ms: 1.06x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 248 ms: 1.06x slower                                                   |
| genshi_text                      | 14.7 ms                                                | 15.6 ms: 1.06x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 78.9 ms: 1.07x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 100.0 us: 1.09x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 76.9 ms: 1.11x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 221 us: 1.12x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.12x slower                                                  |
| pyflate                          | 311 ms                                                 | 350 ms: 1.13x slower                                                   |
| unpickle_pure_python             | 145 us                                                 | 165 us: 1.13x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 395 ms: 1.14x slower                                                   |
| hexiom                           | 4.38 ms                                                | 5.01 ms: 1.14x slower                                                  |
| django_template                  | 19.7 ms                                                | 22.8 ms: 1.16x slower                                                  |
| nqueens                          | 59.5 ms                                                | 69.2 ms: 1.16x slower                                                  |
| many_optionals                   | 403 us                                                 | 471 us: 1.17x slower                                                   |
| crypto_pyaes                     | 51.4 ms                                                | 60.6 ms: 1.18x slower                                                  |
| telco                            | 3.92 ms                                                | 4.63 ms: 1.18x slower                                                  |
| coverage                         | 38.5 ms                                                | 45.9 ms: 1.19x slower                                                  |
| nbody                            | 67.6 ms                                                | 81.1 ms: 1.20x slower                                                  |
| richards_super                   | 34.6 ms                                                | 41.6 ms: 1.20x slower                                                  |
| 2to3                             | 168 ms                                                 | 203 ms: 1.20x slower                                                   |
| json_dumps                       | 6.19 ms                                                | 7.48 ms: 1.21x slower                                                  |
| fannkuch                         | 250 ms                                                 | 303 ms: 1.21x slower                                                   |
| richards                         | 30.6 ms                                                | 37.4 ms: 1.22x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 180 ms: 1.27x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 135 ms: 2.89x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (3): async_tree_eager, asyncio_websockets, logging_format
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.018x faster

# HPT report

- Reliability score: 77.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x