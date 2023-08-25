
# Results vs. 3.10.4

- fork: python
- ref: f533f216e6aaba3f3663
- machine: linux-x86_64
- commit hash: f533f21
- commit date: 2023-03-06
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                         |
| chameleon      | 9.72 ms                                                      | 7.24 ms: 1.34x faster                                                        |
| docutils       | 3.40 sec                                                     | 2.81 sec: 1.21x faster                                                       |
| html5lib       | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                        |
| tornado_http   | 152 ms                                                       | 116 ms: 1.31x faster                                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 91.4 ms: 1.50x faster                                                        |
| float          | 110 ms                                                       | 73.5 ms: 1.50x faster                                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 148 ms: 1.31x faster                                                         |
| regex_dna      | 259 ms                                                       | 232 ms: 1.12x faster                                                         |
| regex_v8       | 26.6 ms                                                      | 24.1 ms: 1.11x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.62 ms: 1.21x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 202 us: 1.59x faster                                                         |
| pickle_pure_python   | 457 us                                                       | 305 us: 1.50x faster                                                         |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                        |
| xml_etree_process    | 76.0 ms                                                      | 57.4 ms: 1.32x faster                                                        |
| json_loads           | 30.0 us                                                      | 24.0 us: 1.25x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 83.5 ms: 1.13x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 143 ms: 1.13x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.85 us: 1.07x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| unpickle             | 14.2 us                                                      | 13.8 us: 1.02x faster                                                        |
| pickle               | 9.94 us                                                      | 10.2 us: 1.02x slower                                                        |
| pickle_dict          | 30.0 us                                                      | 32.2 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.34 ms: 1.14x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| django_template | 51.5 ms                                                      | 39.1 ms: 1.32x faster                                                        |
| genshi_text     | 31.5 ms                                                      | 25.5 ms: 1.23x faster                                                        |
| genshi_xml      | 64.7 ms                                                      | 54.9 ms: 1.18x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.35 ms: 2.23x faster                                                        |
| asyncio_tcp             | 782 ms                                                       | 386 ms: 2.03x faster                                                         |
| logging_silent          | 166 ns                                                       | 95.6 ns: 1.73x faster                                                        |
| go                      | 259 ms                                                       | 153 ms: 1.69x faster                                                         |
| richards                | 74.1 ms                                                      | 44.0 ms: 1.68x faster                                                        |
| scimark_sor             | 177 ms                                                       | 107 ms: 1.66x faster                                                         |
| raytrace                | 488 ms                                                       | 295 ms: 1.65x faster                                                         |
| pyflate                 | 697 ms                                                       | 435 ms: 1.60x faster                                                         |
| unpickle_pure_python    | 321 us                                                       | 202 us: 1.59x faster                                                         |
| scimark_lu              | 164 ms                                                       | 103 ms: 1.58x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                       | 69.4 ms: 1.58x faster                                                        |
| generators              | 58.0 ms                                                      | 38.2 ms: 1.52x faster                                                        |
| nbody                   | 137 ms                                                       | 91.4 ms: 1.50x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 305 us: 1.50x faster                                                         |
| float                   | 110 ms                                                       | 73.5 ms: 1.50x faster                                                        |
| bench_mp_pool           | 7.18 ms                                                      | 4.87 ms: 1.47x faster                                                        |
| hexiom                  | 9.52 ms                                                      | 6.55 ms: 1.45x faster                                                        |
| spectral_norm           | 136 ms                                                       | 94.0 ms: 1.45x faster                                                        |
| chaos                   | 107 ms                                                       | 74.1 ms: 1.45x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 82.3 ms: 1.44x faster                                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.58 ms: 1.43x faster                                                        |
| html5lib                | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.95 ms: 1.39x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                                       |
| async_tree_none         | 700 ms                                                       | 507 ms: 1.38x faster                                                         |
| pprint_pformat          | 2.15 sec                                                     | 1.57 sec: 1.38x faster                                                       |
| pprint_safe_repr        | 1.05 sec                                                     | 764 ms: 1.37x faster                                                         |
| deepcopy_memo           | 48.9 us                                                      | 35.8 us: 1.36x faster                                                        |
| async_tree_memoization  | 824 ms                                                       | 607 ms: 1.36x faster                                                         |
| chameleon               | 9.72 ms                                                      | 7.24 ms: 1.34x faster                                                        |
| logging_simple          | 8.90 us                                                      | 6.66 us: 1.34x faster                                                        |
| xml_etree_process       | 76.0 ms                                                      | 57.4 ms: 1.32x faster                                                        |
| unpack_sequence         | 59.5 ns                                                      | 45.0 ns: 1.32x faster                                                        |
| django_template         | 51.5 ms                                                      | 39.1 ms: 1.32x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                                       |
| tornado_http            | 152 ms                                                       | 116 ms: 1.31x faster                                                         |
| regex_compile           | 194 ms                                                       | 148 ms: 1.31x faster                                                         |
| logging_format          | 9.57 us                                                      | 7.45 us: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 744 ms: 1.28x faster                                                         |
| scimark_fft             | 359 ms                                                       | 282 ms: 1.28x faster                                                         |
| json_loads              | 30.0 us                                                      | 24.0 us: 1.25x faster                                                        |
| dulwich_log             | 80.1 ms                                                      | 64.3 ms: 1.24x faster                                                        |
| mypy2                   | 466 ms                                                       | 375 ms: 1.24x faster                                                         |
| genshi_text             | 31.5 ms                                                      | 25.5 ms: 1.23x faster                                                        |
| 2to3                    | 350 ms                                                       | 284 ms: 1.23x faster                                                         |
| coroutines              | 30.4 ms                                                      | 24.8 ms: 1.23x faster                                                        |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.26 ms: 1.22x faster                                                        |
| docutils                | 3.40 sec                                                     | 2.81 sec: 1.21x faster                                                       |
| sqlglot_optimize        | 70.3 ms                                                      | 58.2 ms: 1.21x faster                                                        |
| sqlglot_normalize       | 144 ms                                                       | 120 ms: 1.21x faster                                                         |
| json                    | 5.96 ms                                                      | 4.97 ms: 1.20x faster                                                        |
| thrift                  | 1.16 ms                                                      | 972 us: 1.20x faster                                                         |
| fannkuch                | 496 ms                                                       | 419 ms: 1.18x faster                                                         |
| genshi_xml              | 64.7 ms                                                      | 54.9 ms: 1.18x faster                                                        |
| deepcopy_reduce         | 4.03 us                                                      | 3.41 us: 1.18x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 965 us: 1.18x faster                                                         |
| pathlib                 | 21.7 ms                                                      | 18.5 ms: 1.17x faster                                                        |
| deepcopy                | 454 us                                                       | 390 us: 1.16x faster                                                         |
| mdp                     | 3.03 sec                                                     | 2.64 sec: 1.15x faster                                                       |
| sqlite_synth            | 2.97 us                                                      | 2.62 us: 1.13x faster                                                        |
| xml_etree_generate      | 94.6 ms                                                      | 83.5 ms: 1.13x faster                                                        |
| xml_etree_parse         | 162 ms                                                       | 143 ms: 1.13x faster                                                         |
| sympy_integrate         | 28.1 ms                                                      | 24.9 ms: 1.13x faster                                                        |
| nqueens                 | 112 ms                                                       | 100 ms: 1.12x faster                                                         |
| sympy_expand            | 599 ms                                                       | 535 ms: 1.12x faster                                                         |
| regex_dna               | 259 ms                                                       | 232 ms: 1.12x faster                                                         |
| regex_v8                | 26.6 ms                                                      | 24.1 ms: 1.11x faster                                                        |
| async_generators        | 422 ms                                                       | 389 ms: 1.08x faster                                                         |
| create_gc_cycles        | 1.82 ms                                                      | 1.68 ms: 1.08x faster                                                        |
| sympy_str               | 358 ms                                                       | 332 ms: 1.08x faster                                                         |
| pidigits                | 271 ms                                                       | 252 ms: 1.08x faster                                                         |
| pickle_list             | 4.11 us                                                      | 3.85 us: 1.07x faster                                                        |
| meteor_contest          | 137 ms                                                       | 129 ms: 1.06x faster                                                         |
| xml_etree_iterparse     | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| sympy_sum               | 193 ms                                                       | 186 ms: 1.04x faster                                                         |
| telco                   | 7.14 ms                                                      | 6.92 ms: 1.03x faster                                                        |
| unpickle                | 14.2 us                                                      | 13.8 us: 1.02x faster                                                        |
| comprehensions          | 26.9 us                                                      | 26.4 us: 1.02x faster                                                        |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                        |
| pickle                  | 9.94 us                                                      | 10.2 us: 1.02x slower                                                        |
| pickle_dict             | 30.0 us                                                      | 32.2 us: 1.07x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.34 ms: 1.14x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.62 ms: 1.21x slower                                                        |
| dask                    | 463 ms                                                       | 566 ms: 1.22x slower                                                         |
| gc_traversal            | 3.45 ms                                                      | 4.26 ms: 1.24x slower                                                        |
| coverage                | 64.0 ms                                                      | 82.8 ms: 1.29x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.25x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x
