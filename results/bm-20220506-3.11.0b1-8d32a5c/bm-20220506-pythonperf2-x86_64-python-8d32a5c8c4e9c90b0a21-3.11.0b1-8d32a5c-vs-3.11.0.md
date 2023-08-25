
# Results vs. 3.11.0

- fork: python
- ref: 8d32a5c8c4e9c90b0a21
- machine: linux-x86_64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.01x faster \*
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 281 ms: 1.02x faster                                                        |
| chameleon      | 7.67 ms                                                      | 7.53 ms: 1.02x faster                                                       |
| docutils       | 2.86 sec                                                     | 2.82 sec: 1.01x faster                                                      |
| html5lib       | 72.9 ms                                                      | 69.0 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 74.7 ms: 1.01x slower                                                       |
| nbody          | 90.7 ms                                                      | 100 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 2.97 ms: 1.18x faster                                                       |
| regex_v8       | 23.9 ms                                                      | 22.8 ms: 1.05x faster                                                       |
| regex_compile  | 158 ms                                                       | 153 ms: 1.03x faster                                                        |
| regex_dna      | 227 ms                                                       | 232 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                      | 24.6 us: 1.17x faster                                                       |
| unpickle_pure_python | 241 us                                                       | 233 us: 1.03x faster                                                        |
| pickle_dict          | 30.8 us                                                      | 29.9 us: 1.03x faster                                                       |
| xml_etree_parse      | 158 ms                                                       | 155 ms: 1.02x faster                                                        |
| unpickle             | 13.4 us                                                      | 13.3 us: 1.01x faster                                                       |
| xml_etree_process    | 56.5 ms                                                      | 56.1 ms: 1.01x faster                                                       |
| pickle_pure_python   | 319 us                                                       | 320 us: 1.00x slower                                                        |
| unpickle_list        | 4.53 us                                                      | 4.56 us: 1.01x slower                                                       |
| json_dumps           | 13.4 ms                                                      | 13.5 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (4): pickle_list, xml_etree_generate, pickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 10.5 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.76 ms                                                      | 7.68 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 56.7 ms: 1.03x faster                                                       |
| genshi_text     | 26.1 ms                                                      | 25.4 ms: 1.03x faster                                                       |
| django_template | 40.2 ms                                                      | 41.3 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot            | 3.50 ms                                                      | 2.97 ms: 1.18x faster                                                       |
| json_loads              | 28.7 us                                                      | 24.6 us: 1.17x faster                                                       |
| chaos                   | 80.9 ms                                                      | 72.4 ms: 1.12x faster                                                       |
| json                    | 5.65 ms                                                      | 5.14 ms: 1.10x faster                                                       |
| nqueens                 | 103 ms                                                       | 95.8 ms: 1.07x faster                                                       |
| sqlglot_normalize       | 126 ms                                                       | 119 ms: 1.06x faster                                                        |
| logging_format          | 8.11 us                                                      | 7.67 us: 1.06x faster                                                       |
| html5lib                | 72.9 ms                                                      | 69.0 ms: 1.06x faster                                                       |
| pycparser               | 1.32 sec                                                     | 1.26 sec: 1.05x faster                                                      |
| regex_v8                | 23.9 ms                                                      | 22.8 ms: 1.05x faster                                                       |
| go                      | 164 ms                                                       | 156 ms: 1.05x faster                                                        |
| gunicorn                | 973 us                                                       | 928 us: 1.05x faster                                                        |
| logging_simple          | 7.19 us                                                      | 6.90 us: 1.04x faster                                                       |
| aiohttp                 | 985 us                                                       | 945 us: 1.04x faster                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.57 sec: 1.04x faster                                                      |
| pprint_safe_repr        | 784 ms                                                       | 755 ms: 1.04x faster                                                        |
| pyflate                 | 449 ms                                                       | 433 ms: 1.04x faster                                                        |
| sympy_sum               | 185 ms                                                       | 178 ms: 1.04x faster                                                        |
| regex_compile           | 158 ms                                                       | 153 ms: 1.03x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 233 us: 1.03x faster                                                        |
| hexiom                  | 7.13 ms                                                      | 6.91 ms: 1.03x faster                                                       |
| genshi_xml              | 58.5 ms                                                      | 56.7 ms: 1.03x faster                                                       |
| deepcopy_memo           | 38.8 us                                                      | 37.6 us: 1.03x faster                                                       |
| pickle_dict             | 30.8 us                                                      | 29.9 us: 1.03x faster                                                       |
| genshi_text             | 26.1 ms                                                      | 25.4 ms: 1.03x faster                                                       |
| sqlalchemy_imperative   | 20.1 ms                                                      | 19.5 ms: 1.03x faster                                                       |
| sympy_expand            | 555 ms                                                       | 540 ms: 1.03x faster                                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.42 us: 1.03x faster                                                       |
| fannkuch                | 429 ms                                                       | 418 ms: 1.03x faster                                                        |
| sympy_str               | 337 ms                                                       | 329 ms: 1.02x faster                                                        |
| raytrace                | 317 ms                                                       | 309 ms: 1.02x faster                                                        |
| sympy_integrate         | 25.8 ms                                                      | 25.2 ms: 1.02x faster                                                       |
| 2to3                    | 288 ms                                                       | 281 ms: 1.02x faster                                                        |
| python_startup          | 10.8 ms                                                      | 10.5 ms: 1.02x faster                                                       |
| pylint                  | 515 ms                                                       | 505 ms: 1.02x faster                                                        |
| chameleon               | 7.67 ms                                                      | 7.53 ms: 1.02x faster                                                       |
| deltablue               | 4.00 ms                                                      | 3.93 ms: 1.02x faster                                                       |
| xml_etree_parse         | 158 ms                                                       | 155 ms: 1.02x faster                                                        |
| flaskblogging           | 3.88 ms                                                      | 3.82 ms: 1.02x faster                                                       |
| sqlglot_optimize        | 59.8 ms                                                      | 58.9 ms: 1.01x faster                                                       |
| deepcopy                | 399 us                                                       | 394 us: 1.01x faster                                                        |
| crypto_pyaes            | 83.4 ms                                                      | 82.3 ms: 1.01x faster                                                       |
| thrift                  | 925 us                                                       | 913 us: 1.01x faster                                                        |
| pathlib                 | 19.1 ms                                                      | 18.8 ms: 1.01x faster                                                       |
| docutils                | 2.86 sec                                                     | 2.82 sec: 1.01x faster                                                      |
| unpickle                | 13.4 us                                                      | 13.3 us: 1.01x faster                                                       |
| python_startup_no_site  | 7.76 ms                                                      | 7.68 ms: 1.01x faster                                                       |
| scimark_sor             | 111 ms                                                       | 110 ms: 1.01x faster                                                        |
| logging_silent          | 101 ns                                                       | 99.8 ns: 1.01x faster                                                       |
| generators              | 56.0 ms                                                      | 55.5 ms: 1.01x faster                                                       |
| async_tree_memoization  | 630 ms                                                       | 624 ms: 1.01x faster                                                        |
| async_tree_none         | 519 ms                                                       | 516 ms: 1.01x faster                                                        |
| dulwich_log             | 68.4 ms                                                      | 68.0 ms: 1.01x faster                                                       |
| xml_etree_process       | 56.5 ms                                                      | 56.1 ms: 1.01x faster                                                       |
| asyncio_tcp             | 753 ms                                                       | 749 ms: 1.01x faster                                                        |
| scimark_lu              | 115 ms                                                       | 114 ms: 1.00x faster                                                        |
| spectral_norm           | 93.3 ms                                                      | 93.1 ms: 1.00x faster                                                       |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.06 ms: 1.00x slower                                                       |
| pickle_pure_python      | 319 us                                                       | 320 us: 1.00x slower                                                        |
| meteor_contest          | 131 ms                                                       | 131 ms: 1.00x slower                                                        |
| unpickle_list           | 4.53 us                                                      | 4.56 us: 1.01x slower                                                       |
| float                   | 74.2 ms                                                      | 74.7 ms: 1.01x slower                                                       |
| async_generators        | 316 ms                                                       | 318 ms: 1.01x slower                                                        |
| json_dumps              | 13.4 ms                                                      | 13.5 ms: 1.01x slower                                                       |
| mdp                     | 2.75 sec                                                     | 2.78 sec: 1.01x slower                                                      |
| scimark_monte_carlo     | 68.2 ms                                                      | 69.2 ms: 1.01x slower                                                       |
| coroutines              | 27.6 ms                                                      | 28.0 ms: 1.02x slower                                                       |
| telco                   | 6.86 ms                                                      | 6.99 ms: 1.02x slower                                                       |
| regex_dna               | 227 ms                                                       | 232 ms: 1.02x slower                                                        |
| dask                    | 410 ms                                                       | 418 ms: 1.02x slower                                                        |
| create_gc_cycles        | 1.61 ms                                                      | 1.64 ms: 1.02x slower                                                       |
| django_template         | 40.2 ms                                                      | 41.3 ms: 1.03x slower                                                       |
| scimark_fft             | 285 ms                                                       | 294 ms: 1.03x slower                                                        |
| richards                | 48.3 ms                                                      | 50.1 ms: 1.04x slower                                                       |
| nbody                   | 90.7 ms                                                      | 100 ms: 1.10x slower                                                        |
| comprehensions          | 24.6 us                                                      | 28.2 us: 1.14x slower                                                       |
| sqlglot_transpile       | 1.92 ms                                                      | 2.30 ms: 1.20x slower                                                       |
| sqlglot_parse           | 1.53 ms                                                      | 1.95 ms: 1.27x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (16): mypy2, bench_mp_pool, mako, pickle_list, async_tree_io, tornado_http, sqlalchemy_declarative, xml_etree_generate, pickle, async_tree_cpu_io_mixed, gc_traversal, pidigits, xml_etree_iterparse, sqlite_synth, bench_thread_pool, unpack_sequence
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
