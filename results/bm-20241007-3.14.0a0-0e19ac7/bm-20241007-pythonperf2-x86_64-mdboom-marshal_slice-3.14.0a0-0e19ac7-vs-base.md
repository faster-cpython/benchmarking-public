# Results vs. base

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.004x faster
- HPT reliability: 99.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                      | 279 ms: 1.01x faster                                                 |
| docutils       | 2.88 sec                                                                    | 2.90 sec: 1.00x slower                                               |
| html5lib       | 70.4 ms                                                                     | 70.8 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 561 ms                                                                      | 546 ms: 1.03x faster                                                 |
| async_tree_memoization     | 403 ms                                                                      | 398 ms: 1.01x faster                                                 |
| async_generators           | 357 ms                                                                      | 353 ms: 1.01x faster                                                 |
| coroutines                 | 21.1 ms                                                                     | 20.9 ms: 1.01x faster                                                |
| asyncio_tcp                | 374 ms                                                                      | 376 ms: 1.01x slower                                                 |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                         |

Benchmark hidden because not significant (8): async_tree_io, async_tree_none_tg, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 90.6 ms                                                                     | 87.3 ms: 1.04x faster                                                |
| float          | 78.0 ms                                                                     | 78.8 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 140 ms                                                                      | 139 ms: 1.00x faster                                                 |
| regex_effbot   | 3.48 ms                                                                     | 3.50 ms: 1.01x slower                                                |
| regex_dna      | 248 ms                                                                      | 252 ms: 1.01x slower                                                 |
| regex_v8       | 26.2 ms                                                                     | 26.9 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|---------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse     | 150 ms                                                                      | 140 ms: 1.07x faster                                                 |
| xml_etree_iterparse | 102 ms                                                                      | 98.5 ms: 1.03x faster                                                |
| unpickle            | 15.4 us                                                                     | 15.1 us: 1.02x faster                                                |
| json_loads          | 25.0 us                                                                     | 24.6 us: 1.02x faster                                                |
| tomli_loads         | 2.56 sec                                                                    | 2.52 sec: 1.02x faster                                               |
| pickle_pure_python  | 312 us                                                                      | 310 us: 1.01x faster                                                 |
| xml_etree_generate  | 84.7 ms                                                                     | 85.1 ms: 1.01x slower                                                |
| xml_etree_process   | 59.2 ms                                                                     | 59.6 ms: 1.01x slower                                                |
| pickle_list         | 4.55 us                                                                     | 4.65 us: 1.02x slower                                                |
| pickle_dict         | 31.6 us                                                                     | 32.4 us: 1.03x slower                                                |
| pickle              | 10.4 us                                                                     | 10.7 us: 1.03x slower                                                |
| Geometric mean      | (ref)                                                                       | 1.01x faster                                                         |

Benchmark hidden because not significant (3): unpickle_list, unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.95 ms                                                                     | 9.01 ms: 1.01x slower                                                |
| python_startup         | 13.4 ms                                                                     | 13.5 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 40.6 ms                                                                     | 39.0 ms: 1.04x faster                                                |
| genshi_xml      | 54.2 ms                                                                     | 52.8 ms: 1.03x faster                                                |
| genshi_text     | 24.7 ms                                                                     | 24.2 ms: 1.02x faster                                                |
| mako            | 10.3 ms                                                                     | 10.4 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                                       | 1.02x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| scimark_sor                | 120 ms                                                                      | 111 ms: 1.08x faster                                                 |
| xml_etree_parse            | 150 ms                                                                      | 140 ms: 1.07x faster                                                 |
| unpack_sequence            | 55.3 ns                                                                     | 53.2 ns: 1.04x faster                                                |
| django_template            | 40.6 ms                                                                     | 39.0 ms: 1.04x faster                                                |
| nbody                      | 90.6 ms                                                                     | 87.3 ms: 1.04x faster                                                |
| xml_etree_iterparse        | 102 ms                                                                      | 98.5 ms: 1.03x faster                                                |
| scimark_monte_carlo        | 65.9 ms                                                                     | 63.8 ms: 1.03x faster                                                |
| telco                      | 8.20 ms                                                                     | 7.96 ms: 1.03x faster                                                |
| json                       | 5.34 ms                                                                     | 5.19 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed_tg | 561 ms                                                                      | 546 ms: 1.03x faster                                                 |
| genshi_xml                 | 54.2 ms                                                                     | 52.8 ms: 1.03x faster                                                |
| bpe_tokeniser              | 4.95 sec                                                                    | 4.82 sec: 1.03x faster                                               |
| pprint_pformat             | 1.67 sec                                                                    | 1.63 sec: 1.02x faster                                               |
| generators                 | 28.8 ms                                                                     | 28.1 ms: 1.02x faster                                                |
| pprint_safe_repr           | 814 ms                                                                      | 797 ms: 1.02x faster                                                 |
| genshi_text                | 24.7 ms                                                                     | 24.2 ms: 1.02x faster                                                |
| scimark_fft                | 290 ms                                                                      | 284 ms: 1.02x faster                                                 |
| unpickle                   | 15.4 us                                                                     | 15.1 us: 1.02x faster                                                |
| json_loads                 | 25.0 us                                                                     | 24.6 us: 1.02x faster                                                |
| tomli_loads                | 2.56 sec                                                                    | 2.52 sec: 1.02x faster                                               |
| meteor_contest             | 126 ms                                                                      | 125 ms: 1.01x faster                                                 |
| raytrace                   | 269 ms                                                                      | 266 ms: 1.01x faster                                                 |
| async_tree_memoization     | 403 ms                                                                      | 398 ms: 1.01x faster                                                 |
| richards_super             | 56.4 ms                                                                     | 55.8 ms: 1.01x faster                                                |
| async_generators           | 357 ms                                                                      | 353 ms: 1.01x faster                                                 |
| 2to3                       | 282 ms                                                                      | 279 ms: 1.01x faster                                                 |
| coroutines                 | 21.1 ms                                                                     | 20.9 ms: 1.01x faster                                                |
| pycparser                  | 1.23 sec                                                                    | 1.22 sec: 1.01x faster                                               |
| deepcopy_reduce            | 2.92 us                                                                     | 2.89 us: 1.01x faster                                                |
| pickle_pure_python         | 312 us                                                                      | 310 us: 1.01x faster                                                 |
| scimark_lu                 | 93.7 ms                                                                     | 93.1 ms: 1.01x faster                                                |
| pathlib                    | 15.8 ms                                                                     | 15.7 ms: 1.01x faster                                                |
| pyflate                    | 490 ms                                                                      | 488 ms: 1.00x faster                                                 |
| regex_compile              | 140 ms                                                                      | 139 ms: 1.00x faster                                                 |
| hexiom                     | 6.19 ms                                                                     | 6.16 ms: 1.00x faster                                                |
| spectral_norm              | 97.2 ms                                                                     | 96.8 ms: 1.00x faster                                                |
| docutils                   | 2.88 sec                                                                    | 2.90 sec: 1.00x slower                                               |
| sqlglot_optimize           | 58.7 ms                                                                     | 59.0 ms: 1.01x slower                                                |
| xml_etree_generate         | 84.7 ms                                                                     | 85.1 ms: 1.01x slower                                                |
| crypto_pyaes               | 71.9 ms                                                                     | 72.3 ms: 1.01x slower                                                |
| html5lib                   | 70.4 ms                                                                     | 70.8 ms: 1.01x slower                                                |
| deepcopy_memo              | 28.8 us                                                                     | 29.0 us: 1.01x slower                                                |
| sympy_integrate            | 23.2 ms                                                                     | 23.3 ms: 1.01x slower                                                |
| asyncio_tcp                | 374 ms                                                                      | 376 ms: 1.01x slower                                                 |
| xml_etree_process          | 59.2 ms                                                                     | 59.6 ms: 1.01x slower                                                |
| python_startup_no_site     | 8.95 ms                                                                     | 9.01 ms: 1.01x slower                                                |
| regex_effbot               | 3.48 ms                                                                     | 3.50 ms: 1.01x slower                                                |
| logging_silent             | 98.6 ns                                                                     | 99.3 ns: 1.01x slower                                                |
| comprehensions             | 17.2 us                                                                     | 17.3 us: 1.01x slower                                                |
| mako                       | 10.3 ms                                                                     | 10.4 ms: 1.01x slower                                                |
| sympy_str                  | 289 ms                                                                      | 291 ms: 1.01x slower                                                 |
| python_startup             | 13.4 ms                                                                     | 13.5 ms: 1.01x slower                                                |
| go                         | 132 ms                                                                      | 133 ms: 1.01x slower                                                 |
| dulwich_log                | 66.1 ms                                                                     | 66.7 ms: 1.01x slower                                                |
| deepcopy                   | 282 us                                                                      | 285 us: 1.01x slower                                                 |
| float                      | 78.0 ms                                                                     | 78.8 ms: 1.01x slower                                                |
| richards                   | 50.2 ms                                                                     | 50.8 ms: 1.01x slower                                                |
| deltablue                  | 3.34 ms                                                                     | 3.38 ms: 1.01x slower                                                |
| mdp                        | 2.46 sec                                                                    | 2.50 sec: 1.01x slower                                               |
| thrift                     | 852 us                                                                      | 864 us: 1.01x slower                                                 |
| regex_dna                  | 248 ms                                                                      | 252 ms: 1.01x slower                                                 |
| gc_traversal               | 4.45 ms                                                                     | 4.53 ms: 1.02x slower                                                |
| sympy_expand               | 488 ms                                                                      | 497 ms: 1.02x slower                                                 |
| fannkuch                   | 352 ms                                                                      | 359 ms: 1.02x slower                                                 |
| coverage                   | 82.0 ms                                                                     | 83.6 ms: 1.02x slower                                                |
| pickle_list                | 4.55 us                                                                     | 4.65 us: 1.02x slower                                                |
| create_gc_cycles           | 1.97 ms                                                                     | 2.02 ms: 1.02x slower                                                |
| logging_format             | 6.74 us                                                                     | 6.89 us: 1.02x slower                                                |
| pickle_dict                | 31.6 us                                                                     | 32.4 us: 1.03x slower                                                |
| regex_v8                   | 26.2 ms                                                                     | 26.9 ms: 1.03x slower                                                |
| pickle                     | 10.4 us                                                                     | 10.7 us: 1.03x slower                                                |
| Geometric mean             | (ref)                                                                       | 1.00x faster                                                         |

Benchmark hidden because not significant (26): async_tree_io, scimark_sparse_mat_mult, async_tree_none_tg, bench_thread_pool, async_tree_io_tg, asyncio_websockets, unpickle_list, async_tree_cpu_io_mixed, async_tree_none, tornado_http, unpickle_pure_python, pidigits, async_tree_memoization_tg, sqlglot_transpile, nqueens, json_dumps, asyncio_tcp_ssl, sqlite_synth, typing_runtime_protocols, pylint, sqlglot_normalize, chaos, logging_simple, sympy_sum, sqlglot_parse, bench_mp_pool

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 99.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x