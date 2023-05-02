
# Results vs. 3.11.0

- fork: python
- ref: f73abf8e03fd370c86fb
- machine: linux-x86_64
- commit hash: f73abf8
- commit date: 2023-05-01
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 268 ms: 1.04x slower                                                   |
| docutils       | 2.59 sec                                                            | 2.71 sec: 1.05x slower                                                 |
| tornado_http   | 96.7 ms                                                             | 98.5 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                               | 1.03x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 89.2 ms: 1.08x faster                                                  |
| pidigits       | 197 ms                                                              | 198 ms: 1.00x slower                                                   |
| float          | 76.0 ms                                                             | 82.0 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                               | 1.00x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.1 ms: 1.01x slower                                                  |
| regex_effbot   | 3.32 ms                                                             | 3.44 ms: 1.04x slower                                                  |
| regex_compile  | 137 ms                                                              | 144 ms: 1.05x slower                                                   |
| regex_dna      | 196 ms                                                              | 210 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                               | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 10.1 ms: 1.25x faster                                                  |
| xml_etree_parse      | 162 ms                                                              | 152 ms: 1.06x faster                                                   |
| unpickle_pure_python | 228 us                                                              | 217 us: 1.05x faster                                                   |
| xml_etree_iterparse  | 108 ms                                                              | 103 ms: 1.05x faster                                                   |
| json_loads           | 26.2 us                                                             | 25.8 us: 1.01x faster                                                  |
| pickle_pure_python   | 307 us                                                              | 319 us: 1.04x slower                                                   |
| pickle_dict          | 30.9 us                                                             | 32.3 us: 1.04x slower                                                  |
| unpickle_list        | 4.96 us                                                             | 5.19 us: 1.05x slower                                                  |
| pickle               | 9.79 us                                                             | 10.3 us: 1.05x slower                                                  |
| xml_etree_process    | 54.1 ms                                                             | 58.2 ms: 1.07x slower                                                  |
| xml_etree_generate   | 76.5 ms                                                             | 84.0 ms: 1.10x slower                                                  |
| pickle_list          | 4.03 us                                                             | 4.79 us: 1.19x slower                                                  |
| unpickle             | 13.2 us                                                             | 15.7 us: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.06 ms: 1.07x slower                                                  |
| python_startup_no_site | 5.98 ms                                                             | 6.65 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                             | 50.5 ms: 1.02x faster                                                  |
| genshi_text    | 21.8 ms                                                             | 22.7 ms: 1.04x slower                                                  |
| mako           | 9.82 ms                                                             | 10.8 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                               | 1.04x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 31.0 ms: 2.37x faster                                                  |
| asyncio_tcp             | 888 ms                                                              | 511 ms: 1.74x faster                                                   |
| json_dumps              | 12.5 ms                                                             | 10.1 ms: 1.25x faster                                                  |
| mypy2                   | 422 ms                                                              | 349 ms: 1.21x faster                                                   |
| coroutines              | 26.3 ms                                                             | 23.0 ms: 1.14x faster                                                  |
| nbody                   | 96.7 ms                                                             | 89.2 ms: 1.08x faster                                                  |
| xml_etree_parse         | 162 ms                                                              | 152 ms: 1.06x faster                                                   |
| richards                | 45.7 ms                                                             | 43.3 ms: 1.06x faster                                                  |
| unpickle_pure_python    | 228 us                                                              | 217 us: 1.05x faster                                                   |
| async_tree_none         | 525 ms                                                              | 499 ms: 1.05x faster                                                   |
| nqueens                 | 84.0 ms                                                             | 80.1 ms: 1.05x faster                                                  |
| xml_etree_iterparse     | 108 ms                                                              | 103 ms: 1.05x faster                                                   |
| async_tree_io           | 1.28 sec                                                            | 1.23 sec: 1.04x faster                                                 |
| hexiom                  | 6.48 ms                                                             | 6.22 ms: 1.04x faster                                                  |
| unpack_sequence         | 49.5 ns                                                             | 47.5 ns: 1.04x faster                                                  |
| deltablue               | 3.66 ms                                                             | 3.54 ms: 1.03x faster                                                  |
| pathlib                 | 18.2 ms                                                             | 17.7 ms: 1.03x faster                                                  |
| fannkuch                | 384 ms                                                              | 374 ms: 1.02x faster                                                   |
| sqlglot_parse           | 1.36 ms                                                             | 1.33 ms: 1.02x faster                                                  |
| genshi_xml              | 51.8 ms                                                             | 50.5 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                              | 722 ms: 1.02x faster                                                   |
| go                      | 138 ms                                                              | 136 ms: 1.01x faster                                                   |
| json_loads              | 26.2 us                                                             | 25.8 us: 1.01x faster                                                  |
| mdp                     | 2.64 sec                                                            | 2.61 sec: 1.01x faster                                                 |
| async_tree_memoization  | 621 ms                                                              | 614 ms: 1.01x faster                                                   |
| pidigits                | 197 ms                                                              | 198 ms: 1.00x slower                                                   |
| create_gc_cycles        | 1.48 ms                                                             | 1.49 ms: 1.01x slower                                                  |
| regex_v8                | 22.0 ms                                                             | 22.1 ms: 1.01x slower                                                  |
| chaos                   | 68.0 ms                                                             | 68.6 ms: 1.01x slower                                                  |
| bench_thread_pool       | 820 us                                                              | 834 us: 1.02x slower                                                   |
| tornado_http            | 96.7 ms                                                             | 98.5 ms: 1.02x slower                                                  |
| sqlglot_optimize        | 53.4 ms                                                             | 54.5 ms: 1.02x slower                                                  |
| logging_silent          | 98.7 ns                                                             | 101 ns: 1.02x slower                                                   |
| json                    | 4.86 ms                                                             | 4.98 ms: 1.03x slower                                                  |
| telco                   | 6.59 ms                                                             | 6.76 ms: 1.03x slower                                                  |
| sqlglot_normalize       | 108 ms                                                              | 111 ms: 1.03x slower                                                   |
| spectral_norm           | 99.5 ms                                                             | 102 ms: 1.03x slower                                                   |
| pprint_pformat          | 1.45 sec                                                            | 1.50 sec: 1.03x slower                                                 |
| logging_simple          | 6.09 us                                                             | 6.28 us: 1.03x slower                                                  |
| sqlalchemy_imperative   | 18.0 ms                                                             | 18.7 ms: 1.03x slower                                                  |
| regex_effbot            | 3.32 ms                                                             | 3.44 ms: 1.04x slower                                                  |
| genshi_text             | 21.8 ms                                                             | 22.7 ms: 1.04x slower                                                  |
| pickle_pure_python      | 307 us                                                              | 319 us: 1.04x slower                                                   |
| pickle_dict             | 30.9 us                                                             | 32.3 us: 1.04x slower                                                  |
| 2to3                    | 257 ms                                                              | 268 ms: 1.04x slower                                                   |
| pprint_safe_repr        | 701 ms                                                              | 733 ms: 1.04x slower                                                   |
| unpickle_list           | 4.96 us                                                             | 5.19 us: 1.05x slower                                                  |
| docutils                | 2.59 sec                                                            | 2.71 sec: 1.05x slower                                                 |
| logging_format          | 6.64 us                                                             | 6.95 us: 1.05x slower                                                  |
| raytrace                | 292 ms                                                              | 306 ms: 1.05x slower                                                   |
| scimark_lu              | 108 ms                                                              | 114 ms: 1.05x slower                                                   |
| comprehensions          | 22.2 us                                                             | 23.4 us: 1.05x slower                                                  |
| pickle                  | 9.79 us                                                             | 10.3 us: 1.05x slower                                                  |
| regex_compile           | 137 ms                                                              | 144 ms: 1.05x slower                                                   |
| sqlalchemy_declarative  | 138 ms                                                              | 146 ms: 1.06x slower                                                   |
| thrift                  | 766 us                                                              | 811 us: 1.06x slower                                                   |
| dulwich_log             | 63.6 ms                                                             | 67.7 ms: 1.06x slower                                                  |
| meteor_contest          | 106 ms                                                              | 113 ms: 1.06x slower                                                   |
| python_startup          | 8.49 ms                                                             | 9.06 ms: 1.07x slower                                                  |
| regex_dna               | 196 ms                                                              | 210 ms: 1.07x slower                                                   |
| deepcopy                | 339 us                                                              | 363 us: 1.07x slower                                                   |
| deepcopy_memo           | 36.4 us                                                             | 39.0 us: 1.07x slower                                                  |
| sqlite_synth            | 2.51 us                                                             | 2.70 us: 1.07x slower                                                  |
| pyflate                 | 414 ms                                                              | 444 ms: 1.07x slower                                                   |
| xml_etree_process       | 54.1 ms                                                             | 58.2 ms: 1.07x slower                                                  |
| scimark_monte_carlo     | 67.8 ms                                                             | 73.0 ms: 1.08x slower                                                  |
| crypto_pyaes            | 73.8 ms                                                             | 79.5 ms: 1.08x slower                                                  |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.83 ms: 1.08x slower                                                  |
| float                   | 76.0 ms                                                             | 82.0 ms: 1.08x slower                                                  |
| deepcopy_reduce         | 2.96 us                                                             | 3.20 us: 1.08x slower                                                  |
| scimark_fft             | 328 ms                                                              | 356 ms: 1.09x slower                                                   |
| gc_traversal            | 3.63 ms                                                             | 3.94 ms: 1.09x slower                                                  |
| xml_etree_generate      | 76.5 ms                                                             | 84.0 ms: 1.10x slower                                                  |
| scimark_sor             | 115 ms                                                              | 126 ms: 1.10x slower                                                   |
| mako                    | 9.82 ms                                                             | 10.8 ms: 1.10x slower                                                  |
| python_startup_no_site  | 5.98 ms                                                             | 6.65 ms: 1.11x slower                                                  |
| pickle_list             | 4.03 us                                                             | 4.79 us: 1.19x slower                                                  |
| unpickle                | 13.2 us                                                             | 15.7 us: 1.19x slower                                                  |
| async_generators        | 361 ms                                                              | 442 ms: 1.22x slower                                                   |
| dask                    | 368 ms                                                              | 539 ms: 1.46x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.01x slower                                                           |

Benchmark hidden because not significant (5): sqlglot_transpile, bench_mp_pool, pycparser, coverage, html5lib
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
