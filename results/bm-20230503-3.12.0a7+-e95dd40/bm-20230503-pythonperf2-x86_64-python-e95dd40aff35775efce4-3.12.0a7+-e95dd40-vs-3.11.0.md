
# Results vs. 3.11.0

- fork: python
- ref: e95dd40aff35775efce4
- machine: linux-x86_64
- commit hash: e95dd40
- commit date: 2023-05-03
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                    | 284 ms: 1.02x faster                                                         |
| docutils       | 2.86 sec                                                                  | 2.90 sec: 1.01x slower                                                       |
| tornado_http   | 125 ms                                                                    | 114 ms: 1.10x faster                                                         |
| Geometric mean | (ref)                                                                     | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                                   | 85.3 ms: 1.08x faster                                                        |
| pidigits       | 252 ms                                                                    | 260 ms: 1.03x slower                                                         |
| float          | 75.7 ms                                                                   | 78.9 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                                     | 1.00x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 154 ms                                                                    | 145 ms: 1.06x faster                                                         |
| regex_v8       | 24.4 ms                                                                   | 23.8 ms: 1.03x faster                                                        |
| regex_dna      | 225 ms                                                                    | 232 ms: 1.03x slower                                                         |
| regex_effbot   | 3.31 ms                                                                   | 3.47 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                     | 1.00x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                                   | 10.5 ms: 1.27x faster                                                        |
| unpickle_pure_python | 238 us                                                                    | 205 us: 1.16x faster                                                         |
| json_loads           | 28.4 us                                                                   | 25.2 us: 1.13x faster                                                        |
| xml_etree_parse      | 161 ms                                                                    | 148 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 106 ms                                                                    | 105 ms: 1.01x faster                                                         |
| pickle_pure_python   | 319 us                                                                    | 318 us: 1.01x faster                                                         |
| unpickle_list        | 4.52 us                                                                   | 4.61 us: 1.02x slower                                                        |
| xml_etree_process    | 55.8 ms                                                                   | 58.8 ms: 1.05x slower                                                        |
| pickle               | 9.92 us                                                                   | 10.5 us: 1.05x slower                                                        |
| pickle_dict          | 31.1 us                                                                   | 33.3 us: 1.07x slower                                                        |
| xml_etree_generate   | 79.1 ms                                                                   | 85.6 ms: 1.08x slower                                                        |
| unpickle             | 13.0 us                                                                   | 15.0 us: 1.15x slower                                                        |
| pickle_list          | 3.78 us                                                                   | 4.41 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                                     | 1.00x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|------------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                                   | 11.2 ms: 1.04x slower                                                        |
| python_startup_no_site | 7.73 ms                                                                   | 8.39 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                                     | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-----------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako      | 10.9 ms                                                                   | 9.92 ms: 1.10x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf2-x86_64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-------------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 752 ms                                                                    | 380 ms: 1.98x faster                                                         |
| generators              | 56.0 ms                                                                   | 36.0 ms: 1.55x faster                                                        |
| coroutines              | 29.5 ms                                                                   | 22.4 ms: 1.31x faster                                                        |
| json_dumps              | 13.4 ms                                                                   | 10.5 ms: 1.27x faster                                                        |
| fannkuch                | 449 ms                                                                    | 357 ms: 1.26x faster                                                         |
| deltablue               | 3.99 ms                                                                   | 3.25 ms: 1.23x faster                                                        |
| hexiom                  | 7.00 ms                                                                   | 5.86 ms: 1.20x faster                                                        |
| mypy2                   | 446 ms                                                                    | 377 ms: 1.18x faster                                                         |
| unpickle_pure_python    | 238 us                                                                    | 205 us: 1.16x faster                                                         |
| scimark_lu              | 114 ms                                                                    | 99.5 ms: 1.15x faster                                                        |
| nqueens                 | 101 ms                                                                    | 88.9 ms: 1.14x faster                                                        |
| json_loads              | 28.4 us                                                                   | 25.2 us: 1.13x faster                                                        |
| chaos                   | 76.2 ms                                                                   | 67.8 ms: 1.12x faster                                                        |
| gc_traversal            | 4.22 ms                                                                   | 3.76 ms: 1.12x faster                                                        |
| async_tree_memoization  | 639 ms                                                                    | 572 ms: 1.12x faster                                                         |
| async_tree_none         | 529 ms                                                                    | 476 ms: 1.11x faster                                                         |
| logging_silent          | 103 ns                                                                    | 92.4 ns: 1.11x faster                                                        |
| richards                | 49.1 ms                                                                   | 44.5 ms: 1.10x faster                                                        |
| sqlglot_parse           | 1.53 ms                                                                   | 1.39 ms: 1.10x faster                                                        |
| tornado_http            | 125 ms                                                                    | 114 ms: 1.10x faster                                                         |
| mako                    | 10.9 ms                                                                   | 9.92 ms: 1.10x faster                                                        |
| xml_etree_parse         | 161 ms                                                                    | 148 ms: 1.09x faster                                                         |
| async_tree_io           | 1.18 sec                                                                  | 1.09 sec: 1.09x faster                                                       |
| go                      | 158 ms                                                                    | 146 ms: 1.08x faster                                                         |
| nbody                   | 92.1 ms                                                                   | 85.3 ms: 1.08x faster                                                        |
| json                    | 5.59 ms                                                                   | 5.18 ms: 1.08x faster                                                        |
| mdp                     | 2.73 sec                                                                  | 2.53 sec: 1.08x faster                                                       |
| async_tree_cpu_io_mixed | 754 ms                                                                    | 703 ms: 1.07x faster                                                         |
| dulwich_log             | 69.1 ms                                                                   | 64.8 ms: 1.07x faster                                                        |
| regex_compile           | 154 ms                                                                    | 145 ms: 1.06x faster                                                         |
| crypto_pyaes            | 85.0 ms                                                                   | 80.3 ms: 1.06x faster                                                        |
| pycparser               | 1.30 sec                                                                  | 1.23 sec: 1.06x faster                                                       |
| spectral_norm           | 95.1 ms                                                                   | 90.2 ms: 1.05x faster                                                        |
| logging_format          | 7.84 us                                                                   | 7.51 us: 1.04x faster                                                        |
| sqlglot_transpile       | 1.88 ms                                                                   | 1.81 ms: 1.04x faster                                                        |
| bench_thread_pool       | 990 us                                                                    | 958 us: 1.03x faster                                                         |
| regex_v8                | 24.4 ms                                                                   | 23.8 ms: 1.03x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                                   | 1.61 ms: 1.03x faster                                                        |
| logging_simple          | 6.95 us                                                                   | 6.78 us: 1.02x faster                                                        |
| 2to3                    | 289 ms                                                                    | 284 ms: 1.02x faster                                                         |
| sqlglot_normalize       | 122 ms                                                                    | 120 ms: 1.02x faster                                                         |
| xml_etree_iterparse     | 106 ms                                                                    | 105 ms: 1.01x faster                                                         |
| comprehensions          | 24.7 us                                                                   | 24.5 us: 1.01x faster                                                        |
| pickle_pure_python      | 319 us                                                                    | 318 us: 1.01x faster                                                         |
| deepcopy_memo           | 37.0 us                                                                   | 37.2 us: 1.01x slower                                                        |
| pathlib                 | 19.2 ms                                                                   | 19.4 ms: 1.01x slower                                                        |
| sqlglot_optimize        | 58.6 ms                                                                   | 59.2 ms: 1.01x slower                                                        |
| docutils                | 2.86 sec                                                                  | 2.90 sec: 1.01x slower                                                       |
| scimark_sor             | 109 ms                                                                    | 111 ms: 1.02x slower                                                         |
| unpickle_list           | 4.52 us                                                                   | 4.61 us: 1.02x slower                                                        |
| deepcopy_reduce         | 3.39 us                                                                   | 3.46 us: 1.02x slower                                                        |
| regex_dna               | 225 ms                                                                    | 232 ms: 1.03x slower                                                         |
| pprint_pformat          | 1.60 sec                                                                  | 1.65 sec: 1.03x slower                                                       |
| pidigits                | 252 ms                                                                    | 260 ms: 1.03x slower                                                         |
| float                   | 75.7 ms                                                                   | 78.9 ms: 1.04x slower                                                        |
| python_startup          | 10.7 ms                                                                   | 11.2 ms: 1.04x slower                                                        |
| raytrace                | 303 ms                                                                    | 316 ms: 1.04x slower                                                         |
| regex_effbot            | 3.31 ms                                                                   | 3.47 ms: 1.05x slower                                                        |
| pprint_safe_repr        | 768 ms                                                                    | 808 ms: 1.05x slower                                                         |
| xml_etree_process       | 55.8 ms                                                                   | 58.8 ms: 1.05x slower                                                        |
| coverage                | 86.0 ms                                                                   | 90.6 ms: 1.05x slower                                                        |
| sqlite_synth            | 2.49 us                                                                   | 2.62 us: 1.05x slower                                                        |
| pickle                  | 9.92 us                                                                   | 10.5 us: 1.05x slower                                                        |
| scimark_monte_carlo     | 67.8 ms                                                                   | 72.3 ms: 1.07x slower                                                        |
| meteor_contest          | 129 ms                                                                    | 138 ms: 1.07x slower                                                         |
| pickle_dict             | 31.1 us                                                                   | 33.3 us: 1.07x slower                                                        |
| scimark_fft             | 276 ms                                                                    | 298 ms: 1.08x slower                                                         |
| xml_etree_generate      | 79.1 ms                                                                   | 85.6 ms: 1.08x slower                                                        |
| telco                   | 6.70 ms                                                                   | 7.26 ms: 1.08x slower                                                        |
| python_startup_no_site  | 7.73 ms                                                                   | 8.39 ms: 1.09x slower                                                        |
| scimark_sparse_mat_mult | 4.06 ms                                                                   | 4.44 ms: 1.09x slower                                                        |
| unpack_sequence         | 45.9 ns                                                                   | 52.7 ns: 1.15x slower                                                        |
| unpickle                | 13.0 us                                                                   | 15.0 us: 1.15x slower                                                        |
| pickle_list             | 3.78 us                                                                   | 4.41 us: 1.17x slower                                                        |
| async_generators        | 318 ms                                                                    | 389 ms: 1.22x slower                                                         |
| dask                    | 418 ms                                                                    | 563 ms: 1.35x slower                                                         |
| bench_mp_pool           | 4.54 ms                                                                   | 7.84 ms: 1.73x slower                                                        |
| Geometric mean          | (ref)                                                                     | 1.03x faster                                                                 |

Benchmark hidden because not significant (2): deepcopy, pyflate
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
