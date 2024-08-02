# Results vs. 3.13.0b2

- fork: python
- ref: 498376d7a7d6f704f22a
- machine: windows-amd64
- commit hash: 498376d
- commit date: 2024-08-02
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 232 ms: 1.12x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.79 sec: 1.10x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.3 ms: 1.21x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 95.3 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                           | 1.15x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 561 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 397 ms: 1.02x slower                                                       |
| async_tree_memoization     | 264 ms                                                          | 272 ms: 1.03x slower                                                       |
| async_tree_none            | 218 ms                                                          | 225 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 398 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 55.3 ms: 1.11x slower                                                      |
| nbody          | 67.6 ms                                                         | 91.2 ms: 1.35x slower                                                      |
| Geometric mean | (ref)                                                           | 1.15x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| regex_dna      | 119 ms                                                          | 125 ms: 1.05x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 94.2 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                           | 1.09x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 90.9 ms                                                         | 95.6 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.2 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 59.1 ms: 1.11x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.26 ms: 1.12x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 42.5 ms: 1.17x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.66 sec: 1.23x slower                                                     |
| unpickle_pure_python | 122 us                                                          | 152 us: 1.25x slower                                                       |
| pickle_pure_python   | 175 us                                                          | 226 us: 1.29x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.14x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.13 ms: 1.12x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 36.9 ms: 1.17x slower                                                      |
| django_template | 21.7 ms                                                         | 26.2 ms: 1.21x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.0 ms: 1.25x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.19x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 526 us: 15.40x faster                                                      |
| deepcopy                   | 220 us                                                          | 193 us: 1.14x faster                                                       |
| async_tree_io_tg           | 605 ms                                                          | 561 ms: 1.08x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 21.3 us: 1.04x faster                                                      |
| gc_traversal               | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                      |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 2.02 us: 1.01x slower                                                      |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 397 ms: 1.02x slower                                                       |
| create_gc_cycles           | 888 us                                                          | 913 us: 1.03x slower                                                       |
| async_tree_memoization     | 264 ms                                                          | 272 ms: 1.03x slower                                                       |
| regex_effbot               | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| async_tree_none            | 218 ms                                                          | 225 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 398 ms: 1.04x slower                                                       |
| regex_dna                  | 119 ms                                                          | 125 ms: 1.05x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 95.6 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 66.2 ms: 1.06x slower                                                      |
| telco                      | 4.67 ms                                                         | 4.97 ms: 1.06x slower                                                      |
| pathlib                    | 75.9 ms                                                         | 81.0 ms: 1.07x slower                                                      |
| generators                 | 19.6 ms                                                         | 20.9 ms: 1.07x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 69.9 ms: 1.08x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 831 us: 1.08x slower                                                       |
| python_startup             | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 13.9 ms: 1.09x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.79 sec: 1.10x slower                                                     |
| sympy_integrate            | 12.2 ms                                                         | 13.6 ms: 1.11x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.78 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 59.1 ms: 1.11x slower                                                      |
| float                      | 49.7 ms                                                         | 55.3 ms: 1.11x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 94.0 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                          | 249 ms: 1.11x slower                                                       |
| json_dumps                 | 5.61 ms                                                         | 6.26 ms: 1.12x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.94 us: 1.12x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 78.0 ms: 1.12x slower                                                      |
| 2to3                       | 207 ms                                                          | 232 ms: 1.12x slower                                                       |
| mako                       | 6.36 ms                                                         | 7.13 ms: 1.12x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.48 us: 1.12x slower                                                      |
| coverage                   | 42.1 ms                                                         | 47.6 ms: 1.13x slower                                                      |
| pylint                     | 205 ms                                                          | 234 ms: 1.14x slower                                                       |
| crypto_pyaes               | 45.5 ms                                                         | 51.9 ms: 1.14x slower                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.70 sec: 1.15x slower                                                     |
| sqlglot_optimize           | 32.7 ms                                                         | 37.6 ms: 1.15x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 65.1 ms: 1.15x slower                                                      |
| sympy_expand               | 271 ms                                                          | 312 ms: 1.15x slower                                                       |
| sympy_str                  | 159 ms                                                          | 184 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 117 us: 1.16x slower                                                       |
| tornado_http               | 81.8 ms                                                         | 95.3 ms: 1.16x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 202 ms: 1.17x slower                                                       |
| xml_etree_process          | 36.4 ms                                                         | 42.5 ms: 1.17x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 44.4 ms: 1.17x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 36.9 ms: 1.17x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 66.8 ms: 1.18x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.14 ms: 1.19x slower                                                      |
| pyflate                    | 279 ms                                                          | 333 ms: 1.19x slower                                                       |
| chaos                      | 38.4 ms                                                         | 45.8 ms: 1.19x slower                                                      |
| scimark_fft                | 171 ms                                                          | 205 ms: 1.20x slower                                                       |
| mdp                        | 1.31 sec                                                        | 1.58 sec: 1.20x slower                                                     |
| comprehensions             | 10.4 us                                                         | 12.5 us: 1.21x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 94.2 ms: 1.21x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 42.3 ms: 1.21x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 573 ms: 1.21x slower                                                       |
| django_template            | 21.7 ms                                                         | 26.2 ms: 1.21x slower                                                      |
| spectral_norm              | 63.7 ms                                                         | 77.3 ms: 1.21x slower                                                      |
| pprint_pformat             | 966 ms                                                          | 1.18 sec: 1.22x slower                                                     |
| sqlglot_parse              | 748 us                                                          | 915 us: 1.22x slower                                                       |
| go                         | 82.1 ms                                                         | 101 ms: 1.22x slower                                                       |
| fannkuch                   | 243 ms                                                          | 298 ms: 1.23x slower                                                       |
| tomli_loads                | 1.35 sec                                                        | 1.66 sec: 1.23x slower                                                     |
| pycparser                  | 754 ms                                                          | 928 ms: 1.23x slower                                                       |
| deltablue                  | 1.88 ms                                                         | 2.35 ms: 1.25x slower                                                      |
| logging_silent             | 52.9 ns                                                         | 66.1 ns: 1.25x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 152 us: 1.25x slower                                                       |
| genshi_text                | 14.4 ms                                                         | 18.0 ms: 1.25x slower                                                      |
| raytrace                   | 162 ms                                                          | 204 ms: 1.25x slower                                                       |
| hexiom                     | 3.72 ms                                                         | 4.72 ms: 1.27x slower                                                      |
| scimark_sor                | 75.3 ms                                                         | 96.2 ms: 1.28x slower                                                      |
| richards_super             | 30.2 ms                                                         | 38.5 ms: 1.28x slower                                                      |
| richards                   | 26.7 ms                                                         | 34.2 ms: 1.28x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 226 us: 1.29x slower                                                       |
| scimark_monte_carlo        | 39.1 ms                                                         | 52.5 ms: 1.34x slower                                                      |
| nbody                      | 67.6 ms                                                         | 91.2 ms: 1.35x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 645 ms: 1.37x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.10x slower                                                               |

Benchmark hidden because not significant (6): json, async_tree_memoization_tg, json_loads, async_tree_none_tg, async_tree_io, regex_v8
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: unknown