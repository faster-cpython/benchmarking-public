# Results vs. base

- fork: faster-cpython
- ref: load_const_return_re
- machine: linux-x86_64
- commit hash: 031f320
- commit date: 2024-10-23
- overall geometric mean: 1.00x faster
- HPT reliability: 99.63%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 314 ms                                                                       | 317 ms: 1.01x slower                                                                   |
| docutils       | 3.22 sec                                                                     | 3.19 sec: 1.01x faster                                                                 |
| html5lib       | 71.0 ms                                                                      | 71.8 ms: 1.01x slower                                                                  |
| sphinx         | 1.28 sec                                                                     | 1.26 sec: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| coroutines                 | 21.2 ms                                                                      | 20.4 ms: 1.04x faster                                                                  |
| async_tree_io              | 842 ms                                                                       | 819 ms: 1.03x faster                                                                   |
| async_generators           | 390 ms                                                                       | 380 ms: 1.03x faster                                                                   |
| async_tree_memoization_tg  | 377 ms                                                                       | 371 ms: 1.02x faster                                                                   |
| async_tree_none            | 342 ms                                                                       | 337 ms: 1.01x faster                                                                   |
| async_tree_io_tg           | 870 ms                                                                       | 861 ms: 1.01x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                       | 560 ms: 1.01x faster                                                                   |
| asyncio_websockets         | 382 ms                                                                       | 385 ms: 1.01x slower                                                                   |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 79.4 ms                                                                      | 80.7 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 242 ms                                                                       | 234 ms: 1.03x faster                                                                   |
| regex_v8       | 25.5 ms                                                                      | 24.8 ms: 1.03x faster                                                                  |
| regex_effbot   | 3.65 ms                                                                      | 3.60 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                                        | 1.02x faster                                                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_process    | 60.3 ms                                                                      | 56.9 ms: 1.06x faster                                                                  |
| xml_etree_generate   | 84.5 ms                                                                      | 80.0 ms: 1.06x faster                                                                  |
| json_loads           | 25.0 us                                                                      | 24.6 us: 1.02x faster                                                                  |
| json_dumps           | 11.0 ms                                                                      | 10.9 ms: 1.01x faster                                                                  |
| unpickle_pure_python | 220 us                                                                       | 222 us: 1.01x slower                                                                   |
| xml_etree_iterparse  | 101 ms                                                                       | 101 ms: 1.01x slower                                                                   |
| tomli_loads          | 2.10 sec                                                                     | 2.13 sec: 1.01x slower                                                                 |
| pickle_pure_python   | 333 us                                                                       | 340 us: 1.02x slower                                                                   |
| Geometric mean       | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 9.05 ms                                                                      | 9.11 ms: 1.01x slower                                                                  |
| python_startup         | 14.9 ms                                                                      | 15.1 ms: 1.01x slower                                                                  |
| Geometric mean         | (ref)                                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text     | 30.2 ms                                                                      | 29.9 ms: 1.01x faster                                                                  |
| mako            | 9.42 ms                                                                      | 9.44 ms: 1.00x slower                                                                  |
| django_template | 43.4 ms                                                                      | 43.8 ms: 1.01x slower                                                                  |
| genshi_xml      | 63.6 ms                                                                      | 66.9 ms: 1.05x slower                                                                  |
| Geometric mean  | (ref)                                                                        | 1.01x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| coverage                   | 86.3 ms                                                                      | 79.3 ms: 1.09x faster                                                                  |
| xml_etree_process          | 60.3 ms                                                                      | 56.9 ms: 1.06x faster                                                                  |
| xml_etree_generate         | 84.5 ms                                                                      | 80.0 ms: 1.06x faster                                                                  |
| thrift                     | 928 us                                                                       | 887 us: 1.05x faster                                                                   |
| raytrace                   | 336 ms                                                                       | 323 ms: 1.04x faster                                                                   |
| nqueens                    | 103 ms                                                                       | 99.5 ms: 1.04x faster                                                                  |
| coroutines                 | 21.2 ms                                                                      | 20.4 ms: 1.04x faster                                                                  |
| regex_dna                  | 242 ms                                                                       | 234 ms: 1.03x faster                                                                   |
| scimark_sparse_mat_mult    | 4.40 ms                                                                      | 4.25 ms: 1.03x faster                                                                  |
| pprint_pformat             | 1.67 sec                                                                     | 1.62 sec: 1.03x faster                                                                 |
| async_tree_io              | 842 ms                                                                       | 819 ms: 1.03x faster                                                                   |
| regex_v8                   | 25.5 ms                                                                      | 24.8 ms: 1.03x faster                                                                  |
| chaos                      | 69.5 ms                                                                      | 67.7 ms: 1.03x faster                                                                  |
| spectral_norm              | 95.7 ms                                                                      | 93.3 ms: 1.03x faster                                                                  |
| async_generators           | 390 ms                                                                       | 380 ms: 1.03x faster                                                                   |
| mdp                        | 2.66 sec                                                                     | 2.60 sec: 1.02x faster                                                                 |
| generators                 | 39.7 ms                                                                      | 38.9 ms: 1.02x faster                                                                  |
| scimark_sor                | 106 ms                                                                       | 104 ms: 1.02x faster                                                                   |
| json_loads                 | 25.0 us                                                                      | 24.6 us: 1.02x faster                                                                  |
| async_tree_memoization_tg  | 377 ms                                                                       | 371 ms: 1.02x faster                                                                   |
| sphinx                     | 1.28 sec                                                                     | 1.26 sec: 1.01x faster                                                                 |
| async_tree_none            | 342 ms                                                                       | 337 ms: 1.01x faster                                                                   |
| sympy_sum                  | 177 ms                                                                       | 175 ms: 1.01x faster                                                                   |
| regex_effbot               | 3.65 ms                                                                      | 3.60 ms: 1.01x faster                                                                  |
| pprint_safe_repr           | 794 ms                                                                       | 784 ms: 1.01x faster                                                                   |
| fannkuch                   | 380 ms                                                                       | 375 ms: 1.01x faster                                                                   |
| sympy_integrate            | 27.6 ms                                                                      | 27.3 ms: 1.01x faster                                                                  |
| json                       | 5.26 ms                                                                      | 5.21 ms: 1.01x faster                                                                  |
| async_tree_io_tg           | 870 ms                                                                       | 861 ms: 1.01x faster                                                                   |
| genshi_text                | 30.2 ms                                                                      | 29.9 ms: 1.01x faster                                                                  |
| docutils                   | 3.22 sec                                                                     | 3.19 sec: 1.01x faster                                                                 |
| telco                      | 7.75 ms                                                                      | 7.69 ms: 1.01x faster                                                                  |
| pathlib                    | 16.1 ms                                                                      | 16.0 ms: 1.01x faster                                                                  |
| meteor_contest             | 131 ms                                                                       | 130 ms: 1.01x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                       | 560 ms: 1.01x faster                                                                   |
| json_dumps                 | 11.0 ms                                                                      | 10.9 ms: 1.01x faster                                                                  |
| sympy_str                  | 323 ms                                                                       | 321 ms: 1.01x faster                                                                   |
| sympy_expand               | 534 ms                                                                       | 533 ms: 1.00x faster                                                                   |
| bpe_tokeniser              | 4.77 sec                                                                     | 4.77 sec: 1.00x slower                                                                 |
| mako                       | 9.42 ms                                                                      | 9.44 ms: 1.00x slower                                                                  |
| sqlglot_parse              | 1.51 ms                                                                      | 1.52 ms: 1.00x slower                                                                  |
| sqlglot_transpile          | 1.98 ms                                                                      | 1.99 ms: 1.00x slower                                                                  |
| comprehensions             | 18.8 us                                                                      | 18.9 us: 1.01x slower                                                                  |
| python_startup_no_site     | 9.05 ms                                                                      | 9.11 ms: 1.01x slower                                                                  |
| unpickle_pure_python       | 220 us                                                                       | 222 us: 1.01x slower                                                                   |
| python_startup             | 14.9 ms                                                                      | 15.1 ms: 1.01x slower                                                                  |
| asyncio_websockets         | 382 ms                                                                       | 385 ms: 1.01x slower                                                                   |
| xml_etree_iterparse        | 101 ms                                                                       | 101 ms: 1.01x slower                                                                   |
| pyflate                    | 452 ms                                                                       | 456 ms: 1.01x slower                                                                   |
| sqlglot_normalize          | 133 ms                                                                       | 135 ms: 1.01x slower                                                                   |
| 2to3                       | 314 ms                                                                       | 317 ms: 1.01x slower                                                                   |
| logging_format             | 7.12 us                                                                      | 7.18 us: 1.01x slower                                                                  |
| tomli_loads                | 2.10 sec                                                                     | 2.13 sec: 1.01x slower                                                                 |
| html5lib                   | 71.0 ms                                                                      | 71.8 ms: 1.01x slower                                                                  |
| create_gc_cycles           | 2.89 ms                                                                      | 2.92 ms: 1.01x slower                                                                  |
| dulwich_log                | 63.1 ms                                                                      | 63.8 ms: 1.01x slower                                                                  |
| django_template            | 43.4 ms                                                                      | 43.8 ms: 1.01x slower                                                                  |
| float                      | 79.4 ms                                                                      | 80.7 ms: 1.02x slower                                                                  |
| pickle_pure_python         | 333 us                                                                       | 340 us: 1.02x slower                                                                   |
| deepcopy                   | 309 us                                                                       | 316 us: 1.02x slower                                                                   |
| logging_simple             | 6.54 us                                                                      | 6.69 us: 1.02x slower                                                                  |
| scimark_monte_carlo        | 68.6 ms                                                                      | 70.3 ms: 1.02x slower                                                                  |
| pycparser                  | 1.27 sec                                                                     | 1.30 sec: 1.02x slower                                                                 |
| go                         | 154 ms                                                                       | 157 ms: 1.02x slower                                                                   |
| richards                   | 46.1 ms                                                                      | 48.3 ms: 1.05x slower                                                                  |
| gc_traversal               | 5.53 ms                                                                      | 5.80 ms: 1.05x slower                                                                  |
| logging_silent             | 98.2 ns                                                                      | 103 ns: 1.05x slower                                                                   |
| genshi_xml                 | 63.6 ms                                                                      | 66.9 ms: 1.05x slower                                                                  |
| richards_super             | 51.0 ms                                                                      | 54.6 ms: 1.07x slower                                                                  |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (20): async_tree_none_tg, pylint, async_tree_memoization, tornado_http, nbody, async_tree_cpu_io_mixed, hexiom, scimark_lu, xml_etree_parse, pidigits, crypto_pyaes, regex_compile, deltablue, sqlglot_optimize, deepcopy_reduce, typing_runtime_protocols, bench_thread_pool, scimark_fft, deepcopy_memo, bench_mp_pool

# HPT report

- Reliability score: 99.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x