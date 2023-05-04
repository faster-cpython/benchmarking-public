
# Results vs. 3.11.0

- fork: brandtbucher
- ref: load_const_immortal
- machine: linux-x86_64
- commit hash: a39e7e6
- commit date: 2023-05-02
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 270 ms: 1.05x slower                                                        |
| docutils       | 2.59 sec                                                            | 2.71 sec: 1.05x slower                                                      |
| tornado_http   | 96.7 ms                                                             | 99.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 90.3 ms: 1.07x faster                                                       |
| pidigits       | 197 ms                                                              | 197 ms: 1.00x slower                                                        |
| float          | 76.0 ms                                                             | 81.6 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.2 ms: 1.01x slower                                                       |
| regex_dna      | 196 ms                                                              | 200 ms: 1.02x slower                                                        |
| regex_compile  | 137 ms                                                              | 146 ms: 1.07x slower                                                        |
| regex_effbot   | 3.32 ms                                                             | 3.57 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 10.0 ms: 1.25x faster                                                       |
| xml_etree_parse      | 162 ms                                                              | 154 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.04x faster                                                        |
| unpickle_pure_python | 228 us                                                              | 220 us: 1.04x faster                                                        |
| pickle_dict          | 30.9 us                                                             | 30.7 us: 1.01x faster                                                       |
| pickle_pure_python   | 307 us                                                              | 317 us: 1.03x slower                                                        |
| pickle               | 9.79 us                                                             | 10.7 us: 1.09x slower                                                       |
| xml_etree_process    | 54.1 ms                                                             | 59.4 ms: 1.10x slower                                                       |
| xml_etree_generate   | 76.5 ms                                                             | 84.8 ms: 1.11x slower                                                       |
| unpickle             | 13.2 us                                                             | 14.7 us: 1.11x slower                                                       |
| pickle_list          | 4.03 us                                                             | 4.62 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                                |

Benchmark hidden because not significant (2): unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.21 ms: 1.08x slower                                                       |
| python_startup_no_site | 5.98 ms                                                             | 6.74 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                               | 1.11x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|-----------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 9.82 ms                                                             | 10.8 ms: 1.10x slower                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 32.8 ms: 2.24x faster                                                       |
| asyncio_tcp             | 888 ms                                                              | 507 ms: 1.75x faster                                                        |
| json_dumps              | 12.5 ms                                                             | 10.0 ms: 1.25x faster                                                       |
| mypy2                   | 422 ms                                                              | 351 ms: 1.20x faster                                                        |
| coroutines              | 26.3 ms                                                             | 23.1 ms: 1.14x faster                                                       |
| nbody                   | 96.7 ms                                                             | 90.3 ms: 1.07x faster                                                       |
| xml_etree_parse         | 162 ms                                                              | 154 ms: 1.05x faster                                                        |
| async_tree_none         | 525 ms                                                              | 503 ms: 1.04x faster                                                        |
| nqueens                 | 84.0 ms                                                             | 80.6 ms: 1.04x faster                                                       |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.04x faster                                                        |
| unpickle_pure_python    | 228 us                                                              | 220 us: 1.04x faster                                                        |
| async_tree_io           | 1.28 sec                                                            | 1.24 sec: 1.03x faster                                                      |
| hexiom                  | 6.48 ms                                                             | 6.27 ms: 1.03x faster                                                       |
| deltablue               | 3.66 ms                                                             | 3.54 ms: 1.03x faster                                                       |
| richards                | 45.7 ms                                                             | 44.6 ms: 1.02x faster                                                       |
| mdp                     | 2.64 sec                                                            | 2.58 sec: 1.02x faster                                                      |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                              | 727 ms: 1.01x faster                                                        |
| sqlglot_parse           | 1.36 ms                                                             | 1.35 ms: 1.01x faster                                                       |
| pickle_dict             | 30.9 us                                                             | 30.7 us: 1.01x faster                                                       |
| pidigits                | 197 ms                                                              | 197 ms: 1.00x slower                                                        |
| coverage                | 101 ms                                                              | 102 ms: 1.01x slower                                                        |
| pycparser               | 1.14 sec                                                            | 1.16 sec: 1.01x slower                                                      |
| chaos                   | 68.0 ms                                                             | 68.6 ms: 1.01x slower                                                       |
| regex_v8                | 22.0 ms                                                             | 22.2 ms: 1.01x slower                                                       |
| create_gc_cycles        | 1.48 ms                                                             | 1.50 ms: 1.01x slower                                                       |
| sqlglot_transpile       | 1.65 ms                                                             | 1.68 ms: 1.01x slower                                                       |
| regex_dna               | 196 ms                                                              | 200 ms: 1.02x slower                                                        |
| logging_silent          | 98.7 ns                                                             | 101 ns: 1.02x slower                                                        |
| bench_thread_pool       | 820 us                                                              | 838 us: 1.02x slower                                                        |
| pathlib                 | 18.2 ms                                                             | 18.7 ms: 1.03x slower                                                       |
| json                    | 4.86 ms                                                             | 5.00 ms: 1.03x slower                                                       |
| pickle_pure_python      | 307 us                                                              | 317 us: 1.03x slower                                                        |
| deepcopy_memo           | 36.4 us                                                             | 37.6 us: 1.03x slower                                                       |
| tornado_http            | 96.7 ms                                                             | 99.8 ms: 1.03x slower                                                       |
| sqlglot_optimize        | 53.4 ms                                                             | 55.3 ms: 1.04x slower                                                       |
| pprint_pformat          | 1.45 sec                                                            | 1.50 sec: 1.04x slower                                                      |
| scimark_lu              | 108 ms                                                              | 113 ms: 1.04x slower                                                        |
| raytrace                | 292 ms                                                              | 304 ms: 1.04x slower                                                        |
| logging_simple          | 6.09 us                                                             | 6.36 us: 1.04x slower                                                       |
| docutils                | 2.59 sec                                                            | 2.71 sec: 1.05x slower                                                      |
| 2to3                    | 257 ms                                                              | 270 ms: 1.05x slower                                                        |
| telco                   | 6.59 ms                                                             | 6.94 ms: 1.05x slower                                                       |
| sqlglot_normalize       | 108 ms                                                              | 114 ms: 1.06x slower                                                        |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.1 ms: 1.06x slower                                                       |
| pprint_safe_repr        | 701 ms                                                              | 742 ms: 1.06x slower                                                        |
| comprehensions          | 22.2 us                                                             | 23.5 us: 1.06x slower                                                       |
| sqlalchemy_declarative  | 138 ms                                                              | 147 ms: 1.07x slower                                                        |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.77 ms: 1.07x slower                                                       |
| regex_compile           | 137 ms                                                              | 146 ms: 1.07x slower                                                        |
| sqlite_synth            | 2.51 us                                                             | 2.69 us: 1.07x slower                                                       |
| gc_traversal            | 3.63 ms                                                             | 3.89 ms: 1.07x slower                                                       |
| dulwich_log             | 63.6 ms                                                             | 68.3 ms: 1.07x slower                                                       |
| float                   | 76.0 ms                                                             | 81.6 ms: 1.07x slower                                                       |
| regex_effbot            | 3.32 ms                                                             | 3.57 ms: 1.07x slower                                                       |
| logging_format          | 6.64 us                                                             | 7.16 us: 1.08x slower                                                       |
| unpack_sequence         | 49.5 ns                                                             | 53.4 ns: 1.08x slower                                                       |
| deepcopy                | 339 us                                                              | 366 us: 1.08x slower                                                        |
| scimark_sor             | 115 ms                                                              | 124 ms: 1.08x slower                                                        |
| python_startup          | 8.49 ms                                                             | 9.21 ms: 1.08x slower                                                       |
| deepcopy_reduce         | 2.96 us                                                             | 3.21 us: 1.09x slower                                                       |
| scimark_fft             | 328 ms                                                              | 356 ms: 1.09x slower                                                        |
| pyflate                 | 414 ms                                                              | 450 ms: 1.09x slower                                                        |
| scimark_monte_carlo     | 67.8 ms                                                             | 73.8 ms: 1.09x slower                                                       |
| spectral_norm           | 99.5 ms                                                             | 109 ms: 1.09x slower                                                        |
| pickle                  | 9.79 us                                                             | 10.7 us: 1.09x slower                                                       |
| crypto_pyaes            | 73.8 ms                                                             | 80.6 ms: 1.09x slower                                                       |
| xml_etree_process       | 54.1 ms                                                             | 59.4 ms: 1.10x slower                                                       |
| mako                    | 9.82 ms                                                             | 10.8 ms: 1.10x slower                                                       |
| xml_etree_generate      | 76.5 ms                                                             | 84.8 ms: 1.11x slower                                                       |
| unpickle                | 13.2 us                                                             | 14.7 us: 1.11x slower                                                       |
| python_startup_no_site  | 5.98 ms                                                             | 6.74 ms: 1.13x slower                                                       |
| pickle_list             | 4.03 us                                                             | 4.62 us: 1.15x slower                                                       |
| async_generators        | 361 ms                                                              | 451 ms: 1.25x slower                                                        |
| dask                    | 368 ms                                                              | 542 ms: 1.47x slower                                                        |
| Geometric mean          | (ref)                                                               | 1.02x slower                                                                |

Benchmark hidden because not significant (6): async_tree_memoization, unpickle_list, go, bench_mp_pool, json_loads, fannkuch
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
