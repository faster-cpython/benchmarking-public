# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.002x slower
- HPT reliability: 98.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 317 ms                                                                       | 313 ms: 1.02x faster                                                      |
| docutils       | 3.21 sec                                                                     | 3.16 sec: 1.02x faster                                                    |
| html5lib       | 72.2 ms                                                                      | 70.7 ms: 1.02x faster                                                     |
| sphinx         | 1.27 sec                                                                     | 1.24 sec: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 378 ms                                                                       | 373 ms: 1.01x faster                                                      |
| async_generators           | 382 ms                                                                       | 377 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed_tg | 568 ms                                                                       | 561 ms: 1.01x faster                                                      |
| async_tree_io_tg           | 874 ms                                                                       | 866 ms: 1.01x faster                                                      |
| coroutines                 | 21.1 ms                                                                      | 21.2 ms: 1.00x slower                                                     |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                              |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                                      | 78.6 ms: 1.01x faster                                                     |
| pidigits       | 251 ms                                                                       | 251 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                                       | 241 ms: 1.02x faster                                                      |
| regex_compile  | 147 ms                                                                       | 147 ms: 1.00x slower                                                      |
| regex_effbot   | 3.56 ms                                                                      | 3.68 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|---------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_process   | 59.0 ms                                                                      | 58.0 ms: 1.02x faster                                                     |
| xml_etree_generate  | 82.3 ms                                                                      | 81.3 ms: 1.01x faster                                                     |
| json_loads          | 24.8 us                                                                      | 25.0 us: 1.01x slower                                                     |
| xml_etree_iterparse | 99.6 ms                                                                      | 101 ms: 1.02x slower                                                      |
| json_dumps          | 11.0 ms                                                                      | 11.2 ms: 1.02x slower                                                     |
| pickle_pure_python  | 337 us                                                                       | 344 us: 1.02x slower                                                      |
| xml_etree_parse     | 141 ms                                                                       | 148 ms: 1.05x slower                                                      |
| Geometric mean      | (ref)                                                                        | 1.01x slower                                                              |

Benchmark hidden because not significant (2): tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.99 ms                                                                      | 9.00 ms: 1.00x slower                                                     |
| python_startup         | 14.8 ms                                                                      | 14.9 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 44.8 ms                                                                      | 44.0 ms: 1.02x faster                                                     |
| mako            | 9.48 ms                                                                      | 9.43 ms: 1.00x faster                                                     |
| genshi_xml      | 63.2 ms                                                                      | 70.9 ms: 1.12x slower                                                     |
| genshi_text     | 27.6 ms                                                                      | 32.0 ms: 1.16x slower                                                     |
| Geometric mean  | (ref)                                                                        | 1.06x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators                 | 38.7 ms                                                                      | 37.3 ms: 1.04x faster                                                     |
| scimark_sparse_mat_mult    | 4.42 ms                                                                      | 4.26 ms: 1.04x faster                                                     |
| logging_simple             | 6.84 us                                                                      | 6.60 us: 1.04x faster                                                     |
| logging_format             | 7.53 us                                                                      | 7.29 us: 1.03x faster                                                     |
| deepcopy_memo              | 30.0 us                                                                      | 29.2 us: 1.03x faster                                                     |
| sqlglot_optimize           | 70.2 ms                                                                      | 68.2 ms: 1.03x faster                                                     |
| sqlglot_transpile          | 1.99 ms                                                                      | 1.95 ms: 1.02x faster                                                     |
| sympy_sum                  | 175 ms                                                                       | 171 ms: 1.02x faster                                                      |
| sphinx                     | 1.27 sec                                                                     | 1.24 sec: 1.02x faster                                                    |
| sqlglot_parse              | 1.52 ms                                                                      | 1.49 ms: 1.02x faster                                                     |
| html5lib                   | 72.2 ms                                                                      | 70.7 ms: 1.02x faster                                                     |
| bpe_tokeniser              | 4.77 sec                                                                     | 4.68 sec: 1.02x faster                                                    |
| xml_etree_process          | 59.0 ms                                                                      | 58.0 ms: 1.02x faster                                                     |
| scimark_monte_carlo        | 69.3 ms                                                                      | 68.1 ms: 1.02x faster                                                     |
| sympy_integrate            | 27.3 ms                                                                      | 26.8 ms: 1.02x faster                                                     |
| django_template            | 44.8 ms                                                                      | 44.0 ms: 1.02x faster                                                     |
| scimark_fft                | 288 ms                                                                       | 283 ms: 1.02x faster                                                      |
| docutils                   | 3.21 sec                                                                     | 3.16 sec: 1.02x faster                                                    |
| 2to3                       | 317 ms                                                                       | 313 ms: 1.02x faster                                                      |
| regex_dna                  | 244 ms                                                                       | 241 ms: 1.02x faster                                                      |
| async_tree_memoization_tg  | 378 ms                                                                       | 373 ms: 1.01x faster                                                      |
| sympy_str                  | 321 ms                                                                       | 317 ms: 1.01x faster                                                      |
| async_generators           | 382 ms                                                                       | 377 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed_tg | 568 ms                                                                       | 561 ms: 1.01x faster                                                      |
| xml_etree_generate         | 82.3 ms                                                                      | 81.3 ms: 1.01x faster                                                     |
| async_tree_io_tg           | 874 ms                                                                       | 866 ms: 1.01x faster                                                      |
| pathlib                    | 16.0 ms                                                                      | 15.9 ms: 1.01x faster                                                     |
| hexiom                     | 7.19 ms                                                                      | 7.12 ms: 1.01x faster                                                     |
| scimark_sor                | 105 ms                                                                       | 104 ms: 1.01x faster                                                      |
| sympy_expand               | 533 ms                                                                       | 529 ms: 1.01x faster                                                      |
| telco                      | 7.75 ms                                                                      | 7.69 ms: 1.01x faster                                                     |
| go                         | 155 ms                                                                       | 154 ms: 1.01x faster                                                      |
| float                      | 79.2 ms                                                                      | 78.6 ms: 1.01x faster                                                     |
| create_gc_cycles           | 2.89 ms                                                                      | 2.88 ms: 1.00x faster                                                     |
| mako                       | 9.48 ms                                                                      | 9.43 ms: 1.00x faster                                                     |
| pidigits                   | 251 ms                                                                       | 251 ms: 1.00x faster                                                      |
| python_startup_no_site     | 8.99 ms                                                                      | 9.00 ms: 1.00x slower                                                     |
| regex_compile              | 147 ms                                                                       | 147 ms: 1.00x slower                                                      |
| coroutines                 | 21.1 ms                                                                      | 21.2 ms: 1.00x slower                                                     |
| python_startup             | 14.8 ms                                                                      | 14.9 ms: 1.00x slower                                                     |
| json_loads                 | 24.8 us                                                                      | 25.0 us: 1.01x slower                                                     |
| pyflate                    | 456 ms                                                                       | 459 ms: 1.01x slower                                                      |
| raytrace                   | 310 ms                                                                       | 313 ms: 1.01x slower                                                      |
| spectral_norm              | 92.5 ms                                                                      | 93.3 ms: 1.01x slower                                                     |
| fannkuch                   | 368 ms                                                                       | 371 ms: 1.01x slower                                                      |
| meteor_contest             | 130 ms                                                                       | 131 ms: 1.01x slower                                                      |
| dulwich_log                | 63.1 ms                                                                      | 63.7 ms: 1.01x slower                                                     |
| comprehensions             | 18.7 us                                                                      | 18.9 us: 1.01x slower                                                     |
| xml_etree_iterparse        | 99.6 ms                                                                      | 101 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.62 sec                                                                     | 1.65 sec: 1.02x slower                                                    |
| pprint_safe_repr           | 788 ms                                                                       | 801 ms: 1.02x slower                                                      |
| json_dumps                 | 11.0 ms                                                                      | 11.2 ms: 1.02x slower                                                     |
| json                       | 5.15 ms                                                                      | 5.25 ms: 1.02x slower                                                     |
| pickle_pure_python         | 337 us                                                                       | 344 us: 1.02x slower                                                      |
| mdp                        | 2.58 sec                                                                     | 2.65 sec: 1.03x slower                                                    |
| regex_effbot               | 3.56 ms                                                                      | 3.68 ms: 1.03x slower                                                     |
| chaos                      | 68.1 ms                                                                      | 70.8 ms: 1.04x slower                                                     |
| xml_etree_parse            | 141 ms                                                                       | 148 ms: 1.05x slower                                                      |
| richards_super             | 55.4 ms                                                                      | 58.2 ms: 1.05x slower                                                     |
| richards                   | 46.4 ms                                                                      | 48.8 ms: 1.05x slower                                                     |
| gc_traversal               | 5.21 ms                                                                      | 5.53 ms: 1.06x slower                                                     |
| genshi_xml                 | 63.2 ms                                                                      | 70.9 ms: 1.12x slower                                                     |
| genshi_text                | 27.6 ms                                                                      | 32.0 ms: 1.16x slower                                                     |
| Geometric mean             | (ref)                                                                        | 1.01x slower                                                              |

Benchmark hidden because not significant (26): pylint, async_tree_memoization, deepcopy_reduce, async_tree_none_tg, async_tree_cpu_io_mixed, typing_runtime_protocols, deltablue, async_tree_none, sqlglot_normalize, coverage, bench_thread_pool, scimark_lu, tomli_loads, nqueens, async_tree_io, nbody, thrift, unpickle_pure_python, logging_silent, asyncio_websockets, crypto_pyaes, pycparser, deepcopy, regex_v8, tornado_http, bench_mp_pool

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 98.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x