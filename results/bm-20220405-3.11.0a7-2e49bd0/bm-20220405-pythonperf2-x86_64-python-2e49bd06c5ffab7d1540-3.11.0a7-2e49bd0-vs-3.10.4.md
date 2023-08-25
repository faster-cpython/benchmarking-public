
# Results vs. 3.10.4

- fork: python
- ref: 2e49bd06c5ffab7d1540
- machine: linux-x86_64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.19x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 293 ms: 1.19x faster                                                        |
| chameleon      | 9.72 ms                                                      | 7.97 ms: 1.22x faster                                                       |
| docutils       | 3.40 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 75.0 ms: 1.26x faster                                                       |
| tornado_http   | 152 ms                                                       | 123 ms: 1.23x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 93.6 ms: 1.47x faster                                                       |
| float          | 110 ms                                                       | 78.4 ms: 1.41x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 159 ms: 1.22x faster                                                        |
| regex_dna      | 259 ms                                                       | 253 ms: 1.03x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.13 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 331 us: 1.38x faster                                                        |
| unpickle_pure_python | 321 us                                                       | 242 us: 1.32x faster                                                        |
| xml_etree_process    | 76.0 ms                                                      | 58.3 ms: 1.30x faster                                                       |
| json_loads           | 30.0 us                                                      | 24.5 us: 1.22x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 82.8 ms: 1.14x faster                                                       |
| unpickle             | 14.2 us                                                      | 13.0 us: 1.09x faster                                                       |
| json_dumps           | 14.2 ms                                                      | 13.5 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 157 ms: 1.03x faster                                                        |
| pickle               | 9.94 us                                                      | 9.88 us: 1.01x faster                                                       |
| pickle_dict          | 30.0 us                                                      | 31.1 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                |

Benchmark hidden because not significant (2): pickle_list, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.4 ms: 1.11x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.46 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 11.2 ms: 1.31x faster                                                       |
| django_template | 51.5 ms                                                      | 40.7 ms: 1.27x faster                                                       |
| genshi_text     | 31.5 ms                                                      | 26.8 ms: 1.17x faster                                                       |
| genshi_xml      | 64.7 ms                                                      | 59.7 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 4.23 ms: 1.77x faster                                                       |
| logging_silent          | 166 ns                                                       | 105 ns: 1.58x faster                                                        |
| scimark_sor             | 177 ms                                                       | 112 ms: 1.57x faster                                                        |
| bench_mp_pool           | 7.18 ms                                                      | 4.60 ms: 1.56x faster                                                       |
| go                      | 259 ms                                                       | 166 ms: 1.55x faster                                                        |
| raytrace                | 488 ms                                                       | 322 ms: 1.52x faster                                                        |
| pyflate                 | 697 ms                                                       | 464 ms: 1.50x faster                                                        |
| nbody                   | 137 ms                                                       | 93.6 ms: 1.47x faster                                                       |
| chaos                   | 107 ms                                                       | 73.4 ms: 1.46x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                       | 77.1 ms: 1.42x faster                                                       |
| float                   | 110 ms                                                       | 78.4 ms: 1.41x faster                                                       |
| richards                | 74.1 ms                                                      | 52.8 ms: 1.40x faster                                                       |
| pickle_pure_python      | 457 us                                                       | 331 us: 1.38x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.18 sec: 1.36x faster                                                      |
| scimark_lu              | 164 ms                                                       | 120 ms: 1.36x faster                                                        |
| async_tree_none         | 700 ms                                                       | 523 ms: 1.34x faster                                                        |
| logging_simple          | 8.90 us                                                      | 6.69 us: 1.33x faster                                                       |
| async_generators        | 422 ms                                                       | 319 ms: 1.32x faster                                                        |
| unpickle_pure_python    | 321 us                                                       | 242 us: 1.32x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 89.5 ms: 1.32x faster                                                       |
| mako                    | 14.7 ms                                                      | 11.2 ms: 1.31x faster                                                       |
| xml_etree_process       | 76.0 ms                                                      | 58.3 ms: 1.30x faster                                                       |
| async_tree_memoization  | 824 ms                                                       | 641 ms: 1.29x faster                                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 818 ms: 1.28x faster                                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.69 sec: 1.27x faster                                                      |
| spectral_norm           | 136 ms                                                       | 107 ms: 1.27x faster                                                        |
| django_template         | 51.5 ms                                                      | 40.7 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed | 952 ms                                                       | 753 ms: 1.26x faster                                                        |
| dask                    | 463 ms                                                       | 367 ms: 1.26x faster                                                        |
| html5lib                | 94.6 ms                                                      | 75.0 ms: 1.26x faster                                                       |
| logging_format          | 9.57 us                                                      | 7.59 us: 1.26x faster                                                       |
| deepcopy_memo           | 48.9 us                                                      | 38.8 us: 1.26x faster                                                       |
| unpack_sequence         | 59.5 ns                                                      | 47.3 ns: 1.26x faster                                                       |
| thrift                  | 1.16 ms                                                      | 928 us: 1.25x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.33 sec: 1.25x faster                                                      |
| hexiom                  | 9.52 ms                                                      | 7.66 ms: 1.24x faster                                                       |
| aiohttp                 | 1.21 ms                                                      | 978 us: 1.24x faster                                                        |
| tornado_http            | 152 ms                                                       | 123 ms: 1.23x faster                                                        |
| json_loads              | 30.0 us                                                      | 24.5 us: 1.22x faster                                                       |
| chameleon               | 9.72 ms                                                      | 7.97 ms: 1.22x faster                                                       |
| regex_compile           | 194 ms                                                       | 159 ms: 1.22x faster                                                        |
| gunicorn                | 1.17 ms                                                      | 968 us: 1.21x faster                                                        |
| scimark_fft             | 359 ms                                                       | 297 ms: 1.21x faster                                                        |
| 2to3                    | 350 ms                                                       | 293 ms: 1.19x faster                                                        |
| sqlite_synth            | 2.97 us                                                      | 2.52 us: 1.18x faster                                                       |
| deepcopy                | 454 us                                                       | 385 us: 1.18x faster                                                        |
| genshi_text             | 31.5 ms                                                      | 26.8 ms: 1.17x faster                                                       |
| sqlalchemy_declarative  | 187 ms                                                       | 160 ms: 1.17x faster                                                        |
| docutils                | 3.40 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| deepcopy_reduce         | 4.03 us                                                      | 3.48 us: 1.16x faster                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.51 ms: 1.15x faster                                                       |
| json                    | 5.96 ms                                                      | 5.17 ms: 1.15x faster                                                       |
| dulwich_log             | 80.1 ms                                                      | 69.8 ms: 1.15x faster                                                       |
| xml_etree_generate      | 94.6 ms                                                      | 82.8 ms: 1.14x faster                                                       |
| sqlglot_normalize       | 144 ms                                                       | 127 ms: 1.14x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 2.38 ms: 1.14x faster                                                       |
| sqlglot_optimize        | 70.3 ms                                                      | 61.9 ms: 1.13x faster                                                       |
| fannkuch                | 496 ms                                                       | 442 ms: 1.12x faster                                                        |
| pathlib                 | 21.7 ms                                                      | 19.3 ms: 1.12x faster                                                       |
| flaskblogging           | 4.39 ms                                                      | 3.92 ms: 1.12x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 1.02 ms: 1.12x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 25.3 ms: 1.11x faster                                                       |
| python_startup          | 11.5 ms                                                      | 10.4 ms: 1.11x faster                                                       |
| sqlglot_parse           | 2.26 ms                                                      | 2.04 ms: 1.11x faster                                                       |
| create_gc_cycles        | 1.82 ms                                                      | 1.65 ms: 1.11x faster                                                       |
| sqlalchemy_imperative   | 22.6 ms                                                      | 20.5 ms: 1.10x faster                                                       |
| nqueens                 | 112 ms                                                       | 102 ms: 1.10x faster                                                        |
| mdp                     | 3.03 sec                                                     | 2.76 sec: 1.10x faster                                                      |
| sympy_expand            | 599 ms                                                       | 549 ms: 1.09x faster                                                        |
| unpickle                | 14.2 us                                                      | 13.0 us: 1.09x faster                                                       |
| sympy_sum               | 193 ms                                                       | 177 ms: 1.09x faster                                                        |
| pylint                  | 562 ms                                                       | 517 ms: 1.09x faster                                                        |
| genshi_xml              | 64.7 ms                                                      | 59.7 ms: 1.08x faster                                                       |
| sympy_str               | 358 ms                                                       | 330 ms: 1.08x faster                                                        |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| generators              | 58.0 ms                                                      | 54.7 ms: 1.06x faster                                                       |
| json_dumps              | 14.2 ms                                                      | 13.5 ms: 1.05x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.79 ms: 1.05x faster                                                       |
| asyncio_tcp             | 782 ms                                                       | 746 ms: 1.05x faster                                                        |
| coroutines              | 30.4 ms                                                      | 29.0 ms: 1.05x faster                                                       |
| xml_etree_iterparse     | 110 ms                                                       | 106 ms: 1.04x faster                                                        |
| xml_etree_parse         | 162 ms                                                       | 157 ms: 1.03x faster                                                        |
| meteor_contest          | 137 ms                                                       | 133 ms: 1.03x faster                                                        |
| regex_dna               | 259 ms                                                       | 253 ms: 1.03x faster                                                        |
| pickle                  | 9.94 us                                                      | 9.88 us: 1.01x faster                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.46 ms: 1.02x slower                                                       |
| comprehensions          | 26.9 us                                                      | 27.8 us: 1.03x slower                                                       |
| pickle_dict             | 30.0 us                                                      | 31.1 us: 1.04x slower                                                       |
| gc_traversal            | 3.45 ms                                                      | 3.58 ms: 1.04x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.13 ms: 1.05x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.19x faster                                                                |

Benchmark hidden because not significant (4): mypy2, regex_v8, pickle_list, unpickle_list
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x
