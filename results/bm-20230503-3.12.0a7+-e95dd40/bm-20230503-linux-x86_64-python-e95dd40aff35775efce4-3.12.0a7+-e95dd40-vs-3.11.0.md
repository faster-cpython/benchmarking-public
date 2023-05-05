
# Results vs. 3.11.0

- fork: python
- ref: e95dd40aff35775efce4
- machine: linux-x86_64
- commit hash: e95dd40
- commit date: 2023-05-03
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 271 ms: 1.05x slower                                                   |
| docutils       | 2.59 sec                                                            | 2.73 sec: 1.05x slower                                                 |
| tornado_http   | 96.7 ms                                                             | 99.5 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                               | 1.05x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 87.5 ms: 1.11x faster                                                  |
| pidigits       | 197 ms                                                              | 197 ms: 1.00x slower                                                   |
| float          | 76.0 ms                                                             | 83.2 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                               | 1.00x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.1 ms: 1.01x slower                                                  |
| regex_dna      | 196 ms                                                              | 200 ms: 1.02x slower                                                   |
| regex_compile  | 137 ms                                                              | 145 ms: 1.06x slower                                                   |
| regex_effbot   | 3.32 ms                                                             | 3.69 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                               | 1.05x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.98 ms: 1.26x faster                                                  |
| xml_etree_parse      | 162 ms                                                              | 154 ms: 1.05x faster                                                   |
| unpickle_pure_python | 228 us                                                              | 219 us: 1.04x faster                                                   |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.03x faster                                                   |
| json_loads           | 26.2 us                                                             | 25.8 us: 1.01x faster                                                  |
| pickle_dict          | 30.9 us                                                             | 30.7 us: 1.01x faster                                                  |
| unpickle_list        | 4.96 us                                                             | 5.02 us: 1.01x slower                                                  |
| pickle_pure_python   | 307 us                                                              | 313 us: 1.02x slower                                                   |
| pickle               | 9.79 us                                                             | 10.5 us: 1.07x slower                                                  |
| xml_etree_process    | 54.1 ms                                                             | 59.2 ms: 1.10x slower                                                  |
| xml_etree_generate   | 76.5 ms                                                             | 84.7 ms: 1.11x slower                                                  |
| pickle_list          | 4.03 us                                                             | 4.50 us: 1.12x slower                                                  |
| unpickle             | 13.2 us                                                             | 15.0 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.20 ms: 1.08x slower                                                  |
| python_startup_no_site | 5.98 ms                                                             | 6.73 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-----------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 9.82 ms                                                             | 10.7 ms: 1.09x slower                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-linux-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 31.4 ms: 2.34x faster                                                  |
| asyncio_tcp             | 888 ms                                                              | 506 ms: 1.76x faster                                                   |
| json_dumps              | 12.5 ms                                                             | 9.98 ms: 1.26x faster                                                  |
| mypy2                   | 422 ms                                                              | 351 ms: 1.20x faster                                                   |
| coroutines              | 26.3 ms                                                             | 23.7 ms: 1.11x faster                                                  |
| nbody                   | 96.7 ms                                                             | 87.5 ms: 1.11x faster                                                  |
| async_tree_none         | 525 ms                                                              | 497 ms: 1.06x faster                                                   |
| async_tree_io           | 1.28 sec                                                            | 1.22 sec: 1.05x faster                                                 |
| xml_etree_parse         | 162 ms                                                              | 154 ms: 1.05x faster                                                   |
| hexiom                  | 6.48 ms                                                             | 6.18 ms: 1.05x faster                                                  |
| unpickle_pure_python    | 228 us                                                              | 219 us: 1.04x faster                                                   |
| deltablue               | 3.66 ms                                                             | 3.52 ms: 1.04x faster                                                  |
| nqueens                 | 84.0 ms                                                             | 80.9 ms: 1.04x faster                                                  |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.03x faster                                                   |
| async_tree_memoization  | 621 ms                                                              | 604 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed | 736 ms                                                              | 719 ms: 1.02x faster                                                   |
| go                      | 138 ms                                                              | 136 ms: 1.02x faster                                                   |
| json_loads              | 26.2 us                                                             | 25.8 us: 1.01x faster                                                  |
| richards                | 45.7 ms                                                             | 45.0 ms: 1.01x faster                                                  |
| fannkuch                | 384 ms                                                              | 380 ms: 1.01x faster                                                   |
| pickle_dict             | 30.9 us                                                             | 30.7 us: 1.01x faster                                                  |
| sqlglot_parse           | 1.36 ms                                                             | 1.35 ms: 1.01x faster                                                  |
| pidigits                | 197 ms                                                              | 197 ms: 1.00x slower                                                   |
| create_gc_cycles        | 1.48 ms                                                             | 1.49 ms: 1.00x slower                                                  |
| regex_v8                | 22.0 ms                                                             | 22.1 ms: 1.01x slower                                                  |
| unpickle_list           | 4.96 us                                                             | 5.02 us: 1.01x slower                                                  |
| sqlglot_transpile       | 1.65 ms                                                             | 1.68 ms: 1.01x slower                                                  |
| pathlib                 | 18.2 ms                                                             | 18.5 ms: 1.02x slower                                                  |
| coverage                | 101 ms                                                              | 103 ms: 1.02x slower                                                   |
| regex_dna               | 196 ms                                                              | 200 ms: 1.02x slower                                                   |
| pickle_pure_python      | 307 us                                                              | 313 us: 1.02x slower                                                   |
| telco                   | 6.59 ms                                                             | 6.73 ms: 1.02x slower                                                  |
| logging_silent          | 98.7 ns                                                             | 101 ns: 1.02x slower                                                   |
| bench_thread_pool       | 820 us                                                              | 838 us: 1.02x slower                                                   |
| pprint_pformat          | 1.45 sec                                                            | 1.49 sec: 1.03x slower                                                 |
| tornado_http            | 96.7 ms                                                             | 99.5 ms: 1.03x slower                                                  |
| json                    | 4.86 ms                                                             | 5.01 ms: 1.03x slower                                                  |
| unpack_sequence         | 49.5 ns                                                             | 51.1 ns: 1.03x slower                                                  |
| chaos                   | 68.0 ms                                                             | 70.4 ms: 1.04x slower                                                  |
| raytrace                | 292 ms                                                              | 303 ms: 1.04x slower                                                   |
| sqlglot_optimize        | 53.4 ms                                                             | 55.5 ms: 1.04x slower                                                  |
| logging_simple          | 6.09 us                                                             | 6.34 us: 1.04x slower                                                  |
| mdp                     | 2.64 sec                                                            | 2.75 sec: 1.04x slower                                                 |
| sqlglot_normalize       | 108 ms                                                              | 113 ms: 1.04x slower                                                   |
| pprint_safe_repr        | 701 ms                                                              | 732 ms: 1.04x slower                                                   |
| scimark_lu              | 108 ms                                                              | 113 ms: 1.05x slower                                                   |
| comprehensions          | 22.2 us                                                             | 23.3 us: 1.05x slower                                                  |
| sqlalchemy_imperative   | 18.0 ms                                                             | 18.9 ms: 1.05x slower                                                  |
| docutils                | 2.59 sec                                                            | 2.73 sec: 1.05x slower                                                 |
| 2to3                    | 257 ms                                                              | 271 ms: 1.05x slower                                                   |
| crypto_pyaes            | 73.8 ms                                                             | 78.0 ms: 1.06x slower                                                  |
| deepcopy_memo           | 36.4 us                                                             | 38.5 us: 1.06x slower                                                  |
| sqlalchemy_declarative  | 138 ms                                                              | 147 ms: 1.06x slower                                                   |
| meteor_contest          | 106 ms                                                              | 113 ms: 1.06x slower                                                   |
| logging_format          | 6.64 us                                                             | 7.06 us: 1.06x slower                                                  |
| regex_compile           | 137 ms                                                              | 145 ms: 1.06x slower                                                   |
| pickle                  | 9.79 us                                                             | 10.5 us: 1.07x slower                                                  |
| dulwich_log             | 63.6 ms                                                             | 68.3 ms: 1.07x slower                                                  |
| scimark_sor             | 115 ms                                                              | 124 ms: 1.08x slower                                                   |
| python_startup          | 8.49 ms                                                             | 9.20 ms: 1.08x slower                                                  |
| spectral_norm           | 99.5 ms                                                             | 108 ms: 1.08x slower                                                   |
| sqlite_synth            | 2.51 us                                                             | 2.72 us: 1.08x slower                                                  |
| deepcopy                | 339 us                                                              | 368 us: 1.09x slower                                                   |
| scimark_monte_carlo     | 67.8 ms                                                             | 73.6 ms: 1.09x slower                                                  |
| mako                    | 9.82 ms                                                             | 10.7 ms: 1.09x slower                                                  |
| deepcopy_reduce         | 2.96 us                                                             | 3.22 us: 1.09x slower                                                  |
| pyflate                 | 414 ms                                                              | 451 ms: 1.09x slower                                                   |
| gc_traversal            | 3.63 ms                                                             | 3.97 ms: 1.09x slower                                                  |
| xml_etree_process       | 54.1 ms                                                             | 59.2 ms: 1.10x slower                                                  |
| float                   | 76.0 ms                                                             | 83.2 ms: 1.10x slower                                                  |
| xml_etree_generate      | 76.5 ms                                                             | 84.7 ms: 1.11x slower                                                  |
| regex_effbot            | 3.32 ms                                                             | 3.69 ms: 1.11x slower                                                  |
| pickle_list             | 4.03 us                                                             | 4.50 us: 1.12x slower                                                  |
| scimark_fft             | 328 ms                                                              | 367 ms: 1.12x slower                                                   |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 5.01 ms: 1.12x slower                                                  |
| python_startup_no_site  | 5.98 ms                                                             | 6.73 ms: 1.13x slower                                                  |
| unpickle                | 13.2 us                                                             | 15.0 us: 1.14x slower                                                  |
| async_generators        | 361 ms                                                              | 446 ms: 1.23x slower                                                   |
| dask                    | 368 ms                                                              | 540 ms: 1.47x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.01x slower                                                           |

Benchmark hidden because not significant (2): pycparser, bench_mp_pool
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
