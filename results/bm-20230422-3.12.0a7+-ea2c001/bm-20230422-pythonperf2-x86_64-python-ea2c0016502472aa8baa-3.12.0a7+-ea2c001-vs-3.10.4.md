
# Results vs. 3.10.4

- fork: python
- ref: ea2c0016502472aa8baa
- machine: linux-x86_64
- commit hash: ea2c001
- commit date: 2023-04-22
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                         |
| chameleon      | 9.72 ms                                                      | 7.44 ms: 1.31x faster                                                        |
| docutils       | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| html5lib       | 94.6 ms                                                      | 68.9 ms: 1.37x faster                                                        |
| tornado_http   | 152 ms                                                       | 119 ms: 1.28x faster                                                         |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 83.7 ms: 1.64x faster                                                        |
| float          | 110 ms                                                       | 77.1 ms: 1.43x faster                                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 143 ms: 1.36x faster                                                         |
| regex_dna      | 259 ms                                                       | 230 ms: 1.13x faster                                                         |
| regex_v8       | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.40 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 209 us: 1.54x faster                                                         |
| pickle_pure_python   | 457 us                                                       | 319 us: 1.43x faster                                                         |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                        |
| xml_etree_process    | 76.0 ms                                                      | 58.5 ms: 1.30x faster                                                        |
| json_loads           | 30.0 us                                                      | 24.7 us: 1.22x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 85.2 ms: 1.11x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 151 ms: 1.07x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.95 us: 1.04x faster                                                        |
| unpickle_list        | 4.49 us                                                      | 4.55 us: 1.01x slower                                                        |
| pickle_dict          | 30.0 us                                                      | 30.7 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                                 |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.1 ms: 1.03x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.37 ms: 1.14x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                                        |
| django_template | 51.5 ms                                                      | 38.3 ms: 1.34x faster                                                        |
| genshi_text     | 31.5 ms                                                      | 25.0 ms: 1.26x faster                                                        |
| genshi_xml      | 64.7 ms                                                      | 53.9 ms: 1.20x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.30 ms: 2.26x faster                                                        |
| asyncio_tcp             | 782 ms                                                       | 379 ms: 2.07x faster                                                         |
| logging_silent          | 166 ns                                                       | 93.5 ns: 1.77x faster                                                        |
| go                      | 259 ms                                                       | 146 ms: 1.77x faster                                                         |
| scimark_lu              | 164 ms                                                       | 95.5 ms: 1.71x faster                                                        |
| richards                | 74.1 ms                                                      | 43.9 ms: 1.69x faster                                                        |
| nbody                   | 137 ms                                                       | 83.7 ms: 1.64x faster                                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.38 ms: 1.64x faster                                                        |
| raytrace                | 488 ms                                                       | 299 ms: 1.63x faster                                                         |
| chaos                   | 107 ms                                                       | 66.3 ms: 1.61x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 68.0 ms: 1.61x faster                                                        |
| hexiom                  | 9.52 ms                                                      | 5.92 ms: 1.61x faster                                                        |
| scimark_sor             | 177 ms                                                       | 110 ms: 1.61x faster                                                         |
| spectral_norm           | 136 ms                                                       | 86.0 ms: 1.58x faster                                                        |
| generators              | 58.0 ms                                                      | 36.6 ms: 1.58x faster                                                        |
| unpickle_pure_python    | 321 us                                                       | 209 us: 1.54x faster                                                         |
| pyflate                 | 697 ms                                                       | 458 ms: 1.52x faster                                                         |
| sqlglot_transpile       | 2.71 ms                                                      | 1.78 ms: 1.52x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 79.0 ms: 1.50x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 319 us: 1.43x faster                                                         |
| float                   | 110 ms                                                       | 77.1 ms: 1.43x faster                                                        |
| fannkuch                | 496 ms                                                       | 351 ms: 1.41x faster                                                         |
| async_tree_io           | 1.61 sec                                                     | 1.15 sec: 1.40x faster                                                       |
| async_tree_memoization  | 824 ms                                                       | 594 ms: 1.39x faster                                                         |
| async_tree_none         | 700 ms                                                       | 505 ms: 1.39x faster                                                         |
| json_dumps              | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                        |
| html5lib                | 94.6 ms                                                      | 68.9 ms: 1.37x faster                                                        |
| regex_compile           | 194 ms                                                       | 143 ms: 1.36x faster                                                         |
| logging_simple          | 8.90 us                                                      | 6.60 us: 1.35x faster                                                        |
| django_template         | 51.5 ms                                                      | 38.3 ms: 1.34x faster                                                        |
| coroutines              | 30.4 ms                                                      | 22.7 ms: 1.34x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                                       |
| thrift                  | 1.16 ms                                                      | 887 us: 1.31x faster                                                         |
| logging_format          | 9.57 us                                                      | 7.32 us: 1.31x faster                                                        |
| chameleon               | 9.72 ms                                                      | 7.44 ms: 1.31x faster                                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                                       |
| deepcopy_memo           | 48.9 us                                                      | 37.5 us: 1.30x faster                                                        |
| xml_etree_process       | 76.0 ms                                                      | 58.5 ms: 1.30x faster                                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 811 ms: 1.30x faster                                                         |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.01 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 739 ms: 1.29x faster                                                         |
| tornado_http            | 152 ms                                                       | 119 ms: 1.28x faster                                                         |
| genshi_text             | 31.5 ms                                                      | 25.0 ms: 1.26x faster                                                        |
| nqueens                 | 112 ms                                                       | 90.1 ms: 1.25x faster                                                        |
| scimark_fft             | 359 ms                                                       | 292 ms: 1.23x faster                                                         |
| dulwich_log             | 80.1 ms                                                      | 65.0 ms: 1.23x faster                                                        |
| 2to3                    | 350 ms                                                       | 284 ms: 1.23x faster                                                         |
| json_loads              | 30.0 us                                                      | 24.7 us: 1.22x faster                                                        |
| mypy2                   | 466 ms                                                       | 388 ms: 1.20x faster                                                         |
| genshi_xml              | 64.7 ms                                                      | 53.9 ms: 1.20x faster                                                        |
| sqlglot_normalize       | 144 ms                                                       | 121 ms: 1.20x faster                                                         |
| mdp                     | 3.03 sec                                                     | 2.54 sec: 1.20x faster                                                       |
| sqlglot_optimize        | 70.3 ms                                                      | 59.0 ms: 1.19x faster                                                        |
| deepcopy                | 454 us                                                       | 383 us: 1.18x faster                                                         |
| bench_mp_pool           | 7.18 ms                                                      | 6.08 ms: 1.18x faster                                                        |
| docutils                | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 966 us: 1.18x faster                                                         |
| deepcopy_reduce         | 4.03 us                                                      | 3.45 us: 1.17x faster                                                        |
| pathlib                 | 21.7 ms                                                      | 18.6 ms: 1.17x faster                                                        |
| json                    | 5.96 ms                                                      | 5.13 ms: 1.16x faster                                                        |
| sympy_expand            | 599 ms                                                       | 529 ms: 1.13x faster                                                         |
| regex_dna               | 259 ms                                                       | 230 ms: 1.13x faster                                                         |
| pylint                  | 562 ms                                                       | 498 ms: 1.13x faster                                                         |
| unpack_sequence         | 59.5 ns                                                      | 52.8 ns: 1.13x faster                                                        |
| regex_v8                | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                                        |
| sqlite_synth            | 2.97 us                                                      | 2.66 us: 1.11x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.3 ms: 1.11x faster                                                        |
| xml_etree_generate      | 94.6 ms                                                      | 85.2 ms: 1.11x faster                                                        |
| comprehensions          | 26.9 us                                                      | 24.3 us: 1.11x faster                                                        |
| sympy_str               | 358 ms                                                       | 325 ms: 1.10x faster                                                         |
| async_generators        | 422 ms                                                       | 386 ms: 1.09x faster                                                         |
| create_gc_cycles        | 1.82 ms                                                      | 1.68 ms: 1.08x faster                                                        |
| xml_etree_parse         | 162 ms                                                       | 151 ms: 1.07x faster                                                         |
| sympy_sum               | 193 ms                                                       | 182 ms: 1.06x faster                                                         |
| xml_etree_iterparse     | 110 ms                                                       | 105 ms: 1.05x faster                                                         |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                                         |
| pickle_list             | 4.11 us                                                      | 3.95 us: 1.04x faster                                                        |
| python_startup          | 11.5 ms                                                      | 11.1 ms: 1.03x faster                                                        |
| telco                   | 7.14 ms                                                      | 7.04 ms: 1.01x faster                                                        |
| meteor_contest          | 137 ms                                                       | 138 ms: 1.01x slower                                                         |
| unpickle_list           | 4.49 us                                                      | 4.55 us: 1.01x slower                                                        |
| pickle_dict             | 30.0 us                                                      | 30.7 us: 1.02x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.40 ms: 1.14x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.37 ms: 1.14x slower                                                        |
| gc_traversal            | 3.45 ms                                                      | 4.02 ms: 1.16x slower                                                        |
| dask                    | 463 ms                                                       | 563 ms: 1.22x slower                                                         |
| coverage                | 64.0 ms                                                      | 89.2 ms: 1.39x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                                 |

Benchmark hidden because not significant (2): pickle, unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x
