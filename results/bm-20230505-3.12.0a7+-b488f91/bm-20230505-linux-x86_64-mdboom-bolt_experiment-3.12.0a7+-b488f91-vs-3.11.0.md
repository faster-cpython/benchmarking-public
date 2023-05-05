
# Results vs. 3.11.0

- fork: mdboom
- ref: bolt_experiment
- machine: linux-x86_64
- commit hash: b488f91
- commit date: 2023-05-05
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 270 ms: 1.05x slower                                              |
| docutils       | 2.59 sec                                                            | 2.73 sec: 1.06x slower                                            |
| tornado_http   | 96.7 ms                                                             | 102 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                               | 1.05x slower                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 87.7 ms: 1.10x faster                                             |
| pidigits       | 197 ms                                                              | 189 ms: 1.04x faster                                              |
| float          | 76.0 ms                                                             | 81.6 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                               | 1.02x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 196 ms                                                              | 203 ms: 1.04x slower                                              |
| regex_compile  | 137 ms                                                              | 146 ms: 1.07x slower                                              |
| regex_effbot   | 3.32 ms                                                             | 3.81 ms: 1.15x slower                                             |
| Geometric mean | (ref)                                                               | 1.06x slower                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.92 ms: 1.26x faster                                             |
| xml_etree_parse      | 162 ms                                                              | 154 ms: 1.05x faster                                              |
| unpickle_pure_python | 228 us                                                              | 220 us: 1.04x faster                                              |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.04x faster                                              |
| json_loads           | 26.2 us                                                             | 25.7 us: 1.02x faster                                             |
| unpickle_list        | 4.96 us                                                             | 4.88 us: 1.02x faster                                             |
| pickle_dict          | 30.9 us                                                             | 31.7 us: 1.02x slower                                             |
| pickle_pure_python   | 307 us                                                              | 323 us: 1.05x slower                                              |
| pickle               | 9.79 us                                                             | 10.6 us: 1.09x slower                                             |
| xml_etree_process    | 54.1 ms                                                             | 59.7 ms: 1.10x slower                                             |
| xml_etree_generate   | 76.5 ms                                                             | 85.3 ms: 1.11x slower                                             |
| pickle_list          | 4.03 us                                                             | 4.57 us: 1.13x slower                                             |
| unpickle             | 13.2 us                                                             | 15.0 us: 1.13x slower                                             |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.14 ms: 1.08x slower                                             |
| python_startup_no_site | 5.98 ms                                                             | 6.67 ms: 1.12x slower                                             |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|-----------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako      | 9.82 ms                                                             | 10.9 ms: 1.11x slower                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 30.7 ms: 2.39x faster                                             |
| asyncio_tcp             | 888 ms                                                              | 510 ms: 1.74x faster                                              |
| json_dumps              | 12.5 ms                                                             | 9.92 ms: 1.26x faster                                             |
| mypy2                   | 422 ms                                                              | 353 ms: 1.20x faster                                              |
| coroutines              | 26.3 ms                                                             | 22.2 ms: 1.18x faster                                             |
| nbody                   | 96.7 ms                                                             | 87.7 ms: 1.10x faster                                             |
| unpack_sequence         | 49.5 ns                                                             | 46.6 ns: 1.06x faster                                             |
| xml_etree_parse         | 162 ms                                                              | 154 ms: 1.05x faster                                              |
| async_tree_none         | 525 ms                                                              | 500 ms: 1.05x faster                                              |
| pidigits                | 197 ms                                                              | 189 ms: 1.04x faster                                              |
| unpickle_pure_python    | 228 us                                                              | 220 us: 1.04x faster                                              |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.04x faster                                              |
| async_tree_io           | 1.28 sec                                                            | 1.24 sec: 1.03x faster                                            |
| deltablue               | 3.66 ms                                                             | 3.56 ms: 1.03x faster                                             |
| richards                | 45.7 ms                                                             | 44.6 ms: 1.02x faster                                             |
| nqueens                 | 84.0 ms                                                             | 82.1 ms: 1.02x faster                                             |
| fannkuch                | 384 ms                                                              | 375 ms: 1.02x faster                                              |
| json_loads              | 26.2 us                                                             | 25.7 us: 1.02x faster                                             |
| async_tree_cpu_io_mixed | 736 ms                                                              | 723 ms: 1.02x faster                                              |
| unpickle_list           | 4.96 us                                                             | 4.88 us: 1.02x faster                                             |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                              |
| sqlglot_parse           | 1.36 ms                                                             | 1.34 ms: 1.01x faster                                             |
| hexiom                  | 6.48 ms                                                             | 6.41 ms: 1.01x faster                                             |
| mdp                     | 2.64 sec                                                            | 2.61 sec: 1.01x faster                                            |
| go                      | 138 ms                                                              | 138 ms: 1.01x faster                                              |
| sqlglot_transpile       | 1.65 ms                                                             | 1.67 ms: 1.01x slower                                             |
| gc_traversal            | 3.63 ms                                                             | 3.68 ms: 1.01x slower                                             |
| json                    | 4.86 ms                                                             | 4.94 ms: 1.02x slower                                             |
| coverage                | 101 ms                                                              | 103 ms: 1.02x slower                                              |
| bench_thread_pool       | 820 us                                                              | 837 us: 1.02x slower                                              |
| pickle_dict             | 30.9 us                                                             | 31.7 us: 1.02x slower                                             |
| chaos                   | 68.0 ms                                                             | 69.8 ms: 1.03x slower                                             |
| pathlib                 | 18.2 ms                                                             | 18.8 ms: 1.03x slower                                             |
| telco                   | 6.59 ms                                                             | 6.82 ms: 1.04x slower                                             |
| regex_dna               | 196 ms                                                              | 203 ms: 1.04x slower                                              |
| sqlglot_optimize        | 53.4 ms                                                             | 55.6 ms: 1.04x slower                                             |
| sqlglot_normalize       | 108 ms                                                              | 113 ms: 1.05x slower                                              |
| comprehensions          | 22.2 us                                                             | 23.3 us: 1.05x slower                                             |
| 2to3                    | 257 ms                                                              | 270 ms: 1.05x slower                                              |
| pickle_pure_python      | 307 us                                                              | 323 us: 1.05x slower                                              |
| logging_silent          | 98.7 ns                                                             | 104 ns: 1.05x slower                                              |
| deepcopy_memo           | 36.4 us                                                             | 38.3 us: 1.05x slower                                             |
| pprint_pformat          | 1.45 sec                                                            | 1.53 sec: 1.05x slower                                            |
| tornado_http            | 96.7 ms                                                             | 102 ms: 1.06x slower                                              |
| docutils                | 2.59 sec                                                            | 2.73 sec: 1.06x slower                                            |
| raytrace                | 292 ms                                                              | 310 ms: 1.06x slower                                              |
| logging_simple          | 6.09 us                                                             | 6.47 us: 1.06x slower                                             |
| sqlalchemy_declarative  | 138 ms                                                              | 147 ms: 1.07x slower                                              |
| pprint_safe_repr        | 701 ms                                                              | 750 ms: 1.07x slower                                              |
| regex_compile           | 137 ms                                                              | 146 ms: 1.07x slower                                              |
| deepcopy                | 339 us                                                              | 363 us: 1.07x slower                                              |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.3 ms: 1.07x slower                                             |
| logging_format          | 6.64 us                                                             | 7.12 us: 1.07x slower                                             |
| scimark_lu              | 108 ms                                                              | 116 ms: 1.07x slower                                              |
| dulwich_log             | 63.6 ms                                                             | 68.3 ms: 1.07x slower                                             |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.80 ms: 1.07x slower                                             |
| float                   | 76.0 ms                                                             | 81.6 ms: 1.07x slower                                             |
| python_startup          | 8.49 ms                                                             | 9.14 ms: 1.08x slower                                             |
| deepcopy_reduce         | 2.96 us                                                             | 3.19 us: 1.08x slower                                             |
| pyflate                 | 414 ms                                                              | 447 ms: 1.08x slower                                              |
| scimark_sor             | 115 ms                                                              | 124 ms: 1.08x slower                                              |
| scimark_fft             | 328 ms                                                              | 355 ms: 1.08x slower                                              |
| scimark_monte_carlo     | 67.8 ms                                                             | 73.6 ms: 1.09x slower                                             |
| pickle                  | 9.79 us                                                             | 10.6 us: 1.09x slower                                             |
| crypto_pyaes            | 73.8 ms                                                             | 80.4 ms: 1.09x slower                                             |
| xml_etree_process       | 54.1 ms                                                             | 59.7 ms: 1.10x slower                                             |
| sqlite_synth            | 2.51 us                                                             | 2.79 us: 1.11x slower                                             |
| mako                    | 9.82 ms                                                             | 10.9 ms: 1.11x slower                                             |
| spectral_norm           | 99.5 ms                                                             | 111 ms: 1.11x slower                                              |
| xml_etree_generate      | 76.5 ms                                                             | 85.3 ms: 1.11x slower                                             |
| python_startup_no_site  | 5.98 ms                                                             | 6.67 ms: 1.12x slower                                             |
| pickle_list             | 4.03 us                                                             | 4.57 us: 1.13x slower                                             |
| unpickle                | 13.2 us                                                             | 15.0 us: 1.13x slower                                             |
| regex_effbot            | 3.32 ms                                                             | 3.81 ms: 1.15x slower                                             |
| async_generators        | 361 ms                                                              | 459 ms: 1.27x slower                                              |
| dask                    | 368 ms                                                              | 542 ms: 1.47x slower                                              |
| Geometric mean          | (ref)                                                               | 1.01x slower                                                      |

Benchmark hidden because not significant (5): async_tree_memoization, pycparser, bench_mp_pool, create_gc_cycles, regex_v8
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
