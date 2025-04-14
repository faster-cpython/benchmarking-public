# Results vs. 3.12.0

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: 50dd66b
- commit date: 2025-03-26
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                         |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                         |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.90x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 306 ms: 1.88x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.87x faster                                         |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 469 ms: 1.55x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                         |
| Geometric mean             | (ref)                                                  | 1.78x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.5 ms: 1.22x faster                                        |
| nbody          | 97.0 ms                                                | 93.8 ms: 1.03x faster                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.09 ms: 1.17x faster                                        |
| regex_dna      | 212 ms                                                 | 211 ms: 1.01x faster                                         |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                       |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.13x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                        |
| xml_etree_generate   | 89.2 ms                                                | 84.5 ms: 1.05x faster                                        |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                         |
| xml_etree_process    | 61.7 ms                                                | 58.9 ms: 1.05x faster                                        |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                         |
| json_loads           | 28.5 us                                                | 30.5 us: 1.07x slower                                        |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.17 ms: 1.18x slower                                        |
| python_startup         | 9.55 ms                                                | 13.0 ms: 1.37x slower                                        |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                        |
| mako            | 11.9 ms                                                | 11.3 ms: 1.06x faster                                        |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                         |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.90x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 306 ms: 1.88x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.87x faster                                         |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 469 ms: 1.55x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                         |
| deepcopy                   | 371 us                                                 | 257 us: 1.45x faster                                         |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                        |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                        |
| go                         | 139 ms                                                 | 114 ms: 1.22x faster                                         |
| float                      | 84.7 ms                                                | 69.5 ms: 1.22x faster                                        |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                       |
| logging_format             | 7.23 us                                                | 6.05 us: 1.20x faster                                        |
| raytrace                   | 312 ms                                                 | 263 ms: 1.19x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.13 ms: 1.19x faster                                        |
| async_generators           | 463 ms                                                 | 391 ms: 1.18x faster                                         |
| dulwich_log                | 68.5 ms                                                | 57.9 ms: 1.18x faster                                        |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                         |
| spectral_norm              | 115 ms                                                 | 97.8 ms: 1.17x faster                                        |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                        |
| regex_effbot               | 3.61 ms                                                | 3.09 ms: 1.17x faster                                        |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                        |
| chaos                      | 67.0 ms                                                | 58.1 ms: 1.15x faster                                        |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.13x faster                                        |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.13x faster                                         |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 67.5 ms: 1.11x faster                                        |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                        |
| logging_silent             | 104 ns                                                 | 94.2 ns: 1.11x faster                                        |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                        |
| crypto_pyaes               | 81.9 ms                                                | 73.9 ms: 1.11x faster                                        |
| scimark_fft                | 382 ms                                                 | 348 ms: 1.10x faster                                         |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.65 ms: 1.09x faster                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                        |
| pyflate                    | 482 ms                                                 | 445 ms: 1.08x faster                                         |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                        |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                       |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                         |
| pprint_safe_repr           | 776 ms                                                 | 730 ms: 1.06x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                       |
| richards                   | 45.8 ms                                                | 43.3 ms: 1.06x faster                                        |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.06x faster                                        |
| xml_etree_generate         | 89.2 ms                                                | 84.5 ms: 1.05x faster                                        |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                       |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                         |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                         |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                       |
| xml_etree_process          | 61.7 ms                                                | 58.9 ms: 1.05x faster                                        |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                         |
| richards_super             | 51.5 ms                                                | 49.4 ms: 1.04x faster                                        |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                        |
| nbody                      | 97.0 ms                                                | 93.8 ms: 1.03x faster                                        |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                        |
| nqueens                    | 83.3 ms                                                | 81.3 ms: 1.02x faster                                        |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                         |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                         |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.01x faster                                         |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.01x faster                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| fannkuch                   | 417 ms                                                 | 420 ms: 1.01x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                         |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                        |
| bench_thread_pool          | 842 us                                                 | 871 us: 1.03x slower                                         |
| json_loads                 | 28.5 us                                                | 30.5 us: 1.07x slower                                        |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                        |
| telco                      | 7.10 ms                                                | 7.98 ms: 1.12x slower                                        |
| python_startup_no_site     | 6.94 ms                                                | 8.17 ms: 1.18x slower                                        |
| gc_traversal               | 3.79 ms                                                | 4.65 ms: 1.23x slower                                        |
| coverage                   | 72.7 ms                                                | 91.7 ms: 1.26x slower                                        |
| python_startup             | 9.55 ms                                                | 13.0 ms: 1.37x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                        |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250326-3.14.0a6+-50dd66b/bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x