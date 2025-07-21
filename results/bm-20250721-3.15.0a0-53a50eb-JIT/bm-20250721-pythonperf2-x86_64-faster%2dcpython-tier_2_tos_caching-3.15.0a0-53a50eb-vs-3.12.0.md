# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 53a50eb
- commit date: 2025-07-21
- overall geometric mean: 1.030x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                                |
| docutils       | 2.87 sec                                                     | 2.94 sec: 1.03x slower                                                              |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 625 ms: 1.67x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                                |
| async_tree_none            | 452 ms                                                       | 274 ms: 1.65x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 331 ms: 1.64x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 274 ms: 1.57x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 500 ms: 1.39x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                                |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 61.5 ms: 1.25x faster                                                               |
| pidigits       | 265 ms                                                       | 256 ms: 1.04x faster                                                                |
| nbody          | 88.0 ms                                                      | 88.8 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                                |
| regex_dna      | 239 ms                                                       | 227 ms: 1.05x faster                                                                |
| regex_effbot   | 3.57 ms                                                      | 3.58 ms: 1.00x slower                                                               |
| regex_v8       | 23.6 ms                                                      | 24.5 ms: 1.04x slower                                                               |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.94 sec: 1.11x faster                                                              |
| xml_etree_iterparse  | 103 ms                                                       | 96.4 ms: 1.07x faster                                                               |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                                |
| xml_etree_generate   | 86.1 ms                                                      | 83.2 ms: 1.04x faster                                                               |
| unpickle_pure_python | 210 us                                                       | 204 us: 1.03x faster                                                                |
| xml_etree_process    | 58.4 ms                                                      | 58.2 ms: 1.00x faster                                                               |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                               |
| pickle_pure_python   | 318 us                                                       | 338 us: 1.06x slower                                                                |
| json_dumps           | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                               |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.70 ms: 1.01x slower                                                               |
| python_startup         | 11.6 ms                                                      | 15.2 ms: 1.31x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.15x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.2 ms: 1.08x faster                                                               |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 2.00x faster                                                              |
| async_tree_io              | 1.04 sec                                                     | 625 ms: 1.67x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                                |
| async_tree_none            | 452 ms                                                       | 274 ms: 1.65x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 331 ms: 1.64x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 274 ms: 1.57x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 500 ms: 1.39x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                                |
| deepcopy                   | 368 us                                                       | 278 us: 1.33x faster                                                                |
| deepcopy_memo              | 36.8 us                                                      | 28.4 us: 1.29x faster                                                               |
| richards                   | 45.7 ms                                                      | 35.5 ms: 1.29x faster                                                               |
| generators                 | 37.4 ms                                                      | 29.1 ms: 1.29x faster                                                               |
| float                      | 76.6 ms                                                      | 61.5 ms: 1.25x faster                                                               |
| richards_super             | 51.3 ms                                                      | 41.6 ms: 1.24x faster                                                               |
| comprehensions             | 21.9 us                                                      | 17.8 us: 1.23x faster                                                               |
| go                         | 150 ms                                                       | 126 ms: 1.19x faster                                                                |
| spectral_norm              | 91.6 ms                                                      | 79.4 ms: 1.15x faster                                                               |
| tomli_loads                | 2.16 sec                                                     | 1.94 sec: 1.11x faster                                                              |
| deltablue                  | 3.24 ms                                                      | 2.92 ms: 1.11x faster                                                               |
| deepcopy_reduce            | 3.37 us                                                      | 3.04 us: 1.11x faster                                                               |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.11x faster                                                               |
| dulwich_log                | 65.4 ms                                                      | 59.7 ms: 1.09x faster                                                               |
| logging_format             | 7.48 us                                                      | 6.87 us: 1.09x faster                                                               |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                                |
| django_template            | 38.2 ms                                                      | 35.2 ms: 1.08x faster                                                               |
| pprint_pformat             | 1.65 sec                                                     | 1.53 sec: 1.08x faster                                                              |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.0 ms: 1.08x faster                                                               |
| pprint_safe_repr           | 807 ms                                                       | 753 ms: 1.07x faster                                                                |
| xml_etree_iterparse        | 103 ms                                                       | 96.4 ms: 1.07x faster                                                               |
| sympy_integrate            | 23.9 ms                                                      | 22.4 ms: 1.07x faster                                                               |
| chaos                      | 64.0 ms                                                      | 60.1 ms: 1.07x faster                                                               |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                                |
| logging_simple             | 6.71 us                                                      | 6.32 us: 1.06x faster                                                               |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                                |
| regex_dna                  | 239 ms                                                       | 227 ms: 1.05x faster                                                                |
| meteor_contest             | 128 ms                                                       | 123 ms: 1.04x faster                                                                |
| pyflate                    | 439 ms                                                       | 423 ms: 1.04x faster                                                                |
| pidigits                   | 265 ms                                                       | 256 ms: 1.04x faster                                                                |
| xml_etree_generate         | 86.1 ms                                                      | 83.2 ms: 1.04x faster                                                               |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.03x faster                                                                |
| unpickle_pure_python       | 210 us                                                       | 204 us: 1.03x faster                                                                |
| scimark_lu                 | 98.8 ms                                                      | 96.4 ms: 1.02x faster                                                               |
| raytrace                   | 298 ms                                                       | 292 ms: 1.02x faster                                                                |
| crypto_pyaes               | 80.3 ms                                                      | 79.0 ms: 1.02x faster                                                               |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                               |
| logging_silent             | 94.4 ns                                                      | 93.3 ns: 1.01x faster                                                               |
| asyncio_websockets         | 387 ms                                                       | 383 ms: 1.01x faster                                                                |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                                |
| xml_etree_process          | 58.4 ms                                                      | 58.2 ms: 1.00x faster                                                               |
| regex_effbot               | 3.57 ms                                                      | 3.58 ms: 1.00x slower                                                               |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                                                |
| scimark_fft                | 301 ms                                                       | 303 ms: 1.01x slower                                                                |
| python_startup_no_site     | 8.64 ms                                                      | 8.70 ms: 1.01x slower                                                               |
| nbody                      | 88.0 ms                                                      | 88.8 ms: 1.01x slower                                                               |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                               |
| docutils                   | 2.87 sec                                                     | 2.94 sec: 1.03x slower                                                              |
| nqueens                    | 89.9 ms                                                      | 92.6 ms: 1.03x slower                                                               |
| sympy_expand               | 484 ms                                                       | 500 ms: 1.03x slower                                                                |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                               |
| regex_v8                   | 23.6 ms                                                      | 24.5 ms: 1.04x slower                                                               |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                               |
| json                       | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                                               |
| hexiom                     | 5.96 ms                                                      | 6.28 ms: 1.05x slower                                                               |
| fannkuch                   | 350 ms                                                       | 370 ms: 1.06x slower                                                                |
| pickle_pure_python         | 318 us                                                       | 338 us: 1.06x slower                                                                |
| json_dumps                 | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                               |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                                |
| async_generators           | 390 ms                                                       | 447 ms: 1.15x slower                                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.91 ms: 1.17x slower                                                               |
| coverage                   | 66.7 ms                                                      | 78.7 ms: 1.18x slower                                                               |
| python_startup             | 11.6 ms                                                      | 15.2 ms: 1.31x slower                                                               |
| create_gc_cycles           | 1.59 ms                                                      | 2.85 ms: 1.79x slower                                                               |
| gc_traversal               | 3.48 ms                                                      | 6.47 ms: 1.86x slower                                                               |
| telco                      | 6.96 ms                                                      | 160 ms: 22.97x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                        |

Benchmark hidden because not significant (1): pycparser
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250721-3.15.0a0-53a50eb-JIT/bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.15x