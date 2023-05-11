
# Results vs. 3.10.4

- fork: faster-cpython
- ref: instrument_all_possi
- machine: linux-x86_64
- commit hash: 5418580
- commit date: 2023-05-10
- overall geometric mean: 1.27x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 285 ms: 1.24x faster                                                                   |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                                                 |
| tornado_http   | 151 ms                                                       | 113 ms: 1.33x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 84.7 ms: 1.56x faster                                                                  |
| float          | 109 ms                                                       | 79.0 ms: 1.38x faster                                                                  |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 144 ms: 1.32x faster                                                                   |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                                                   |
| regex_v8       | 26.0 ms                                                      | 23.4 ms: 1.11x faster                                                                  |
| regex_effbot   | 2.99 ms                                                      | 3.41 ms: 1.14x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 205 us: 1.55x faster                                                                   |
| pickle_pure_python   | 451 us                                                       | 320 us: 1.41x faster                                                                   |
| json_dumps           | 14.3 ms                                                      | 10.2 ms: 1.40x faster                                                                  |
| xml_etree_process    | 77.6 ms                                                      | 58.7 ms: 1.32x faster                                                                  |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                                                  |
| xml_etree_generate   | 94.1 ms                                                      | 85.6 ms: 1.10x faster                                                                  |
| xml_etree_parse      | 160 ms                                                       | 149 ms: 1.07x faster                                                                   |
| xml_etree_iterparse  | 109 ms                                                       | 104 ms: 1.05x faster                                                                   |
| pickle               | 10.1 us                                                      | 10.3 us: 1.02x slower                                                                  |
| pickle_list          | 4.11 us                                                      | 4.45 us: 1.08x slower                                                                  |
| pickle_dict          | 29.5 us                                                      | 32.6 us: 1.10x slower                                                                  |
| unpickle             | 13.3 us                                                      | 14.9 us: 1.12x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                           |

Benchmark hidden because not significant (1): unpickle_list

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
| mako      | 14.7 ms                                                      | 10.2 ms: 1.45x faster                                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.22 ms: 2.35x faster                                                                  |
| asyncio_tcp             | 787 ms                                                       | 379 ms: 2.08x faster                                                                   |
| go                      | 264 ms                                                       | 144 ms: 1.84x faster                                                                   |
| logging_silent          | 165 ns                                                       | 91.1 ns: 1.81x faster                                                                  |
| richards                | 73.9 ms                                                      | 43.5 ms: 1.70x faster                                                                  |
| chaos                   | 108 ms                                                       | 64.3 ms: 1.68x faster                                                                  |
| scimark_lu              | 164 ms                                                       | 99.6 ms: 1.65x faster                                                                  |
| hexiom                  | 9.54 ms                                                      | 5.79 ms: 1.65x faster                                                                  |
| raytrace                | 491 ms                                                       | 299 ms: 1.64x faster                                                                   |
| scimark_sor             | 177 ms                                                       | 109 ms: 1.62x faster                                                                   |
| sqlglot_parse           | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                                                  |
| scimark_monte_carlo     | 109 ms                                                       | 68.1 ms: 1.60x faster                                                                  |
| pyflate                 | 731 ms                                                       | 461 ms: 1.59x faster                                                                   |
| generators              | 57.0 ms                                                      | 36.4 ms: 1.57x faster                                                                  |
| nbody                   | 132 ms                                                       | 84.7 ms: 1.56x faster                                                                  |
| unpickle_pure_python    | 318 us                                                       | 205 us: 1.55x faster                                                                   |
| async_tree_io           | 1.61 sec                                                     | 1.05 sec: 1.54x faster                                                                 |
| async_tree_none         | 698 ms                                                       | 455 ms: 1.53x faster                                                                   |
| async_tree_memoization  | 822 ms                                                       | 546 ms: 1.51x faster                                                                   |
| sqlglot_transpile       | 2.69 ms                                                      | 1.79 ms: 1.50x faster                                                                  |
| crypto_pyaes            | 119 ms                                                       | 79.2 ms: 1.50x faster                                                                  |
| spectral_norm           | 138 ms                                                       | 92.6 ms: 1.49x faster                                                                  |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.45x faster                                                                  |
| fannkuch                | 496 ms                                                       | 343 ms: 1.45x faster                                                                   |
| pickle_pure_python      | 451 us                                                       | 320 us: 1.41x faster                                                                   |
| json_dumps              | 14.3 ms                                                      | 10.2 ms: 1.40x faster                                                                  |
| float                   | 109 ms                                                       | 79.0 ms: 1.38x faster                                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                       | 698 ms: 1.36x faster                                                                   |
| logging_simple          | 9.24 us                                                      | 6.80 us: 1.36x faster                                                                  |
| coroutines              | 30.6 ms                                                      | 22.6 ms: 1.35x faster                                                                  |
| unpack_sequence         | 59.7 ns                                                      | 44.8 ns: 1.33x faster                                                                  |
| tornado_http            | 151 ms                                                       | 113 ms: 1.33x faster                                                                   |
| pycparser               | 1.66 sec                                                     | 1.25 sec: 1.33x faster                                                                 |
| regex_compile           | 191 ms                                                       | 144 ms: 1.32x faster                                                                   |
| logging_format          | 9.94 us                                                      | 7.51 us: 1.32x faster                                                                  |
| xml_etree_process       | 77.6 ms                                                      | 58.7 ms: 1.32x faster                                                                  |
| deepcopy_memo           | 49.2 us                                                      | 37.2 us: 1.32x faster                                                                  |
| pprint_pformat          | 2.12 sec                                                     | 1.64 sec: 1.30x faster                                                                 |
| pprint_safe_repr        | 1.03 sec                                                     | 798 ms: 1.29x faster                                                                   |
| mypy2                   | 466 ms                                                       | 369 ms: 1.27x faster                                                                   |
| nqueens                 | 114 ms                                                       | 90.1 ms: 1.26x faster                                                                  |
| sqlglot_normalize       | 147 ms                                                       | 118 ms: 1.25x faster                                                                   |
| comprehensions          | 27.3 us                                                      | 22.0 us: 1.24x faster                                                                  |
| json_loads              | 30.3 us                                                      | 24.5 us: 1.24x faster                                                                  |
| 2to3                    | 352 ms                                                       | 285 ms: 1.24x faster                                                                   |
| dulwich_log             | 80.5 ms                                                      | 65.9 ms: 1.22x faster                                                                  |
| deepcopy                | 457 us                                                       | 375 us: 1.22x faster                                                                   |
| scimark_fft             | 359 ms                                                       | 298 ms: 1.20x faster                                                                   |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.23 ms: 1.20x faster                                                                  |
| sqlglot_optimize        | 70.1 ms                                                      | 58.4 ms: 1.20x faster                                                                  |
| bench_thread_pool       | 1.14 ms                                                      | 959 us: 1.19x faster                                                                   |
| docutils                | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                                                 |
| mdp                     | 2.95 sec                                                     | 2.53 sec: 1.17x faster                                                                 |
| regex_dna               | 261 ms                                                       | 227 ms: 1.15x faster                                                                   |
| json                    | 5.94 ms                                                      | 5.18 ms: 1.15x faster                                                                  |
| deepcopy_reduce         | 3.91 us                                                      | 3.45 us: 1.13x faster                                                                  |
| sqlite_synth            | 2.96 us                                                      | 2.66 us: 1.12x faster                                                                  |
| meteor_contest          | 142 ms                                                       | 128 ms: 1.11x faster                                                                   |
| regex_v8                | 26.0 ms                                                      | 23.4 ms: 1.11x faster                                                                  |
| create_gc_cycles        | 1.80 ms                                                      | 1.63 ms: 1.10x faster                                                                  |
| async_generators        | 419 ms                                                       | 380 ms: 1.10x faster                                                                   |
| xml_etree_generate      | 94.1 ms                                                      | 85.6 ms: 1.10x faster                                                                  |
| xml_etree_parse         | 160 ms                                                       | 149 ms: 1.07x faster                                                                   |
| pathlib                 | 21.3 ms                                                      | 20.1 ms: 1.06x faster                                                                  |
| xml_etree_iterparse     | 109 ms                                                       | 104 ms: 1.05x faster                                                                   |
| pidigits                | 271 ms                                                       | 261 ms: 1.04x faster                                                                   |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                                  |
| telco                   | 7.14 ms                                                      | 7.23 ms: 1.01x slower                                                                  |
| pickle                  | 10.1 us                                                      | 10.3 us: 1.02x slower                                                                  |
| pickle_list             | 4.11 us                                                      | 4.45 us: 1.08x slower                                                                  |
| pickle_dict             | 29.5 us                                                      | 32.6 us: 1.10x slower                                                                  |
| unpickle                | 13.3 us                                                      | 14.9 us: 1.12x slower                                                                  |
| regex_effbot            | 2.99 ms                                                      | 3.41 ms: 1.14x slower                                                                  |
| python_startup_no_site  | 7.32 ms                                                      | 8.38 ms: 1.14x slower                                                                  |
| dask                    | 478 ms                                                       | 556 ms: 1.16x slower                                                                   |
| gc_traversal            | 3.46 ms                                                      | 4.06 ms: 1.18x slower                                                                  |
| coverage                | 71.1 ms                                                      | 88.5 ms: 1.24x slower                                                                  |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                                           |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
