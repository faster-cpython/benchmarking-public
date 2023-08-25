
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.27x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                                    |
| docutils       | 3.40 sec                                                     | 2.88 sec: 1.18x faster                                                                  |
| tornado_http   | 152 ms                                                       | 114 ms: 1.34x faster                                                                    |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 85.2 ms: 1.61x faster                                                                   |
| float          | 110 ms                                                       | 78.5 ms: 1.40x faster                                                                   |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                                    |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 145 ms: 1.33x faster                                                                    |
| regex_v8       | 26.6 ms                                                      | 23.4 ms: 1.14x faster                                                                   |
| regex_dna      | 259 ms                                                       | 228 ms: 1.14x faster                                                                    |
| regex_effbot   | 2.99 ms                                                      | 3.41 ms: 1.14x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 206 us: 1.56x faster                                                                    |
| pickle_pure_python   | 457 us                                                       | 318 us: 1.44x faster                                                                    |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.37x faster                                                                   |
| xml_etree_process    | 76.0 ms                                                      | 59.1 ms: 1.29x faster                                                                   |
| json_loads           | 30.0 us                                                      | 24.3 us: 1.24x faster                                                                   |
| xml_etree_parse      | 162 ms                                                       | 144 ms: 1.12x faster                                                                    |
| xml_etree_generate   | 94.6 ms                                                      | 86.1 ms: 1.10x faster                                                                   |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                                                    |
| unpickle             | 14.2 us                                                      | 14.8 us: 1.05x slower                                                                   |
| pickle_list          | 4.11 us                                                      | 4.42 us: 1.07x slower                                                                   |
| unpickle_list        | 4.49 us                                                      | 4.86 us: 1.08x slower                                                                   |
| pickle_dict          | 30.0 us                                                      | 32.5 us: 1.08x slower                                                                   |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                            |

Benchmark hidden because not significant (1): pickle

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
| deltablue               | 7.47 ms                                                      | 3.23 ms: 2.32x faster                                                                   |
| asyncio_tcp             | 782 ms                                                       | 381 ms: 2.06x faster                                                                    |
| go                      | 259 ms                                                       | 144 ms: 1.80x faster                                                                    |
| logging_silent          | 166 ns                                                       | 92.8 ns: 1.79x faster                                                                   |
| richards                | 74.1 ms                                                      | 43.8 ms: 1.69x faster                                                                   |
| scimark_lu              | 164 ms                                                       | 99.3 ms: 1.65x faster                                                                   |
| sqlglot_parse           | 2.26 ms                                                      | 1.39 ms: 1.62x faster                                                                   |
| hexiom                  | 9.52 ms                                                      | 5.90 ms: 1.61x faster                                                                   |
| nbody                   | 137 ms                                                       | 85.2 ms: 1.61x faster                                                                   |
| chaos                   | 107 ms                                                       | 66.6 ms: 1.61x faster                                                                   |
| raytrace                | 488 ms                                                       | 308 ms: 1.58x faster                                                                    |
| generators              | 58.0 ms                                                      | 36.6 ms: 1.58x faster                                                                   |
| pyflate                 | 697 ms                                                       | 443 ms: 1.57x faster                                                                    |
| scimark_sor             | 177 ms                                                       | 113 ms: 1.57x faster                                                                    |
| unpickle_pure_python    | 321 us                                                       | 206 us: 1.56x faster                                                                    |
| scimark_monte_carlo     | 109 ms                                                       | 70.7 ms: 1.55x faster                                                                   |
| sqlglot_transpile       | 2.71 ms                                                      | 1.79 ms: 1.51x faster                                                                   |
| spectral_norm           | 136 ms                                                       | 91.2 ms: 1.49x faster                                                                   |
| crypto_pyaes            | 118 ms                                                       | 80.2 ms: 1.47x faster                                                                   |
| bench_mp_pool           | 7.18 ms                                                      | 4.87 ms: 1.47x faster                                                                   |
| mako                    | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                                                   |
| async_tree_io           | 1.61 sec                                                     | 1.10 sec: 1.46x faster                                                                  |
| async_tree_none         | 700 ms                                                       | 479 ms: 1.46x faster                                                                    |
| pickle_pure_python      | 457 us                                                       | 318 us: 1.44x faster                                                                    |
| async_tree_memoization  | 824 ms                                                       | 575 ms: 1.43x faster                                                                    |
| fannkuch                | 496 ms                                                       | 347 ms: 1.43x faster                                                                    |
| float                   | 110 ms                                                       | 78.5 ms: 1.40x faster                                                                   |
| deepcopy_memo           | 48.9 us                                                      | 35.5 us: 1.38x faster                                                                   |
| json_dumps              | 14.2 ms                                                      | 10.3 ms: 1.37x faster                                                                   |
| coroutines              | 30.4 ms                                                      | 22.4 ms: 1.36x faster                                                                   |
| pycparser               | 1.66 sec                                                     | 1.23 sec: 1.35x faster                                                                  |
| logging_simple          | 8.90 us                                                      | 6.60 us: 1.35x faster                                                                   |
| tornado_http            | 152 ms                                                       | 114 ms: 1.34x faster                                                                    |
| pprint_pformat          | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                                  |
| async_tree_cpu_io_mixed | 952 ms                                                       | 712 ms: 1.34x faster                                                                    |
| regex_compile           | 194 ms                                                       | 145 ms: 1.33x faster                                                                    |
| pprint_safe_repr        | 1.05 sec                                                     | 793 ms: 1.32x faster                                                                    |
| logging_format          | 9.57 us                                                      | 7.39 us: 1.29x faster                                                                   |
| unpack_sequence         | 59.5 ns                                                      | 46.0 ns: 1.29x faster                                                                   |
| xml_etree_process       | 76.0 ms                                                      | 59.1 ms: 1.29x faster                                                                   |
| nqueens                 | 112 ms                                                       | 90.7 ms: 1.24x faster                                                                   |
| json_loads              | 30.0 us                                                      | 24.3 us: 1.24x faster                                                                   |
| mypy2                   | 466 ms                                                       | 378 ms: 1.23x faster                                                                    |
| 2to3                    | 350 ms                                                       | 286 ms: 1.22x faster                                                                    |
| dulwich_log             | 80.1 ms                                                      | 65.6 ms: 1.22x faster                                                                   |
| deepcopy                | 454 us                                                       | 376 us: 1.21x faster                                                                    |
| scimark_fft             | 359 ms                                                       | 299 ms: 1.20x faster                                                                    |
| sqlglot_normalize       | 144 ms                                                       | 121 ms: 1.19x faster                                                                    |
| deepcopy_reduce         | 4.03 us                                                      | 3.38 us: 1.19x faster                                                                   |
| mdp                     | 3.03 sec                                                     | 2.55 sec: 1.19x faster                                                                  |
| sqlglot_optimize        | 70.3 ms                                                      | 59.3 ms: 1.19x faster                                                                   |
| docutils                | 3.40 sec                                                     | 2.88 sec: 1.18x faster                                                                  |
| bench_thread_pool       | 1.14 ms                                                      | 971 us: 1.17x faster                                                                    |
| json                    | 5.96 ms                                                      | 5.12 ms: 1.16x faster                                                                   |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.47 ms: 1.16x faster                                                                   |
| create_gc_cycles        | 1.82 ms                                                      | 1.60 ms: 1.14x faster                                                                   |
| regex_v8                | 26.6 ms                                                      | 23.4 ms: 1.14x faster                                                                   |
| regex_dna               | 259 ms                                                       | 228 ms: 1.14x faster                                                                    |
| xml_etree_parse         | 162 ms                                                       | 144 ms: 1.12x faster                                                                    |
| sqlite_synth            | 2.97 us                                                      | 2.65 us: 1.12x faster                                                                   |
| pathlib                 | 21.7 ms                                                      | 19.4 ms: 1.12x faster                                                                   |
| comprehensions          | 26.9 us                                                      | 24.4 us: 1.10x faster                                                                   |
| xml_etree_generate      | 94.6 ms                                                      | 86.1 ms: 1.10x faster                                                                   |
| async_generators        | 422 ms                                                       | 390 ms: 1.08x faster                                                                    |
| xml_etree_iterparse     | 110 ms                                                       | 103 ms: 1.07x faster                                                                    |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                                                    |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                                   |
| meteor_contest          | 137 ms                                                       | 138 ms: 1.01x slower                                                                    |
| gc_traversal            | 3.45 ms                                                      | 3.53 ms: 1.02x slower                                                                   |
| unpickle                | 14.2 us                                                      | 14.8 us: 1.05x slower                                                                   |
| pickle_list             | 4.11 us                                                      | 4.42 us: 1.07x slower                                                                   |
| unpickle_list           | 4.49 us                                                      | 4.86 us: 1.08x slower                                                                   |
| pickle_dict             | 30.0 us                                                      | 32.5 us: 1.08x slower                                                                   |
| regex_effbot            | 2.99 ms                                                      | 3.41 ms: 1.14x slower                                                                   |
| python_startup_no_site  | 7.32 ms                                                      | 8.44 ms: 1.15x slower                                                                   |
| dask                    | 463 ms                                                       | 564 ms: 1.22x slower                                                                    |
| coverage                | 64.0 ms                                                      | 98.7 ms: 1.54x slower                                                                   |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                                            |

Benchmark hidden because not significant (2): telco, pickle
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x
