# Results vs. base

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: linux-x86_64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.01x faster
- HPT reliability: 99.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 307 ms                                                                       | 304 ms: 1.01x faster                                                               |
| chameleon      | 7.41 ms                                                                      | 7.30 ms: 1.02x faster                                                              |
| docutils       | 2.92 sec                                                                     | 2.93 sec: 1.00x slower                                                             |
| tornado_http   | 126 ms                                                                       | 128 ms: 1.02x slower                                                               |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_none_tg      | 438 ms                                                                       | 433 ms: 1.01x faster                                                               |
| async_tree_cpu_io_mixed | 709 ms                                                                       | 702 ms: 1.01x faster                                                               |
| async_tree_io           | 1.09 sec                                                                     | 1.08 sec: 1.01x faster                                                             |
| async_tree_io_tg        | 1.09 sec                                                                     | 1.08 sec: 1.01x faster                                                             |
| Geometric mean          | (ref)                                                                        | 1.01x faster                                                                       |

Benchmark hidden because not significant (4): async_tree_none, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_dna      | 253 ms                                                                       | 252 ms: 1.00x faster                                                               |
| regex_v8       | 25.5 ms                                                                      | 25.7 ms: 1.01x slower                                                              |
| regex_effbot   | 3.56 ms                                                                      | 3.67 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.0 ms                                                                      | 84.2 ms: 1.02x faster                                                              |
| xml_etree_iterparse  | 104 ms                                                                       | 102 ms: 1.02x faster                                                               |
| xml_etree_parse      | 146 ms                                                                       | 143 ms: 1.02x faster                                                               |
| json_loads           | 25.0 us                                                                      | 24.6 us: 1.01x faster                                                              |
| pickle               | 10.3 us                                                                      | 10.2 us: 1.01x faster                                                              |
| unpickle_pure_python | 234 us                                                                       | 232 us: 1.01x faster                                                               |
| pickle_dict          | 30.5 us                                                                      | 30.4 us: 1.01x faster                                                              |
| tomli_loads          | 2.14 sec                                                                     | 2.18 sec: 1.02x slower                                                             |
| pickle_list          | 4.30 us                                                                      | 4.50 us: 1.04x slower                                                              |
| Geometric mean       | (ref)                                                                        | 1.00x faster                                                                       |

Benchmark hidden because not significant (5): unpickle_list, unpickle, pickle_pure_python, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 14.1 ms                                                                      | 12.8 ms: 1.10x faster                                                              |
| python_startup         | 15.6 ms                                                                      | 14.4 ms: 1.08x faster                                                              |
| Geometric mean         | (ref)                                                                        | 1.09x faster                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                                      | 58.6 ms: 1.03x faster                                                              |
| django_template | 39.4 ms                                                                      | 38.5 ms: 1.02x faster                                                              |
| genshi_text     | 28.2 ms                                                                      | 27.9 ms: 1.01x faster                                                              |
| mako            | 9.75 ms                                                                      | 9.92 ms: 1.02x slower                                                              |
| Geometric mean  | (ref)                                                                        | 1.01x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|--------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| bench_mp_pool            | 7.02 ms                                                                      | 4.87 ms: 1.44x faster                                                              |
| gc_traversal             | 3.92 ms                                                                      | 3.48 ms: 1.13x faster                                                              |
| python_startup_no_site   | 14.1 ms                                                                      | 12.8 ms: 1.10x faster                                                              |
| python_startup           | 15.6 ms                                                                      | 14.4 ms: 1.08x faster                                                              |
| sqlglot_normalize        | 128 ms                                                                       | 120 ms: 1.07x faster                                                               |
| fannkuch                 | 396 ms                                                                       | 383 ms: 1.03x faster                                                               |
| genshi_xml               | 60.6 ms                                                                      | 58.6 ms: 1.03x faster                                                              |
| django_template          | 39.4 ms                                                                      | 38.5 ms: 1.02x faster                                                              |
| raytrace                 | 312 ms                                                                       | 305 ms: 1.02x faster                                                               |
| xml_etree_generate       | 86.0 ms                                                                      | 84.2 ms: 1.02x faster                                                              |
| xml_etree_iterparse      | 104 ms                                                                       | 102 ms: 1.02x faster                                                               |
| create_gc_cycles         | 1.58 ms                                                                      | 1.55 ms: 1.02x faster                                                              |
| xml_etree_parse          | 146 ms                                                                       | 143 ms: 1.02x faster                                                               |
| pyflate                  | 524 ms                                                                       | 515 ms: 1.02x faster                                                               |
| scimark_fft              | 325 ms                                                                       | 319 ms: 1.02x faster                                                               |
| sqlglot_parse            | 1.43 ms                                                                      | 1.40 ms: 1.02x faster                                                              |
| chaos                    | 67.6 ms                                                                      | 66.6 ms: 1.02x faster                                                              |
| coverage                 | 80.3 ms                                                                      | 79.0 ms: 1.02x faster                                                              |
| chameleon                | 7.41 ms                                                                      | 7.30 ms: 1.02x faster                                                              |
| scimark_monte_carlo      | 76.2 ms                                                                      | 75.1 ms: 1.01x faster                                                              |
| json_loads               | 25.0 us                                                                      | 24.6 us: 1.01x faster                                                              |
| sqlglot_transpile        | 1.85 ms                                                                      | 1.83 ms: 1.01x faster                                                              |
| pickle                   | 10.3 us                                                                      | 10.2 us: 1.01x faster                                                              |
| async_tree_none_tg       | 438 ms                                                                       | 433 ms: 1.01x faster                                                               |
| genshi_text              | 28.2 ms                                                                      | 27.9 ms: 1.01x faster                                                              |
| comprehensions           | 19.0 us                                                                      | 18.8 us: 1.01x faster                                                              |
| asyncio_tcp              | 376 ms                                                                       | 372 ms: 1.01x faster                                                               |
| deepcopy_memo            | 37.6 us                                                                      | 37.1 us: 1.01x faster                                                              |
| async_tree_cpu_io_mixed  | 709 ms                                                                       | 702 ms: 1.01x faster                                                               |
| sqlglot_optimize         | 63.3 ms                                                                      | 62.7 ms: 1.01x faster                                                              |
| mdp                      | 2.60 sec                                                                     | 2.57 sec: 1.01x faster                                                             |
| generators               | 33.9 ms                                                                      | 33.5 ms: 1.01x faster                                                              |
| go                       | 174 ms                                                                       | 172 ms: 1.01x faster                                                               |
| async_tree_io            | 1.09 sec                                                                     | 1.08 sec: 1.01x faster                                                             |
| hexiom                   | 7.25 ms                                                                      | 7.19 ms: 1.01x faster                                                              |
| async_tree_io_tg         | 1.09 sec                                                                     | 1.08 sec: 1.01x faster                                                             |
| unpickle_pure_python     | 234 us                                                                       | 232 us: 1.01x faster                                                               |
| spectral_norm            | 94.4 ms                                                                      | 93.7 ms: 1.01x faster                                                              |
| pprint_pformat           | 1.72 sec                                                                     | 1.70 sec: 1.01x faster                                                             |
| 2to3                     | 307 ms                                                                       | 304 ms: 1.01x faster                                                               |
| gunicorn                 | 1.09 ms                                                                      | 1.08 ms: 1.01x faster                                                              |
| nqueens                  | 102 ms                                                                       | 101 ms: 1.01x faster                                                               |
| pickle_dict              | 30.5 us                                                                      | 30.4 us: 1.01x faster                                                              |
| logging_silent           | 98.0 ns                                                                      | 97.4 ns: 1.01x faster                                                              |
| deepcopy                 | 370 us                                                                       | 368 us: 1.01x faster                                                               |
| deltablue                | 3.76 ms                                                                      | 3.74 ms: 1.01x faster                                                              |
| crypto_pyaes             | 77.8 ms                                                                      | 77.4 ms: 1.00x faster                                                              |
| regex_dna                | 253 ms                                                                       | 252 ms: 1.00x faster                                                               |
| pprint_safe_repr         | 836 ms                                                                       | 833 ms: 1.00x faster                                                               |
| meteor_contest           | 131 ms                                                                       | 132 ms: 1.00x slower                                                               |
| sympy_integrate          | 24.6 ms                                                                      | 24.7 ms: 1.00x slower                                                              |
| docutils                 | 2.92 sec                                                                     | 2.93 sec: 1.00x slower                                                             |
| sympy_sum                | 160 ms                                                                       | 161 ms: 1.01x slower                                                               |
| unpack_sequence          | 62.2 ns                                                                      | 62.6 ns: 1.01x slower                                                              |
| sympy_expand             | 511 ms                                                                       | 514 ms: 1.01x slower                                                               |
| regex_v8                 | 25.5 ms                                                                      | 25.7 ms: 1.01x slower                                                              |
| sqlite_synth             | 2.69 us                                                                      | 2.70 us: 1.01x slower                                                              |
| sympy_str                | 302 ms                                                                       | 305 ms: 1.01x slower                                                               |
| logging_format           | 7.49 us                                                                      | 7.55 us: 1.01x slower                                                              |
| pathlib                  | 19.4 ms                                                                      | 19.6 ms: 1.01x slower                                                              |
| async_generators         | 384 ms                                                                       | 388 ms: 1.01x slower                                                               |
| scimark_sparse_mat_mult  | 4.19 ms                                                                      | 4.25 ms: 1.02x slower                                                              |
| mako                     | 9.75 ms                                                                      | 9.92 ms: 1.02x slower                                                              |
| tomli_loads              | 2.14 sec                                                                     | 2.18 sec: 1.02x slower                                                             |
| dulwich_log              | 68.7 ms                                                                      | 69.9 ms: 1.02x slower                                                              |
| thrift                   | 862 us                                                                       | 879 us: 1.02x slower                                                               |
| tornado_http             | 126 ms                                                                       | 128 ms: 1.02x slower                                                               |
| scimark_lu               | 122 ms                                                                       | 125 ms: 1.02x slower                                                               |
| pycparser                | 1.31 sec                                                                     | 1.35 sec: 1.03x slower                                                             |
| regex_effbot             | 3.56 ms                                                                      | 3.67 ms: 1.03x slower                                                              |
| typing_runtime_protocols | 117 us                                                                       | 121 us: 1.04x slower                                                               |
| pickle_list              | 4.30 us                                                                      | 4.50 us: 1.04x slower                                                              |
| Geometric mean           | (ref)                                                                        | 1.01x faster                                                                       |

Benchmark hidden because not significant (29): async_tree_none, html5lib, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, deepcopy_reduce, unpickle_list, unpickle, pickle_pure_python, richards, scimark_sor, coroutines, aiohttp, telco, float, pidigits, xml_etree_process, json_dumps, asyncio_tcp_ssl, richards_super, asyncio_websockets, regex_compile, logging_simple, pylint, mypy2, dask, bench_thread_pool, json, nbody


# HPT report

- Reliability score: 99.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.00x