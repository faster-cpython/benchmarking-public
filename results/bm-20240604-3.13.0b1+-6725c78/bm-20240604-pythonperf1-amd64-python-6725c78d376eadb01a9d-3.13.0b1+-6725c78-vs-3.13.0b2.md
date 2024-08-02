# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-amd64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.00x slower
- HPT reliability: 95.12%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 208 ms: 1.01x slower                                                        |
| chameleon      | 4.80 ms                                                         | 4.74 ms: 1.01x faster                                                       |
| docutils       | 1.63 sec                                                        | 1.61 sec: 1.01x faster                                                      |
| html5lib       | 35.0 ms                                                         | 35.6 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 50.2 ms: 1.01x slower                                                       |
| nbody          | 67.6 ms                                                         | 69.4 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 78.2 ms: 1.00x slower                                                       |
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.9 us: 1.02x faster                                                       |
| unpickle_list        | 2.62 us                                                         | 2.59 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 62.7 ms: 1.01x slower                                                       |
| xml_etree_generate   | 53.2 ms                                                         | 53.5 ms: 1.01x slower                                                       |
| tomli_loads          | 1.35 sec                                                        | 1.36 sec: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 91.9 ms: 1.01x slower                                                       |
| pickle_pure_python   | 175 us                                                          | 178 us: 1.01x slower                                                        |
| json_dumps           | 5.61 ms                                                         | 5.68 ms: 1.01x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 124 us: 1.02x slower                                                        |
| pickle               | 7.11 us                                                         | 7.32 us: 1.03x slower                                                       |
| pickle_dict          | 18.1 us                                                         | 18.7 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_process, unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 20.3 ms                                                         | 20.1 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 21.2 ms: 1.02x faster                                                       |
| genshi_text     | 14.4 ms                                                         | 14.7 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark               | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json                    | 3.19 ms                                                         | 2.91 ms: 1.09x faster                                                       |
| scimark_lu              | 56.6 ms                                                         | 53.0 ms: 1.07x faster                                                       |
| spectral_norm           | 63.7 ms                                                         | 62.1 ms: 1.03x faster                                                       |
| json_loads              | 14.2 us                                                         | 13.9 us: 1.02x faster                                                       |
| django_template         | 21.7 ms                                                         | 21.2 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult | 2.50 ms                                                         | 2.45 ms: 1.02x faster                                                       |
| comprehensions          | 10.4 us                                                         | 10.2 us: 1.02x faster                                                       |
| logging_format          | 6.22 us                                                         | 6.13 us: 1.02x faster                                                       |
| logging_simple          | 5.78 us                                                         | 5.70 us: 1.02x faster                                                       |
| nqueens                 | 56.7 ms                                                         | 55.9 ms: 1.01x faster                                                       |
| pathlib                 | 75.9 ms                                                         | 74.8 ms: 1.01x faster                                                       |
| sqlglot_normalize       | 173 ms                                                          | 171 ms: 1.01x faster                                                        |
| chameleon               | 4.80 ms                                                         | 4.74 ms: 1.01x faster                                                       |
| deepcopy_reduce         | 1.99 us                                                         | 1.97 us: 1.01x faster                                                       |
| unpickle_list           | 2.62 us                                                         | 2.59 us: 1.01x faster                                                       |
| thrift                  | 8.11 ms                                                         | 8.02 ms: 1.01x faster                                                       |
| scimark_sor             | 75.3 ms                                                         | 74.6 ms: 1.01x faster                                                       |
| raytrace                | 162 ms                                                          | 161 ms: 1.01x faster                                                        |
| python_startup          | 20.3 ms                                                         | 20.1 ms: 1.01x faster                                                       |
| regex_effbot            | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                       |
| docutils                | 1.63 sec                                                        | 1.61 sec: 1.01x faster                                                      |
| mypy2                   | 418 ms                                                          | 415 ms: 1.01x faster                                                        |
| coroutines              | 12.8 ms                                                         | 12.7 ms: 1.01x faster                                                       |
| regex_compile           | 78.0 ms                                                         | 78.2 ms: 1.00x slower                                                       |
| sqlite_synth            | 1.60 us                                                         | 1.60 us: 1.00x slower                                                       |
| xml_etree_iterparse     | 62.3 ms                                                         | 62.7 ms: 1.01x slower                                                       |
| 2to3                    | 207 ms                                                          | 208 ms: 1.01x slower                                                        |
| xml_etree_generate      | 53.2 ms                                                         | 53.5 ms: 1.01x slower                                                       |
| hexiom                  | 3.72 ms                                                         | 3.75 ms: 1.01x slower                                                       |
| regex_dna               | 119 ms                                                          | 120 ms: 1.01x slower                                                        |
| go                      | 82.1 ms                                                         | 82.7 ms: 1.01x slower                                                       |
| tomli_loads             | 1.35 sec                                                        | 1.36 sec: 1.01x slower                                                      |
| deepcopy                | 220 us                                                          | 222 us: 1.01x slower                                                        |
| telco                   | 4.67 ms                                                         | 4.71 ms: 1.01x slower                                                       |
| deltablue               | 1.88 ms                                                         | 1.90 ms: 1.01x slower                                                       |
| float                   | 49.7 ms                                                         | 50.2 ms: 1.01x slower                                                       |
| sqlglot_parse           | 748 us                                                          | 757 us: 1.01x slower                                                        |
| xml_etree_parse         | 90.9 ms                                                         | 91.9 ms: 1.01x slower                                                       |
| pickle_pure_python      | 175 us                                                          | 178 us: 1.01x slower                                                        |
| json_dumps              | 5.61 ms                                                         | 5.68 ms: 1.01x slower                                                       |
| dulwich_log             | 38.0 ms                                                         | 38.5 ms: 1.01x slower                                                       |
| scimark_fft             | 171 ms                                                          | 173 ms: 1.01x slower                                                        |
| pprint_safe_repr        | 474 ms                                                          | 481 ms: 1.01x slower                                                        |
| unpickle_pure_python    | 122 us                                                          | 124 us: 1.02x slower                                                        |
| sqlglot_transpile       | 955 us                                                          | 970 us: 1.02x slower                                                        |
| pprint_pformat          | 966 ms                                                          | 981 ms: 1.02x slower                                                        |
| html5lib                | 35.0 ms                                                         | 35.6 ms: 1.02x slower                                                       |
| generators              | 19.6 ms                                                         | 19.9 ms: 1.02x slower                                                       |
| scimark_monte_carlo     | 39.1 ms                                                         | 39.9 ms: 1.02x slower                                                       |
| genshi_text             | 14.4 ms                                                         | 14.7 ms: 1.02x slower                                                       |
| async_generators        | 223 ms                                                          | 228 ms: 1.02x slower                                                        |
| fannkuch                | 243 ms                                                          | 249 ms: 1.02x slower                                                        |
| create_gc_cycles        | 888 us                                                          | 909 us: 1.02x slower                                                        |
| nbody                   | 67.6 ms                                                         | 69.4 ms: 1.03x slower                                                       |
| richards_super          | 30.2 ms                                                         | 31.0 ms: 1.03x slower                                                       |
| pickle                  | 7.11 us                                                         | 7.32 us: 1.03x slower                                                       |
| pickle_dict             | 18.1 us                                                         | 18.7 us: 1.03x slower                                                       |
| richards                | 26.7 ms                                                         | 27.5 ms: 1.03x slower                                                       |
| meteor_contest          | 69.9 ms                                                         | 72.0 ms: 1.03x slower                                                       |
| coverage                | 42.1 ms                                                         | 43.7 ms: 1.04x slower                                                       |
| deepcopy_memo           | 22.1 us                                                         | 22.9 us: 1.04x slower                                                       |
| bench_thread_pool       | 768 us                                                          | 798 us: 1.04x slower                                                        |
| Geometric mean          | (ref)                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (36): pycparser, asyncio_tcp_ssl, regex_v8, async_tree_cpu_io_mixed, python_startup_no_site, async_tree_io, async_tree_memoization, async_tree_none, sympy_sum, pylint, typing_runtime_protocols, async_tree_cpu_io_mixed_tg, flaskblogging, crypto_pyaes, sympy_integrate, sympy_expand, sqlglot_optimize, xml_etree_process, mdp, pyflate, chaos, asyncio_tcp, logging_silent, sympy_str, gc_traversal, pidigits, unpickle, bench_mp_pool, genshi_xml, tornado_http, async_tree_none_tg, aiohttp, mako, pickle_list, async_tree_io_tg, async_tree_memoization_tg

# HPT report

- Reliability score: 95.12% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown