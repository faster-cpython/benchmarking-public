# Results vs. base

- fork: savannahostrowski
- ref: jit_inv_mem_100k
- machine: linux-x86_64
- commit hash: 17ece50
- commit date: 2024-09-23
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 280 ms: 1.02x slower                                                         |
| docutils       | 2.96 sec                                                              | 2.93 sec: 1.01x faster                                                       |
| html5lib       | 65.1 ms                                                               | 65.8 ms: 1.01x slower                                                        |
| tornado_http   | 94.4 ms                                                               | 94.9 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines             | 23.6 ms                                                               | 23.1 ms: 1.02x faster                                                        |
| asyncio_tcp            | 497 ms                                                                | 495 ms: 1.01x faster                                                         |
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                       |
| async_generators       | 451 ms                                                                | 457 ms: 1.01x slower                                                         |
| async_tree_memoization | 399 ms                                                                | 409 ms: 1.02x slower                                                         |
| async_tree_io          | 856 ms                                                                | 886 ms: 1.03x slower                                                         |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                 |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                                         |
| nbody          | 79.7 ms                                                               | 80.6 ms: 1.01x slower                                                        |
| float          | 69.9 ms                                                               | 71.1 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.82 ms                                                               | 3.65 ms: 1.05x faster                                                        |
| regex_dna      | 224 ms                                                                | 221 ms: 1.02x faster                                                         |
| regex_compile  | 142 ms                                                                | 144 ms: 1.02x slower                                                         |
| regex_v8       | 24.6 ms                                                               | 25.4 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_list        | 5.40 us                                                               | 5.15 us: 1.05x faster                                                        |
| tomli_loads          | 1.95 sec                                                              | 1.92 sec: 1.01x faster                                                       |
| json_dumps           | 10.1 ms                                                               | 10.0 ms: 1.01x faster                                                        |
| xml_etree_generate   | 77.8 ms                                                               | 78.2 ms: 1.01x slower                                                        |
| xml_etree_iterparse  | 98.2 ms                                                               | 98.8 ms: 1.01x slower                                                        |
| json_loads           | 26.9 us                                                               | 27.2 us: 1.01x slower                                                        |
| pickle_list          | 5.09 us                                                               | 5.15 us: 1.01x slower                                                        |
| xml_etree_parse      | 146 ms                                                                | 148 ms: 1.01x slower                                                         |
| pickle_dict          | 34.1 us                                                               | 34.9 us: 1.02x slower                                                        |
| unpickle_pure_python | 215 us                                                                | 221 us: 1.03x slower                                                         |
| xml_etree_process    | 54.1 ms                                                               | 55.6 ms: 1.03x slower                                                        |
| pickle               | 11.4 us                                                               | 11.9 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                        |
| python_startup_no_site | 7.09 ms                                                               | 7.07 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 10.0 ms                                                               | 9.75 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark               | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal            | 3.90 ms                                                               | 3.68 ms: 1.06x faster                                                        |
| mdp                     | 2.66 sec                                                              | 2.54 sec: 1.05x faster                                                       |
| regex_effbot            | 3.82 ms                                                               | 3.65 ms: 1.05x faster                                                        |
| unpickle_list           | 5.40 us                                                               | 5.15 us: 1.05x faster                                                        |
| unpack_sequence         | 112 ns                                                                | 107 ns: 1.05x faster                                                         |
| mako                    | 10.0 ms                                                               | 9.75 ms: 1.03x faster                                                        |
| create_gc_cycles        | 1.76 ms                                                               | 1.72 ms: 1.03x faster                                                        |
| coroutines              | 23.6 ms                                                               | 23.1 ms: 1.02x faster                                                        |
| pathlib                 | 16.2 ms                                                               | 15.9 ms: 1.02x faster                                                        |
| regex_dna               | 224 ms                                                                | 221 ms: 1.02x faster                                                         |
| tomli_loads             | 1.95 sec                                                              | 1.92 sec: 1.01x faster                                                       |
| docutils                | 2.96 sec                                                              | 2.93 sec: 1.01x faster                                                       |
| json_dumps              | 10.1 ms                                                               | 10.0 ms: 1.01x faster                                                        |
| deepcopy_reduce         | 2.67 us                                                               | 2.64 us: 1.01x faster                                                        |
| asyncio_tcp             | 497 ms                                                                | 495 ms: 1.01x faster                                                         |
| python_startup          | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                        |
| python_startup_no_site  | 7.09 ms                                                               | 7.07 ms: 1.00x faster                                                        |
| scimark_sparse_mat_mult | 4.39 ms                                                               | 4.38 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                       |
| pidigits                | 186 ms                                                                | 186 ms: 1.00x slower                                                         |
| deepcopy_memo           | 27.0 us                                                               | 27.1 us: 1.00x slower                                                        |
| xml_etree_generate      | 77.8 ms                                                               | 78.2 ms: 1.01x slower                                                        |
| tornado_http            | 94.4 ms                                                               | 94.9 ms: 1.01x slower                                                        |
| xml_etree_iterparse     | 98.2 ms                                                               | 98.8 ms: 1.01x slower                                                        |
| richards_super          | 45.7 ms                                                               | 46.0 ms: 1.01x slower                                                        |
| sqlglot_normalize       | 113 ms                                                                | 114 ms: 1.01x slower                                                         |
| thrift                  | 781 us                                                                | 786 us: 1.01x slower                                                         |
| scimark_sor             | 116 ms                                                                | 117 ms: 1.01x slower                                                         |
| sympy_expand            | 503 ms                                                                | 507 ms: 1.01x slower                                                         |
| crypto_pyaes            | 66.2 ms                                                               | 66.7 ms: 1.01x slower                                                        |
| html5lib                | 65.1 ms                                                               | 65.8 ms: 1.01x slower                                                        |
| go                      | 130 ms                                                                | 132 ms: 1.01x slower                                                         |
| nbody                   | 79.7 ms                                                               | 80.6 ms: 1.01x slower                                                        |
| bpe_tokeniser           | 4.45 sec                                                              | 4.50 sec: 1.01x slower                                                       |
| json_loads              | 26.9 us                                                               | 27.2 us: 1.01x slower                                                        |
| pickle_list             | 5.09 us                                                               | 5.15 us: 1.01x slower                                                        |
| dulwich_log             | 67.6 ms                                                               | 68.5 ms: 1.01x slower                                                        |
| comprehensions          | 16.7 us                                                               | 16.9 us: 1.01x slower                                                        |
| async_generators        | 451 ms                                                                | 457 ms: 1.01x slower                                                         |
| chaos                   | 58.8 ms                                                               | 59.6 ms: 1.01x slower                                                        |
| fannkuch                | 373 ms                                                                | 378 ms: 1.01x slower                                                         |
| xml_etree_parse         | 146 ms                                                                | 148 ms: 1.01x slower                                                         |
| 2to3                    | 276 ms                                                                | 280 ms: 1.02x slower                                                         |
| scimark_fft             | 312 ms                                                                | 317 ms: 1.02x slower                                                         |
| regex_compile           | 142 ms                                                                | 144 ms: 1.02x slower                                                         |
| json                    | 5.02 ms                                                               | 5.10 ms: 1.02x slower                                                        |
| sympy_integrate         | 22.8 ms                                                               | 23.1 ms: 1.02x slower                                                        |
| sympy_sum               | 172 ms                                                                | 176 ms: 1.02x slower                                                         |
| sympy_str               | 299 ms                                                                | 305 ms: 1.02x slower                                                         |
| float                   | 69.9 ms                                                               | 71.1 ms: 1.02x slower                                                        |
| meteor_contest          | 106 ms                                                                | 108 ms: 1.02x slower                                                         |
| logging_format          | 6.10 us                                                               | 6.22 us: 1.02x slower                                                        |
| raytrace                | 276 ms                                                                | 281 ms: 1.02x slower                                                         |
| hexiom                  | 6.88 ms                                                               | 7.02 ms: 1.02x slower                                                        |
| logging_simple          | 5.57 us                                                               | 5.69 us: 1.02x slower                                                        |
| scimark_lu              | 109 ms                                                                | 111 ms: 1.02x slower                                                         |
| pyflate                 | 448 ms                                                                | 459 ms: 1.02x slower                                                         |
| pickle_dict             | 34.1 us                                                               | 34.9 us: 1.02x slower                                                        |
| async_tree_memoization  | 399 ms                                                                | 409 ms: 1.02x slower                                                         |
| unpickle_pure_python    | 215 us                                                                | 221 us: 1.03x slower                                                         |
| xml_etree_process       | 54.1 ms                                                               | 55.6 ms: 1.03x slower                                                        |
| richards                | 39.7 ms                                                               | 40.9 ms: 1.03x slower                                                        |
| regex_v8                | 24.6 ms                                                               | 25.4 ms: 1.03x slower                                                        |
| async_tree_io           | 856 ms                                                                | 886 ms: 1.03x slower                                                         |
| nqueens                 | 83.9 ms                                                               | 87.1 ms: 1.04x slower                                                        |
| pickle                  | 11.4 us                                                               | 11.9 us: 1.05x slower                                                        |
| sqlglot_optimize        | 58.0 ms                                                               | 60.7 ms: 1.05x slower                                                        |
| coverage                | 85.2 ms                                                               | 89.3 ms: 1.05x slower                                                        |
| pycparser               | 1.16 sec                                                              | 1.22 sec: 1.05x slower                                                       |
| generators              | 32.7 ms                                                               | 35.2 ms: 1.08x slower                                                        |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                                 |

Benchmark hidden because not significant (27): scimark_monte_carlo, async_tree_cpu_io_mixed_tg, genshi_xml, sqlite_synth, telco, pprint_pformat, pprint_safe_repr, asyncio_websockets, async_tree_cpu_io_mixed, bench_mp_pool, genshi_text, typing_runtime_protocols, sqlglot_parse, sqlglot_transpile, bench_thread_pool, deltablue, django_template, logging_silent, pickle_pure_python, async_tree_none, unpickle, deepcopy, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg, spectral_norm, pylint

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.97x