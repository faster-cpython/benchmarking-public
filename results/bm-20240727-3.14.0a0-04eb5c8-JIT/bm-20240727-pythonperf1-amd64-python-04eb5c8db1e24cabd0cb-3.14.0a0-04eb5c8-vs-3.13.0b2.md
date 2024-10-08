# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-amd64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.04x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 233 ms: 1.13x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.88 sec: 1.16x slower                                                     |
| html5lib       | 35.0 ms                                                         | 41.6 ms: 1.19x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 96.3 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                           | 1.16x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg   | 605 ms                                                          | 536 ms: 1.13x faster                                                       |
| async_tree_io      | 588 ms                                                          | 539 ms: 1.09x faster                                                       |
| async_tree_none_tg | 202 ms                                                          | 195 ms: 1.04x faster                                                       |
| Geometric mean     | (ref)                                                           | 1.03x faster                                                               |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.1 ms: 1.32x faster                                                      |
| float          | 49.7 ms                                                         | 45.0 ms: 1.11x faster                                                      |
| pidigits       | 150 ms                                                          | 152 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                           | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| regex_dna      | 119 ms                                                          | 125 ms: 1.05x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 91.7 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.31 sec: 1.03x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 52.4 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.5 ms: 1.01x faster                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.8 ms: 1.02x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 183 us: 1.04x slower                                                       |
| xml_etree_process    | 36.4 ms                                                         | 38.1 ms: 1.04x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.8 us: 1.04x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.08 ms: 1.08x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 135 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.3 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.5 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.19 ms: 1.22x faster                                                      |
| django_template | 21.7 ms                                                         | 26.2 ms: 1.21x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.9 ms: 1.32x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 46.7 ms: 1.48x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.18x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 523 us: 15.51x faster                                                      |
| spectral_norm            | 63.7 ms                                                         | 46.8 ms: 1.36x faster                                                      |
| deepcopy_memo            | 22.1 us                                                         | 16.3 us: 1.35x faster                                                      |
| nbody                    | 67.6 ms                                                         | 51.1 ms: 1.32x faster                                                      |
| mako                     | 6.36 ms                                                         | 5.19 ms: 1.22x faster                                                      |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.09 ms: 1.20x faster                                                      |
| deepcopy                 | 220 us                                                          | 191 us: 1.15x faster                                                       |
| scimark_fft              | 171 ms                                                          | 150 ms: 1.14x faster                                                       |
| async_tree_io_tg         | 605 ms                                                          | 536 ms: 1.13x faster                                                       |
| crypto_pyaes             | 45.5 ms                                                         | 40.6 ms: 1.12x faster                                                      |
| float                    | 49.7 ms                                                         | 45.0 ms: 1.11x faster                                                      |
| async_tree_io            | 588 ms                                                          | 539 ms: 1.09x faster                                                       |
| pyflate                  | 279 ms                                                          | 256 ms: 1.09x faster                                                       |
| fannkuch                 | 243 ms                                                          | 229 ms: 1.06x faster                                                       |
| pycparser                | 754 ms                                                          | 709 ms: 1.06x faster                                                       |
| deepcopy_reduce          | 1.99 us                                                         | 1.88 us: 1.06x faster                                                      |
| async_tree_none_tg       | 202 ms                                                          | 195 ms: 1.04x faster                                                       |
| tomli_loads              | 1.35 sec                                                        | 1.31 sec: 1.03x faster                                                     |
| scimark_monte_carlo      | 39.1 ms                                                         | 38.2 ms: 1.02x faster                                                      |
| xml_etree_generate       | 53.2 ms                                                         | 52.4 ms: 1.01x faster                                                      |
| xml_etree_iterparse      | 62.3 ms                                                         | 61.5 ms: 1.01x faster                                                      |
| pprint_safe_repr         | 474 ms                                                          | 478 ms: 1.01x slower                                                       |
| pidigits                 | 150 ms                                                          | 152 ms: 1.01x slower                                                       |
| telco                    | 4.67 ms                                                         | 4.72 ms: 1.01x slower                                                      |
| comprehensions           | 10.4 us                                                         | 10.5 us: 1.01x slower                                                      |
| xml_etree_parse          | 90.9 ms                                                         | 92.8 ms: 1.02x slower                                                      |
| pprint_pformat           | 966 ms                                                          | 987 ms: 1.02x slower                                                       |
| gc_traversal             | 1.55 ms                                                         | 1.60 ms: 1.03x slower                                                      |
| regex_effbot             | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 72.2 ms: 1.03x slower                                                      |
| pickle_pure_python       | 175 us                                                          | 183 us: 1.04x slower                                                       |
| xml_etree_process        | 36.4 ms                                                         | 38.1 ms: 1.04x slower                                                      |
| json_loads               | 14.2 us                                                         | 14.8 us: 1.04x slower                                                      |
| python_startup           | 20.3 ms                                                         | 21.3 ms: 1.05x slower                                                      |
| regex_dna                | 119 ms                                                          | 125 ms: 1.05x slower                                                       |
| create_gc_cycles         | 888 us                                                          | 935 us: 1.05x slower                                                       |
| chaos                    | 38.4 ms                                                         | 40.6 ms: 1.06x slower                                                      |
| logging_simple           | 5.78 us                                                         | 6.13 us: 1.06x slower                                                      |
| coroutines               | 12.8 ms                                                         | 13.7 ms: 1.07x slower                                                      |
| logging_format           | 6.22 us                                                         | 6.69 us: 1.07x slower                                                      |
| logging_silent           | 52.9 ns                                                         | 57.3 ns: 1.08x slower                                                      |
| python_startup_no_site   | 16.2 ms                                                         | 17.5 ms: 1.08x slower                                                      |
| json_dumps               | 5.61 ms                                                         | 6.08 ms: 1.08x slower                                                      |
| nqueens                  | 56.7 ms                                                         | 62.1 ms: 1.10x slower                                                      |
| unpickle_pure_python     | 122 us                                                          | 135 us: 1.10x slower                                                       |
| generators               | 19.6 ms                                                         | 21.7 ms: 1.11x slower                                                      |
| dulwich_log              | 38.0 ms                                                         | 42.4 ms: 1.12x slower                                                      |
| sqlglot_parse            | 748 us                                                          | 835 us: 1.12x slower                                                       |
| pathlib                  | 75.9 ms                                                         | 84.7 ms: 1.12x slower                                                      |
| 2to3                     | 207 ms                                                          | 233 ms: 1.13x slower                                                       |
| sqlglot_transpile        | 955 us                                                          | 1.08 ms: 1.13x slower                                                      |
| bench_mp_pool            | 64.8 ms                                                         | 73.2 ms: 1.13x slower                                                      |
| asyncio_tcp              | 471 ms                                                          | 536 ms: 1.14x slower                                                       |
| coverage                 | 42.1 ms                                                         | 48.4 ms: 1.15x slower                                                      |
| async_generators         | 223 ms                                                          | 257 ms: 1.15x slower                                                       |
| sqlglot_optimize         | 32.7 ms                                                         | 37.8 ms: 1.15x slower                                                      |
| richards                 | 26.7 ms                                                         | 30.9 ms: 1.16x slower                                                      |
| docutils                 | 1.63 sec                                                        | 1.88 sec: 1.16x slower                                                     |
| sqlglot_normalize        | 173 ms                                                          | 201 ms: 1.16x slower                                                       |
| richards_super           | 30.2 ms                                                         | 35.1 ms: 1.16x slower                                                      |
| sympy_sum                | 84.4 ms                                                         | 98.7 ms: 1.17x slower                                                      |
| regex_compile            | 78.0 ms                                                         | 91.7 ms: 1.18x slower                                                      |
| tornado_http             | 81.8 ms                                                         | 96.3 ms: 1.18x slower                                                      |
| mdp                      | 1.31 sec                                                        | 1.55 sec: 1.18x slower                                                     |
| raytrace                 | 162 ms                                                          | 192 ms: 1.18x slower                                                       |
| sympy_str                | 159 ms                                                          | 189 ms: 1.19x slower                                                       |
| html5lib                 | 35.0 ms                                                         | 41.6 ms: 1.19x slower                                                      |
| typing_runtime_protocols | 101 us                                                          | 120 us: 1.19x slower                                                       |
| sympy_integrate          | 12.2 ms                                                         | 14.7 ms: 1.20x slower                                                      |
| scimark_sor              | 75.3 ms                                                         | 90.5 ms: 1.20x slower                                                      |
| django_template          | 21.7 ms                                                         | 26.2 ms: 1.21x slower                                                      |
| sympy_expand             | 271 ms                                                          | 329 ms: 1.22x slower                                                       |
| go                       | 82.1 ms                                                         | 101 ms: 1.23x slower                                                       |
| deltablue                | 1.88 ms                                                         | 2.34 ms: 1.24x slower                                                      |
| pylint                   | 205 ms                                                          | 255 ms: 1.24x slower                                                       |
| hexiom                   | 3.72 ms                                                         | 4.74 ms: 1.27x slower                                                      |
| genshi_text              | 14.4 ms                                                         | 18.9 ms: 1.32x slower                                                      |
| scimark_lu               | 56.6 ms                                                         | 75.9 ms: 1.34x slower                                                      |
| genshi_xml               | 31.6 ms                                                         | 46.7 ms: 1.48x slower                                                      |
| bench_thread_pool        | 768 us                                                          | 3.06 ms: 3.98x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (8): async_tree_memoization_tg, regex_v8, json, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_tcp_ssl
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown