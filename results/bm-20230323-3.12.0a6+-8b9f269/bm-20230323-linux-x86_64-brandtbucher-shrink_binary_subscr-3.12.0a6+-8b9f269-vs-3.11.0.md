
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_binary_subscr
- machine: linux-x86_64
- commit hash: 8b9f269
- commit date: 2023-03-23
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 251 ms: 1.02x faster                                                         |
| chameleon      | 6.52 ms                                                             | 6.41 ms: 1.02x faster                                                        |
| docutils       | 2.59 sec                                                            | 2.53 sec: 1.02x faster                                                       |
| html5lib       | 64.0 ms                                                             | 61.9 ms: 1.03x faster                                                        |
| tornado_http   | 96.7 ms                                                             | 91.2 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                               | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 87.5 ms: 1.11x faster                                                        |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                         |
| float          | 76.0 ms                                                             | 73.3 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                               | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 21.4 ms: 1.02x faster                                                        |
| regex_compile  | 137 ms                                                              | 134 ms: 1.02x faster                                                         |
| regex_dna      | 196 ms                                                              | 205 ms: 1.04x slower                                                         |
| regex_effbot   | 3.32 ms                                                             | 3.50 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.65 ms: 1.30x faster                                                        |
| unpickle_pure_python | 228 us                                                              | 199 us: 1.15x faster                                                         |
| xml_etree_parse      | 162 ms                                                              | 149 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 108 ms                                                              | 99.3 ms: 1.08x faster                                                        |
| pickle_pure_python   | 307 us                                                              | 286 us: 1.07x faster                                                         |
| json_loads           | 26.2 us                                                             | 24.4 us: 1.07x faster                                                        |
| unpickle_list        | 4.96 us                                                             | 4.99 us: 1.01x slower                                                        |
| unpickle             | 13.2 us                                                             | 13.3 us: 1.01x slower                                                        |
| pickle_dict          | 30.9 us                                                             | 31.5 us: 1.02x slower                                                        |
| xml_etree_process    | 54.1 ms                                                             | 55.7 ms: 1.03x slower                                                        |
| xml_etree_generate   | 76.5 ms                                                             | 80.8 ms: 1.06x slower                                                        |
| pickle               | 9.79 us                                                             | 10.5 us: 1.07x slower                                                        |
| pickle_list          | 4.03 us                                                             | 4.36 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.79 ms: 1.03x slower                                                        |
| python_startup_no_site | 5.98 ms                                                             | 6.49 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                               | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 47.7 ms: 1.09x faster                                                        |
| genshi_text     | 21.8 ms                                                             | 21.4 ms: 1.02x faster                                                        |
| django_template | 32.9 ms                                                             | 33.3 ms: 1.01x slower                                                        |
| mako            | 9.82 ms                                                             | 9.99 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                               | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 29.9 ms: 2.46x faster                                                        |
| asyncio_tcp             | 888 ms                                                              | 506 ms: 1.76x faster                                                         |
| json_dumps              | 12.5 ms                                                             | 9.65 ms: 1.30x faster                                                        |
| mypy2                   | 422 ms                                                              | 335 ms: 1.26x faster                                                         |
| unpack_sequence         | 49.5 ns                                                             | 42.8 ns: 1.16x faster                                                        |
| unpickle_pure_python    | 228 us                                                              | 199 us: 1.15x faster                                                         |
| deltablue               | 3.66 ms                                                             | 3.24 ms: 1.13x faster                                                        |
| coroutines              | 26.3 ms                                                             | 23.4 ms: 1.12x faster                                                        |
| nbody                   | 96.7 ms                                                             | 87.5 ms: 1.11x faster                                                        |
| xml_etree_parse         | 162 ms                                                              | 149 ms: 1.09x faster                                                         |
| genshi_xml              | 51.8 ms                                                             | 47.7 ms: 1.09x faster                                                        |
| xml_etree_iterparse     | 108 ms                                                              | 99.3 ms: 1.08x faster                                                        |
| pickle_pure_python      | 307 us                                                              | 286 us: 1.07x faster                                                         |
| json_loads              | 26.2 us                                                             | 24.4 us: 1.07x faster                                                        |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.18 ms: 1.07x faster                                                        |
| hexiom                  | 6.48 ms                                                             | 6.08 ms: 1.07x faster                                                        |
| logging_simple          | 6.09 us                                                             | 5.73 us: 1.06x faster                                                        |
| tornado_http            | 96.7 ms                                                             | 91.2 ms: 1.06x faster                                                        |
| deepcopy_memo           | 36.4 us                                                             | 34.4 us: 1.06x faster                                                        |
| scimark_fft             | 328 ms                                                              | 310 ms: 1.06x faster                                                         |
| coverage                | 101 ms                                                              | 95.7 ms: 1.06x faster                                                        |
| spectral_norm           | 99.5 ms                                                             | 94.4 ms: 1.05x faster                                                        |
| logging_format          | 6.64 us                                                             | 6.34 us: 1.05x faster                                                        |
| mdp                     | 2.64 sec                                                            | 2.52 sec: 1.05x faster                                                       |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.05x faster                                                        |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                         |
| gunicorn                | 1.13 ms                                                             | 1.08 ms: 1.04x faster                                                        |
| deepcopy                | 339 us                                                              | 326 us: 1.04x faster                                                         |
| bench_thread_pool       | 820 us                                                              | 789 us: 1.04x faster                                                         |
| sqlglot_optimize        | 53.4 ms                                                             | 51.4 ms: 1.04x faster                                                        |
| meteor_contest          | 106 ms                                                              | 102 ms: 1.04x faster                                                         |
| float                   | 76.0 ms                                                             | 73.3 ms: 1.04x faster                                                        |
| json                    | 4.86 ms                                                             | 4.70 ms: 1.03x faster                                                        |
| pprint_safe_repr        | 701 ms                                                              | 678 ms: 1.03x faster                                                         |
| html5lib                | 64.0 ms                                                             | 61.9 ms: 1.03x faster                                                        |
| pprint_pformat          | 1.45 sec                                                            | 1.41 sec: 1.03x faster                                                       |
| pycparser               | 1.14 sec                                                            | 1.11 sec: 1.03x faster                                                       |
| sympy_expand            | 477 ms                                                              | 463 ms: 1.03x faster                                                         |
| richards                | 45.7 ms                                                             | 44.3 ms: 1.03x faster                                                        |
| nqueens                 | 84.0 ms                                                             | 81.6 ms: 1.03x faster                                                        |
| raytrace                | 292 ms                                                              | 285 ms: 1.03x faster                                                         |
| regex_v8                | 22.0 ms                                                             | 21.4 ms: 1.02x faster                                                        |
| sqlglot_normalize       | 108 ms                                                              | 106 ms: 1.02x faster                                                         |
| docutils                | 2.59 sec                                                            | 2.53 sec: 1.02x faster                                                       |
| 2to3                    | 257 ms                                                              | 251 ms: 1.02x faster                                                         |
| logging_silent          | 98.7 ns                                                             | 96.6 ns: 1.02x faster                                                        |
| scimark_sor             | 115 ms                                                              | 112 ms: 1.02x faster                                                         |
| sqlalchemy_declarative  | 138 ms                                                              | 136 ms: 1.02x faster                                                         |
| sympy_str               | 291 ms                                                              | 286 ms: 1.02x faster                                                         |
| sympy_integrate         | 21.0 ms                                                             | 20.6 ms: 1.02x faster                                                        |
| genshi_text             | 21.8 ms                                                             | 21.4 ms: 1.02x faster                                                        |
| regex_compile           | 137 ms                                                              | 134 ms: 1.02x faster                                                         |
| chameleon               | 6.52 ms                                                             | 6.41 ms: 1.02x faster                                                        |
| sqlalchemy_imperative   | 18.0 ms                                                             | 17.7 ms: 1.02x faster                                                        |
| telco                   | 6.59 ms                                                             | 6.49 ms: 1.02x faster                                                        |
| create_gc_cycles        | 1.48 ms                                                             | 1.46 ms: 1.01x faster                                                        |
| sympy_sum               | 167 ms                                                              | 166 ms: 1.01x faster                                                         |
| dulwich_log             | 63.6 ms                                                             | 63.8 ms: 1.00x slower                                                        |
| chaos                   | 68.0 ms                                                             | 68.2 ms: 1.00x slower                                                        |
| unpickle_list           | 4.96 us                                                             | 4.99 us: 1.01x slower                                                        |
| deepcopy_reduce         | 2.96 us                                                             | 2.98 us: 1.01x slower                                                        |
| unpickle                | 13.2 us                                                             | 13.3 us: 1.01x slower                                                        |
| gc_traversal            | 3.63 ms                                                             | 3.66 ms: 1.01x slower                                                        |
| fannkuch                | 384 ms                                                              | 388 ms: 1.01x slower                                                         |
| django_template         | 32.9 ms                                                             | 33.3 ms: 1.01x slower                                                        |
| async_tree_io           | 1.28 sec                                                            | 1.30 sec: 1.01x slower                                                       |
| pickle_dict             | 30.9 us                                                             | 31.5 us: 1.02x slower                                                        |
| mako                    | 9.82 ms                                                             | 9.99 ms: 1.02x slower                                                        |
| go                      | 138 ms                                                              | 142 ms: 1.03x slower                                                         |
| xml_etree_process       | 54.1 ms                                                             | 55.7 ms: 1.03x slower                                                        |
| python_startup          | 8.49 ms                                                             | 8.79 ms: 1.03x slower                                                        |
| thrift                  | 766 us                                                              | 793 us: 1.04x slower                                                         |
| sqlite_synth            | 2.51 us                                                             | 2.62 us: 1.04x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                             | 1.73 ms: 1.04x slower                                                        |
| regex_dna               | 196 ms                                                              | 205 ms: 1.04x slower                                                         |
| async_tree_memoization  | 621 ms                                                              | 649 ms: 1.05x slower                                                         |
| sqlglot_parse           | 1.36 ms                                                             | 1.43 ms: 1.05x slower                                                        |
| regex_effbot            | 3.32 ms                                                             | 3.50 ms: 1.05x slower                                                        |
| xml_etree_generate      | 76.5 ms                                                             | 80.8 ms: 1.06x slower                                                        |
| pickle                  | 9.79 us                                                             | 10.5 us: 1.07x slower                                                        |
| comprehensions          | 22.2 us                                                             | 24.0 us: 1.08x slower                                                        |
| pickle_list             | 4.03 us                                                             | 4.36 us: 1.08x slower                                                        |
| python_startup_no_site  | 5.98 ms                                                             | 6.49 ms: 1.09x slower                                                        |
| async_generators        | 361 ms                                                              | 415 ms: 1.15x slower                                                         |
| dask                    | 368 ms                                                              | 508 ms: 1.38x slower                                                         |
| Geometric mean          | (ref)                                                               | 1.03x faster                                                                 |

Benchmark hidden because not significant (9): async_tree_none, pathlib, bench_mp_pool, crypto_pyaes, pyflate, scimark_lu, djangocms, async_tree_cpu_io_mixed, scimark_monte_carlo
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint
