
# Results vs. 3.11.0

- fork: brandtbucher
- ref: immortal_interpreter
- machine: linux-x86_64
- commit hash: 7f90633
- commit date: 2023-04-28
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 268 ms: 1.04x slower                                                         |
| docutils       | 2.59 sec                                                            | 2.73 sec: 1.06x slower                                                       |
| html5lib       | 64.0 ms                                                             | 65.1 ms: 1.02x slower                                                        |
| tornado_http   | 96.7 ms                                                             | 105 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 88.2 ms: 1.10x faster                                                        |
| pidigits       | 197 ms                                                              | 189 ms: 1.04x faster                                                         |
| float          | 76.0 ms                                                             | 82.1 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                               | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.4 ms: 1.02x slower                                                        |
| regex_effbot   | 3.32 ms                                                             | 3.41 ms: 1.03x slower                                                        |
| regex_dna      | 196 ms                                                              | 205 ms: 1.04x slower                                                         |
| regex_compile  | 137 ms                                                              | 143 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 10.2 ms: 1.23x faster                                                        |
| unpickle_pure_python | 228 us                                                              | 217 us: 1.05x faster                                                         |
| xml_etree_iterparse  | 108 ms                                                              | 105 ms: 1.03x faster                                                         |
| xml_etree_parse      | 162 ms                                                              | 158 ms: 1.03x faster                                                         |
| json_loads           | 26.2 us                                                             | 25.8 us: 1.02x faster                                                        |
| unpickle_list        | 4.96 us                                                             | 4.91 us: 1.01x faster                                                        |
| pickle_pure_python   | 307 us                                                              | 317 us: 1.03x slower                                                         |
| pickle_dict          | 30.9 us                                                             | 32.6 us: 1.05x slower                                                        |
| xml_etree_process    | 54.1 ms                                                             | 58.7 ms: 1.09x slower                                                        |
| pickle               | 9.79 us                                                             | 10.8 us: 1.10x slower                                                        |
| xml_etree_generate   | 76.5 ms                                                             | 84.2 ms: 1.10x slower                                                        |
| unpickle             | 13.2 us                                                             | 14.9 us: 1.13x slower                                                        |
| pickle_list          | 4.03 us                                                             | 4.70 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.08 ms: 1.07x slower                                                        |
| python_startup_no_site | 5.98 ms                                                             | 6.66 ms: 1.11x slower                                                        |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                             | 50.8 ms: 1.02x faster                                                        |
| genshi_text    | 21.8 ms                                                             | 22.7 ms: 1.04x slower                                                        |
| mako           | 9.82 ms                                                             | 10.9 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 31.1 ms: 2.36x faster                                                        |
| asyncio_tcp             | 888 ms                                                              | 508 ms: 1.75x faster                                                         |
| json_dumps              | 12.5 ms                                                             | 10.2 ms: 1.23x faster                                                        |
| mypy2                   | 422 ms                                                              | 352 ms: 1.20x faster                                                         |
| coroutines              | 26.3 ms                                                             | 22.4 ms: 1.17x faster                                                        |
| nbody                   | 96.7 ms                                                             | 88.2 ms: 1.10x faster                                                        |
| hexiom                  | 6.48 ms                                                             | 6.08 ms: 1.07x faster                                                        |
| nqueens                 | 84.0 ms                                                             | 79.3 ms: 1.06x faster                                                        |
| unpickle_pure_python    | 228 us                                                              | 217 us: 1.05x faster                                                         |
| richards                | 45.7 ms                                                             | 43.4 ms: 1.05x faster                                                        |
| pidigits                | 197 ms                                                              | 189 ms: 1.04x faster                                                         |
| deltablue               | 3.66 ms                                                             | 3.53 ms: 1.04x faster                                                        |
| xml_etree_iterparse     | 108 ms                                                              | 105 ms: 1.03x faster                                                         |
| xml_etree_parse         | 162 ms                                                              | 158 ms: 1.03x faster                                                         |
| fannkuch                | 384 ms                                                              | 376 ms: 1.02x faster                                                         |
| genshi_xml              | 51.8 ms                                                             | 50.8 ms: 1.02x faster                                                        |
| sqlglot_parse           | 1.36 ms                                                             | 1.34 ms: 1.02x faster                                                        |
| pathlib                 | 18.2 ms                                                             | 17.9 ms: 1.02x faster                                                        |
| json_loads              | 26.2 us                                                             | 25.8 us: 1.02x faster                                                        |
| mdp                     | 2.64 sec                                                            | 2.60 sec: 1.01x faster                                                       |
| go                      | 138 ms                                                              | 137 ms: 1.01x faster                                                         |
| unpickle_list           | 4.96 us                                                             | 4.91 us: 1.01x faster                                                        |
| async_tree_io           | 1.28 sec                                                            | 1.27 sec: 1.01x faster                                                       |
| coverage                | 101 ms                                                              | 100 ms: 1.01x faster                                                         |
| logging_silent          | 98.7 ns                                                             | 98.2 ns: 1.01x faster                                                        |
| chaos                   | 68.0 ms                                                             | 68.8 ms: 1.01x slower                                                        |
| pprint_pformat          | 1.45 sec                                                            | 1.47 sec: 1.01x slower                                                       |
| create_gc_cycles        | 1.48 ms                                                             | 1.50 ms: 1.02x slower                                                        |
| html5lib                | 64.0 ms                                                             | 65.1 ms: 1.02x slower                                                        |
| pycparser               | 1.14 sec                                                            | 1.16 sec: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 736 ms                                                              | 749 ms: 1.02x slower                                                         |
| bench_thread_pool       | 820 us                                                              | 835 us: 1.02x slower                                                         |
| regex_v8                | 22.0 ms                                                             | 22.4 ms: 1.02x slower                                                        |
| sqlglot_optimize        | 53.4 ms                                                             | 54.4 ms: 1.02x slower                                                        |
| scimark_lu              | 108 ms                                                              | 111 ms: 1.02x slower                                                         |
| logging_simple          | 6.09 us                                                             | 6.24 us: 1.02x slower                                                        |
| sqlglot_normalize       | 108 ms                                                              | 111 ms: 1.03x slower                                                         |
| regex_effbot            | 3.32 ms                                                             | 3.41 ms: 1.03x slower                                                        |
| pprint_safe_repr        | 701 ms                                                              | 721 ms: 1.03x slower                                                         |
| raytrace                | 292 ms                                                              | 301 ms: 1.03x slower                                                         |
| pickle_pure_python      | 307 us                                                              | 317 us: 1.03x slower                                                         |
| comprehensions          | 22.2 us                                                             | 23.1 us: 1.04x slower                                                        |
| genshi_text             | 21.8 ms                                                             | 22.7 ms: 1.04x slower                                                        |
| logging_format          | 6.64 us                                                             | 6.91 us: 1.04x slower                                                        |
| regex_dna               | 196 ms                                                              | 205 ms: 1.04x slower                                                         |
| 2to3                    | 257 ms                                                              | 268 ms: 1.04x slower                                                         |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.69 ms: 1.05x slower                                                        |
| thrift                  | 766 us                                                              | 803 us: 1.05x slower                                                         |
| meteor_contest          | 106 ms                                                              | 112 ms: 1.05x slower                                                         |
| regex_compile           | 137 ms                                                              | 143 ms: 1.05x slower                                                         |
| scimark_monte_carlo     | 67.8 ms                                                             | 71.3 ms: 1.05x slower                                                        |
| unpack_sequence         | 49.5 ns                                                             | 52.1 ns: 1.05x slower                                                        |
| pickle_dict             | 30.9 us                                                             | 32.6 us: 1.05x slower                                                        |
| docutils                | 2.59 sec                                                            | 2.73 sec: 1.06x slower                                                       |
| dulwich_log             | 63.6 ms                                                             | 67.3 ms: 1.06x slower                                                        |
| sqlalchemy_declarative  | 138 ms                                                              | 147 ms: 1.06x slower                                                         |
| async_tree_memoization  | 621 ms                                                              | 661 ms: 1.06x slower                                                         |
| crypto_pyaes            | 73.8 ms                                                             | 78.6 ms: 1.07x slower                                                        |
| sqlite_synth            | 2.51 us                                                             | 2.69 us: 1.07x slower                                                        |
| python_startup          | 8.49 ms                                                             | 9.08 ms: 1.07x slower                                                        |
| scimark_sor             | 115 ms                                                              | 123 ms: 1.07x slower                                                         |
| deepcopy_reduce         | 2.96 us                                                             | 3.17 us: 1.07x slower                                                        |
| telco                   | 6.59 ms                                                             | 7.06 ms: 1.07x slower                                                        |
| pyflate                 | 414 ms                                                              | 444 ms: 1.07x slower                                                         |
| deepcopy_memo           | 36.4 us                                                             | 39.1 us: 1.07x slower                                                        |
| deepcopy                | 339 us                                                              | 365 us: 1.08x slower                                                         |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.5 ms: 1.08x slower                                                        |
| float                   | 76.0 ms                                                             | 82.1 ms: 1.08x slower                                                        |
| scimark_fft             | 328 ms                                                              | 355 ms: 1.08x slower                                                         |
| tornado_http            | 96.7 ms                                                             | 105 ms: 1.08x slower                                                         |
| xml_etree_process       | 54.1 ms                                                             | 58.7 ms: 1.09x slower                                                        |
| gc_traversal            | 3.63 ms                                                             | 3.94 ms: 1.09x slower                                                        |
| spectral_norm           | 99.5 ms                                                             | 108 ms: 1.09x slower                                                         |
| pickle                  | 9.79 us                                                             | 10.8 us: 1.10x slower                                                        |
| xml_etree_generate      | 76.5 ms                                                             | 84.2 ms: 1.10x slower                                                        |
| mako                    | 9.82 ms                                                             | 10.9 ms: 1.11x slower                                                        |
| python_startup_no_site  | 5.98 ms                                                             | 6.66 ms: 1.11x slower                                                        |
| unpickle                | 13.2 us                                                             | 14.9 us: 1.13x slower                                                        |
| pickle_list             | 4.03 us                                                             | 4.70 us: 1.17x slower                                                        |
| async_generators        | 361 ms                                                              | 439 ms: 1.21x slower                                                         |
| dask                    | 368 ms                                                              | 540 ms: 1.47x slower                                                         |
| Geometric mean          | (ref)                                                               | 1.01x slower                                                                 |

Benchmark hidden because not significant (4): bench_mp_pool, async_tree_none, json, sqlglot_transpile
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
