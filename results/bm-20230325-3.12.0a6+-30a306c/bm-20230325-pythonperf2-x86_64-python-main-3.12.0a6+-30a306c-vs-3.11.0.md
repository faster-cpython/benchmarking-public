
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 30a306c
- commit date: 2023-03-25
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 285 ms: 1.01x faster                                         |
| chameleon      | 7.67 ms                                                      | 7.46 ms: 1.03x faster                                        |
| docutils       | 2.86 sec                                                     | 2.81 sec: 1.02x faster                                       |
| html5lib       | 72.9 ms                                                      | 68.9 ms: 1.06x faster                                        |
| tornado_http   | 122 ms                                                       | 114 ms: 1.07x faster                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 84.6 ms: 1.07x faster                                        |
| float          | 74.2 ms                                                      | 71.4 ms: 1.04x faster                                        |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 147 ms: 1.07x faster                                         |
| regex_v8       | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.43 ms: 1.02x faster                                        |
| regex_dna      | 227 ms                                                       | 235 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                        |
| json_loads           | 28.7 us                                                      | 24.2 us: 1.19x faster                                        |
| unpickle_pure_python | 241 us                                                       | 206 us: 1.17x faster                                         |
| xml_etree_parse      | 158 ms                                                       | 142 ms: 1.11x faster                                         |
| xml_etree_iterparse  | 104 ms                                                       | 102 ms: 1.02x faster                                         |
| pickle_list          | 3.83 us                                                      | 3.75 us: 1.02x faster                                        |
| xml_etree_process    | 56.5 ms                                                      | 57.5 ms: 1.02x slower                                        |
| pickle_dict          | 30.8 us                                                      | 31.8 us: 1.03x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 83.6 ms: 1.04x slower                                        |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                 |

Benchmark hidden because not significant (3): pickle_pure_python, unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.0 ms: 1.03x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.32 ms: 1.07x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 10.0 ms: 1.09x faster                                        |
| genshi_xml      | 58.5 ms                                                      | 55.3 ms: 1.06x faster                                        |
| genshi_text     | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                        |
| django_template | 40.2 ms                                                      | 40.8 ms: 1.01x slower                                        |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 387 ms: 1.95x faster                                         |
| generators              | 56.0 ms                                                      | 37.9 ms: 1.48x faster                                        |
| json_dumps              | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                        |
| mypy2                   | 451 ms                                                       | 379 ms: 1.19x faster                                         |
| json_loads              | 28.7 us                                                      | 24.2 us: 1.19x faster                                        |
| unpickle_pure_python    | 241 us                                                       | 206 us: 1.17x faster                                         |
| deltablue               | 4.00 ms                                                      | 3.44 ms: 1.16x faster                                        |
| scimark_lu              | 115 ms                                                       | 101 ms: 1.13x faster                                         |
| chaos                   | 80.9 ms                                                      | 71.5 ms: 1.13x faster                                        |
| json                    | 5.65 ms                                                      | 5.03 ms: 1.12x faster                                        |
| deepcopy_memo           | 38.8 us                                                      | 34.6 us: 1.12x faster                                        |
| xml_etree_parse         | 158 ms                                                       | 142 ms: 1.11x faster                                         |
| coroutines              | 27.6 ms                                                      | 24.8 ms: 1.11x faster                                        |
| hexiom                  | 7.13 ms                                                      | 6.50 ms: 1.10x faster                                        |
| mako                    | 11.0 ms                                                      | 10.0 ms: 1.09x faster                                        |
| raytrace                | 317 ms                                                       | 290 ms: 1.09x faster                                         |
| mdp                     | 2.75 sec                                                     | 2.53 sec: 1.09x faster                                       |
| pycparser               | 1.32 sec                                                     | 1.23 sec: 1.08x faster                                       |
| regex_compile           | 158 ms                                                       | 147 ms: 1.07x faster                                         |
| nbody                   | 90.7 ms                                                      | 84.6 ms: 1.07x faster                                        |
| gc_traversal            | 3.85 ms                                                      | 3.59 ms: 1.07x faster                                        |
| tornado_http            | 122 ms                                                       | 114 ms: 1.07x faster                                         |
| logging_format          | 8.11 us                                                      | 7.62 us: 1.06x faster                                        |
| nqueens                 | 103 ms                                                       | 97.0 ms: 1.06x faster                                        |
| genshi_xml              | 58.5 ms                                                      | 55.3 ms: 1.06x faster                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.83 ms: 1.06x faster                                        |
| html5lib                | 72.9 ms                                                      | 68.9 ms: 1.06x faster                                        |
| deepcopy                | 399 us                                                       | 380 us: 1.05x faster                                         |
| bench_thread_pool       | 1.01 ms                                                      | 966 us: 1.05x faster                                         |
| unpack_sequence         | 45.6 ns                                                      | 43.8 ns: 1.04x faster                                        |
| dulwich_log             | 68.4 ms                                                      | 65.7 ms: 1.04x faster                                        |
| float                   | 74.2 ms                                                      | 71.4 ms: 1.04x faster                                        |
| scimark_fft             | 285 ms                                                       | 274 ms: 1.04x faster                                         |
| async_tree_memoization  | 630 ms                                                       | 607 ms: 1.04x faster                                         |
| sqlglot_normalize       | 126 ms                                                       | 121 ms: 1.04x faster                                         |
| genshi_text             | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.58 sec: 1.03x faster                                       |
| regex_v8                | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                        |
| sympy_expand            | 555 ms                                                       | 538 ms: 1.03x faster                                         |
| logging_silent          | 101 ns                                                       | 97.9 ns: 1.03x faster                                        |
| richards                | 48.3 ms                                                      | 46.9 ms: 1.03x faster                                        |
| chameleon               | 7.67 ms                                                      | 7.46 ms: 1.03x faster                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.42 us: 1.03x faster                                        |
| xml_etree_iterparse     | 104 ms                                                       | 102 ms: 1.02x faster                                         |
| sympy_integrate         | 25.8 ms                                                      | 25.2 ms: 1.02x faster                                        |
| sqlglot_optimize        | 59.8 ms                                                      | 58.4 ms: 1.02x faster                                        |
| pprint_safe_repr        | 784 ms                                                       | 767 ms: 1.02x faster                                         |
| logging_simple          | 7.19 us                                                      | 7.04 us: 1.02x faster                                        |
| pickle_list             | 3.83 us                                                      | 3.75 us: 1.02x faster                                        |
| pathlib                 | 19.1 ms                                                      | 18.7 ms: 1.02x faster                                        |
| sympy_str               | 337 ms                                                       | 330 ms: 1.02x faster                                         |
| regex_effbot            | 3.50 ms                                                      | 3.43 ms: 1.02x faster                                        |
| docutils                | 2.86 sec                                                     | 2.81 sec: 1.02x faster                                       |
| async_tree_none         | 519 ms                                                       | 510 ms: 1.02x faster                                         |
| go                      | 164 ms                                                       | 162 ms: 1.01x faster                                         |
| spectral_norm           | 93.3 ms                                                      | 92.1 ms: 1.01x faster                                        |
| meteor_contest          | 131 ms                                                       | 129 ms: 1.01x faster                                         |
| telco                   | 6.86 ms                                                      | 6.78 ms: 1.01x faster                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 741 ms: 1.01x faster                                         |
| 2to3                    | 288 ms                                                       | 285 ms: 1.01x faster                                         |
| async_tree_io           | 1.17 sec                                                     | 1.16 sec: 1.01x faster                                       |
| scimark_sor             | 111 ms                                                       | 111 ms: 1.01x faster                                         |
| scimark_monte_carlo     | 68.2 ms                                                      | 69.1 ms: 1.01x slower                                        |
| sqlglot_parse           | 1.53 ms                                                      | 1.55 ms: 1.01x slower                                        |
| django_template         | 40.2 ms                                                      | 40.8 ms: 1.01x slower                                        |
| xml_etree_process       | 56.5 ms                                                      | 57.5 ms: 1.02x slower                                        |
| python_startup          | 10.8 ms                                                      | 11.0 ms: 1.03x slower                                        |
| fannkuch                | 429 ms                                                       | 442 ms: 1.03x slower                                         |
| pickle_dict             | 30.8 us                                                      | 31.8 us: 1.03x slower                                        |
| regex_dna               | 227 ms                                                       | 235 ms: 1.03x slower                                         |
| pidigits                | 251 ms                                                       | 261 ms: 1.04x slower                                         |
| xml_etree_generate      | 80.5 ms                                                      | 83.6 ms: 1.04x slower                                        |
| pickle                  | 9.64 us                                                      | 10.1 us: 1.05x slower                                        |
| sqlite_synth            | 2.50 us                                                      | 2.63 us: 1.05x slower                                        |
| coverage                | 84.8 ms                                                      | 90.5 ms: 1.07x slower                                        |
| comprehensions          | 24.6 us                                                      | 26.4 us: 1.07x slower                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.32 ms: 1.07x slower                                        |
| async_generators        | 316 ms                                                       | 377 ms: 1.20x slower                                         |
| dask                    | 410 ms                                                       | 568 ms: 1.39x slower                                         |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                 |

Benchmark hidden because not significant (10): pyflate, thrift, pickle_pure_python, unpickle, unpickle_list, crypto_pyaes, sqlglot_transpile, sympy_sum, create_gc_cycles, bench_mp_pool
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
