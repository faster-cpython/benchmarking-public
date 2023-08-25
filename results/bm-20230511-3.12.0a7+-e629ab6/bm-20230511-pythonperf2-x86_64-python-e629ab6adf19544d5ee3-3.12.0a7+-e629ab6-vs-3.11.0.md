
# Results vs. 3.11.0

- fork: python
- ref: e629ab6adf19544d5ee3
- machine: linux-x86_64
- commit hash: e629ab6
- commit date: 2023-05-11
- overall geometric mean: 1.04x faster \*
- HPT reliability: 97.67%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 283 ms: 1.01x faster                                                         |
| docutils       | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                                       |
| tornado_http   | 122 ms                                                       | 114 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 84.2 ms: 1.08x faster                                                        |
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                                         |
| float          | 74.2 ms                                                      | 79.9 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 145 ms: 1.09x faster                                                         |
| regex_effbot   | 3.50 ms                                                      | 3.55 ms: 1.02x slower                                                        |
| regex_v8       | 23.9 ms                                                      | 24.3 ms: 1.02x slower                                                        |
| regex_dna      | 227 ms                                                       | 234 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                        |
| json_loads           | 28.7 us                                                      | 24.5 us: 1.17x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 206 us: 1.17x faster                                                         |
| xml_etree_parse      | 158 ms                                                       | 150 ms: 1.05x faster                                                         |
| pickle_pure_python   | 319 us                                                       | 323 us: 1.01x slower                                                         |
| xml_etree_iterparse  | 104 ms                                                       | 107 ms: 1.02x slower                                                         |
| pickle_dict          | 30.8 us                                                      | 31.9 us: 1.04x slower                                                        |
| pickle               | 9.64 us                                                      | 10.0 us: 1.04x slower                                                        |
| xml_etree_process    | 56.5 ms                                                      | 59.0 ms: 1.04x slower                                                        |
| unpickle_list        | 4.53 us                                                      | 4.81 us: 1.06x slower                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 86.0 ms: 1.07x slower                                                        |
| unpickle             | 13.4 us                                                      | 14.8 us: 1.10x slower                                                        |
| pickle_list          | 3.83 us                                                      | 4.33 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.43 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 9.84 ms: 1.12x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 379 ms: 1.99x faster                                                         |
| generators              | 56.0 ms                                                      | 36.5 ms: 1.53x faster                                                        |
| json_dumps              | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                        |
| chaos                   | 80.9 ms                                                      | 64.8 ms: 1.25x faster                                                        |
| fannkuch                | 429 ms                                                       | 345 ms: 1.24x faster                                                         |
| deltablue               | 4.00 ms                                                      | 3.25 ms: 1.23x faster                                                        |
| mypy2                   | 451 ms                                                       | 367 ms: 1.23x faster                                                         |
| hexiom                  | 7.13 ms                                                      | 5.85 ms: 1.22x faster                                                        |
| coroutines              | 27.6 ms                                                      | 22.8 ms: 1.21x faster                                                        |
| json_loads              | 28.7 us                                                      | 24.5 us: 1.17x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 206 us: 1.17x faster                                                         |
| scimark_lu              | 115 ms                                                       | 99.4 ms: 1.15x faster                                                        |
| async_tree_memoization  | 630 ms                                                       | 549 ms: 1.15x faster                                                         |
| async_tree_none         | 519 ms                                                       | 456 ms: 1.14x faster                                                         |
| comprehensions          | 24.6 us                                                      | 22.0 us: 1.12x faster                                                        |
| async_tree_io           | 1.17 sec                                                     | 1.05 sec: 1.12x faster                                                       |
| mako                    | 11.0 ms                                                      | 9.84 ms: 1.12x faster                                                        |
| sqlglot_parse           | 1.53 ms                                                      | 1.38 ms: 1.11x faster                                                        |
| logging_format          | 8.11 us                                                      | 7.30 us: 1.11x faster                                                        |
| nqueens                 | 103 ms                                                       | 92.8 ms: 1.11x faster                                                        |
| json                    | 5.65 ms                                                      | 5.18 ms: 1.09x faster                                                        |
| regex_compile           | 158 ms                                                       | 145 ms: 1.09x faster                                                         |
| logging_simple          | 7.19 us                                                      | 6.66 us: 1.08x faster                                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.78 ms: 1.08x faster                                                        |
| nbody                   | 90.7 ms                                                      | 84.2 ms: 1.08x faster                                                        |
| go                      | 164 ms                                                       | 152 ms: 1.08x faster                                                         |
| async_tree_cpu_io_mixed | 749 ms                                                       | 697 ms: 1.07x faster                                                         |
| richards                | 48.3 ms                                                      | 44.9 ms: 1.07x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 117 ms: 1.07x faster                                                         |
| tornado_http            | 122 ms                                                       | 114 ms: 1.07x faster                                                         |
| deepcopy_memo           | 38.8 us                                                      | 36.4 us: 1.07x faster                                                        |
| raytrace                | 317 ms                                                       | 297 ms: 1.07x faster                                                         |
| mdp                     | 2.75 sec                                                     | 2.58 sec: 1.06x faster                                                       |
| deepcopy                | 399 us                                                       | 376 us: 1.06x faster                                                         |
| bench_thread_pool       | 1.01 ms                                                      | 960 us: 1.05x faster                                                         |
| xml_etree_parse         | 158 ms                                                       | 150 ms: 1.05x faster                                                         |
| logging_silent          | 101 ns                                                       | 96.0 ns: 1.05x faster                                                        |
| dulwich_log             | 68.4 ms                                                      | 65.7 ms: 1.04x faster                                                        |
| crypto_pyaes            | 83.4 ms                                                      | 80.2 ms: 1.04x faster                                                        |
| pycparser               | 1.32 sec                                                     | 1.28 sec: 1.04x faster                                                       |
| spectral_norm           | 93.3 ms                                                      | 90.5 ms: 1.03x faster                                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.42 us: 1.03x faster                                                        |
| sqlglot_optimize        | 59.8 ms                                                      | 58.4 ms: 1.02x faster                                                        |
| 2to3                    | 288 ms                                                       | 283 ms: 1.01x faster                                                         |
| meteor_contest          | 131 ms                                                       | 129 ms: 1.01x faster                                                         |
| pyflate                 | 449 ms                                                       | 444 ms: 1.01x faster                                                         |
| docutils                | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                                       |
| pickle_pure_python      | 319 us                                                       | 323 us: 1.01x slower                                                         |
| regex_effbot            | 3.50 ms                                                      | 3.55 ms: 1.02x slower                                                        |
| create_gc_cycles        | 1.61 ms                                                      | 1.63 ms: 1.02x slower                                                        |
| regex_v8                | 23.9 ms                                                      | 24.3 ms: 1.02x slower                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.66 sec: 1.02x slower                                                       |
| xml_etree_iterparse     | 104 ms                                                       | 107 ms: 1.02x slower                                                         |
| regex_dna               | 227 ms                                                       | 234 ms: 1.03x slower                                                         |
| pickle_dict             | 30.8 us                                                      | 31.9 us: 1.04x slower                                                        |
| pidigits                | 251 ms                                                       | 260 ms: 1.04x slower                                                         |
| telco                   | 6.86 ms                                                      | 7.11 ms: 1.04x slower                                                        |
| pprint_safe_repr        | 784 ms                                                       | 813 ms: 1.04x slower                                                         |
| pickle                  | 9.64 us                                                      | 10.0 us: 1.04x slower                                                        |
| xml_etree_process       | 56.5 ms                                                      | 59.0 ms: 1.04x slower                                                        |
| python_startup          | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                        |
| gc_traversal            | 3.85 ms                                                      | 4.06 ms: 1.05x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.64 us: 1.06x slower                                                        |
| scimark_fft             | 285 ms                                                       | 302 ms: 1.06x slower                                                         |
| unpickle_list           | 4.53 us                                                      | 4.81 us: 1.06x slower                                                        |
| xml_etree_generate      | 80.5 ms                                                      | 86.0 ms: 1.07x slower                                                        |
| float                   | 74.2 ms                                                      | 79.9 ms: 1.08x slower                                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 73.6 ms: 1.08x slower                                                        |
| pathlib                 | 19.1 ms                                                      | 20.7 ms: 1.08x slower                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.43 ms: 1.09x slower                                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.41 ms: 1.09x slower                                                        |
| unpickle                | 13.4 us                                                      | 14.8 us: 1.10x slower                                                        |
| coverage                | 84.8 ms                                                      | 94.6 ms: 1.12x slower                                                        |
| pickle_list             | 3.83 us                                                      | 4.33 us: 1.13x slower                                                        |
| unpack_sequence         | 45.6 ns                                                      | 52.9 ns: 1.16x slower                                                        |
| async_generators        | 316 ms                                                       | 385 ms: 1.22x slower                                                         |
| bench_mp_pool           | 4.62 ms                                                      | 5.93 ms: 1.28x slower                                                        |
| dask                    | 410 ms                                                       | 562 ms: 1.37x slower                                                         |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): scimark_sor
Ignored benchmarks (20) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 97.67% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
