# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.09x slower
- HPT reliability: 74.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 313 ms: 1.10x slower                                                      |
| docutils       | 2.87 sec                                                     | 3.16 sec: 1.10x slower                                                    |
| tornado_http   | 121 ms                                                       | 123 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.07x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 373 ms: 1.45x faster                                                      |
| async_tree_none_tg         | 431 ms                                                       | 322 ms: 1.34x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 410 ms: 1.33x faster                                                      |
| async_tree_none            | 452 ms                                                       | 342 ms: 1.32x faster                                                      |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 844 ms: 1.23x faster                                                      |
| async_tree_io_tg           | 1.05 sec                                                     | 866 ms: 1.22x faster                                                      |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                      |
| Geometric mean             | (ref)                                                        | 1.29x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                      |
| nbody          | 88.0 ms                                                      | 85.2 ms: 1.03x faster                                                     |
| float          | 76.6 ms                                                      | 78.6 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                        | 1.02x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                                      |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                      |
| regex_effbot   | 3.57 ms                                                      | 3.68 ms: 1.03x slower                                                     |
| regex_v8       | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                        | 1.04x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.3 ms: 1.06x faster                                                     |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                    |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                      |
| xml_etree_process    | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                     |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                     |
| xml_etree_parse      | 144 ms                                                       | 148 ms: 1.03x slower                                                      |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.04x slower                                                      |
| pickle_pure_python   | 318 us                                                       | 344 us: 1.08x slower                                                      |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                     |
| python_startup         | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.43 ms: 1.06x faster                                                     |
| django_template | 38.2 ms                                                      | 44.0 ms: 1.15x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 373 ms: 1.45x faster                                                      |
| async_tree_none_tg         | 431 ms                                                       | 322 ms: 1.34x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 410 ms: 1.33x faster                                                      |
| async_tree_none            | 452 ms                                                       | 342 ms: 1.32x faster                                                      |
| deepcopy_memo              | 36.8 us                                                      | 29.2 us: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 844 ms: 1.23x faster                                                      |
| async_tree_io_tg           | 1.05 sec                                                     | 866 ms: 1.22x faster                                                      |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                      |
| deepcopy                   | 368 us                                                       | 308 us: 1.19x faster                                                      |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                     |
| comprehensions             | 21.9 us                                                      | 18.9 us: 1.16x faster                                                     |
| deepcopy_reduce            | 3.37 us                                                      | 3.03 us: 1.11x faster                                                     |
| crypto_pyaes               | 80.3 ms                                                      | 73.0 ms: 1.10x faster                                                     |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.09x faster                                                     |
| scimark_fft                | 301 ms                                                       | 283 ms: 1.06x faster                                                      |
| mako                       | 10.0 ms                                                      | 9.43 ms: 1.06x faster                                                     |
| xml_etree_generate         | 86.1 ms                                                      | 81.3 ms: 1.06x faster                                                     |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                      |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.04x faster                                                      |
| async_generators           | 390 ms                                                       | 377 ms: 1.03x faster                                                      |
| tomli_loads                | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                    |
| nbody                      | 88.0 ms                                                      | 85.2 ms: 1.03x faster                                                     |
| logging_format             | 7.48 us                                                      | 7.29 us: 1.03x faster                                                     |
| dulwich_log                | 65.4 ms                                                      | 63.7 ms: 1.03x faster                                                     |
| scimark_lu                 | 98.8 ms                                                      | 96.2 ms: 1.03x faster                                                     |
| logging_silent             | 94.4 ns                                                      | 92.2 ns: 1.02x faster                                                     |
| logging_simple             | 6.71 us                                                      | 6.60 us: 1.02x faster                                                     |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                      |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.1 ms: 1.01x faster                                                     |
| asyncio_websockets         | 387 ms                                                       | 383 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 801 ms: 1.01x faster                                                      |
| xml_etree_process          | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                     |
| generators                 | 37.4 ms                                                      | 37.3 ms: 1.00x faster                                                     |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.26 ms: 1.01x slower                                                     |
| spectral_norm              | 91.6 ms                                                      | 93.3 ms: 1.02x slower                                                     |
| tornado_http               | 121 ms                                                       | 123 ms: 1.02x slower                                                      |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                      |
| deltablue                  | 3.24 ms                                                      | 3.31 ms: 1.02x slower                                                     |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                      |
| float                      | 76.6 ms                                                      | 78.6 ms: 1.03x slower                                                     |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                     |
| json                       | 5.12 ms                                                      | 5.25 ms: 1.03x slower                                                     |
| xml_etree_parse            | 144 ms                                                       | 148 ms: 1.03x slower                                                      |
| go                         | 150 ms                                                       | 154 ms: 1.03x slower                                                      |
| regex_effbot               | 3.57 ms                                                      | 3.68 ms: 1.03x slower                                                     |
| mdp                        | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                    |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.04x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                     |
| pyflate                    | 439 ms                                                       | 459 ms: 1.05x slower                                                      |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.05x slower                                                    |
| sympy_str                  | 302 ms                                                       | 317 ms: 1.05x slower                                                      |
| raytrace                   | 298 ms                                                       | 313 ms: 1.05x slower                                                      |
| sympy_sum                  | 162 ms                                                       | 171 ms: 1.06x slower                                                      |
| fannkuch                   | 350 ms                                                       | 371 ms: 1.06x slower                                                      |
| richards                   | 45.7 ms                                                      | 48.8 ms: 1.07x slower                                                     |
| pickle_pure_python         | 318 us                                                       | 344 us: 1.08x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.49 ms: 1.08x slower                                                     |
| regex_v8                   | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                     |
| sympy_expand               | 484 ms                                                       | 529 ms: 1.09x slower                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.95 ms: 1.10x slower                                                     |
| 2to3                       | 285 ms                                                       | 313 ms: 1.10x slower                                                      |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                     |
| docutils                   | 2.87 sec                                                     | 3.16 sec: 1.10x slower                                                    |
| telco                      | 6.96 ms                                                      | 7.69 ms: 1.10x slower                                                     |
| chaos                      | 64.0 ms                                                      | 70.8 ms: 1.11x slower                                                     |
| sympy_integrate            | 23.9 ms                                                      | 26.8 ms: 1.12x slower                                                     |
| richards_super             | 51.3 ms                                                      | 58.2 ms: 1.13x slower                                                     |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.14x slower                                                      |
| django_template            | 38.2 ms                                                      | 44.0 ms: 1.15x slower                                                     |
| sqlglot_normalize          | 116 ms                                                       | 134 ms: 1.16x slower                                                      |
| sqlglot_optimize           | 57.5 ms                                                      | 68.2 ms: 1.19x slower                                                     |
| hexiom                     | 5.96 ms                                                      | 7.12 ms: 1.20x slower                                                     |
| typing_runtime_protocols   | 152 us                                                       | 182 us: 1.20x slower                                                      |
| coverage                   | 66.7 ms                                                      | 81.1 ms: 1.22x slower                                                     |
| python_startup             | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                     |
| gc_traversal               | 3.48 ms                                                      | 5.53 ms: 1.59x slower                                                     |
| create_gc_cycles           | 1.59 ms                                                      | 2.88 ms: 1.81x slower                                                     |
| bench_mp_pool              | 4.76 ms                                                      | 2.82 sec: 591.17x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                              |

Benchmark hidden because not significant (2): bench_thread_pool, pprint_pformat
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 74.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x