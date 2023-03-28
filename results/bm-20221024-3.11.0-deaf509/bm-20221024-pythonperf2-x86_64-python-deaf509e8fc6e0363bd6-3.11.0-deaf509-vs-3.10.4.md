
# Results vs. 3.10.4

- fork: python
- ref: deaf509e8fc6e0363bd6
- machine: linux-x86_64
- commit hash: deaf509
- commit date: 2022-10-24
- overall geometric mean: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 289 ms: 1.22x faster                                                      |
| chameleon      | 9.62 ms                                                      | 7.50 ms: 1.28x faster                                                     |
| docutils       | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                    |
| html5lib       | 96.3 ms                                                      | 70.2 ms: 1.37x faster                                                     |
| tornado_http   | 151 ms                                                       | 125 ms: 1.21x faster                                                      |
| Geometric mean | (ref)                                                        | 1.25x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 75.7 ms: 1.45x faster                                                     |
| nbody          | 132 ms                                                       | 92.1 ms: 1.44x faster                                                     |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                        | 1.31x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 154 ms: 1.24x faster                                                      |
| regex_dna      | 261 ms                                                       | 225 ms: 1.16x faster                                                      |
| regex_v8       | 26.0 ms                                                      | 24.4 ms: 1.06x faster                                                     |
| regex_effbot   | 2.99 ms                                                      | 3.31 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                        | 1.08x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 451 us                                                       | 319 us: 1.41x faster                                                      |
| xml_etree_process    | 77.6 ms                                                      | 55.8 ms: 1.39x faster                                                     |
| unpickle_pure_python | 318 us                                                       | 238 us: 1.34x faster                                                      |
| xml_etree_generate   | 94.1 ms                                                      | 79.1 ms: 1.19x faster                                                     |
| pickle_list          | 4.11 us                                                      | 3.78 us: 1.09x faster                                                     |
| json_dumps           | 14.3 ms                                                      | 13.4 ms: 1.07x faster                                                     |
| json_loads           | 30.3 us                                                      | 28.4 us: 1.07x faster                                                     |
| unpickle_list        | 4.73 us                                                      | 4.52 us: 1.05x faster                                                     |
| xml_etree_iterparse  | 109 ms                                                       | 106 ms: 1.03x faster                                                      |
| pickle               | 10.1 us                                                      | 9.92 us: 1.02x faster                                                     |
| unpickle             | 13.3 us                                                      | 13.0 us: 1.02x faster                                                     |
| pickle_dict          | 29.5 us                                                      | 31.1 us: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.7 ms: 1.07x faster                                                     |
| python_startup_no_site | 7.32 ms                                                      | 7.73 ms: 1.05x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                     |
| django_template | 52.0 ms                                                      | 39.6 ms: 1.31x faster                                                     |
| genshi_text     | 31.7 ms                                                      | 26.3 ms: 1.21x faster                                                     |
| genshi_xml      | 63.5 ms                                                      | 57.8 ms: 1.10x faster                                                     |
| Geometric mean  | (ref)                                                        | 1.24x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.99 ms: 1.89x faster                                                     |
| pyflate                 | 731 ms                                                       | 438 ms: 1.67x faster                                                      |
| go                      | 264 ms                                                       | 158 ms: 1.67x faster                                                      |
| scimark_sor             | 177 ms                                                       | 109 ms: 1.62x faster                                                      |
| raytrace                | 491 ms                                                       | 303 ms: 1.62x faster                                                      |
| logging_silent          | 165 ns                                                       | 103 ns: 1.60x faster                                                      |
| scimark_monte_carlo     | 109 ms                                                       | 67.8 ms: 1.60x faster                                                     |
| bench_mp_pool           | 7.10 ms                                                      | 4.54 ms: 1.56x faster                                                     |
| richards                | 73.9 ms                                                      | 49.1 ms: 1.50x faster                                                     |
| sqlglot_parse           | 2.24 ms                                                      | 1.53 ms: 1.47x faster                                                     |
| spectral_norm           | 138 ms                                                       | 95.1 ms: 1.45x faster                                                     |
| float                   | 109 ms                                                       | 75.7 ms: 1.45x faster                                                     |
| scimark_lu              | 164 ms                                                       | 114 ms: 1.44x faster                                                      |
| nbody                   | 132 ms                                                       | 92.1 ms: 1.44x faster                                                     |
| sqlglot_transpile       | 2.69 ms                                                      | 1.88 ms: 1.43x faster                                                     |
| chaos                   | 108 ms                                                       | 76.2 ms: 1.41x faster                                                     |
| pickle_pure_python      | 451 us                                                       | 319 us: 1.41x faster                                                      |
| crypto_pyaes            | 119 ms                                                       | 85.0 ms: 1.40x faster                                                     |
| xml_etree_process       | 77.6 ms                                                      | 55.8 ms: 1.39x faster                                                     |
| html5lib                | 96.3 ms                                                      | 70.2 ms: 1.37x faster                                                     |
| async_tree_io           | 1.61 sec                                                     | 1.18 sec: 1.36x faster                                                    |
| hexiom                  | 9.54 ms                                                      | 7.00 ms: 1.36x faster                                                     |
| mako                    | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                     |
| pprint_safe_repr        | 1.03 sec                                                     | 768 ms: 1.34x faster                                                      |
| unpickle_pure_python    | 318 us                                                       | 238 us: 1.34x faster                                                      |
| deepcopy_memo           | 49.2 us                                                      | 37.0 us: 1.33x faster                                                     |
| logging_simple          | 9.24 us                                                      | 6.95 us: 1.33x faster                                                     |
| pprint_pformat          | 2.12 sec                                                     | 1.60 sec: 1.33x faster                                                    |
| async_tree_none         | 698 ms                                                       | 529 ms: 1.32x faster                                                      |
| async_generators        | 419 ms                                                       | 318 ms: 1.31x faster                                                      |
| django_template         | 52.0 ms                                                      | 39.6 ms: 1.31x faster                                                     |
| unpack_sequence         | 59.7 ns                                                      | 45.9 ns: 1.30x faster                                                     |
| thrift                  | 1.23 ms                                                      | 942 us: 1.30x faster                                                      |
| scimark_fft             | 359 ms                                                       | 276 ms: 1.30x faster                                                      |
| async_tree_memoization  | 822 ms                                                       | 639 ms: 1.29x faster                                                      |
| chameleon               | 9.62 ms                                                      | 7.50 ms: 1.28x faster                                                     |
| pycparser               | 1.66 sec                                                     | 1.30 sec: 1.27x faster                                                    |
| logging_format          | 9.94 us                                                      | 7.84 us: 1.27x faster                                                     |
| async_tree_cpu_io_mixed | 951 ms                                                       | 754 ms: 1.26x faster                                                      |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.06 ms: 1.26x faster                                                     |
| regex_compile           | 191 ms                                                       | 154 ms: 1.24x faster                                                      |
| aiohttp                 | 1.18 ms                                                      | 959 us: 1.23x faster                                                      |
| gunicorn                | 1.15 ms                                                      | 936 us: 1.22x faster                                                      |
| 2to3                    | 352 ms                                                       | 289 ms: 1.22x faster                                                      |
| sqlalchemy_declarative  | 188 ms                                                       | 156 ms: 1.21x faster                                                      |
| sqlglot_normalize       | 147 ms                                                       | 122 ms: 1.21x faster                                                      |
| tornado_http            | 151 ms                                                       | 125 ms: 1.21x faster                                                      |
| genshi_text             | 31.7 ms                                                      | 26.3 ms: 1.21x faster                                                     |
| sqlglot_optimize        | 70.1 ms                                                      | 58.6 ms: 1.20x faster                                                     |
| docutils                | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                    |
| deepcopy                | 457 us                                                       | 384 us: 1.19x faster                                                      |
| sqlite_synth            | 2.96 us                                                      | 2.49 us: 1.19x faster                                                     |
| xml_etree_generate      | 94.1 ms                                                      | 79.1 ms: 1.19x faster                                                     |
| dulwich_log             | 80.5 ms                                                      | 69.1 ms: 1.16x faster                                                     |
| regex_dna               | 261 ms                                                       | 225 ms: 1.16x faster                                                      |
| deepcopy_reduce         | 3.91 us                                                      | 3.39 us: 1.15x faster                                                     |
| sqlalchemy_imperative   | 22.9 ms                                                      | 19.8 ms: 1.15x faster                                                     |
| bench_thread_pool       | 1.14 ms                                                      | 990 us: 1.15x faster                                                      |
| flaskblogging           | 4.37 ms                                                      | 3.81 ms: 1.15x faster                                                     |
| dask                    | 478 ms                                                       | 418 ms: 1.14x faster                                                      |
| nqueens                 | 114 ms                                                       | 101 ms: 1.13x faster                                                      |
| sympy_integrate         | 28.1 ms                                                      | 25.3 ms: 1.11x faster                                                     |
| pathlib                 | 21.3 ms                                                      | 19.2 ms: 1.11x faster                                                     |
| fannkuch                | 496 ms                                                       | 449 ms: 1.10x faster                                                      |
| sympy_expand            | 603 ms                                                       | 547 ms: 1.10x faster                                                      |
| comprehensions          | 27.3 us                                                      | 24.7 us: 1.10x faster                                                     |
| genshi_xml              | 63.5 ms                                                      | 57.8 ms: 1.10x faster                                                     |
| create_gc_cycles        | 1.80 ms                                                      | 1.65 ms: 1.10x faster                                                     |
| meteor_contest          | 142 ms                                                       | 129 ms: 1.10x faster                                                      |
| pickle_list             | 4.11 us                                                      | 3.78 us: 1.09x faster                                                     |
| pylint                  | 562 ms                                                       | 517 ms: 1.09x faster                                                      |
| mdp                     | 2.95 sec                                                     | 2.73 sec: 1.08x faster                                                    |
| pidigits                | 271 ms                                                       | 252 ms: 1.08x faster                                                      |
| sympy_str               | 358 ms                                                       | 333 ms: 1.08x faster                                                      |
| python_startup          | 11.5 ms                                                      | 10.7 ms: 1.07x faster                                                     |
| json_dumps              | 14.3 ms                                                      | 13.4 ms: 1.07x faster                                                     |
| json_loads              | 30.3 us                                                      | 28.4 us: 1.07x faster                                                     |
| telco                   | 7.14 ms                                                      | 6.70 ms: 1.07x faster                                                     |
| regex_v8                | 26.0 ms                                                      | 24.4 ms: 1.06x faster                                                     |
| json                    | 5.94 ms                                                      | 5.59 ms: 1.06x faster                                                     |
| sympy_sum               | 193 ms                                                       | 182 ms: 1.06x faster                                                      |
| asyncio_tcp             | 787 ms                                                       | 752 ms: 1.05x faster                                                      |
| unpickle_list           | 4.73 us                                                      | 4.52 us: 1.05x faster                                                     |
| coroutines              | 30.6 ms                                                      | 29.5 ms: 1.04x faster                                                     |
| xml_etree_iterparse     | 109 ms                                                       | 106 ms: 1.03x faster                                                      |
| pickle                  | 10.1 us                                                      | 9.92 us: 1.02x faster                                                     |
| generators              | 57.0 ms                                                      | 56.0 ms: 1.02x faster                                                     |
| unpickle                | 13.3 us                                                      | 13.0 us: 1.02x faster                                                     |
| pickle_dict             | 29.5 us                                                      | 31.1 us: 1.05x slower                                                     |
| python_startup_no_site  | 7.32 ms                                                      | 7.73 ms: 1.05x slower                                                     |
| regex_effbot            | 2.99 ms                                                      | 3.31 ms: 1.11x slower                                                     |
| coverage                | 71.1 ms                                                      | 86.0 ms: 1.21x slower                                                     |
| gc_traversal            | 3.46 ms                                                      | 4.22 ms: 1.22x slower                                                     |
| Geometric mean          | (ref)                                                        | 1.22x faster                                                              |

Benchmark hidden because not significant (2): mypy2, xml_etree_parse
