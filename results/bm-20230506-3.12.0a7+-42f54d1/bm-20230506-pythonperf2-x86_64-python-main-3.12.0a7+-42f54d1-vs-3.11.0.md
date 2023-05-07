
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 289 ms                                                                    | 284 ms: 1.02x faster                                         |
| docutils       | 2.86 sec                                                                  | 2.90 sec: 1.01x slower                                       |
| tornado_http   | 125 ms                                                                    | 116 ms: 1.08x faster                                         |
| Geometric mean | (ref)                                                                     | 1.03x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 75.7 ms                                                                   | 77.6 ms: 1.02x slower                                        |
| pidigits       | 252 ms                                                                    | 260 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                                     | 1.02x slower                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 154 ms                                                                    | 146 ms: 1.05x faster                                         |
| regex_v8       | 24.4 ms                                                                   | 23.9 ms: 1.02x faster                                        |
| regex_effbot   | 3.31 ms                                                                   | 3.42 ms: 1.03x slower                                        |
| regex_dna      | 225 ms                                                                    | 234 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                                     | 1.00x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                                   | 10.2 ms: 1.30x faster                                        |
| json_loads           | 28.4 us                                                                   | 24.2 us: 1.18x faster                                        |
| unpickle_pure_python | 238 us                                                                    | 206 us: 1.16x faster                                         |
| xml_etree_parse      | 161 ms                                                                    | 146 ms: 1.10x faster                                         |
| pickle_dict          | 31.1 us                                                                   | 31.8 us: 1.02x slower                                        |
| xml_etree_process    | 55.8 ms                                                                   | 58.8 ms: 1.05x slower                                        |
| unpickle_list        | 4.52 us                                                                   | 4.81 us: 1.06x slower                                        |
| xml_etree_generate   | 79.1 ms                                                                   | 85.2 ms: 1.08x slower                                        |
| unpickle             | 13.0 us                                                                   | 14.6 us: 1.12x slower                                        |
| pickle_list          | 3.78 us                                                                   | 4.42 us: 1.17x slower                                        |
| Geometric mean       | (ref)                                                                     | 1.02x faster                                                 |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle_pure_python, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                                   | 11.3 ms: 1.05x slower                                        |
| python_startup_no_site | 7.73 ms                                                                   | 8.39 ms: 1.09x slower                                        |
| Geometric mean         | (ref)                                                                     | 1.07x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|-----------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 10.9 ms                                                                   | 10.1 ms: 1.08x faster                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:-------------------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp             | 752 ms                                                                    | 383 ms: 1.96x faster                                         |
| generators              | 56.0 ms                                                                   | 36.6 ms: 1.53x faster                                        |
| coroutines              | 29.5 ms                                                                   | 22.3 ms: 1.32x faster                                        |
| fannkuch                | 449 ms                                                                    | 343 ms: 1.31x faster                                         |
| json_dumps              | 13.4 ms                                                                   | 10.2 ms: 1.30x faster                                        |
| deltablue               | 3.99 ms                                                                   | 3.27 ms: 1.22x faster                                        |
| mypy2                   | 446 ms                                                                    | 373 ms: 1.20x faster                                         |
| hexiom                  | 7.00 ms                                                                   | 5.86 ms: 1.19x faster                                        |
| json_loads              | 28.4 us                                                                   | 24.2 us: 1.18x faster                                        |
| unpickle_pure_python    | 238 us                                                                    | 206 us: 1.16x faster                                         |
| nqueens                 | 101 ms                                                                    | 88.1 ms: 1.14x faster                                        |
| scimark_lu              | 114 ms                                                                    | 100 ms: 1.14x faster                                         |
| chaos                   | 76.2 ms                                                                   | 67.4 ms: 1.13x faster                                        |
| logging_silent          | 103 ns                                                                    | 91.5 ns: 1.12x faster                                        |
| sqlglot_parse           | 1.53 ms                                                                   | 1.38 ms: 1.11x faster                                        |
| async_tree_memoization  | 639 ms                                                                    | 578 ms: 1.11x faster                                         |
| gc_traversal            | 4.22 ms                                                                   | 3.82 ms: 1.10x faster                                        |
| xml_etree_parse         | 161 ms                                                                    | 146 ms: 1.10x faster                                         |
| async_tree_none         | 529 ms                                                                    | 481 ms: 1.10x faster                                         |
| richards                | 49.1 ms                                                                   | 45.0 ms: 1.09x faster                                        |
| mdp                     | 2.73 sec                                                                  | 2.51 sec: 1.09x faster                                       |
| tornado_http            | 125 ms                                                                    | 116 ms: 1.08x faster                                         |
| go                      | 158 ms                                                                    | 147 ms: 1.08x faster                                         |
| mako                    | 10.9 ms                                                                   | 10.1 ms: 1.08x faster                                        |
| async_tree_io           | 1.18 sec                                                                  | 1.10 sec: 1.08x faster                                       |
| json                    | 5.59 ms                                                                   | 5.21 ms: 1.07x faster                                        |
| dulwich_log             | 69.1 ms                                                                   | 65.3 ms: 1.06x faster                                        |
| async_tree_cpu_io_mixed | 754 ms                                                                    | 715 ms: 1.05x faster                                         |
| sqlglot_transpile       | 1.88 ms                                                                   | 1.78 ms: 1.05x faster                                        |
| regex_compile           | 154 ms                                                                    | 146 ms: 1.05x faster                                         |
| pycparser               | 1.30 sec                                                                  | 1.24 sec: 1.05x faster                                       |
| bench_thread_pool       | 990 us                                                                    | 944 us: 1.05x faster                                         |
| logging_format          | 7.84 us                                                                   | 7.56 us: 1.04x faster                                        |
| crypto_pyaes            | 85.0 ms                                                                   | 82.1 ms: 1.03x faster                                        |
| spectral_norm           | 95.1 ms                                                                   | 92.6 ms: 1.03x faster                                        |
| regex_v8                | 24.4 ms                                                                   | 23.9 ms: 1.02x faster                                        |
| deepcopy                | 384 us                                                                    | 375 us: 1.02x faster                                         |
| deepcopy_memo           | 37.0 us                                                                   | 36.2 us: 1.02x faster                                        |
| 2to3                    | 289 ms                                                                    | 284 ms: 1.02x faster                                         |
| sqlglot_normalize       | 122 ms                                                                    | 120 ms: 1.02x faster                                         |
| comprehensions          | 24.7 us                                                                   | 24.4 us: 1.01x faster                                        |
| logging_simple          | 6.95 us                                                                   | 6.87 us: 1.01x faster                                        |
| meteor_contest          | 129 ms                                                                    | 129 ms: 1.00x faster                                         |
| sqlglot_optimize        | 58.6 ms                                                                   | 58.8 ms: 1.00x slower                                        |
| raytrace                | 303 ms                                                                    | 307 ms: 1.01x slower                                         |
| docutils                | 2.86 sec                                                                  | 2.90 sec: 1.01x slower                                       |
| pprint_pformat          | 1.60 sec                                                                  | 1.62 sec: 1.01x slower                                       |
| pickle_dict             | 31.1 us                                                                   | 31.8 us: 1.02x slower                                        |
| float                   | 75.7 ms                                                                   | 77.6 ms: 1.02x slower                                        |
| scimark_sor             | 109 ms                                                                    | 112 ms: 1.03x slower                                         |
| regex_effbot            | 3.31 ms                                                                   | 3.42 ms: 1.03x slower                                        |
| pidigits                | 252 ms                                                                    | 260 ms: 1.04x slower                                         |
| pprint_safe_repr        | 768 ms                                                                    | 798 ms: 1.04x slower                                         |
| regex_dna               | 225 ms                                                                    | 234 ms: 1.04x slower                                         |
| pathlib                 | 19.2 ms                                                                   | 20.0 ms: 1.04x slower                                        |
| scimark_sparse_mat_mult | 4.06 ms                                                                   | 4.26 ms: 1.05x slower                                        |
| python_startup          | 10.7 ms                                                                   | 11.3 ms: 1.05x slower                                        |
| xml_etree_process       | 55.8 ms                                                                   | 58.8 ms: 1.05x slower                                        |
| sqlite_synth            | 2.49 us                                                                   | 2.63 us: 1.06x slower                                        |
| scimark_monte_carlo     | 67.8 ms                                                                   | 71.7 ms: 1.06x slower                                        |
| unpickle_list           | 4.52 us                                                                   | 4.81 us: 1.06x slower                                        |
| xml_etree_generate      | 79.1 ms                                                                   | 85.2 ms: 1.08x slower                                        |
| coverage                | 86.0 ms                                                                   | 92.9 ms: 1.08x slower                                        |
| python_startup_no_site  | 7.73 ms                                                                   | 8.39 ms: 1.09x slower                                        |
| telco                   | 6.70 ms                                                                   | 7.27 ms: 1.09x slower                                        |
| scimark_fft             | 276 ms                                                                    | 300 ms: 1.09x slower                                         |
| unpack_sequence         | 45.9 ns                                                                   | 50.1 ns: 1.09x slower                                        |
| bench_mp_pool           | 4.54 ms                                                                   | 4.98 ms: 1.10x slower                                        |
| unpickle                | 13.0 us                                                                   | 14.6 us: 1.12x slower                                        |
| pickle_list             | 3.78 us                                                                   | 4.42 us: 1.17x slower                                        |
| async_generators        | 318 ms                                                                    | 392 ms: 1.23x slower                                         |
| dask                    | 418 ms                                                                    | 560 ms: 1.34x slower                                         |
| Geometric mean          | (ref)                                                                     | 1.04x faster                                                 |

Benchmark hidden because not significant (7): create_gc_cycles, xml_etree_iterparse, deepcopy_reduce, nbody, pickle_pure_python, pyflate, pickle
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
