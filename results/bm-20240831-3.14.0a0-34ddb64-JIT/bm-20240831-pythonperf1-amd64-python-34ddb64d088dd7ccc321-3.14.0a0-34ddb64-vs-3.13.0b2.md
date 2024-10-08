# Results vs. 3.13.0b2

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-amd64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.02x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 243 ms: 1.17x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.94 sec: 1.19x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.8 ms: 1.22x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 99.1 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                           | 1.20x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg       | 605 ms                                                          | 559 ms: 1.08x faster                                                       |
| async_tree_none        | 218 ms                                                          | 206 ms: 1.06x faster                                                       |
| async_tree_memoization | 264 ms                                                          | 251 ms: 1.05x faster                                                       |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 50.0 ms: 1.35x faster                                                      |
| float          | 49.7 ms                                                         | 45.3 ms: 1.10x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                           | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                      |
| regex_dna      | 119 ms                                                          | 124 ms: 1.04x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 95.6 ms: 1.23x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.27 sec: 1.06x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 50.5 ms: 1.05x faster                                                      |
| xml_etree_process    | 36.4 ms                                                         | 35.8 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.7 ms: 1.01x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.78 ms: 1.03x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 94.0 ms: 1.03x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 195 us: 1.11x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 145 us: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.6 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.26 ms: 1.21x faster                                                      |
| django_template | 21.7 ms                                                         | 26.8 ms: 1.24x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 19.7 ms: 1.37x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 46.3 ms: 1.46x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.20x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 519 us: 15.61x faster                                                      |
| deepcopy_memo            | 22.1 us                                                         | 15.0 us: 1.47x faster                                                      |
| spectral_norm            | 63.7 ms                                                         | 44.1 ms: 1.45x faster                                                      |
| nbody                    | 67.6 ms                                                         | 50.0 ms: 1.35x faster                                                      |
| scimark_sor              | 75.3 ms                                                         | 60.5 ms: 1.24x faster                                                      |
| mako                     | 6.36 ms                                                         | 5.26 ms: 1.21x faster                                                      |
| deepcopy                 | 220 us                                                          | 183 us: 1.20x faster                                                       |
| crypto_pyaes             | 45.5 ms                                                         | 38.2 ms: 1.19x faster                                                      |
| scimark_fft              | 171 ms                                                          | 149 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.18 ms: 1.14x faster                                                      |
| deepcopy_reduce          | 1.99 us                                                         | 1.81 us: 1.10x faster                                                      |
| float                    | 49.7 ms                                                         | 45.3 ms: 1.10x faster                                                      |
| json                     | 3.19 ms                                                         | 2.93 ms: 1.09x faster                                                      |
| async_tree_io_tg         | 605 ms                                                          | 559 ms: 1.08x faster                                                       |
| pyflate                  | 279 ms                                                          | 262 ms: 1.06x faster                                                       |
| tomli_loads              | 1.35 sec                                                        | 1.27 sec: 1.06x faster                                                     |
| async_tree_none          | 218 ms                                                          | 206 ms: 1.06x faster                                                       |
| xml_etree_generate       | 53.2 ms                                                         | 50.5 ms: 1.05x faster                                                      |
| async_tree_memoization   | 264 ms                                                          | 251 ms: 1.05x faster                                                       |
| scimark_lu               | 56.6 ms                                                         | 54.0 ms: 1.05x faster                                                      |
| deltablue                | 1.88 ms                                                         | 1.82 ms: 1.03x faster                                                      |
| fannkuch                 | 243 ms                                                          | 239 ms: 1.02x faster                                                       |
| telco                    | 4.67 ms                                                         | 4.58 ms: 1.02x faster                                                      |
| xml_etree_process        | 36.4 ms                                                         | 35.8 ms: 1.02x faster                                                      |
| xml_etree_iterparse      | 62.3 ms                                                         | 61.7 ms: 1.01x faster                                                      |
| pidigits                 | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| json_loads               | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| gc_traversal             | 1.55 ms                                                         | 1.58 ms: 1.02x slower                                                      |
| regex_effbot             | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                      |
| json_dumps               | 5.61 ms                                                         | 5.78 ms: 1.03x slower                                                      |
| xml_etree_parse          | 90.9 ms                                                         | 94.0 ms: 1.03x slower                                                      |
| comprehensions           | 10.4 us                                                         | 10.8 us: 1.04x slower                                                      |
| regex_dna                | 119 ms                                                          | 124 ms: 1.04x slower                                                       |
| pathlib                  | 75.9 ms                                                         | 79.1 ms: 1.04x slower                                                      |
| logging_simple           | 5.78 us                                                         | 6.05 us: 1.05x slower                                                      |
| create_gc_cycles         | 888 us                                                          | 933 us: 1.05x slower                                                       |
| logging_format           | 6.22 us                                                         | 6.56 us: 1.05x slower                                                      |
| chaos                    | 38.4 ms                                                         | 40.7 ms: 1.06x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 74.6 ms: 1.07x slower                                                      |
| pprint_safe_repr         | 474 ms                                                          | 507 ms: 1.07x slower                                                       |
| bench_thread_pool        | 768 us                                                          | 827 us: 1.08x slower                                                       |
| coroutines               | 12.8 ms                                                         | 13.8 ms: 1.08x slower                                                      |
| logging_silent           | 52.9 ns                                                         | 57.3 ns: 1.08x slower                                                      |
| pprint_pformat           | 966 ms                                                          | 1.05 sec: 1.08x slower                                                     |
| nqueens                  | 56.7 ms                                                         | 61.4 ms: 1.08x slower                                                      |
| python_startup           | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                      |
| typing_runtime_protocols | 101 us                                                          | 111 us: 1.10x slower                                                       |
| mdp                      | 1.31 sec                                                        | 1.46 sec: 1.11x slower                                                     |
| pickle_pure_python       | 175 us                                                          | 195 us: 1.11x slower                                                       |
| scimark_monte_carlo      | 39.1 ms                                                         | 43.5 ms: 1.11x slower                                                      |
| generators               | 19.6 ms                                                         | 21.7 ms: 1.11x slower                                                      |
| go                       | 82.1 ms                                                         | 92.0 ms: 1.12x slower                                                      |
| asyncio_tcp              | 471 ms                                                          | 530 ms: 1.13x slower                                                       |
| coverage                 | 42.1 ms                                                         | 47.6 ms: 1.13x slower                                                      |
| python_startup_no_site   | 16.2 ms                                                         | 18.6 ms: 1.15x slower                                                      |
| bench_mp_pool            | 64.8 ms                                                         | 74.4 ms: 1.15x slower                                                      |
| dulwich_log              | 38.0 ms                                                         | 44.0 ms: 1.16x slower                                                      |
| async_generators         | 223 ms                                                          | 261 ms: 1.17x slower                                                       |
| sqlglot_normalize        | 173 ms                                                          | 203 ms: 1.17x slower                                                       |
| 2to3                     | 207 ms                                                          | 243 ms: 1.17x slower                                                       |
| sympy_sum                | 84.4 ms                                                         | 99.3 ms: 1.18x slower                                                      |
| unpickle_pure_python     | 122 us                                                          | 145 us: 1.19x slower                                                       |
| sympy_str                | 159 ms                                                          | 190 ms: 1.19x slower                                                       |
| docutils                 | 1.63 sec                                                        | 1.94 sec: 1.19x slower                                                     |
| sqlglot_parse            | 748 us                                                          | 901 us: 1.20x slower                                                       |
| tornado_http             | 81.8 ms                                                         | 99.1 ms: 1.21x slower                                                      |
| sympy_expand             | 271 ms                                                          | 329 ms: 1.21x slower                                                       |
| raytrace                 | 162 ms                                                          | 198 ms: 1.22x slower                                                       |
| html5lib                 | 35.0 ms                                                         | 42.8 ms: 1.22x slower                                                      |
| sqlglot_optimize         | 32.7 ms                                                         | 40.0 ms: 1.22x slower                                                      |
| sympy_integrate          | 12.2 ms                                                         | 15.0 ms: 1.22x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 1.17 ms: 1.23x slower                                                      |
| regex_compile            | 78.0 ms                                                         | 95.6 ms: 1.23x slower                                                      |
| django_template          | 21.7 ms                                                         | 26.8 ms: 1.24x slower                                                      |
| richards_super           | 30.2 ms                                                         | 39.3 ms: 1.30x slower                                                      |
| hexiom                   | 3.72 ms                                                         | 4.87 ms: 1.31x slower                                                      |
| pylint                   | 205 ms                                                          | 269 ms: 1.31x slower                                                       |
| richards                 | 26.7 ms                                                         | 36.0 ms: 1.35x slower                                                      |
| genshi_text              | 14.4 ms                                                         | 19.7 ms: 1.37x slower                                                      |
| genshi_xml               | 31.6 ms                                                         | 46.3 ms: 1.46x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (8): regex_v8, async_tree_none_tg, async_tree_memoization_tg, pycparser, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_tcp_ssl
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown