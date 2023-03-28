
# Results vs. 3.10.4

- fork: python
- ref: 2e49bd06c5ffab7d1540
- machine: linux-x86_64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 293 ms: 1.20x faster                                                        |
| chameleon      | 9.62 ms                                                      | 7.97 ms: 1.21x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| html5lib       | 96.3 ms                                                      | 75.0 ms: 1.28x faster                                                       |
| tornado_http   | 151 ms                                                       | 123 ms: 1.22x faster                                                        |
| Geometric mean | (ref)                                                        | 1.22x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 93.6 ms: 1.41x faster                                                       |
| float          | 109 ms                                                       | 78.4 ms: 1.40x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 159 ms: 1.20x faster                                                        |
| regex_dna      | 261 ms                                                       | 253 ms: 1.03x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 26.6 ms: 1.02x slower                                                       |
| regex_effbot   | 2.99 ms                                                      | 3.13 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 451 us                                                       | 331 us: 1.36x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 58.3 ms: 1.33x faster                                                       |
| unpickle_pure_python | 318 us                                                       | 242 us: 1.31x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                                       |
| xml_etree_generate   | 94.1 ms                                                      | 82.8 ms: 1.14x faster                                                       |
| json_dumps           | 14.3 ms                                                      | 13.5 ms: 1.06x faster                                                       |
| unpickle_list        | 4.73 us                                                      | 4.52 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 109 ms                                                       | 106 ms: 1.03x faster                                                        |
| pickle               | 10.1 us                                                      | 9.88 us: 1.03x faster                                                       |
| unpickle             | 13.3 us                                                      | 13.0 us: 1.02x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 157 ms: 1.02x faster                                                        |
| pickle_dict          | 29.5 us                                                      | 31.1 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                |

Benchmark hidden because not significant (1): pickle_list

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
| django_template | 52.0 ms                                                      | 40.7 ms: 1.28x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 26.8 ms: 1.18x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 59.7 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 4.23 ms: 1.78x faster                                                       |
| go                      | 264 ms                                                       | 166 ms: 1.59x faster                                                        |
| pyflate                 | 731 ms                                                       | 464 ms: 1.58x faster                                                        |
| scimark_sor             | 177 ms                                                       | 112 ms: 1.57x faster                                                        |
| logging_silent          | 165 ns                                                       | 105 ns: 1.57x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.60 ms: 1.54x faster                                                       |
| raytrace                | 491 ms                                                       | 322 ms: 1.53x faster                                                        |
| chaos                   | 108 ms                                                       | 73.4 ms: 1.47x faster                                                       |
| nbody                   | 132 ms                                                       | 93.6 ms: 1.41x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                       | 77.1 ms: 1.41x faster                                                       |
| richards                | 73.9 ms                                                      | 52.8 ms: 1.40x faster                                                       |
| float                   | 109 ms                                                       | 78.4 ms: 1.40x faster                                                       |
| logging_simple          | 9.24 us                                                      | 6.69 us: 1.38x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.18 sec: 1.37x faster                                                      |
| scimark_lu              | 164 ms                                                       | 120 ms: 1.36x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 331 us: 1.36x faster                                                        |
| async_tree_none         | 698 ms                                                       | 523 ms: 1.34x faster                                                        |
| xml_etree_process       | 77.6 ms                                                      | 58.3 ms: 1.33x faster                                                       |
| crypto_pyaes            | 119 ms                                                       | 89.5 ms: 1.32x faster                                                       |
| thrift                  | 1.23 ms                                                      | 928 us: 1.32x faster                                                        |
| mako                    | 14.7 ms                                                      | 11.2 ms: 1.31x faster                                                       |
| async_generators        | 419 ms                                                       | 319 ms: 1.31x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 242 us: 1.31x faster                                                        |
| logging_format          | 9.94 us                                                      | 7.59 us: 1.31x faster                                                       |
| dask                    | 478 ms                                                       | 367 ms: 1.30x faster                                                        |
| spectral_norm           | 138 ms                                                       | 107 ms: 1.29x faster                                                        |
| html5lib                | 96.3 ms                                                      | 75.0 ms: 1.28x faster                                                       |
| async_tree_memoization  | 822 ms                                                       | 641 ms: 1.28x faster                                                        |
| django_template         | 52.0 ms                                                      | 40.7 ms: 1.28x faster                                                       |
| deepcopy_memo           | 49.2 us                                                      | 38.8 us: 1.27x faster                                                       |
| unpack_sequence         | 59.7 ns                                                      | 47.3 ns: 1.26x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                       | 753 ms: 1.26x faster                                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.69 sec: 1.25x faster                                                      |
| pprint_safe_repr        | 1.03 sec                                                     | 818 ms: 1.25x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.33 sec: 1.25x faster                                                      |
| hexiom                  | 9.54 ms                                                      | 7.66 ms: 1.24x faster                                                       |
| json_loads              | 30.3 us                                                      | 24.5 us: 1.24x faster                                                       |
| tornado_http            | 151 ms                                                       | 123 ms: 1.22x faster                                                        |
| scimark_fft             | 359 ms                                                       | 297 ms: 1.21x faster                                                        |
| chameleon               | 9.62 ms                                                      | 7.97 ms: 1.21x faster                                                       |
| aiohttp                 | 1.18 ms                                                      | 978 us: 1.20x faster                                                        |
| 2to3                    | 352 ms                                                       | 293 ms: 1.20x faster                                                        |
| regex_compile           | 191 ms                                                       | 159 ms: 1.20x faster                                                        |
| deepcopy                | 457 us                                                       | 385 us: 1.19x faster                                                        |
| gunicorn                | 1.15 ms                                                      | 968 us: 1.18x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 26.8 ms: 1.18x faster                                                       |
| sqlite_synth            | 2.96 us                                                      | 2.52 us: 1.18x faster                                                       |
| sqlalchemy_declarative  | 188 ms                                                       | 160 ms: 1.18x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| sqlglot_normalize       | 147 ms                                                       | 127 ms: 1.16x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 69.8 ms: 1.15x faster                                                       |
| json                    | 5.94 ms                                                      | 5.17 ms: 1.15x faster                                                       |
| xml_etree_generate      | 94.1 ms                                                      | 82.8 ms: 1.14x faster                                                       |
| sqlglot_optimize        | 70.1 ms                                                      | 61.9 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.51 ms: 1.13x faster                                                       |
| sqlglot_transpile       | 2.69 ms                                                      | 2.38 ms: 1.13x faster                                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.48 us: 1.13x faster                                                       |
| fannkuch                | 496 ms                                                       | 442 ms: 1.12x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 1.02 ms: 1.12x faster                                                       |
| flaskblogging           | 4.37 ms                                                      | 3.92 ms: 1.11x faster                                                       |
| sqlalchemy_imperative   | 22.9 ms                                                      | 20.5 ms: 1.11x faster                                                       |
| nqueens                 | 114 ms                                                       | 102 ms: 1.11x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.3 ms: 1.11x faster                                                       |
| python_startup          | 11.5 ms                                                      | 10.4 ms: 1.11x faster                                                       |
| sqlglot_parse           | 2.24 ms                                                      | 2.04 ms: 1.10x faster                                                       |
| pathlib                 | 21.3 ms                                                      | 19.3 ms: 1.10x faster                                                       |
| sympy_expand            | 603 ms                                                       | 549 ms: 1.10x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.65 ms: 1.10x faster                                                       |
| sympy_sum               | 193 ms                                                       | 177 ms: 1.09x faster                                                        |
| pylint                  | 562 ms                                                       | 517 ms: 1.09x faster                                                        |
| sympy_str               | 358 ms                                                       | 330 ms: 1.08x faster                                                        |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| mdp                     | 2.95 sec                                                     | 2.76 sec: 1.07x faster                                                      |
| meteor_contest          | 142 ms                                                       | 133 ms: 1.07x faster                                                        |
| genshi_xml              | 63.5 ms                                                      | 59.7 ms: 1.06x faster                                                       |
| json_dumps              | 14.3 ms                                                      | 13.5 ms: 1.06x faster                                                       |
| asyncio_tcp             | 787 ms                                                       | 746 ms: 1.06x faster                                                        |
| coroutines              | 30.6 ms                                                      | 29.0 ms: 1.05x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.79 ms: 1.05x faster                                                       |
| unpickle_list           | 4.73 us                                                      | 4.52 us: 1.05x faster                                                       |
| generators              | 57.0 ms                                                      | 54.7 ms: 1.04x faster                                                       |
| regex_dna               | 261 ms                                                       | 253 ms: 1.03x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 106 ms: 1.03x faster                                                        |
| pickle                  | 10.1 us                                                      | 9.88 us: 1.03x faster                                                       |
| unpickle                | 13.3 us                                                      | 13.0 us: 1.02x faster                                                       |
| xml_etree_parse         | 160 ms                                                       | 157 ms: 1.02x faster                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.46 ms: 1.02x slower                                                       |
| comprehensions          | 27.3 us                                                      | 27.8 us: 1.02x slower                                                       |
| regex_v8                | 26.0 ms                                                      | 26.6 ms: 1.02x slower                                                       |
| gc_traversal            | 3.46 ms                                                      | 3.58 ms: 1.04x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.13 ms: 1.05x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 31.1 us: 1.05x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.19x faster                                                                |

Benchmark hidden because not significant (2): mypy2, pickle_list
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: coverage
