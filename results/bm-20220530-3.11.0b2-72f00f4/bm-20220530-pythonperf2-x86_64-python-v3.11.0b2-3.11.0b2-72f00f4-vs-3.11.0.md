
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b2
- machine: linux-x86_64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.01x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 282 ms: 1.02x faster                                             |
| chameleon      | 7.67 ms                                                      | 7.52 ms: 1.02x faster                                            |
| docutils       | 2.86 sec                                                     | 2.83 sec: 1.01x faster                                           |
| html5lib       | 72.9 ms                                                      | 70.5 ms: 1.03x faster                                            |
| tornado_http   | 122 ms                                                       | 117 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 73.8 ms: 1.01x faster                                            |
| nbody          | 90.7 ms                                                      | 96.9 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 3.11 ms: 1.12x faster                                            |
| regex_compile  | 158 ms                                                       | 157 ms: 1.01x faster                                             |
| regex_v8       | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_loads           | 28.7 us                                                      | 25.1 us: 1.14x faster                                            |
| xml_etree_parse      | 158 ms                                                       | 153 ms: 1.03x faster                                             |
| unpickle_pure_python | 241 us                                                       | 234 us: 1.03x faster                                             |
| xml_etree_generate   | 80.5 ms                                                      | 79.0 ms: 1.02x faster                                            |
| unpickle             | 13.4 us                                                      | 13.3 us: 1.01x faster                                            |
| xml_etree_process    | 56.5 ms                                                      | 55.8 ms: 1.01x faster                                            |
| pickle_dict          | 30.8 us                                                      | 30.4 us: 1.01x faster                                            |
| json_dumps           | 13.4 ms                                                      | 13.3 ms: 1.01x faster                                            |
| pickle_list          | 3.83 us                                                      | 3.86 us: 1.01x slower                                            |
| unpickle_list        | 4.53 us                                                      | 4.57 us: 1.01x slower                                            |
| pickle               | 9.64 us                                                      | 9.77 us: 1.01x slower                                            |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                             |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                     |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                            |
| python_startup_no_site | 7.76 ms                                                      | 7.70 ms: 1.01x faster                                            |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                            |
| genshi_xml      | 58.5 ms                                                      | 56.0 ms: 1.04x faster                                            |
| django_template | 40.2 ms                                                      | 39.5 ms: 1.02x faster                                            |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_loads              | 28.7 us                                                      | 25.1 us: 1.14x faster                                            |
| regex_effbot            | 3.50 ms                                                      | 3.11 ms: 1.12x faster                                            |
| chaos                   | 80.9 ms                                                      | 72.1 ms: 1.12x faster                                            |
| json                    | 5.65 ms                                                      | 5.16 ms: 1.09x faster                                            |
| genshi_text             | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                            |
| go                      | 164 ms                                                       | 154 ms: 1.06x faster                                             |
| nqueens                 | 103 ms                                                       | 97.7 ms: 1.05x faster                                            |
| deepcopy_memo           | 38.8 us                                                      | 36.9 us: 1.05x faster                                            |
| gunicorn                | 973 us                                                       | 929 us: 1.05x faster                                             |
| sympy_sum               | 185 ms                                                       | 177 ms: 1.04x faster                                             |
| genshi_xml              | 58.5 ms                                                      | 56.0 ms: 1.04x faster                                            |
| aiohttp                 | 985 us                                                       | 944 us: 1.04x faster                                             |
| pyflate                 | 449 ms                                                       | 431 ms: 1.04x faster                                             |
| sympy_expand            | 555 ms                                                       | 533 ms: 1.04x faster                                             |
| logging_format          | 8.11 us                                                      | 7.81 us: 1.04x faster                                            |
| raytrace                | 317 ms                                                       | 305 ms: 1.04x faster                                             |
| pprint_pformat          | 1.63 sec                                                     | 1.57 sec: 1.04x faster                                           |
| deepcopy                | 399 us                                                       | 385 us: 1.04x faster                                             |
| tornado_http            | 122 ms                                                       | 117 ms: 1.04x faster                                             |
| async_tree_memoization  | 630 ms                                                       | 609 ms: 1.03x faster                                             |
| html5lib                | 72.9 ms                                                      | 70.5 ms: 1.03x faster                                            |
| sqlalchemy_imperative   | 20.1 ms                                                      | 19.4 ms: 1.03x faster                                            |
| scimark_sor             | 111 ms                                                       | 108 ms: 1.03x faster                                             |
| sympy_str               | 337 ms                                                       | 327 ms: 1.03x faster                                             |
| pprint_safe_repr        | 784 ms                                                       | 759 ms: 1.03x faster                                             |
| sympy_integrate         | 25.8 ms                                                      | 25.0 ms: 1.03x faster                                            |
| scimark_lu              | 115 ms                                                       | 111 ms: 1.03x faster                                             |
| xml_etree_parse         | 158 ms                                                       | 153 ms: 1.03x faster                                             |
| unpickle_pure_python    | 241 us                                                       | 234 us: 1.03x faster                                             |
| hexiom                  | 7.13 ms                                                      | 6.99 ms: 1.02x faster                                            |
| chameleon               | 7.67 ms                                                      | 7.52 ms: 1.02x faster                                            |
| xml_etree_generate      | 80.5 ms                                                      | 79.0 ms: 1.02x faster                                            |
| 2to3                    | 288 ms                                                       | 282 ms: 1.02x faster                                             |
| logging_silent          | 101 ns                                                       | 98.9 ns: 1.02x faster                                            |
| django_template         | 40.2 ms                                                      | 39.5 ms: 1.02x faster                                            |
| pycparser               | 1.32 sec                                                     | 1.30 sec: 1.02x faster                                           |
| dulwich_log             | 68.4 ms                                                      | 67.2 ms: 1.02x faster                                            |
| sqlglot_normalize       | 126 ms                                                       | 124 ms: 1.02x faster                                             |
| async_tree_none         | 519 ms                                                       | 511 ms: 1.02x faster                                             |
| generators              | 56.0 ms                                                      | 55.2 ms: 1.01x faster                                            |
| unpickle                | 13.4 us                                                      | 13.3 us: 1.01x faster                                            |
| deepcopy_reduce         | 3.51 us                                                      | 3.47 us: 1.01x faster                                            |
| xml_etree_process       | 56.5 ms                                                      | 55.8 ms: 1.01x faster                                            |
| async_tree_cpu_io_mixed | 749 ms                                                       | 740 ms: 1.01x faster                                             |
| meteor_contest          | 131 ms                                                       | 129 ms: 1.01x faster                                             |
| unpack_sequence         | 45.6 ns                                                      | 45.1 ns: 1.01x faster                                            |
| scimark_monte_carlo     | 68.2 ms                                                      | 67.5 ms: 1.01x faster                                            |
| docutils                | 2.86 sec                                                     | 2.83 sec: 1.01x faster                                           |
| pickle_dict             | 30.8 us                                                      | 30.4 us: 1.01x faster                                            |
| asyncio_tcp             | 753 ms                                                       | 746 ms: 1.01x faster                                             |
| python_startup          | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                            |
| async_tree_io           | 1.17 sec                                                     | 1.16 sec: 1.01x faster                                           |
| python_startup_no_site  | 7.76 ms                                                      | 7.70 ms: 1.01x faster                                            |
| async_generators        | 316 ms                                                       | 313 ms: 1.01x faster                                             |
| regex_compile           | 158 ms                                                       | 157 ms: 1.01x faster                                             |
| json_dumps              | 13.4 ms                                                      | 13.3 ms: 1.01x faster                                            |
| float                   | 74.2 ms                                                      | 73.8 ms: 1.01x faster                                            |
| scimark_fft             | 285 ms                                                       | 284 ms: 1.00x faster                                             |
| pickle_list             | 3.83 us                                                      | 3.86 us: 1.01x slower                                            |
| unpickle_list           | 4.53 us                                                      | 4.57 us: 1.01x slower                                            |
| regex_v8                | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                            |
| thrift                  | 925 us                                                       | 935 us: 1.01x slower                                             |
| coroutines              | 27.6 ms                                                      | 27.9 ms: 1.01x slower                                            |
| pickle                  | 9.64 us                                                      | 9.77 us: 1.01x slower                                            |
| xml_etree_iterparse     | 104 ms                                                       | 106 ms: 1.02x slower                                             |
| sqlite_synth            | 2.50 us                                                      | 2.54 us: 1.02x slower                                            |
| telco                   | 6.86 ms                                                      | 6.99 ms: 1.02x slower                                            |
| create_gc_cycles        | 1.61 ms                                                      | 1.64 ms: 1.02x slower                                            |
| gc_traversal            | 3.85 ms                                                      | 3.94 ms: 1.02x slower                                            |
| mdp                     | 2.75 sec                                                     | 2.85 sec: 1.04x slower                                           |
| fannkuch                | 429 ms                                                       | 447 ms: 1.04x slower                                             |
| nbody                   | 90.7 ms                                                      | 96.9 ms: 1.07x slower                                            |
| comprehensions          | 24.6 us                                                      | 27.9 us: 1.13x slower                                            |
| sqlglot_transpile       | 1.92 ms                                                      | 2.29 ms: 1.19x slower                                            |
| sqlglot_parse           | 1.53 ms                                                      | 1.95 ms: 1.27x slower                                            |
| Geometric mean          | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (18): mypy2, bench_mp_pool, pylint, bench_thread_pool, sqlalchemy_declarative, deltablue, mako, sqlglot_optimize, dask, regex_dna, pidigits, scimark_sparse_mat_mult, crypto_pyaes, spectral_norm, logging_simple, pathlib, richards, pickle_pure_python
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, coverage, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
