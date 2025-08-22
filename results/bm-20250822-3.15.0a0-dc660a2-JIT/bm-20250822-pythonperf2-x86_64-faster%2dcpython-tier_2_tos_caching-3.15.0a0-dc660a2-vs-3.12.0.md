# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: dc660a2
- commit date: 2025-08-22
- overall geometric mean: 1.048x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                                |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 616 ms: 1.69x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 627 ms: 1.68x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 326 ms: 1.67x faster                                                                |
| async_tree_none            | 452 ms                                                       | 272 ms: 1.66x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 497 ms: 1.40x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                                |
| Geometric mean             | (ref)                                                        | 1.58x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 59.8 ms: 1.28x faster                                                               |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                                |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                                |
| regex_dna      | 239 ms                                                       | 227 ms: 1.05x faster                                                                |
| regex_effbot   | 3.57 ms                                                      | 3.59 ms: 1.01x slower                                                               |
| regex_v8       | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.89 sec: 1.14x faster                                                              |
| unpickle_pure_python | 210 us                                                       | 191 us: 1.10x faster                                                                |
| xml_etree_generate   | 86.1 ms                                                      | 79.8 ms: 1.08x faster                                                               |
| xml_etree_iterparse  | 103 ms                                                       | 95.6 ms: 1.08x faster                                                               |
| xml_etree_process    | 58.4 ms                                                      | 55.0 ms: 1.06x faster                                                               |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                                |
| pickle_pure_python   | 318 us                                                       | 331 us: 1.04x slower                                                                |
| json_loads           | 24.4 us                                                      | 25.7 us: 1.05x slower                                                               |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                               |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.3 ms: 1.08x faster                                                               |
| mako            | 10.0 ms                                                      | 10.1 ms: 1.01x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                              |
| async_tree_io              | 1.04 sec                                                     | 616 ms: 1.69x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 627 ms: 1.68x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 326 ms: 1.67x faster                                                                |
| async_tree_none            | 452 ms                                                       | 272 ms: 1.66x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 497 ms: 1.40x faster                                                                |
| richards                   | 45.7 ms                                                      | 32.7 ms: 1.40x faster                                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                                |
| richards_super             | 51.3 ms                                                      | 37.8 ms: 1.36x faster                                                               |
| deepcopy                   | 368 us                                                       | 280 us: 1.31x faster                                                                |
| deepcopy_memo              | 36.8 us                                                      | 28.3 us: 1.30x faster                                                               |
| float                      | 76.6 ms                                                      | 59.8 ms: 1.28x faster                                                               |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                               |
| go                         | 150 ms                                                       | 121 ms: 1.24x faster                                                                |
| generators                 | 37.4 ms                                                      | 31.0 ms: 1.21x faster                                                               |
| spectral_norm              | 91.6 ms                                                      | 76.7 ms: 1.19x faster                                                               |
| logging_format             | 7.48 us                                                      | 6.31 us: 1.19x faster                                                               |
| logging_simple             | 6.71 us                                                      | 5.77 us: 1.16x faster                                                               |
| tomli_loads                | 2.16 sec                                                     | 1.89 sec: 1.14x faster                                                              |
| deltablue                  | 3.24 ms                                                      | 2.85 ms: 1.14x faster                                                               |
| pathlib                    | 18.9 ms                                                      | 16.6 ms: 1.14x faster                                                               |
| dulwich_log                | 65.4 ms                                                      | 58.5 ms: 1.12x faster                                                               |
| pprint_pformat             | 1.65 sec                                                     | 1.49 sec: 1.11x faster                                                              |
| deepcopy_reduce            | 3.37 us                                                      | 3.05 us: 1.11x faster                                                               |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.5 ms: 1.10x faster                                                               |
| unpickle_pure_python       | 210 us                                                       | 191 us: 1.10x faster                                                                |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                                |
| pyflate                    | 439 ms                                                       | 405 ms: 1.08x faster                                                                |
| django_template            | 38.2 ms                                                      | 35.3 ms: 1.08x faster                                                               |
| pprint_safe_repr           | 807 ms                                                       | 746 ms: 1.08x faster                                                                |
| xml_etree_generate         | 86.1 ms                                                      | 79.8 ms: 1.08x faster                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 95.6 ms: 1.08x faster                                                               |
| raytrace                   | 298 ms                                                       | 277 ms: 1.07x faster                                                                |
| sympy_integrate            | 23.9 ms                                                      | 22.3 ms: 1.07x faster                                                               |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                                |
| chaos                      | 64.0 ms                                                      | 59.7 ms: 1.07x faster                                                               |
| xml_etree_process          | 58.4 ms                                                      | 55.0 ms: 1.06x faster                                                               |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                                                |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                                |
| crypto_pyaes               | 80.3 ms                                                      | 76.3 ms: 1.05x faster                                                               |
| regex_dna                  | 239 ms                                                       | 227 ms: 1.05x faster                                                                |
| scimark_sor                | 109 ms                                                       | 105 ms: 1.04x faster                                                                |
| scimark_lu                 | 98.8 ms                                                      | 95.1 ms: 1.04x faster                                                               |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                                |
| pycparser                  | 1.23 sec                                                     | 1.19 sec: 1.04x faster                                                              |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.04x faster                                                                |
| logging_silent             | 94.4 ns                                                      | 92.3 ns: 1.02x faster                                                               |
| coroutines                 | 23.0 ms                                                      | 22.5 ms: 1.02x faster                                                               |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                                |
| hexiom                     | 5.96 ms                                                      | 5.93 ms: 1.00x faster                                                               |
| scimark_fft                | 301 ms                                                       | 300 ms: 1.00x faster                                                                |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                                                |
| regex_effbot               | 3.57 ms                                                      | 3.59 ms: 1.01x slower                                                               |
| regex_v8                   | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                               |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                               |
| mako                       | 10.0 ms                                                      | 10.1 ms: 1.01x slower                                                               |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                              |
| python_startup_no_site     | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                               |
| nqueens                    | 89.9 ms                                                      | 92.7 ms: 1.03x slower                                                               |
| fannkuch                   | 350 ms                                                       | 362 ms: 1.03x slower                                                                |
| sympy_expand               | 484 ms                                                       | 503 ms: 1.04x slower                                                                |
| pickle_pure_python         | 318 us                                                       | 331 us: 1.04x slower                                                                |
| json_loads                 | 24.4 us                                                      | 25.7 us: 1.05x slower                                                               |
| json                       | 5.12 ms                                                      | 5.42 ms: 1.06x slower                                                               |
| async_generators           | 390 ms                                                       | 436 ms: 1.12x slower                                                                |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.13x slower                                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.98 ms: 1.18x slower                                                               |
| coverage                   | 66.7 ms                                                      | 83.0 ms: 1.24x slower                                                               |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                               |
| create_gc_cycles           | 1.59 ms                                                      | 2.83 ms: 1.78x slower                                                               |
| gc_traversal               | 3.48 ms                                                      | 6.54 ms: 1.88x slower                                                               |
| telco                      | 6.96 ms                                                      | 159 ms: 22.89x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                        |

Benchmark hidden because not significant (2): nbody, json_dumps
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250822-3.15.0a0-dc660a2-JIT/bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.15x