# Results vs. base

- fork: savannahostrowski
- ref: jit_inv_cold_10k
- machine: linux-x86_64
- commit hash: 14c70a7
- commit date: 2024-09-19
- overall geometric mean: 1.01x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 285 ms: 1.03x slower                                                         |
| docutils       | 2.96 sec                                                              | 2.88 sec: 1.03x faster                                                       |
| html5lib       | 65.1 ms                                                               | 63.9 ms: 1.02x faster                                                        |
| tornado_http   | 94.4 ms                                                               | 95.5 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 574 ms                                                                | 558 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 557 ms                                                                | 546 ms: 1.02x faster                                                         |
| asyncio_tcp                | 497 ms                                                                | 491 ms: 1.01x faster                                                         |
| coroutines                 | 23.6 ms                                                               | 23.4 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                       |
| async_generators           | 451 ms                                                                | 460 ms: 1.02x slower                                                         |
| async_tree_io              | 856 ms                                                                | 883 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                 |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization, asyncio_websockets, async_tree_memoization_tg, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                                         |
| float          | 69.9 ms                                                               | 71.5 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.82 ms                                                               | 3.65 ms: 1.05x faster                                                        |
| regex_dna      | 224 ms                                                                | 215 ms: 1.04x faster                                                         |
| regex_compile  | 142 ms                                                                | 139 ms: 1.02x faster                                                         |
| regex_v8       | 24.6 ms                                                               | 25.5 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 34.1 us                                                               | 33.4 us: 1.02x faster                                                        |
| pickle_list          | 5.09 us                                                               | 5.00 us: 1.02x faster                                                        |
| unpickle_list        | 5.40 us                                                               | 5.31 us: 1.02x faster                                                        |
| json_loads           | 26.9 us                                                               | 26.8 us: 1.00x faster                                                        |
| tomli_loads          | 1.95 sec                                                              | 1.96 sec: 1.01x slower                                                       |
| xml_etree_iterparse  | 98.2 ms                                                               | 99.4 ms: 1.01x slower                                                        |
| unpickle_pure_python | 215 us                                                                | 219 us: 1.02x slower                                                         |
| xml_etree_process    | 54.1 ms                                                               | 55.5 ms: 1.02x slower                                                        |
| xml_etree_generate   | 77.8 ms                                                               | 79.8 ms: 1.03x slower                                                        |
| pickle               | 11.4 us                                                               | 11.7 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                 |

Benchmark hidden because not significant (4): unpickle, xml_etree_parse, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                               | 7.04 ms: 1.01x faster                                                        |
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 36.1 ms                                                               | 35.4 ms: 1.02x faster                                                        |
| genshi_xml      | 59.6 ms                                                               | 61.0 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 3.90 ms                                                               | 3.71 ms: 1.05x faster                                                        |
| regex_effbot               | 3.82 ms                                                               | 3.65 ms: 1.05x faster                                                        |
| regex_dna                  | 224 ms                                                                | 215 ms: 1.04x faster                                                         |
| docutils                   | 2.96 sec                                                              | 2.88 sec: 1.03x faster                                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                                | 558 ms: 1.03x faster                                                         |
| unpack_sequence            | 112 ns                                                                | 109 ns: 1.03x faster                                                         |
| scimark_monte_carlo        | 63.5 ms                                                               | 61.9 ms: 1.03x faster                                                        |
| pickle_dict                | 34.1 us                                                               | 33.4 us: 1.02x faster                                                        |
| create_gc_cycles           | 1.76 ms                                                               | 1.72 ms: 1.02x faster                                                        |
| regex_compile              | 142 ms                                                                | 139 ms: 1.02x faster                                                         |
| django_template            | 36.1 ms                                                               | 35.4 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 557 ms                                                                | 546 ms: 1.02x faster                                                         |
| html5lib                   | 65.1 ms                                                               | 63.9 ms: 1.02x faster                                                        |
| pickle_list                | 5.09 us                                                               | 5.00 us: 1.02x faster                                                        |
| mdp                        | 2.66 sec                                                              | 2.62 sec: 1.02x faster                                                       |
| unpickle_list              | 5.40 us                                                               | 5.31 us: 1.02x faster                                                        |
| pprint_safe_repr           | 753 ms                                                                | 742 ms: 1.01x faster                                                         |
| deepcopy_reduce            | 2.67 us                                                               | 2.63 us: 1.01x faster                                                        |
| asyncio_tcp                | 497 ms                                                                | 491 ms: 1.01x faster                                                         |
| pprint_pformat             | 1.57 sec                                                              | 1.55 sec: 1.01x faster                                                       |
| coroutines                 | 23.6 ms                                                               | 23.4 ms: 1.01x faster                                                        |
| python_startup_no_site     | 7.09 ms                                                               | 7.04 ms: 1.01x faster                                                        |
| scimark_fft                | 312 ms                                                                | 309 ms: 1.01x faster                                                         |
| logging_silent             | 104 ns                                                                | 103 ns: 1.01x faster                                                         |
| python_startup             | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                        |
| json_loads                 | 26.9 us                                                               | 26.8 us: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                       |
| pidigits                   | 186 ms                                                                | 186 ms: 1.00x slower                                                         |
| deepcopy_memo              | 27.0 us                                                               | 27.1 us: 1.00x slower                                                        |
| sympy_expand               | 503 ms                                                                | 505 ms: 1.00x slower                                                         |
| comprehensions             | 16.7 us                                                               | 16.8 us: 1.00x slower                                                        |
| bench_thread_pool          | 837 us                                                                | 841 us: 1.00x slower                                                         |
| tomli_loads                | 1.95 sec                                                              | 1.96 sec: 1.01x slower                                                       |
| scimark_sor                | 116 ms                                                                | 117 ms: 1.01x slower                                                         |
| deepcopy                   | 263 us                                                                | 265 us: 1.01x slower                                                         |
| meteor_contest             | 106 ms                                                                | 107 ms: 1.01x slower                                                         |
| thrift                     | 781 us                                                                | 790 us: 1.01x slower                                                         |
| telco                      | 8.01 ms                                                               | 8.10 ms: 1.01x slower                                                        |
| tornado_http               | 94.4 ms                                                               | 95.5 ms: 1.01x slower                                                        |
| xml_etree_iterparse        | 98.2 ms                                                               | 99.4 ms: 1.01x slower                                                        |
| chaos                      | 58.8 ms                                                               | 59.6 ms: 1.01x slower                                                        |
| unpickle_pure_python       | 215 us                                                                | 219 us: 1.02x slower                                                         |
| logging_simple             | 5.57 us                                                               | 5.67 us: 1.02x slower                                                        |
| pyflate                    | 448 ms                                                                | 456 ms: 1.02x slower                                                         |
| dulwich_log                | 67.6 ms                                                               | 68.9 ms: 1.02x slower                                                        |
| async_generators           | 451 ms                                                                | 460 ms: 1.02x slower                                                         |
| raytrace                   | 276 ms                                                                | 281 ms: 1.02x slower                                                         |
| sympy_str                  | 299 ms                                                                | 306 ms: 1.02x slower                                                         |
| genshi_xml                 | 59.6 ms                                                               | 61.0 ms: 1.02x slower                                                        |
| float                      | 69.9 ms                                                               | 71.5 ms: 1.02x slower                                                        |
| xml_etree_process          | 54.1 ms                                                               | 55.5 ms: 1.02x slower                                                        |
| pycparser                  | 1.16 sec                                                              | 1.19 sec: 1.02x slower                                                       |
| sqlglot_normalize          | 113 ms                                                                | 116 ms: 1.03x slower                                                         |
| xml_etree_generate         | 77.8 ms                                                               | 79.8 ms: 1.03x slower                                                        |
| pickle                     | 11.4 us                                                               | 11.7 us: 1.03x slower                                                        |
| richards_super             | 45.7 ms                                                               | 47.0 ms: 1.03x slower                                                        |
| logging_format             | 6.10 us                                                               | 6.28 us: 1.03x slower                                                        |
| 2to3                       | 276 ms                                                                | 285 ms: 1.03x slower                                                         |
| crypto_pyaes               | 66.2 ms                                                               | 68.2 ms: 1.03x slower                                                        |
| async_tree_io              | 856 ms                                                                | 883 ms: 1.03x slower                                                         |
| fannkuch                   | 373 ms                                                                | 386 ms: 1.04x slower                                                         |
| regex_v8                   | 24.6 ms                                                               | 25.5 ms: 1.04x slower                                                        |
| scimark_sparse_mat_mult    | 4.39 ms                                                               | 4.56 ms: 1.04x slower                                                        |
| go                         | 130 ms                                                                | 137 ms: 1.05x slower                                                         |
| nqueens                    | 83.9 ms                                                               | 88.1 ms: 1.05x slower                                                        |
| scimark_lu                 | 109 ms                                                                | 115 ms: 1.06x slower                                                         |
| bpe_tokeniser              | 4.45 sec                                                              | 4.88 sec: 1.10x slower                                                       |
| richards                   | 39.7 ms                                                               | 43.5 ms: 1.10x slower                                                        |
| sqlglot_optimize           | 58.0 ms                                                               | 63.7 ms: 1.10x slower                                                        |
| spectral_norm              | 102 ms                                                                | 113 ms: 1.10x slower                                                         |
| generators                 | 32.7 ms                                                               | 36.2 ms: 1.11x slower                                                        |
| deltablue                  | 3.21 ms                                                               | 3.68 ms: 1.15x slower                                                        |
| hexiom                     | 6.88 ms                                                               | 7.89 ms: 1.15x slower                                                        |
| sympy_integrate            | 22.8 ms                                                               | 26.5 ms: 1.16x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                                 |

Benchmark hidden because not significant (23): async_tree_none_tg, async_tree_memoization, unpickle, xml_etree_parse, sqlite_synth, pickle_pure_python, sqlglot_parse, json_dumps, bench_mp_pool, asyncio_websockets, pathlib, sqlglot_transpile, json, nbody, async_tree_memoization_tg, sympy_sum, mako, genshi_text, coverage, typing_runtime_protocols, async_tree_io_tg, async_tree_none, pylint

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.97x