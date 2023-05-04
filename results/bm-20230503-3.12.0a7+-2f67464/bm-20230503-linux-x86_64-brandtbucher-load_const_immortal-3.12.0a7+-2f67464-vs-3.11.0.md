
# Results vs. 3.11.0

- fork: brandtbucher
- ref: load_const_immortal
- machine: linux-x86_64
- commit hash: 2f67464
- commit date: 2023-05-03
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 270 ms: 1.05x slower                                                        |
| docutils       | 2.59 sec                                                            | 2.76 sec: 1.06x slower                                                      |
| tornado_http   | 96.7 ms                                                             | 99.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 89.2 ms: 1.08x faster                                                       |
| pidigits       | 197 ms                                                              | 197 ms: 1.00x slower                                                        |
| float          | 76.0 ms                                                             | 81.9 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                               | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.3 ms: 1.02x slower                                                       |
| regex_dna      | 196 ms                                                              | 209 ms: 1.06x slower                                                        |
| regex_effbot   | 3.32 ms                                                             | 3.55 ms: 1.07x slower                                                       |
| regex_compile  | 137 ms                                                              | 146 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.86 ms: 1.27x faster                                                       |
| xml_etree_parse      | 162 ms                                                              | 153 ms: 1.06x faster                                                        |
| unpickle_pure_python | 228 us                                                              | 219 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.04x faster                                                        |
| json_loads           | 26.2 us                                                             | 26.0 us: 1.01x faster                                                       |
| unpickle_list        | 4.96 us                                                             | 4.94 us: 1.00x faster                                                       |
| pickle_pure_python   | 307 us                                                              | 318 us: 1.04x slower                                                        |
| pickle_dict          | 30.9 us                                                             | 32.1 us: 1.04x slower                                                       |
| pickle               | 9.79 us                                                             | 10.8 us: 1.10x slower                                                       |
| pickle_list          | 4.03 us                                                             | 4.48 us: 1.11x slower                                                       |
| xml_etree_process    | 54.1 ms                                                             | 60.4 ms: 1.12x slower                                                       |
| xml_etree_generate   | 76.5 ms                                                             | 86.3 ms: 1.13x slower                                                       |
| unpickle             | 13.2 us                                                             | 15.0 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.16 ms: 1.08x slower                                                       |
| python_startup_no_site | 5.98 ms                                                             | 6.68 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|-----------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 9.82 ms                                                             | 10.7 ms: 1.09x slower                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 31.0 ms: 2.37x faster                                                       |
| asyncio_tcp             | 888 ms                                                              | 510 ms: 1.74x faster                                                        |
| json_dumps              | 12.5 ms                                                             | 9.86 ms: 1.27x faster                                                       |
| mypy2                   | 422 ms                                                              | 354 ms: 1.19x faster                                                        |
| coroutines              | 26.3 ms                                                             | 22.3 ms: 1.18x faster                                                       |
| nbody                   | 96.7 ms                                                             | 89.2 ms: 1.08x faster                                                       |
| xml_etree_parse         | 162 ms                                                              | 153 ms: 1.06x faster                                                        |
| async_tree_none         | 525 ms                                                              | 500 ms: 1.05x faster                                                        |
| unpickle_pure_python    | 228 us                                                              | 219 us: 1.04x faster                                                        |
| async_tree_io           | 1.28 sec                                                            | 1.24 sec: 1.04x faster                                                      |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.04x faster                                                        |
| hexiom                  | 6.48 ms                                                             | 6.30 ms: 1.03x faster                                                       |
| deltablue               | 3.66 ms                                                             | 3.57 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed | 736 ms                                                              | 722 ms: 1.02x faster                                                        |
| meteor_contest          | 106 ms                                                              | 105 ms: 1.01x faster                                                        |
| go                      | 138 ms                                                              | 137 ms: 1.01x faster                                                        |
| sqlglot_parse           | 1.36 ms                                                             | 1.35 ms: 1.01x faster                                                       |
| fannkuch                | 384 ms                                                              | 379 ms: 1.01x faster                                                        |
| nqueens                 | 84.0 ms                                                             | 83.3 ms: 1.01x faster                                                       |
| mdp                     | 2.64 sec                                                            | 2.62 sec: 1.01x faster                                                      |
| json_loads              | 26.2 us                                                             | 26.0 us: 1.01x faster                                                       |
| unpickle_list           | 4.96 us                                                             | 4.94 us: 1.00x faster                                                       |
| pidigits                | 197 ms                                                              | 197 ms: 1.00x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                             | 1.67 ms: 1.01x slower                                                       |
| create_gc_cycles        | 1.48 ms                                                             | 1.49 ms: 1.01x slower                                                       |
| unpack_sequence         | 49.5 ns                                                             | 50.0 ns: 1.01x slower                                                       |
| coverage                | 101 ms                                                              | 102 ms: 1.01x slower                                                        |
| regex_v8                | 22.0 ms                                                             | 22.3 ms: 1.02x slower                                                       |
| bench_thread_pool       | 820 us                                                              | 833 us: 1.02x slower                                                        |
| pathlib                 | 18.2 ms                                                             | 18.5 ms: 1.02x slower                                                       |
| chaos                   | 68.0 ms                                                             | 69.4 ms: 1.02x slower                                                       |
| json                    | 4.86 ms                                                             | 4.98 ms: 1.02x slower                                                       |
| logging_silent          | 98.7 ns                                                             | 102 ns: 1.03x slower                                                        |
| tornado_http            | 96.7 ms                                                             | 99.8 ms: 1.03x slower                                                       |
| pickle_pure_python      | 307 us                                                              | 318 us: 1.04x slower                                                        |
| logging_simple          | 6.09 us                                                             | 6.31 us: 1.04x slower                                                       |
| sqlglot_optimize        | 53.4 ms                                                             | 55.4 ms: 1.04x slower                                                       |
| pickle_dict             | 30.9 us                                                             | 32.1 us: 1.04x slower                                                       |
| scimark_lu              | 108 ms                                                              | 113 ms: 1.04x slower                                                        |
| sqlglot_normalize       | 108 ms                                                              | 113 ms: 1.04x slower                                                        |
| pprint_pformat          | 1.45 sec                                                            | 1.51 sec: 1.04x slower                                                      |
| raytrace                | 292 ms                                                              | 306 ms: 1.05x slower                                                        |
| 2to3                    | 257 ms                                                              | 270 ms: 1.05x slower                                                        |
| pprint_safe_repr        | 701 ms                                                              | 740 ms: 1.06x slower                                                        |
| sqlalchemy_declarative  | 138 ms                                                              | 147 ms: 1.06x slower                                                        |
| comprehensions          | 22.2 us                                                             | 23.5 us: 1.06x slower                                                       |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.74 ms: 1.06x slower                                                       |
| regex_dna               | 196 ms                                                              | 209 ms: 1.06x slower                                                        |
| docutils                | 2.59 sec                                                            | 2.76 sec: 1.06x slower                                                      |
| logging_format          | 6.64 us                                                             | 7.08 us: 1.07x slower                                                       |
| deepcopy_memo           | 36.4 us                                                             | 38.8 us: 1.07x slower                                                       |
| regex_effbot            | 3.32 ms                                                             | 3.55 ms: 1.07x slower                                                       |
| sqlite_synth            | 2.51 us                                                             | 2.68 us: 1.07x slower                                                       |
| dulwich_log             | 63.6 ms                                                             | 68.0 ms: 1.07x slower                                                       |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.3 ms: 1.07x slower                                                       |
| scimark_sor             | 115 ms                                                              | 123 ms: 1.07x slower                                                        |
| telco                   | 6.59 ms                                                             | 7.05 ms: 1.07x slower                                                       |
| regex_compile           | 137 ms                                                              | 146 ms: 1.07x slower                                                        |
| scimark_fft             | 328 ms                                                              | 353 ms: 1.08x slower                                                        |
| python_startup          | 8.49 ms                                                             | 9.16 ms: 1.08x slower                                                       |
| float                   | 76.0 ms                                                             | 81.9 ms: 1.08x slower                                                       |
| deepcopy                | 339 us                                                              | 367 us: 1.08x slower                                                        |
| scimark_monte_carlo     | 67.8 ms                                                             | 73.4 ms: 1.08x slower                                                       |
| spectral_norm           | 99.5 ms                                                             | 108 ms: 1.09x slower                                                        |
| mako                    | 9.82 ms                                                             | 10.7 ms: 1.09x slower                                                       |
| gc_traversal            | 3.63 ms                                                             | 3.94 ms: 1.09x slower                                                       |
| pyflate                 | 414 ms                                                              | 450 ms: 1.09x slower                                                        |
| deepcopy_reduce         | 2.96 us                                                             | 3.23 us: 1.09x slower                                                       |
| crypto_pyaes            | 73.8 ms                                                             | 80.5 ms: 1.09x slower                                                       |
| pickle                  | 9.79 us                                                             | 10.8 us: 1.10x slower                                                       |
| pickle_list             | 4.03 us                                                             | 4.48 us: 1.11x slower                                                       |
| xml_etree_process       | 54.1 ms                                                             | 60.4 ms: 1.12x slower                                                       |
| python_startup_no_site  | 5.98 ms                                                             | 6.68 ms: 1.12x slower                                                       |
| xml_etree_generate      | 76.5 ms                                                             | 86.3 ms: 1.13x slower                                                       |
| unpickle                | 13.2 us                                                             | 15.0 us: 1.14x slower                                                       |
| async_generators        | 361 ms                                                              | 455 ms: 1.26x slower                                                        |
| dask                    | 368 ms                                                              | 542 ms: 1.47x slower                                                        |
| Geometric mean          | (ref)                                                               | 1.02x slower                                                                |

Benchmark hidden because not significant (4): async_tree_memoization, richards, bench_mp_pool, pycparser
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
