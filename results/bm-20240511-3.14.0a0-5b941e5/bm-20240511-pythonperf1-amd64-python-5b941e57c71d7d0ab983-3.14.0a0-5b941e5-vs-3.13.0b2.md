# Results vs. 3.13.0b2

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-amd64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.02x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 209 ms: 1.01x slower                                                       |
| chameleon      | 4.80 ms                                                         | 4.74 ms: 1.01x faster                                                      |
| html5lib       | 35.0 ms                                                         | 34.1 ms: 1.03x faster                                                      |
| tornado_http   | 81.8 ms                                                         | 82.5 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                           | 1.00x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 48.8 ms: 1.02x faster                                                      |
| nbody          | 67.6 ms                                                         | 68.4 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                           | 1.00x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 78.0 ms                                                         | 77.4 ms: 1.01x faster                                                      |
| regex_dna      | 119 ms                                                          | 119 ms: 1.00x slower                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 122 us                                                          | 119 us: 1.02x faster                                                       |
| json_dumps           | 5.61 ms                                                         | 5.53 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.5 ms: 1.01x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.0 us: 1.01x faster                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 52.7 ms: 1.01x faster                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 90.1 ms: 1.01x faster                                                      |
| xml_etree_process    | 36.4 ms                                                         | 36.3 ms: 1.00x faster                                                      |
| pickle               | 7.11 us                                                         | 7.17 us: 1.01x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 177 us: 1.01x slower                                                       |
| pickle_dict          | 18.1 us                                                         | 18.3 us: 1.01x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.38 sec: 1.03x slower                                                     |
| unpickle             | 8.40 us                                                         | 8.88 us: 1.06x slower                                                      |
| pickle_list          | 2.90 us                                                         | 3.11 us: 1.07x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.83 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.5 ms: 1.01x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.1 ms: 1.06x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.20 ms: 1.02x faster                                                      |
| django_template | 21.7 ms                                                         | 22.0 ms: 1.02x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 14.7 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 493 us: 16.43x faster                                                      |
| spectral_norm            | 63.7 ms                                                         | 62.1 ms: 1.03x faster                                                      |
| scimark_lu               | 56.6 ms                                                         | 55.1 ms: 1.03x faster                                                      |
| html5lib                 | 35.0 ms                                                         | 34.1 ms: 1.03x faster                                                      |
| mako                     | 6.36 ms                                                         | 6.20 ms: 1.02x faster                                                      |
| generators               | 19.6 ms                                                         | 19.1 ms: 1.02x faster                                                      |
| unpickle_pure_python     | 122 us                                                          | 119 us: 1.02x faster                                                       |
| deepcopy_reduce          | 1.99 us                                                         | 1.96 us: 1.02x faster                                                      |
| float                    | 49.7 ms                                                         | 48.8 ms: 1.02x faster                                                      |
| scimark_sor              | 75.3 ms                                                         | 74.1 ms: 1.02x faster                                                      |
| json_dumps               | 5.61 ms                                                         | 5.53 ms: 1.02x faster                                                      |
| chameleon                | 4.80 ms                                                         | 4.74 ms: 1.01x faster                                                      |
| xml_etree_iterparse      | 62.3 ms                                                         | 61.5 ms: 1.01x faster                                                      |
| typing_runtime_protocols | 101 us                                                          | 99.6 us: 1.01x faster                                                      |
| json_loads               | 14.2 us                                                         | 14.0 us: 1.01x faster                                                      |
| gc_traversal             | 1.55 ms                                                         | 1.54 ms: 1.01x faster                                                      |
| hexiom                   | 3.72 ms                                                         | 3.68 ms: 1.01x faster                                                      |
| xml_etree_generate       | 53.2 ms                                                         | 52.7 ms: 1.01x faster                                                      |
| xml_etree_parse          | 90.9 ms                                                         | 90.1 ms: 1.01x faster                                                      |
| deepcopy                 | 220 us                                                          | 218 us: 1.01x faster                                                       |
| regex_compile            | 78.0 ms                                                         | 77.4 ms: 1.01x faster                                                      |
| go                       | 82.1 ms                                                         | 81.4 ms: 1.01x faster                                                      |
| pprint_safe_repr         | 474 ms                                                          | 471 ms: 1.01x faster                                                       |
| sympy_integrate          | 12.2 ms                                                         | 12.2 ms: 1.01x faster                                                      |
| xml_etree_process        | 36.4 ms                                                         | 36.3 ms: 1.00x faster                                                      |
| pprint_pformat           | 966 ms                                                          | 963 ms: 1.00x faster                                                       |
| regex_dna                | 119 ms                                                          | 119 ms: 1.00x slower                                                       |
| sympy_expand             | 271 ms                                                          | 272 ms: 1.01x slower                                                       |
| sympy_str                | 159 ms                                                          | 160 ms: 1.01x slower                                                       |
| sympy_sum                | 84.4 ms                                                         | 84.9 ms: 1.01x slower                                                      |
| logging_format           | 6.22 us                                                         | 6.27 us: 1.01x slower                                                      |
| logging_simple           | 5.78 us                                                         | 5.82 us: 1.01x slower                                                      |
| pickle                   | 7.11 us                                                         | 7.17 us: 1.01x slower                                                      |
| pickle_pure_python       | 175 us                                                          | 177 us: 1.01x slower                                                       |
| tornado_http             | 81.8 ms                                                         | 82.5 ms: 1.01x slower                                                      |
| deepcopy_memo            | 22.1 us                                                         | 22.3 us: 1.01x slower                                                      |
| python_startup           | 20.3 ms                                                         | 20.5 ms: 1.01x slower                                                      |
| pickle_dict              | 18.1 us                                                         | 18.3 us: 1.01x slower                                                      |
| 2to3                     | 207 ms                                                          | 209 ms: 1.01x slower                                                       |
| nbody                    | 67.6 ms                                                         | 68.4 ms: 1.01x slower                                                      |
| sqlglot_normalize        | 173 ms                                                          | 175 ms: 1.01x slower                                                       |
| sqlite_synth             | 1.60 us                                                         | 1.62 us: 1.01x slower                                                      |
| pyflate                  | 279 ms                                                          | 282 ms: 1.01x slower                                                       |
| nqueens                  | 56.7 ms                                                         | 57.4 ms: 1.01x slower                                                      |
| django_template          | 21.7 ms                                                         | 22.0 ms: 1.02x slower                                                      |
| sqlglot_optimize         | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                      |
| deltablue                | 1.88 ms                                                         | 1.92 ms: 1.02x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 973 us: 1.02x slower                                                       |
| telco                    | 4.67 ms                                                         | 4.77 ms: 1.02x slower                                                      |
| sqlglot_parse            | 748 us                                                          | 764 us: 1.02x slower                                                       |
| tomli_loads              | 1.35 sec                                                        | 1.38 sec: 1.03x slower                                                     |
| genshi_text              | 14.4 ms                                                         | 14.7 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.57 ms: 1.03x slower                                                      |
| coverage                 | 42.1 ms                                                         | 43.2 ms: 1.03x slower                                                      |
| regex_effbot             | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| fannkuch                 | 243 ms                                                          | 251 ms: 1.03x slower                                                       |
| richards                 | 26.7 ms                                                         | 27.5 ms: 1.03x slower                                                      |
| async_generators         | 223 ms                                                          | 230 ms: 1.03x slower                                                       |
| raytrace                 | 162 ms                                                          | 167 ms: 1.03x slower                                                       |
| meteor_contest           | 69.9 ms                                                         | 72.4 ms: 1.04x slower                                                      |
| richards_super           | 30.2 ms                                                         | 31.3 ms: 1.04x slower                                                      |
| crypto_pyaes             | 45.5 ms                                                         | 47.5 ms: 1.04x slower                                                      |
| pathlib                  | 75.9 ms                                                         | 79.9 ms: 1.05x slower                                                      |
| python_startup_no_site   | 16.2 ms                                                         | 17.1 ms: 1.06x slower                                                      |
| unpickle                 | 8.40 us                                                         | 8.88 us: 1.06x slower                                                      |
| scimark_fft              | 171 ms                                                          | 182 ms: 1.06x slower                                                       |
| bench_thread_pool        | 768 us                                                          | 818 us: 1.07x slower                                                       |
| scimark_monte_carlo      | 39.1 ms                                                         | 41.7 ms: 1.07x slower                                                      |
| pickle_list              | 2.90 us                                                         | 3.11 us: 1.07x slower                                                      |
| bench_mp_pool            | 64.8 ms                                                         | 69.7 ms: 1.08x slower                                                      |
| unpickle_list            | 2.62 us                                                         | 2.83 us: 1.08x slower                                                      |
| mdp                      | 1.31 sec                                                        | 1.43 sec: 1.09x slower                                                     |
| asyncio_tcp              | 471 ms                                                          | 564 ms: 1.20x slower                                                       |
| Geometric mean           | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (22): pycparser, json, regex_v8, async_tree_cpu_io_mixed, comprehensions, docutils, chaos, async_tree_io, flaskblogging, async_tree_cpu_io_mixed_tg, coroutines, logging_silent, pidigits, async_tree_io_tg, create_gc_cycles, pylint, async_tree_none, async_tree_memoization, asyncio_tcp_ssl, genshi_xml, async_tree_none_tg, async_tree_memoization_tg
Ignored benchmarks (3) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, dulwich_log, mypy2

# HPT report

- Reliability score: 99.84% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown