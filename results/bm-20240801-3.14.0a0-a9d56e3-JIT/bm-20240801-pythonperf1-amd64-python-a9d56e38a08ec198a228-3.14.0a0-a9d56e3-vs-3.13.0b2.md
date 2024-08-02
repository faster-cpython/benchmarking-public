# Results vs. 3.13.0b2

- fork: python
- ref: a9d56e38a08ec198a228
- machine: windows-amd64
- commit hash: a9d56e3
- commit date: 2024-08-01
- overall geometric mean: 1.01x slower
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 240 ms: 1.16x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.85 sec: 1.14x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.0 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 95.5 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                           | 1.17x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|--------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg   | 605 ms                                                          | 537 ms: 1.13x faster                                                       |
| async_tree_io      | 588 ms                                                          | 545 ms: 1.08x faster                                                       |
| async_tree_none_tg | 202 ms                                                          | 194 ms: 1.04x faster                                                       |
| async_tree_none    | 218 ms                                                          | 212 ms: 1.03x faster                                                       |
| Geometric mean     | (ref)                                                           | 1.04x faster                                                               |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.5 ms: 1.31x faster                                                      |
| float          | 49.7 ms                                                         | 45.4 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                           | 1.13x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.7 ms: 1.07x faster                                                      |
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 91.7 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.26 sec: 1.07x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 52.3 ms: 1.02x faster                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.5 ms: 1.02x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.6 us: 1.03x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 37.8 ms: 1.04x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 184 us: 1.05x slower                                                       |
| json_dumps           | 5.61 ms                                                         | 5.99 ms: 1.07x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 137 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 4.97 ms: 1.28x faster                                                      |
| django_template | 21.7 ms                                                         | 25.9 ms: 1.19x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 40.9 ms: 1.29x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.7 ms: 1.30x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.12x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 533 us: 15.20x faster                                                      |
| spectral_norm            | 63.7 ms                                                         | 45.8 ms: 1.39x faster                                                      |
| deepcopy_memo            | 22.1 us                                                         | 16.1 us: 1.37x faster                                                      |
| nbody                    | 67.6 ms                                                         | 51.5 ms: 1.31x faster                                                      |
| mako                     | 6.36 ms                                                         | 4.97 ms: 1.28x faster                                                      |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.07 ms: 1.21x faster                                                      |
| deepcopy                 | 220 us                                                          | 185 us: 1.19x faster                                                       |
| scimark_fft              | 171 ms                                                          | 147 ms: 1.16x faster                                                       |
| crypto_pyaes             | 45.5 ms                                                         | 39.4 ms: 1.15x faster                                                      |
| fannkuch                 | 243 ms                                                          | 215 ms: 1.13x faster                                                       |
| pyflate                  | 279 ms                                                          | 247 ms: 1.13x faster                                                       |
| async_tree_io_tg         | 605 ms                                                          | 537 ms: 1.13x faster                                                       |
| deepcopy_reduce          | 1.99 us                                                         | 1.82 us: 1.10x faster                                                      |
| float                    | 49.7 ms                                                         | 45.4 ms: 1.09x faster                                                      |
| async_tree_io            | 588 ms                                                          | 545 ms: 1.08x faster                                                       |
| regex_v8                 | 15.8 ms                                                         | 14.7 ms: 1.07x faster                                                      |
| tomli_loads              | 1.35 sec                                                        | 1.26 sec: 1.07x faster                                                     |
| asyncio_tcp_ssl          | 1.48 sec                                                        | 1.42 sec: 1.04x faster                                                     |
| async_tree_none_tg       | 202 ms                                                          | 194 ms: 1.04x faster                                                       |
| async_tree_none          | 218 ms                                                          | 212 ms: 1.03x faster                                                       |
| scimark_monte_carlo      | 39.1 ms                                                         | 38.0 ms: 1.03x faster                                                      |
| telco                    | 4.67 ms                                                         | 4.54 ms: 1.03x faster                                                      |
| xml_etree_generate       | 53.2 ms                                                         | 52.3 ms: 1.02x faster                                                      |
| comprehensions           | 10.4 us                                                         | 10.3 us: 1.01x faster                                                      |
| regex_dna                | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| meteor_contest           | 69.9 ms                                                         | 70.7 ms: 1.01x slower                                                      |
| gc_traversal             | 1.55 ms                                                         | 1.58 ms: 1.01x slower                                                      |
| xml_etree_parse          | 90.9 ms                                                         | 92.5 ms: 1.02x slower                                                      |
| pprint_safe_repr         | 474 ms                                                          | 484 ms: 1.02x slower                                                       |
| create_gc_cycles         | 888 us                                                          | 912 us: 1.03x slower                                                       |
| chaos                    | 38.4 ms                                                         | 39.4 ms: 1.03x slower                                                      |
| json_loads               | 14.2 us                                                         | 14.6 us: 1.03x slower                                                      |
| pprint_pformat           | 966 ms                                                          | 995 ms: 1.03x slower                                                       |
| xml_etree_process        | 36.4 ms                                                         | 37.8 ms: 1.04x slower                                                      |
| pickle_pure_python       | 175 us                                                          | 184 us: 1.05x slower                                                       |
| logging_simple           | 5.78 us                                                         | 6.06 us: 1.05x slower                                                      |
| logging_format           | 6.22 us                                                         | 6.53 us: 1.05x slower                                                      |
| bench_thread_pool        | 768 us                                                          | 814 us: 1.06x slower                                                       |
| json_dumps               | 5.61 ms                                                         | 5.99 ms: 1.07x slower                                                      |
| pathlib                  | 75.9 ms                                                         | 81.0 ms: 1.07x slower                                                      |
| coroutines               | 12.8 ms                                                         | 13.7 ms: 1.07x slower                                                      |
| python_startup           | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| python_startup_no_site   | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| nqueens                  | 56.7 ms                                                         | 62.3 ms: 1.10x slower                                                      |
| mdp                      | 1.31 sec                                                        | 1.45 sec: 1.11x slower                                                     |
| logging_silent           | 52.9 ns                                                         | 58.7 ns: 1.11x slower                                                      |
| sqlglot_normalize        | 173 ms                                                          | 192 ms: 1.11x slower                                                       |
| sqlglot_optimize         | 32.7 ms                                                         | 36.8 ms: 1.12x slower                                                      |
| unpickle_pure_python     | 122 us                                                          | 137 us: 1.13x slower                                                       |
| sqlglot_parse            | 748 us                                                          | 844 us: 1.13x slower                                                       |
| bench_mp_pool            | 64.8 ms                                                         | 73.0 ms: 1.13x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 1.08 ms: 1.13x slower                                                      |
| dulwich_log              | 38.0 ms                                                         | 43.1 ms: 1.13x slower                                                      |
| coverage                 | 42.1 ms                                                         | 47.7 ms: 1.13x slower                                                      |
| docutils                 | 1.63 sec                                                        | 1.85 sec: 1.14x slower                                                     |
| sympy_sum                | 84.4 ms                                                         | 96.3 ms: 1.14x slower                                                      |
| 2to3                     | 207 ms                                                          | 240 ms: 1.16x slower                                                       |
| typing_runtime_protocols | 101 us                                                          | 118 us: 1.17x slower                                                       |
| tornado_http             | 81.8 ms                                                         | 95.5 ms: 1.17x slower                                                      |
| async_generators         | 223 ms                                                          | 261 ms: 1.17x slower                                                       |
| regex_compile            | 78.0 ms                                                         | 91.7 ms: 1.18x slower                                                      |
| generators               | 19.6 ms                                                         | 23.0 ms: 1.18x slower                                                      |
| asyncio_tcp              | 471 ms                                                          | 555 ms: 1.18x slower                                                       |
| richards_super           | 30.2 ms                                                         | 35.6 ms: 1.18x slower                                                      |
| richards                 | 26.7 ms                                                         | 31.5 ms: 1.18x slower                                                      |
| raytrace                 | 162 ms                                                          | 192 ms: 1.19x slower                                                       |
| sympy_str                | 159 ms                                                          | 189 ms: 1.19x slower                                                       |
| django_template          | 21.7 ms                                                         | 25.9 ms: 1.19x slower                                                      |
| html5lib                 | 35.0 ms                                                         | 42.0 ms: 1.20x slower                                                      |
| sympy_integrate          | 12.2 ms                                                         | 14.7 ms: 1.20x slower                                                      |
| sympy_expand             | 271 ms                                                          | 330 ms: 1.22x slower                                                       |
| go                       | 82.1 ms                                                         | 101 ms: 1.23x slower                                                       |
| scimark_sor              | 75.3 ms                                                         | 92.7 ms: 1.23x slower                                                      |
| pylint                   | 205 ms                                                          | 254 ms: 1.24x slower                                                       |
| deltablue                | 1.88 ms                                                         | 2.35 ms: 1.25x slower                                                      |
| genshi_xml               | 31.6 ms                                                         | 40.9 ms: 1.29x slower                                                      |
| hexiom                   | 3.72 ms                                                         | 4.83 ms: 1.30x slower                                                      |
| genshi_text              | 14.4 ms                                                         | 18.7 ms: 1.30x slower                                                      |
| scimark_lu               | 56.6 ms                                                         | 75.2 ms: 1.33x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (9): json, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, xml_etree_iterparse, pidigits, regex_effbot, async_tree_cpu_io_mixed, pycparser
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.76% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown