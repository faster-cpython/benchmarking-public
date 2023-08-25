
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 06249ec
- commit date: 2023-04-01
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 288 ms: 1.21x faster                                         |
| chameleon      | 9.72 ms                                                      | 7.16 ms: 1.36x faster                                        |
| docutils       | 3.40 sec                                                     | 2.82 sec: 1.21x faster                                       |
| html5lib       | 94.6 ms                                                      | 70.9 ms: 1.33x faster                                        |
| tornado_http   | 152 ms                                                       | 113 ms: 1.34x faster                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 86.8 ms: 1.58x faster                                        |
| float          | 110 ms                                                       | 73.7 ms: 1.50x faster                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.35x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 150 ms: 1.29x faster                                         |
| regex_v8       | 26.6 ms                                                      | 23.4 ms: 1.14x faster                                        |
| regex_dna      | 259 ms                                                       | 231 ms: 1.12x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.38 ms: 1.13x slower                                        |
| Geometric mean | (ref)                                                        | 1.10x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 215 us: 1.49x faster                                         |
| pickle_pure_python   | 457 us                                                       | 319 us: 1.43x faster                                         |
| json_dumps           | 14.2 ms                                                      | 10.4 ms: 1.36x faster                                        |
| xml_etree_process    | 76.0 ms                                                      | 60.0 ms: 1.27x faster                                        |
| json_loads           | 30.0 us                                                      | 23.9 us: 1.25x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 143 ms: 1.13x faster                                         |
| xml_etree_generate   | 94.6 ms                                                      | 86.2 ms: 1.10x faster                                        |
| unpickle             | 14.2 us                                                      | 13.0 us: 1.09x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                         |
| pickle_list          | 4.11 us                                                      | 3.90 us: 1.05x faster                                        |
| pickle               | 9.94 us                                                      | 10.3 us: 1.03x slower                                        |
| pickle_dict          | 30.0 us                                                      | 31.5 us: 1.05x slower                                        |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.31 ms: 1.14x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                        |
| django_template | 51.5 ms                                                      | 39.9 ms: 1.29x faster                                        |
| genshi_text     | 31.5 ms                                                      | 26.4 ms: 1.19x faster                                        |
| genshi_xml      | 64.7 ms                                                      | 56.5 ms: 1.15x faster                                        |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.63 ms: 2.06x faster                                        |
| asyncio_tcp             | 782 ms                                                       | 385 ms: 2.03x faster                                         |
| logging_silent          | 166 ns                                                       | 94.8 ns: 1.75x faster                                        |
| raytrace                | 488 ms                                                       | 296 ms: 1.65x faster                                         |
| scimark_lu              | 164 ms                                                       | 101 ms: 1.63x faster                                         |
| scimark_monte_carlo     | 109 ms                                                       | 67.5 ms: 1.62x faster                                        |
| nbody                   | 137 ms                                                       | 86.8 ms: 1.58x faster                                        |
| scimark_sor             | 177 ms                                                       | 114 ms: 1.55x faster                                         |
| bench_mp_pool           | 7.18 ms                                                      | 4.65 ms: 1.54x faster                                        |
| pyflate                 | 697 ms                                                       | 459 ms: 1.52x faster                                         |
| richards                | 74.1 ms                                                      | 49.1 ms: 1.51x faster                                        |
| chaos                   | 107 ms                                                       | 71.4 ms: 1.50x faster                                        |
| go                      | 259 ms                                                       | 173 ms: 1.50x faster                                         |
| generators              | 58.0 ms                                                      | 38.7 ms: 1.50x faster                                        |
| float                   | 110 ms                                                       | 73.7 ms: 1.50x faster                                        |
| unpickle_pure_python    | 321 us                                                       | 215 us: 1.49x faster                                         |
| mako                    | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                        |
| spectral_norm           | 136 ms                                                       | 94.1 ms: 1.45x faster                                        |
| pickle_pure_python      | 457 us                                                       | 319 us: 1.43x faster                                         |
| crypto_pyaes            | 118 ms                                                       | 83.5 ms: 1.42x faster                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.60 ms: 1.41x faster                                        |
| hexiom                  | 9.52 ms                                                      | 6.77 ms: 1.41x faster                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.96 ms: 1.38x faster                                        |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.78 ms: 1.37x faster                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                       |
| json_dumps              | 14.2 ms                                                      | 10.4 ms: 1.36x faster                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 771 ms: 1.36x faster                                         |
| scimark_fft             | 359 ms                                                       | 264 ms: 1.36x faster                                         |
| chameleon               | 9.72 ms                                                      | 7.16 ms: 1.36x faster                                        |
| async_tree_none         | 700 ms                                                       | 516 ms: 1.36x faster                                         |
| unpack_sequence         | 59.5 ns                                                      | 44.0 ns: 1.35x faster                                        |
| deepcopy_memo           | 48.9 us                                                      | 36.2 us: 1.35x faster                                        |
| tornado_http            | 152 ms                                                       | 113 ms: 1.34x faster                                         |
| async_tree_memoization  | 824 ms                                                       | 614 ms: 1.34x faster                                         |
| html5lib                | 94.6 ms                                                      | 70.9 ms: 1.33x faster                                        |
| pycparser               | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                       |
| regex_compile           | 194 ms                                                       | 150 ms: 1.29x faster                                         |
| django_template         | 51.5 ms                                                      | 39.9 ms: 1.29x faster                                        |
| xml_etree_process       | 76.0 ms                                                      | 60.0 ms: 1.27x faster                                        |
| logging_simple          | 8.90 us                                                      | 7.03 us: 1.27x faster                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 756 ms: 1.26x faster                                         |
| json_loads              | 30.0 us                                                      | 23.9 us: 1.25x faster                                        |
| thrift                  | 1.16 ms                                                      | 942 us: 1.24x faster                                         |
| 2to3                    | 350 ms                                                       | 288 ms: 1.21x faster                                         |
| mypy2                   | 466 ms                                                       | 386 ms: 1.21x faster                                         |
| docutils                | 3.40 sec                                                     | 2.82 sec: 1.21x faster                                       |
| dulwich_log             | 80.1 ms                                                      | 66.4 ms: 1.21x faster                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 58.8 ms: 1.20x faster                                        |
| genshi_text             | 31.5 ms                                                      | 26.4 ms: 1.19x faster                                        |
| sqlglot_normalize       | 144 ms                                                       | 121 ms: 1.19x faster                                         |
| logging_format          | 9.57 us                                                      | 8.05 us: 1.19x faster                                        |
| mdp                     | 3.03 sec                                                     | 2.57 sec: 1.18x faster                                       |
| json                    | 5.96 ms                                                      | 5.05 ms: 1.18x faster                                        |
| coroutines              | 30.4 ms                                                      | 26.2 ms: 1.16x faster                                        |
| deepcopy_reduce         | 4.03 us                                                      | 3.50 us: 1.15x faster                                        |
| bench_thread_pool       | 1.14 ms                                                      | 987 us: 1.15x faster                                         |
| genshi_xml              | 64.7 ms                                                      | 56.5 ms: 1.15x faster                                        |
| regex_v8                | 26.6 ms                                                      | 23.4 ms: 1.14x faster                                        |
| deepcopy                | 454 us                                                       | 398 us: 1.14x faster                                         |
| sqlite_synth            | 2.97 us                                                      | 2.62 us: 1.13x faster                                        |
| xml_etree_parse         | 162 ms                                                       | 143 ms: 1.13x faster                                         |
| regex_dna               | 259 ms                                                       | 231 ms: 1.12x faster                                         |
| fannkuch                | 496 ms                                                       | 445 ms: 1.11x faster                                         |
| sympy_expand            | 599 ms                                                       | 541 ms: 1.11x faster                                         |
| pathlib                 | 21.7 ms                                                      | 19.7 ms: 1.10x faster                                        |
| xml_etree_generate      | 94.6 ms                                                      | 86.2 ms: 1.10x faster                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.6 ms: 1.10x faster                                        |
| unpickle                | 14.2 us                                                      | 13.0 us: 1.09x faster                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.68 ms: 1.08x faster                                        |
| async_generators        | 422 ms                                                       | 391 ms: 1.08x faster                                         |
| xml_etree_iterparse     | 110 ms                                                       | 103 ms: 1.07x faster                                         |
| sympy_str               | 358 ms                                                       | 334 ms: 1.07x faster                                         |
| meteor_contest          | 137 ms                                                       | 128 ms: 1.07x faster                                         |
| nqueens                 | 112 ms                                                       | 106 ms: 1.06x faster                                         |
| pickle_list             | 4.11 us                                                      | 3.90 us: 1.05x faster                                        |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| python_startup          | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                        |
| telco                   | 7.14 ms                                                      | 6.93 ms: 1.03x faster                                        |
| sympy_sum               | 193 ms                                                       | 188 ms: 1.03x faster                                         |
| comprehensions          | 26.9 us                                                      | 27.7 us: 1.03x slower                                        |
| pickle                  | 9.94 us                                                      | 10.3 us: 1.03x slower                                        |
| pickle_dict             | 30.0 us                                                      | 31.5 us: 1.05x slower                                        |
| regex_effbot            | 2.99 ms                                                      | 3.38 ms: 1.13x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.31 ms: 1.14x slower                                        |
| gc_traversal            | 3.45 ms                                                      | 4.04 ms: 1.17x slower                                        |
| dask                    | 463 ms                                                       | 577 ms: 1.25x slower                                         |
| coverage                | 64.0 ms                                                      | 84.4 ms: 1.32x slower                                        |
| Geometric mean          | (ref)                                                        | 1.24x faster                                                 |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x
