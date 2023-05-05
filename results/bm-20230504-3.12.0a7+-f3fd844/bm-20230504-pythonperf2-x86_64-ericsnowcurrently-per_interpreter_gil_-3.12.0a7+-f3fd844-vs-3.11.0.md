
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                    | 286 ms: 1.01x faster                                                                    |
| docutils       | 2.86 sec                                                                  | 2.88 sec: 1.01x slower                                                                  |
| tornado_http   | 125 ms                                                                    | 114 ms: 1.10x faster                                                                    |
| Geometric mean | (ref)                                                                     | 1.03x faster                                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                                   | 85.2 ms: 1.08x faster                                                                   |
| pidigits       | 252 ms                                                                    | 260 ms: 1.03x slower                                                                    |
| float          | 75.7 ms                                                                   | 78.5 ms: 1.04x slower                                                                   |
| Geometric mean | (ref)                                                                     | 1.00x faster                                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| regex_compile  | 154 ms                                                                    | 145 ms: 1.06x faster                                                                    |
| regex_v8       | 24.4 ms                                                                   | 23.4 ms: 1.04x faster                                                                   |
| regex_dna      | 225 ms                                                                    | 228 ms: 1.01x slower                                                                    |
| regex_effbot   | 3.31 ms                                                                   | 3.41 ms: 1.03x slower                                                                   |
| Geometric mean | (ref)                                                                     | 1.01x faster                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                                   | 10.3 ms: 1.29x faster                                                                   |
| json_loads           | 28.4 us                                                                   | 24.3 us: 1.17x faster                                                                   |
| unpickle_pure_python | 238 us                                                                    | 206 us: 1.16x faster                                                                    |
| xml_etree_parse      | 161 ms                                                                    | 144 ms: 1.11x faster                                                                    |
| xml_etree_iterparse  | 106 ms                                                                    | 103 ms: 1.02x faster                                                                    |
| pickle_pure_python   | 319 us                                                                    | 318 us: 1.01x faster                                                                    |
| pickle_dict          | 31.1 us                                                                   | 32.5 us: 1.04x slower                                                                   |
| xml_etree_process    | 55.8 ms                                                                   | 59.1 ms: 1.06x slower                                                                   |
| unpickle_list        | 4.52 us                                                                   | 4.86 us: 1.08x slower                                                                   |
| xml_etree_generate   | 79.1 ms                                                                   | 86.1 ms: 1.09x slower                                                                   |
| unpickle             | 13.0 us                                                                   | 14.8 us: 1.14x slower                                                                   |
| pickle_list          | 3.78 us                                                                   | 4.42 us: 1.17x slower                                                                   |
| Geometric mean       | (ref)                                                                     | 1.01x faster                                                                            |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                                   | 11.3 ms: 1.05x slower                                                                   |
| python_startup_no_site | 7.73 ms                                                                   | 8.44 ms: 1.09x slower                                                                   |
| Geometric mean         | (ref)                                                                     | 1.07x slower                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| mako      | 10.9 ms                                                                   | 10.0 ms: 1.09x faster                                                                   |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| asyncio_tcp             | 752 ms                                                                    | 381 ms: 1.98x faster                                                                    |
| generators              | 56.0 ms                                                                   | 36.6 ms: 1.53x faster                                                                   |
| coroutines              | 29.5 ms                                                                   | 22.4 ms: 1.31x faster                                                                   |
| fannkuch                | 449 ms                                                                    | 347 ms: 1.29x faster                                                                    |
| json_dumps              | 13.4 ms                                                                   | 10.3 ms: 1.29x faster                                                                   |
| deltablue               | 3.99 ms                                                                   | 3.23 ms: 1.24x faster                                                                   |
| gc_traversal            | 4.22 ms                                                                   | 3.53 ms: 1.20x faster                                                                   |
| hexiom                  | 7.00 ms                                                                   | 5.90 ms: 1.19x faster                                                                   |
| mypy2                   | 446 ms                                                                    | 378 ms: 1.18x faster                                                                    |
| json_loads              | 28.4 us                                                                   | 24.3 us: 1.17x faster                                                                   |
| unpickle_pure_python    | 238 us                                                                    | 206 us: 1.16x faster                                                                    |
| scimark_lu              | 114 ms                                                                    | 99.3 ms: 1.15x faster                                                                   |
| chaos                   | 76.2 ms                                                                   | 66.6 ms: 1.14x faster                                                                   |
| richards                | 49.1 ms                                                                   | 43.8 ms: 1.12x faster                                                                   |
| xml_etree_parse         | 161 ms                                                                    | 144 ms: 1.11x faster                                                                    |
| nqueens                 | 101 ms                                                                    | 90.7 ms: 1.11x faster                                                                   |
| async_tree_memoization  | 639 ms                                                                    | 575 ms: 1.11x faster                                                                    |
| logging_silent          | 103 ns                                                                    | 92.8 ns: 1.11x faster                                                                   |
| async_tree_none         | 529 ms                                                                    | 479 ms: 1.10x faster                                                                    |
| tornado_http            | 125 ms                                                                    | 114 ms: 1.10x faster                                                                    |
| go                      | 158 ms                                                                    | 144 ms: 1.10x faster                                                                    |
| sqlglot_parse           | 1.53 ms                                                                   | 1.39 ms: 1.10x faster                                                                   |
| json                    | 5.59 ms                                                                   | 5.12 ms: 1.09x faster                                                                   |
| mako                    | 10.9 ms                                                                   | 10.0 ms: 1.09x faster                                                                   |
| nbody                   | 92.1 ms                                                                   | 85.2 ms: 1.08x faster                                                                   |
| async_tree_io           | 1.18 sec                                                                  | 1.10 sec: 1.08x faster                                                                  |
| mdp                     | 2.73 sec                                                                  | 2.55 sec: 1.07x faster                                                                  |
| logging_format          | 7.84 us                                                                   | 7.39 us: 1.06x faster                                                                   |
| regex_compile           | 154 ms                                                                    | 145 ms: 1.06x faster                                                                    |
| crypto_pyaes            | 85.0 ms                                                                   | 80.2 ms: 1.06x faster                                                                   |
| async_tree_cpu_io_mixed | 754 ms                                                                    | 712 ms: 1.06x faster                                                                    |
| pycparser               | 1.30 sec                                                                  | 1.23 sec: 1.06x faster                                                                  |
| dulwich_log             | 69.1 ms                                                                   | 65.6 ms: 1.05x faster                                                                   |
| logging_simple          | 6.95 us                                                                   | 6.60 us: 1.05x faster                                                                   |
| sqlglot_transpile       | 1.88 ms                                                                   | 1.79 ms: 1.05x faster                                                                   |
| regex_v8                | 24.4 ms                                                                   | 23.4 ms: 1.04x faster                                                                   |
| spectral_norm           | 95.1 ms                                                                   | 91.2 ms: 1.04x faster                                                                   |
| deepcopy_memo           | 37.0 us                                                                   | 35.5 us: 1.04x faster                                                                   |
| create_gc_cycles        | 1.65 ms                                                                   | 1.60 ms: 1.03x faster                                                                   |
| xml_etree_iterparse     | 106 ms                                                                    | 103 ms: 1.02x faster                                                                    |
| deepcopy                | 384 us                                                                    | 376 us: 1.02x faster                                                                    |
| 2to3                    | 289 ms                                                                    | 286 ms: 1.01x faster                                                                    |
| comprehensions          | 24.7 us                                                                   | 24.4 us: 1.01x faster                                                                   |
| sqlglot_normalize       | 122 ms                                                                    | 121 ms: 1.01x faster                                                                    |
| pickle_pure_python      | 319 us                                                                    | 318 us: 1.01x faster                                                                    |
| docutils                | 2.86 sec                                                                  | 2.88 sec: 1.01x slower                                                                  |
| pprint_pformat          | 1.60 sec                                                                  | 1.61 sec: 1.01x slower                                                                  |
| pyflate                 | 438 ms                                                                    | 443 ms: 1.01x slower                                                                    |
| sqlglot_optimize        | 58.6 ms                                                                   | 59.3 ms: 1.01x slower                                                                   |
| pathlib                 | 19.2 ms                                                                   | 19.4 ms: 1.01x slower                                                                   |
| regex_dna               | 225 ms                                                                    | 228 ms: 1.01x slower                                                                    |
| raytrace                | 303 ms                                                                    | 308 ms: 1.02x slower                                                                    |
| regex_effbot            | 3.31 ms                                                                   | 3.41 ms: 1.03x slower                                                                   |
| pprint_safe_repr        | 768 ms                                                                    | 793 ms: 1.03x slower                                                                    |
| pidigits                | 252 ms                                                                    | 260 ms: 1.03x slower                                                                    |
| scimark_sor             | 109 ms                                                                    | 113 ms: 1.04x slower                                                                    |
| float                   | 75.7 ms                                                                   | 78.5 ms: 1.04x slower                                                                   |
| scimark_monte_carlo     | 67.8 ms                                                                   | 70.7 ms: 1.04x slower                                                                   |
| pickle_dict             | 31.1 us                                                                   | 32.5 us: 1.04x slower                                                                   |
| python_startup          | 10.7 ms                                                                   | 11.3 ms: 1.05x slower                                                                   |
| xml_etree_process       | 55.8 ms                                                                   | 59.1 ms: 1.06x slower                                                                   |
| telco                   | 6.70 ms                                                                   | 7.11 ms: 1.06x slower                                                                   |
| sqlite_synth            | 2.49 us                                                                   | 2.65 us: 1.07x slower                                                                   |
| meteor_contest          | 129 ms                                                                    | 138 ms: 1.07x slower                                                                    |
| bench_mp_pool           | 4.54 ms                                                                   | 4.87 ms: 1.07x slower                                                                   |
| unpickle_list           | 4.52 us                                                                   | 4.86 us: 1.08x slower                                                                   |
| scimark_fft             | 276 ms                                                                    | 299 ms: 1.08x slower                                                                    |
| xml_etree_generate      | 79.1 ms                                                                   | 86.1 ms: 1.09x slower                                                                   |
| python_startup_no_site  | 7.73 ms                                                                   | 8.44 ms: 1.09x slower                                                                   |
| scimark_sparse_mat_mult | 4.06 ms                                                                   | 4.47 ms: 1.10x slower                                                                   |
| unpickle                | 13.0 us                                                                   | 14.8 us: 1.14x slower                                                                   |
| coverage                | 86.0 ms                                                                   | 98.7 ms: 1.15x slower                                                                   |
| pickle_list             | 3.78 us                                                                   | 4.42 us: 1.17x slower                                                                   |
| async_generators        | 318 ms                                                                    | 390 ms: 1.23x slower                                                                    |
| dask                    | 418 ms                                                                    | 564 ms: 1.35x slower                                                                    |
| Geometric mean          | (ref)                                                                     | 1.04x faster                                                                            |

Benchmark hidden because not significant (4): bench_thread_pool, deepcopy_reduce, unpack_sequence, pickle
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
