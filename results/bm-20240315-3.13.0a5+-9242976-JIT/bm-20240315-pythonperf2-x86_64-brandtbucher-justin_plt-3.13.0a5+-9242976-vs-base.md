# Results vs. base

- fork: brandtbucher
- ref: justin_plt
- machine: linux-x86_64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.01x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 307 ms                                                                       | 308 ms: 1.01x slower                                                     |
| chameleon      | 7.41 ms                                                                      | 7.33 ms: 1.01x faster                                                    |
| docutils       | 2.92 sec                                                                     | 2.96 sec: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 709 ms                                                                       | 701 ms: 1.01x faster                                                     |
| async_tree_none_tg      | 438 ms                                                                       | 435 ms: 1.01x faster                                                     |
| Geometric mean          | (ref)                                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (6): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 261 ms                                                                       | 262 ms: 1.00x slower                                                     |
| float          | 78.7 ms                                                                      | 79.2 ms: 1.01x slower                                                    |
| nbody          | 94.5 ms                                                                      | 103 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                        | 1.03x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 253 ms                                                                       | 236 ms: 1.07x faster                                                     |
| regex_effbot   | 3.56 ms                                                                      | 3.54 ms: 1.01x faster                                                    |
| regex_v8       | 25.5 ms                                                                      | 25.9 ms: 1.01x slower                                                    |
| regex_compile  | 146 ms                                                                       | 152 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_list        | 4.60 us                                                                      | 4.57 us: 1.01x faster                                                    |
| xml_etree_generate   | 86.0 ms                                                                      | 85.5 ms: 1.01x faster                                                    |
| pickle_pure_python   | 310 us                                                                       | 316 us: 1.02x slower                                                     |
| unpickle             | 14.9 us                                                                      | 15.2 us: 1.02x slower                                                    |
| unpickle_pure_python | 234 us                                                                       | 241 us: 1.03x slower                                                     |
| pickle_list          | 4.30 us                                                                      | 4.45 us: 1.03x slower                                                    |
| pickle               | 10.3 us                                                                      | 10.7 us: 1.03x slower                                                    |
| pickle_dict          | 30.5 us                                                                      | 32.5 us: 1.06x slower                                                    |
| tomli_loads          | 2.14 sec                                                                     | 2.34 sec: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                        | 1.02x slower                                                             |

Benchmark hidden because not significant (5): xml_etree_parse, json_dumps, json_loads, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 14.1 ms                                                                      | 12.6 ms: 1.11x faster                                                    |
| python_startup         | 15.6 ms                                                                      | 14.2 ms: 1.10x faster                                                    |
| Geometric mean         | (ref)                                                                        | 1.11x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                                      | 38.4 ms: 1.03x faster                                                    |
| genshi_text     | 28.2 ms                                                                      | 28.5 ms: 1.01x slower                                                    |
| genshi_xml      | 60.6 ms                                                                      | 61.9 ms: 1.02x slower                                                    |
| mako            | 9.75 ms                                                                      | 10.3 ms: 1.05x slower                                                    |
| Geometric mean  | (ref)                                                                        | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|--------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| bench_mp_pool            | 7.02 ms                                                                      | 4.77 ms: 1.47x faster                                                    |
| python_startup_no_site   | 14.1 ms                                                                      | 12.6 ms: 1.11x faster                                                    |
| python_startup           | 15.6 ms                                                                      | 14.2 ms: 1.10x faster                                                    |
| regex_dna                | 253 ms                                                                       | 236 ms: 1.07x faster                                                     |
| sqlglot_normalize        | 128 ms                                                                       | 120 ms: 1.07x faster                                                     |
| logging_format           | 7.49 us                                                                      | 7.28 us: 1.03x faster                                                    |
| django_template          | 39.4 ms                                                                      | 38.4 ms: 1.03x faster                                                    |
| raytrace                 | 312 ms                                                                       | 306 ms: 1.02x faster                                                     |
| logging_simple           | 6.76 us                                                                      | 6.66 us: 1.02x faster                                                    |
| async_tree_cpu_io_mixed  | 709 ms                                                                       | 701 ms: 1.01x faster                                                     |
| chameleon                | 7.41 ms                                                                      | 7.33 ms: 1.01x faster                                                    |
| asyncio_tcp              | 376 ms                                                                       | 373 ms: 1.01x faster                                                     |
| async_tree_none_tg       | 438 ms                                                                       | 435 ms: 1.01x faster                                                     |
| unpickle_list            | 4.60 us                                                                      | 4.57 us: 1.01x faster                                                    |
| gunicorn                 | 1.09 ms                                                                      | 1.08 ms: 1.01x faster                                                    |
| deepcopy_memo            | 37.6 us                                                                      | 37.4 us: 1.01x faster                                                    |
| xml_etree_generate       | 86.0 ms                                                                      | 85.5 ms: 1.01x faster                                                    |
| aiohttp                  | 1.12 ms                                                                      | 1.11 ms: 1.01x faster                                                    |
| logging_silent           | 98.0 ns                                                                      | 97.5 ns: 1.01x faster                                                    |
| regex_effbot             | 3.56 ms                                                                      | 3.54 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl          | 1.58 sec                                                                     | 1.58 sec: 1.00x faster                                                   |
| pidigits                 | 261 ms                                                                       | 262 ms: 1.00x slower                                                     |
| mdp                      | 2.60 sec                                                                     | 2.61 sec: 1.00x slower                                                   |
| 2to3                     | 307 ms                                                                       | 308 ms: 1.01x slower                                                     |
| float                    | 78.7 ms                                                                      | 79.2 ms: 1.01x slower                                                    |
| pathlib                  | 19.4 ms                                                                      | 19.6 ms: 1.01x slower                                                    |
| sympy_str                | 302 ms                                                                       | 305 ms: 1.01x slower                                                     |
| go                       | 174 ms                                                                       | 175 ms: 1.01x slower                                                     |
| sqlglot_parse            | 1.43 ms                                                                      | 1.44 ms: 1.01x slower                                                    |
| genshi_text              | 28.2 ms                                                                      | 28.5 ms: 1.01x slower                                                    |
| generators               | 33.9 ms                                                                      | 34.2 ms: 1.01x slower                                                    |
| meteor_contest           | 131 ms                                                                       | 133 ms: 1.01x slower                                                     |
| sympy_expand             | 511 ms                                                                       | 517 ms: 1.01x slower                                                     |
| sympy_sum                | 160 ms                                                                       | 162 ms: 1.01x slower                                                     |
| docutils                 | 2.92 sec                                                                     | 2.96 sec: 1.01x slower                                                   |
| sqlglot_transpile        | 1.85 ms                                                                      | 1.88 ms: 1.01x slower                                                    |
| coroutines               | 22.4 ms                                                                      | 22.8 ms: 1.01x slower                                                    |
| regex_v8                 | 25.5 ms                                                                      | 25.9 ms: 1.01x slower                                                    |
| create_gc_cycles         | 1.58 ms                                                                      | 1.60 ms: 1.02x slower                                                    |
| crypto_pyaes             | 77.8 ms                                                                      | 79.1 ms: 1.02x slower                                                    |
| sqlite_synth             | 2.69 us                                                                      | 2.73 us: 1.02x slower                                                    |
| comprehensions           | 19.0 us                                                                      | 19.3 us: 1.02x slower                                                    |
| pickle_pure_python       | 310 us                                                                       | 316 us: 1.02x slower                                                     |
| deepcopy                 | 370 us                                                                       | 378 us: 1.02x slower                                                     |
| unpickle                 | 14.9 us                                                                      | 15.2 us: 1.02x slower                                                    |
| richards                 | 50.5 ms                                                                      | 51.5 ms: 1.02x slower                                                    |
| sympy_integrate          | 24.6 ms                                                                      | 25.1 ms: 1.02x slower                                                    |
| telco                    | 8.13 ms                                                                      | 8.30 ms: 1.02x slower                                                    |
| typing_runtime_protocols | 117 us                                                                       | 120 us: 1.02x slower                                                     |
| genshi_xml               | 60.6 ms                                                                      | 61.9 ms: 1.02x slower                                                    |
| pyflate                  | 524 ms                                                                       | 536 ms: 1.02x slower                                                     |
| richards_super           | 56.2 ms                                                                      | 57.6 ms: 1.02x slower                                                    |
| unpickle_pure_python     | 234 us                                                                       | 241 us: 1.03x slower                                                     |
| scimark_sor              | 152 ms                                                                       | 156 ms: 1.03x slower                                                     |
| async_generators         | 384 ms                                                                       | 395 ms: 1.03x slower                                                     |
| pickle_list              | 4.30 us                                                                      | 4.45 us: 1.03x slower                                                    |
| chaos                    | 67.6 ms                                                                      | 69.9 ms: 1.03x slower                                                    |
| pickle                   | 10.3 us                                                                      | 10.7 us: 1.03x slower                                                    |
| regex_compile            | 146 ms                                                                       | 152 ms: 1.04x slower                                                     |
| pycparser                | 1.31 sec                                                                     | 1.37 sec: 1.04x slower                                                   |
| nqueens                  | 102 ms                                                                       | 106 ms: 1.04x slower                                                     |
| pprint_pformat           | 1.72 sec                                                                     | 1.80 sec: 1.05x slower                                                   |
| mako                     | 9.75 ms                                                                      | 10.3 ms: 1.05x slower                                                    |
| pprint_safe_repr         | 836 ms                                                                       | 883 ms: 1.06x slower                                                     |
| hexiom                   | 7.25 ms                                                                      | 7.68 ms: 1.06x slower                                                    |
| pickle_dict              | 30.5 us                                                                      | 32.5 us: 1.06x slower                                                    |
| spectral_norm            | 94.4 ms                                                                      | 101 ms: 1.06x slower                                                     |
| scimark_monte_carlo      | 76.2 ms                                                                      | 81.4 ms: 1.07x slower                                                    |
| scimark_fft              | 325 ms                                                                       | 353 ms: 1.09x slower                                                     |
| scimark_sparse_mat_mult  | 4.19 ms                                                                      | 4.56 ms: 1.09x slower                                                    |
| tomli_loads              | 2.14 sec                                                                     | 2.34 sec: 1.09x slower                                                   |
| nbody                    | 94.5 ms                                                                      | 103 ms: 1.09x slower                                                     |
| scimark_lu               | 122 ms                                                                       | 134 ms: 1.10x slower                                                     |
| fannkuch                 | 396 ms                                                                       | 448 ms: 1.13x slower                                                     |
| unpack_sequence          | 62.2 ns                                                                      | 80.1 ns: 1.29x slower                                                    |
| Geometric mean           | (ref)                                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (26): async_tree_none, async_tree_cpu_io_mixed_tg, json, async_tree_memoization, tornado_http, thrift, deltablue, async_tree_memoization_tg, coverage, dask, xml_etree_parse, json_dumps, gc_traversal, asyncio_websockets, async_tree_io, async_tree_io_tg, html5lib, json_loads, dulwich_log, sqlglot_optimize, xml_etree_process, xml_etree_iterparse, deepcopy_reduce, mypy2, bench_thread_pool, pylint


# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 0.92x