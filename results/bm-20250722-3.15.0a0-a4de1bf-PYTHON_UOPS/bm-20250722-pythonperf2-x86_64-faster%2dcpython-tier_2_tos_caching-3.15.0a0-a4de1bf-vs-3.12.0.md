# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.142x slower
- HPT reliability: 99.34%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 328 ms: 1.15x slower                                                                |
| docutils       | 2.87 sec                                                     | 3.14 sec: 1.10x slower                                                              |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 661 ms: 1.59x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 665 ms: 1.57x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 355 ms: 1.52x faster                                                                |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 358 ms: 1.52x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 292 ms: 1.47x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 528 ms: 1.32x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 530 ms: 1.32x faster                                                                |
| Geometric mean             | (ref)                                                        | 1.48x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 257 ms: 1.03x faster                                                                |
| float          | 76.6 ms                                                      | 102 ms: 1.34x slower                                                                |
| nbody          | 88.0 ms                                                      | 198 ms: 2.25x slower                                                                |
| Geometric mean | (ref)                                                        | 1.43x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 226 ms: 1.05x faster                                                                |
| regex_v8       | 23.6 ms                                                      | 23.7 ms: 1.00x slower                                                               |
| regex_effbot   | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                               |
| regex_compile  | 144 ms                                                       | 160 ms: 1.11x slower                                                                |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 109 ms: 1.06x slower                                                                |
| json_loads           | 24.4 us                                                      | 26.2 us: 1.07x slower                                                               |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                               |
| xml_etree_generate   | 86.1 ms                                                      | 111 ms: 1.29x slower                                                                |
| pickle_pure_python   | 318 us                                                       | 414 us: 1.30x slower                                                                |
| xml_etree_process    | 58.4 ms                                                      | 76.9 ms: 1.32x slower                                                               |
| tomli_loads          | 2.16 sec                                                     | 2.92 sec: 1.35x slower                                                              |
| unpickle_pure_python | 210 us                                                       | 383 us: 1.83x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.24x slower                                                                        |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.69 ms: 1.01x slower                                                               |
| python_startup         | 11.6 ms                                                      | 15.2 ms: 1.31x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.15x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.7 ms: 1.07x faster                                                               |
| mako            | 10.0 ms                                                      | 18.4 ms: 1.84x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.31x slower                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.49 sec: 1.73x faster                                                              |
| async_tree_io_tg           | 1.05 sec                                                     | 661 ms: 1.59x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 665 ms: 1.57x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 355 ms: 1.52x faster                                                                |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 358 ms: 1.52x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 292 ms: 1.47x faster                                                                |
| deepcopy                   | 368 us                                                       | 277 us: 1.33x faster                                                                |
| deepcopy_memo              | 36.8 us                                                      | 27.7 us: 1.33x faster                                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 528 ms: 1.32x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 530 ms: 1.32x faster                                                                |
| generators                 | 37.4 ms                                                      | 29.9 ms: 1.25x faster                                                               |
| deepcopy_reduce            | 3.37 us                                                      | 2.94 us: 1.15x faster                                                               |
| pathlib                    | 18.9 ms                                                      | 17.0 ms: 1.11x faster                                                               |
| logging_format             | 7.48 us                                                      | 6.74 us: 1.11x faster                                                               |
| logging_simple             | 6.71 us                                                      | 6.17 us: 1.09x faster                                                               |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.07x faster                                                                |
| django_template            | 38.2 ms                                                      | 35.7 ms: 1.07x faster                                                               |
| regex_dna                  | 239 ms                                                       | 226 ms: 1.05x faster                                                                |
| scimark_lu                 | 98.8 ms                                                      | 94.2 ms: 1.05x faster                                                               |
| dulwich_log                | 65.4 ms                                                      | 62.4 ms: 1.05x faster                                                               |
| coroutines                 | 23.0 ms                                                      | 22.2 ms: 1.03x faster                                                               |
| pidigits                   | 265 ms                                                       | 257 ms: 1.03x faster                                                                |
| logging_silent             | 94.4 ns                                                      | 92.2 ns: 1.02x faster                                                               |
| sympy_integrate            | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                                               |
| chaos                      | 64.0 ms                                                      | 63.2 ms: 1.01x faster                                                               |
| regex_v8                   | 23.6 ms                                                      | 23.7 ms: 1.00x slower                                                               |
| python_startup_no_site     | 8.64 ms                                                      | 8.69 ms: 1.01x slower                                                               |
| regex_effbot               | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                               |
| sympy_sum                  | 162 ms                                                       | 164 ms: 1.01x slower                                                                |
| json                       | 5.12 ms                                                      | 5.36 ms: 1.05x slower                                                               |
| sympy_str                  | 302 ms                                                       | 318 ms: 1.05x slower                                                                |
| xml_etree_iterparse        | 103 ms                                                       | 109 ms: 1.06x slower                                                                |
| json_loads                 | 24.4 us                                                      | 26.2 us: 1.07x slower                                                               |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                               |
| docutils                   | 2.87 sec                                                     | 3.14 sec: 1.10x slower                                                              |
| sqlite_synth               | 2.77 us                                                      | 3.04 us: 1.10x slower                                                               |
| regex_compile              | 144 ms                                                       | 160 ms: 1.11x slower                                                                |
| raytrace                   | 298 ms                                                       | 332 ms: 1.11x slower                                                                |
| richards                   | 45.7 ms                                                      | 52.6 ms: 1.15x slower                                                               |
| 2to3                       | 285 ms                                                       | 328 ms: 1.15x slower                                                                |
| sympy_expand               | 484 ms                                                       | 559 ms: 1.16x slower                                                                |
| richards_super             | 51.3 ms                                                      | 59.4 ms: 1.16x slower                                                               |
| async_generators           | 390 ms                                                       | 459 ms: 1.18x slower                                                                |
| nqueens                    | 89.9 ms                                                      | 106 ms: 1.18x slower                                                                |
| coverage                   | 66.7 ms                                                      | 79.6 ms: 1.19x slower                                                               |
| pycparser                  | 1.23 sec                                                     | 1.51 sec: 1.22x slower                                                              |
| meteor_contest             | 128 ms                                                       | 162 ms: 1.26x slower                                                                |
| xml_etree_generate         | 86.1 ms                                                      | 111 ms: 1.29x slower                                                                |
| scimark_monte_carlo        | 69.0 ms                                                      | 89.0 ms: 1.29x slower                                                               |
| pickle_pure_python         | 318 us                                                       | 414 us: 1.30x slower                                                                |
| python_startup             | 11.6 ms                                                      | 15.2 ms: 1.31x slower                                                               |
| xml_etree_process          | 58.4 ms                                                      | 76.9 ms: 1.32x slower                                                               |
| comprehensions             | 21.9 us                                                      | 29.2 us: 1.33x slower                                                               |
| float                      | 76.6 ms                                                      | 102 ms: 1.34x slower                                                                |
| tomli_loads                | 2.16 sec                                                     | 2.92 sec: 1.35x slower                                                              |
| crypto_pyaes               | 80.3 ms                                                      | 109 ms: 1.36x slower                                                                |
| typing_runtime_protocols   | 152 us                                                       | 208 us: 1.37x slower                                                                |
| pprint_pformat             | 1.65 sec                                                     | 2.32 sec: 1.40x slower                                                              |
| pprint_safe_repr           | 807 ms                                                       | 1.14 sec: 1.41x slower                                                              |
| pyflate                    | 439 ms                                                       | 633 ms: 1.44x slower                                                                |
| go                         | 150 ms                                                       | 228 ms: 1.52x slower                                                                |
| scimark_fft                | 301 ms                                                       | 479 ms: 1.59x slower                                                                |
| deltablue                  | 3.24 ms                                                      | 5.71 ms: 1.76x slower                                                               |
| fannkuch                   | 350 ms                                                       | 622 ms: 1.78x slower                                                                |
| hexiom                     | 5.96 ms                                                      | 10.7 ms: 1.79x slower                                                               |
| gc_traversal               | 3.48 ms                                                      | 6.27 ms: 1.80x slower                                                               |
| create_gc_cycles           | 1.59 ms                                                      | 2.90 ms: 1.82x slower                                                               |
| unpickle_pure_python       | 210 us                                                       | 383 us: 1.83x slower                                                                |
| mako                       | 10.0 ms                                                      | 18.4 ms: 1.84x slower                                                               |
| spectral_norm              | 91.6 ms                                                      | 172 ms: 1.88x slower                                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 8.59 ms: 2.04x slower                                                               |
| nbody                      | 88.0 ms                                                      | 198 ms: 2.25x slower                                                                |
| telco                      | 6.96 ms                                                      | 159 ms: 22.80x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                                        |

Benchmark hidden because not significant (2): asyncio_websockets, xml_etree_parse
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250722-3.15.0a0-a4de1bf-PYTHON_UOPS/bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.142x slower

# HPT report

- Reliability score: 99.34% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.14x