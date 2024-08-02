# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-amd64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 210 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (4): chameleon, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none | 218 ms                                                          | 225 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| nbody          | 67.6 ms                                                         | 68.7 ms: 1.02x slower                                                      |
| float          | 49.7 ms                                                         | 50.5 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                           | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 76.7 ms: 1.02x faster                                                      |
| regex_dna      | 119 ms                                                          | 117 ms: 1.02x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                           | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.7 us: 1.04x faster                                                      |
| xml_etree_process    | 36.4 ms                                                         | 36.6 ms: 1.00x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 18.3 us: 1.01x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.36 sec: 1.01x slower                                                     |
| xml_etree_parse      | 90.9 ms                                                         | 91.8 ms: 1.01x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 53.7 ms: 1.01x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 177 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 63.3 ms: 1.02x slower                                                      |
| pickle               | 7.11 us                                                         | 7.23 us: 1.02x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.77 ms: 1.03x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 126 us: 1.03x slower                                                       |
| unpickle             | 8.40 us                                                         | 8.73 us: 1.04x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.85 us: 1.09x slower                                                      |
| pickle_list          | 2.90 us                                                         | 3.26 us: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                      |
| python_startup         | 20.3 ms                                                         | 21.0 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 21.9 ms: 1.01x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 14.6 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 501 us: 16.18x faster                                                      |
| pycparser                | 754 ms                                                          | 684 ms: 1.10x faster                                                       |
| json                     | 3.19 ms                                                         | 2.92 ms: 1.09x faster                                                      |
| regex_v8                 | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                      |
| json_loads               | 14.2 us                                                         | 13.7 us: 1.04x faster                                                      |
| raytrace                 | 162 ms                                                          | 157 ms: 1.03x faster                                                       |
| regex_compile            | 78.0 ms                                                         | 76.7 ms: 1.02x faster                                                      |
| regex_dna                | 119 ms                                                          | 117 ms: 1.02x faster                                                       |
| typing_runtime_protocols | 101 us                                                          | 99.8 us: 1.01x faster                                                      |
| sympy_sum                | 84.4 ms                                                         | 83.6 ms: 1.01x faster                                                      |
| regex_effbot             | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| sqlite_synth             | 1.60 us                                                         | 1.59 us: 1.01x faster                                                      |
| logging_simple           | 5.78 us                                                         | 5.80 us: 1.00x slower                                                      |
| pidigits                 | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| sympy_expand             | 271 ms                                                          | 272 ms: 1.00x slower                                                       |
| xml_etree_process        | 36.4 ms                                                         | 36.6 ms: 1.00x slower                                                      |
| sympy_integrate          | 12.2 ms                                                         | 12.3 ms: 1.00x slower                                                      |
| logging_format           | 6.22 us                                                         | 6.26 us: 1.01x slower                                                      |
| coroutines               | 12.8 ms                                                         | 12.8 ms: 1.01x slower                                                      |
| telco                    | 4.67 ms                                                         | 4.70 ms: 1.01x slower                                                      |
| sympy_str                | 159 ms                                                          | 160 ms: 1.01x slower                                                       |
| pickle_dict              | 18.1 us                                                         | 18.3 us: 1.01x slower                                                      |
| generators               | 19.6 ms                                                         | 19.7 ms: 1.01x slower                                                      |
| django_template          | 21.7 ms                                                         | 21.9 ms: 1.01x slower                                                      |
| tomli_loads              | 1.35 sec                                                        | 1.36 sec: 1.01x slower                                                     |
| deltablue                | 1.88 ms                                                         | 1.90 ms: 1.01x slower                                                      |
| crypto_pyaes             | 45.5 ms                                                         | 45.9 ms: 1.01x slower                                                      |
| xml_etree_parse          | 90.9 ms                                                         | 91.8 ms: 1.01x slower                                                      |
| richards                 | 26.7 ms                                                         | 27.0 ms: 1.01x slower                                                      |
| xml_etree_generate       | 53.2 ms                                                         | 53.7 ms: 1.01x slower                                                      |
| pickle_pure_python       | 175 us                                                          | 177 us: 1.01x slower                                                       |
| gc_traversal             | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                      |
| sqlglot_normalize        | 173 ms                                                          | 175 ms: 1.01x slower                                                       |
| sqlglot_transpile        | 955 us                                                          | 966 us: 1.01x slower                                                       |
| nqueens                  | 56.7 ms                                                         | 57.4 ms: 1.01x slower                                                      |
| richards_super           | 30.2 ms                                                         | 30.6 ms: 1.01x slower                                                      |
| 2to3                     | 207 ms                                                          | 210 ms: 1.01x slower                                                       |
| nbody                    | 67.6 ms                                                         | 68.7 ms: 1.02x slower                                                      |
| spectral_norm            | 63.7 ms                                                         | 64.7 ms: 1.02x slower                                                      |
| genshi_text              | 14.4 ms                                                         | 14.6 ms: 1.02x slower                                                      |
| xml_etree_iterparse      | 62.3 ms                                                         | 63.3 ms: 1.02x slower                                                      |
| pickle                   | 7.11 us                                                         | 7.23 us: 1.02x slower                                                      |
| sqlglot_optimize         | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                      |
| float                    | 49.7 ms                                                         | 50.5 ms: 1.02x slower                                                      |
| go                       | 82.1 ms                                                         | 83.5 ms: 1.02x slower                                                      |
| sqlglot_parse            | 748 us                                                          | 762 us: 1.02x slower                                                       |
| pyflate                  | 279 ms                                                          | 284 ms: 1.02x slower                                                       |
| deepcopy_memo            | 22.1 us                                                         | 22.5 us: 1.02x slower                                                      |
| fannkuch                 | 243 ms                                                          | 249 ms: 1.02x slower                                                       |
| bench_mp_pool            | 64.8 ms                                                         | 66.2 ms: 1.02x slower                                                      |
| hexiom                   | 3.72 ms                                                         | 3.81 ms: 1.02x slower                                                      |
| logging_silent           | 52.9 ns                                                         | 54.1 ns: 1.02x slower                                                      |
| python_startup_no_site   | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 71.5 ms: 1.02x slower                                                      |
| scimark_lu               | 56.6 ms                                                         | 58.1 ms: 1.03x slower                                                      |
| json_dumps               | 5.61 ms                                                         | 5.77 ms: 1.03x slower                                                      |
| create_gc_cycles         | 888 us                                                          | 916 us: 1.03x slower                                                       |
| pprint_pformat           | 966 ms                                                          | 997 ms: 1.03x slower                                                       |
| async_tree_none          | 218 ms                                                          | 225 ms: 1.03x slower                                                       |
| unpickle_pure_python     | 122 us                                                          | 126 us: 1.03x slower                                                       |
| pathlib                  | 75.9 ms                                                         | 78.7 ms: 1.04x slower                                                      |
| python_startup           | 20.3 ms                                                         | 21.0 ms: 1.04x slower                                                      |
| pprint_safe_repr         | 474 ms                                                          | 492 ms: 1.04x slower                                                       |
| unpickle                 | 8.40 us                                                         | 8.73 us: 1.04x slower                                                      |
| scimark_sor              | 75.3 ms                                                         | 78.5 ms: 1.04x slower                                                      |
| bench_thread_pool        | 768 us                                                          | 802 us: 1.04x slower                                                       |
| scimark_monte_carlo      | 39.1 ms                                                         | 41.2 ms: 1.05x slower                                                      |
| scimark_fft              | 171 ms                                                          | 181 ms: 1.06x slower                                                       |
| mdp                      | 1.31 sec                                                        | 1.41 sec: 1.08x slower                                                     |
| unpickle_list            | 2.62 us                                                         | 2.85 us: 1.09x slower                                                      |
| coverage                 | 42.1 ms                                                         | 46.3 ms: 1.10x slower                                                      |
| pickle_list              | 2.90 us                                                         | 3.26 us: 1.12x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (23): asyncio_tcp_ssl, genshi_xml, docutils, asyncio_tcp, tornado_http, chaos, flaskblogging, async_generators, chameleon, scimark_sparse_mat_mult, deepcopy_reduce, deepcopy, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, html5lib, comprehensions, mako, async_tree_none_tg, async_tree_cpu_io_mixed, pylint, async_tree_memoization, async_tree_io
Ignored benchmarks (3) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, dulwich_log, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown