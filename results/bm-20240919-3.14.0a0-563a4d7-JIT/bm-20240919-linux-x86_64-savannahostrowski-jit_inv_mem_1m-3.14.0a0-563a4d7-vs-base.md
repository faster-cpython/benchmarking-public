# Results vs. base

- fork: savannahostrowski
- ref: jit_inv_mem_1m
- machine: linux-x86_64
- commit hash: 563a4d7
- commit date: 2024-09-19
- overall geometric mean: 1.01x slower
- HPT reliability: 99.23%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 277 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 497 ms                                                                | 487 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 557 ms                                                                | 547 ms: 1.02x faster                                                       |
| coroutines                 | 23.6 ms                                                               | 23.4 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                     |
| async_generators           | 451 ms                                                                | 453 ms: 1.01x slower                                                       |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                               |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_memoization, asyncio_websockets, async_tree_none, async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 69.9 ms                                                               | 69.7 ms: 1.00x faster                                                      |
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                                       |
| nbody          | 79.7 ms                                                               | 81.3 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 224 ms                                                                | 218 ms: 1.03x faster                                                       |
| regex_effbot   | 3.82 ms                                                               | 3.76 ms: 1.02x faster                                                      |
| regex_v8       | 24.6 ms                                                               | 24.7 ms: 1.00x slower                                                      |
| regex_compile  | 142 ms                                                                | 144 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 10.1 ms                                                               | 9.88 ms: 1.02x faster                                                      |
| unpickle_list        | 5.40 us                                                               | 5.31 us: 1.02x faster                                                      |
| xml_etree_parse      | 146 ms                                                                | 144 ms: 1.01x faster                                                       |
| pickle_list          | 5.09 us                                                               | 5.07 us: 1.00x faster                                                      |
| xml_etree_iterparse  | 98.2 ms                                                               | 98.8 ms: 1.01x slower                                                      |
| xml_etree_process    | 54.1 ms                                                               | 54.5 ms: 1.01x slower                                                      |
| unpickle_pure_python | 215 us                                                                | 217 us: 1.01x slower                                                       |
| pickle               | 11.4 us                                                               | 11.6 us: 1.02x slower                                                      |
| pickle_dict          | 34.1 us                                                               | 34.9 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (5): pickle_pure_python, json_loads, tomli_loads, xml_etree_generate, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                               | 7.05 ms: 1.01x faster                                                      |
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 10.0 ms                                                               | 9.79 ms: 1.02x faster                                                      |
| genshi_text    | 25.5 ms                                                               | 25.8 ms: 1.01x slower                                                      |
| genshi_xml     | 59.6 ms                                                               | 61.2 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 3.90 ms                                                               | 3.74 ms: 1.04x faster                                                      |
| regex_dna                  | 224 ms                                                                | 218 ms: 1.03x faster                                                       |
| json_dumps                 | 10.1 ms                                                               | 9.88 ms: 1.02x faster                                                      |
| mako                       | 10.0 ms                                                               | 9.79 ms: 1.02x faster                                                      |
| asyncio_tcp                | 497 ms                                                                | 487 ms: 1.02x faster                                                       |
| regex_effbot               | 3.82 ms                                                               | 3.76 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg | 557 ms                                                                | 547 ms: 1.02x faster                                                       |
| unpickle_list              | 5.40 us                                                               | 5.31 us: 1.02x faster                                                      |
| xml_etree_parse            | 146 ms                                                                | 144 ms: 1.01x faster                                                       |
| create_gc_cycles           | 1.76 ms                                                               | 1.74 ms: 1.01x faster                                                      |
| pathlib                    | 16.2 ms                                                               | 16.0 ms: 1.01x faster                                                      |
| sqlglot_normalize          | 113 ms                                                                | 112 ms: 1.01x faster                                                       |
| sqlite_synth               | 2.76 us                                                               | 2.73 us: 1.01x faster                                                      |
| scimark_fft                | 312 ms                                                                | 309 ms: 1.01x faster                                                       |
| coroutines                 | 23.6 ms                                                               | 23.4 ms: 1.01x faster                                                      |
| python_startup_no_site     | 7.09 ms                                                               | 7.05 ms: 1.01x faster                                                      |
| chaos                      | 58.8 ms                                                               | 58.6 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                     |
| python_startup             | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                      |
| pickle_list                | 5.09 us                                                               | 5.07 us: 1.00x faster                                                      |
| float                      | 69.9 ms                                                               | 69.7 ms: 1.00x faster                                                      |
| pidigits                   | 186 ms                                                                | 185 ms: 1.00x faster                                                       |
| regex_v8                   | 24.6 ms                                                               | 24.7 ms: 1.00x slower                                                      |
| fannkuch                   | 373 ms                                                                | 374 ms: 1.00x slower                                                       |
| bench_thread_pool          | 837 us                                                                | 840 us: 1.00x slower                                                       |
| 2to3                       | 276 ms                                                                | 277 ms: 1.00x slower                                                       |
| sqlglot_transpile          | 1.69 ms                                                               | 1.70 ms: 1.00x slower                                                      |
| async_generators           | 451 ms                                                                | 453 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 98.2 ms                                                               | 98.8 ms: 1.01x slower                                                      |
| xml_etree_process          | 54.1 ms                                                               | 54.5 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 58.0 ms                                                               | 58.4 ms: 1.01x slower                                                      |
| bpe_tokeniser              | 4.45 sec                                                              | 4.49 sec: 1.01x slower                                                     |
| thrift                     | 781 us                                                                | 788 us: 1.01x slower                                                       |
| deltablue                  | 3.21 ms                                                               | 3.24 ms: 1.01x slower                                                      |
| scimark_sor                | 116 ms                                                                | 117 ms: 1.01x slower                                                       |
| raytrace                   | 276 ms                                                                | 279 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 215 us                                                                | 217 us: 1.01x slower                                                       |
| unpack_sequence            | 112 ns                                                                | 113 ns: 1.01x slower                                                       |
| sympy_sum                  | 172 ms                                                                | 174 ms: 1.01x slower                                                       |
| meteor_contest             | 106 ms                                                                | 107 ms: 1.01x slower                                                       |
| logging_silent             | 104 ns                                                                | 105 ns: 1.01x slower                                                       |
| sympy_integrate            | 22.8 ms                                                               | 23.1 ms: 1.01x slower                                                      |
| genshi_text                | 25.5 ms                                                               | 25.8 ms: 1.01x slower                                                      |
| logging_format             | 6.10 us                                                               | 6.18 us: 1.01x slower                                                      |
| dulwich_log                | 67.6 ms                                                               | 68.5 ms: 1.01x slower                                                      |
| regex_compile              | 142 ms                                                                | 144 ms: 1.02x slower                                                       |
| pickle                     | 11.4 us                                                               | 11.6 us: 1.02x slower                                                      |
| logging_simple             | 5.57 us                                                               | 5.67 us: 1.02x slower                                                      |
| go                         | 130 ms                                                                | 133 ms: 1.02x slower                                                       |
| typing_runtime_protocols   | 164 us                                                                | 167 us: 1.02x slower                                                       |
| deepcopy_memo              | 27.0 us                                                               | 27.5 us: 1.02x slower                                                      |
| sympy_expand               | 503 ms                                                                | 513 ms: 1.02x slower                                                       |
| sympy_str                  | 299 ms                                                                | 305 ms: 1.02x slower                                                       |
| mdp                        | 2.66 sec                                                              | 2.71 sec: 1.02x slower                                                     |
| nbody                      | 79.7 ms                                                               | 81.3 ms: 1.02x slower                                                      |
| scimark_lu                 | 109 ms                                                                | 111 ms: 1.02x slower                                                       |
| pickle_dict                | 34.1 us                                                               | 34.9 us: 1.02x slower                                                      |
| deepcopy                   | 263 us                                                                | 269 us: 1.02x slower                                                       |
| comprehensions             | 16.7 us                                                               | 17.1 us: 1.02x slower                                                      |
| genshi_xml                 | 59.6 ms                                                               | 61.2 ms: 1.03x slower                                                      |
| deepcopy_reduce            | 2.67 us                                                               | 2.74 us: 1.03x slower                                                      |
| pycparser                  | 1.16 sec                                                              | 1.19 sec: 1.03x slower                                                     |
| hexiom                     | 6.88 ms                                                               | 7.07 ms: 1.03x slower                                                      |
| coverage                   | 85.2 ms                                                               | 88.0 ms: 1.03x slower                                                      |
| richards_super             | 45.7 ms                                                               | 47.7 ms: 1.04x slower                                                      |
| pyflate                    | 448 ms                                                                | 470 ms: 1.05x slower                                                       |
| richards                   | 39.7 ms                                                               | 41.9 ms: 1.06x slower                                                      |
| nqueens                    | 83.9 ms                                                               | 88.8 ms: 1.06x slower                                                      |
| generators                 | 32.7 ms                                                               | 36.2 ms: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                               |

Benchmark hidden because not significant (28): async_tree_cpu_io_mixed, async_tree_memoization, spectral_norm, pprint_safe_repr, pprint_pformat, pickle_pure_python, telco, docutils, scimark_monte_carlo, asyncio_websockets, bench_mp_pool, json_loads, django_template, html5lib, scimark_sparse_mat_mult, tomli_loads, async_tree_none, json, crypto_pyaes, sqlglot_parse, xml_etree_generate, tornado_http, async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_none_tg, unpickle, pylint

# HPT report

- Reliability score: 99.23% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x