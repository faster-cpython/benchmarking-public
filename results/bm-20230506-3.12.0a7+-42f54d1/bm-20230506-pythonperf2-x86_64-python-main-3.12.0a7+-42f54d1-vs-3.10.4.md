
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.27x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                         |
| docutils       | 3.40 sec                                                     | 2.90 sec: 1.17x faster                                       |
| tornado_http   | 152 ms                                                       | 116 ms: 1.32x faster                                         |
| Geometric mean | (ref)                                                        | 1.24x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 91.8 ms: 1.49x faster                                        |
| float          | 110 ms                                                       | 77.6 ms: 1.42x faster                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 146 ms: 1.32x faster                                         |
| regex_v8       | 26.6 ms                                                      | 23.9 ms: 1.12x faster                                        |
| regex_dna      | 259 ms                                                       | 234 ms: 1.11x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.42 ms: 1.14x slower                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 206 us: 1.56x faster                                         |
| pickle_pure_python   | 457 us                                                       | 319 us: 1.44x faster                                         |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                        |
| xml_etree_process    | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                        |
| json_loads           | 30.0 us                                                      | 24.2 us: 1.24x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 85.2 ms: 1.11x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 146 ms: 1.11x faster                                         |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| unpickle             | 14.2 us                                                      | 14.6 us: 1.03x slower                                        |
| pickle_dict          | 30.0 us                                                      | 31.8 us: 1.06x slower                                        |
| unpickle_list        | 4.49 us                                                      | 4.81 us: 1.07x slower                                        |
| pickle_list          | 4.11 us                                                      | 4.42 us: 1.08x slower                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.39 ms: 1.15x slower                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.27 ms: 2.29x faster                                        |
| asyncio_tcp             | 782 ms                                                       | 383 ms: 2.04x faster                                         |
| logging_silent          | 166 ns                                                       | 91.5 ns: 1.81x faster                                        |
| go                      | 259 ms                                                       | 147 ms: 1.76x faster                                         |
| richards                | 74.1 ms                                                      | 45.0 ms: 1.65x faster                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.38 ms: 1.64x faster                                        |
| scimark_lu              | 164 ms                                                       | 100 ms: 1.63x faster                                         |
| hexiom                  | 9.52 ms                                                      | 5.86 ms: 1.62x faster                                        |
| pyflate                 | 697 ms                                                       | 438 ms: 1.59x faster                                         |
| chaos                   | 107 ms                                                       | 67.4 ms: 1.59x faster                                        |
| raytrace                | 488 ms                                                       | 307 ms: 1.59x faster                                         |
| generators              | 58.0 ms                                                      | 36.6 ms: 1.58x faster                                        |
| scimark_sor             | 177 ms                                                       | 112 ms: 1.57x faster                                         |
| unpickle_pure_python    | 321 us                                                       | 206 us: 1.56x faster                                         |
| scimark_monte_carlo     | 109 ms                                                       | 71.7 ms: 1.53x faster                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.78 ms: 1.52x faster                                        |
| nbody                   | 137 ms                                                       | 91.8 ms: 1.49x faster                                        |
| spectral_norm           | 136 ms                                                       | 92.6 ms: 1.47x faster                                        |
| async_tree_io           | 1.61 sec                                                     | 1.10 sec: 1.46x faster                                       |
| async_tree_none         | 700 ms                                                       | 481 ms: 1.45x faster                                         |
| mako                    | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                        |
| fannkuch                | 496 ms                                                       | 343 ms: 1.45x faster                                         |
| bench_mp_pool           | 7.18 ms                                                      | 4.98 ms: 1.44x faster                                        |
| crypto_pyaes            | 118 ms                                                       | 82.1 ms: 1.44x faster                                        |
| pickle_pure_python      | 457 us                                                       | 319 us: 1.44x faster                                         |
| async_tree_memoization  | 824 ms                                                       | 578 ms: 1.43x faster                                         |
| float                   | 110 ms                                                       | 77.6 ms: 1.42x faster                                        |
| json_dumps              | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                        |
| coroutines              | 30.4 ms                                                      | 22.3 ms: 1.36x faster                                        |
| deepcopy_memo           | 48.9 us                                                      | 36.2 us: 1.35x faster                                        |
| pycparser               | 1.66 sec                                                     | 1.24 sec: 1.34x faster                                       |
| async_tree_cpu_io_mixed | 952 ms                                                       | 715 ms: 1.33x faster                                         |
| pprint_pformat          | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                       |
| regex_compile           | 194 ms                                                       | 146 ms: 1.32x faster                                         |
| pprint_safe_repr        | 1.05 sec                                                     | 798 ms: 1.32x faster                                         |
| tornado_http            | 152 ms                                                       | 116 ms: 1.32x faster                                         |
| logging_simple          | 8.90 us                                                      | 6.87 us: 1.30x faster                                        |
| xml_etree_process       | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                        |
| nqueens                 | 112 ms                                                       | 88.1 ms: 1.28x faster                                        |
| logging_format          | 9.57 us                                                      | 7.56 us: 1.27x faster                                        |
| mypy2                   | 466 ms                                                       | 373 ms: 1.25x faster                                         |
| json_loads              | 30.0 us                                                      | 24.2 us: 1.24x faster                                        |
| 2to3                    | 350 ms                                                       | 284 ms: 1.23x faster                                         |
| dulwich_log             | 80.1 ms                                                      | 65.3 ms: 1.23x faster                                        |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.26 ms: 1.22x faster                                        |
| deepcopy                | 454 us                                                       | 375 us: 1.21x faster                                         |
| mdp                     | 3.03 sec                                                     | 2.51 sec: 1.21x faster                                       |
| bench_thread_pool       | 1.14 ms                                                      | 944 us: 1.20x faster                                         |
| sqlglot_normalize       | 144 ms                                                       | 120 ms: 1.20x faster                                         |
| scimark_fft             | 359 ms                                                       | 300 ms: 1.20x faster                                         |
| deepcopy_reduce         | 4.03 us                                                      | 3.37 us: 1.20x faster                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 58.8 ms: 1.20x faster                                        |
| unpack_sequence         | 59.5 ns                                                      | 50.1 ns: 1.19x faster                                        |
| docutils                | 3.40 sec                                                     | 2.90 sec: 1.17x faster                                       |
| json                    | 5.96 ms                                                      | 5.21 ms: 1.14x faster                                        |
| sqlite_synth            | 2.97 us                                                      | 2.63 us: 1.13x faster                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.63 ms: 1.12x faster                                        |
| regex_v8                | 26.6 ms                                                      | 23.9 ms: 1.12x faster                                        |
| xml_etree_generate      | 94.6 ms                                                      | 85.2 ms: 1.11x faster                                        |
| regex_dna               | 259 ms                                                       | 234 ms: 1.11x faster                                         |
| xml_etree_parse         | 162 ms                                                       | 146 ms: 1.11x faster                                         |
| comprehensions          | 26.9 us                                                      | 24.4 us: 1.10x faster                                        |
| pathlib                 | 21.7 ms                                                      | 20.0 ms: 1.08x faster                                        |
| async_generators        | 422 ms                                                       | 392 ms: 1.08x faster                                         |
| meteor_contest          | 137 ms                                                       | 129 ms: 1.06x faster                                         |
| xml_etree_iterparse     | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                        |
| telco                   | 7.14 ms                                                      | 7.27 ms: 1.02x slower                                        |
| unpickle                | 14.2 us                                                      | 14.6 us: 1.03x slower                                        |
| pickle_dict             | 30.0 us                                                      | 31.8 us: 1.06x slower                                        |
| unpickle_list           | 4.49 us                                                      | 4.81 us: 1.07x slower                                        |
| pickle_list             | 4.11 us                                                      | 4.42 us: 1.08x slower                                        |
| gc_traversal            | 3.45 ms                                                      | 3.82 ms: 1.11x slower                                        |
| regex_effbot            | 2.99 ms                                                      | 3.42 ms: 1.14x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.39 ms: 1.15x slower                                        |
| dask                    | 463 ms                                                       | 560 ms: 1.21x slower                                         |
| coverage                | 64.0 ms                                                      | 92.9 ms: 1.45x slower                                        |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                 |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x
