# Results vs. base

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-x86_64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 437 ms                                                                      | 431 ms: 1.01x faster                                                           |
| docutils       | 3.51 sec                                                                    | 3.48 sec: 1.01x faster                                                         |
| html5lib       | 109 ms                                                                      | 109 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.90 sec                                                                    | 1.77 sec: 1.07x faster                                                         |
| async_generators           | 521 ms                                                                      | 499 ms: 1.04x faster                                                           |
| coroutines                 | 29.3 ms                                                                     | 28.3 ms: 1.03x faster                                                          |
| async_tree_memoization_tg  | 471 ms                                                                      | 462 ms: 1.02x faster                                                           |
| async_tree_none_tg         | 366 ms                                                                      | 360 ms: 1.02x faster                                                           |
| async_tree_none            | 419 ms                                                                      | 413 ms: 1.01x faster                                                           |
| async_tree_memoization     | 521 ms                                                                      | 514 ms: 1.01x faster                                                           |
| async_tree_io_tg           | 891 ms                                                                      | 880 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 632 ms                                                                      | 626 ms: 1.01x faster                                                           |
| async_tree_io              | 948 ms                                                                      | 940 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed    | 683 ms                                                                      | 678 ms: 1.01x faster                                                           |
| asyncio_websockets         | 381 ms                                                                      | 384 ms: 1.01x slower                                                           |
| Geometric mean             | (ref)                                                                       | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 201 ms                                                                      | 193 ms: 1.04x faster                                                           |
| float          | 146 ms                                                                      | 142 ms: 1.03x faster                                                           |
| pidigits       | 251 ms                                                                      | 250 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 233 ms                                                                      | 229 ms: 1.02x faster                                                           |
| regex_v8       | 26.9 ms                                                                     | 27.4 ms: 1.02x slower                                                          |
| regex_effbot   | 3.48 ms                                                                     | 3.65 ms: 1.05x slower                                                          |
| regex_dna      | 237 ms                                                                      | 248 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 3.41 sec                                                                    | 3.32 sec: 1.03x faster                                                         |
| json_dumps           | 14.5 ms                                                                     | 14.1 ms: 1.03x faster                                                          |
| xml_etree_process    | 97.6 ms                                                                     | 96.1 ms: 1.02x faster                                                          |
| xml_etree_generate   | 119 ms                                                                      | 118 ms: 1.01x faster                                                           |
| pickle_pure_python   | 598 us                                                                      | 594 us: 1.01x faster                                                           |
| unpickle_pure_python | 406 us                                                                      | 409 us: 1.01x slower                                                           |
| xml_etree_parse      | 136 ms                                                                      | 138 ms: 1.01x slower                                                           |
| json_loads           | 29.7 us                                                                     | 30.0 us: 1.01x slower                                                          |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 85.5 ms                                                                     | 82.9 ms: 1.03x faster                                                          |
| django_template | 69.3 ms                                                                     | 67.7 ms: 1.02x faster                                                          |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.90 sec                                                                    | 1.77 sec: 1.07x faster                                                         |
| scimark_sor                | 256 ms                                                                      | 240 ms: 1.07x faster                                                           |
| scimark_lu                 | 248 ms                                                                      | 235 ms: 1.05x faster                                                           |
| coverage                   | 109 ms                                                                      | 104 ms: 1.05x faster                                                           |
| async_generators           | 521 ms                                                                      | 499 ms: 1.04x faster                                                           |
| nbody                      | 201 ms                                                                      | 193 ms: 1.04x faster                                                           |
| nqueens                    | 133 ms                                                                      | 128 ms: 1.04x faster                                                           |
| coroutines                 | 29.3 ms                                                                     | 28.3 ms: 1.03x faster                                                          |
| genshi_xml                 | 85.5 ms                                                                     | 82.9 ms: 1.03x faster                                                          |
| pprint_pformat             | 3.00 sec                                                                    | 2.92 sec: 1.03x faster                                                         |
| spectral_norm              | 171 ms                                                                      | 166 ms: 1.03x faster                                                           |
| float                      | 146 ms                                                                      | 142 ms: 1.03x faster                                                           |
| tomli_loads                | 3.41 sec                                                                    | 3.32 sec: 1.03x faster                                                         |
| json_dumps                 | 14.5 ms                                                                     | 14.1 ms: 1.03x faster                                                          |
| chaos                      | 127 ms                                                                      | 124 ms: 1.03x faster                                                           |
| fannkuch                   | 583 ms                                                                      | 569 ms: 1.02x faster                                                           |
| hexiom                     | 11.9 ms                                                                     | 11.7 ms: 1.02x faster                                                          |
| pycparser                  | 1.77 sec                                                                    | 1.73 sec: 1.02x faster                                                         |
| django_template            | 69.3 ms                                                                     | 67.7 ms: 1.02x faster                                                          |
| richards                   | 82.7 ms                                                                     | 80.8 ms: 1.02x faster                                                          |
| pprint_safe_repr           | 1.45 sec                                                                    | 1.42 sec: 1.02x faster                                                         |
| sqlglot_optimize           | 95.4 ms                                                                     | 93.5 ms: 1.02x faster                                                          |
| raytrace                   | 610 ms                                                                      | 599 ms: 1.02x faster                                                           |
| async_tree_memoization_tg  | 471 ms                                                                      | 462 ms: 1.02x faster                                                           |
| sqlglot_normalize          | 189 ms                                                                      | 186 ms: 1.02x faster                                                           |
| regex_compile              | 233 ms                                                                      | 229 ms: 1.02x faster                                                           |
| deepcopy_reduce            | 4.85 us                                                                     | 4.77 us: 1.02x faster                                                          |
| async_tree_none_tg         | 366 ms                                                                      | 360 ms: 1.02x faster                                                           |
| xml_etree_process          | 97.6 ms                                                                     | 96.1 ms: 1.02x faster                                                          |
| logging_silent             | 186 ns                                                                      | 183 ns: 1.02x faster                                                           |
| 2to3                       | 437 ms                                                                      | 431 ms: 1.01x faster                                                           |
| pyflate                    | 774 ms                                                                      | 763 ms: 1.01x faster                                                           |
| sympy_integrate            | 32.6 ms                                                                     | 32.1 ms: 1.01x faster                                                          |
| async_tree_none            | 419 ms                                                                      | 413 ms: 1.01x faster                                                           |
| mdp                        | 3.25 sec                                                                    | 3.21 sec: 1.01x faster                                                         |
| async_tree_memoization     | 521 ms                                                                      | 514 ms: 1.01x faster                                                           |
| async_tree_io_tg           | 891 ms                                                                      | 880 ms: 1.01x faster                                                           |
| meteor_contest             | 176 ms                                                                      | 174 ms: 1.01x faster                                                           |
| bpe_tokeniser              | 6.77 sec                                                                    | 6.69 sec: 1.01x faster                                                         |
| sympy_sum                  | 265 ms                                                                      | 262 ms: 1.01x faster                                                           |
| go                         | 333 ms                                                                      | 330 ms: 1.01x faster                                                           |
| docutils                   | 3.51 sec                                                                    | 3.48 sec: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 632 ms                                                                      | 626 ms: 1.01x faster                                                           |
| crypto_pyaes               | 122 ms                                                                      | 121 ms: 1.01x faster                                                           |
| async_tree_io              | 948 ms                                                                      | 940 ms: 1.01x faster                                                           |
| telco                      | 10.6 ms                                                                     | 10.5 ms: 1.01x faster                                                          |
| comprehensions             | 30.2 us                                                                     | 30.0 us: 1.01x faster                                                          |
| deltablue                  | 8.31 ms                                                                     | 8.25 ms: 1.01x faster                                                          |
| xml_etree_generate         | 119 ms                                                                      | 118 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed    | 683 ms                                                                      | 678 ms: 1.01x faster                                                           |
| sympy_str                  | 456 ms                                                                      | 453 ms: 1.01x faster                                                           |
| pickle_pure_python         | 598 us                                                                      | 594 us: 1.01x faster                                                           |
| html5lib                   | 109 ms                                                                      | 109 ms: 1.01x faster                                                           |
| deepcopy                   | 453 us                                                                      | 451 us: 1.01x faster                                                           |
| pidigits                   | 251 ms                                                                      | 250 ms: 1.00x faster                                                           |
| sympy_expand               | 823 ms                                                                      | 819 ms: 1.00x faster                                                           |
| unpickle_pure_python       | 406 us                                                                      | 409 us: 1.01x slower                                                           |
| asyncio_websockets         | 381 ms                                                                      | 384 ms: 1.01x slower                                                           |
| logging_simple             | 11.6 us                                                                     | 11.7 us: 1.01x slower                                                          |
| xml_etree_parse            | 136 ms                                                                      | 138 ms: 1.01x slower                                                           |
| generators                 | 41.3 ms                                                                     | 41.7 ms: 1.01x slower                                                          |
| json_loads                 | 29.7 us                                                                     | 30.0 us: 1.01x slower                                                          |
| deepcopy_memo              | 52.3 us                                                                     | 53.0 us: 1.01x slower                                                          |
| scimark_sparse_mat_mult    | 5.72 ms                                                                     | 5.80 ms: 1.01x slower                                                          |
| regex_v8                   | 26.9 ms                                                                     | 27.4 ms: 1.02x slower                                                          |
| scimark_fft                | 413 ms                                                                      | 425 ms: 1.03x slower                                                           |
| create_gc_cycles           | 1.61 ms                                                                     | 1.68 ms: 1.04x slower                                                          |
| regex_effbot               | 3.48 ms                                                                     | 3.65 ms: 1.05x slower                                                          |
| regex_dna                  | 237 ms                                                                      | 248 ms: 1.05x slower                                                           |
| gc_traversal               | 2.79 ms                                                                     | 3.27 ms: 1.17x slower                                                          |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (19): pylint, richards_super, bench_mp_pool, scimark_monte_carlo, tornado_http, logging_format, json, python_startup_no_site, thrift, genshi_text, python_startup, typing_runtime_protocols, xml_etree_iterparse, bench_thread_pool, asyncio_tcp, sqlglot_transpile, sqlglot_parse, pathlib, mako

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x