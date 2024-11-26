# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.003x faster
- HPT reliability: 99.12%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 318 ms                                                                      | 316 ms: 1.01x faster                                                 |
| docutils       | 3.27 sec                                                                    | 3.22 sec: 1.02x faster                                               |
| sphinx         | 1.28 sec                                                                    | 1.27 sec: 1.01x faster                                               |
| tornado_http   | 124 ms                                                                      | 122 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|---------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg | 387 ms                                                                      | 375 ms: 1.03x faster                                                 |
| async_tree_none           | 326 ms                                                                      | 322 ms: 1.01x faster                                                 |
| coroutines                | 21.3 ms                                                                     | 21.5 ms: 1.01x slower                                                |
| Geometric mean            | (ref)                                                                       | 1.01x faster                                                         |

Benchmark hidden because not significant (10): async_tree_none_tg, async_tree_memoization, async_tree_io_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_tcp, async_generators, asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 77.5 ms                                                                     | 78.1 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                         |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 253 ms                                                                      | 247 ms: 1.02x faster                                                 |
| regex_effbot   | 3.51 ms                                                                     | 3.47 ms: 1.01x faster                                                |
| regex_compile  | 149 ms                                                                      | 147 ms: 1.01x faster                                                 |
| regex_v8       | 25.8 ms                                                                     | 25.6 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|--------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps         | 10.7 ms                                                                     | 10.5 ms: 1.02x faster                                                |
| pickle_dict        | 30.7 us                                                                     | 30.2 us: 1.02x faster                                                |
| pickle_list        | 4.31 us                                                                     | 4.25 us: 1.02x faster                                                |
| xml_etree_process  | 57.1 ms                                                                     | 56.6 ms: 1.01x faster                                                |
| xml_etree_generate | 79.8 ms                                                                     | 79.4 ms: 1.01x faster                                                |
| json_loads         | 23.5 us                                                                     | 23.9 us: 1.02x slower                                                |
| unpickle_list      | 4.66 us                                                                     | 4.75 us: 1.02x slower                                                |
| Geometric mean     | (ref)                                                                       | 1.00x faster                                                         |

Benchmark hidden because not significant (7): unpickle_pure_python, tomli_loads, pickle, unpickle, pickle_pure_python, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 15.1 ms                                                                     | 14.9 ms: 1.01x faster                                                |
| python_startup_no_site | 9.06 ms                                                                     | 8.99 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 44.9 ms                                                                     | 42.5 ms: 1.06x faster                                                |
| mako            | 9.20 ms                                                                     | 9.15 ms: 1.00x faster                                                |
| genshi_text     | 28.2 ms                                                                     | 28.9 ms: 1.03x slower                                                |
| genshi_xml      | 62.3 ms                                                                     | 64.8 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                                       | 1.00x slower                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|---------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template           | 44.9 ms                                                                     | 42.5 ms: 1.06x faster                                                |
| gc_traversal              | 5.43 ms                                                                     | 5.17 ms: 1.05x faster                                                |
| richards                  | 46.5 ms                                                                     | 45.0 ms: 1.03x faster                                                |
| async_tree_memoization_tg | 387 ms                                                                      | 375 ms: 1.03x faster                                                 |
| thrift                    | 910 us                                                                      | 883 us: 1.03x faster                                                 |
| logging_format            | 7.46 us                                                                     | 7.28 us: 1.02x faster                                                |
| regex_dna                 | 253 ms                                                                      | 247 ms: 1.02x faster                                                 |
| sympy_sum                 | 179 ms                                                                      | 174 ms: 1.02x faster                                                 |
| json_dumps                | 10.7 ms                                                                     | 10.5 ms: 1.02x faster                                                |
| raytrace                  | 331 ms                                                                      | 324 ms: 1.02x faster                                                 |
| sympy_str                 | 326 ms                                                                      | 320 ms: 1.02x faster                                                 |
| sympy_expand              | 536 ms                                                                      | 526 ms: 1.02x faster                                                 |
| sympy_integrate           | 27.8 ms                                                                     | 27.3 ms: 1.02x faster                                                |
| docutils                  | 3.27 sec                                                                    | 3.22 sec: 1.02x faster                                               |
| dulwich_log               | 67.0 ms                                                                     | 65.9 ms: 1.02x faster                                                |
| scimark_fft               | 283 ms                                                                      | 278 ms: 1.02x faster                                                 |
| pickle_dict               | 30.7 us                                                                     | 30.2 us: 1.02x faster                                                |
| tornado_http              | 124 ms                                                                      | 122 ms: 1.02x faster                                                 |
| pickle_list               | 4.31 us                                                                     | 4.25 us: 1.02x faster                                                |
| regex_effbot              | 3.51 ms                                                                     | 3.47 ms: 1.01x faster                                                |
| sqlglot_optimize          | 70.2 ms                                                                     | 69.3 ms: 1.01x faster                                                |
| pycparser                 | 1.27 sec                                                                    | 1.25 sec: 1.01x faster                                               |
| scimark_monte_carlo       | 69.1 ms                                                                     | 68.3 ms: 1.01x faster                                                |
| go                        | 153 ms                                                                      | 152 ms: 1.01x faster                                                 |
| regex_compile             | 149 ms                                                                      | 147 ms: 1.01x faster                                                 |
| python_startup            | 15.1 ms                                                                     | 14.9 ms: 1.01x faster                                                |
| async_tree_none           | 326 ms                                                                      | 322 ms: 1.01x faster                                                 |
| logging_silent            | 91.1 ns                                                                     | 90.2 ns: 1.01x faster                                                |
| sphinx                    | 1.28 sec                                                                    | 1.27 sec: 1.01x faster                                               |
| xml_etree_process         | 57.1 ms                                                                     | 56.6 ms: 1.01x faster                                                |
| python_startup_no_site    | 9.06 ms                                                                     | 8.99 ms: 1.01x faster                                                |
| bpe_tokeniser             | 4.83 sec                                                                    | 4.79 sec: 1.01x faster                                               |
| deepcopy_reduce           | 3.00 us                                                                     | 2.98 us: 1.01x faster                                                |
| logging_simple            | 6.76 us                                                                     | 6.71 us: 1.01x faster                                                |
| 2to3                      | 318 ms                                                                      | 316 ms: 1.01x faster                                                 |
| regex_v8                  | 25.8 ms                                                                     | 25.6 ms: 1.01x faster                                                |
| xml_etree_generate        | 79.8 ms                                                                     | 79.4 ms: 1.01x faster                                                |
| scimark_sparse_mat_mult   | 4.15 ms                                                                     | 4.13 ms: 1.01x faster                                                |
| coverage                  | 78.8 ms                                                                     | 78.4 ms: 1.01x faster                                                |
| mako                      | 9.20 ms                                                                     | 9.15 ms: 1.00x faster                                                |
| spectral_norm             | 90.6 ms                                                                     | 90.2 ms: 1.00x faster                                                |
| sqlite_synth              | 2.72 us                                                                     | 2.71 us: 1.00x faster                                                |
| create_gc_cycles          | 2.80 ms                                                                     | 2.80 ms: 1.00x slower                                                |
| sqlglot_normalize         | 134 ms                                                                      | 135 ms: 1.01x slower                                                 |
| deepcopy                  | 300 us                                                                      | 302 us: 1.01x slower                                                 |
| float                     | 77.5 ms                                                                     | 78.1 ms: 1.01x slower                                                |
| nqueens                   | 102 ms                                                                      | 102 ms: 1.01x slower                                                 |
| coroutines                | 21.3 ms                                                                     | 21.5 ms: 1.01x slower                                                |
| pprint_pformat            | 1.61 sec                                                                    | 1.62 sec: 1.01x slower                                               |
| comprehensions            | 19.3 us                                                                     | 19.4 us: 1.01x slower                                                |
| fannkuch                  | 364 ms                                                                      | 367 ms: 1.01x slower                                                 |
| mdp                       | 2.59 sec                                                                    | 2.62 sec: 1.01x slower                                               |
| unpack_sequence           | 87.5 ns                                                                     | 88.6 ns: 1.01x slower                                                |
| richards_super            | 52.5 ms                                                                     | 53.3 ms: 1.01x slower                                                |
| typing_runtime_protocols  | 179 us                                                                      | 181 us: 1.02x slower                                                 |
| telco                     | 7.63 ms                                                                     | 7.76 ms: 1.02x slower                                                |
| pprint_safe_repr          | 780 ms                                                                      | 794 ms: 1.02x slower                                                 |
| json_loads                | 23.5 us                                                                     | 23.9 us: 1.02x slower                                                |
| unpickle_list             | 4.66 us                                                                     | 4.75 us: 1.02x slower                                                |
| generators                | 38.8 ms                                                                     | 39.8 ms: 1.03x slower                                                |
| genshi_text               | 28.2 ms                                                                     | 28.9 ms: 1.03x slower                                                |
| deepcopy_memo             | 27.3 us                                                                     | 28.1 us: 1.03x slower                                                |
| scimark_sor               | 102 ms                                                                      | 106 ms: 1.03x slower                                                 |
| genshi_xml                | 62.3 ms                                                                     | 64.8 ms: 1.04x slower                                                |
| chaos                     | 65.7 ms                                                                     | 68.4 ms: 1.04x slower                                                |
| Geometric mean            | (ref)                                                                       | 1.00x faster                                                         |

Benchmark hidden because not significant (33): async_tree_none_tg, pylint, async_tree_memoization, async_tree_io_tg, nbody, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, sqlglot_transpile, pathlib, asyncio_tcp, async_generators, sqlglot_parse, scimark_lu, crypto_pyaes, bench_thread_pool, pidigits, asyncio_tcp_ssl, html5lib, meteor_contest, pyflate, unpickle_pure_python, tomli_loads, pickle, json, hexiom, unpickle, asyncio_websockets, pickle_pure_python, deltablue, xml_etree_parse, xml_etree_iterparse, bench_mp_pool

- Geometric mean (including insignificant results): 1.003x faster
# HPT report

- Reliability score: 99.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x