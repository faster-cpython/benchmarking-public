# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-amd64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.03x faster
- HPT reliability: 92.79%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 227 ms: 1.10x slower                                                      |
| docutils       | 1.63 sec                                                        | 1.73 sec: 1.07x slower                                                    |
| html5lib       | 35.0 ms                                                         | 36.4 ms: 1.04x slower                                                     |
| tornado_http   | 81.8 ms                                                         | 83.1 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                           | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg       | 605 ms                                                          | 594 ms: 1.02x faster                                                      |
| async_tree_none        | 218 ms                                                          | 223 ms: 1.02x slower                                                      |
| async_tree_memoization | 264 ms                                                          | 272 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                              |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.5 ms: 1.31x faster                                                     |
| float          | 49.7 ms                                                         | 44.4 ms: 1.12x faster                                                     |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                           | 1.14x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 115 ms: 1.03x faster                                                      |
| regex_effbot   | 1.58 ms                                                         | 1.56 ms: 1.02x faster                                                     |
| regex_compile  | 78.0 ms                                                         | 85.8 ms: 1.10x slower                                                     |
| regex_v8       | 15.8 ms                                                         | 18.9 ms: 1.20x slower                                                     |
| Geometric mean | (ref)                                                           | 1.06x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.18 sec: 1.15x faster                                                    |
| xml_etree_iterparse  | 62.3 ms                                                         | 59.6 ms: 1.05x faster                                                     |
| pickle_pure_python   | 175 us                                                          | 168 us: 1.04x faster                                                      |
| pickle_list          | 2.90 us                                                         | 2.82 us: 1.03x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 51.7 ms: 1.03x faster                                                     |
| pickle_dict          | 18.1 us                                                         | 17.9 us: 1.01x faster                                                     |
| xml_etree_process    | 36.4 ms                                                         | 36.1 ms: 1.01x faster                                                     |
| json_loads           | 14.2 us                                                         | 14.1 us: 1.01x faster                                                     |
| pickle               | 7.11 us                                                         | 7.20 us: 1.01x slower                                                     |
| json_dumps           | 5.61 ms                                                         | 5.69 ms: 1.01x slower                                                     |
| unpickle_pure_python | 122 us                                                          | 125 us: 1.02x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.78 us: 1.05x slower                                                     |
| unpickle_list        | 2.62 us                                                         | 2.88 us: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.28 ms: 1.20x faster                                                     |
| django_template | 21.7 ms                                                         | 24.0 ms: 1.11x slower                                                     |
| genshi_text     | 14.4 ms                                                         | 17.3 ms: 1.21x slower                                                     |
| genshi_xml      | 31.6 ms                                                         | 42.4 ms: 1.34x slower                                                     |
| Geometric mean  | (ref)                                                           | 1.10x slower                                                              |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 491 us: 16.50x faster                                                     |
| deepcopy_memo            | 22.1 us                                                         | 15.4 us: 1.44x faster                                                     |
| spectral_norm            | 63.7 ms                                                         | 45.7 ms: 1.40x faster                                                     |
| nbody                    | 67.6 ms                                                         | 51.5 ms: 1.31x faster                                                     |
| deepcopy                 | 220 us                                                          | 169 us: 1.30x faster                                                      |
| mako                     | 6.36 ms                                                         | 5.28 ms: 1.20x faster                                                     |
| deepcopy_reduce          | 1.99 us                                                         | 1.72 us: 1.16x faster                                                     |
| tomli_loads              | 1.35 sec                                                        | 1.18 sec: 1.15x faster                                                    |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.19 ms: 1.14x faster                                                     |
| scimark_fft              | 171 ms                                                          | 151 ms: 1.13x faster                                                      |
| float                    | 49.7 ms                                                         | 44.4 ms: 1.12x faster                                                     |
| crypto_pyaes             | 45.5 ms                                                         | 40.8 ms: 1.11x faster                                                     |
| pyflate                  | 279 ms                                                          | 256 ms: 1.09x faster                                                      |
| json                     | 3.19 ms                                                         | 2.94 ms: 1.09x faster                                                     |
| fannkuch                 | 243 ms                                                          | 225 ms: 1.08x faster                                                      |
| logging_simple           | 5.78 us                                                         | 5.46 us: 1.06x faster                                                     |
| scimark_monte_carlo      | 39.1 ms                                                         | 37.2 ms: 1.05x faster                                                     |
| logging_format           | 6.22 us                                                         | 5.92 us: 1.05x faster                                                     |
| xml_etree_iterparse      | 62.3 ms                                                         | 59.6 ms: 1.05x faster                                                     |
| telco                    | 4.67 ms                                                         | 4.47 ms: 1.05x faster                                                     |
| pprint_safe_repr         | 474 ms                                                          | 454 ms: 1.04x faster                                                      |
| pickle_pure_python       | 175 us                                                          | 168 us: 1.04x faster                                                      |
| pprint_pformat           | 966 ms                                                          | 930 ms: 1.04x faster                                                      |
| regex_dna                | 119 ms                                                          | 115 ms: 1.03x faster                                                      |
| pickle_list              | 2.90 us                                                         | 2.82 us: 1.03x faster                                                     |
| xml_etree_generate       | 53.2 ms                                                         | 51.7 ms: 1.03x faster                                                     |
| async_tree_io_tg         | 605 ms                                                          | 594 ms: 1.02x faster                                                      |
| regex_effbot             | 1.58 ms                                                         | 1.56 ms: 1.02x faster                                                     |
| pickle_dict              | 18.1 us                                                         | 17.9 us: 1.01x faster                                                     |
| pathlib                  | 75.9 ms                                                         | 74.9 ms: 1.01x faster                                                     |
| xml_etree_process        | 36.4 ms                                                         | 36.1 ms: 1.01x faster                                                     |
| sqlite_synth             | 1.60 us                                                         | 1.59 us: 1.01x faster                                                     |
| json_loads               | 14.2 us                                                         | 14.1 us: 1.01x faster                                                     |
| pidigits                 | 150 ms                                                          | 149 ms: 1.00x faster                                                      |
| gc_traversal             | 1.55 ms                                                         | 1.56 ms: 1.01x slower                                                     |
| pickle                   | 7.11 us                                                         | 7.20 us: 1.01x slower                                                     |
| json_dumps               | 5.61 ms                                                         | 5.69 ms: 1.01x slower                                                     |
| tornado_http             | 81.8 ms                                                         | 83.1 ms: 1.02x slower                                                     |
| generators               | 19.6 ms                                                         | 19.9 ms: 1.02x slower                                                     |
| create_gc_cycles         | 888 us                                                          | 905 us: 1.02x slower                                                      |
| chaos                    | 38.4 ms                                                         | 39.1 ms: 1.02x slower                                                     |
| unpickle_pure_python     | 122 us                                                          | 125 us: 1.02x slower                                                      |
| async_tree_none          | 218 ms                                                          | 223 ms: 1.02x slower                                                      |
| python_startup_no_site   | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                     |
| async_tree_memoization   | 264 ms                                                          | 272 ms: 1.03x slower                                                      |
| sqlglot_parse            | 748 us                                                          | 771 us: 1.03x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 72.1 ms: 1.03x slower                                                     |
| html5lib                 | 35.0 ms                                                         | 36.4 ms: 1.04x slower                                                     |
| sqlglot_transpile        | 955 us                                                          | 998 us: 1.05x slower                                                      |
| unpickle                 | 8.40 us                                                         | 8.78 us: 1.05x slower                                                     |
| raytrace                 | 162 ms                                                          | 170 ms: 1.05x slower                                                      |
| richards                 | 26.7 ms                                                         | 28.1 ms: 1.05x slower                                                     |
| richards_super           | 30.2 ms                                                         | 31.8 ms: 1.05x slower                                                     |
| coverage                 | 42.1 ms                                                         | 44.5 ms: 1.06x slower                                                     |
| nqueens                  | 56.7 ms                                                         | 60.0 ms: 1.06x slower                                                     |
| bench_mp_pool            | 64.8 ms                                                         | 68.6 ms: 1.06x slower                                                     |
| docutils                 | 1.63 sec                                                        | 1.73 sec: 1.07x slower                                                    |
| sqlglot_optimize         | 32.7 ms                                                         | 35.0 ms: 1.07x slower                                                     |
| typing_runtime_protocols | 101 us                                                          | 108 us: 1.07x slower                                                      |
| sympy_sum                | 84.4 ms                                                         | 90.8 ms: 1.08x slower                                                     |
| go                       | 82.1 ms                                                         | 88.6 ms: 1.08x slower                                                     |
| scimark_sor              | 75.3 ms                                                         | 81.7 ms: 1.08x slower                                                     |
| sympy_str                | 159 ms                                                          | 173 ms: 1.09x slower                                                      |
| pycparser                | 754 ms                                                          | 825 ms: 1.09x slower                                                      |
| mdp                      | 1.31 sec                                                        | 1.44 sec: 1.10x slower                                                    |
| 2to3                     | 207 ms                                                          | 227 ms: 1.10x slower                                                      |
| sympy_expand             | 271 ms                                                          | 297 ms: 1.10x slower                                                      |
| regex_compile            | 78.0 ms                                                         | 85.8 ms: 1.10x slower                                                     |
| unpickle_list            | 2.62 us                                                         | 2.88 us: 1.10x slower                                                     |
| django_template          | 21.7 ms                                                         | 24.0 ms: 1.11x slower                                                     |
| async_generators         | 223 ms                                                          | 248 ms: 1.11x slower                                                      |
| sympy_integrate          | 12.2 ms                                                         | 13.6 ms: 1.11x slower                                                     |
| deltablue                | 1.88 ms                                                         | 2.10 ms: 1.11x slower                                                     |
| pylint                   | 205 ms                                                          | 230 ms: 1.12x slower                                                      |
| regex_v8                 | 15.8 ms                                                         | 18.9 ms: 1.20x slower                                                     |
| genshi_text              | 14.4 ms                                                         | 17.3 ms: 1.21x slower                                                     |
| scimark_lu               | 56.6 ms                                                         | 69.3 ms: 1.22x slower                                                     |
| hexiom                   | 3.72 ms                                                         | 4.62 ms: 1.24x slower                                                     |
| genshi_xml               | 31.6 ms                                                         | 42.4 ms: 1.34x slower                                                     |
| Geometric mean           | (ref)                                                           | 1.03x faster                                                              |

Benchmark hidden because not significant (13): asyncio_tcp_ssl, async_tree_memoization_tg, asyncio_tcp, comprehensions, async_tree_cpu_io_mixed_tg, coroutines, async_tree_none_tg, logging_silent, xml_etree_parse, python_startup, bench_thread_pool, async_tree_cpu_io_mixed, async_tree_io
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 92.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown