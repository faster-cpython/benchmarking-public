
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 4fe1c4b
- commit date: 2023-04-15
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                         |
| chameleon      | 7.67 ms                                                      | 7.49 ms: 1.02x faster                                        |
| docutils       | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                       |
| html5lib       | 72.9 ms                                                      | 68.4 ms: 1.07x faster                                        |
| tornado_http   | 122 ms                                                       | 114 ms: 1.07x faster                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 78.5 ms: 1.16x faster                                        |
| float          | 74.2 ms                                                      | 70.4 ms: 1.05x faster                                        |
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 148 ms: 1.07x faster                                         |
| regex_effbot   | 3.50 ms                                                      | 3.44 ms: 1.02x faster                                        |
| regex_v8       | 23.9 ms                                                      | 23.9 ms: 1.00x faster                                        |
| regex_dna      | 227 ms                                                       | 234 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                        |
| json_loads           | 28.7 us                                                      | 24.0 us: 1.20x faster                                        |
| unpickle_pure_python | 241 us                                                       | 211 us: 1.14x faster                                         |
| xml_etree_parse      | 158 ms                                                       | 146 ms: 1.08x faster                                         |
| xml_etree_iterparse  | 104 ms                                                       | 101 ms: 1.03x faster                                         |
| pickle_list          | 3.83 us                                                      | 3.74 us: 1.02x faster                                        |
| pickle_dict          | 30.8 us                                                      | 30.2 us: 1.02x faster                                        |
| pickle_pure_python   | 319 us                                                       | 321 us: 1.01x slower                                         |
| xml_etree_process    | 56.5 ms                                                      | 57.0 ms: 1.01x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.63 us: 1.02x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 82.4 ms: 1.02x slower                                        |
| pickle               | 9.64 us                                                      | 9.98 us: 1.04x slower                                        |
| unpickle             | 13.4 us                                                      | 14.2 us: 1.05x slower                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.34 ms: 1.08x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 9.90 ms: 1.11x faster                                        |
| genshi_xml      | 58.5 ms                                                      | 53.7 ms: 1.09x faster                                        |
| genshi_text     | 26.1 ms                                                      | 25.8 ms: 1.01x faster                                        |
| django_template | 40.2 ms                                                      | 41.3 ms: 1.03x slower                                        |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 383 ms: 1.97x faster                                         |
| generators              | 56.0 ms                                                      | 35.6 ms: 1.57x faster                                        |
| json_dumps              | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                        |
| json_loads              | 28.7 us                                                      | 24.0 us: 1.20x faster                                        |
| mypy2                   | 451 ms                                                       | 379 ms: 1.19x faster                                         |
| deltablue               | 4.00 ms                                                      | 3.39 ms: 1.18x faster                                        |
| nbody                   | 90.7 ms                                                      | 78.5 ms: 1.16x faster                                        |
| sqlglot_parse           | 1.53 ms                                                      | 1.34 ms: 1.15x faster                                        |
| scimark_lu              | 115 ms                                                       | 100.0 ms: 1.15x faster                                       |
| unpickle_pure_python    | 241 us                                                       | 211 us: 1.14x faster                                         |
| sqlglot_transpile       | 1.92 ms                                                      | 1.70 ms: 1.13x faster                                        |
| json                    | 5.65 ms                                                      | 5.03 ms: 1.12x faster                                        |
| coroutines              | 27.6 ms                                                      | 24.7 ms: 1.12x faster                                        |
| deepcopy_memo           | 38.8 us                                                      | 34.9 us: 1.11x faster                                        |
| mako                    | 11.0 ms                                                      | 9.90 ms: 1.11x faster                                        |
| chaos                   | 80.9 ms                                                      | 72.9 ms: 1.11x faster                                        |
| scimark_fft             | 285 ms                                                       | 261 ms: 1.09x faster                                         |
| genshi_xml              | 58.5 ms                                                      | 53.7 ms: 1.09x faster                                        |
| mdp                     | 2.75 sec                                                     | 2.52 sec: 1.09x faster                                       |
| fannkuch                | 429 ms                                                       | 395 ms: 1.08x faster                                         |
| gc_traversal            | 3.85 ms                                                      | 3.55 ms: 1.08x faster                                        |
| xml_etree_parse         | 158 ms                                                       | 146 ms: 1.08x faster                                         |
| hexiom                  | 7.13 ms                                                      | 6.63 ms: 1.08x faster                                        |
| raytrace                | 317 ms                                                       | 295 ms: 1.07x faster                                         |
| logging_silent          | 101 ns                                                       | 94.1 ns: 1.07x faster                                        |
| tornado_http            | 122 ms                                                       | 114 ms: 1.07x faster                                         |
| sqlglot_normalize       | 126 ms                                                       | 118 ms: 1.07x faster                                         |
| regex_compile           | 158 ms                                                       | 148 ms: 1.07x faster                                         |
| html5lib                | 72.9 ms                                                      | 68.4 ms: 1.07x faster                                        |
| pylint                  | 515 ms                                                       | 484 ms: 1.06x faster                                         |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.80 ms: 1.06x faster                                        |
| deepcopy                | 399 us                                                       | 377 us: 1.06x faster                                         |
| dulwich_log             | 68.4 ms                                                      | 64.7 ms: 1.06x faster                                        |
| float                   | 74.2 ms                                                      | 70.4 ms: 1.05x faster                                        |
| bench_thread_pool       | 1.01 ms                                                      | 962 us: 1.05x faster                                         |
| spectral_norm           | 93.3 ms                                                      | 89.6 ms: 1.04x faster                                        |
| logging_format          | 8.11 us                                                      | 7.80 us: 1.04x faster                                        |
| meteor_contest          | 131 ms                                                       | 126 ms: 1.04x faster                                         |
| logging_simple          | 7.19 us                                                      | 6.92 us: 1.04x faster                                        |
| sqlglot_optimize        | 59.8 ms                                                      | 57.8 ms: 1.03x faster                                        |
| xml_etree_iterparse     | 104 ms                                                       | 101 ms: 1.03x faster                                         |
| sympy_expand            | 555 ms                                                       | 537 ms: 1.03x faster                                         |
| deepcopy_reduce         | 3.51 us                                                      | 3.41 us: 1.03x faster                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.58 sec: 1.03x faster                                       |
| thrift                  | 925 us                                                       | 899 us: 1.03x faster                                         |
| pathlib                 | 19.1 ms                                                      | 18.5 ms: 1.03x faster                                        |
| nqueens                 | 103 ms                                                       | 100 ms: 1.03x faster                                         |
| docutils                | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                       |
| chameleon               | 7.67 ms                                                      | 7.49 ms: 1.02x faster                                        |
| pickle_list             | 3.83 us                                                      | 3.74 us: 1.02x faster                                        |
| async_tree_memoization  | 630 ms                                                       | 617 ms: 1.02x faster                                         |
| richards                | 48.3 ms                                                      | 47.3 ms: 1.02x faster                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 66.9 ms: 1.02x faster                                        |
| sympy_integrate         | 25.8 ms                                                      | 25.3 ms: 1.02x faster                                        |
| pickle_dict             | 30.8 us                                                      | 30.2 us: 1.02x faster                                        |
| sympy_str               | 337 ms                                                       | 331 ms: 1.02x faster                                         |
| regex_effbot            | 3.50 ms                                                      | 3.44 ms: 1.02x faster                                        |
| telco                   | 6.86 ms                                                      | 6.76 ms: 1.02x faster                                        |
| pycparser               | 1.32 sec                                                     | 1.30 sec: 1.02x faster                                       |
| genshi_text             | 26.1 ms                                                      | 25.8 ms: 1.01x faster                                        |
| pprint_safe_repr        | 784 ms                                                       | 773 ms: 1.01x faster                                         |
| 2to3                    | 288 ms                                                       | 284 ms: 1.01x faster                                         |
| sympy_sum               | 185 ms                                                       | 183 ms: 1.01x faster                                         |
| async_tree_io           | 1.17 sec                                                     | 1.16 sec: 1.01x faster                                       |
| async_tree_none         | 519 ms                                                       | 515 ms: 1.01x faster                                         |
| crypto_pyaes            | 83.4 ms                                                      | 82.8 ms: 1.01x faster                                        |
| scimark_sor             | 111 ms                                                       | 110 ms: 1.01x faster                                         |
| regex_v8                | 23.9 ms                                                      | 23.9 ms: 1.00x faster                                        |
| pickle_pure_python      | 319 us                                                       | 321 us: 1.01x slower                                         |
| comprehensions          | 24.6 us                                                      | 24.8 us: 1.01x slower                                        |
| xml_etree_process       | 56.5 ms                                                      | 57.0 ms: 1.01x slower                                        |
| create_gc_cycles        | 1.61 ms                                                      | 1.64 ms: 1.02x slower                                        |
| unpickle_list           | 4.53 us                                                      | 4.63 us: 1.02x slower                                        |
| xml_etree_generate      | 80.5 ms                                                      | 82.4 ms: 1.02x slower                                        |
| django_template         | 40.2 ms                                                      | 41.3 ms: 1.03x slower                                        |
| regex_dna               | 227 ms                                                       | 234 ms: 1.03x slower                                         |
| python_startup          | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                        |
| pidigits                | 251 ms                                                       | 260 ms: 1.03x slower                                         |
| sqlite_synth            | 2.50 us                                                      | 2.58 us: 1.03x slower                                        |
| pickle                  | 9.64 us                                                      | 9.98 us: 1.04x slower                                        |
| pyflate                 | 449 ms                                                       | 469 ms: 1.05x slower                                         |
| go                      | 164 ms                                                       | 172 ms: 1.05x slower                                         |
| unpickle                | 13.4 us                                                      | 14.2 us: 1.05x slower                                        |
| coverage                | 84.8 ms                                                      | 91.1 ms: 1.07x slower                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.34 ms: 1.08x slower                                        |
| bench_mp_pool           | 4.62 ms                                                      | 5.44 ms: 1.18x slower                                        |
| async_generators        | 316 ms                                                       | 388 ms: 1.23x slower                                         |
| dask                    | 410 ms                                                       | 564 ms: 1.38x slower                                         |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                 |

Benchmark hidden because not significant (2): unpack_sequence, async_tree_cpu_io_mixed
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
