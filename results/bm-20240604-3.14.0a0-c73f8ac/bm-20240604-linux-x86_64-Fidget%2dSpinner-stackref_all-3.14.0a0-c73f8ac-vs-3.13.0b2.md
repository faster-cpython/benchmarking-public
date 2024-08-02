# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: c73f8ac
- commit date: 2024-06-04
- overall geometric mean: 1.00x slower
- HPT reliability: 83.72%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 272 ms: 1.01x faster                                                    |
| docutils       | 2.83 sec                                                   | 2.80 sec: 1.01x faster                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 600 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 632 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.01x slower                                                            |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_none, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 190 ms: 1.01x faster                                                    |
| nbody          | 88.3 ms                                                    | 92.2 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                      | 1.01x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.9 ms: 1.01x faster                                                   |
| regex_compile  | 137 ms                                                     | 136 ms: 1.01x faster                                                    |
| regex_effbot   | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                      | 1.00x faster                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 158 ms: 1.02x faster                                                    |
| unpickle_list        | 5.34 us                                                    | 5.25 us: 1.02x faster                                                   |
| json_dumps           | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                   |
| pickle_pure_python   | 305 us                                                     | 312 us: 1.02x slower                                                    |
| pickle_dict          | 34.8 us                                                    | 36.2 us: 1.04x slower                                                   |
| pickle               | 11.5 us                                                    | 11.9 us: 1.04x slower                                                   |
| unpickle_pure_python | 218 us                                                     | 227 us: 1.04x slower                                                    |
| pickle_list          | 5.11 us                                                    | 5.35 us: 1.05x slower                                                   |
| tomli_loads          | 2.12 sec                                                   | 2.23 sec: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_process, unpickle, xml_etree_generate, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                      | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.3 ms: 1.01x faster                                                   |
| django_template | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 53.9 ms: 1.05x slower                                                   |
| mako            | 11.2 ms                                                    | 12.0 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pathlib                    | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                   |
| richards_super             | 57.4 ms                                                    | 54.4 ms: 1.06x faster                                                   |
| richards                   | 50.9 ms                                                    | 48.2 ms: 1.06x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.00 ms: 1.05x faster                                                   |
| scimark_fft                | 392 ms                                                     | 376 ms: 1.04x faster                                                    |
| scimark_lu                 | 122 ms                                                     | 118 ms: 1.03x faster                                                    |
| pyflate                    | 484 ms                                                     | 471 ms: 1.03x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.02x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 158 ms: 1.02x faster                                                    |
| dulwich_log                | 67.2 ms                                                    | 66.0 ms: 1.02x faster                                                   |
| unpickle_list              | 5.34 us                                                    | 5.25 us: 1.02x faster                                                   |
| thrift                     | 823 us                                                     | 809 us: 1.02x faster                                                    |
| sqlite_synth               | 2.99 us                                                    | 2.94 us: 1.02x faster                                                   |
| genshi_text                | 23.7 ms                                                    | 23.3 ms: 1.01x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                   |
| crypto_pyaes               | 77.5 ms                                                    | 76.6 ms: 1.01x faster                                                   |
| regex_v8                   | 25.1 ms                                                    | 24.9 ms: 1.01x faster                                                   |
| docutils                   | 2.83 sec                                                   | 2.80 sec: 1.01x faster                                                  |
| regex_compile              | 137 ms                                                     | 136 ms: 1.01x faster                                                    |
| python_startup             | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.76 sec: 1.01x faster                                                  |
| 2to3                       | 274 ms                                                     | 272 ms: 1.01x faster                                                    |
| gc_traversal               | 3.98 ms                                                    | 3.95 ms: 1.01x faster                                                   |
| asyncio_tcp                | 508 ms                                                     | 505 ms: 1.01x faster                                                    |
| pidigits                   | 191 ms                                                     | 190 ms: 1.01x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 563 ms: 1.01x faster                                                    |
| go                         | 145 ms                                                     | 145 ms: 1.00x slower                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.85 sec: 1.00x slower                                                  |
| bench_thread_pool          | 834 us                                                     | 838 us: 1.01x slower                                                    |
| regex_effbot               | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                   |
| sqlglot_normalize          | 110 ms                                                     | 111 ms: 1.01x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 82.1 ms: 1.01x slower                                                   |
| raytrace                   | 267 ms                                                     | 269 ms: 1.01x slower                                                    |
| fannkuch                   | 402 ms                                                     | 406 ms: 1.01x slower                                                    |
| chaos                      | 61.3 ms                                                    | 62.0 ms: 1.01x slower                                                   |
| scimark_monte_carlo        | 69.2 ms                                                    | 69.9 ms: 1.01x slower                                                   |
| hexiom                     | 6.30 ms                                                    | 6.38 ms: 1.01x slower                                                   |
| meteor_contest             | 110 ms                                                     | 111 ms: 1.02x slower                                                    |
| sqlglot_transpile          | 1.63 ms                                                    | 1.66 ms: 1.02x slower                                                   |
| json                       | 5.31 ms                                                    | 5.39 ms: 1.02x slower                                                   |
| spectral_norm              | 116 ms                                                     | 118 ms: 1.02x slower                                                    |
| logging_simple             | 5.74 us                                                    | 5.84 us: 1.02x slower                                                   |
| deepcopy                   | 367 us                                                     | 373 us: 1.02x slower                                                    |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.02x slower                                                   |
| logging_silent             | 105 ns                                                     | 107 ns: 1.02x slower                                                    |
| pprint_pformat             | 1.56 sec                                                   | 1.58 sec: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 600 ms: 1.02x slower                                                    |
| async_generators           | 442 ms                                                     | 452 ms: 1.02x slower                                                    |
| coroutines                 | 23.2 ms                                                    | 23.7 ms: 1.02x slower                                                   |
| pickle_pure_python         | 305 us                                                     | 312 us: 1.02x slower                                                    |
| scimark_sor                | 127 ms                                                     | 131 ms: 1.03x slower                                                    |
| pprint_safe_repr           | 758 ms                                                     | 780 ms: 1.03x slower                                                    |
| deltablue                  | 3.25 ms                                                    | 3.35 ms: 1.03x slower                                                   |
| comprehensions             | 16.6 us                                                    | 17.1 us: 1.03x slower                                                   |
| deepcopy_memo              | 39.7 us                                                    | 41.0 us: 1.03x slower                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 632 ms: 1.03x slower                                                    |
| typing_runtime_protocols   | 165 us                                                     | 171 us: 1.04x slower                                                    |
| django_template            | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                   |
| pickle_dict                | 34.8 us                                                    | 36.2 us: 1.04x slower                                                   |
| pickle                     | 11.5 us                                                    | 11.9 us: 1.04x slower                                                   |
| unpickle_pure_python       | 218 us                                                     | 227 us: 1.04x slower                                                    |
| nbody                      | 88.3 ms                                                    | 92.2 ms: 1.04x slower                                                   |
| genshi_xml                 | 51.6 ms                                                    | 53.9 ms: 1.05x slower                                                   |
| pickle_list                | 5.11 us                                                    | 5.35 us: 1.05x slower                                                   |
| tomli_loads                | 2.12 sec                                                   | 2.23 sec: 1.05x slower                                                  |
| mako                       | 11.2 ms                                                    | 12.0 ms: 1.06x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.00x slower                                                            |

Benchmark hidden because not significant (30): async_tree_io_tg, async_tree_none, coverage, sympy_sum, sympy_str, xml_etree_process, unpickle, tornado_http, bench_mp_pool, regex_dna, dask, pylint, sympy_integrate, python_startup_no_site, sqlglot_optimize, xml_etree_generate, float, generators, html5lib, logging_format, sympy_expand, telco, deepcopy_reduce, async_tree_memoization_tg, pycparser, xml_etree_iterparse, json_loads, async_tree_io, async_tree_none_tg, async_tree_memoization
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 83.72% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x