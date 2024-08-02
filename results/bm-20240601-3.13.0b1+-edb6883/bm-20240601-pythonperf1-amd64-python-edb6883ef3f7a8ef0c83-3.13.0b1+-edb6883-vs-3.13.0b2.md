# Results vs. 3.13.0b2

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: windows-amd64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.01x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 208 ms: 1.01x slower                                                        |
| chameleon      | 4.80 ms                                                         | 4.86 ms: 1.01x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.61 sec: 1.01x faster                                                      |
| html5lib       | 35.0 ms                                                         | 35.4 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 70.9 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 116 ms: 1.03x faster                                                        |
| regex_effbot   | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.8 us: 1.02x faster                                                       |
| xml_etree_parse      | 90.9 ms                                                         | 90.2 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.9 ms: 1.01x faster                                                       |
| pickle               | 7.11 us                                                         | 7.20 us: 1.01x slower                                                       |
| pickle_dict          | 18.1 us                                                         | 18.5 us: 1.02x slower                                                       |
| pickle_pure_python   | 175 us                                                          | 179 us: 1.02x slower                                                        |
| tomli_loads          | 1.35 sec                                                        | 1.38 sec: 1.02x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.69 us: 1.03x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 125 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (5): xml_etree_process, xml_etree_generate, unpickle, json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 20.3 ms                                                         | 20.1 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 21.8 ms: 1.01x slower                                                       |
| genshi_xml      | 31.6 ms                                                         | 31.9 ms: 1.01x slower                                                       |
| mako            | 6.36 ms                                                         | 6.51 ms: 1.02x slower                                                       |
| genshi_text     | 14.4 ms                                                         | 14.7 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json                     | 3.19 ms                                                         | 3.00 ms: 1.06x faster                                                       |
| scimark_lu               | 56.6 ms                                                         | 54.2 ms: 1.04x faster                                                       |
| regex_dna                | 119 ms                                                          | 116 ms: 1.03x faster                                                        |
| json_loads               | 14.2 us                                                         | 13.8 us: 1.02x faster                                                       |
| regex_effbot             | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                       |
| generators               | 19.6 ms                                                         | 19.2 ms: 1.02x faster                                                       |
| raytrace                 | 162 ms                                                          | 160 ms: 1.02x faster                                                        |
| pathlib                  | 75.9 ms                                                         | 74.8 ms: 1.01x faster                                                       |
| telco                    | 4.67 ms                                                         | 4.62 ms: 1.01x faster                                                       |
| sympy_sum                | 84.4 ms                                                         | 83.5 ms: 1.01x faster                                                       |
| docutils                 | 1.63 sec                                                        | 1.61 sec: 1.01x faster                                                      |
| python_startup           | 20.3 ms                                                         | 20.1 ms: 1.01x faster                                                       |
| xml_etree_parse          | 90.9 ms                                                         | 90.2 ms: 1.01x faster                                                       |
| thrift                   | 8.11 ms                                                         | 8.05 ms: 1.01x faster                                                       |
| xml_etree_iterparse      | 62.3 ms                                                         | 61.9 ms: 1.01x faster                                                       |
| deepcopy_reduce          | 1.99 us                                                         | 1.98 us: 1.01x faster                                                       |
| coroutines               | 12.8 ms                                                         | 12.7 ms: 1.01x faster                                                       |
| deepcopy                 | 220 us                                                          | 218 us: 1.01x faster                                                        |
| sqlite_synth             | 1.60 us                                                         | 1.59 us: 1.00x faster                                                       |
| gc_traversal             | 1.55 ms                                                         | 1.56 ms: 1.01x slower                                                       |
| sympy_integrate          | 12.2 ms                                                         | 12.3 ms: 1.01x slower                                                       |
| django_template          | 21.7 ms                                                         | 21.8 ms: 1.01x slower                                                       |
| logging_simple           | 5.78 us                                                         | 5.83 us: 1.01x slower                                                       |
| 2to3                     | 207 ms                                                          | 208 ms: 1.01x slower                                                        |
| crypto_pyaes             | 45.5 ms                                                         | 45.8 ms: 1.01x slower                                                       |
| richards_super           | 30.2 ms                                                         | 30.4 ms: 1.01x slower                                                       |
| sympy_expand             | 271 ms                                                          | 273 ms: 1.01x slower                                                        |
| genshi_xml               | 31.6 ms                                                         | 31.9 ms: 1.01x slower                                                       |
| html5lib                 | 35.0 ms                                                         | 35.4 ms: 1.01x slower                                                       |
| richards                 | 26.7 ms                                                         | 27.0 ms: 1.01x slower                                                       |
| pickle                   | 7.11 us                                                         | 7.20 us: 1.01x slower                                                       |
| chameleon                | 4.80 ms                                                         | 4.86 ms: 1.01x slower                                                       |
| hexiom                   | 3.72 ms                                                         | 3.77 ms: 1.01x slower                                                       |
| sympy_str                | 159 ms                                                          | 161 ms: 1.01x slower                                                        |
| sqlglot_parse            | 748 us                                                          | 759 us: 1.01x slower                                                        |
| sqlglot_transpile        | 955 us                                                          | 969 us: 1.01x slower                                                        |
| pyflate                  | 279 ms                                                          | 283 ms: 1.02x slower                                                        |
| dulwich_log              | 38.0 ms                                                         | 38.7 ms: 1.02x slower                                                       |
| sqlglot_optimize         | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                       |
| pickle_dict              | 18.1 us                                                         | 18.5 us: 1.02x slower                                                       |
| scimark_sor              | 75.3 ms                                                         | 76.8 ms: 1.02x slower                                                       |
| sqlglot_normalize        | 173 ms                                                          | 176 ms: 1.02x slower                                                        |
| deepcopy_memo            | 22.1 us                                                         | 22.5 us: 1.02x slower                                                       |
| pickle_pure_python       | 175 us                                                          | 179 us: 1.02x slower                                                        |
| create_gc_cycles         | 888 us                                                          | 907 us: 1.02x slower                                                        |
| tomli_loads              | 1.35 sec                                                        | 1.38 sec: 1.02x slower                                                      |
| logging_silent           | 52.9 ns                                                         | 54.1 ns: 1.02x slower                                                       |
| fannkuch                 | 243 ms                                                          | 249 ms: 1.02x slower                                                        |
| typing_runtime_protocols | 101 us                                                          | 103 us: 1.02x slower                                                        |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.56 ms: 1.02x slower                                                       |
| mako                     | 6.36 ms                                                         | 6.51 ms: 1.02x slower                                                       |
| genshi_text              | 14.4 ms                                                         | 14.7 ms: 1.02x slower                                                       |
| bench_thread_pool        | 768 us                                                          | 787 us: 1.02x slower                                                        |
| unpickle_list            | 2.62 us                                                         | 2.69 us: 1.03x slower                                                       |
| unpickle_pure_python     | 122 us                                                          | 125 us: 1.03x slower                                                        |
| go                       | 82.1 ms                                                         | 84.5 ms: 1.03x slower                                                       |
| deltablue                | 1.88 ms                                                         | 1.94 ms: 1.03x slower                                                       |
| meteor_contest           | 69.9 ms                                                         | 72.1 ms: 1.03x slower                                                       |
| coverage                 | 42.1 ms                                                         | 43.4 ms: 1.03x slower                                                       |
| pprint_safe_repr         | 474 ms                                                          | 494 ms: 1.04x slower                                                        |
| pprint_pformat           | 966 ms                                                          | 1.01 sec: 1.04x slower                                                      |
| nbody                    | 67.6 ms                                                         | 70.9 ms: 1.05x slower                                                       |
| scimark_monte_carlo      | 39.1 ms                                                         | 41.5 ms: 1.06x slower                                                       |
| scimark_fft              | 171 ms                                                          | 182 ms: 1.07x slower                                                        |
| mdp                      | 1.31 sec                                                        | 1.44 sec: 1.10x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (33): pycparser, async_tree_cpu_io_mixed, python_startup_no_site, aiohttp, logging_format, xml_etree_process, comprehensions, chaos, asyncio_tcp_ssl, pylint, regex_compile, nqueens, xml_etree_generate, float, pidigits, unpickle, async_tree_cpu_io_mixed_tg, json_dumps, mypy2, bench_mp_pool, flaskblogging, async_generators, tornado_http, spectral_norm, asyncio_tcp, pickle_list, async_tree_none, async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, regex_v8

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown