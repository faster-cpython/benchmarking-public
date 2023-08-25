
# Results vs. 3.10.4

- fork: faster-cpython
- ref: instrument_all_possi
- machine: linux-x86_64
- commit hash: 5418580
- commit date: 2023-05-10
- overall geometric mean: 1.27x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                                   |
| docutils       | 3.40 sec                                                     | 2.88 sec: 1.18x faster                                                                 |
| tornado_http   | 152 ms                                                       | 113 ms: 1.34x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 84.7 ms: 1.62x faster                                                                  |
| float          | 110 ms                                                       | 79.0 ms: 1.40x faster                                                                  |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 144 ms: 1.34x faster                                                                   |
| regex_dna      | 259 ms                                                       | 227 ms: 1.14x faster                                                                   |
| regex_v8       | 26.6 ms                                                      | 23.4 ms: 1.14x faster                                                                  |
| regex_effbot   | 2.99 ms                                                      | 3.41 ms: 1.14x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 205 us: 1.56x faster                                                                   |
| pickle_pure_python   | 457 us                                                       | 320 us: 1.43x faster                                                                   |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                                  |
| xml_etree_process    | 76.0 ms                                                      | 58.7 ms: 1.30x faster                                                                  |
| json_loads           | 30.0 us                                                      | 24.5 us: 1.23x faster                                                                  |
| xml_etree_generate   | 94.6 ms                                                      | 85.6 ms: 1.11x faster                                                                  |
| xml_etree_parse      | 162 ms                                                       | 149 ms: 1.08x faster                                                                   |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                                   |
| pickle               | 9.94 us                                                      | 10.3 us: 1.04x slower                                                                  |
| unpickle_list        | 4.49 us                                                      | 4.72 us: 1.05x slower                                                                  |
| unpickle             | 14.2 us                                                      | 14.9 us: 1.05x slower                                                                  |
| pickle_list          | 4.11 us                                                      | 4.45 us: 1.08x slower                                                                  |
| pickle_dict          | 30.0 us                                                      | 32.6 us: 1.09x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                                  |
| python_startup_no_site | 7.32 ms                                                      | 8.38 ms: 1.14x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|-----------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.22 ms: 2.32x faster                                                                  |
| asyncio_tcp             | 782 ms                                                       | 379 ms: 2.06x faster                                                                   |
| logging_silent          | 166 ns                                                       | 91.1 ns: 1.82x faster                                                                  |
| go                      | 259 ms                                                       | 144 ms: 1.80x faster                                                                   |
| richards                | 74.1 ms                                                      | 43.5 ms: 1.70x faster                                                                  |
| chaos                   | 107 ms                                                       | 64.3 ms: 1.67x faster                                                                  |
| scimark_lu              | 164 ms                                                       | 99.6 ms: 1.64x faster                                                                  |
| hexiom                  | 9.52 ms                                                      | 5.79 ms: 1.64x faster                                                                  |
| raytrace                | 488 ms                                                       | 299 ms: 1.63x faster                                                                   |
| scimark_sor             | 177 ms                                                       | 109 ms: 1.62x faster                                                                   |
| sqlglot_parse           | 2.26 ms                                                      | 1.39 ms: 1.62x faster                                                                  |
| nbody                   | 137 ms                                                       | 84.7 ms: 1.62x faster                                                                  |
| scimark_monte_carlo     | 109 ms                                                       | 68.1 ms: 1.61x faster                                                                  |
| generators              | 58.0 ms                                                      | 36.4 ms: 1.59x faster                                                                  |
| unpickle_pure_python    | 321 us                                                       | 205 us: 1.56x faster                                                                   |
| async_tree_none         | 700 ms                                                       | 455 ms: 1.54x faster                                                                   |
| async_tree_io           | 1.61 sec                                                     | 1.05 sec: 1.54x faster                                                                 |
| pyflate                 | 697 ms                                                       | 461 ms: 1.51x faster                                                                   |
| sqlglot_transpile       | 2.71 ms                                                      | 1.79 ms: 1.51x faster                                                                  |
| async_tree_memoization  | 824 ms                                                       | 546 ms: 1.51x faster                                                                   |
| crypto_pyaes            | 118 ms                                                       | 79.2 ms: 1.49x faster                                                                  |
| spectral_norm           | 136 ms                                                       | 92.6 ms: 1.47x faster                                                                  |
| fannkuch                | 496 ms                                                       | 343 ms: 1.45x faster                                                                   |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                                  |
| pickle_pure_python      | 457 us                                                       | 320 us: 1.43x faster                                                                   |
| float                   | 110 ms                                                       | 79.0 ms: 1.40x faster                                                                  |
| json_dumps              | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                                  |
| async_tree_cpu_io_mixed | 952 ms                                                       | 698 ms: 1.36x faster                                                                   |
| coroutines              | 30.4 ms                                                      | 22.6 ms: 1.34x faster                                                                  |
| regex_compile           | 194 ms                                                       | 144 ms: 1.34x faster                                                                   |
| tornado_http            | 152 ms                                                       | 113 ms: 1.34x faster                                                                   |
| pycparser               | 1.66 sec                                                     | 1.25 sec: 1.33x faster                                                                 |
| unpack_sequence         | 59.5 ns                                                      | 44.8 ns: 1.33x faster                                                                  |
| pprint_pformat          | 2.15 sec                                                     | 1.64 sec: 1.32x faster                                                                 |
| pprint_safe_repr        | 1.05 sec                                                     | 798 ms: 1.32x faster                                                                   |
| deepcopy_memo           | 48.9 us                                                      | 37.2 us: 1.31x faster                                                                  |
| logging_simple          | 8.90 us                                                      | 6.80 us: 1.31x faster                                                                  |
| xml_etree_process       | 76.0 ms                                                      | 58.7 ms: 1.30x faster                                                                  |
| logging_format          | 9.57 us                                                      | 7.51 us: 1.27x faster                                                                  |
| mypy2                   | 466 ms                                                       | 369 ms: 1.27x faster                                                                   |
| nqueens                 | 112 ms                                                       | 90.1 ms: 1.25x faster                                                                  |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.23 ms: 1.23x faster                                                                  |
| 2to3                    | 350 ms                                                       | 285 ms: 1.23x faster                                                                   |
| sqlglot_normalize       | 144 ms                                                       | 118 ms: 1.23x faster                                                                   |
| json_loads              | 30.0 us                                                      | 24.5 us: 1.23x faster                                                                  |
| comprehensions          | 26.9 us                                                      | 22.0 us: 1.22x faster                                                                  |
| dulwich_log             | 80.1 ms                                                      | 65.9 ms: 1.21x faster                                                                  |
| deepcopy                | 454 us                                                       | 375 us: 1.21x faster                                                                   |
| scimark_fft             | 359 ms                                                       | 298 ms: 1.21x faster                                                                   |
| sqlglot_optimize        | 70.3 ms                                                      | 58.4 ms: 1.20x faster                                                                  |
| mdp                     | 3.03 sec                                                     | 2.53 sec: 1.20x faster                                                                 |
| bench_thread_pool       | 1.14 ms                                                      | 959 us: 1.19x faster                                                                   |
| docutils                | 3.40 sec                                                     | 2.88 sec: 1.18x faster                                                                 |
| deepcopy_reduce         | 4.03 us                                                      | 3.45 us: 1.17x faster                                                                  |
| json                    | 5.96 ms                                                      | 5.18 ms: 1.15x faster                                                                  |
| regex_dna               | 259 ms                                                       | 227 ms: 1.14x faster                                                                   |
| regex_v8                | 26.6 ms                                                      | 23.4 ms: 1.14x faster                                                                  |
| sqlite_synth            | 2.97 us                                                      | 2.66 us: 1.12x faster                                                                  |
| create_gc_cycles        | 1.82 ms                                                      | 1.63 ms: 1.11x faster                                                                  |
| async_generators        | 422 ms                                                       | 380 ms: 1.11x faster                                                                   |
| xml_etree_generate      | 94.6 ms                                                      | 85.6 ms: 1.11x faster                                                                  |
| xml_etree_parse         | 162 ms                                                       | 149 ms: 1.08x faster                                                                   |
| pathlib                 | 21.7 ms                                                      | 20.1 ms: 1.08x faster                                                                  |
| meteor_contest          | 137 ms                                                       | 128 ms: 1.07x faster                                                                   |
| xml_etree_iterparse     | 110 ms                                                       | 104 ms: 1.06x faster                                                                   |
| pidigits                | 271 ms                                                       | 261 ms: 1.04x faster                                                                   |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                                  |
| telco                   | 7.14 ms                                                      | 7.23 ms: 1.01x slower                                                                  |
| pickle                  | 9.94 us                                                      | 10.3 us: 1.04x slower                                                                  |
| unpickle_list           | 4.49 us                                                      | 4.72 us: 1.05x slower                                                                  |
| unpickle                | 14.2 us                                                      | 14.9 us: 1.05x slower                                                                  |
| pickle_list             | 4.11 us                                                      | 4.45 us: 1.08x slower                                                                  |
| pickle_dict             | 30.0 us                                                      | 32.6 us: 1.09x slower                                                                  |
| regex_effbot            | 2.99 ms                                                      | 3.41 ms: 1.14x slower                                                                  |
| python_startup_no_site  | 7.32 ms                                                      | 8.38 ms: 1.14x slower                                                                  |
| gc_traversal            | 3.45 ms                                                      | 4.06 ms: 1.18x slower                                                                  |
| dask                    | 463 ms                                                       | 556 ms: 1.20x slower                                                                   |
| coverage                | 64.0 ms                                                      | 88.5 ms: 1.38x slower                                                                  |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x
