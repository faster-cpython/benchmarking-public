
# Results vs. 3.11.0

- fork: faster-cpython
- ref: instrument_all_possi
- machine: linux-x86_64
- commit hash: 5418580
- commit date: 2023-05-10
- overall geometric mean: 1.04x faster \*
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 285 ms: 1.01x faster                                                                   |
| docutils       | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                                                 |
| tornado_http   | 122 ms                                                       | 113 ms: 1.07x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 84.7 ms: 1.07x faster                                                                  |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                                                   |
| float          | 74.2 ms                                                      | 79.0 ms: 1.07x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.09x faster                                                                   |
| regex_effbot   | 3.50 ms                                                      | 3.41 ms: 1.03x faster                                                                  |
| regex_v8       | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                                  |
| json_loads           | 28.7 us                                                      | 24.5 us: 1.17x faster                                                                  |
| unpickle_pure_python | 241 us                                                       | 205 us: 1.17x faster                                                                   |
| xml_etree_parse      | 158 ms                                                       | 149 ms: 1.06x faster                                                                   |
| xml_etree_process    | 56.5 ms                                                      | 58.7 ms: 1.04x slower                                                                  |
| unpickle_list        | 4.53 us                                                      | 4.72 us: 1.04x slower                                                                  |
| pickle_dict          | 30.8 us                                                      | 32.6 us: 1.06x slower                                                                  |
| xml_etree_generate   | 80.5 ms                                                      | 85.6 ms: 1.06x slower                                                                  |
| pickle               | 9.64 us                                                      | 10.3 us: 1.07x slower                                                                  |
| unpickle             | 13.4 us                                                      | 14.9 us: 1.11x slower                                                                  |
| pickle_list          | 3.83 us                                                      | 4.45 us: 1.16x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                                  |
| python_startup_no_site | 7.76 ms                                                      | 8.38 ms: 1.08x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|-----------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 379 ms: 1.99x faster                                                                   |
| generators              | 56.0 ms                                                      | 36.4 ms: 1.54x faster                                                                  |
| json_dumps              | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                                  |
| chaos                   | 80.9 ms                                                      | 64.3 ms: 1.26x faster                                                                  |
| fannkuch                | 429 ms                                                       | 343 ms: 1.25x faster                                                                   |
| deltablue               | 4.00 ms                                                      | 3.22 ms: 1.24x faster                                                                  |
| hexiom                  | 7.13 ms                                                      | 5.79 ms: 1.23x faster                                                                  |
| mypy2                   | 451 ms                                                       | 369 ms: 1.22x faster                                                                   |
| coroutines              | 27.6 ms                                                      | 22.6 ms: 1.22x faster                                                                  |
| json_loads              | 28.7 us                                                      | 24.5 us: 1.17x faster                                                                  |
| unpickle_pure_python    | 241 us                                                       | 205 us: 1.17x faster                                                                   |
| async_tree_memoization  | 630 ms                                                       | 546 ms: 1.15x faster                                                                   |
| scimark_lu              | 115 ms                                                       | 99.6 ms: 1.15x faster                                                                  |
| async_tree_none         | 519 ms                                                       | 455 ms: 1.14x faster                                                                   |
| nqueens                 | 103 ms                                                       | 90.1 ms: 1.14x faster                                                                  |
| go                      | 164 ms                                                       | 144 ms: 1.14x faster                                                                   |
| async_tree_io           | 1.17 sec                                                     | 1.05 sec: 1.12x faster                                                                 |
| comprehensions          | 24.6 us                                                      | 22.0 us: 1.12x faster                                                                  |
| richards                | 48.3 ms                                                      | 43.5 ms: 1.11x faster                                                                  |
| logging_silent          | 101 ns                                                       | 91.1 ns: 1.11x faster                                                                  |
| sqlglot_parse           | 1.53 ms                                                      | 1.39 ms: 1.10x faster                                                                  |
| regex_compile           | 158 ms                                                       | 144 ms: 1.09x faster                                                                   |
| json                    | 5.65 ms                                                      | 5.18 ms: 1.09x faster                                                                  |
| mdp                     | 2.75 sec                                                     | 2.53 sec: 1.09x faster                                                                 |
| mako                    | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                                  |
| logging_format          | 8.11 us                                                      | 7.51 us: 1.08x faster                                                                  |
| async_tree_cpu_io_mixed | 749 ms                                                       | 698 ms: 1.07x faster                                                                   |
| tornado_http            | 122 ms                                                       | 113 ms: 1.07x faster                                                                   |
| sqlglot_transpile       | 1.92 ms                                                      | 1.79 ms: 1.07x faster                                                                  |
| sqlglot_normalize       | 126 ms                                                       | 118 ms: 1.07x faster                                                                   |
| nbody                   | 90.7 ms                                                      | 84.7 ms: 1.07x faster                                                                  |
| deepcopy                | 399 us                                                       | 375 us: 1.07x faster                                                                   |
| pycparser               | 1.32 sec                                                     | 1.25 sec: 1.06x faster                                                                 |
| raytrace                | 317 ms                                                       | 299 ms: 1.06x faster                                                                   |
| xml_etree_parse         | 158 ms                                                       | 149 ms: 1.06x faster                                                                   |
| logging_simple          | 7.19 us                                                      | 6.80 us: 1.06x faster                                                                  |
| bench_thread_pool       | 1.01 ms                                                      | 959 us: 1.05x faster                                                                   |
| crypto_pyaes            | 83.4 ms                                                      | 79.2 ms: 1.05x faster                                                                  |
| deepcopy_memo           | 38.8 us                                                      | 37.2 us: 1.04x faster                                                                  |
| dulwich_log             | 68.4 ms                                                      | 65.9 ms: 1.04x faster                                                                  |
| regex_effbot            | 3.50 ms                                                      | 3.41 ms: 1.03x faster                                                                  |
| sqlglot_optimize        | 59.8 ms                                                      | 58.4 ms: 1.02x faster                                                                  |
| meteor_contest          | 131 ms                                                       | 128 ms: 1.02x faster                                                                   |
| regex_v8                | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                                  |
| scimark_sor             | 111 ms                                                       | 109 ms: 1.02x faster                                                                   |
| unpack_sequence         | 45.6 ns                                                      | 44.8 ns: 1.02x faster                                                                  |
| deepcopy_reduce         | 3.51 us                                                      | 3.45 us: 1.02x faster                                                                  |
| 2to3                    | 288 ms                                                       | 285 ms: 1.01x faster                                                                   |
| spectral_norm           | 93.3 ms                                                      | 92.6 ms: 1.01x faster                                                                  |
| docutils                | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                                                 |
| create_gc_cycles        | 1.61 ms                                                      | 1.63 ms: 1.02x slower                                                                  |
| pprint_safe_repr        | 784 ms                                                       | 798 ms: 1.02x slower                                                                   |
| pyflate                 | 449 ms                                                       | 461 ms: 1.03x slower                                                                   |
| pidigits                | 251 ms                                                       | 261 ms: 1.04x slower                                                                   |
| xml_etree_process       | 56.5 ms                                                      | 58.7 ms: 1.04x slower                                                                  |
| unpickle_list           | 4.53 us                                                      | 4.72 us: 1.04x slower                                                                  |
| coverage                | 84.8 ms                                                      | 88.5 ms: 1.04x slower                                                                  |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.23 ms: 1.05x slower                                                                  |
| scimark_fft             | 285 ms                                                       | 298 ms: 1.05x slower                                                                   |
| python_startup          | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                                  |
| telco                   | 6.86 ms                                                      | 7.23 ms: 1.05x slower                                                                  |
| pathlib                 | 19.1 ms                                                      | 20.1 ms: 1.05x slower                                                                  |
| gc_traversal            | 3.85 ms                                                      | 4.06 ms: 1.06x slower                                                                  |
| pickle_dict             | 30.8 us                                                      | 32.6 us: 1.06x slower                                                                  |
| xml_etree_generate      | 80.5 ms                                                      | 85.6 ms: 1.06x slower                                                                  |
| sqlite_synth            | 2.50 us                                                      | 2.66 us: 1.06x slower                                                                  |
| float                   | 74.2 ms                                                      | 79.0 ms: 1.07x slower                                                                  |
| pickle                  | 9.64 us                                                      | 10.3 us: 1.07x slower                                                                  |
| python_startup_no_site  | 7.76 ms                                                      | 8.38 ms: 1.08x slower                                                                  |
| unpickle                | 13.4 us                                                      | 14.9 us: 1.11x slower                                                                  |
| pickle_list             | 3.83 us                                                      | 4.45 us: 1.16x slower                                                                  |
| async_generators        | 316 ms                                                       | 380 ms: 1.20x slower                                                                   |
| dask                    | 410 ms                                                       | 556 ms: 1.36x slower                                                                   |
| bench_mp_pool           | 4.62 ms                                                      | 7.35 ms: 1.59x slower                                                                  |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                                           |

Benchmark hidden because not significant (5): xml_etree_iterparse, scimark_monte_carlo, regex_dna, pickle_pure_python, pprint_pformat
Ignored benchmarks (20) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
