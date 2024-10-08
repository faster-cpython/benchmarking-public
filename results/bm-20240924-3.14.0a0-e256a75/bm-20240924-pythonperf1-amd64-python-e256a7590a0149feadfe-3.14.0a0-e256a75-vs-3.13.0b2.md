# Results vs. 3.13.0b2

- fork: python
- ref: e256a7590a0149feadfe
- machine: windows-amd64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 222 ms: 1.07x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.71 sec: 1.05x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.5 ms: 1.16x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 83.1 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                           | 1.07x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg | 605 ms                                                          | 553 ms: 1.09x faster                                                       |
| async_tree_none  | 218 ms                                                          | 207 ms: 1.05x faster                                                       |
| async_tree_io    | 588 ms                                                          | 566 ms: 1.04x faster                                                       |
| Geometric mean   | (ref)                                                           | 1.03x faster                                                               |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 55.2 ms: 1.11x slower                                                      |
| nbody          | 67.6 ms                                                         | 83.2 ms: 1.23x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.7 ms: 1.07x faster                                                      |
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 90.4 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                           | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.11 us                                                         | 7.04 us: 1.01x faster                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.5 ms: 1.02x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 18.5 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 63.9 ms: 1.03x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.8 us: 1.04x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.77 us: 1.06x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.7 ms: 1.09x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.39 us: 1.12x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 40.9 ms: 1.12x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.35 ms: 1.13x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.59 sec: 1.18x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 212 us: 1.21x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 149 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.2 ms: 1.10x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.81 ms: 1.07x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 35.4 ms: 1.12x slower                                                      |
| django_template | 21.7 ms                                                         | 24.8 ms: 1.14x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.0 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 523 us: 15.51x faster                                                      |
| deepcopy                 | 220 us                                                          | 193 us: 1.14x faster                                                       |
| async_tree_io_tg         | 605 ms                                                          | 553 ms: 1.09x faster                                                       |
| regex_v8                 | 15.8 ms                                                         | 14.7 ms: 1.07x faster                                                      |
| deepcopy_memo            | 22.1 us                                                         | 20.8 us: 1.06x faster                                                      |
| async_tree_none          | 218 ms                                                          | 207 ms: 1.05x faster                                                       |
| async_tree_io            | 588 ms                                                          | 566 ms: 1.04x faster                                                       |
| deepcopy_reduce          | 1.99 us                                                         | 1.94 us: 1.03x faster                                                      |
| gc_traversal             | 1.55 ms                                                         | 1.53 ms: 1.02x faster                                                      |
| regex_dna                | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| pickle                   | 7.11 us                                                         | 7.04 us: 1.01x faster                                                      |
| regex_effbot             | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| tornado_http             | 81.8 ms                                                         | 83.1 ms: 1.02x slower                                                      |
| xml_etree_parse          | 90.9 ms                                                         | 92.5 ms: 1.02x slower                                                      |
| bench_mp_pool            | 64.8 ms                                                         | 66.0 ms: 1.02x slower                                                      |
| pickle_dict              | 18.1 us                                                         | 18.5 us: 1.02x slower                                                      |
| sqlite_synth             | 1.60 us                                                         | 1.63 us: 1.02x slower                                                      |
| xml_etree_iterparse      | 62.3 ms                                                         | 63.9 ms: 1.03x slower                                                      |
| json_loads               | 14.2 us                                                         | 14.8 us: 1.04x slower                                                      |
| bench_thread_pool        | 768 us                                                          | 802 us: 1.05x slower                                                       |
| crypto_pyaes             | 45.5 ms                                                         | 47.8 ms: 1.05x slower                                                      |
| docutils                 | 1.63 sec                                                        | 1.71 sec: 1.05x slower                                                     |
| go                       | 82.1 ms                                                         | 86.6 ms: 1.06x slower                                                      |
| unpickle_list            | 2.62 us                                                         | 2.77 us: 1.06x slower                                                      |
| sympy_sum                | 84.4 ms                                                         | 89.7 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.66 ms: 1.07x slower                                                      |
| mako                     | 6.36 ms                                                         | 6.81 ms: 1.07x slower                                                      |
| sympy_integrate          | 12.2 ms                                                         | 13.1 ms: 1.07x slower                                                      |
| generators               | 19.6 ms                                                         | 21.0 ms: 1.07x slower                                                      |
| 2to3                     | 207 ms                                                          | 222 ms: 1.07x slower                                                       |
| xml_etree_generate       | 53.2 ms                                                         | 57.7 ms: 1.09x slower                                                      |
| typing_runtime_protocols | 101 us                                                          | 110 us: 1.09x slower                                                       |
| async_generators         | 223 ms                                                          | 243 ms: 1.09x slower                                                       |
| telco                    | 4.67 ms                                                         | 5.09 ms: 1.09x slower                                                      |
| pylint                   | 205 ms                                                          | 224 ms: 1.09x slower                                                       |
| spectral_norm            | 63.7 ms                                                         | 69.8 ms: 1.09x slower                                                      |
| python_startup           | 20.3 ms                                                         | 22.2 ms: 1.10x slower                                                      |
| logging_simple           | 5.78 us                                                         | 6.35 us: 1.10x slower                                                      |
| logging_format           | 6.22 us                                                         | 6.85 us: 1.10x slower                                                      |
| mdp                      | 1.31 sec                                                        | 1.44 sec: 1.10x slower                                                     |
| scimark_lu               | 56.6 ms                                                         | 62.5 ms: 1.10x slower                                                      |
| sympy_str                | 159 ms                                                          | 176 ms: 1.11x slower                                                       |
| sqlglot_optimize         | 32.7 ms                                                         | 36.3 ms: 1.11x slower                                                      |
| float                    | 49.7 ms                                                         | 55.2 ms: 1.11x slower                                                      |
| chaos                    | 38.4 ms                                                         | 42.7 ms: 1.11x slower                                                      |
| sqlglot_normalize        | 173 ms                                                          | 193 ms: 1.12x slower                                                       |
| unpickle                 | 8.40 us                                                         | 9.39 us: 1.12x slower                                                      |
| genshi_xml               | 31.6 ms                                                         | 35.4 ms: 1.12x slower                                                      |
| xml_etree_process        | 36.4 ms                                                         | 40.9 ms: 1.12x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 78.6 ms: 1.13x slower                                                      |
| dulwich_log              | 38.0 ms                                                         | 42.8 ms: 1.13x slower                                                      |
| sympy_expand             | 271 ms                                                          | 306 ms: 1.13x slower                                                       |
| json_dumps               | 5.61 ms                                                         | 6.35 ms: 1.13x slower                                                      |
| coroutines               | 12.8 ms                                                         | 14.5 ms: 1.14x slower                                                      |
| python_startup_no_site   | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                      |
| comprehensions           | 10.4 us                                                         | 11.9 us: 1.14x slower                                                      |
| pprint_safe_repr         | 474 ms                                                          | 542 ms: 1.14x slower                                                       |
| django_template          | 21.7 ms                                                         | 24.8 ms: 1.14x slower                                                      |
| pyflate                  | 279 ms                                                          | 322 ms: 1.16x slower                                                       |
| nqueens                  | 56.7 ms                                                         | 65.5 ms: 1.16x slower                                                      |
| html5lib                 | 35.0 ms                                                         | 40.5 ms: 1.16x slower                                                      |
| pprint_pformat           | 966 ms                                                          | 1.12 sec: 1.16x slower                                                     |
| regex_compile            | 78.0 ms                                                         | 90.4 ms: 1.16x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 1.11 ms: 1.16x slower                                                      |
| raytrace                 | 162 ms                                                          | 189 ms: 1.17x slower                                                       |
| coverage                 | 42.1 ms                                                         | 49.3 ms: 1.17x slower                                                      |
| hexiom                   | 3.72 ms                                                         | 4.39 ms: 1.18x slower                                                      |
| tomli_loads              | 1.35 sec                                                        | 1.59 sec: 1.18x slower                                                     |
| genshi_text              | 14.4 ms                                                         | 17.0 ms: 1.19x slower                                                      |
| sqlglot_parse            | 748 us                                                          | 888 us: 1.19x slower                                                       |
| scimark_fft              | 171 ms                                                          | 204 ms: 1.19x slower                                                       |
| pickle_pure_python       | 175 us                                                          | 212 us: 1.21x slower                                                       |
| logging_silent           | 52.9 ns                                                         | 63.8 ns: 1.21x slower                                                      |
| richards_super           | 30.2 ms                                                         | 36.4 ms: 1.21x slower                                                      |
| richards                 | 26.7 ms                                                         | 32.3 ms: 1.21x slower                                                      |
| deltablue                | 1.88 ms                                                         | 2.28 ms: 1.21x slower                                                      |
| unpickle_pure_python     | 122 us                                                          | 149 us: 1.23x slower                                                       |
| fannkuch                 | 243 ms                                                          | 299 ms: 1.23x slower                                                       |
| nbody                    | 67.6 ms                                                         | 83.2 ms: 1.23x slower                                                      |
| scimark_sor              | 75.3 ms                                                         | 93.1 ms: 1.24x slower                                                      |
| scimark_monte_carlo      | 39.1 ms                                                         | 49.0 ms: 1.25x slower                                                      |
| json                     | 3.19 ms                                                         | 4.50 ms: 1.41x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (12): async_tree_memoization_tg, pycparser, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, create_gc_cycles, asyncio_tcp, asyncio_tcp_ssl, pathlib, pidigits, async_tree_cpu_io_mixed_tg, pickle_list
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown