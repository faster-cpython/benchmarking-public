
# Results vs. 3.10.4

- fork: python
- ref: ef7c2bfcf1fd618438f9
- machine: linux-x86_64
- commit hash: ef7c2bf
- commit date: 2023-02-05
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 281 ms: 1.25x faster                                                         |
| chameleon      | 9.62 ms                                                      | 7.63 ms: 1.26x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.75 sec: 1.24x faster                                                       |
| html5lib       | 96.3 ms                                                      | 66.2 ms: 1.45x faster                                                        |
| tornado_http   | 151 ms                                                       | 120 ms: 1.26x faster                                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 71.5 ms: 1.53x faster                                                        |
| nbody          | 132 ms                                                       | 89.9 ms: 1.47x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 145 ms: 1.31x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 22.1 ms: 1.18x faster                                                        |
| regex_dna      | 261 ms                                                       | 222 ms: 1.18x faster                                                         |
| regex_effbot   | 2.99 ms                                                      | 3.31 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 208 us: 1.53x faster                                                         |
| pickle_pure_python   | 451 us                                                       | 307 us: 1.47x faster                                                         |
| json_dumps           | 14.3 ms                                                      | 10.0 ms: 1.42x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 55.7 ms: 1.39x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.1 us: 1.26x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 81.1 ms: 1.16x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| unpickle_list        | 4.73 us                                                      | 4.36 us: 1.08x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.95 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 109 ms                                                       | 106 ms: 1.03x faster                                                         |
| unpickle             | 13.3 us                                                      | 13.5 us: 1.02x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 32.6 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.26 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.45x faster                                                        |
| django_template | 52.0 ms                                                      | 38.3 ms: 1.36x faster                                                        |
| genshi_text     | 31.7 ms                                                      | 24.9 ms: 1.27x faster                                                        |
| genshi_xml      | 63.5 ms                                                      | 54.1 ms: 1.17x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.49 ms: 2.16x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 387 ms: 2.04x faster                                                         |
| logging_silent          | 165 ns                                                       | 95.9 ns: 1.72x faster                                                        |
| go                      | 264 ms                                                       | 155 ms: 1.71x faster                                                         |
| pyflate                 | 731 ms                                                       | 431 ms: 1.70x faster                                                         |
| raytrace                | 491 ms                                                       | 291 ms: 1.69x faster                                                         |
| scimark_sor             | 177 ms                                                       | 107 ms: 1.65x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                       | 66.9 ms: 1.62x faster                                                        |
| scimark_lu              | 164 ms                                                       | 102 ms: 1.61x faster                                                         |
| chaos                   | 108 ms                                                       | 67.4 ms: 1.60x faster                                                        |
| richards                | 73.9 ms                                                      | 46.5 ms: 1.59x faster                                                        |
| float                   | 109 ms                                                       | 71.5 ms: 1.53x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 208 us: 1.53x faster                                                         |
| hexiom                  | 9.54 ms                                                      | 6.43 ms: 1.48x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 80.0 ms: 1.48x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.80 ms: 1.48x faster                                                        |
| nbody                   | 132 ms                                                       | 89.9 ms: 1.47x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 307 us: 1.47x faster                                                         |
| html5lib                | 96.3 ms                                                      | 66.2 ms: 1.45x faster                                                        |
| spectral_norm           | 138 ms                                                       | 95.3 ms: 1.45x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.45x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 10.0 ms: 1.42x faster                                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.58 ms: 1.42x faster                                                        |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.59 ms: 1.42x faster                                                        |
| xml_etree_process       | 77.6 ms                                                      | 55.7 ms: 1.39x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 43.2 ns: 1.38x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.95 ms: 1.38x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                                       |
| async_tree_none         | 698 ms                                                       | 508 ms: 1.37x faster                                                         |
| thrift                  | 1.23 ms                                                      | 892 us: 1.37x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.21 sec: 1.36x faster                                                       |
| django_template         | 52.0 ms                                                      | 38.3 ms: 1.36x faster                                                        |
| async_tree_memoization  | 822 ms                                                       | 608 ms: 1.35x faster                                                         |
| pprint_pformat          | 2.12 sec                                                     | 1.58 sec: 1.35x faster                                                       |
| pprint_safe_repr        | 1.03 sec                                                     | 767 ms: 1.34x faster                                                         |
| deepcopy_memo           | 49.2 us                                                      | 36.8 us: 1.34x faster                                                        |
| logging_simple          | 9.24 us                                                      | 6.93 us: 1.33x faster                                                        |
| scimark_fft             | 359 ms                                                       | 271 ms: 1.32x faster                                                         |
| regex_compile           | 191 ms                                                       | 145 ms: 1.31x faster                                                         |
| async_generators        | 419 ms                                                       | 322 ms: 1.30x faster                                                         |
| logging_format          | 9.94 us                                                      | 7.64 us: 1.30x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 739 ms: 1.29x faster                                                         |
| genshi_text             | 31.7 ms                                                      | 24.9 ms: 1.27x faster                                                        |
| comprehensions          | 27.3 us                                                      | 21.5 us: 1.27x faster                                                        |
| chameleon               | 9.62 ms                                                      | 7.63 ms: 1.26x faster                                                        |
| json_loads              | 30.3 us                                                      | 24.1 us: 1.26x faster                                                        |
| tornado_http            | 151 ms                                                       | 120 ms: 1.26x faster                                                         |
| 2to3                    | 352 ms                                                       | 281 ms: 1.25x faster                                                         |
| mypy2                   | 466 ms                                                       | 374 ms: 1.25x faster                                                         |
| docutils                | 3.41 sec                                                     | 2.75 sec: 1.24x faster                                                       |
| sqlglot_normalize       | 147 ms                                                       | 119 ms: 1.23x faster                                                         |
| fannkuch                | 496 ms                                                       | 404 ms: 1.23x faster                                                         |
| dulwich_log             | 80.5 ms                                                      | 65.6 ms: 1.23x faster                                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 57.8 ms: 1.21x faster                                                        |
| deepcopy                | 457 us                                                       | 380 us: 1.20x faster                                                         |
| deepcopy_reduce         | 3.91 us                                                      | 3.28 us: 1.19x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 959 us: 1.19x faster                                                         |
| regex_v8                | 26.0 ms                                                      | 22.1 ms: 1.18x faster                                                        |
| regex_dna               | 261 ms                                                       | 222 ms: 1.18x faster                                                         |
| genshi_xml              | 63.5 ms                                                      | 54.1 ms: 1.17x faster                                                        |
| json                    | 5.94 ms                                                      | 5.07 ms: 1.17x faster                                                        |
| xml_etree_generate      | 94.1 ms                                                      | 81.1 ms: 1.16x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.56 us: 1.16x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 24.3 ms: 1.16x faster                                                        |
| sympy_str               | 358 ms                                                       | 311 ms: 1.15x faster                                                         |
| sympy_expand            | 603 ms                                                       | 528 ms: 1.14x faster                                                         |
| nqueens                 | 114 ms                                                       | 100 ms: 1.14x faster                                                         |
| pathlib                 | 21.3 ms                                                      | 18.9 ms: 1.13x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.60 ms: 1.13x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| sympy_sum               | 193 ms                                                       | 172 ms: 1.12x faster                                                         |
| meteor_contest          | 142 ms                                                       | 128 ms: 1.11x faster                                                         |
| unpickle_list           | 4.73 us                                                      | 4.36 us: 1.08x faster                                                        |
| mdp                     | 2.95 sec                                                     | 2.72 sec: 1.08x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.61 ms: 1.08x faster                                                        |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| coroutines              | 30.6 ms                                                      | 29.2 ms: 1.05x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.95 us: 1.04x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 106 ms: 1.03x faster                                                         |
| python_startup          | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                        |
| unpickle                | 13.3 us                                                      | 13.5 us: 1.02x slower                                                        |
| generators              | 57.0 ms                                                      | 60.8 ms: 1.07x slower                                                        |
| gc_traversal            | 3.46 ms                                                      | 3.76 ms: 1.09x slower                                                        |
| pickle_dict             | 29.5 us                                                      | 32.6 us: 1.10x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.31 ms: 1.11x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.26 ms: 1.13x slower                                                        |
| coverage                | 71.1 ms                                                      | 82.2 ms: 1.16x slower                                                        |
| dask                    | 478 ms                                                       | 568 ms: 1.19x slower                                                         |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                                 |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
