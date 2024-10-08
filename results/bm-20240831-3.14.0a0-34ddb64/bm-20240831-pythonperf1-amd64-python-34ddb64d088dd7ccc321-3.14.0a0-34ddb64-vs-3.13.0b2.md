# Results vs. 3.13.0b2

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-amd64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 226 ms: 1.09x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.7 ms: 1.16x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 93.8 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 564 ms: 1.07x faster                                                       |
| async_tree_none            | 218 ms                                                          | 210 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 399 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 152 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 56.2 ms: 1.13x slower                                                      |
| nbody          | 67.6 ms                                                         | 83.6 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.54 ms: 1.03x faster                                                      |
| regex_dna      | 119 ms                                                          | 116 ms: 1.03x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 91.5 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.4 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.0 ms: 1.04x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 95.6 ms: 1.05x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.7 ms: 1.09x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.24 ms: 1.11x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 40.9 ms: 1.12x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.59 sec: 1.18x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 208 us: 1.19x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 149 us: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.87 ms: 1.08x slower                                                      |
| django_template | 21.7 ms                                                         | 24.2 ms: 1.11x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.5 ms: 1.15x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 36.3 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.12x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 525 us: 15.44x faster                                                      |
| deepcopy                   | 220 us                                                          | 186 us: 1.18x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 19.5 us: 1.13x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 564 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.90 us: 1.05x faster                                                      |
| async_tree_none            | 218 ms                                                          | 210 ms: 1.04x faster                                                       |
| regex_effbot               | 1.58 ms                                                         | 1.54 ms: 1.03x faster                                                      |
| regex_dna                  | 119 ms                                                          | 116 ms: 1.03x faster                                                       |
| pidigits                   | 150 ms                                                          | 152 ms: 1.01x slower                                                       |
| json_loads                 | 14.2 us                                                         | 14.4 us: 1.01x slower                                                      |
| go                         | 82.1 ms                                                         | 84.7 ms: 1.03x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 917 us: 1.03x slower                                                       |
| docutils                   | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                     |
| xml_etree_iterparse        | 62.3 ms                                                         | 65.0 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 399 ms: 1.04x slower                                                       |
| pathlib                    | 75.9 ms                                                         | 79.4 ms: 1.05x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 95.6 ms: 1.05x slower                                                      |
| generators                 | 19.6 ms                                                         | 20.6 ms: 1.05x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 47.8 ms: 1.05x slower                                                      |
| spectral_norm              | 63.7 ms                                                         | 67.4 ms: 1.06x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 68.7 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.66 ms: 1.06x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.63 us: 1.07x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 90.1 ms: 1.07x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.1 ms: 1.07x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.25 us: 1.08x slower                                                      |
| mako                       | 6.36 ms                                                         | 6.87 ms: 1.08x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 831 us: 1.08x slower                                                       |
| xml_etree_generate         | 53.2 ms                                                         | 57.7 ms: 1.09x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 512 ms: 1.09x slower                                                       |
| telco                      | 4.67 ms                                                         | 5.09 ms: 1.09x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.43 sec: 1.09x slower                                                     |
| 2to3                       | 207 ms                                                          | 226 ms: 1.09x slower                                                       |
| python_startup             | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 62.3 ms: 1.10x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.1 ms: 1.10x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 191 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 32.7 ms                                                         | 36.3 ms: 1.11x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 6.24 ms: 1.11x slower                                                      |
| sympy_str                  | 159 ms                                                          | 177 ms: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                      |
| chaos                      | 38.4 ms                                                         | 42.7 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                          | 249 ms: 1.11x slower                                                       |
| django_template            | 21.7 ms                                                         | 24.2 ms: 1.11x slower                                                      |
| pylint                     | 205 ms                                                          | 228 ms: 1.12x slower                                                       |
| meteor_contest             | 69.9 ms                                                         | 78.3 ms: 1.12x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 40.9 ms: 1.12x slower                                                      |
| float                      | 49.7 ms                                                         | 56.2 ms: 1.13x slower                                                      |
| sympy_expand               | 271 ms                                                          | 307 ms: 1.13x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 115 us: 1.14x slower                                                       |
| comprehensions             | 10.4 us                                                         | 11.8 us: 1.14x slower                                                      |
| scimark_fft                | 171 ms                                                          | 195 ms: 1.14x slower                                                       |
| tornado_http               | 81.8 ms                                                         | 93.8 ms: 1.15x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 16.5 ms: 1.15x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 36.3 ms: 1.15x slower                                                      |
| pprint_pformat             | 966 ms                                                          | 1.11 sec: 1.15x slower                                                     |
| nqueens                    | 56.7 ms                                                         | 65.2 ms: 1.15x slower                                                      |
| pyflate                    | 279 ms                                                          | 322 ms: 1.16x slower                                                       |
| raytrace                   | 162 ms                                                          | 188 ms: 1.16x slower                                                       |
| sqlglot_transpile          | 955 us                                                          | 1.11 ms: 1.16x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 4.32 ms: 1.16x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 40.7 ms: 1.16x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 44.4 ms: 1.17x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 555 ms: 1.17x slower                                                       |
| coverage                   | 42.1 ms                                                         | 49.3 ms: 1.17x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 91.5 ms: 1.17x slower                                                      |
| scimark_sor                | 75.3 ms                                                         | 88.7 ms: 1.18x slower                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.59 sec: 1.18x slower                                                     |
| logging_silent             | 52.9 ns                                                         | 62.5 ns: 1.18x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 208 us: 1.19x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 891 us: 1.19x slower                                                       |
| fannkuch                   | 243 ms                                                          | 291 ms: 1.20x slower                                                       |
| deltablue                  | 1.88 ms                                                         | 2.25 ms: 1.20x slower                                                      |
| richards_super             | 30.2 ms                                                         | 36.2 ms: 1.20x slower                                                      |
| richards                   | 26.7 ms                                                         | 32.4 ms: 1.21x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 149 us: 1.22x slower                                                       |
| nbody                      | 67.6 ms                                                         | 83.6 ms: 1.24x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 49.1 ms: 1.25x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_io, json, regex_v8, async_tree_memoization, gc_traversal, async_tree_cpu_io_mixed, pycparser, async_tree_none_tg, asyncio_tcp_ssl
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown