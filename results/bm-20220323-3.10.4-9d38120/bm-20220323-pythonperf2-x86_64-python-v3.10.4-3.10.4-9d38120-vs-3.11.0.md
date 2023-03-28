
# Results vs. 3.11.0

- fork: python
- ref: v3.10.4
- machine: linux-x86_64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.22x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 289 ms                                                                    | 352 ms: 1.22x slower                                         |
| chameleon      | 7.50 ms                                                                   | 9.62 ms: 1.28x slower                                        |
| docutils       | 2.86 sec                                                                  | 3.41 sec: 1.19x slower                                       |
| html5lib       | 70.2 ms                                                                   | 96.3 ms: 1.37x slower                                        |
| tornado_http   | 125 ms                                                                    | 151 ms: 1.21x slower                                         |
| Geometric mean | (ref)                                                                     | 1.25x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 252 ms                                                                    | 271 ms: 1.08x slower                                         |
| nbody          | 92.1 ms                                                                   | 132 ms: 1.44x slower                                         |
| float          | 75.7 ms                                                                   | 109 ms: 1.45x slower                                         |
| Geometric mean | (ref)                                                                     | 1.31x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.31 ms                                                                   | 2.99 ms: 1.11x faster                                        |
| regex_v8       | 24.4 ms                                                                   | 26.0 ms: 1.06x slower                                        |
| regex_dna      | 225 ms                                                                    | 261 ms: 1.16x slower                                         |
| regex_compile  | 154 ms                                                                    | 191 ms: 1.24x slower                                         |
| Geometric mean | (ref)                                                                     | 1.08x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_dict          | 31.1 us                                                                   | 29.5 us: 1.05x faster                                        |
| unpickle             | 13.0 us                                                                   | 13.3 us: 1.02x slower                                        |
| pickle               | 9.92 us                                                                   | 10.1 us: 1.02x slower                                        |
| xml_etree_iterparse  | 106 ms                                                                    | 109 ms: 1.03x slower                                         |
| unpickle_list        | 4.52 us                                                                   | 4.73 us: 1.05x slower                                        |
| json_loads           | 28.4 us                                                                   | 30.3 us: 1.07x slower                                        |
| json_dumps           | 13.4 ms                                                                   | 14.3 ms: 1.07x slower                                        |
| pickle_list          | 3.78 us                                                                   | 4.11 us: 1.09x slower                                        |
| xml_etree_generate   | 79.1 ms                                                                   | 94.1 ms: 1.19x slower                                        |
| unpickle_pure_python | 238 us                                                                    | 318 us: 1.34x slower                                         |
| xml_etree_process    | 55.8 ms                                                                   | 77.6 ms: 1.39x slower                                        |
| pickle_pure_python   | 319 us                                                                    | 451 us: 1.41x slower                                         |
| Geometric mean       | (ref)                                                                     | 1.11x slower                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 7.73 ms                                                                   | 7.32 ms: 1.05x faster                                        |
| python_startup         | 10.7 ms                                                                   | 11.5 ms: 1.07x slower                                        |
| Geometric mean         | (ref)                                                                     | 1.01x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 57.8 ms                                                                   | 63.5 ms: 1.10x slower                                        |
| genshi_text     | 26.3 ms                                                                   | 31.7 ms: 1.21x slower                                        |
| django_template | 39.6 ms                                                                   | 52.0 ms: 1.31x slower                                        |
| mako            | 10.9 ms                                                                   | 14.7 ms: 1.35x slower                                        |
| Geometric mean  | (ref)                                                                     | 1.24x slower                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| gc_traversal            | 4.22 ms                                                                   | 3.46 ms: 1.22x faster                                        |
| coverage                | 86.0 ms                                                                   | 71.1 ms: 1.21x faster                                        |
| regex_effbot            | 3.31 ms                                                                   | 2.99 ms: 1.11x faster                                        |
| python_startup_no_site  | 7.73 ms                                                                   | 7.32 ms: 1.05x faster                                        |
| pickle_dict             | 31.1 us                                                                   | 29.5 us: 1.05x faster                                        |
| unpickle                | 13.0 us                                                                   | 13.3 us: 1.02x slower                                        |
| generators              | 56.0 ms                                                                   | 57.0 ms: 1.02x slower                                        |
| pickle                  | 9.92 us                                                                   | 10.1 us: 1.02x slower                                        |
| xml_etree_iterparse     | 106 ms                                                                    | 109 ms: 1.03x slower                                         |
| coroutines              | 29.5 ms                                                                   | 30.6 ms: 1.04x slower                                        |
| unpickle_list           | 4.52 us                                                                   | 4.73 us: 1.05x slower                                        |
| asyncio_tcp             | 752 ms                                                                    | 787 ms: 1.05x slower                                         |
| sympy_sum               | 182 ms                                                                    | 193 ms: 1.06x slower                                         |
| json                    | 5.59 ms                                                                   | 5.94 ms: 1.06x slower                                        |
| regex_v8                | 24.4 ms                                                                   | 26.0 ms: 1.06x slower                                        |
| telco                   | 6.70 ms                                                                   | 7.14 ms: 1.07x slower                                        |
| json_loads              | 28.4 us                                                                   | 30.3 us: 1.07x slower                                        |
| json_dumps              | 13.4 ms                                                                   | 14.3 ms: 1.07x slower                                        |
| python_startup          | 10.7 ms                                                                   | 11.5 ms: 1.07x slower                                        |
| sympy_str               | 333 ms                                                                    | 358 ms: 1.08x slower                                         |
| pidigits                | 252 ms                                                                    | 271 ms: 1.08x slower                                         |
| mdp                     | 2.73 sec                                                                  | 2.95 sec: 1.08x slower                                       |
| pylint                  | 517 ms                                                                    | 562 ms: 1.09x slower                                         |
| pickle_list             | 3.78 us                                                                   | 4.11 us: 1.09x slower                                        |
| meteor_contest          | 129 ms                                                                    | 142 ms: 1.10x slower                                         |
| create_gc_cycles        | 1.65 ms                                                                   | 1.80 ms: 1.10x slower                                        |
| genshi_xml              | 57.8 ms                                                                   | 63.5 ms: 1.10x slower                                        |
| comprehensions          | 24.7 us                                                                   | 27.3 us: 1.10x slower                                        |
| sympy_expand            | 547 ms                                                                    | 603 ms: 1.10x slower                                         |
| fannkuch                | 449 ms                                                                    | 496 ms: 1.10x slower                                         |
| pathlib                 | 19.2 ms                                                                   | 21.3 ms: 1.11x slower                                        |
| sympy_integrate         | 25.3 ms                                                                   | 28.1 ms: 1.11x slower                                        |
| nqueens                 | 101 ms                                                                    | 114 ms: 1.13x slower                                         |
| dask                    | 418 ms                                                                    | 478 ms: 1.14x slower                                         |
| flaskblogging           | 3.81 ms                                                                   | 4.37 ms: 1.15x slower                                        |
| bench_thread_pool       | 990 us                                                                    | 1.14 ms: 1.15x slower                                        |
| sqlalchemy_imperative   | 19.8 ms                                                                   | 22.9 ms: 1.15x slower                                        |
| deepcopy_reduce         | 3.39 us                                                                   | 3.91 us: 1.15x slower                                        |
| regex_dna               | 225 ms                                                                    | 261 ms: 1.16x slower                                         |
| dulwich_log             | 69.1 ms                                                                   | 80.5 ms: 1.16x slower                                        |
| xml_etree_generate      | 79.1 ms                                                                   | 94.1 ms: 1.19x slower                                        |
| sqlite_synth            | 2.49 us                                                                   | 2.96 us: 1.19x slower                                        |
| deepcopy                | 384 us                                                                    | 457 us: 1.19x slower                                         |
| docutils                | 2.86 sec                                                                  | 3.41 sec: 1.19x slower                                       |
| sqlglot_optimize        | 58.6 ms                                                                   | 70.1 ms: 1.20x slower                                        |
| genshi_text             | 26.3 ms                                                                   | 31.7 ms: 1.21x slower                                        |
| tornado_http            | 125 ms                                                                    | 151 ms: 1.21x slower                                         |
| sqlglot_normalize       | 122 ms                                                                    | 147 ms: 1.21x slower                                         |
| sqlalchemy_declarative  | 156 ms                                                                    | 188 ms: 1.21x slower                                         |
| 2to3                    | 289 ms                                                                    | 352 ms: 1.22x slower                                         |
| gunicorn                | 936 us                                                                    | 1.15 ms: 1.22x slower                                        |
| aiohttp                 | 959 us                                                                    | 1.18 ms: 1.23x slower                                        |
| regex_compile           | 154 ms                                                                    | 191 ms: 1.24x slower                                         |
| scimark_sparse_mat_mult | 4.06 ms                                                                   | 5.09 ms: 1.26x slower                                        |
| async_tree_cpu_io_mixed | 754 ms                                                                    | 951 ms: 1.26x slower                                         |
| logging_format          | 7.84 us                                                                   | 9.94 us: 1.27x slower                                        |
| pycparser               | 1.30 sec                                                                  | 1.66 sec: 1.27x slower                                       |
| chameleon               | 7.50 ms                                                                   | 9.62 ms: 1.28x slower                                        |
| async_tree_memoization  | 639 ms                                                                    | 822 ms: 1.29x slower                                         |
| scimark_fft             | 276 ms                                                                    | 359 ms: 1.30x slower                                         |
| thrift                  | 942 us                                                                    | 1.23 ms: 1.30x slower                                        |
| unpack_sequence         | 45.9 ns                                                                   | 59.7 ns: 1.30x slower                                        |
| django_template         | 39.6 ms                                                                   | 52.0 ms: 1.31x slower                                        |
| async_generators        | 318 ms                                                                    | 419 ms: 1.31x slower                                         |
| async_tree_none         | 529 ms                                                                    | 698 ms: 1.32x slower                                         |
| pprint_pformat          | 1.60 sec                                                                  | 2.12 sec: 1.33x slower                                       |
| logging_simple          | 6.95 us                                                                   | 9.24 us: 1.33x slower                                        |
| deepcopy_memo           | 37.0 us                                                                   | 49.2 us: 1.33x slower                                        |
| unpickle_pure_python    | 238 us                                                                    | 318 us: 1.34x slower                                         |
| pprint_safe_repr        | 768 ms                                                                    | 1.03 sec: 1.34x slower                                       |
| mako                    | 10.9 ms                                                                   | 14.7 ms: 1.35x slower                                        |
| hexiom                  | 7.00 ms                                                                   | 9.54 ms: 1.36x slower                                        |
| async_tree_io           | 1.18 sec                                                                  | 1.61 sec: 1.36x slower                                       |
| html5lib                | 70.2 ms                                                                   | 96.3 ms: 1.37x slower                                        |
| xml_etree_process       | 55.8 ms                                                                   | 77.6 ms: 1.39x slower                                        |
| crypto_pyaes            | 85.0 ms                                                                   | 119 ms: 1.40x slower                                         |
| pickle_pure_python      | 319 us                                                                    | 451 us: 1.41x slower                                         |
| chaos                   | 76.2 ms                                                                   | 108 ms: 1.41x slower                                         |
| sqlglot_transpile       | 1.88 ms                                                                   | 2.69 ms: 1.43x slower                                        |
| nbody                   | 92.1 ms                                                                   | 132 ms: 1.44x slower                                         |
| scimark_lu              | 114 ms                                                                    | 164 ms: 1.44x slower                                         |
| float                   | 75.7 ms                                                                   | 109 ms: 1.45x slower                                         |
| spectral_norm           | 95.1 ms                                                                   | 138 ms: 1.45x slower                                         |
| sqlglot_parse           | 1.53 ms                                                                   | 2.24 ms: 1.47x slower                                        |
| richards                | 49.1 ms                                                                   | 73.9 ms: 1.50x slower                                        |
| bench_mp_pool           | 4.54 ms                                                                   | 7.10 ms: 1.56x slower                                        |
| scimark_monte_carlo     | 67.8 ms                                                                   | 109 ms: 1.60x slower                                         |
| logging_silent          | 103 ns                                                                    | 165 ns: 1.60x slower                                         |
| raytrace                | 303 ms                                                                    | 491 ms: 1.62x slower                                         |
| scimark_sor             | 109 ms                                                                    | 177 ms: 1.62x slower                                         |
| go                      | 158 ms                                                                    | 264 ms: 1.67x slower                                         |
| pyflate                 | 438 ms                                                                    | 731 ms: 1.67x slower                                         |
| deltablue               | 3.99 ms                                                                   | 7.54 ms: 1.89x slower                                        |
| Geometric mean          | (ref)                                                                     | 1.22x slower                                                 |

Benchmark hidden because not significant (2): xml_etree_parse, mypy2
