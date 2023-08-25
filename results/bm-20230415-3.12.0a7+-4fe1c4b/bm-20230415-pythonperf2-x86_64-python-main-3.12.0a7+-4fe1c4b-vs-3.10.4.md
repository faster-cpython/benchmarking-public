
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 4fe1c4b
- commit date: 2023-04-15
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                         |
| chameleon      | 9.72 ms                                                      | 7.49 ms: 1.30x faster                                        |
| docutils       | 3.40 sec                                                     | 2.78 sec: 1.22x faster                                       |
| html5lib       | 94.6 ms                                                      | 68.4 ms: 1.38x faster                                        |
| tornado_http   | 152 ms                                                       | 114 ms: 1.34x faster                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 78.5 ms: 1.75x faster                                        |
| float          | 110 ms                                                       | 70.4 ms: 1.57x faster                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.42x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 148 ms: 1.31x faster                                         |
| regex_v8       | 26.6 ms                                                      | 23.9 ms: 1.12x faster                                        |
| regex_dna      | 259 ms                                                       | 234 ms: 1.11x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 211 us: 1.52x faster                                         |
| pickle_pure_python   | 457 us                                                       | 321 us: 1.43x faster                                         |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                        |
| xml_etree_process    | 76.0 ms                                                      | 57.0 ms: 1.33x faster                                        |
| json_loads           | 30.0 us                                                      | 24.0 us: 1.25x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 82.4 ms: 1.15x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 146 ms: 1.10x faster                                         |
| pickle_list          | 4.11 us                                                      | 3.74 us: 1.10x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                         |
| pickle               | 9.94 us                                                      | 9.98 us: 1.00x slower                                        |
| pickle_dict          | 30.0 us                                                      | 30.2 us: 1.01x slower                                        |
| unpickle_list        | 4.49 us                                                      | 4.63 us: 1.03x slower                                        |
| Geometric mean       | (ref)                                                        | 1.16x faster                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.1 ms: 1.04x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.34 ms: 1.14x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.90 ms: 1.48x faster                                        |
| django_template | 51.5 ms                                                      | 41.3 ms: 1.25x faster                                        |
| genshi_text     | 31.5 ms                                                      | 25.8 ms: 1.22x faster                                        |
| genshi_xml      | 64.7 ms                                                      | 53.7 ms: 1.21x faster                                        |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.39 ms: 2.20x faster                                        |
| asyncio_tcp             | 782 ms                                                       | 383 ms: 2.04x faster                                         |
| logging_silent          | 166 ns                                                       | 94.1 ns: 1.76x faster                                        |
| nbody                   | 137 ms                                                       | 78.5 ms: 1.75x faster                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.34 ms: 1.69x faster                                        |
| raytrace                | 488 ms                                                       | 295 ms: 1.65x faster                                         |
| scimark_lu              | 164 ms                                                       | 100.0 ms: 1.64x faster                                       |
| scimark_monte_carlo     | 109 ms                                                       | 66.9 ms: 1.64x faster                                        |
| generators              | 58.0 ms                                                      | 35.6 ms: 1.63x faster                                        |
| scimark_sor             | 177 ms                                                       | 110 ms: 1.60x faster                                         |
| sqlglot_transpile       | 2.71 ms                                                      | 1.70 ms: 1.60x faster                                        |
| float                   | 110 ms                                                       | 70.4 ms: 1.57x faster                                        |
| richards                | 74.1 ms                                                      | 47.3 ms: 1.57x faster                                        |
| unpickle_pure_python    | 321 us                                                       | 211 us: 1.52x faster                                         |
| spectral_norm           | 136 ms                                                       | 89.6 ms: 1.52x faster                                        |
| go                      | 259 ms                                                       | 172 ms: 1.51x faster                                         |
| pyflate                 | 697 ms                                                       | 469 ms: 1.49x faster                                         |
| mako                    | 14.7 ms                                                      | 9.90 ms: 1.48x faster                                        |
| chaos                   | 107 ms                                                       | 72.9 ms: 1.47x faster                                        |
| hexiom                  | 9.52 ms                                                      | 6.63 ms: 1.44x faster                                        |
| crypto_pyaes            | 118 ms                                                       | 82.8 ms: 1.43x faster                                        |
| pickle_pure_python      | 457 us                                                       | 321 us: 1.43x faster                                         |
| deepcopy_memo           | 48.9 us                                                      | 34.9 us: 1.40x faster                                        |
| html5lib                | 94.6 ms                                                      | 68.4 ms: 1.38x faster                                        |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.38x faster                                       |
| scimark_fft             | 359 ms                                                       | 261 ms: 1.38x faster                                         |
| json_dumps              | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                        |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.80 ms: 1.37x faster                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.58 sec: 1.36x faster                                       |
| async_tree_none         | 700 ms                                                       | 515 ms: 1.36x faster                                         |
| pprint_safe_repr        | 1.05 sec                                                     | 773 ms: 1.36x faster                                         |
| async_tree_memoization  | 824 ms                                                       | 617 ms: 1.34x faster                                         |
| tornado_http            | 152 ms                                                       | 114 ms: 1.34x faster                                         |
| xml_etree_process       | 76.0 ms                                                      | 57.0 ms: 1.33x faster                                        |
| unpack_sequence         | 59.5 ns                                                      | 45.0 ns: 1.32x faster                                        |
| bench_mp_pool           | 7.18 ms                                                      | 5.44 ms: 1.32x faster                                        |
| regex_compile           | 194 ms                                                       | 148 ms: 1.31x faster                                         |
| chameleon               | 9.72 ms                                                      | 7.49 ms: 1.30x faster                                        |
| thrift                  | 1.16 ms                                                      | 899 us: 1.29x faster                                         |
| logging_simple          | 8.90 us                                                      | 6.92 us: 1.29x faster                                        |
| pycparser               | 1.66 sec                                                     | 1.30 sec: 1.28x faster                                       |
| async_tree_cpu_io_mixed | 952 ms                                                       | 749 ms: 1.27x faster                                         |
| fannkuch                | 496 ms                                                       | 395 ms: 1.25x faster                                         |
| json_loads              | 30.0 us                                                      | 24.0 us: 1.25x faster                                        |
| django_template         | 51.5 ms                                                      | 41.3 ms: 1.25x faster                                        |
| dulwich_log             | 80.1 ms                                                      | 64.7 ms: 1.24x faster                                        |
| coroutines              | 30.4 ms                                                      | 24.7 ms: 1.23x faster                                        |
| 2to3                    | 350 ms                                                       | 284 ms: 1.23x faster                                         |
| mypy2                   | 466 ms                                                       | 379 ms: 1.23x faster                                         |
| logging_format          | 9.57 us                                                      | 7.80 us: 1.23x faster                                        |
| sqlglot_normalize       | 144 ms                                                       | 118 ms: 1.22x faster                                         |
| docutils                | 3.40 sec                                                     | 2.78 sec: 1.22x faster                                       |
| genshi_text             | 31.5 ms                                                      | 25.8 ms: 1.22x faster                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 57.8 ms: 1.22x faster                                        |
| genshi_xml              | 64.7 ms                                                      | 53.7 ms: 1.21x faster                                        |
| mdp                     | 3.03 sec                                                     | 2.52 sec: 1.21x faster                                       |
| deepcopy                | 454 us                                                       | 377 us: 1.20x faster                                         |
| json                    | 5.96 ms                                                      | 5.03 ms: 1.19x faster                                        |
| deepcopy_reduce         | 4.03 us                                                      | 3.41 us: 1.18x faster                                        |
| bench_thread_pool       | 1.14 ms                                                      | 962 us: 1.18x faster                                         |
| pathlib                 | 21.7 ms                                                      | 18.5 ms: 1.17x faster                                        |
| pylint                  | 562 ms                                                       | 484 ms: 1.16x faster                                         |
| sqlite_synth            | 2.97 us                                                      | 2.58 us: 1.15x faster                                        |
| xml_etree_generate      | 94.6 ms                                                      | 82.4 ms: 1.15x faster                                        |
| nqueens                 | 112 ms                                                       | 100 ms: 1.12x faster                                         |
| sympy_expand            | 599 ms                                                       | 537 ms: 1.12x faster                                         |
| regex_v8                | 26.6 ms                                                      | 23.9 ms: 1.12x faster                                        |
| regex_dna               | 259 ms                                                       | 234 ms: 1.11x faster                                         |
| sympy_integrate         | 28.1 ms                                                      | 25.3 ms: 1.11x faster                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.64 ms: 1.11x faster                                        |
| xml_etree_parse         | 162 ms                                                       | 146 ms: 1.10x faster                                         |
| pickle_list             | 4.11 us                                                      | 3.74 us: 1.10x faster                                        |
| xml_etree_iterparse     | 110 ms                                                       | 101 ms: 1.09x faster                                         |
| async_generators        | 422 ms                                                       | 388 ms: 1.09x faster                                         |
| meteor_contest          | 137 ms                                                       | 126 ms: 1.09x faster                                         |
| comprehensions          | 26.9 us                                                      | 24.8 us: 1.09x faster                                        |
| sympy_str               | 358 ms                                                       | 331 ms: 1.08x faster                                         |
| telco                   | 7.14 ms                                                      | 6.76 ms: 1.06x faster                                        |
| sympy_sum               | 193 ms                                                       | 183 ms: 1.05x faster                                         |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| python_startup          | 11.5 ms                                                      | 11.1 ms: 1.04x faster                                        |
| pickle                  | 9.94 us                                                      | 9.98 us: 1.00x slower                                        |
| pickle_dict             | 30.0 us                                                      | 30.2 us: 1.01x slower                                        |
| gc_traversal            | 3.45 ms                                                      | 3.55 ms: 1.03x slower                                        |
| unpickle_list           | 4.49 us                                                      | 4.63 us: 1.03x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.34 ms: 1.14x slower                                        |
| regex_effbot            | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                        |
| dask                    | 463 ms                                                       | 564 ms: 1.22x slower                                         |
| coverage                | 64.0 ms                                                      | 91.1 ms: 1.42x slower                                        |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                 |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x
