# Results vs. base

- fork: faster-cpython
- ref: refactor_refcnt_mort
- machine: linux-x86_64
- commit hash: 2fbc12f
- commit date: 2024-10-10
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                | 256 ms: 1.02x slower                                                            |
| docutils       | 2.62 sec                                                              | 2.65 sec: 1.01x slower                                                          |
| html5lib       | 61.3 ms                                                               | 62.6 ms: 1.02x slower                                                           |
| tornado_http   | 90.4 ms                                                               | 91.3 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io    | 939 ms                                                                | 930 ms: 1.01x faster                                                            |
| async_generators | 432 ms                                                                | 438 ms: 1.01x slower                                                            |
| asyncio_tcp      | 471 ms                                                                | 479 ms: 1.02x slower                                                            |
| coroutines       | 23.4 ms                                                               | 24.2 ms: 1.03x slower                                                           |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 189 ms: 1.01x slower                                                            |
| float          | 77.2 ms                                                               | 79.1 ms: 1.03x slower                                                           |
| nbody          | 86.0 ms                                                               | 93.0 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.65 ms                                                               | 3.57 ms: 1.02x faster                                                           |
| regex_v8       | 24.8 ms                                                               | 24.4 ms: 1.01x faster                                                           |
| regex_dna      | 218 ms                                                                | 217 ms: 1.01x faster                                                            |
| regex_compile  | 128 ms                                                                | 130 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_list          | 5.13 us                                                               | 5.01 us: 1.02x faster                                                           |
| pickle_dict          | 34.7 us                                                               | 34.0 us: 1.02x faster                                                           |
| pickle               | 11.8 us                                                               | 11.7 us: 1.01x faster                                                           |
| xml_etree_iterparse  | 104 ms                                                                | 105 ms: 1.01x slower                                                            |
| xml_etree_generate   | 86.2 ms                                                               | 87.8 ms: 1.02x slower                                                           |
| pickle_pure_python   | 307 us                                                                | 315 us: 1.03x slower                                                            |
| xml_etree_process    | 59.1 ms                                                               | 60.7 ms: 1.03x slower                                                           |
| unpickle_pure_python | 215 us                                                                | 224 us: 1.05x slower                                                            |
| tomli_loads          | 2.08 sec                                                              | 2.17 sec: 1.05x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (5): unpickle, json_dumps, unpickle_list, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.03 ms                                                               | 7.06 ms: 1.00x slower                                                           |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.5 ms                                                               | 35.0 ms: 1.01x slower                                                           |
| mako            | 11.3 ms                                                               | 11.6 ms: 1.03x slower                                                           |
| genshi_xml      | 49.3 ms                                                               | 51.8 ms: 1.05x slower                                                           |
| genshi_text     | 21.8 ms                                                               | 23.5 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.04x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json                     | 5.04 ms                                                               | 4.85 ms: 1.04x faster                                                           |
| pickle_list              | 5.13 us                                                               | 5.01 us: 1.02x faster                                                           |
| regex_effbot             | 3.65 ms                                                               | 3.57 ms: 1.02x faster                                                           |
| pickle_dict              | 34.7 us                                                               | 34.0 us: 1.02x faster                                                           |
| regex_v8                 | 24.8 ms                                                               | 24.4 ms: 1.01x faster                                                           |
| pickle                   | 11.8 us                                                               | 11.7 us: 1.01x faster                                                           |
| async_tree_io            | 939 ms                                                                | 930 ms: 1.01x faster                                                            |
| regex_dna                | 218 ms                                                                | 217 ms: 1.01x faster                                                            |
| create_gc_cycles         | 1.79 ms                                                               | 1.78 ms: 1.01x faster                                                           |
| nqueens                  | 80.0 ms                                                               | 80.3 ms: 1.00x slower                                                           |
| python_startup_no_site   | 7.03 ms                                                               | 7.06 ms: 1.00x slower                                                           |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                           |
| mdp                      | 2.50 sec                                                              | 2.52 sec: 1.01x slower                                                          |
| pidigits                 | 187 ms                                                                | 189 ms: 1.01x slower                                                            |
| telco                    | 7.96 ms                                                               | 8.02 ms: 1.01x slower                                                           |
| tornado_http             | 90.4 ms                                                               | 91.3 ms: 1.01x slower                                                           |
| pathlib                  | 15.9 ms                                                               | 16.1 ms: 1.01x slower                                                           |
| xml_etree_iterparse      | 104 ms                                                                | 105 ms: 1.01x slower                                                            |
| docutils                 | 2.62 sec                                                              | 2.65 sec: 1.01x slower                                                          |
| thrift                   | 774 us                                                                | 783 us: 1.01x slower                                                            |
| bench_thread_pool        | 840 us                                                                | 850 us: 1.01x slower                                                            |
| django_template          | 34.5 ms                                                               | 35.0 ms: 1.01x slower                                                           |
| async_generators         | 432 ms                                                                | 438 ms: 1.01x slower                                                            |
| sympy_sum                | 147 ms                                                                | 149 ms: 1.01x slower                                                            |
| sympy_integrate          | 19.8 ms                                                               | 20.1 ms: 1.01x slower                                                           |
| 2to3                     | 252 ms                                                                | 256 ms: 1.02x slower                                                            |
| pyflate                  | 476 ms                                                                | 483 ms: 1.02x slower                                                            |
| pprint_pformat           | 1.49 sec                                                              | 1.52 sec: 1.02x slower                                                          |
| dulwich_log              | 64.3 ms                                                               | 65.4 ms: 1.02x slower                                                           |
| sqlglot_parse            | 1.29 ms                                                               | 1.31 ms: 1.02x slower                                                           |
| sqlglot_transpile        | 1.59 ms                                                               | 1.61 ms: 1.02x slower                                                           |
| typing_runtime_protocols | 161 us                                                                | 163 us: 1.02x slower                                                            |
| regex_compile            | 128 ms                                                                | 130 ms: 1.02x slower                                                            |
| asyncio_tcp              | 471 ms                                                                | 479 ms: 1.02x slower                                                            |
| fannkuch                 | 406 ms                                                                | 413 ms: 1.02x slower                                                            |
| chaos                    | 60.1 ms                                                               | 61.2 ms: 1.02x slower                                                           |
| sympy_str                | 267 ms                                                                | 272 ms: 1.02x slower                                                            |
| bpe_tokeniser            | 4.71 sec                                                              | 4.79 sec: 1.02x slower                                                          |
| xml_etree_generate       | 86.2 ms                                                               | 87.8 ms: 1.02x slower                                                           |
| richards_super           | 52.3 ms                                                               | 53.3 ms: 1.02x slower                                                           |
| sympy_expand             | 454 ms                                                                | 463 ms: 1.02x slower                                                            |
| richards                 | 46.1 ms                                                               | 47.1 ms: 1.02x slower                                                           |
| html5lib                 | 61.3 ms                                                               | 62.6 ms: 1.02x slower                                                           |
| comprehensions           | 16.6 us                                                               | 17.0 us: 1.02x slower                                                           |
| pprint_safe_repr         | 720 ms                                                                | 736 ms: 1.02x slower                                                            |
| logging_silent           | 103 ns                                                                | 106 ns: 1.02x slower                                                            |
| sqlglot_optimize         | 53.3 ms                                                               | 54.5 ms: 1.02x slower                                                           |
| logging_simple           | 5.56 us                                                               | 5.69 us: 1.02x slower                                                           |
| float                    | 77.2 ms                                                               | 79.1 ms: 1.03x slower                                                           |
| pickle_pure_python       | 307 us                                                                | 315 us: 1.03x slower                                                            |
| xml_etree_process        | 59.1 ms                                                               | 60.7 ms: 1.03x slower                                                           |
| go                       | 119 ms                                                                | 123 ms: 1.03x slower                                                            |
| scimark_monte_carlo      | 67.1 ms                                                               | 69.2 ms: 1.03x slower                                                           |
| sqlglot_normalize        | 106 ms                                                                | 110 ms: 1.03x slower                                                            |
| mako                     | 11.3 ms                                                               | 11.6 ms: 1.03x slower                                                           |
| logging_format           | 6.16 us                                                               | 6.35 us: 1.03x slower                                                           |
| coroutines               | 23.4 ms                                                               | 24.2 ms: 1.03x slower                                                           |
| hexiom                   | 6.20 ms                                                               | 6.39 ms: 1.03x slower                                                           |
| deepcopy                 | 259 us                                                                | 268 us: 1.03x slower                                                            |
| generators               | 27.1 ms                                                               | 28.2 ms: 1.04x slower                                                           |
| deepcopy_reduce          | 2.65 us                                                               | 2.76 us: 1.04x slower                                                           |
| pycparser                | 1.14 sec                                                              | 1.19 sec: 1.04x slower                                                          |
| deltablue                | 3.21 ms                                                               | 3.36 ms: 1.04x slower                                                           |
| scimark_fft              | 357 ms                                                                | 373 ms: 1.04x slower                                                            |
| unpickle_pure_python     | 215 us                                                                | 224 us: 1.05x slower                                                            |
| deepcopy_memo            | 30.7 us                                                               | 32.2 us: 1.05x slower                                                           |
| tomli_loads              | 2.08 sec                                                              | 2.17 sec: 1.05x slower                                                          |
| spectral_norm            | 112 ms                                                                | 117 ms: 1.05x slower                                                            |
| scimark_sor              | 123 ms                                                                | 129 ms: 1.05x slower                                                            |
| gc_traversal             | 3.79 ms                                                               | 3.98 ms: 1.05x slower                                                           |
| genshi_xml               | 49.3 ms                                                               | 51.8 ms: 1.05x slower                                                           |
| raytrace                 | 260 ms                                                                | 275 ms: 1.06x slower                                                            |
| scimark_lu               | 112 ms                                                                | 119 ms: 1.06x slower                                                            |
| unpack_sequence          | 46.5 ns                                                               | 49.7 ns: 1.07x slower                                                           |
| genshi_text              | 21.8 ms                                                               | 23.5 ms: 1.08x slower                                                           |
| nbody                    | 86.0 ms                                                               | 93.0 ms: 1.08x slower                                                           |
| scimark_sparse_mat_mult  | 4.55 ms                                                               | 4.93 ms: 1.08x slower                                                           |
| coverage                 | 83.7 ms                                                               | 91.8 ms: 1.10x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (19): async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, unpickle, json_dumps, unpickle_list, asyncio_tcp_ssl, json_loads, meteor_contest, async_tree_cpu_io_mixed, sqlite_synth, crypto_pyaes, asyncio_websockets, bench_mp_pool, xml_etree_parse, async_tree_none, pylint

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x