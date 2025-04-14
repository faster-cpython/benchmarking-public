# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: darwin-arm64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.044x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 195 ms: 1.16x slower                                                   |
| docutils       | 1.45 sec                                               | 1.47 sec: 1.01x slower                                                 |
| html5lib       | 33.4 ms                                                | 36.2 ms: 1.08x slower                                                  |
| sphinx         | 613 ms                                                 | 635 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 331 ms: 2.03x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 343 ms: 1.95x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 317 ms: 1.94x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 358 ms: 1.88x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 184 ms: 1.73x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 149 ms: 1.72x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 172 ms: 1.53x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 207 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 388 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 413 ms: 1.28x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| async_generators                 | 299 ms                                                 | 276 ms: 1.08x faster                                                   |
| coroutines                       | 19.7 ms                                                | 18.7 ms: 1.05x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 369 ms: 1.01x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 372 ms: 1.07x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 167 ms: 1.18x slower                                                   |
| async_tree_eager                 | 65.8 ms                                                | 83.9 ms: 1.27x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 127 ms: 2.70x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 281 ms: 1.01x faster                                                   |
| float          | 54.1 ms                                                | 54.8 ms: 1.01x slower                                                  |
| nbody          | 67.6 ms                                                | 105 ms: 1.55x slower                                                   |
| Geometric mean | (ref)                                                  | 1.16x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.08 ms: 1.17x faster                                                  |
| regex_dna      | 143 ms                                                 | 137 ms: 1.04x faster                                                   |
| regex_v8       | 15.1 ms                                                | 14.9 ms: 1.01x faster                                                  |
| regex_compile  | 75.9 ms                                                | 86.4 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 66.4 ms: 1.14x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 60.5 ms: 1.09x slower                                                  |
| json_loads           | 17.0 us                                                | 18.6 us: 1.09x slower                                                  |
| xml_etree_process    | 38.9 ms                                                | 44.9 ms: 1.16x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.60 sec: 1.18x slower                                                 |
| pickle_pure_python   | 197 us                                                 | 250 us: 1.27x slower                                                   |
| json_dumps           | 6.19 ms                                                | 7.95 ms: 1.29x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 187 us: 1.29x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.2 ms: 1.08x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 15.6 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 37.4 ms: 1.23x slower                                                  |
| genshi_text     | 14.7 ms                                                | 18.3 ms: 1.25x slower                                                  |
| django_template | 19.7 ms                                                | 26.9 ms: 1.37x slower                                                  |
| mako            | 7.44 ms                                                | 10.8 ms: 1.45x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.32x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.6 ms: 2.37x faster                                                  |
| gc_traversal                     | 2.95 ms                                                | 1.43 ms: 2.06x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 331 ms: 2.03x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 343 ms: 1.95x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 317 ms: 1.94x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 358 ms: 1.88x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 184 ms: 1.73x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 149 ms: 1.72x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 172 ms: 1.53x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 207 ms: 1.50x faster                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 780 us: 1.47x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 388 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 413 ms: 1.28x faster                                                   |
| deepcopy                         | 226 us                                                 | 186 us: 1.22x faster                                                   |
| regex_effbot                     | 2.44 ms                                                | 2.08 ms: 1.17x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.33 us: 1.16x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 66.4 ms: 1.14x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| async_generators                 | 299 ms                                                 | 276 ms: 1.08x faster                                                   |
| coroutines                       | 19.7 ms                                                | 18.7 ms: 1.05x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 27.7 ms: 1.05x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 24.8 us: 1.05x faster                                                  |
| regex_dna                        | 143 ms                                                 | 137 ms: 1.04x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.96 us: 1.03x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 369 ms: 1.01x faster                                                   |
| regex_v8                         | 15.1 ms                                                | 14.9 ms: 1.01x faster                                                  |
| pathlib                          | 24.7 ms                                                | 24.5 ms: 1.01x faster                                                  |
| pidigits                         | 283 ms                                                 | 281 ms: 1.01x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.47 sec: 1.01x slower                                                 |
| float                            | 54.1 ms                                                | 54.8 ms: 1.01x slower                                                  |
| generators                       | 29.4 ms                                                | 29.8 ms: 1.01x slower                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 66.6 ms: 1.02x slower                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.38 sec: 1.03x slower                                                 |
| json                             | 3.00 ms                                                | 3.10 ms: 1.03x slower                                                  |
| sphinx                           | 613 ms                                                 | 635 ms: 1.04x slower                                                   |
| pycparser                        | 673 ms                                                 | 711 ms: 1.06x slower                                                   |
| comprehensions                   | 14.0 us                                                | 14.8 us: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 372 ms: 1.07x slower                                                   |
| python_startup                   | 17.8 ms                                                | 19.2 ms: 1.08x slower                                                  |
| html5lib                         | 33.4 ms                                                | 36.2 ms: 1.08x slower                                                  |
| go                               | 98.5 ms                                                | 107 ms: 1.09x slower                                                   |
| xml_etree_generate               | 55.4 ms                                                | 60.5 ms: 1.09x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.6 us: 1.09x slower                                                  |
| thrift                           | 468 us                                                 | 513 us: 1.10x slower                                                   |
| mdp                              | 1.49 sec                                               | 1.67 sec: 1.12x slower                                                 |
| shortest_path                    | 331 ms                                                 | 370 ms: 1.12x slower                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 69.6 ms: 1.12x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 85.8 ms: 1.13x slower                                                  |
| regex_compile                    | 75.9 ms                                                | 86.4 ms: 1.14x slower                                                  |
| logging_simple                   | 3.60 us                                                | 4.13 us: 1.15x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 44.9 ms: 1.16x slower                                                  |
| 2to3                             | 168 ms                                                 | 195 ms: 1.16x slower                                                   |
| logging_format                   | 3.90 us                                                | 4.53 us: 1.16x slower                                                  |
| sympy_str                        | 144 ms                                                 | 168 ms: 1.17x slower                                                   |
| raytrace                         | 204 ms                                                 | 239 ms: 1.17x slower                                                   |
| connected_components             | 300 ms                                                 | 352 ms: 1.17x slower                                                   |
| sympy_integrate                  | 11.1 ms                                                | 13.0 ms: 1.17x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 167 ms: 1.18x slower                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.77 ms: 1.18x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.60 sec: 1.18x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 90.6 ms: 1.19x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 15.6 ms: 1.19x slower                                                  |
| pyflate                          | 311 ms                                                 | 370 ms: 1.19x slower                                                   |
| chaos                            | 41.6 ms                                                | 49.7 ms: 1.19x slower                                                  |
| deltablue                        | 2.57 ms                                                | 3.08 ms: 1.20x slower                                                  |
| many_optionals                   | 403 us                                                 | 484 us: 1.20x slower                                                   |
| logging_silent                   | 72.5 ns                                                | 87.2 ns: 1.20x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 286 ms: 1.22x slower                                                   |
| genshi_xml                       | 30.5 ms                                                | 37.4 ms: 1.23x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 238 ms: 1.23x slower                                                   |
| scimark_sor                      | 85.8 ms                                                | 106 ms: 1.23x slower                                                   |
| pprint_pformat                   | 986 ms                                                 | 1.23 sec: 1.24x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 604 ms: 1.25x slower                                                   |
| genshi_text                      | 14.7 ms                                                | 18.3 ms: 1.25x slower                                                  |
| nqueens                          | 59.5 ms                                                | 75.0 ms: 1.26x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 87.6 ms: 1.27x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 116 us: 1.27x slower                                                   |
| pickle_pure_python               | 197 us                                                 | 250 us: 1.27x slower                                                   |
| async_tree_eager                 | 65.8 ms                                                | 83.9 ms: 1.27x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.95 ms: 1.29x slower                                                  |
| unpickle_pure_python             | 145 us                                                 | 187 us: 1.29x slower                                                   |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 4.09 ms: 1.30x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 67.0 ms: 1.30x slower                                                  |
| fannkuch                         | 250 ms                                                 | 327 ms: 1.31x slower                                                   |
| telco                            | 3.92 ms                                                | 5.24 ms: 1.34x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 98.6 ms: 1.34x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 60.6 ms: 1.36x slower                                                  |
| django_template                  | 19.7 ms                                                | 26.9 ms: 1.37x slower                                                  |
| hexiom                           | 4.38 ms                                                | 6.02 ms: 1.38x slower                                                  |
| richards                         | 30.6 ms                                                | 42.4 ms: 1.39x slower                                                  |
| richards_super                   | 34.6 ms                                                | 48.7 ms: 1.41x slower                                                  |
| mako                             | 7.44 ms                                                | 10.8 ms: 1.45x slower                                                  |
| nbody                            | 67.6 ms                                                | 105 ms: 1.55x slower                                                   |
| bench_thread_pool                | 483 us                                                 | 756 us: 1.57x slower                                                   |
| coverage                         | 38.5 ms                                                | 61.1 ms: 1.59x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 127 ms: 2.70x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (2): pylint, k_core
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.044x slower

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.24x