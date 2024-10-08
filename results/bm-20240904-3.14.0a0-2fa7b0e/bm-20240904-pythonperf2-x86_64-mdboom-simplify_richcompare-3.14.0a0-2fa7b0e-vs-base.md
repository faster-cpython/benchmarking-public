# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.00x faster
- HPT reliability: 62.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 283 ms                                                                      | 284 ms: 1.00x slower                                                        |
| tornado_http   | 117 ms                                                                      | 116 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp      | 368 ms                                                                      | 366 ms: 1.01x faster                                                        |
| async_generators | 366 ms                                                                      | 371 ms: 1.01x slower                                                        |
| coroutines       | 21.5 ms                                                                     | 22.4 ms: 1.04x slower                                                       |
| Geometric mean   | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (10): asyncio_websockets, async_tree_memoization, async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.9 ms                                                                     | 85.8 ms: 1.02x faster                                                       |
| float          | 81.1 ms                                                                     | 79.2 ms: 1.02x faster                                                       |
| pidigits       | 253 ms                                                                      | 252 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                      | 141 ms: 1.01x faster                                                        |
| regex_effbot   | 3.51 ms                                                                     | 3.47 ms: 1.01x faster                                                       |
| regex_v8       | 26.2 ms                                                                     | 26.8 ms: 1.02x slower                                                       |
| regex_dna      | 233 ms                                                                      | 255 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.63 sec                                                                    | 2.56 sec: 1.03x faster                                                      |
| xml_etree_process    | 60.8 ms                                                                     | 59.3 ms: 1.02x faster                                                       |
| xml_etree_generate   | 85.8 ms                                                                     | 84.1 ms: 1.02x faster                                                       |
| pickle_pure_python   | 315 us                                                                      | 310 us: 1.01x faster                                                        |
| unpickle_pure_python | 218 us                                                                      | 216 us: 1.01x faster                                                        |
| json_dumps           | 10.8 ms                                                                     | 10.9 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 9.07 ms                                                                     | 9.08 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 58.2 ms                                                                     | 54.8 ms: 1.06x faster                                                       |
| genshi_text    | 25.5 ms                                                                     | 25.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_sor              | 121 ms                                                                      | 109 ms: 1.11x faster                                                        |
| coverage                 | 79.8 ms                                                                     | 74.9 ms: 1.07x faster                                                       |
| genshi_xml               | 58.2 ms                                                                     | 54.8 ms: 1.06x faster                                                       |
| scimark_fft              | 306 ms                                                                      | 296 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult  | 4.32 ms                                                                     | 4.18 ms: 1.03x faster                                                       |
| fannkuch                 | 372 ms                                                                      | 360 ms: 1.03x faster                                                        |
| tomli_loads              | 2.63 sec                                                                    | 2.56 sec: 1.03x faster                                                      |
| pyflate                  | 494 ms                                                                      | 481 ms: 1.03x faster                                                        |
| pycparser                | 1.26 sec                                                                    | 1.23 sec: 1.03x faster                                                      |
| xml_etree_process        | 60.8 ms                                                                     | 59.3 ms: 1.02x faster                                                       |
| nbody                    | 87.9 ms                                                                     | 85.8 ms: 1.02x faster                                                       |
| float                    | 81.1 ms                                                                     | 79.2 ms: 1.02x faster                                                       |
| generators               | 29.0 ms                                                                     | 28.4 ms: 1.02x faster                                                       |
| deltablue                | 3.50 ms                                                                     | 3.42 ms: 1.02x faster                                                       |
| xml_etree_generate       | 85.8 ms                                                                     | 84.1 ms: 1.02x faster                                                       |
| go                       | 137 ms                                                                      | 134 ms: 1.02x faster                                                        |
| deepcopy_memo            | 30.0 us                                                                     | 29.4 us: 1.02x faster                                                       |
| json                     | 5.37 ms                                                                     | 5.28 ms: 1.02x faster                                                       |
| deepcopy_reduce          | 2.93 us                                                                     | 2.89 us: 1.01x faster                                                       |
| pickle_pure_python       | 315 us                                                                      | 310 us: 1.01x faster                                                        |
| regex_compile            | 142 ms                                                                      | 141 ms: 1.01x faster                                                        |
| genshi_text              | 25.5 ms                                                                     | 25.2 ms: 1.01x faster                                                       |
| tornado_http             | 117 ms                                                                      | 116 ms: 1.01x faster                                                        |
| telco                    | 8.27 ms                                                                     | 8.17 ms: 1.01x faster                                                       |
| regex_effbot             | 3.51 ms                                                                     | 3.47 ms: 1.01x faster                                                       |
| typing_runtime_protocols | 177 us                                                                      | 175 us: 1.01x faster                                                        |
| gc_traversal             | 4.68 ms                                                                     | 4.63 ms: 1.01x faster                                                       |
| unpickle_pure_python     | 218 us                                                                      | 216 us: 1.01x faster                                                        |
| pathlib                  | 15.8 ms                                                                     | 15.7 ms: 1.01x faster                                                       |
| pprint_safe_repr         | 806 ms                                                                      | 802 ms: 1.01x faster                                                        |
| asyncio_tcp              | 368 ms                                                                      | 366 ms: 1.01x faster                                                        |
| spectral_norm            | 96.5 ms                                                                     | 96.0 ms: 1.00x faster                                                       |
| deepcopy                 | 286 us                                                                      | 285 us: 1.00x faster                                                        |
| richards_super           | 56.2 ms                                                                     | 56.0 ms: 1.00x faster                                                       |
| pidigits                 | 253 ms                                                                      | 252 ms: 1.00x faster                                                        |
| python_startup           | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| bpe_tokeniser            | 4.96 sec                                                                    | 4.96 sec: 1.00x slower                                                      |
| python_startup_no_site   | 9.07 ms                                                                     | 9.08 ms: 1.00x slower                                                       |
| mdp                      | 2.50 sec                                                                    | 2.51 sec: 1.00x slower                                                      |
| richards                 | 50.0 ms                                                                     | 50.1 ms: 1.00x slower                                                       |
| 2to3                     | 283 ms                                                                      | 284 ms: 1.00x slower                                                        |
| sympy_sum                | 152 ms                                                                      | 152 ms: 1.00x slower                                                        |
| sqlglot_optimize         | 59.0 ms                                                                     | 59.3 ms: 1.00x slower                                                       |
| raytrace                 | 273 ms                                                                      | 275 ms: 1.01x slower                                                        |
| json_dumps               | 10.8 ms                                                                     | 10.9 ms: 1.01x slower                                                       |
| scimark_lu               | 95.0 ms                                                                     | 95.7 ms: 1.01x slower                                                       |
| comprehensions           | 17.3 us                                                                     | 17.4 us: 1.01x slower                                                       |
| meteor_contest           | 127 ms                                                                      | 128 ms: 1.01x slower                                                        |
| logging_format           | 6.80 us                                                                     | 6.88 us: 1.01x slower                                                       |
| hexiom                   | 6.25 ms                                                                     | 6.32 ms: 1.01x slower                                                       |
| sympy_expand             | 498 ms                                                                      | 503 ms: 1.01x slower                                                        |
| async_generators         | 366 ms                                                                      | 371 ms: 1.01x slower                                                        |
| sqlglot_normalize        | 119 ms                                                                      | 121 ms: 1.01x slower                                                        |
| thrift                   | 846 us                                                                      | 857 us: 1.01x slower                                                        |
| sympy_str                | 290 ms                                                                      | 294 ms: 1.01x slower                                                        |
| logging_silent           | 97.8 ns                                                                     | 99.3 ns: 1.02x slower                                                       |
| nqueens                  | 88.3 ms                                                                     | 89.7 ms: 1.02x slower                                                       |
| crypto_pyaes             | 72.6 ms                                                                     | 74.1 ms: 1.02x slower                                                       |
| chaos                    | 61.5 ms                                                                     | 62.8 ms: 1.02x slower                                                       |
| regex_v8                 | 26.2 ms                                                                     | 26.8 ms: 1.02x slower                                                       |
| logging_simple           | 6.19 us                                                                     | 6.34 us: 1.02x slower                                                       |
| scimark_monte_carlo      | 66.0 ms                                                                     | 68.4 ms: 1.04x slower                                                       |
| coroutines               | 21.5 ms                                                                     | 22.4 ms: 1.04x slower                                                       |
| regex_dna                | 233 ms                                                                      | 255 ms: 1.09x slower                                                        |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (25): create_gc_cycles, sqlglot_parse, asyncio_websockets, sqlglot_transpile, pprint_pformat, async_tree_memoization, async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_none_tg, async_tree_io_tg, docutils, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, xml_etree_parse, json_loads, sympy_integrate, async_tree_none, html5lib, xml_etree_iterparse, mako, async_tree_io, django_template, pylint, bench_thread_pool, bench_mp_pool

# HPT report

- Reliability score: 62.61% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x