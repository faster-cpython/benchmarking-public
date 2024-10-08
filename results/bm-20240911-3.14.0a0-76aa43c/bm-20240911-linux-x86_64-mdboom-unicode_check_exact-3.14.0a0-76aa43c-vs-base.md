# Results vs. base

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-x86_64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.00x slower
- HPT reliability: 89.44%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                | 255 ms: 1.00x slower                                                 |
| docutils       | 2.64 sec                                                              | 2.66 sec: 1.00x slower                                               |
| html5lib       | 63.4 ms                                                               | 63.0 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_generators   | 433 ms                                                                | 427 ms: 1.01x faster                                                 |
| asyncio_websockets | 558 ms                                                                | 554 ms: 1.01x faster                                                 |
| asyncio_tcp        | 477 ms                                                                | 475 ms: 1.00x faster                                                 |
| coroutines         | 23.1 ms                                                               | 23.6 ms: 1.02x slower                                                |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (9): async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_cpu_io_mixed, asyncio_tcp_ssl, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 187 ms: 1.00x slower                                                 |
| nbody          | 88.5 ms                                                               | 89.4 ms: 1.01x slower                                                |
| float          | 76.7 ms                                                               | 77.7 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.80 ms                                                               | 3.53 ms: 1.08x faster                                                |
| regex_dna      | 223 ms                                                                | 217 ms: 1.03x faster                                                 |
| regex_compile  | 129 ms                                                                | 130 ms: 1.00x slower                                                 |
| regex_v8       | 24.0 ms                                                               | 24.8 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 157 ms                                                                | 154 ms: 1.02x faster                                                 |
| json_loads           | 27.1 us                                                               | 26.7 us: 1.02x faster                                                |
| xml_etree_iterparse  | 105 ms                                                                | 104 ms: 1.01x faster                                                 |
| unpickle_pure_python | 215 us                                                                | 213 us: 1.01x faster                                                 |
| pickle_list          | 5.11 us                                                               | 5.06 us: 1.01x faster                                                |
| pickle_pure_python   | 302 us                                                                | 301 us: 1.00x faster                                                 |
| xml_etree_generate   | 85.0 ms                                                               | 85.6 ms: 1.01x slower                                                |
| xml_etree_process    | 58.5 ms                                                               | 59.3 ms: 1.01x slower                                                |
| pickle_dict          | 34.4 us                                                               | 34.9 us: 1.01x slower                                                |
| json_dumps           | 10.2 ms                                                               | 10.4 ms: 1.02x slower                                                |
| unpickle_list        | 5.26 us                                                               | 5.44 us: 1.03x slower                                                |
| unpickle             | 14.8 us                                                               | 15.6 us: 1.05x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (2): tomli_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                |
| python_startup_no_site | 6.99 ms                                                               | 6.97 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                               | 11.2 ms: 1.00x slower                                                |
| django_template | 34.2 ms                                                               | 34.8 ms: 1.02x slower                                                |
| genshi_xml      | 51.2 ms                                                               | 52.2 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                         |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot             | 3.80 ms                                                               | 3.53 ms: 1.08x faster                                                |
| gc_traversal             | 3.84 ms                                                               | 3.66 ms: 1.05x faster                                                |
| unpack_sequence          | 52.0 ns                                                               | 50.5 ns: 1.03x faster                                                |
| regex_dna                | 223 ms                                                                | 217 ms: 1.03x faster                                                 |
| json                     | 5.04 ms                                                               | 4.92 ms: 1.02x faster                                                |
| xml_etree_parse          | 157 ms                                                                | 154 ms: 1.02x faster                                                 |
| json_loads               | 27.1 us                                                               | 26.7 us: 1.02x faster                                                |
| async_generators         | 433 ms                                                                | 427 ms: 1.01x faster                                                 |
| xml_etree_iterparse      | 105 ms                                                                | 104 ms: 1.01x faster                                                 |
| unpickle_pure_python     | 215 us                                                                | 213 us: 1.01x faster                                                 |
| pickle_list              | 5.11 us                                                               | 5.06 us: 1.01x faster                                                |
| typing_runtime_protocols | 162 us                                                                | 161 us: 1.01x faster                                                 |
| html5lib                 | 63.4 ms                                                               | 63.0 ms: 1.01x faster                                                |
| deepcopy                 | 262 us                                                                | 261 us: 1.01x faster                                                 |
| asyncio_websockets       | 558 ms                                                                | 554 ms: 1.01x faster                                                 |
| pprint_pformat           | 1.48 sec                                                              | 1.47 sec: 1.01x faster                                               |
| asyncio_tcp              | 477 ms                                                                | 475 ms: 1.00x faster                                                 |
| create_gc_cycles         | 1.72 ms                                                               | 1.71 ms: 1.00x faster                                                |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                |
| pickle_pure_python       | 302 us                                                                | 301 us: 1.00x faster                                                 |
| python_startup_no_site   | 6.99 ms                                                               | 6.97 ms: 1.00x faster                                                |
| mako                     | 11.1 ms                                                               | 11.2 ms: 1.00x slower                                                |
| pidigits                 | 186 ms                                                                | 187 ms: 1.00x slower                                                 |
| sqlglot_transpile        | 1.58 ms                                                               | 1.58 ms: 1.00x slower                                                |
| sqlglot_normalize        | 108 ms                                                                | 109 ms: 1.00x slower                                                 |
| pyflate                  | 472 ms                                                                | 474 ms: 1.00x slower                                                 |
| dulwich_log              | 64.2 ms                                                               | 64.5 ms: 1.00x slower                                                |
| docutils                 | 2.64 sec                                                              | 2.66 sec: 1.00x slower                                               |
| comprehensions           | 16.3 us                                                               | 16.4 us: 1.00x slower                                                |
| sqlglot_optimize         | 53.4 ms                                                               | 53.7 ms: 1.00x slower                                                |
| regex_compile            | 129 ms                                                                | 130 ms: 1.00x slower                                                 |
| 2to3                     | 253 ms                                                                | 255 ms: 1.00x slower                                                 |
| spectral_norm            | 112 ms                                                                | 112 ms: 1.01x slower                                                 |
| raytrace                 | 258 ms                                                                | 259 ms: 1.01x slower                                                 |
| richards_super           | 51.6 ms                                                               | 51.9 ms: 1.01x slower                                                |
| xml_etree_generate       | 85.0 ms                                                               | 85.6 ms: 1.01x slower                                                |
| thrift                   | 764 us                                                                | 770 us: 1.01x slower                                                 |
| scimark_monte_carlo      | 67.3 ms                                                               | 67.8 ms: 1.01x slower                                                |
| richards                 | 45.7 ms                                                               | 46.0 ms: 1.01x slower                                                |
| nbody                    | 88.5 ms                                                               | 89.4 ms: 1.01x slower                                                |
| chaos                    | 58.2 ms                                                               | 58.9 ms: 1.01x slower                                                |
| fannkuch                 | 398 ms                                                                | 403 ms: 1.01x slower                                                 |
| xml_etree_process        | 58.5 ms                                                               | 59.3 ms: 1.01x slower                                                |
| pickle_dict              | 34.4 us                                                               | 34.9 us: 1.01x slower                                                |
| float                    | 76.7 ms                                                               | 77.7 ms: 1.01x slower                                                |
| crypto_pyaes             | 70.8 ms                                                               | 71.8 ms: 1.01x slower                                                |
| django_template          | 34.2 ms                                                               | 34.8 ms: 1.02x slower                                                |
| go                       | 116 ms                                                                | 117 ms: 1.02x slower                                                 |
| genshi_xml               | 51.2 ms                                                               | 52.2 ms: 1.02x slower                                                |
| scimark_lu               | 112 ms                                                                | 114 ms: 1.02x slower                                                 |
| coroutines               | 23.1 ms                                                               | 23.6 ms: 1.02x slower                                                |
| deepcopy_memo            | 30.2 us                                                               | 30.8 us: 1.02x slower                                                |
| scimark_sor              | 124 ms                                                                | 127 ms: 1.02x slower                                                 |
| json_dumps               | 10.2 ms                                                               | 10.4 ms: 1.02x slower                                                |
| coverage                 | 84.3 ms                                                               | 86.5 ms: 1.03x slower                                                |
| hexiom                   | 6.06 ms                                                               | 6.22 ms: 1.03x slower                                                |
| logging_simple           | 5.58 us                                                               | 5.74 us: 1.03x slower                                                |
| logging_silent           | 97.6 ns                                                               | 100 ns: 1.03x slower                                                 |
| mdp                      | 2.51 sec                                                              | 2.58 sec: 1.03x slower                                               |
| regex_v8                 | 24.0 ms                                                               | 24.8 ms: 1.03x slower                                                |
| unpickle_list            | 5.26 us                                                               | 5.44 us: 1.03x slower                                                |
| scimark_sparse_mat_mult  | 4.81 ms                                                               | 4.98 ms: 1.04x slower                                                |
| scimark_fft              | 356 ms                                                                | 371 ms: 1.04x slower                                                 |
| logging_format           | 6.13 us                                                               | 6.38 us: 1.04x slower                                                |
| unpickle                 | 14.8 us                                                               | 15.6 us: 1.05x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (32): async_tree_io, sympy_str, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, generators, telco, async_tree_cpu_io_mixed_tg, sympy_expand, tomli_loads, genshi_text, pycparser, sympy_sum, async_tree_none, pickle, bench_mp_pool, async_tree_cpu_io_mixed, asyncio_tcp_ssl, async_tree_memoization, bench_thread_pool, pathlib, deepcopy_reduce, sqlglot_parse, sympy_integrate, meteor_contest, deltablue, tornado_http, pprint_safe_repr, nqueens, bpe_tokeniser, sqlite_synth, pylint

# HPT report

- Reliability score: 89.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x