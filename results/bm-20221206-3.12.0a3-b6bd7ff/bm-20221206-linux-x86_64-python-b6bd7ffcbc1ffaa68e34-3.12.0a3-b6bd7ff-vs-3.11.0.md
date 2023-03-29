
# Results vs. 3.11.0

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: linux-x86_64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 246 ms: 1.05x faster                                                  |
| chameleon      | 6.52 ms                                                             | 6.45 ms: 1.01x faster                                                 |
| docutils       | 2.59 sec                                                            | 2.57 sec: 1.01x faster                                                |
| html5lib       | 64.0 ms                                                             | 59.7 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                               | 1.03x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 197 ms                                                              | 189 ms: 1.04x faster                                                  |
| float          | 76.0 ms                                                             | 73.2 ms: 1.04x faster                                                 |
| nbody          | 96.7 ms                                                             | 94.0 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                               | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 129 ms: 1.06x faster                                                  |
| regex_v8       | 22.0 ms                                                             | 22.3 ms: 1.02x slower                                                 |
| regex_effbot   | 3.32 ms                                                             | 3.63 ms: 1.09x slower                                                 |
| regex_dna      | 196 ms                                                              | 217 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                               | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.52 ms: 1.32x faster                                                 |
| unpickle_pure_python | 228 us                                                              | 200 us: 1.14x faster                                                  |
| json_loads           | 26.2 us                                                             | 23.8 us: 1.10x faster                                                 |
| xml_etree_parse      | 162 ms                                                              | 148 ms: 1.09x faster                                                  |
| pickle_pure_python   | 307 us                                                              | 282 us: 1.09x faster                                                  |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.03x faster                                                  |
| pickle_list          | 4.03 us                                                             | 3.95 us: 1.02x faster                                                 |
| xml_etree_process    | 54.1 ms                                                             | 53.7 ms: 1.01x faster                                                 |
| xml_etree_generate   | 76.5 ms                                                             | 76.9 ms: 1.00x slower                                                 |
| unpickle             | 13.2 us                                                             | 13.3 us: 1.01x slower                                                 |
| pickle_dict          | 30.9 us                                                             | 31.5 us: 1.02x slower                                                 |
| pickle               | 9.79 us                                                             | 10.1 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                               | 1.05x faster                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.52 ms: 1.00x slower                                                 |
| python_startup_no_site | 5.98 ms                                                             | 6.07 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                             | 48.0 ms: 1.08x faster                                                 |
| genshi_text    | 21.8 ms                                                             | 20.9 ms: 1.05x faster                                                 |
| mako           | 9.82 ms                                                             | 9.43 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                               | 1.04x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps              | 12.5 ms                                                             | 9.52 ms: 1.32x faster                                                 |
| mypy2                   | 422 ms                                                              | 329 ms: 1.28x faster                                                  |
| unpack_sequence         | 49.5 ns                                                             | 43.1 ns: 1.15x faster                                                 |
| unpickle_pure_python    | 228 us                                                              | 200 us: 1.14x faster                                                  |
| deltablue               | 3.66 ms                                                             | 3.22 ms: 1.14x faster                                                 |
| json_loads              | 26.2 us                                                             | 23.8 us: 1.10x faster                                                 |
| xml_etree_parse         | 162 ms                                                              | 148 ms: 1.09x faster                                                  |
| scimark_sor             | 115 ms                                                              | 105 ms: 1.09x faster                                                  |
| richards                | 45.7 ms                                                             | 42.0 ms: 1.09x faster                                                 |
| pickle_pure_python      | 307 us                                                              | 282 us: 1.09x faster                                                  |
| logging_silent          | 98.7 ns                                                             | 90.9 ns: 1.09x faster                                                 |
| genshi_xml              | 51.8 ms                                                             | 48.0 ms: 1.08x faster                                                 |
| html5lib                | 64.0 ms                                                             | 59.7 ms: 1.07x faster                                                 |
| hexiom                  | 6.48 ms                                                             | 6.08 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.20 ms: 1.06x faster                                                 |
| deepcopy_memo           | 36.4 us                                                             | 34.2 us: 1.06x faster                                                 |
| regex_compile           | 137 ms                                                              | 129 ms: 1.06x faster                                                  |
| mdp                     | 2.64 sec                                                            | 2.50 sec: 1.06x faster                                                |
| sqlglot_optimize        | 53.4 ms                                                             | 50.6 ms: 1.05x faster                                                 |
| bench_thread_pool       | 820 us                                                              | 778 us: 1.05x faster                                                  |
| coroutines              | 26.3 ms                                                             | 25.0 ms: 1.05x faster                                                 |
| nqueens                 | 84.0 ms                                                             | 80.1 ms: 1.05x faster                                                 |
| genshi_text             | 21.8 ms                                                             | 20.9 ms: 1.05x faster                                                 |
| pycparser               | 1.14 sec                                                            | 1.09 sec: 1.05x faster                                                |
| 2to3                    | 257 ms                                                              | 246 ms: 1.05x faster                                                  |
| scimark_fft             | 328 ms                                                              | 314 ms: 1.04x faster                                                  |
| raytrace                | 292 ms                                                              | 281 ms: 1.04x faster                                                  |
| sympy_expand            | 477 ms                                                              | 458 ms: 1.04x faster                                                  |
| mako                    | 9.82 ms                                                             | 9.43 ms: 1.04x faster                                                 |
| json                    | 4.86 ms                                                             | 4.67 ms: 1.04x faster                                                 |
| pidigits                | 197 ms                                                              | 189 ms: 1.04x faster                                                  |
| float                   | 76.0 ms                                                             | 73.2 ms: 1.04x faster                                                 |
| scimark_monte_carlo     | 67.8 ms                                                             | 65.4 ms: 1.04x faster                                                 |
| logging_simple          | 6.09 us                                                             | 5.88 us: 1.04x faster                                                 |
| spectral_norm           | 99.5 ms                                                             | 96.0 ms: 1.04x faster                                                 |
| sqlglot_normalize       | 108 ms                                                              | 105 ms: 1.04x faster                                                  |
| logging_format          | 6.64 us                                                             | 6.41 us: 1.04x faster                                                 |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.03x faster                                                  |
| sympy_integrate         | 21.0 ms                                                             | 20.4 ms: 1.03x faster                                                 |
| sympy_str               | 291 ms                                                              | 283 ms: 1.03x faster                                                  |
| create_gc_cycles        | 1.48 ms                                                             | 1.44 ms: 1.03x faster                                                 |
| nbody                   | 96.7 ms                                                             | 94.0 ms: 1.03x faster                                                 |
| pprint_pformat          | 1.45 sec                                                            | 1.41 sec: 1.03x faster                                                |
| pprint_safe_repr        | 701 ms                                                              | 686 ms: 1.02x faster                                                  |
| dask                    | 368 ms                                                              | 360 ms: 1.02x faster                                                  |
| go                      | 138 ms                                                              | 136 ms: 1.02x faster                                                  |
| pickle_list             | 4.03 us                                                             | 3.95 us: 1.02x faster                                                 |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                                  |
| telco                   | 6.59 ms                                                             | 6.46 ms: 1.02x faster                                                 |
| sympy_sum               | 167 ms                                                              | 164 ms: 1.02x faster                                                  |
| pyflate                 | 414 ms                                                              | 405 ms: 1.02x faster                                                  |
| scimark_lu              | 108 ms                                                              | 106 ms: 1.02x faster                                                  |
| deepcopy                | 339 us                                                              | 332 us: 1.02x faster                                                  |
| thrift                  | 766 us                                                              | 751 us: 1.02x faster                                                  |
| async_generators        | 361 ms                                                              | 354 ms: 1.02x faster                                                  |
| dulwich_log             | 63.6 ms                                                             | 62.5 ms: 1.02x faster                                                 |
| chaos                   | 68.0 ms                                                             | 66.9 ms: 1.02x faster                                                 |
| sqlglot_parse           | 1.36 ms                                                             | 1.34 ms: 1.01x faster                                                 |
| fannkuch                | 384 ms                                                              | 379 ms: 1.01x faster                                                  |
| sqlglot_transpile       | 1.65 ms                                                             | 1.63 ms: 1.01x faster                                                 |
| chameleon               | 6.52 ms                                                             | 6.45 ms: 1.01x faster                                                 |
| xml_etree_process       | 54.1 ms                                                             | 53.7 ms: 1.01x faster                                                 |
| docutils                | 2.59 sec                                                            | 2.57 sec: 1.01x faster                                                |
| asyncio_tcp             | 888 ms                                                              | 890 ms: 1.00x slower                                                  |
| python_startup          | 8.49 ms                                                             | 8.52 ms: 1.00x slower                                                 |
| xml_etree_generate      | 76.5 ms                                                             | 76.9 ms: 1.00x slower                                                 |
| unpickle                | 13.2 us                                                             | 13.3 us: 1.01x slower                                                 |
| coverage                | 101 ms                                                              | 102 ms: 1.01x slower                                                  |
| python_startup_no_site  | 5.98 ms                                                             | 6.07 ms: 1.02x slower                                                 |
| regex_v8                | 22.0 ms                                                             | 22.3 ms: 1.02x slower                                                 |
| pickle_dict             | 30.9 us                                                             | 31.5 us: 1.02x slower                                                 |
| crypto_pyaes            | 73.8 ms                                                             | 75.3 ms: 1.02x slower                                                 |
| async_tree_none         | 525 ms                                                              | 536 ms: 1.02x slower                                                  |
| sqlite_synth            | 2.51 us                                                             | 2.58 us: 1.03x slower                                                 |
| pickle                  | 9.79 us                                                             | 10.1 us: 1.04x slower                                                 |
| async_tree_io           | 1.28 sec                                                            | 1.34 sec: 1.04x slower                                                |
| async_tree_cpu_io_mixed | 736 ms                                                              | 769 ms: 1.05x slower                                                  |
| gc_traversal            | 3.63 ms                                                             | 3.81 ms: 1.05x slower                                                 |
| comprehensions          | 22.2 us                                                             | 23.5 us: 1.06x slower                                                 |
| async_tree_memoization  | 621 ms                                                              | 665 ms: 1.07x slower                                                  |
| generators              | 73.4 ms                                                             | 79.1 ms: 1.08x slower                                                 |
| regex_effbot            | 3.32 ms                                                             | 3.63 ms: 1.09x slower                                                 |
| regex_dna               | 196 ms                                                              | 217 ms: 1.10x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.03x faster                                                          |

Benchmark hidden because not significant (6): bench_mp_pool, unpickle_list, django_template, pathlib, deepcopy_reduce, djangocms
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
