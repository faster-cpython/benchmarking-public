# Results vs. 3.13.0b2

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-amd64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.01x slower
- HPT reliability: 99.74%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 242 ms: 1.17x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.85 sec: 1.14x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.1 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 95.2 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                           | 1.17x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg   | 605 ms                                                          | 540 ms: 1.12x faster                                                       |
| async_tree_io      | 588 ms                                                          | 553 ms: 1.06x faster                                                       |
| async_tree_none_tg | 202 ms                                                          | 194 ms: 1.04x faster                                                       |
| Geometric mean     | (ref)                                                           | 1.03x faster                                                               |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 50.1 ms: 1.35x faster                                                      |
| float          | 49.7 ms                                                         | 45.0 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                           | 1.14x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.61 ms: 1.02x slower                                                      |
| regex_compile  | 78.0 ms                                                         | 91.0 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.26 sec: 1.07x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 52.6 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.8 ms: 1.01x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 37.6 ms: 1.03x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 182 us: 1.04x slower                                                       |
| xml_etree_parse      | 90.9 ms                                                         | 95.5 ms: 1.05x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.96 ms: 1.06x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 138 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.4 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.05 ms: 1.26x faster                                                      |
| django_template | 21.7 ms                                                         | 25.7 ms: 1.18x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.9 ms: 1.25x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 40.0 ms: 1.27x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.10x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 520 us: 15.58x faster                                                      |
| spectral_norm            | 63.7 ms                                                         | 45.0 ms: 1.42x faster                                                      |
| deepcopy_memo            | 22.1 us                                                         | 15.7 us: 1.40x faster                                                      |
| nbody                    | 67.6 ms                                                         | 50.1 ms: 1.35x faster                                                      |
| mako                     | 6.36 ms                                                         | 5.05 ms: 1.26x faster                                                      |
| scimark_sor              | 75.3 ms                                                         | 60.4 ms: 1.25x faster                                                      |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.10 ms: 1.19x faster                                                      |
| scimark_fft              | 171 ms                                                          | 147 ms: 1.16x faster                                                       |
| deepcopy                 | 220 us                                                          | 193 us: 1.14x faster                                                       |
| fannkuch                 | 243 ms                                                          | 214 ms: 1.14x faster                                                       |
| crypto_pyaes             | 45.5 ms                                                         | 40.3 ms: 1.13x faster                                                      |
| async_tree_io_tg         | 605 ms                                                          | 540 ms: 1.12x faster                                                       |
| pyflate                  | 279 ms                                                          | 251 ms: 1.11x faster                                                       |
| float                    | 49.7 ms                                                         | 45.0 ms: 1.11x faster                                                      |
| deepcopy_reduce          | 1.99 us                                                         | 1.85 us: 1.08x faster                                                      |
| tomli_loads              | 1.35 sec                                                        | 1.26 sec: 1.07x faster                                                     |
| json                     | 3.19 ms                                                         | 2.99 ms: 1.07x faster                                                      |
| async_tree_io            | 588 ms                                                          | 553 ms: 1.06x faster                                                       |
| scimark_lu               | 56.6 ms                                                         | 54.0 ms: 1.05x faster                                                      |
| async_tree_none_tg       | 202 ms                                                          | 194 ms: 1.04x faster                                                       |
| telco                    | 4.67 ms                                                         | 4.61 ms: 1.01x faster                                                      |
| xml_etree_generate       | 53.2 ms                                                         | 52.6 ms: 1.01x faster                                                      |
| xml_etree_iterparse      | 62.3 ms                                                         | 61.8 ms: 1.01x faster                                                      |
| json_loads               | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| gc_traversal             | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                      |
| regex_effbot             | 1.58 ms                                                         | 1.61 ms: 1.02x slower                                                      |
| comprehensions           | 10.4 us                                                         | 10.6 us: 1.02x slower                                                      |
| pprint_safe_repr         | 474 ms                                                          | 484 ms: 1.02x slower                                                       |
| logging_format           | 6.22 us                                                         | 6.39 us: 1.03x slower                                                      |
| logging_simple           | 5.78 us                                                         | 5.94 us: 1.03x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 71.8 ms: 1.03x slower                                                      |
| pprint_pformat           | 966 ms                                                          | 993 ms: 1.03x slower                                                       |
| xml_etree_process        | 36.4 ms                                                         | 37.6 ms: 1.03x slower                                                      |
| pickle_pure_python       | 175 us                                                          | 182 us: 1.04x slower                                                       |
| chaos                    | 38.4 ms                                                         | 39.9 ms: 1.04x slower                                                      |
| create_gc_cycles         | 888 us                                                          | 925 us: 1.04x slower                                                       |
| xml_etree_parse          | 90.9 ms                                                         | 95.5 ms: 1.05x slower                                                      |
| json_dumps               | 5.61 ms                                                         | 5.96 ms: 1.06x slower                                                      |
| pathlib                  | 75.9 ms                                                         | 81.4 ms: 1.07x slower                                                      |
| bench_thread_pool        | 768 us                                                          | 826 us: 1.08x slower                                                       |
| coroutines               | 12.8 ms                                                         | 13.8 ms: 1.08x slower                                                      |
| logging_silent           | 52.9 ns                                                         | 57.2 ns: 1.08x slower                                                      |
| python_startup           | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| nqueens                  | 56.7 ms                                                         | 62.7 ms: 1.11x slower                                                      |
| sqlglot_normalize        | 173 ms                                                          | 194 ms: 1.12x slower                                                       |
| sqlglot_parse            | 748 us                                                          | 838 us: 1.12x slower                                                       |
| mdp                      | 1.31 sec                                                        | 1.47 sec: 1.12x slower                                                     |
| sqlglot_optimize         | 32.7 ms                                                         | 36.9 ms: 1.13x slower                                                      |
| unpickle_pure_python     | 122 us                                                          | 138 us: 1.13x slower                                                       |
| coverage                 | 42.1 ms                                                         | 47.7 ms: 1.13x slower                                                      |
| python_startup_no_site   | 16.2 ms                                                         | 18.4 ms: 1.13x slower                                                      |
| bench_mp_pool            | 64.8 ms                                                         | 73.7 ms: 1.14x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 1.09 ms: 1.14x slower                                                      |
| richards                 | 26.7 ms                                                         | 30.4 ms: 1.14x slower                                                      |
| dulwich_log              | 38.0 ms                                                         | 43.4 ms: 1.14x slower                                                      |
| docutils                 | 1.63 sec                                                        | 1.85 sec: 1.14x slower                                                     |
| generators               | 19.6 ms                                                         | 22.5 ms: 1.15x slower                                                      |
| typing_runtime_protocols | 101 us                                                          | 116 us: 1.15x slower                                                       |
| richards_super           | 30.2 ms                                                         | 35.0 ms: 1.16x slower                                                      |
| tornado_http             | 81.8 ms                                                         | 95.2 ms: 1.16x slower                                                      |
| sympy_sum                | 84.4 ms                                                         | 98.4 ms: 1.17x slower                                                      |
| async_generators         | 223 ms                                                          | 261 ms: 1.17x slower                                                       |
| regex_compile            | 78.0 ms                                                         | 91.0 ms: 1.17x slower                                                      |
| 2to3                     | 207 ms                                                          | 242 ms: 1.17x slower                                                       |
| raytrace                 | 162 ms                                                          | 190 ms: 1.17x slower                                                       |
| django_template          | 21.7 ms                                                         | 25.7 ms: 1.18x slower                                                      |
| html5lib                 | 35.0 ms                                                         | 42.1 ms: 1.20x slower                                                      |
| sympy_str                | 159 ms                                                          | 192 ms: 1.20x slower                                                       |
| pylint                   | 205 ms                                                          | 248 ms: 1.21x slower                                                       |
| sympy_integrate          | 12.2 ms                                                         | 14.9 ms: 1.22x slower                                                      |
| sympy_expand             | 271 ms                                                          | 334 ms: 1.23x slower                                                       |
| go                       | 82.1 ms                                                         | 102 ms: 1.24x slower                                                       |
| deltablue                | 1.88 ms                                                         | 2.34 ms: 1.24x slower                                                      |
| genshi_text              | 14.4 ms                                                         | 17.9 ms: 1.25x slower                                                      |
| genshi_xml               | 31.6 ms                                                         | 40.0 ms: 1.27x slower                                                      |
| hexiom                   | 3.72 ms                                                         | 4.79 ms: 1.29x slower                                                      |
| asyncio_tcp              | 471 ms                                                          | 632 ms: 1.34x slower                                                       |
| Geometric mean           | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (11): regex_v8, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, pidigits, async_tree_memoization, scimark_monte_carlo, regex_dna, async_tree_cpu_io_mixed, asyncio_tcp_ssl, pycparser
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.74% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown