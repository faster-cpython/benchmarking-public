
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.04x faster \*
- HPT reliability: 99.69%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 286 ms: 1.01x faster                                                                    |
| docutils       | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                                                  |
| tornado_http   | 122 ms                                                       | 114 ms: 1.07x faster                                                                    |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 85.2 ms: 1.06x faster                                                                   |
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                                                    |
| float          | 74.2 ms                                                      | 78.5 ms: 1.06x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 145 ms: 1.09x faster                                                                    |
| regex_effbot   | 3.50 ms                                                      | 3.41 ms: 1.03x faster                                                                   |
| regex_v8       | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                                   |
| regex_dna      | 227 ms                                                       | 228 ms: 1.01x slower                                                                    |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.29x faster                                                                   |
| json_loads           | 28.7 us                                                      | 24.3 us: 1.18x faster                                                                   |
| unpickle_pure_python | 241 us                                                       | 206 us: 1.17x faster                                                                    |
| xml_etree_parse      | 158 ms                                                       | 144 ms: 1.09x faster                                                                    |
| xml_etree_iterparse  | 104 ms                                                       | 103 ms: 1.01x faster                                                                    |
| pickle_pure_python   | 319 us                                                       | 318 us: 1.00x faster                                                                    |
| pickle               | 9.64 us                                                      | 9.94 us: 1.03x slower                                                                   |
| xml_etree_process    | 56.5 ms                                                      | 59.1 ms: 1.05x slower                                                                   |
| pickle_dict          | 30.8 us                                                      | 32.5 us: 1.06x slower                                                                   |
| xml_etree_generate   | 80.5 ms                                                      | 86.1 ms: 1.07x slower                                                                   |
| unpickle_list        | 4.53 us                                                      | 4.86 us: 1.07x slower                                                                   |
| unpickle             | 13.4 us                                                      | 14.8 us: 1.10x slower                                                                   |
| pickle_list          | 3.83 us                                                      | 4.42 us: 1.15x slower                                                                   |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                                   |
| python_startup_no_site | 7.76 ms                                                      | 8.44 ms: 1.09x slower                                                                   |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.0 ms: 1.10x faster                                                                   |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 381 ms: 1.98x faster                                                                    |
| generators              | 56.0 ms                                                      | 36.6 ms: 1.53x faster                                                                   |
| json_dumps              | 13.4 ms                                                      | 10.3 ms: 1.29x faster                                                                   |
| deltablue               | 4.00 ms                                                      | 3.23 ms: 1.24x faster                                                                   |
| fannkuch                | 429 ms                                                       | 347 ms: 1.24x faster                                                                    |
| coroutines              | 27.6 ms                                                      | 22.4 ms: 1.23x faster                                                                   |
| chaos                   | 80.9 ms                                                      | 66.6 ms: 1.21x faster                                                                   |
| hexiom                  | 7.13 ms                                                      | 5.90 ms: 1.21x faster                                                                   |
| mypy2                   | 451 ms                                                       | 378 ms: 1.19x faster                                                                    |
| json_loads              | 28.7 us                                                      | 24.3 us: 1.18x faster                                                                   |
| unpickle_pure_python    | 241 us                                                       | 206 us: 1.17x faster                                                                    |
| scimark_lu              | 115 ms                                                       | 99.3 ms: 1.15x faster                                                                   |
| go                      | 164 ms                                                       | 144 ms: 1.14x faster                                                                    |
| nqueens                 | 103 ms                                                       | 90.7 ms: 1.13x faster                                                                   |
| richards                | 48.3 ms                                                      | 43.8 ms: 1.10x faster                                                                   |
| json                    | 5.65 ms                                                      | 5.12 ms: 1.10x faster                                                                   |
| sqlglot_parse           | 1.53 ms                                                      | 1.39 ms: 1.10x faster                                                                   |
| logging_format          | 8.11 us                                                      | 7.39 us: 1.10x faster                                                                   |
| mako                    | 11.0 ms                                                      | 10.0 ms: 1.10x faster                                                                   |
| async_tree_memoization  | 630 ms                                                       | 575 ms: 1.10x faster                                                                    |
| xml_etree_parse         | 158 ms                                                       | 144 ms: 1.09x faster                                                                    |
| deepcopy_memo           | 38.8 us                                                      | 35.5 us: 1.09x faster                                                                   |
| gc_traversal            | 3.85 ms                                                      | 3.53 ms: 1.09x faster                                                                   |
| logging_simple          | 7.19 us                                                      | 6.60 us: 1.09x faster                                                                   |
| logging_silent          | 101 ns                                                       | 92.8 ns: 1.09x faster                                                                   |
| regex_compile           | 158 ms                                                       | 145 ms: 1.09x faster                                                                    |
| async_tree_none         | 519 ms                                                       | 479 ms: 1.08x faster                                                                    |
| mdp                     | 2.75 sec                                                     | 2.55 sec: 1.08x faster                                                                  |
| pycparser               | 1.32 sec                                                     | 1.23 sec: 1.07x faster                                                                  |
| tornado_http            | 122 ms                                                       | 114 ms: 1.07x faster                                                                    |
| sqlglot_transpile       | 1.92 ms                                                      | 1.79 ms: 1.07x faster                                                                   |
| async_tree_io           | 1.17 sec                                                     | 1.10 sec: 1.07x faster                                                                  |
| nbody                   | 90.7 ms                                                      | 85.2 ms: 1.06x faster                                                                   |
| deepcopy                | 399 us                                                       | 376 us: 1.06x faster                                                                    |
| async_tree_cpu_io_mixed | 749 ms                                                       | 712 ms: 1.05x faster                                                                    |
| dulwich_log             | 68.4 ms                                                      | 65.6 ms: 1.04x faster                                                                   |
| sqlglot_normalize       | 126 ms                                                       | 121 ms: 1.04x faster                                                                    |
| bench_thread_pool       | 1.01 ms                                                      | 971 us: 1.04x faster                                                                    |
| crypto_pyaes            | 83.4 ms                                                      | 80.2 ms: 1.04x faster                                                                   |
| deepcopy_reduce         | 3.51 us                                                      | 3.38 us: 1.04x faster                                                                   |
| raytrace                | 317 ms                                                       | 308 ms: 1.03x faster                                                                    |
| regex_effbot            | 3.50 ms                                                      | 3.41 ms: 1.03x faster                                                                   |
| spectral_norm           | 93.3 ms                                                      | 91.2 ms: 1.02x faster                                                                   |
| regex_v8                | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                                   |
| pyflate                 | 449 ms                                                       | 443 ms: 1.01x faster                                                                    |
| pprint_pformat          | 1.63 sec                                                     | 1.61 sec: 1.01x faster                                                                  |
| xml_etree_iterparse     | 104 ms                                                       | 103 ms: 1.01x faster                                                                    |
| sqlglot_optimize        | 59.8 ms                                                      | 59.3 ms: 1.01x faster                                                                   |
| comprehensions          | 24.6 us                                                      | 24.4 us: 1.01x faster                                                                   |
| 2to3                    | 288 ms                                                       | 286 ms: 1.01x faster                                                                    |
| pickle_pure_python      | 319 us                                                       | 318 us: 1.00x faster                                                                    |
| regex_dna               | 227 ms                                                       | 228 ms: 1.01x slower                                                                    |
| docutils                | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                                                  |
| pprint_safe_repr        | 784 ms                                                       | 793 ms: 1.01x slower                                                                    |
| scimark_sor             | 111 ms                                                       | 113 ms: 1.02x slower                                                                    |
| pathlib                 | 19.1 ms                                                      | 19.4 ms: 1.02x slower                                                                   |
| pickle                  | 9.64 us                                                      | 9.94 us: 1.03x slower                                                                   |
| pidigits                | 251 ms                                                       | 260 ms: 1.03x slower                                                                    |
| scimark_monte_carlo     | 68.2 ms                                                      | 70.7 ms: 1.04x slower                                                                   |
| telco                   | 6.86 ms                                                      | 7.11 ms: 1.04x slower                                                                   |
| xml_etree_process       | 56.5 ms                                                      | 59.1 ms: 1.05x slower                                                                   |
| python_startup          | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                                   |
| scimark_fft             | 285 ms                                                       | 299 ms: 1.05x slower                                                                    |
| bench_mp_pool           | 4.62 ms                                                      | 4.87 ms: 1.05x slower                                                                   |
| pickle_dict             | 30.8 us                                                      | 32.5 us: 1.06x slower                                                                   |
| meteor_contest          | 131 ms                                                       | 138 ms: 1.06x slower                                                                    |
| float                   | 74.2 ms                                                      | 78.5 ms: 1.06x slower                                                                   |
| sqlite_synth            | 2.50 us                                                      | 2.65 us: 1.06x slower                                                                   |
| xml_etree_generate      | 80.5 ms                                                      | 86.1 ms: 1.07x slower                                                                   |
| unpickle_list           | 4.53 us                                                      | 4.86 us: 1.07x slower                                                                   |
| python_startup_no_site  | 7.76 ms                                                      | 8.44 ms: 1.09x slower                                                                   |
| unpickle                | 13.4 us                                                      | 14.8 us: 1.10x slower                                                                   |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.47 ms: 1.10x slower                                                                   |
| pickle_list             | 3.83 us                                                      | 4.42 us: 1.15x slower                                                                   |
| coverage                | 84.8 ms                                                      | 98.7 ms: 1.16x slower                                                                   |
| async_generators        | 316 ms                                                       | 390 ms: 1.24x slower                                                                    |
| dask                    | 410 ms                                                       | 564 ms: 1.38x slower                                                                    |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                                            |

Benchmark hidden because not significant (2): create_gc_cycles, unpack_sequence
Ignored benchmarks (20) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.69% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
