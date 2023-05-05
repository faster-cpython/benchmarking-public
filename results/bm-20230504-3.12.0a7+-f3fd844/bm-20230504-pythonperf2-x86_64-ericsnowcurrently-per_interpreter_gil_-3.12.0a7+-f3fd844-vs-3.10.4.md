
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 286 ms: 1.23x faster                                                                    |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                                                  |
| tornado_http   | 151 ms                                                       | 114 ms: 1.33x faster                                                                    |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 85.2 ms: 1.55x faster                                                                   |
| float          | 109 ms                                                       | 78.5 ms: 1.39x faster                                                                   |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                                    |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 145 ms: 1.31x faster                                                                    |
| regex_dna      | 261 ms                                                       | 228 ms: 1.14x faster                                                                    |
| regex_v8       | 26.0 ms                                                      | 23.4 ms: 1.11x faster                                                                   |
| regex_effbot   | 2.99 ms                                                      | 3.41 ms: 1.14x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 206 us: 1.54x faster                                                                    |
| pickle_pure_python   | 451 us                                                       | 318 us: 1.42x faster                                                                    |
| json_dumps           | 14.3 ms                                                      | 10.3 ms: 1.38x faster                                                                   |
| xml_etree_process    | 77.6 ms                                                      | 59.1 ms: 1.31x faster                                                                   |
| json_loads           | 30.3 us                                                      | 24.3 us: 1.25x faster                                                                   |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                                    |
| xml_etree_generate   | 94.1 ms                                                      | 86.1 ms: 1.09x faster                                                                   |
| xml_etree_iterparse  | 109 ms                                                       | 103 ms: 1.06x faster                                                                    |
| pickle               | 10.1 us                                                      | 9.94 us: 1.02x faster                                                                   |
| unpickle_list        | 4.73 us                                                      | 4.86 us: 1.03x slower                                                                   |
| pickle_list          | 4.11 us                                                      | 4.42 us: 1.07x slower                                                                   |
| pickle_dict          | 29.5 us                                                      | 32.5 us: 1.10x slower                                                                   |
| unpickle             | 13.3 us                                                      | 14.8 us: 1.12x slower                                                                   |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                                   |
| python_startup_no_site | 7.32 ms                                                      | 8.44 ms: 1.15x slower                                                                   |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                                                   |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.23 ms: 2.34x faster                                                                   |
| asyncio_tcp             | 787 ms                                                       | 381 ms: 2.07x faster                                                                    |
| go                      | 264 ms                                                       | 144 ms: 1.83x faster                                                                    |
| logging_silent          | 165 ns                                                       | 92.8 ns: 1.77x faster                                                                   |
| richards                | 73.9 ms                                                      | 43.8 ms: 1.69x faster                                                                   |
| pyflate                 | 731 ms                                                       | 443 ms: 1.65x faster                                                                    |
| scimark_lu              | 164 ms                                                       | 99.3 ms: 1.65x faster                                                                   |
| chaos                   | 108 ms                                                       | 66.6 ms: 1.62x faster                                                                   |
| hexiom                  | 9.54 ms                                                      | 5.90 ms: 1.62x faster                                                                   |
| sqlglot_parse           | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                                                   |
| raytrace                | 491 ms                                                       | 308 ms: 1.59x faster                                                                    |
| scimark_sor             | 177 ms                                                       | 113 ms: 1.57x faster                                                                    |
| generators              | 57.0 ms                                                      | 36.6 ms: 1.56x faster                                                                   |
| nbody                   | 132 ms                                                       | 85.2 ms: 1.55x faster                                                                   |
| unpickle_pure_python    | 318 us                                                       | 206 us: 1.54x faster                                                                    |
| scimark_monte_carlo     | 109 ms                                                       | 70.7 ms: 1.54x faster                                                                   |
| spectral_norm           | 138 ms                                                       | 91.2 ms: 1.51x faster                                                                   |
| sqlglot_transpile       | 2.69 ms                                                      | 1.79 ms: 1.50x faster                                                                   |
| crypto_pyaes            | 119 ms                                                       | 80.2 ms: 1.48x faster                                                                   |
| mako                    | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                                                   |
| async_tree_io           | 1.61 sec                                                     | 1.10 sec: 1.47x faster                                                                  |
| bench_mp_pool           | 7.10 ms                                                      | 4.87 ms: 1.46x faster                                                                   |
| async_tree_none         | 698 ms                                                       | 479 ms: 1.46x faster                                                                    |
| async_tree_memoization  | 822 ms                                                       | 575 ms: 1.43x faster                                                                    |
| fannkuch                | 496 ms                                                       | 347 ms: 1.43x faster                                                                    |
| pickle_pure_python      | 451 us                                                       | 318 us: 1.42x faster                                                                    |
| logging_simple          | 9.24 us                                                      | 6.60 us: 1.40x faster                                                                   |
| float                   | 109 ms                                                       | 78.5 ms: 1.39x faster                                                                   |
| deepcopy_memo           | 49.2 us                                                      | 35.5 us: 1.38x faster                                                                   |
| json_dumps              | 14.3 ms                                                      | 10.3 ms: 1.38x faster                                                                   |
| coroutines              | 30.6 ms                                                      | 22.4 ms: 1.36x faster                                                                   |
| logging_format          | 9.94 us                                                      | 7.39 us: 1.35x faster                                                                   |
| pycparser               | 1.66 sec                                                     | 1.23 sec: 1.34x faster                                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                       | 712 ms: 1.34x faster                                                                    |
| tornado_http            | 151 ms                                                       | 114 ms: 1.33x faster                                                                    |
| pprint_pformat          | 2.12 sec                                                     | 1.61 sec: 1.32x faster                                                                  |
| regex_compile           | 191 ms                                                       | 145 ms: 1.31x faster                                                                    |
| xml_etree_process       | 77.6 ms                                                      | 59.1 ms: 1.31x faster                                                                   |
| unpack_sequence         | 59.7 ns                                                      | 46.0 ns: 1.30x faster                                                                   |
| pprint_safe_repr        | 1.03 sec                                                     | 793 ms: 1.29x faster                                                                    |
| nqueens                 | 114 ms                                                       | 90.7 ms: 1.25x faster                                                                   |
| json_loads              | 30.3 us                                                      | 24.3 us: 1.25x faster                                                                   |
| 2to3                    | 352 ms                                                       | 286 ms: 1.23x faster                                                                    |
| mypy2                   | 466 ms                                                       | 378 ms: 1.23x faster                                                                    |
| dulwich_log             | 80.5 ms                                                      | 65.6 ms: 1.23x faster                                                                   |
| sqlglot_normalize       | 147 ms                                                       | 121 ms: 1.22x faster                                                                    |
| deepcopy                | 457 us                                                       | 376 us: 1.22x faster                                                                    |
| scimark_fft             | 359 ms                                                       | 299 ms: 1.20x faster                                                                    |
| docutils                | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                                                  |
| sqlglot_optimize        | 70.1 ms                                                      | 59.3 ms: 1.18x faster                                                                   |
| bench_thread_pool       | 1.14 ms                                                      | 971 us: 1.17x faster                                                                    |
| json                    | 5.94 ms                                                      | 5.12 ms: 1.16x faster                                                                   |
| mdp                     | 2.95 sec                                                     | 2.55 sec: 1.16x faster                                                                  |
| deepcopy_reduce         | 3.91 us                                                      | 3.38 us: 1.16x faster                                                                   |
| regex_dna               | 261 ms                                                       | 228 ms: 1.14x faster                                                                    |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.47 ms: 1.14x faster                                                                   |
| create_gc_cycles        | 1.80 ms                                                      | 1.60 ms: 1.13x faster                                                                   |
| comprehensions          | 27.3 us                                                      | 24.4 us: 1.12x faster                                                                   |
| sqlite_synth            | 2.96 us                                                      | 2.65 us: 1.12x faster                                                                   |
| regex_v8                | 26.0 ms                                                      | 23.4 ms: 1.11x faster                                                                   |
| xml_etree_parse         | 160 ms                                                       | 144 ms: 1.11x faster                                                                    |
| pathlib                 | 21.3 ms                                                      | 19.4 ms: 1.09x faster                                                                   |
| xml_etree_generate      | 94.1 ms                                                      | 86.1 ms: 1.09x faster                                                                   |
| async_generators        | 419 ms                                                       | 390 ms: 1.07x faster                                                                    |
| xml_etree_iterparse     | 109 ms                                                       | 103 ms: 1.06x faster                                                                    |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                                                    |
| meteor_contest          | 142 ms                                                       | 138 ms: 1.03x faster                                                                    |
| pickle                  | 10.1 us                                                      | 9.94 us: 1.02x faster                                                                   |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                                   |
| gc_traversal            | 3.46 ms                                                      | 3.53 ms: 1.02x slower                                                                   |
| unpickle_list           | 4.73 us                                                      | 4.86 us: 1.03x slower                                                                   |
| pickle_list             | 4.11 us                                                      | 4.42 us: 1.07x slower                                                                   |
| pickle_dict             | 29.5 us                                                      | 32.5 us: 1.10x slower                                                                   |
| unpickle                | 13.3 us                                                      | 14.8 us: 1.12x slower                                                                   |
| regex_effbot            | 2.99 ms                                                      | 3.41 ms: 1.14x slower                                                                   |
| python_startup_no_site  | 7.32 ms                                                      | 8.44 ms: 1.15x slower                                                                   |
| dask                    | 478 ms                                                       | 564 ms: 1.18x slower                                                                    |
| coverage                | 71.1 ms                                                      | 98.7 ms: 1.39x slower                                                                   |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                                            |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
