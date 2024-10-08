# Results vs. 3.13.0b2

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-amd64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 227 ms: 1.10x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.70 sec: 1.05x slower                                                     |
| html5lib       | 35.0 ms                                                         | 39.9 ms: 1.14x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 93.8 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg | 605 ms                                                          | 541 ms: 1.12x faster                                                       |
| async_tree_io    | 588 ms                                                          | 613 ms: 1.04x slower                                                       |
| Geometric mean   | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 152 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 57.2 ms: 1.15x slower                                                      |
| nbody          | 67.6 ms                                                         | 84.6 ms: 1.25x slower                                                      |
| Geometric mean | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 90.8 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_list          | 2.90 us                                                         | 2.99 us: 1.03x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 94.3 ms: 1.04x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 19.0 us: 1.05x slower                                                      |
| pickle               | 7.11 us                                                         | 7.44 us: 1.05x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.3 ms: 1.05x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.78 us: 1.06x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 58.4 ms: 1.10x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.21 ms: 1.11x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.2 ms: 1.13x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.64 us: 1.15x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.60 sec: 1.19x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 213 us: 1.21x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 150 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.10x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.1 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.85 ms: 1.08x slower                                                      |
| django_template | 21.7 ms                                                         | 24.9 ms: 1.15x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 36.6 ms: 1.16x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 515 us: 15.75x faster                                                      |
| deepcopy                 | 220 us                                                          | 189 us: 1.16x faster                                                       |
| async_tree_io_tg         | 605 ms                                                          | 541 ms: 1.12x faster                                                       |
| deepcopy_memo            | 22.1 us                                                         | 20.3 us: 1.09x faster                                                      |
| deepcopy_reduce          | 1.99 us                                                         | 1.89 us: 1.05x faster                                                      |
| regex_dna                | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| pidigits                 | 150 ms                                                          | 152 ms: 1.01x slower                                                       |
| create_gc_cycles         | 888 us                                                          | 902 us: 1.02x slower                                                       |
| sqlite_synth             | 1.60 us                                                         | 1.62 us: 1.02x slower                                                      |
| pickle_list              | 2.90 us                                                         | 2.99 us: 1.03x slower                                                      |
| xml_etree_parse          | 90.9 ms                                                         | 94.3 ms: 1.04x slower                                                      |
| async_tree_io            | 588 ms                                                          | 613 ms: 1.04x slower                                                       |
| pickle_dict              | 18.1 us                                                         | 19.0 us: 1.05x slower                                                      |
| pickle                   | 7.11 us                                                         | 7.44 us: 1.05x slower                                                      |
| docutils                 | 1.63 sec                                                        | 1.70 sec: 1.05x slower                                                     |
| pathlib                  | 75.9 ms                                                         | 79.4 ms: 1.05x slower                                                      |
| xml_etree_iterparse      | 62.3 ms                                                         | 65.3 ms: 1.05x slower                                                      |
| bench_mp_pool            | 64.8 ms                                                         | 67.8 ms: 1.05x slower                                                      |
| crypto_pyaes             | 45.5 ms                                                         | 47.8 ms: 1.05x slower                                                      |
| go                       | 82.1 ms                                                         | 86.9 ms: 1.06x slower                                                      |
| unpickle_list            | 2.62 us                                                         | 2.78 us: 1.06x slower                                                      |
| logging_format           | 6.22 us                                                         | 6.64 us: 1.07x slower                                                      |
| generators               | 19.6 ms                                                         | 20.9 ms: 1.07x slower                                                      |
| bench_thread_pool        | 768 us                                                          | 823 us: 1.07x slower                                                       |
| asyncio_tcp_ssl          | 1.48 sec                                                        | 1.59 sec: 1.07x slower                                                     |
| sympy_integrate          | 12.2 ms                                                         | 13.1 ms: 1.07x slower                                                      |
| logging_simple           | 5.78 us                                                         | 6.23 us: 1.08x slower                                                      |
| mako                     | 6.36 ms                                                         | 6.85 ms: 1.08x slower                                                      |
| sympy_sum                | 84.4 ms                                                         | 91.1 ms: 1.08x slower                                                      |
| spectral_norm            | 63.7 ms                                                         | 69.0 ms: 1.08x slower                                                      |
| sqlglot_normalize        | 173 ms                                                          | 190 ms: 1.10x slower                                                       |
| telco                    | 4.67 ms                                                         | 5.12 ms: 1.10x slower                                                      |
| xml_etree_generate       | 53.2 ms                                                         | 58.4 ms: 1.10x slower                                                      |
| 2to3                     | 207 ms                                                          | 227 ms: 1.10x slower                                                       |
| python_startup           | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                      |
| pylint                   | 205 ms                                                          | 226 ms: 1.11x slower                                                       |
| sqlglot_optimize         | 32.7 ms                                                         | 36.2 ms: 1.11x slower                                                      |
| json_dumps               | 5.61 ms                                                         | 6.21 ms: 1.11x slower                                                      |
| coroutines               | 12.8 ms                                                         | 14.1 ms: 1.11x slower                                                      |
| sympy_str                | 159 ms                                                          | 177 ms: 1.11x slower                                                       |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.79 ms: 1.11x slower                                                      |
| asyncio_tcp              | 471 ms                                                          | 525 ms: 1.11x slower                                                       |
| python_startup_no_site   | 16.2 ms                                                         | 18.1 ms: 1.11x slower                                                      |
| async_generators         | 223 ms                                                          | 249 ms: 1.12x slower                                                       |
| mdp                      | 1.31 sec                                                        | 1.47 sec: 1.12x slower                                                     |
| typing_runtime_protocols | 101 us                                                          | 113 us: 1.12x slower                                                       |
| chaos                    | 38.4 ms                                                         | 43.0 ms: 1.12x slower                                                      |
| nqueens                  | 56.7 ms                                                         | 63.8 ms: 1.13x slower                                                      |
| xml_etree_process        | 36.4 ms                                                         | 41.2 ms: 1.13x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 79.0 ms: 1.13x slower                                                      |
| sympy_expand             | 271 ms                                                          | 307 ms: 1.13x slower                                                       |
| html5lib                 | 35.0 ms                                                         | 39.9 ms: 1.14x slower                                                      |
| comprehensions           | 10.4 us                                                         | 11.9 us: 1.14x slower                                                      |
| scimark_lu               | 56.6 ms                                                         | 64.7 ms: 1.14x slower                                                      |
| tornado_http             | 81.8 ms                                                         | 93.8 ms: 1.15x slower                                                      |
| unpickle                 | 8.40 us                                                         | 9.64 us: 1.15x slower                                                      |
| django_template          | 21.7 ms                                                         | 24.9 ms: 1.15x slower                                                      |
| float                    | 49.7 ms                                                         | 57.2 ms: 1.15x slower                                                      |
| pyflate                  | 279 ms                                                          | 321 ms: 1.15x slower                                                       |
| pprint_pformat           | 966 ms                                                          | 1.12 sec: 1.16x slower                                                     |
| coverage                 | 42.1 ms                                                         | 48.6 ms: 1.16x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 1.10 ms: 1.16x slower                                                      |
| dulwich_log              | 38.0 ms                                                         | 44.1 ms: 1.16x slower                                                      |
| pprint_safe_repr         | 474 ms                                                          | 549 ms: 1.16x slower                                                       |
| genshi_xml               | 31.6 ms                                                         | 36.6 ms: 1.16x slower                                                      |
| regex_compile            | 78.0 ms                                                         | 90.8 ms: 1.16x slower                                                      |
| raytrace                 | 162 ms                                                          | 191 ms: 1.18x slower                                                       |
| logging_silent           | 52.9 ns                                                         | 62.5 ns: 1.18x slower                                                      |
| tomli_loads              | 1.35 sec                                                        | 1.60 sec: 1.19x slower                                                     |
| genshi_text              | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                      |
| sqlglot_parse            | 748 us                                                          | 892 us: 1.19x slower                                                       |
| fannkuch                 | 243 ms                                                          | 291 ms: 1.20x slower                                                       |
| richards_super           | 30.2 ms                                                         | 36.1 ms: 1.20x slower                                                      |
| deltablue                | 1.88 ms                                                         | 2.26 ms: 1.20x slower                                                      |
| scimark_fft              | 171 ms                                                          | 205 ms: 1.20x slower                                                       |
| richards                 | 26.7 ms                                                         | 32.1 ms: 1.20x slower                                                      |
| hexiom                   | 3.72 ms                                                         | 4.50 ms: 1.21x slower                                                      |
| scimark_sor              | 75.3 ms                                                         | 91.5 ms: 1.21x slower                                                      |
| pickle_pure_python       | 175 us                                                          | 213 us: 1.21x slower                                                       |
| unpickle_pure_python     | 122 us                                                          | 150 us: 1.23x slower                                                       |
| nbody                    | 67.6 ms                                                         | 84.6 ms: 1.25x slower                                                      |
| scimark_monte_carlo      | 39.1 ms                                                         | 50.4 ms: 1.29x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (12): regex_v8, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, json, async_tree_none, gc_traversal, regex_effbot, json_loads, pycparser, async_tree_cpu_io_mixed_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown