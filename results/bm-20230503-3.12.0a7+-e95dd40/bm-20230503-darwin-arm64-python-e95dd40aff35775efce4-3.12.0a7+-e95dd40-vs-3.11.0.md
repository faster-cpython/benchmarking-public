
# Results vs. 3.11.0

- fork: python
- ref: e95dd40aff35775efce4
- machine: darwin-arm64
- commit hash: e95dd40
- commit date: 2023-05-03
- overall geometric mean: 1.05x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                              | 173 ms: 1.08x slower                                                   |
| docutils       | 1.47 sec                                                            | 1.56 sec: 1.06x slower                                                 |
| Geometric mean | (ref)                                                               | 1.05x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 281 ms                                                              | 281 ms: 1.00x slower                                                   |
| nbody          | 65.5 ms                                                             | 69.7 ms: 1.06x slower                                                  |
| float          | 53.0 ms                                                             | 58.9 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                               | 1.06x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 151 ms                                                              | 150 ms: 1.01x faster                                                   |
| regex_v8       | 16.1 ms                                                             | 16.3 ms: 1.01x slower                                                  |
| regex_effbot   | 2.63 ms                                                             | 2.69 ms: 1.02x slower                                                  |
| regex_compile  | 76.6 ms                                                             | 78.7 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                               | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.59 ms                                                             | 6.92 ms: 1.10x faster                                                  |
| unpickle_pure_python | 158 us                                                              | 151 us: 1.05x faster                                                   |
| pickle_pure_python   | 198 us                                                              | 194 us: 1.02x faster                                                   |
| xml_etree_parse      | 106 ms                                                              | 108 ms: 1.02x slower                                                   |
| unpickle             | 9.66 us                                                             | 10.1 us: 1.04x slower                                                  |
| pickle_dict          | 17.9 us                                                             | 19.0 us: 1.06x slower                                                  |
| pickle_list          | 2.83 us                                                             | 3.05 us: 1.08x slower                                                  |
| xml_etree_iterparse  | 69.2 ms                                                             | 75.1 ms: 1.09x slower                                                  |
| pickle               | 7.17 us                                                             | 7.95 us: 1.11x slower                                                  |
| json_loads           | 16.0 us                                                             | 17.9 us: 1.12x slower                                                  |
| xml_etree_process    | 35.0 ms                                                             | 40.2 ms: 1.15x slower                                                  |
| xml_etree_generate   | 48.2 ms                                                             | 58.0 ms: 1.20x slower                                                  |
| unpickle_list        | 2.63 us                                                             | 3.19 us: 1.21x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.07x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.3 ms                                                             | 12.5 ms: 1.02x slower                                                  |
| python_startup_no_site | 10.1 ms                                                             | 10.4 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-----------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 8.42 ms                                                             | 7.81 ms: 1.08x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                              | 420 ms: 1.55x faster                                                   |
| unpack_sequence         | 33.5 ns                                                             | 28.1 ns: 1.19x faster                                                  |
| generators              | 28.6 ms                                                             | 24.9 ms: 1.15x faster                                                  |
| deltablue               | 2.81 ms                                                             | 2.47 ms: 1.14x faster                                                  |
| json_dumps              | 7.59 ms                                                             | 6.92 ms: 1.10x faster                                                  |
| hexiom                  | 4.73 ms                                                             | 4.32 ms: 1.10x faster                                                  |
| mako                    | 8.42 ms                                                             | 7.81 ms: 1.08x faster                                                  |
| sqlglot_parse           | 956 us                                                              | 903 us: 1.06x faster                                                   |
| unpickle_pure_python    | 158 us                                                              | 151 us: 1.05x faster                                                   |
| create_gc_cycles        | 722 us                                                              | 695 us: 1.04x faster                                                   |
| sqlglot_transpile       | 1.12 ms                                                             | 1.08 ms: 1.03x faster                                                  |
| pickle_pure_python      | 198 us                                                              | 194 us: 1.02x faster                                                   |
| chaos                   | 49.4 ms                                                             | 48.4 ms: 1.02x faster                                                  |
| regex_dna               | 151 ms                                                              | 150 ms: 1.01x faster                                                   |
| pidigits                | 281 ms                                                              | 281 ms: 1.00x slower                                                   |
| go                      | 109 ms                                                              | 109 ms: 1.00x slower                                                   |
| gc_traversal            | 2.41 ms                                                             | 2.42 ms: 1.00x slower                                                  |
| async_tree_cpu_io_mixed | 534 ms                                                              | 536 ms: 1.00x slower                                                   |
| richards                | 32.2 ms                                                             | 32.4 ms: 1.01x slower                                                  |
| coverage                | 58.4 ms                                                             | 58.8 ms: 1.01x slower                                                  |
| async_tree_io           | 707 ms                                                              | 712 ms: 1.01x slower                                                   |
| regex_v8                | 16.1 ms                                                             | 16.3 ms: 1.01x slower                                                  |
| sqlalchemy_imperative   | 7.26 ms                                                             | 7.37 ms: 1.01x slower                                                  |
| python_startup          | 12.3 ms                                                             | 12.5 ms: 1.02x slower                                                  |
| coroutines              | 17.7 ms                                                             | 18.0 ms: 1.02x slower                                                  |
| mdp                     | 1.54 sec                                                            | 1.58 sec: 1.02x slower                                                 |
| regex_effbot            | 2.63 ms                                                             | 2.69 ms: 1.02x slower                                                  |
| xml_etree_parse         | 106 ms                                                              | 108 ms: 1.02x slower                                                   |
| regex_compile           | 76.6 ms                                                             | 78.7 ms: 1.03x slower                                                  |
| dulwich_log             | 29.7 ms                                                             | 30.7 ms: 1.03x slower                                                  |
| python_startup_no_site  | 10.1 ms                                                             | 10.4 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 3.31 ms: 1.04x slower                                                  |
| scimark_sor             | 82.9 ms                                                             | 86.4 ms: 1.04x slower                                                  |
| logging_silent          | 68.0 ns                                                             | 71.0 ns: 1.04x slower                                                  |
| unpickle                | 9.66 us                                                             | 10.1 us: 1.04x slower                                                  |
| bench_thread_pool       | 474 us                                                              | 499 us: 1.05x slower                                                   |
| meteor_contest          | 73.3 ms                                                             | 77.4 ms: 1.05x slower                                                  |
| logging_format          | 3.77 us                                                             | 4.00 us: 1.06x slower                                                  |
| logging_simple          | 3.49 us                                                             | 3.72 us: 1.06x slower                                                  |
| pickle_dict             | 17.9 us                                                             | 19.0 us: 1.06x slower                                                  |
| docutils                | 1.47 sec                                                            | 1.56 sec: 1.06x slower                                                 |
| nbody                   | 65.5 ms                                                             | 69.7 ms: 1.06x slower                                                  |
| deepcopy                | 224 us                                                              | 239 us: 1.07x slower                                                   |
| scimark_fft             | 200 ms                                                              | 214 ms: 1.07x slower                                                   |
| fannkuch                | 260 ms                                                              | 279 ms: 1.07x slower                                                   |
| 2to3                    | 161 ms                                                              | 173 ms: 1.08x slower                                                   |
| pickle_list             | 2.83 us                                                             | 3.05 us: 1.08x slower                                                  |
| crypto_pyaes            | 51.8 ms                                                             | 55.9 ms: 1.08x slower                                                  |
| xml_etree_iterparse     | 69.2 ms                                                             | 75.1 ms: 1.09x slower                                                  |
| spectral_norm           | 72.5 ms                                                             | 79.0 ms: 1.09x slower                                                  |
| json                    | 2.77 ms                                                             | 3.03 ms: 1.09x slower                                                  |
| pprint_pformat          | 946 ms                                                              | 1.04 sec: 1.10x slower                                                 |
| pprint_safe_repr        | 463 ms                                                              | 511 ms: 1.10x slower                                                   |
| bench_mp_pool           | 43.8 ms                                                             | 48.4 ms: 1.10x slower                                                  |
| sqlalchemy_declarative  | 62.6 ms                                                             | 69.2 ms: 1.11x slower                                                  |
| pickle                  | 7.17 us                                                             | 7.95 us: 1.11x slower                                                  |
| pyflate                 | 309 ms                                                              | 343 ms: 1.11x slower                                                   |
| float                   | 53.0 ms                                                             | 58.9 ms: 1.11x slower                                                  |
| json_loads              | 16.0 us                                                             | 17.9 us: 1.12x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                             | 2.13 us: 1.12x slower                                                  |
| comprehensions          | 16.1 us                                                             | 18.0 us: 1.12x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                             | 52.1 ms: 1.12x slower                                                  |
| scimark_lu              | 72.2 ms                                                             | 82.0 ms: 1.14x slower                                                  |
| xml_etree_process       | 35.0 ms                                                             | 40.2 ms: 1.15x slower                                                  |
| sqlglot_normalize       | 171 ms                                                              | 200 ms: 1.17x slower                                                   |
| sqlglot_optimize        | 31.2 ms                                                             | 36.5 ms: 1.17x slower                                                  |
| telco                   | 3.40 ms                                                             | 4.03 ms: 1.19x slower                                                  |
| xml_etree_generate      | 48.2 ms                                                             | 58.0 ms: 1.20x slower                                                  |
| raytrace                | 207 ms                                                              | 250 ms: 1.21x slower                                                   |
| unpickle_list           | 2.63 us                                                             | 3.19 us: 1.21x slower                                                  |
| sqlite_synth            | 1.28 us                                                             | 1.60 us: 1.25x slower                                                  |
| dask                    | 226 ms                                                              | 334 ms: 1.48x slower                                                   |
| async_generators        | 195 ms                                                              | 315 ms: 1.62x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.05x slower                                                           |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_none, tornado_http, pathlib, deepcopy_memo, pycparser, nqueens, mypy2
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
