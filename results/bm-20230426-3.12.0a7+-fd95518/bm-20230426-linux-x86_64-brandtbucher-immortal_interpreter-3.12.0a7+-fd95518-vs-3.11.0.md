
# Results vs. 3.11.0

- fork: brandtbucher
- ref: immortal_interpreter
- machine: linux-x86_64
- commit hash: fd95518
- commit date: 2023-04-26
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 269 ms: 1.05x slower                                                         |
| chameleon      | 6.52 ms                                                             | 7.01 ms: 1.08x slower                                                        |
| docutils       | 2.59 sec                                                            | 2.72 sec: 1.05x slower                                                       |
| html5lib       | 64.0 ms                                                             | 65.6 ms: 1.02x slower                                                        |
| tornado_http   | 96.7 ms                                                             | 106 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 88.5 ms: 1.09x faster                                                        |
| pidigits       | 197 ms                                                              | 189 ms: 1.04x faster                                                         |
| float          | 76.0 ms                                                             | 81.1 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                               | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.4 ms: 1.02x slower                                                        |
| regex_compile  | 137 ms                                                              | 143 ms: 1.05x slower                                                         |
| regex_effbot   | 3.32 ms                                                             | 3.49 ms: 1.05x slower                                                        |
| regex_dna      | 196 ms                                                              | 207 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.92 ms: 1.26x faster                                                        |
| unpickle_pure_python | 228 us                                                              | 216 us: 1.06x faster                                                         |
| xml_etree_parse      | 162 ms                                                              | 154 ms: 1.05x faster                                                         |
| xml_etree_iterparse  | 108 ms                                                              | 103 ms: 1.05x faster                                                         |
| json_loads           | 26.2 us                                                             | 25.6 us: 1.02x faster                                                        |
| unpickle_list        | 4.96 us                                                             | 4.91 us: 1.01x faster                                                        |
| pickle_pure_python   | 307 us                                                              | 315 us: 1.03x slower                                                         |
| pickle               | 9.79 us                                                             | 10.4 us: 1.06x slower                                                        |
| xml_etree_process    | 54.1 ms                                                             | 58.8 ms: 1.09x slower                                                        |
| xml_etree_generate   | 76.5 ms                                                             | 84.6 ms: 1.11x slower                                                        |
| unpickle             | 13.2 us                                                             | 14.7 us: 1.11x slower                                                        |
| pickle_list          | 4.03 us                                                             | 4.52 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                               | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.13 ms: 1.07x slower                                                        |
| python_startup_no_site | 5.98 ms                                                             | 6.69 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 21.8 ms                                                             | 22.8 ms: 1.04x slower                                                        |
| django_template | 32.9 ms                                                             | 34.7 ms: 1.06x slower                                                        |
| mako            | 9.82 ms                                                             | 10.8 ms: 1.10x slower                                                        |
| Geometric mean  | (ref)                                                               | 1.05x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 31.2 ms: 2.35x faster                                                        |
| asyncio_tcp             | 888 ms                                                              | 505 ms: 1.76x faster                                                         |
| json_dumps              | 12.5 ms                                                             | 9.92 ms: 1.26x faster                                                        |
| mypy2                   | 422 ms                                                              | 349 ms: 1.21x faster                                                         |
| coroutines              | 26.3 ms                                                             | 23.0 ms: 1.14x faster                                                        |
| nbody                   | 96.7 ms                                                             | 88.5 ms: 1.09x faster                                                        |
| hexiom                  | 6.48 ms                                                             | 6.13 ms: 1.06x faster                                                        |
| unpickle_pure_python    | 228 us                                                              | 216 us: 1.06x faster                                                         |
| richards                | 45.7 ms                                                             | 43.4 ms: 1.05x faster                                                        |
| xml_etree_parse         | 162 ms                                                              | 154 ms: 1.05x faster                                                         |
| nqueens                 | 84.0 ms                                                             | 79.8 ms: 1.05x faster                                                        |
| xml_etree_iterparse     | 108 ms                                                              | 103 ms: 1.05x faster                                                         |
| pidigits                | 197 ms                                                              | 189 ms: 1.04x faster                                                         |
| deltablue               | 3.66 ms                                                             | 3.53 ms: 1.04x faster                                                        |
| sqlglot_parse           | 1.36 ms                                                             | 1.32 ms: 1.03x faster                                                        |
| fannkuch                | 384 ms                                                              | 374 ms: 1.03x faster                                                         |
| json_loads              | 26.2 us                                                             | 25.6 us: 1.02x faster                                                        |
| mdp                     | 2.64 sec                                                            | 2.59 sec: 1.02x faster                                                       |
| unpickle_list           | 4.96 us                                                             | 4.91 us: 1.01x faster                                                        |
| coverage                | 101 ms                                                              | 100 ms: 1.01x faster                                                         |
| logging_silent          | 98.7 ns                                                             | 99.0 ns: 1.00x slower                                                        |
| json                    | 4.86 ms                                                             | 4.91 ms: 1.01x slower                                                        |
| pprint_pformat          | 1.45 sec                                                            | 1.47 sec: 1.01x slower                                                       |
| pathlib                 | 18.2 ms                                                             | 18.5 ms: 1.01x slower                                                        |
| scimark_lu              | 108 ms                                                              | 110 ms: 1.02x slower                                                         |
| sqlglot_optimize        | 53.4 ms                                                             | 54.3 ms: 1.02x slower                                                        |
| bench_thread_pool       | 820 us                                                              | 835 us: 1.02x slower                                                         |
| chaos                   | 68.0 ms                                                             | 69.2 ms: 1.02x slower                                                        |
| create_gc_cycles        | 1.48 ms                                                             | 1.51 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                              | 750 ms: 1.02x slower                                                         |
| regex_v8                | 22.0 ms                                                             | 22.4 ms: 1.02x slower                                                        |
| logging_simple          | 6.09 us                                                             | 6.22 us: 1.02x slower                                                        |
| html5lib                | 64.0 ms                                                             | 65.6 ms: 1.02x slower                                                        |
| pickle_pure_python      | 307 us                                                              | 315 us: 1.03x slower                                                         |
| raytrace                | 292 ms                                                              | 300 ms: 1.03x slower                                                         |
| sqlglot_normalize       | 108 ms                                                              | 112 ms: 1.03x slower                                                         |
| djangocms               | 32.3 us                                                             | 33.3 us: 1.03x slower                                                        |
| pprint_safe_repr        | 701 ms                                                              | 724 ms: 1.03x slower                                                         |
| sympy_integrate         | 21.0 ms                                                             | 21.9 ms: 1.04x slower                                                        |
| genshi_text             | 21.8 ms                                                             | 22.8 ms: 1.04x slower                                                        |
| thrift                  | 766 us                                                              | 800 us: 1.05x slower                                                         |
| sympy_expand            | 477 ms                                                              | 498 ms: 1.05x slower                                                         |
| async_tree_memoization  | 621 ms                                                              | 650 ms: 1.05x slower                                                         |
| telco                   | 6.59 ms                                                             | 6.90 ms: 1.05x slower                                                        |
| 2to3                    | 257 ms                                                              | 269 ms: 1.05x slower                                                         |
| logging_format          | 6.64 us                                                             | 6.96 us: 1.05x slower                                                        |
| regex_compile           | 137 ms                                                              | 143 ms: 1.05x slower                                                         |
| regex_effbot            | 3.32 ms                                                             | 3.49 ms: 1.05x slower                                                        |
| comprehensions          | 22.2 us                                                             | 23.4 us: 1.05x slower                                                        |
| scimark_monte_carlo     | 67.8 ms                                                             | 71.3 ms: 1.05x slower                                                        |
| docutils                | 2.59 sec                                                            | 2.72 sec: 1.05x slower                                                       |
| sqlalchemy_declarative  | 138 ms                                                              | 146 ms: 1.05x slower                                                         |
| regex_dna               | 196 ms                                                              | 207 ms: 1.05x slower                                                         |
| spectral_norm           | 99.5 ms                                                             | 105 ms: 1.05x slower                                                         |
| django_template         | 32.9 ms                                                             | 34.7 ms: 1.06x slower                                                        |
| deepcopy_memo           | 36.4 us                                                             | 38.5 us: 1.06x slower                                                        |
| meteor_contest          | 106 ms                                                              | 112 ms: 1.06x slower                                                         |
| pickle                  | 9.79 us                                                             | 10.4 us: 1.06x slower                                                        |
| scimark_sor             | 115 ms                                                              | 122 ms: 1.06x slower                                                         |
| dulwich_log             | 63.6 ms                                                             | 67.8 ms: 1.07x slower                                                        |
| sympy_str               | 291 ms                                                              | 311 ms: 1.07x slower                                                         |
| float                   | 76.0 ms                                                             | 81.1 ms: 1.07x slower                                                        |
| scimark_fft             | 328 ms                                                              | 352 ms: 1.07x slower                                                         |
| python_startup          | 8.49 ms                                                             | 9.13 ms: 1.07x slower                                                        |
| chameleon               | 6.52 ms                                                             | 7.01 ms: 1.08x slower                                                        |
| sqlite_synth            | 2.51 us                                                             | 2.71 us: 1.08x slower                                                        |
| deepcopy_reduce         | 2.96 us                                                             | 3.19 us: 1.08x slower                                                        |
| pyflate                 | 414 ms                                                              | 446 ms: 1.08x slower                                                         |
| deepcopy                | 339 us                                                              | 366 us: 1.08x slower                                                         |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.5 ms: 1.08x slower                                                        |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.85 ms: 1.08x slower                                                        |
| xml_etree_process       | 54.1 ms                                                             | 58.8 ms: 1.09x slower                                                        |
| crypto_pyaes            | 73.8 ms                                                             | 80.5 ms: 1.09x slower                                                        |
| unpack_sequence         | 49.5 ns                                                             | 54.1 ns: 1.09x slower                                                        |
| tornado_http            | 96.7 ms                                                             | 106 ms: 1.09x slower                                                         |
| sympy_sum               | 167 ms                                                              | 183 ms: 1.09x slower                                                         |
| mako                    | 9.82 ms                                                             | 10.8 ms: 1.10x slower                                                        |
| gc_traversal            | 3.63 ms                                                             | 3.99 ms: 1.10x slower                                                        |
| xml_etree_generate      | 76.5 ms                                                             | 84.6 ms: 1.11x slower                                                        |
| unpickle                | 13.2 us                                                             | 14.7 us: 1.11x slower                                                        |
| python_startup_no_site  | 5.98 ms                                                             | 6.69 ms: 1.12x slower                                                        |
| pickle_list             | 4.03 us                                                             | 4.52 us: 1.12x slower                                                        |
| async_generators        | 361 ms                                                              | 437 ms: 1.21x slower                                                         |
| dask                    | 368 ms                                                              | 539 ms: 1.46x slower                                                         |
| Geometric mean          | (ref)                                                               | 1.01x slower                                                                 |

Benchmark hidden because not significant (9): pylint, sqlglot_transpile, genshi_xml, bench_mp_pool, pickle_dict, async_tree_io, go, pycparser, async_tree_none
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn
