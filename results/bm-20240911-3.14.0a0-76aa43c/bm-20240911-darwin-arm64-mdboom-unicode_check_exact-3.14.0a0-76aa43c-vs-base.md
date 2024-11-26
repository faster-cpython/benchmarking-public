# Results vs. base

- fork: mdboom
- ref: unicode_check_exact
- machine: darwin-arm64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.000x slower
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 160 ms                                                                | 157 ms: 1.02x faster                                                 |
| docutils       | 1.43 sec                                                              | 1.41 sec: 1.01x faster                                               |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                         |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.28 sec                                                              | 1.27 sec: 1.01x faster                                               |
| async_generators           | 280 ms                                                                | 279 ms: 1.00x faster                                                 |
| async_tree_cpu_io_mixed_tg | 463 ms                                                                | 462 ms: 1.00x faster                                                 |
| coroutines                 | 16.0 ms                                                               | 16.0 ms: 1.00x faster                                                |
| async_tree_eager           | 60.7 ms                                                               | 60.9 ms: 1.00x slower                                                |
| async_tree_eager_tg        | 42.1 ms                                                               | 42.4 ms: 1.01x slower                                                |
| asyncio_tcp                | 412 ms                                                                | 434 ms: 1.05x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (14): async_tree_io, async_tree_none_tg, async_tree_none, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_eager_io, async_tree_memoization_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 282 ms                                                                | 282 ms: 1.00x faster                                                 |
| nbody          | 59.6 ms                                                               | 60.6 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 67.1 ms                                                               | 67.5 ms: 1.00x slower                                                |
| regex_v8       | 16.4 ms                                                               | 16.5 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 184 us                                                                | 182 us: 1.01x faster                                                 |
| unpickle_list        | 2.93 us                                                               | 2.90 us: 1.01x faster                                                |
| json_dumps           | 6.44 ms                                                               | 6.39 ms: 1.01x faster                                                |
| unpickle_pure_python | 141 us                                                                | 140 us: 1.01x faster                                                 |
| xml_etree_generate   | 53.1 ms                                                               | 53.0 ms: 1.00x faster                                                |
| xml_etree_process    | 37.2 ms                                                               | 37.5 ms: 1.01x slower                                                |
| pickle_list          | 2.95 us                                                               | 2.98 us: 1.01x slower                                                |
| xml_etree_parse      | 107 ms                                                                | 111 ms: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (6): tomli_loads, unpickle, xml_etree_iterparse, pickle, json_loads, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup | 16.8 ms                                                               | 16.9 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 19.7 ms                                                               | 19.7 ms: 1.00x faster                                                |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (3): genshi_xml, mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| richards_super             | 35.1 ms                                                               | 34.4 ms: 1.02x faster                                                |
| 2to3                       | 160 ms                                                                | 157 ms: 1.02x faster                                                 |
| deltablue                  | 2.14 ms                                                               | 2.11 ms: 1.02x faster                                                |
| docutils                   | 1.43 sec                                                              | 1.41 sec: 1.01x faster                                               |
| pickle_pure_python         | 184 us                                                                | 182 us: 1.01x faster                                                 |
| deepcopy                   | 145 us                                                                | 144 us: 1.01x faster                                                 |
| json                       | 2.97 ms                                                               | 2.94 ms: 1.01x faster                                                |
| deepcopy_memo              | 16.5 us                                                               | 16.3 us: 1.01x faster                                                |
| unpickle_list              | 2.93 us                                                               | 2.90 us: 1.01x faster                                                |
| logging_silent             | 60.6 ns                                                               | 60.0 ns: 1.01x faster                                                |
| deepcopy_reduce            | 1.52 us                                                               | 1.50 us: 1.01x faster                                                |
| pprint_pformat             | 933 ms                                                                | 924 ms: 1.01x faster                                                 |
| logging_format             | 3.37 us                                                               | 3.34 us: 1.01x faster                                                |
| asyncio_tcp_ssl            | 1.28 sec                                                              | 1.27 sec: 1.01x faster                                               |
| json_dumps                 | 6.44 ms                                                               | 6.39 ms: 1.01x faster                                                |
| bench_thread_pool          | 451 us                                                                | 448 us: 1.01x faster                                                 |
| sympy_str                  | 131 ms                                                                | 131 ms: 1.01x faster                                                 |
| unpickle_pure_python       | 141 us                                                                | 140 us: 1.01x faster                                                 |
| fannkuch                   | 262 ms                                                                | 260 ms: 1.01x faster                                                 |
| sympy_sum                  | 69.2 ms                                                               | 68.8 ms: 1.00x faster                                                |
| dulwich_log                | 27.2 ms                                                               | 27.1 ms: 1.00x faster                                                |
| sqlglot_parse              | 744 us                                                                | 741 us: 1.00x faster                                                 |
| sqlglot_normalize          | 168 ms                                                                | 167 ms: 1.00x faster                                                 |
| async_generators           | 280 ms                                                                | 279 ms: 1.00x faster                                                 |
| spectral_norm              | 66.9 ms                                                               | 66.7 ms: 1.00x faster                                                |
| async_tree_cpu_io_mixed_tg | 463 ms                                                                | 462 ms: 1.00x faster                                                 |
| thrift                     | 428 us                                                                | 426 us: 1.00x faster                                                 |
| xml_etree_generate         | 53.1 ms                                                               | 53.0 ms: 1.00x faster                                                |
| sqlite_synth               | 1.55 us                                                               | 1.55 us: 1.00x faster                                                |
| django_template            | 19.7 ms                                                               | 19.7 ms: 1.00x faster                                                |
| scimark_sor                | 92.8 ms                                                               | 92.6 ms: 1.00x faster                                                |
| coroutines                 | 16.0 ms                                                               | 16.0 ms: 1.00x faster                                                |
| bpe_tokeniser              | 3.14 sec                                                              | 3.13 sec: 1.00x faster                                               |
| pidigits                   | 282 ms                                                                | 282 ms: 1.00x faster                                                 |
| scimark_monte_carlo        | 43.1 ms                                                               | 43.2 ms: 1.00x slower                                                |
| crypto_pyaes               | 50.3 ms                                                               | 50.4 ms: 1.00x slower                                                |
| telco                      | 4.78 ms                                                               | 4.80 ms: 1.00x slower                                                |
| async_tree_eager           | 60.7 ms                                                               | 60.9 ms: 1.00x slower                                                |
| generators                 | 20.3 ms                                                               | 20.4 ms: 1.00x slower                                                |
| regex_compile              | 67.1 ms                                                               | 67.5 ms: 1.00x slower                                                |
| async_tree_eager_tg        | 42.1 ms                                                               | 42.4 ms: 1.01x slower                                                |
| xml_etree_process          | 37.2 ms                                                               | 37.5 ms: 1.01x slower                                                |
| regex_v8                   | 16.4 ms                                                               | 16.5 ms: 1.01x slower                                                |
| sqlglot_optimize           | 31.1 ms                                                               | 31.3 ms: 1.01x slower                                                |
| create_gc_cycles           | 892 us                                                                | 898 us: 1.01x slower                                                 |
| gc_traversal               | 2.45 ms                                                               | 2.47 ms: 1.01x slower                                                |
| scimark_sparse_mat_mult    | 2.78 ms                                                               | 2.80 ms: 1.01x slower                                                |
| python_startup             | 16.8 ms                                                               | 16.9 ms: 1.01x slower                                                |
| pickle_list                | 2.95 us                                                               | 2.98 us: 1.01x slower                                                |
| hexiom                     | 4.06 ms                                                               | 4.10 ms: 1.01x slower                                                |
| nbody                      | 59.6 ms                                                               | 60.6 ms: 1.02x slower                                                |
| scimark_lu                 | 66.6 ms                                                               | 68.0 ms: 1.02x slower                                                |
| chaos                      | 35.0 ms                                                               | 35.8 ms: 1.02x slower                                                |
| xml_etree_parse            | 107 ms                                                                | 111 ms: 1.04x slower                                                 |
| asyncio_tcp                | 412 ms                                                                | 434 ms: 1.05x slower                                                 |
| comprehensions             | 9.98 us                                                               | 10.6 us: 1.07x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (49): tornado_http, pycparser, async_tree_io, pylint, typing_runtime_protocols, regex_effbot, tomli_loads, genshi_xml, sqlglot_transpile, float, unpickle, xml_etree_iterparse, sympy_integrate, nqueens, mako, async_tree_none_tg, async_tree_none, raytrace, richards, mdp, pathlib, pickle, sympy_expand, regex_dna, async_tree_eager_cpu_io_mixed_tg, logging_simple, json_loads, async_tree_eager_cpu_io_mixed, async_tree_memoization, meteor_contest, coverage, pprint_safe_repr, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_eager_io, html5lib, pyflate, pickle_dict, async_tree_memoization_tg, async_tree_eager_memoization, go, scimark_fft, unpack_sequence, async_tree_eager_memoization_tg, genshi_text, async_tree_eager_io_tg, python_startup_no_site, bench_mp_pool, async_tree_io_tg

- Geometric mean (including insignificant results): 1.000x slower
# HPT report

- Reliability score: 99.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x