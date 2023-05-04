
# Results vs. 3.11.0

- fork: python
- ref: da1980afcb8820ffaa05
- machine: linux-x86_64
- commit hash: da1980a
- commit date: 2023-05-03
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 271 ms: 1.05x slower                                                   |
| docutils       | 2.59 sec                                                            | 2.73 sec: 1.05x slower                                                 |
| tornado_http   | 96.7 ms                                                             | 99.9 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                               | 1.05x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 87.4 ms: 1.11x faster                                                  |
| pidigits       | 197 ms                                                              | 189 ms: 1.04x faster                                                   |
| float          | 76.0 ms                                                             | 82.0 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                               | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.2 ms: 1.01x slower                                                  |
| regex_effbot   | 3.32 ms                                                             | 3.40 ms: 1.02x slower                                                  |
| regex_dna      | 196 ms                                                              | 205 ms: 1.04x slower                                                   |
| regex_compile  | 137 ms                                                              | 145 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                               | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 10.0 ms: 1.25x faster                                                  |
| xml_etree_parse      | 162 ms                                                              | 153 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 108 ms                                                              | 103 ms: 1.04x faster                                                   |
| unpickle_pure_python | 228 us                                                              | 220 us: 1.04x faster                                                   |
| json_loads           | 26.2 us                                                             | 25.7 us: 1.02x faster                                                  |
| pickle_pure_python   | 307 us                                                              | 316 us: 1.03x slower                                                   |
| unpickle_list        | 4.96 us                                                             | 5.10 us: 1.03x slower                                                  |
| pickle_dict          | 30.9 us                                                             | 31.8 us: 1.03x slower                                                  |
| pickle               | 9.79 us                                                             | 10.5 us: 1.07x slower                                                  |
| xml_etree_process    | 54.1 ms                                                             | 58.7 ms: 1.08x slower                                                  |
| xml_etree_generate   | 76.5 ms                                                             | 84.3 ms: 1.10x slower                                                  |
| unpickle             | 13.2 us                                                             | 14.8 us: 1.12x slower                                                  |
| pickle_list          | 4.03 us                                                             | 4.58 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.14 ms: 1.08x slower                                                  |
| python_startup_no_site | 5.98 ms                                                             | 6.69 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|-----------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 9.82 ms                                                             | 10.9 ms: 1.11x slower                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 32.3 ms: 2.27x faster                                                  |
| asyncio_tcp             | 888 ms                                                              | 510 ms: 1.74x faster                                                   |
| json_dumps              | 12.5 ms                                                             | 10.0 ms: 1.25x faster                                                  |
| mypy2                   | 422 ms                                                              | 352 ms: 1.20x faster                                                   |
| coroutines              | 26.3 ms                                                             | 22.9 ms: 1.15x faster                                                  |
| nbody                   | 96.7 ms                                                             | 87.4 ms: 1.11x faster                                                  |
| xml_etree_parse         | 162 ms                                                              | 153 ms: 1.06x faster                                                   |
| async_tree_none         | 525 ms                                                              | 500 ms: 1.05x faster                                                   |
| xml_etree_iterparse     | 108 ms                                                              | 103 ms: 1.04x faster                                                   |
| pidigits                | 197 ms                                                              | 189 ms: 1.04x faster                                                   |
| async_tree_io           | 1.28 sec                                                            | 1.23 sec: 1.04x faster                                                 |
| hexiom                  | 6.48 ms                                                             | 6.23 ms: 1.04x faster                                                  |
| unpickle_pure_python    | 228 us                                                              | 220 us: 1.04x faster                                                   |
| richards                | 45.7 ms                                                             | 44.7 ms: 1.02x faster                                                  |
| json_loads              | 26.2 us                                                             | 25.7 us: 1.02x faster                                                  |
| create_gc_cycles        | 1.48 ms                                                             | 1.46 ms: 1.02x faster                                                  |
| sqlglot_parse           | 1.36 ms                                                             | 1.34 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                              | 724 ms: 1.02x faster                                                   |
| async_tree_memoization  | 621 ms                                                              | 612 ms: 1.02x faster                                                   |
| nqueens                 | 84.0 ms                                                             | 82.8 ms: 1.01x faster                                                  |
| mdp                     | 2.64 sec                                                            | 2.61 sec: 1.01x faster                                                 |
| deltablue               | 3.66 ms                                                             | 3.64 ms: 1.01x faster                                                  |
| go                      | 138 ms                                                              | 138 ms: 1.00x faster                                                   |
| gc_traversal            | 3.63 ms                                                             | 3.64 ms: 1.00x slower                                                  |
| unpack_sequence         | 49.5 ns                                                             | 49.9 ns: 1.01x slower                                                  |
| sqlglot_transpile       | 1.65 ms                                                             | 1.67 ms: 1.01x slower                                                  |
| regex_v8                | 22.0 ms                                                             | 22.2 ms: 1.01x slower                                                  |
| json                    | 4.86 ms                                                             | 4.91 ms: 1.01x slower                                                  |
| pathlib                 | 18.2 ms                                                             | 18.5 ms: 1.01x slower                                                  |
| coverage                | 101 ms                                                              | 103 ms: 1.02x slower                                                   |
| bench_thread_pool       | 820 us                                                              | 836 us: 1.02x slower                                                   |
| regex_effbot            | 3.32 ms                                                             | 3.40 ms: 1.02x slower                                                  |
| chaos                   | 68.0 ms                                                             | 69.9 ms: 1.03x slower                                                  |
| pickle_pure_python      | 307 us                                                              | 316 us: 1.03x slower                                                   |
| telco                   | 6.59 ms                                                             | 6.78 ms: 1.03x slower                                                  |
| unpickle_list           | 4.96 us                                                             | 5.10 us: 1.03x slower                                                  |
| pickle_dict             | 30.9 us                                                             | 31.8 us: 1.03x slower                                                  |
| pprint_pformat          | 1.45 sec                                                            | 1.50 sec: 1.03x slower                                                 |
| tornado_http            | 96.7 ms                                                             | 99.9 ms: 1.03x slower                                                  |
| sqlglot_optimize        | 53.4 ms                                                             | 55.5 ms: 1.04x slower                                                  |
| regex_dna               | 196 ms                                                              | 205 ms: 1.04x slower                                                   |
| logging_simple          | 6.09 us                                                             | 6.35 us: 1.04x slower                                                  |
| comprehensions          | 22.2 us                                                             | 23.2 us: 1.04x slower                                                  |
| pprint_safe_repr        | 701 ms                                                              | 734 ms: 1.05x slower                                                   |
| raytrace                | 292 ms                                                              | 306 ms: 1.05x slower                                                   |
| logging_silent          | 98.7 ns                                                             | 104 ns: 1.05x slower                                                   |
| sqlglot_normalize       | 108 ms                                                              | 114 ms: 1.05x slower                                                   |
| docutils                | 2.59 sec                                                            | 2.73 sec: 1.05x slower                                                 |
| 2to3                    | 257 ms                                                              | 271 ms: 1.05x slower                                                   |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.0 ms: 1.06x slower                                                  |
| sqlalchemy_declarative  | 138 ms                                                              | 146 ms: 1.06x slower                                                   |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.73 ms: 1.06x slower                                                  |
| scimark_lu              | 108 ms                                                              | 115 ms: 1.06x slower                                                   |
| logging_format          | 6.64 us                                                             | 7.06 us: 1.06x slower                                                  |
| regex_compile           | 137 ms                                                              | 145 ms: 1.06x slower                                                   |
| dulwich_log             | 63.6 ms                                                             | 67.8 ms: 1.07x slower                                                  |
| deepcopy_memo           | 36.4 us                                                             | 38.9 us: 1.07x slower                                                  |
| sqlite_synth            | 2.51 us                                                             | 2.70 us: 1.07x slower                                                  |
| pickle                  | 9.79 us                                                             | 10.5 us: 1.07x slower                                                  |
| python_startup          | 8.49 ms                                                             | 9.14 ms: 1.08x slower                                                  |
| scimark_fft             | 328 ms                                                              | 353 ms: 1.08x slower                                                   |
| crypto_pyaes            | 73.8 ms                                                             | 79.6 ms: 1.08x slower                                                  |
| float                   | 76.0 ms                                                             | 82.0 ms: 1.08x slower                                                  |
| scimark_monte_carlo     | 67.8 ms                                                             | 73.3 ms: 1.08x slower                                                  |
| xml_etree_process       | 54.1 ms                                                             | 58.7 ms: 1.08x slower                                                  |
| deepcopy                | 339 us                                                              | 370 us: 1.09x slower                                                   |
| spectral_norm           | 99.5 ms                                                             | 109 ms: 1.10x slower                                                   |
| xml_etree_generate      | 76.5 ms                                                             | 84.3 ms: 1.10x slower                                                  |
| scimark_sor             | 115 ms                                                              | 127 ms: 1.10x slower                                                   |
| pyflate                 | 414 ms                                                              | 456 ms: 1.10x slower                                                   |
| meteor_contest          | 106 ms                                                              | 118 ms: 1.11x slower                                                   |
| mako                    | 9.82 ms                                                             | 10.9 ms: 1.11x slower                                                  |
| deepcopy_reduce         | 2.96 us                                                             | 3.28 us: 1.11x slower                                                  |
| python_startup_no_site  | 5.98 ms                                                             | 6.69 ms: 1.12x slower                                                  |
| unpickle                | 13.2 us                                                             | 14.8 us: 1.12x slower                                                  |
| pickle_list             | 4.03 us                                                             | 4.58 us: 1.14x slower                                                  |
| async_generators        | 361 ms                                                              | 453 ms: 1.25x slower                                                   |
| dask                    | 368 ms                                                              | 542 ms: 1.47x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.01x slower                                                           |

Benchmark hidden because not significant (3): fannkuch, bench_mp_pool, pycparser
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
