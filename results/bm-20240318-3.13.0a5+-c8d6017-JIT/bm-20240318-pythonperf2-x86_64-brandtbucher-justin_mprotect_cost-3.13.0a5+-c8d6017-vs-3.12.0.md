# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: linux-x86_64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 304 ms: 1.07x slower                                                               |
| chameleon      | 7.23 ms                                                      | 7.30 ms: 1.01x slower                                                              |
| docutils       | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                             |
| tornado_http   | 121 ms                                                       | 128 ms: 1.06x slower                                                               |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 436 ms: 1.04x faster                                                               |
| async_tree_none_tg         | 431 ms                                                       | 433 ms: 1.01x slower                                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 705 ms: 1.01x slower                                                               |
| async_tree_memoization_tg  | 540 ms                                                       | 553 ms: 1.02x slower                                                               |
| async_tree_io_tg           | 1.05 sec                                                     | 1.08 sec: 1.02x slower                                                             |
| async_tree_io              | 1.04 sec                                                     | 1.08 sec: 1.04x slower                                                             |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                       |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 261 ms: 1.01x faster                                                               |
| float          | 76.6 ms                                                      | 78.6 ms: 1.03x slower                                                              |
| nbody          | 88.0 ms                                                      | 95.5 ms: 1.09x slower                                                              |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 146 ms: 1.02x slower                                                               |
| regex_effbot   | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                                              |
| regex_dna      | 239 ms                                                       | 252 ms: 1.06x slower                                                               |
| regex_v8       | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                              |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.4 us: 1.07x faster                                                              |
| pickle               | 10.5 us                                                      | 10.2 us: 1.04x faster                                                              |
| pickle_pure_python   | 318 us                                                       | 309 us: 1.03x faster                                                               |
| xml_etree_generate   | 86.1 ms                                                      | 84.2 ms: 1.02x faster                                                              |
| unpickle_list        | 4.66 us                                                      | 4.59 us: 1.02x faster                                                              |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                               |
| xml_etree_process    | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                              |
| tomli_loads          | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                                             |
| json_loads           | 24.4 us                                                      | 24.6 us: 1.01x slower                                                              |
| pickle_list          | 4.43 us                                                      | 4.50 us: 1.02x slower                                                              |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                              |
| unpickle_pure_python | 210 us                                                       | 232 us: 1.11x slower                                                               |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                       |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 14.4 ms: 1.24x slower                                                              |
| python_startup_no_site | 8.64 ms                                                      | 12.8 ms: 1.48x slower                                                              |
| Geometric mean         | (ref)                                                        | 1.35x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.92 ms: 1.01x faster                                                              |
| django_template | 38.2 ms                                                      | 38.5 ms: 1.01x slower                                                              |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 152 us                                                       | 121 us: 1.25x faster                                                               |
| comprehensions             | 21.9 us                                                      | 18.8 us: 1.17x faster                                                              |
| generators                 | 37.4 ms                                                      | 33.5 ms: 1.12x faster                                                              |
| pickle_dict                | 32.5 us                                                      | 30.4 us: 1.07x faster                                                              |
| crypto_pyaes               | 80.3 ms                                                      | 77.4 ms: 1.04x faster                                                              |
| async_tree_none            | 452 ms                                                       | 436 ms: 1.04x faster                                                               |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.04x faster                                                              |
| pickle_pure_python         | 318 us                                                       | 309 us: 1.03x faster                                                               |
| deepcopy_reduce            | 3.37 us                                                      | 3.28 us: 1.03x faster                                                              |
| create_gc_cycles           | 1.59 ms                                                      | 1.55 ms: 1.03x faster                                                              |
| coroutines                 | 23.0 ms                                                      | 22.4 ms: 1.03x faster                                                              |
| sqlite_synth               | 2.77 us                                                      | 2.70 us: 1.03x faster                                                              |
| xml_etree_generate         | 86.1 ms                                                      | 84.2 ms: 1.02x faster                                                              |
| asyncio_tcp                | 378 ms                                                       | 372 ms: 1.02x faster                                                               |
| unpickle_list              | 4.66 us                                                      | 4.59 us: 1.02x faster                                                              |
| pidigits                   | 265 ms                                                       | 261 ms: 1.01x faster                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                               |
| mako                       | 10.0 ms                                                      | 9.92 ms: 1.01x faster                                                              |
| async_generators           | 390 ms                                                       | 388 ms: 1.01x faster                                                               |
| sympy_sum                  | 162 ms                                                       | 161 ms: 1.01x faster                                                               |
| async_tree_none_tg         | 431 ms                                                       | 433 ms: 1.01x slower                                                               |
| xml_etree_process          | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                              |
| sympy_str                  | 302 ms                                                       | 305 ms: 1.01x slower                                                               |
| logging_simple             | 6.71 us                                                      | 6.77 us: 1.01x slower                                                              |
| django_template            | 38.2 ms                                                      | 38.5 ms: 1.01x slower                                                              |
| logging_format             | 7.48 us                                                      | 7.55 us: 1.01x slower                                                              |
| tomli_loads                | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                                             |
| chameleon                  | 7.23 ms                                                      | 7.30 ms: 1.01x slower                                                              |
| deepcopy_memo              | 36.8 us                                                      | 37.1 us: 1.01x slower                                                              |
| json_loads                 | 24.4 us                                                      | 24.6 us: 1.01x slower                                                              |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 705 ms: 1.01x slower                                                               |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.25 ms: 1.01x slower                                                              |
| pickle_list                | 4.43 us                                                      | 4.50 us: 1.02x slower                                                              |
| regex_compile              | 144 ms                                                       | 146 ms: 1.02x slower                                                               |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                              |
| docutils                   | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                             |
| spectral_norm              | 91.6 ms                                                      | 93.7 ms: 1.02x slower                                                              |
| async_tree_memoization_tg  | 540 ms                                                       | 553 ms: 1.02x slower                                                               |
| async_tree_io_tg           | 1.05 sec                                                     | 1.08 sec: 1.02x slower                                                             |
| raytrace                   | 298 ms                                                       | 305 ms: 1.03x slower                                                               |
| float                      | 76.6 ms                                                      | 78.6 ms: 1.03x slower                                                              |
| meteor_contest             | 128 ms                                                       | 132 ms: 1.03x slower                                                               |
| regex_effbot               | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                                              |
| pprint_pformat             | 1.65 sec                                                     | 1.70 sec: 1.03x slower                                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.83 ms: 1.03x slower                                                              |
| bench_thread_pool          | 950 us                                                       | 979 us: 1.03x slower                                                               |
| pprint_safe_repr           | 807 ms                                                       | 833 ms: 1.03x slower                                                               |
| sympy_integrate            | 23.9 ms                                                      | 24.7 ms: 1.03x slower                                                              |
| logging_silent             | 94.4 ns                                                      | 97.4 ns: 1.03x slower                                                              |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.03x slower                                                               |
| pathlib                    | 18.9 ms                                                      | 19.6 ms: 1.04x slower                                                              |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                              |
| async_tree_io              | 1.04 sec                                                     | 1.08 sec: 1.04x slower                                                             |
| chaos                      | 64.0 ms                                                      | 66.6 ms: 1.04x slower                                                              |
| dask                       | 392 ms                                                       | 408 ms: 1.04x slower                                                               |
| regex_dna                  | 239 ms                                                       | 252 ms: 1.06x slower                                                               |
| tornado_http               | 121 ms                                                       | 128 ms: 1.06x slower                                                               |
| scimark_fft                | 301 ms                                                       | 319 ms: 1.06x slower                                                               |
| sympy_expand               | 484 ms                                                       | 514 ms: 1.06x slower                                                               |
| json                       | 5.12 ms                                                      | 5.45 ms: 1.06x slower                                                              |
| 2to3                       | 285 ms                                                       | 304 ms: 1.07x slower                                                               |
| dulwich_log                | 65.4 ms                                                      | 69.9 ms: 1.07x slower                                                              |
| gunicorn                   | 1.00 ms                                                      | 1.08 ms: 1.08x slower                                                              |
| nbody                      | 88.0 ms                                                      | 95.5 ms: 1.09x slower                                                              |
| regex_v8                   | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                              |
| scimark_monte_carlo        | 69.0 ms                                                      | 75.1 ms: 1.09x slower                                                              |
| sqlglot_optimize           | 57.5 ms                                                      | 62.7 ms: 1.09x slower                                                              |
| pycparser                  | 1.23 sec                                                     | 1.35 sec: 1.09x slower                                                             |
| fannkuch                   | 350 ms                                                       | 383 ms: 1.09x slower                                                               |
| richards_super             | 51.3 ms                                                      | 56.3 ms: 1.10x slower                                                              |
| aiohttp                    | 1.02 ms                                                      | 1.12 ms: 1.10x slower                                                              |
| richards                   | 45.7 ms                                                      | 50.4 ms: 1.10x slower                                                              |
| mypy2                      | 830 ms                                                       | 919 ms: 1.11x slower                                                               |
| unpickle_pure_python       | 210 us                                                       | 232 us: 1.11x slower                                                               |
| nqueens                    | 89.9 ms                                                      | 101 ms: 1.13x slower                                                               |
| go                         | 150 ms                                                       | 172 ms: 1.15x slower                                                               |
| deltablue                  | 3.24 ms                                                      | 3.74 ms: 1.16x slower                                                              |
| telco                      | 6.96 ms                                                      | 8.12 ms: 1.17x slower                                                              |
| pyflate                    | 439 ms                                                       | 515 ms: 1.17x slower                                                               |
| unpack_sequence            | 53.2 ns                                                      | 62.6 ns: 1.18x slower                                                              |
| coverage                   | 66.7 ms                                                      | 79.0 ms: 1.19x slower                                                              |
| hexiom                     | 5.96 ms                                                      | 7.19 ms: 1.21x slower                                                              |
| python_startup             | 11.6 ms                                                      | 14.4 ms: 1.24x slower                                                              |
| scimark_lu                 | 98.8 ms                                                      | 125 ms: 1.26x slower                                                               |
| scimark_sor                | 109 ms                                                       | 152 ms: 1.39x slower                                                               |
| python_startup_no_site     | 8.64 ms                                                      | 12.8 ms: 1.48x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                       |

Benchmark hidden because not significant (10): xml_etree_parse, asyncio_tcp_ssl, deepcopy, asyncio_websockets, mdp, unpickle, gc_traversal, async_tree_memoization, async_tree_cpu_io_mixed, bench_mp_pool
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240318-3.13.0a5+-c8d6017-JIT/bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x


# Memory

- memory change: 1.11x