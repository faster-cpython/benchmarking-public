
# Results vs. 3.11.0

- fork: python
- ref: e629ab6adf19544d5ee3
- machine: linux-x86_64
- commit hash: e629ab6
- commit date: 2023-05-11
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                    | 283 ms: 1.02x faster                                                         |
| docutils       | 2.86 sec                                                                  | 2.88 sec: 1.01x slower                                                       |
| tornado_http   | 125 ms                                                                    | 114 ms: 1.10x faster                                                         |
| Geometric mean | (ref)                                                                     | 1.04x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                                   | 84.2 ms: 1.09x faster                                                        |
| pidigits       | 252 ms                                                                    | 260 ms: 1.03x slower                                                         |
| float          | 75.7 ms                                                                   | 79.9 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                     | 1.00x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 154 ms                                                                    | 145 ms: 1.06x faster                                                         |
| regex_v8       | 24.4 ms                                                                   | 24.3 ms: 1.00x faster                                                        |
| regex_dna      | 225 ms                                                                    | 234 ms: 1.04x slower                                                         |
| regex_effbot   | 3.31 ms                                                                   | 3.55 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                                     | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|----------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                                   | 10.3 ms: 1.30x faster                                                        |
| json_loads           | 28.4 us                                                                   | 24.5 us: 1.16x faster                                                        |
| unpickle_pure_python | 238 us                                                                    | 206 us: 1.16x faster                                                         |
| xml_etree_parse      | 161 ms                                                                    | 150 ms: 1.07x faster                                                         |
| pickle_pure_python   | 319 us                                                                    | 323 us: 1.01x slower                                                         |
| pickle               | 9.92 us                                                                   | 10.0 us: 1.01x slower                                                        |
| pickle_dict          | 31.1 us                                                                   | 31.9 us: 1.02x slower                                                        |
| xml_etree_process    | 55.8 ms                                                                   | 59.0 ms: 1.06x slower                                                        |
| unpickle_list        | 4.52 us                                                                   | 4.81 us: 1.06x slower                                                        |
| xml_etree_generate   | 79.1 ms                                                                   | 86.0 ms: 1.09x slower                                                        |
| unpickle             | 13.0 us                                                                   | 14.8 us: 1.14x slower                                                        |
| pickle_list          | 3.78 us                                                                   | 4.33 us: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                                     | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|------------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                                   | 11.3 ms: 1.05x slower                                                        |
| python_startup_no_site | 7.73 ms                                                                   | 8.43 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                                     | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|-----------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako      | 10.9 ms                                                                   | 9.84 ms: 1.11x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|-------------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 752 ms                                                                    | 379 ms: 1.99x faster                                                         |
| generators              | 56.0 ms                                                                   | 36.5 ms: 1.53x faster                                                        |
| fannkuch                | 449 ms                                                                    | 345 ms: 1.30x faster                                                         |
| json_dumps              | 13.4 ms                                                                   | 10.3 ms: 1.30x faster                                                        |
| coroutines              | 29.5 ms                                                                   | 22.8 ms: 1.29x faster                                                        |
| deltablue               | 3.99 ms                                                                   | 3.25 ms: 1.23x faster                                                        |
| mypy2                   | 446 ms                                                                    | 367 ms: 1.21x faster                                                         |
| hexiom                  | 7.00 ms                                                                   | 5.85 ms: 1.20x faster                                                        |
| chaos                   | 76.2 ms                                                                   | 64.8 ms: 1.18x faster                                                        |
| async_tree_memoization  | 639 ms                                                                    | 549 ms: 1.16x faster                                                         |
| async_tree_none         | 529 ms                                                                    | 456 ms: 1.16x faster                                                         |
| json_loads              | 28.4 us                                                                   | 24.5 us: 1.16x faster                                                        |
| unpickle_pure_python    | 238 us                                                                    | 206 us: 1.16x faster                                                         |
| scimark_lu              | 114 ms                                                                    | 99.4 ms: 1.15x faster                                                        |
| async_tree_io           | 1.18 sec                                                                  | 1.05 sec: 1.13x faster                                                       |
| comprehensions          | 24.7 us                                                                   | 22.0 us: 1.13x faster                                                        |
| sqlglot_parse           | 1.53 ms                                                                   | 1.38 ms: 1.11x faster                                                        |
| mako                    | 10.9 ms                                                                   | 9.84 ms: 1.11x faster                                                        |
| tornado_http            | 125 ms                                                                    | 114 ms: 1.10x faster                                                         |
| nbody                   | 92.1 ms                                                                   | 84.2 ms: 1.09x faster                                                        |
| richards                | 49.1 ms                                                                   | 44.9 ms: 1.09x faster                                                        |
| nqueens                 | 101 ms                                                                    | 92.8 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed | 754 ms                                                                    | 697 ms: 1.08x faster                                                         |
| json                    | 5.59 ms                                                                   | 5.18 ms: 1.08x faster                                                        |
| logging_format          | 7.84 us                                                                   | 7.30 us: 1.07x faster                                                        |
| xml_etree_parse         | 161 ms                                                                    | 150 ms: 1.07x faster                                                         |
| logging_silent          | 103 ns                                                                    | 96.0 ns: 1.07x faster                                                        |
| regex_compile           | 154 ms                                                                    | 145 ms: 1.06x faster                                                         |
| crypto_pyaes            | 85.0 ms                                                                   | 80.2 ms: 1.06x faster                                                        |
| sqlglot_transpile       | 1.88 ms                                                                   | 1.78 ms: 1.06x faster                                                        |
| mdp                     | 2.73 sec                                                                  | 2.58 sec: 1.05x faster                                                       |
| dulwich_log             | 69.1 ms                                                                   | 65.7 ms: 1.05x faster                                                        |
| spectral_norm           | 95.1 ms                                                                   | 90.5 ms: 1.05x faster                                                        |
| logging_simple          | 6.95 us                                                                   | 6.66 us: 1.04x faster                                                        |
| sqlglot_normalize       | 122 ms                                                                    | 117 ms: 1.04x faster                                                         |
| gc_traversal            | 4.22 ms                                                                   | 4.06 ms: 1.04x faster                                                        |
| go                      | 158 ms                                                                    | 152 ms: 1.04x faster                                                         |
| bench_thread_pool       | 990 us                                                                    | 960 us: 1.03x faster                                                         |
| 2to3                    | 289 ms                                                                    | 283 ms: 1.02x faster                                                         |
| raytrace                | 303 ms                                                                    | 297 ms: 1.02x faster                                                         |
| pycparser               | 1.30 sec                                                                  | 1.28 sec: 1.02x faster                                                       |
| deepcopy                | 384 us                                                                    | 376 us: 1.02x faster                                                         |
| deepcopy_memo           | 37.0 us                                                                   | 36.4 us: 1.02x faster                                                        |
| regex_v8                | 24.4 ms                                                                   | 24.3 ms: 1.00x faster                                                        |
| meteor_contest          | 129 ms                                                                    | 129 ms: 1.00x faster                                                         |
| docutils                | 2.86 sec                                                                  | 2.88 sec: 1.01x slower                                                       |
| pickle_pure_python      | 319 us                                                                    | 323 us: 1.01x slower                                                         |
| pickle                  | 9.92 us                                                                   | 10.0 us: 1.01x slower                                                        |
| pyflate                 | 438 ms                                                                    | 444 ms: 1.02x slower                                                         |
| scimark_sor             | 109 ms                                                                    | 111 ms: 1.02x slower                                                         |
| pickle_dict             | 31.1 us                                                                   | 31.9 us: 1.02x slower                                                        |
| pidigits                | 252 ms                                                                    | 260 ms: 1.03x slower                                                         |
| regex_dna               | 225 ms                                                                    | 234 ms: 1.04x slower                                                         |
| pprint_pformat          | 1.60 sec                                                                  | 1.66 sec: 1.04x slower                                                       |
| python_startup          | 10.7 ms                                                                   | 11.3 ms: 1.05x slower                                                        |
| float                   | 75.7 ms                                                                   | 79.9 ms: 1.06x slower                                                        |
| xml_etree_process       | 55.8 ms                                                                   | 59.0 ms: 1.06x slower                                                        |
| pprint_safe_repr        | 768 ms                                                                    | 813 ms: 1.06x slower                                                         |
| telco                   | 6.70 ms                                                                   | 7.11 ms: 1.06x slower                                                        |
| sqlite_synth            | 2.49 us                                                                   | 2.64 us: 1.06x slower                                                        |
| unpickle_list           | 4.52 us                                                                   | 4.81 us: 1.06x slower                                                        |
| regex_effbot            | 3.31 ms                                                                   | 3.55 ms: 1.07x slower                                                        |
| pathlib                 | 19.2 ms                                                                   | 20.7 ms: 1.08x slower                                                        |
| scimark_monte_carlo     | 67.8 ms                                                                   | 73.6 ms: 1.09x slower                                                        |
| scimark_sparse_mat_mult | 4.06 ms                                                                   | 4.41 ms: 1.09x slower                                                        |
| xml_etree_generate      | 79.1 ms                                                                   | 86.0 ms: 1.09x slower                                                        |
| python_startup_no_site  | 7.73 ms                                                                   | 8.43 ms: 1.09x slower                                                        |
| scimark_fft             | 276 ms                                                                    | 302 ms: 1.09x slower                                                         |
| coverage                | 86.0 ms                                                                   | 94.6 ms: 1.10x slower                                                        |
| unpickle                | 13.0 us                                                                   | 14.8 us: 1.14x slower                                                        |
| pickle_list             | 3.78 us                                                                   | 4.33 us: 1.15x slower                                                        |
| unpack_sequence         | 45.9 ns                                                                   | 52.9 ns: 1.15x slower                                                        |
| async_generators        | 318 ms                                                                    | 385 ms: 1.21x slower                                                         |
| bench_mp_pool           | 4.54 ms                                                                   | 5.93 ms: 1.31x slower                                                        |
| dask                    | 418 ms                                                                    | 562 ms: 1.34x slower                                                         |
| Geometric mean          | (ref)                                                                     | 1.04x faster                                                                 |

Benchmark hidden because not significant (4): create_gc_cycles, sqlglot_optimize, xml_etree_iterparse, deepcopy_reduce
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
