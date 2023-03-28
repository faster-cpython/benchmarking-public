
# Results vs. 3.10.4

- fork: python
- ref: f533f216e6aaba3f3663
- machine: linux-x86_64
- commit hash: f533f21
- commit date: 2023-03-06
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 284 ms: 1.24x faster                                                         |
| chameleon      | 9.62 ms                                                      | 7.24 ms: 1.33x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.81 sec: 1.21x faster                                                       |
| html5lib       | 96.3 ms                                                      | 66.8 ms: 1.44x faster                                                        |
| tornado_http   | 151 ms                                                       | 116 ms: 1.30x faster                                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 73.5 ms: 1.49x faster                                                        |
| nbody          | 132 ms                                                       | 91.4 ms: 1.45x faster                                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 148 ms: 1.29x faster                                                         |
| regex_dna      | 261 ms                                                       | 232 ms: 1.12x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 24.1 ms: 1.08x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.62 ms: 1.21x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 202 us: 1.58x faster                                                         |
| pickle_pure_python   | 451 us                                                       | 305 us: 1.48x faster                                                         |
| json_dumps           | 14.3 ms                                                      | 10.2 ms: 1.40x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 57.4 ms: 1.35x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.0 us: 1.26x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 83.5 ms: 1.13x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.85 us: 1.07x faster                                                        |
| unpickle_list        | 4.73 us                                                      | 4.51 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 109 ms                                                       | 104 ms: 1.04x faster                                                         |
| unpickle             | 13.3 us                                                      | 13.8 us: 1.04x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 32.2 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.16x faster                                                                 |

Benchmark hidden because not significant (1): pickle

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
| mako            | 14.7 ms                                                      | 10.2 ms: 1.45x faster                                                        |
| django_template | 52.0 ms                                                      | 39.1 ms: 1.33x faster                                                        |
| genshi_text     | 31.7 ms                                                      | 25.5 ms: 1.24x faster                                                        |
| genshi_xml      | 63.5 ms                                                      | 54.9 ms: 1.16x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf2-x86_64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.35 ms: 2.25x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 386 ms: 2.04x faster                                                         |
| go                      | 264 ms                                                       | 153 ms: 1.72x faster                                                         |
| logging_silent          | 165 ns                                                       | 95.6 ns: 1.72x faster                                                        |
| pyflate                 | 731 ms                                                       | 435 ms: 1.68x faster                                                         |
| richards                | 73.9 ms                                                      | 44.0 ms: 1.68x faster                                                        |
| raytrace                | 491 ms                                                       | 295 ms: 1.67x faster                                                         |
| scimark_sor             | 177 ms                                                       | 107 ms: 1.66x faster                                                         |
| scimark_lu              | 164 ms                                                       | 103 ms: 1.59x faster                                                         |
| unpickle_pure_python    | 318 us                                                       | 202 us: 1.58x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                       | 69.4 ms: 1.57x faster                                                        |
| generators              | 57.0 ms                                                      | 38.2 ms: 1.49x faster                                                        |
| float                   | 109 ms                                                       | 73.5 ms: 1.49x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 305 us: 1.48x faster                                                         |
| spectral_norm           | 138 ms                                                       | 94.0 ms: 1.47x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.87 ms: 1.46x faster                                                        |
| chaos                   | 108 ms                                                       | 74.1 ms: 1.46x faster                                                        |
| hexiom                  | 9.54 ms                                                      | 6.55 ms: 1.46x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.45x faster                                                        |
| nbody                   | 132 ms                                                       | 91.4 ms: 1.45x faster                                                        |
| html5lib                | 96.3 ms                                                      | 66.8 ms: 1.44x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 82.3 ms: 1.44x faster                                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.58 ms: 1.42x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 10.2 ms: 1.40x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                                       |
| logging_simple          | 9.24 us                                                      | 6.66 us: 1.39x faster                                                        |
| async_tree_none         | 698 ms                                                       | 507 ms: 1.38x faster                                                         |
| sqlglot_transpile       | 2.69 ms                                                      | 1.95 ms: 1.38x faster                                                        |
| deepcopy_memo           | 49.2 us                                                      | 35.8 us: 1.37x faster                                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.57 sec: 1.36x faster                                                       |
| async_tree_memoization  | 822 ms                                                       | 607 ms: 1.35x faster                                                         |
| xml_etree_process       | 77.6 ms                                                      | 57.4 ms: 1.35x faster                                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 764 ms: 1.34x faster                                                         |
| logging_format          | 9.94 us                                                      | 7.45 us: 1.33x faster                                                        |
| django_template         | 52.0 ms                                                      | 39.1 ms: 1.33x faster                                                        |
| chameleon               | 9.62 ms                                                      | 7.24 ms: 1.33x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 45.0 ns: 1.33x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.26 sec: 1.31x faster                                                       |
| tornado_http            | 151 ms                                                       | 116 ms: 1.30x faster                                                         |
| regex_compile           | 191 ms                                                       | 148 ms: 1.29x faster                                                         |
| async_tree_cpu_io_mixed | 951 ms                                                       | 744 ms: 1.28x faster                                                         |
| scimark_fft             | 359 ms                                                       | 282 ms: 1.28x faster                                                         |
| json_loads              | 30.3 us                                                      | 24.0 us: 1.26x faster                                                        |
| thrift                  | 1.23 ms                                                      | 972 us: 1.26x faster                                                         |
| dulwich_log             | 80.5 ms                                                      | 64.3 ms: 1.25x faster                                                        |
| mypy2                   | 466 ms                                                       | 375 ms: 1.24x faster                                                         |
| genshi_text             | 31.7 ms                                                      | 25.5 ms: 1.24x faster                                                        |
| 2to3                    | 352 ms                                                       | 284 ms: 1.24x faster                                                         |
| coroutines              | 30.6 ms                                                      | 24.8 ms: 1.23x faster                                                        |
| sqlglot_normalize       | 147 ms                                                       | 120 ms: 1.23x faster                                                         |
| docutils                | 3.41 sec                                                     | 2.81 sec: 1.21x faster                                                       |
| sqlglot_optimize        | 70.1 ms                                                      | 58.2 ms: 1.20x faster                                                        |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.26 ms: 1.20x faster                                                        |
| json                    | 5.94 ms                                                      | 4.97 ms: 1.20x faster                                                        |
| fannkuch                | 496 ms                                                       | 419 ms: 1.18x faster                                                         |
| bench_thread_pool       | 1.14 ms                                                      | 965 us: 1.18x faster                                                         |
| deepcopy                | 457 us                                                       | 390 us: 1.17x faster                                                         |
| genshi_xml              | 63.5 ms                                                      | 54.9 ms: 1.16x faster                                                        |
| pathlib                 | 21.3 ms                                                      | 18.5 ms: 1.15x faster                                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.41 us: 1.15x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.62 us: 1.13x faster                                                        |
| nqueens                 | 114 ms                                                       | 100 ms: 1.13x faster                                                         |
| sympy_integrate         | 28.1 ms                                                      | 24.9 ms: 1.13x faster                                                        |
| xml_etree_generate      | 94.1 ms                                                      | 83.5 ms: 1.13x faster                                                        |
| sympy_expand            | 603 ms                                                       | 535 ms: 1.13x faster                                                         |
| regex_dna               | 261 ms                                                       | 232 ms: 1.12x faster                                                         |
| xml_etree_parse         | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| mdp                     | 2.95 sec                                                     | 2.64 sec: 1.12x faster                                                       |
| meteor_contest          | 142 ms                                                       | 129 ms: 1.10x faster                                                         |
| regex_v8                | 26.0 ms                                                      | 24.1 ms: 1.08x faster                                                        |
| sympy_str               | 358 ms                                                       | 332 ms: 1.08x faster                                                         |
| async_generators        | 419 ms                                                       | 389 ms: 1.08x faster                                                         |
| pidigits                | 271 ms                                                       | 252 ms: 1.08x faster                                                         |
| create_gc_cycles        | 1.80 ms                                                      | 1.68 ms: 1.07x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.85 us: 1.07x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.51 us: 1.05x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 104 ms: 1.04x faster                                                         |
| sympy_sum               | 193 ms                                                       | 186 ms: 1.04x faster                                                         |
| comprehensions          | 27.3 us                                                      | 26.4 us: 1.03x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.92 ms: 1.03x faster                                                        |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                        |
| unpickle                | 13.3 us                                                      | 13.8 us: 1.04x slower                                                        |
| pickle_dict             | 29.5 us                                                      | 32.2 us: 1.09x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.34 ms: 1.14x slower                                                        |
| coverage                | 71.1 ms                                                      | 82.8 ms: 1.17x slower                                                        |
| dask                    | 478 ms                                                       | 566 ms: 1.18x slower                                                         |
| regex_effbot            | 2.99 ms                                                      | 3.62 ms: 1.21x slower                                                        |
| gc_traversal            | 3.46 ms                                                      | 4.26 ms: 1.23x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                                 |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
