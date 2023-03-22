
# Results vs. 3.11.0

- fork: python
- ref: deaf509e8fc6e0363bd6
- machine: darwin-arm64
- commit hash: deaf509
- commit date: 2022-10-24
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 181 ms: 1.13x slower                                                |
| chameleon      | 4.57 ms                                                | 4.61 ms: 1.01x slower                                               |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 51.7 ms: 1.03x faster                                               |
| nbody          | 65.5 ms                                                | 65.2 ms: 1.00x faster                                               |
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 76.3 ms: 1.01x faster                                               |
| regex_dna      | 152 ms                                                 | 151 ms: 1.00x faster                                                |
| regex_v8       | 16.2 ms                                                | 16.5 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 99.6 ms: 1.07x faster                                               |
| xml_etree_iterparse  | 69.2 ms                                                | 65.6 ms: 1.05x faster                                               |
| xml_etree_generate   | 48.8 ms                                                | 48.4 ms: 1.01x faster                                               |
| json_dumps           | 7.72 ms                                                | 7.67 ms: 1.01x faster                                               |
| xml_etree_process    | 35.2 ms                                                | 35.1 ms: 1.00x faster                                               |
| pickle_dict          | 17.9 us                                                | 17.9 us: 1.00x slower                                               |
| unpickle_pure_python | 159 us                                                 | 159 us: 1.00x slower                                                |
| json_loads           | 16.1 us                                                | 16.1 us: 1.00x slower                                               |
| pickle               | 7.17 us                                                | 7.21 us: 1.01x slower                                               |
| pickle_pure_python   | 199 us                                                 | 200 us: 1.01x slower                                                |
| pickle_list          | 2.81 us                                                | 2.86 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.24 ms: 1.29x faster                                               |
| python_startup         | 11.5 ms                                                | 9.19 ms: 1.25x faster                                               |
| Geometric mean         | (ref)                                                  | 1.27x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako           | 8.49 ms                                                | 8.40 ms: 1.01x faster                                               |
| genshi_text    | 15.3 ms                                                | 15.3 ms: 1.00x slower                                               |
| genshi_xml     | 29.8 ms                                                | 30.5 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.6 ms: 1.35x faster                                               |
| python_startup_no_site  | 9.31 ms                                                | 7.24 ms: 1.29x faster                                               |
| python_startup          | 11.5 ms                                                | 9.19 ms: 1.25x faster                                               |
| xml_etree_parse         | 106 ms                                                 | 99.6 ms: 1.07x faster                                               |
| async_tree_memoization  | 336 ms                                                 | 317 ms: 1.06x faster                                                |
| flaskblogging           | 2.42 ms                                                | 2.29 ms: 1.06x faster                                               |
| xml_etree_iterparse     | 69.2 ms                                                | 65.6 ms: 1.05x faster                                               |
| bench_mp_pool           | 43.2 ms                                                | 41.4 ms: 1.04x faster                                               |
| nqueens                 | 61.8 ms                                                | 59.5 ms: 1.04x faster                                               |
| bench_thread_pool       | 473 us                                                 | 457 us: 1.03x faster                                                |
| dulwich_log             | 29.9 ms                                                | 29.1 ms: 1.03x faster                                               |
| float                   | 53.0 ms                                                | 51.7 ms: 1.03x faster                                               |
| generators              | 28.8 ms                                                | 28.4 ms: 1.01x faster                                               |
| async_tree_io           | 706 ms                                                 | 696 ms: 1.01x faster                                                |
| unpack_sequence         | 33.6 ns                                                | 33.1 ns: 1.01x faster                                               |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.22 ms: 1.01x faster                                               |
| logging_format          | 3.78 us                                                | 3.73 us: 1.01x faster                                               |
| async_tree_none         | 285 ms                                                 | 281 ms: 1.01x faster                                                |
| mako                    | 8.49 ms                                                | 8.40 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed | 534 ms                                                 | 528 ms: 1.01x faster                                                |
| logging_simple          | 3.50 us                                                | 3.47 us: 1.01x faster                                               |
| sqlglot_parse           | 957 us                                                 | 948 us: 1.01x faster                                                |
| thrift                  | 433 us                                                 | 429 us: 1.01x faster                                                |
| xml_etree_generate      | 48.8 ms                                                | 48.4 ms: 1.01x faster                                               |
| logging_silent          | 68.0 ns                                                | 67.4 ns: 1.01x faster                                               |
| deepcopy_reduce         | 1.91 us                                                | 1.90 us: 1.01x faster                                               |
| sqlglot_transpile       | 1.12 ms                                                | 1.11 ms: 1.01x faster                                               |
| deepcopy                | 224 us                                                 | 222 us: 1.01x faster                                                |
| sympy_sum               | 86.0 ms                                                | 85.5 ms: 1.01x faster                                               |
| json_dumps              | 7.72 ms                                                | 7.67 ms: 1.01x faster                                               |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.01x faster                                              |
| deepcopy_memo           | 26.3 us                                                | 26.2 us: 1.01x faster                                               |
| regex_compile           | 76.7 ms                                                | 76.3 ms: 1.01x faster                                               |
| sympy_str               | 152 ms                                                 | 151 ms: 1.00x faster                                                |
| sympy_expand            | 243 ms                                                 | 242 ms: 1.00x faster                                                |
| sqlalchemy_declarative  | 62.7 ms                                                | 62.4 ms: 1.00x faster                                               |
| xml_etree_process       | 35.2 ms                                                | 35.1 ms: 1.00x faster                                               |
| nbody                   | 65.5 ms                                                | 65.2 ms: 1.00x faster                                               |
| chaos                   | 49.5 ms                                                | 49.3 ms: 1.00x faster                                               |
| telco                   | 3.39 ms                                                | 3.39 ms: 1.00x faster                                               |
| mdp                     | 1.54 sec                                               | 1.54 sec: 1.00x faster                                              |
| regex_dna               | 152 ms                                                 | 151 ms: 1.00x faster                                                |
| meteor_contest          | 73.8 ms                                                | 73.9 ms: 1.00x slower                                               |
| coroutines              | 17.7 ms                                                | 17.8 ms: 1.00x slower                                               |
| scimark_lu              | 72.1 ms                                                | 72.2 ms: 1.00x slower                                               |
| pickle_dict             | 17.9 us                                                | 17.9 us: 1.00x slower                                               |
| async_generators        | 195 ms                                                 | 195 ms: 1.00x slower                                                |
| scimark_sor             | 83.0 ms                                                | 83.3 ms: 1.00x slower                                               |
| pprint_pformat          | 950 ms                                                 | 953 ms: 1.00x slower                                                |
| sqlglot_optimize        | 31.2 ms                                                | 31.3 ms: 1.00x slower                                               |
| genshi_text             | 15.3 ms                                                | 15.3 ms: 1.00x slower                                               |
| unpickle_pure_python    | 159 us                                                 | 159 us: 1.00x slower                                                |
| deltablue               | 2.81 ms                                                | 2.82 ms: 1.00x slower                                               |
| json_loads              | 16.1 us                                                | 16.1 us: 1.00x slower                                               |
| pprint_safe_repr        | 465 ms                                                 | 467 ms: 1.01x slower                                                |
| pyflate                 | 311 ms                                                 | 313 ms: 1.01x slower                                                |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                                |
| fannkuch                | 261 ms                                                 | 262 ms: 1.01x slower                                                |
| scimark_fft             | 199 ms                                                 | 201 ms: 1.01x slower                                                |
| go                      | 109 ms                                                 | 109 ms: 1.01x slower                                                |
| pickle                  | 7.17 us                                                | 7.21 us: 1.01x slower                                               |
| pickle_pure_python      | 199 us                                                 | 200 us: 1.01x slower                                                |
| chameleon               | 4.57 ms                                                | 4.61 ms: 1.01x slower                                               |
| scimark_monte_carlo     | 46.4 ms                                                | 46.9 ms: 1.01x slower                                               |
| richards                | 32.2 ms                                                | 32.7 ms: 1.02x slower                                               |
| sqlite_synth            | 1.27 us                                                | 1.29 us: 1.02x slower                                               |
| regex_v8                | 16.2 ms                                                | 16.5 ms: 1.02x slower                                               |
| pickle_list             | 2.81 us                                                | 2.86 us: 1.02x slower                                               |
| json                    | 2.77 ms                                                | 2.83 ms: 1.02x slower                                               |
| genshi_xml              | 29.8 ms                                                | 30.5 ms: 1.02x slower                                               |
| 2to3                    | 161 ms                                                 | 181 ms: 1.13x slower                                                |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (18): tornado_http, pylint, gunicorn, coverage, pycparser, unpickle, regex_effbot, crypto_pyaes, html5lib, spectral_norm, aiohttp, sqlglot_normalize, hexiom, raytrace, scimark_sparse_mat_mult, django_template, unpickle_list, sympy_integrate
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: mypy
