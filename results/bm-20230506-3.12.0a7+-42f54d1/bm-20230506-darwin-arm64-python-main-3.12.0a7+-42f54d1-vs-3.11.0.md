
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.05x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                              | 174 ms: 1.08x slower                                   |
| docutils       | 1.47 sec                                                            | 1.57 sec: 1.07x slower                                 |
| Geometric mean | (ref)                                                               | 1.04x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.5 ms                                                             | 69.4 ms: 1.06x slower                                  |
| float          | 53.0 ms                                                             | 59.6 ms: 1.12x slower                                  |
| Geometric mean | (ref)                                                               | 1.06x slower                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 151 ms                                                              | 150 ms: 1.01x faster                                   |
| regex_v8       | 16.1 ms                                                             | 16.3 ms: 1.01x slower                                  |
| regex_effbot   | 2.63 ms                                                             | 2.70 ms: 1.03x slower                                  |
| regex_compile  | 76.6 ms                                                             | 78.7 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                               | 1.01x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.59 ms                                                             | 6.95 ms: 1.09x faster                                  |
| unpickle_pure_python | 158 us                                                              | 151 us: 1.05x faster                                   |
| pickle_pure_python   | 198 us                                                              | 194 us: 1.02x faster                                   |
| xml_etree_parse      | 106 ms                                                              | 109 ms: 1.03x slower                                   |
| unpickle             | 9.66 us                                                             | 10.1 us: 1.05x slower                                  |
| pickle_dict          | 17.9 us                                                             | 18.9 us: 1.06x slower                                  |
| xml_etree_iterparse  | 69.2 ms                                                             | 75.2 ms: 1.09x slower                                  |
| pickle               | 7.17 us                                                             | 7.95 us: 1.11x slower                                  |
| json_loads           | 16.0 us                                                             | 17.8 us: 1.11x slower                                  |
| pickle_list          | 2.83 us                                                             | 3.17 us: 1.12x slower                                  |
| xml_etree_process    | 35.0 ms                                                             | 40.4 ms: 1.15x slower                                  |
| xml_etree_generate   | 48.2 ms                                                             | 58.6 ms: 1.22x slower                                  |
| unpickle_list        | 2.63 us                                                             | 3.24 us: 1.23x slower                                  |
| Geometric mean       | (ref)                                                               | 1.07x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.3 ms                                                             | 12.6 ms: 1.02x slower                                  |
| python_startup_no_site | 10.1 ms                                                             | 10.5 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                               | 1.03x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|-----------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 8.42 ms                                                             | 7.79 ms: 1.08x faster                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230506-darwin-arm64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                              | 461 ms: 1.41x faster                                   |
| unpack_sequence         | 33.5 ns                                                             | 28.0 ns: 1.20x faster                                  |
| generators              | 28.6 ms                                                             | 24.9 ms: 1.15x faster                                  |
| deltablue               | 2.81 ms                                                             | 2.47 ms: 1.14x faster                                  |
| hexiom                  | 4.73 ms                                                             | 4.33 ms: 1.09x faster                                  |
| json_dumps              | 7.59 ms                                                             | 6.95 ms: 1.09x faster                                  |
| mako                    | 8.42 ms                                                             | 7.79 ms: 1.08x faster                                  |
| sqlglot_parse           | 956 us                                                              | 902 us: 1.06x faster                                   |
| unpickle_pure_python    | 158 us                                                              | 151 us: 1.05x faster                                   |
| create_gc_cycles        | 722 us                                                              | 698 us: 1.03x faster                                   |
| sqlglot_transpile       | 1.12 ms                                                             | 1.08 ms: 1.03x faster                                  |
| chaos                   | 49.4 ms                                                             | 48.0 ms: 1.03x faster                                  |
| deepcopy_memo           | 26.3 us                                                             | 25.6 us: 1.03x faster                                  |
| pickle_pure_python      | 198 us                                                              | 194 us: 1.02x faster                                   |
| regex_dna               | 151 ms                                                              | 150 ms: 1.01x faster                                   |
| meteor_contest          | 73.3 ms                                                             | 73.4 ms: 1.00x slower                                  |
| gc_traversal            | 2.41 ms                                                             | 2.42 ms: 1.00x slower                                  |
| async_tree_cpu_io_mixed | 534 ms                                                              | 538 ms: 1.01x slower                                   |
| coverage                | 58.4 ms                                                             | 59.1 ms: 1.01x slower                                  |
| async_tree_io           | 707 ms                                                              | 716 ms: 1.01x slower                                   |
| regex_v8                | 16.1 ms                                                             | 16.3 ms: 1.01x slower                                  |
| coroutines              | 17.7 ms                                                             | 18.0 ms: 1.02x slower                                  |
| mdp                     | 1.54 sec                                                            | 1.57 sec: 1.02x slower                                 |
| python_startup          | 12.3 ms                                                             | 12.6 ms: 1.02x slower                                  |
| logging_silent          | 68.0 ns                                                             | 69.6 ns: 1.02x slower                                  |
| regex_effbot            | 2.63 ms                                                             | 2.70 ms: 1.03x slower                                  |
| regex_compile           | 76.6 ms                                                             | 78.7 ms: 1.03x slower                                  |
| xml_etree_parse         | 106 ms                                                              | 109 ms: 1.03x slower                                   |
| dulwich_log             | 29.7 ms                                                             | 30.7 ms: 1.03x slower                                  |
| scimark_sor             | 82.9 ms                                                             | 86.6 ms: 1.04x slower                                  |
| python_startup_no_site  | 10.1 ms                                                             | 10.5 ms: 1.05x slower                                  |
| unpickle                | 9.66 us                                                             | 10.1 us: 1.05x slower                                  |
| bench_thread_pool       | 474 us                                                              | 497 us: 1.05x slower                                   |
| scimark_fft             | 200 ms                                                              | 210 ms: 1.05x slower                                   |
| pickle_dict             | 17.9 us                                                             | 18.9 us: 1.06x slower                                  |
| fannkuch                | 260 ms                                                              | 276 ms: 1.06x slower                                   |
| nbody                   | 65.5 ms                                                             | 69.4 ms: 1.06x slower                                  |
| logging_simple          | 3.49 us                                                             | 3.72 us: 1.07x slower                                  |
| logging_format          | 3.77 us                                                             | 4.02 us: 1.07x slower                                  |
| docutils                | 1.47 sec                                                            | 1.57 sec: 1.07x slower                                 |
| deepcopy                | 224 us                                                              | 240 us: 1.07x slower                                   |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 3.44 ms: 1.08x slower                                  |
| crypto_pyaes            | 51.8 ms                                                             | 55.9 ms: 1.08x slower                                  |
| 2to3                    | 161 ms                                                              | 174 ms: 1.08x slower                                   |
| xml_etree_iterparse     | 69.2 ms                                                             | 75.2 ms: 1.09x slower                                  |
| spectral_norm           | 72.5 ms                                                             | 79.1 ms: 1.09x slower                                  |
| pprint_pformat          | 946 ms                                                              | 1.04 sec: 1.09x slower                                 |
| sqlalchemy_declarative  | 62.6 ms                                                             | 68.6 ms: 1.10x slower                                  |
| json                    | 2.77 ms                                                             | 3.04 ms: 1.10x slower                                  |
| bench_mp_pool           | 43.8 ms                                                             | 48.1 ms: 1.10x slower                                  |
| pprint_safe_repr        | 463 ms                                                              | 511 ms: 1.10x slower                                   |
| pickle                  | 7.17 us                                                             | 7.95 us: 1.11x slower                                  |
| json_loads              | 16.0 us                                                             | 17.8 us: 1.11x slower                                  |
| pyflate                 | 309 ms                                                              | 343 ms: 1.11x slower                                   |
| comprehensions          | 16.1 us                                                             | 17.9 us: 1.11x slower                                  |
| deepcopy_reduce         | 1.91 us                                                             | 2.14 us: 1.12x slower                                  |
| pickle_list             | 2.83 us                                                             | 3.17 us: 1.12x slower                                  |
| float                   | 53.0 ms                                                             | 59.6 ms: 1.12x slower                                  |
| scimark_monte_carlo     | 46.5 ms                                                             | 52.7 ms: 1.13x slower                                  |
| scimark_lu              | 72.2 ms                                                             | 82.2 ms: 1.14x slower                                  |
| xml_etree_process       | 35.0 ms                                                             | 40.4 ms: 1.15x slower                                  |
| sqlglot_normalize       | 171 ms                                                              | 200 ms: 1.17x slower                                   |
| sqlglot_optimize        | 31.2 ms                                                             | 36.6 ms: 1.17x slower                                  |
| telco                   | 3.40 ms                                                             | 4.04 ms: 1.19x slower                                  |
| raytrace                | 207 ms                                                              | 250 ms: 1.21x slower                                   |
| xml_etree_generate      | 48.2 ms                                                             | 58.6 ms: 1.22x slower                                  |
| unpickle_list           | 2.63 us                                                             | 3.24 us: 1.23x slower                                  |
| sqlite_synth            | 1.28 us                                                             | 1.58 us: 1.23x slower                                  |
| dask                    | 226 ms                                                              | 334 ms: 1.48x slower                                   |
| async_generators        | 195 ms                                                              | 316 ms: 1.62x slower                                   |
| Geometric mean          | (ref)                                                               | 1.05x slower                                           |

Benchmark hidden because not significant (11): tornado_http, pathlib, go, pidigits, sqlalchemy_imperative, richards, async_tree_none, pycparser, async_tree_memoization, nqueens, mypy2
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
