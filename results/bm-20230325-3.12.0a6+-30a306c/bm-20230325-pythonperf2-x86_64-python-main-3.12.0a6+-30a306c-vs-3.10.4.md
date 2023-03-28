
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 30a306c
- commit date: 2023-03-25
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 285 ms: 1.24x faster                                         |
| chameleon      | 9.62 ms                                                      | 7.46 ms: 1.29x faster                                        |
| docutils       | 3.41 sec                                                     | 2.81 sec: 1.22x faster                                       |
| html5lib       | 96.3 ms                                                      | 68.9 ms: 1.40x faster                                        |
| tornado_http   | 151 ms                                                       | 114 ms: 1.33x faster                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 84.6 ms: 1.56x faster                                        |
| float          | 109 ms                                                       | 71.4 ms: 1.53x faster                                        |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.36x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 147 ms: 1.30x faster                                         |
| regex_v8       | 26.0 ms                                                      | 23.2 ms: 1.12x faster                                        |
| regex_dna      | 261 ms                                                       | 235 ms: 1.11x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.43 ms: 1.15x slower                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 206 us: 1.54x faster                                         |
| pickle_pure_python   | 451 us                                                       | 318 us: 1.42x faster                                         |
| json_dumps           | 14.3 ms                                                      | 10.2 ms: 1.39x faster                                        |
| xml_etree_process    | 77.6 ms                                                      | 57.5 ms: 1.35x faster                                        |
| json_loads           | 30.3 us                                                      | 24.2 us: 1.25x faster                                        |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                         |
| xml_etree_generate   | 94.1 ms                                                      | 83.6 ms: 1.13x faster                                        |
| pickle_list          | 4.11 us                                                      | 3.75 us: 1.10x faster                                        |
| xml_etree_iterparse  | 109 ms                                                       | 102 ms: 1.07x faster                                         |
| unpickle_list        | 4.73 us                                                      | 4.54 us: 1.04x faster                                        |
| unpickle             | 13.3 us                                                      | 13.4 us: 1.01x slower                                        |
| pickle_dict          | 29.5 us                                                      | 31.8 us: 1.08x slower                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.32 ms: 1.14x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                        |
| django_template | 52.0 ms                                                      | 40.8 ms: 1.27x faster                                        |
| genshi_text     | 31.7 ms                                                      | 25.2 ms: 1.26x faster                                        |
| genshi_xml      | 63.5 ms                                                      | 55.3 ms: 1.15x faster                                        |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.44 ms: 2.19x faster                                        |
| asyncio_tcp             | 787 ms                                                       | 387 ms: 2.03x faster                                         |
| raytrace                | 491 ms                                                       | 290 ms: 1.69x faster                                         |
| logging_silent          | 165 ns                                                       | 97.9 ns: 1.68x faster                                        |
| pyflate                 | 731 ms                                                       | 446 ms: 1.64x faster                                         |
| go                      | 264 ms                                                       | 162 ms: 1.63x faster                                         |
| scimark_lu              | 164 ms                                                       | 101 ms: 1.63x faster                                         |
| scimark_sor             | 177 ms                                                       | 111 ms: 1.60x faster                                         |
| richards                | 73.9 ms                                                      | 46.9 ms: 1.57x faster                                        |
| scimark_monte_carlo     | 109 ms                                                       | 69.1 ms: 1.57x faster                                        |
| nbody                   | 132 ms                                                       | 84.6 ms: 1.56x faster                                        |
| unpickle_pure_python    | 318 us                                                       | 206 us: 1.54x faster                                         |
| float                   | 109 ms                                                       | 71.4 ms: 1.53x faster                                        |
| chaos                   | 108 ms                                                       | 71.5 ms: 1.51x faster                                        |
| generators              | 57.0 ms                                                      | 37.9 ms: 1.51x faster                                        |
| spectral_norm           | 138 ms                                                       | 92.1 ms: 1.50x faster                                        |
| mako                    | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                        |
| hexiom                  | 9.54 ms                                                      | 6.50 ms: 1.47x faster                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.86 ms: 1.46x faster                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.55 ms: 1.44x faster                                        |
| deepcopy_memo           | 49.2 us                                                      | 34.6 us: 1.42x faster                                        |
| pickle_pure_python      | 451 us                                                       | 318 us: 1.42x faster                                         |
| crypto_pyaes            | 119 ms                                                       | 83.6 ms: 1.42x faster                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.92 ms: 1.40x faster                                        |
| html5lib                | 96.3 ms                                                      | 68.9 ms: 1.40x faster                                        |
| json_dumps              | 14.3 ms                                                      | 10.2 ms: 1.39x faster                                        |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                       |
| async_tree_none         | 698 ms                                                       | 510 ms: 1.37x faster                                         |
| unpack_sequence         | 59.7 ns                                                      | 43.8 ns: 1.36x faster                                        |
| async_tree_memoization  | 822 ms                                                       | 607 ms: 1.35x faster                                         |
| pycparser               | 1.66 sec                                                     | 1.23 sec: 1.35x faster                                       |
| xml_etree_process       | 77.6 ms                                                      | 57.5 ms: 1.35x faster                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.58 sec: 1.34x faster                                       |
| pprint_safe_repr        | 1.03 sec                                                     | 767 ms: 1.34x faster                                         |
| thrift                  | 1.23 ms                                                      | 919 us: 1.33x faster                                         |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.83 ms: 1.33x faster                                        |
| tornado_http            | 151 ms                                                       | 114 ms: 1.33x faster                                         |
| logging_simple          | 9.24 us                                                      | 7.04 us: 1.31x faster                                        |
| scimark_fft             | 359 ms                                                       | 274 ms: 1.31x faster                                         |
| logging_format          | 9.94 us                                                      | 7.62 us: 1.30x faster                                        |
| regex_compile           | 191 ms                                                       | 147 ms: 1.30x faster                                         |
| chameleon               | 9.62 ms                                                      | 7.46 ms: 1.29x faster                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 741 ms: 1.28x faster                                         |
| django_template         | 52.0 ms                                                      | 40.8 ms: 1.27x faster                                        |
| genshi_text             | 31.7 ms                                                      | 25.2 ms: 1.26x faster                                        |
| json_loads              | 30.3 us                                                      | 24.2 us: 1.25x faster                                        |
| 2to3                    | 352 ms                                                       | 285 ms: 1.24x faster                                         |
| coroutines              | 30.6 ms                                                      | 24.8 ms: 1.23x faster                                        |
| mypy2                   | 466 ms                                                       | 379 ms: 1.23x faster                                         |
| dulwich_log             | 80.5 ms                                                      | 65.7 ms: 1.23x faster                                        |
| docutils                | 3.41 sec                                                     | 2.81 sec: 1.22x faster                                       |
| sqlglot_normalize       | 147 ms                                                       | 121 ms: 1.21x faster                                         |
| deepcopy                | 457 us                                                       | 380 us: 1.20x faster                                         |
| sqlglot_optimize        | 70.1 ms                                                      | 58.4 ms: 1.20x faster                                        |
| bench_thread_pool       | 1.14 ms                                                      | 966 us: 1.18x faster                                         |
| json                    | 5.94 ms                                                      | 5.03 ms: 1.18x faster                                        |
| nqueens                 | 114 ms                                                       | 97.0 ms: 1.17x faster                                        |
| mdp                     | 2.95 sec                                                     | 2.53 sec: 1.17x faster                                       |
| genshi_xml              | 63.5 ms                                                      | 55.3 ms: 1.15x faster                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.42 us: 1.15x faster                                        |
| pathlib                 | 21.3 ms                                                      | 18.7 ms: 1.14x faster                                        |
| xml_etree_parse         | 160 ms                                                       | 142 ms: 1.13x faster                                         |
| xml_etree_generate      | 94.1 ms                                                      | 83.6 ms: 1.13x faster                                        |
| sqlite_synth            | 2.96 us                                                      | 2.63 us: 1.13x faster                                        |
| fannkuch                | 496 ms                                                       | 442 ms: 1.12x faster                                         |
| regex_v8                | 26.0 ms                                                      | 23.2 ms: 1.12x faster                                        |
| sympy_expand            | 603 ms                                                       | 538 ms: 1.12x faster                                         |
| sympy_integrate         | 28.1 ms                                                      | 25.2 ms: 1.12x faster                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.62 ms: 1.11x faster                                        |
| regex_dna               | 261 ms                                                       | 235 ms: 1.11x faster                                         |
| async_generators        | 419 ms                                                       | 377 ms: 1.11x faster                                         |
| meteor_contest          | 142 ms                                                       | 129 ms: 1.10x faster                                         |
| pickle_list             | 4.11 us                                                      | 3.75 us: 1.10x faster                                        |
| sympy_str               | 358 ms                                                       | 330 ms: 1.08x faster                                         |
| xml_etree_iterparse     | 109 ms                                                       | 102 ms: 1.07x faster                                         |
| telco                   | 7.14 ms                                                      | 6.78 ms: 1.05x faster                                        |
| unpickle_list           | 4.73 us                                                      | 4.54 us: 1.04x faster                                        |
| sympy_sum               | 193 ms                                                       | 185 ms: 1.04x faster                                         |
| pidigits                | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| python_startup          | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                        |
| comprehensions          | 27.3 us                                                      | 26.4 us: 1.03x faster                                        |
| unpickle                | 13.3 us                                                      | 13.4 us: 1.01x slower                                        |
| gc_traversal            | 3.46 ms                                                      | 3.59 ms: 1.04x slower                                        |
| pickle_dict             | 29.5 us                                                      | 31.8 us: 1.08x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.32 ms: 1.14x slower                                        |
| regex_effbot            | 2.99 ms                                                      | 3.43 ms: 1.15x slower                                        |
| dask                    | 478 ms                                                       | 568 ms: 1.19x slower                                         |
| coverage                | 71.1 ms                                                      | 90.5 ms: 1.27x slower                                        |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                 |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
