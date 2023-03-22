
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0
- machine: darwin-arm64
- commit hash: deaf509
- commit date: 2022-10-24
- overall geometric mean: 1.01x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 181 ms                                                              | 161 ms: 1.13x faster                                   |
| chameleon      | 4.61 ms                                                             | 4.57 ms: 1.01x faster                                  |
| docutils       | 1.46 sec                                                            | 1.47 sec: 1.01x slower                                 |
| Geometric mean | (ref)                                                               | 1.02x faster                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 282 ms                                                              | 281 ms: 1.01x faster                                   |
| nbody          | 65.2 ms                                                             | 65.5 ms: 1.00x slower                                  |
| float          | 51.7 ms                                                             | 53.0 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                               | 1.01x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 16.5 ms                                                             | 16.2 ms: 1.02x faster                                  |
| regex_dna      | 151 ms                                                              | 152 ms: 1.00x slower                                   |
| regex_compile  | 76.3 ms                                                             | 76.7 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                               | 1.00x faster                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| pickle_list          | 2.86 us                                                             | 2.81 us: 1.02x faster                                  |
| pickle_pure_python   | 200 us                                                              | 199 us: 1.01x faster                                   |
| pickle               | 7.21 us                                                             | 7.17 us: 1.01x faster                                  |
| json_loads           | 16.1 us                                                             | 16.1 us: 1.00x faster                                  |
| unpickle_pure_python | 159 us                                                              | 159 us: 1.00x faster                                   |
| pickle_dict          | 17.9 us                                                             | 17.9 us: 1.00x faster                                  |
| xml_etree_process    | 35.1 ms                                                             | 35.2 ms: 1.00x slower                                  |
| json_dumps           | 7.67 ms                                                             | 7.72 ms: 1.01x slower                                  |
| xml_etree_generate   | 48.4 ms                                                             | 48.8 ms: 1.01x slower                                  |
| xml_etree_iterparse  | 65.6 ms                                                             | 69.2 ms: 1.05x slower                                  |
| xml_etree_parse      | 99.6 ms                                                             | 106 ms: 1.07x slower                                   |
| Geometric mean       | (ref)                                                               | 1.01x slower                                           |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 9.19 ms                                                             | 11.5 ms: 1.25x slower                                  |
| python_startup_no_site | 7.24 ms                                                             | 9.31 ms: 1.29x slower                                  |
| Geometric mean         | (ref)                                                               | 1.27x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml     | 30.5 ms                                                             | 29.8 ms: 1.02x faster                                  |
| genshi_text    | 15.3 ms                                                             | 15.3 ms: 1.00x faster                                  |
| mako           | 8.40 ms                                                             | 8.49 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                               | 1.00x faster                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3                    | 181 ms                                                              | 161 ms: 1.13x faster                                   |
| genshi_xml              | 30.5 ms                                                             | 29.8 ms: 1.02x faster                                  |
| json                    | 2.83 ms                                                             | 2.77 ms: 1.02x faster                                  |
| pickle_list             | 2.86 us                                                             | 2.81 us: 1.02x faster                                  |
| regex_v8                | 16.5 ms                                                             | 16.2 ms: 1.02x faster                                  |
| sqlite_synth            | 1.29 us                                                             | 1.27 us: 1.02x faster                                  |
| richards                | 32.7 ms                                                             | 32.2 ms: 1.02x faster                                  |
| scimark_monte_carlo     | 46.9 ms                                                             | 46.4 ms: 1.01x faster                                  |
| chameleon               | 4.61 ms                                                             | 4.57 ms: 1.01x faster                                  |
| pickle_pure_python      | 200 us                                                              | 199 us: 1.01x faster                                   |
| pickle                  | 7.21 us                                                             | 7.17 us: 1.01x faster                                  |
| go                      | 109 ms                                                              | 109 ms: 1.01x faster                                   |
| scimark_fft             | 201 ms                                                              | 199 ms: 1.01x faster                                   |
| fannkuch                | 262 ms                                                              | 261 ms: 1.01x faster                                   |
| pidigits                | 282 ms                                                              | 281 ms: 1.01x faster                                   |
| pyflate                 | 313 ms                                                              | 311 ms: 1.01x faster                                   |
| pprint_safe_repr        | 467 ms                                                              | 465 ms: 1.01x faster                                   |
| json_loads              | 16.1 us                                                             | 16.1 us: 1.00x faster                                  |
| deltablue               | 2.82 ms                                                             | 2.81 ms: 1.00x faster                                  |
| unpickle_pure_python    | 159 us                                                              | 159 us: 1.00x faster                                   |
| genshi_text             | 15.3 ms                                                             | 15.3 ms: 1.00x faster                                  |
| sqlglot_optimize        | 31.3 ms                                                             | 31.2 ms: 1.00x faster                                  |
| pprint_pformat          | 953 ms                                                              | 950 ms: 1.00x faster                                   |
| scimark_sor             | 83.3 ms                                                             | 83.0 ms: 1.00x faster                                  |
| async_generators        | 195 ms                                                              | 195 ms: 1.00x faster                                   |
| pickle_dict             | 17.9 us                                                             | 17.9 us: 1.00x faster                                  |
| scimark_lu              | 72.2 ms                                                             | 72.1 ms: 1.00x faster                                  |
| coroutines              | 17.8 ms                                                             | 17.7 ms: 1.00x faster                                  |
| meteor_contest          | 73.9 ms                                                             | 73.8 ms: 1.00x faster                                  |
| regex_dna               | 151 ms                                                              | 152 ms: 1.00x slower                                   |
| mdp                     | 1.54 sec                                                            | 1.54 sec: 1.00x slower                                 |
| telco                   | 3.39 ms                                                             | 3.39 ms: 1.00x slower                                  |
| chaos                   | 49.3 ms                                                             | 49.5 ms: 1.00x slower                                  |
| nbody                   | 65.2 ms                                                             | 65.5 ms: 1.00x slower                                  |
| xml_etree_process       | 35.1 ms                                                             | 35.2 ms: 1.00x slower                                  |
| sqlalchemy_declarative  | 62.4 ms                                                             | 62.7 ms: 1.00x slower                                  |
| sympy_expand            | 242 ms                                                              | 243 ms: 1.00x slower                                   |
| sympy_str               | 151 ms                                                              | 152 ms: 1.00x slower                                   |
| regex_compile           | 76.3 ms                                                             | 76.7 ms: 1.01x slower                                  |
| deepcopy_memo           | 26.2 us                                                             | 26.3 us: 1.01x slower                                  |
| docutils                | 1.46 sec                                                            | 1.47 sec: 1.01x slower                                 |
| json_dumps              | 7.67 ms                                                             | 7.72 ms: 1.01x slower                                  |
| sympy_sum               | 85.5 ms                                                             | 86.0 ms: 1.01x slower                                  |
| deepcopy                | 222 us                                                              | 224 us: 1.01x slower                                   |
| sqlglot_transpile       | 1.11 ms                                                             | 1.12 ms: 1.01x slower                                  |
| deepcopy_reduce         | 1.90 us                                                             | 1.91 us: 1.01x slower                                  |
| logging_silent          | 67.4 ns                                                             | 68.0 ns: 1.01x slower                                  |
| xml_etree_generate      | 48.4 ms                                                             | 48.8 ms: 1.01x slower                                  |
| thrift                  | 429 us                                                              | 433 us: 1.01x slower                                   |
| sqlglot_parse           | 948 us                                                              | 957 us: 1.01x slower                                   |
| logging_simple          | 3.47 us                                                             | 3.50 us: 1.01x slower                                  |
| async_tree_cpu_io_mixed | 528 ms                                                              | 534 ms: 1.01x slower                                   |
| mako                    | 8.40 ms                                                             | 8.49 ms: 1.01x slower                                  |
| async_tree_none         | 281 ms                                                              | 285 ms: 1.01x slower                                   |
| logging_format          | 3.73 us                                                             | 3.78 us: 1.01x slower                                  |
| sqlalchemy_imperative   | 7.22 ms                                                             | 7.31 ms: 1.01x slower                                  |
| unpack_sequence         | 33.1 ns                                                             | 33.6 ns: 1.01x slower                                  |
| async_tree_io           | 696 ms                                                              | 706 ms: 1.01x slower                                   |
| generators              | 28.4 ms                                                             | 28.8 ms: 1.01x slower                                  |
| float                   | 51.7 ms                                                             | 53.0 ms: 1.03x slower                                  |
| dulwich_log             | 29.1 ms                                                             | 29.9 ms: 1.03x slower                                  |
| bench_thread_pool       | 457 us                                                              | 473 us: 1.03x slower                                   |
| nqueens                 | 59.5 ms                                                             | 61.8 ms: 1.04x slower                                  |
| bench_mp_pool           | 41.4 ms                                                             | 43.2 ms: 1.04x slower                                  |
| xml_etree_iterparse     | 65.6 ms                                                             | 69.2 ms: 1.05x slower                                  |
| flaskblogging           | 2.29 ms                                                             | 2.42 ms: 1.06x slower                                  |
| async_tree_memoization  | 317 ms                                                              | 336 ms: 1.06x slower                                   |
| xml_etree_parse         | 99.6 ms                                                             | 106 ms: 1.07x slower                                   |
| python_startup          | 9.19 ms                                                             | 11.5 ms: 1.25x slower                                  |
| python_startup_no_site  | 7.24 ms                                                             | 9.31 ms: 1.29x slower                                  |
| pathlib                 | 20.6 ms                                                             | 27.8 ms: 1.35x slower                                  |
| Geometric mean          | (ref)                                                               | 1.01x slower                                           |

Benchmark hidden because not significant (18): sympy_integrate, unpickle_list, django_template, scimark_sparse_mat_mult, raytrace, hexiom, sqlglot_normalize, aiohttp, spectral_norm, html5lib, crypto_pyaes, regex_effbot, unpickle, pycparser, coverage, gunicorn, pylint, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: mypy
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2
