# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.09x slower
- HPT reliability: 77.31%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 313 ms: 1.08x slower                                                      |
| docutils       | 2.81 sec                                                     | 3.16 sec: 1.12x slower                                                    |
| html5lib       | 71.9 ms                                                      | 70.7 ms: 1.02x faster                                                     |
| tornado_http   | 120 ms                                                       | 123 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 373 ms: 1.24x faster                                                      |
| async_tree_memoization     | 452 ms                                                       | 410 ms: 1.10x faster                                                      |
| async_tree_none            | 372 ms                                                       | 342 ms: 1.09x faster                                                      |
| async_tree_none_tg         | 340 ms                                                       | 322 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 576 ms: 1.04x faster                                                      |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                     |
| async_generators           | 359 ms                                                       | 377 ms: 1.05x slower                                                      |
| async_tree_io_tg           | 819 ms                                                       | 866 ms: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                              |

Benchmark hidden because not significant (2): async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.6 ms: 1.04x faster                                                     |
| nbody          | 88.0 ms                                                      | 85.2 ms: 1.03x faster                                                     |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                        | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 241 ms: 1.01x faster                                                      |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                      |
| regex_effbot   | 3.37 ms                                                      | 3.68 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                        | 1.02x slower                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.09 sec: 1.15x faster                                                    |
| xml_etree_process    | 60.9 ms                                                      | 58.0 ms: 1.05x faster                                                     |
| xml_etree_generate   | 85.3 ms                                                      | 81.3 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 100 ms                                                       | 101 ms: 1.01x slower                                                      |
| unpickle_pure_python | 214 us                                                       | 217 us: 1.01x slower                                                      |
| xml_etree_parse      | 145 ms                                                       | 148 ms: 1.02x slower                                                      |
| json_dumps           | 11.0 ms                                                      | 11.2 ms: 1.02x slower                                                     |
| json_loads           | 24.0 us                                                      | 25.0 us: 1.04x slower                                                     |
| pickle_pure_python   | 318 us                                                       | 344 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.00 ms: 1.01x slower                                                     |
| python_startup         | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.43 ms: 1.10x faster                                                     |
| django_template | 38.9 ms                                                      | 44.0 ms: 1.13x slower                                                     |
| genshi_text     | 26.6 ms                                                      | 32.0 ms: 1.20x slower                                                     |
| genshi_xml      | 57.3 ms                                                      | 70.9 ms: 1.24x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.11x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 29.2 us: 1.35x faster                                                     |
| deepcopy                   | 397 us                                                       | 308 us: 1.29x faster                                                      |
| async_tree_memoization_tg  | 461 ms                                                       | 373 ms: 1.24x faster                                                      |
| scimark_sor                | 126 ms                                                       | 104 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 3.54 us                                                      | 3.03 us: 1.17x faster                                                     |
| tomli_loads                | 2.41 sec                                                     | 2.09 sec: 1.15x faster                                                    |
| telco                      | 8.58 ms                                                      | 7.69 ms: 1.12x faster                                                     |
| scimark_fft                | 314 ms                                                       | 283 ms: 1.11x faster                                                      |
| mako                       | 10.4 ms                                                      | 9.43 ms: 1.10x faster                                                     |
| async_tree_memoization     | 452 ms                                                       | 410 ms: 1.10x faster                                                      |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                     |
| async_tree_none            | 372 ms                                                       | 342 ms: 1.09x faster                                                      |
| bpe_tokeniser              | 5.10 sec                                                     | 4.68 sec: 1.09x faster                                                    |
| richards                   | 52.7 ms                                                      | 48.8 ms: 1.08x faster                                                     |
| pyflate                    | 492 ms                                                       | 459 ms: 1.07x faster                                                      |
| logging_silent             | 97.7 ns                                                      | 92.2 ns: 1.06x faster                                                     |
| async_tree_none_tg         | 340 ms                                                       | 322 ms: 1.06x faster                                                      |
| xml_etree_process          | 60.9 ms                                                      | 58.0 ms: 1.05x faster                                                     |
| xml_etree_generate         | 85.3 ms                                                      | 81.3 ms: 1.05x faster                                                     |
| spectral_norm              | 97.4 ms                                                      | 93.3 ms: 1.04x faster                                                     |
| go                         | 160 ms                                                       | 154 ms: 1.04x faster                                                      |
| float                      | 81.9 ms                                                      | 78.6 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 576 ms: 1.04x faster                                                      |
| nbody                      | 88.0 ms                                                      | 85.2 ms: 1.03x faster                                                     |
| deltablue                  | 3.41 ms                                                      | 3.31 ms: 1.03x faster                                                     |
| dulwich_log                | 65.5 ms                                                      | 63.7 ms: 1.03x faster                                                     |
| richards_super             | 59.8 ms                                                      | 58.2 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                     |
| html5lib                   | 71.9 ms                                                      | 70.7 ms: 1.02x faster                                                     |
| scimark_lu                 | 97.8 ms                                                      | 96.2 ms: 1.02x faster                                                     |
| pprint_safe_repr           | 812 ms                                                       | 801 ms: 1.01x faster                                                      |
| regex_dna                  | 244 ms                                                       | 241 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.26 ms: 1.01x faster                                                     |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                      |
| python_startup_no_site     | 8.94 ms                                                      | 9.00 ms: 1.01x slower                                                     |
| xml_etree_iterparse        | 100 ms                                                       | 101 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 214 us                                                       | 217 us: 1.01x slower                                                      |
| fannkuch                   | 365 ms                                                       | 371 ms: 1.02x slower                                                      |
| xml_etree_parse            | 145 ms                                                       | 148 ms: 1.02x slower                                                      |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                      |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                      |
| json_dumps                 | 11.0 ms                                                      | 11.2 ms: 1.02x slower                                                     |
| thrift                     | 877 us                                                       | 899 us: 1.03x slower                                                      |
| pycparser                  | 1.26 sec                                                     | 1.29 sec: 1.03x slower                                                    |
| logging_format             | 7.07 us                                                      | 7.29 us: 1.03x slower                                                     |
| tornado_http               | 120 ms                                                       | 123 ms: 1.03x slower                                                      |
| logging_simple             | 6.40 us                                                      | 6.60 us: 1.03x slower                                                     |
| json_loads                 | 24.0 us                                                      | 25.0 us: 1.04x slower                                                     |
| bench_thread_pool          | 901 us                                                       | 941 us: 1.04x slower                                                      |
| typing_runtime_protocols   | 174 us                                                       | 182 us: 1.05x slower                                                      |
| sympy_expand               | 505 ms                                                       | 529 ms: 1.05x slower                                                      |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.1 ms: 1.05x slower                                                     |
| async_generators           | 359 ms                                                       | 377 ms: 1.05x slower                                                      |
| mdp                        | 2.52 sec                                                     | 2.65 sec: 1.05x slower                                                    |
| async_tree_io_tg           | 819 ms                                                       | 866 ms: 1.06x slower                                                      |
| sympy_str                  | 296 ms                                                       | 317 ms: 1.07x slower                                                      |
| 2to3                       | 291 ms                                                       | 313 ms: 1.08x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.49 ms: 1.08x slower                                                     |
| pickle_pure_python         | 318 us                                                       | 344 us: 1.08x slower                                                      |
| raytrace                   | 289 ms                                                       | 313 ms: 1.08x slower                                                      |
| regex_effbot               | 3.37 ms                                                      | 3.68 ms: 1.09x slower                                                     |
| sqlglot_transpile          | 1.78 ms                                                      | 1.95 ms: 1.09x slower                                                     |
| comprehensions             | 17.3 us                                                      | 18.9 us: 1.10x slower                                                     |
| sympy_sum                  | 154 ms                                                       | 171 ms: 1.11x slower                                                      |
| generators                 | 33.5 ms                                                      | 37.3 ms: 1.11x slower                                                     |
| python_startup             | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                     |
| docutils                   | 2.81 sec                                                     | 3.16 sec: 1.12x slower                                                    |
| hexiom                     | 6.33 ms                                                      | 7.12 ms: 1.12x slower                                                     |
| sqlglot_normalize          | 118 ms                                                       | 134 ms: 1.13x slower                                                      |
| django_template            | 38.9 ms                                                      | 44.0 ms: 1.13x slower                                                     |
| sqlglot_optimize           | 59.7 ms                                                      | 68.2 ms: 1.14x slower                                                     |
| chaos                      | 61.7 ms                                                      | 70.8 ms: 1.15x slower                                                     |
| sympy_integrate            | 23.3 ms                                                      | 26.8 ms: 1.15x slower                                                     |
| nqueens                    | 88.2 ms                                                      | 102 ms: 1.16x slower                                                      |
| pylint                     | 346 ms                                                       | 407 ms: 1.18x slower                                                      |
| genshi_text                | 26.6 ms                                                      | 32.0 ms: 1.20x slower                                                     |
| genshi_xml                 | 57.3 ms                                                      | 70.9 ms: 1.24x slower                                                     |
| gc_traversal               | 4.11 ms                                                      | 5.53 ms: 1.35x slower                                                     |
| create_gc_cycles           | 1.76 ms                                                      | 2.88 ms: 1.64x slower                                                     |
| bench_mp_pool              | 4.65 ms                                                      | 2.82 sec: 605.07x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                              |

Benchmark hidden because not significant (7): regex_v8, async_tree_io, coverage, pprint_pformat, asyncio_websockets, crypto_pyaes, json
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: sphinx

# HPT report

- Reliability score: 77.31% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.20x