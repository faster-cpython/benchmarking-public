# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.01x faster
- HPT reliability: 97.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 318 ms                                                                      | 315 ms: 1.01x faster                                                     |
| docutils       | 3.27 sec                                                                    | 3.17 sec: 1.03x faster                                                   |
| html5lib       | 71.5 ms                                                                     | 73.1 ms: 1.02x slower                                                    |
| tornado_http   | 124 ms                                                                      | 123 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 833 ms                                                                      | 782 ms: 1.07x faster                                                     |
| async_tree_io              | 842 ms                                                                      | 805 ms: 1.05x faster                                                     |
| async_tree_memoization     | 417 ms                                                                      | 407 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                      | 547 ms: 1.02x faster                                                     |
| asyncio_tcp                | 377 ms                                                                      | 371 ms: 1.02x faster                                                     |
| async_generators           | 386 ms                                                                      | 382 ms: 1.01x faster                                                     |
| asyncio_websockets         | 382 ms                                                                      | 390 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed    | 566 ms                                                                      | 580 ms: 1.03x slower                                                     |
| coroutines                 | 21.3 ms                                                                     | 22.1 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (4): async_tree_none_tg, asyncio_tcp_ssl, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 77.5 ms                                                                     | 75.3 ms: 1.03x faster                                                    |
| pidigits       | 252 ms                                                                      | 251 ms: 1.00x faster                                                     |
| nbody          | 81.0 ms                                                                     | 83.3 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 253 ms                                                                      | 236 ms: 1.07x faster                                                     |
| regex_v8       | 25.8 ms                                                                     | 24.8 ms: 1.04x faster                                                    |
| regex_compile  | 149 ms                                                                      | 150 ms: 1.01x slower                                                     |
| regex_effbot   | 3.51 ms                                                                     | 3.60 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|---------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle            | 15.7 us                                                                     | 14.8 us: 1.06x faster                                                    |
| pickle_dict         | 30.7 us                                                                     | 29.8 us: 1.03x faster                                                    |
| pickle_pure_python  | 334 us                                                                      | 325 us: 1.03x faster                                                     |
| xml_etree_iterparse | 102 ms                                                                      | 99.8 ms: 1.02x faster                                                    |
| xml_etree_process   | 57.1 ms                                                                     | 56.4 ms: 1.01x faster                                                    |
| xml_etree_generate  | 79.8 ms                                                                     | 78.8 ms: 1.01x faster                                                    |
| tomli_loads         | 2.18 sec                                                                    | 2.20 sec: 1.01x slower                                                   |
| unpickle_list       | 4.66 us                                                                     | 4.71 us: 1.01x slower                                                    |
| json_loads          | 23.5 us                                                                     | 23.8 us: 1.01x slower                                                    |
| Geometric mean      | (ref)                                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (5): xml_etree_parse, pickle, pickle_list, unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 15.1 ms                                                                     | 13.4 ms: 1.13x faster                                                    |
| python_startup_no_site | 9.06 ms                                                                     | 8.97 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                                       | 1.07x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.20 ms                                                                     | 9.15 ms: 1.00x faster                                                    |
| django_template | 44.9 ms                                                                     | 46.0 ms: 1.02x slower                                                    |
| genshi_text     | 28.2 ms                                                                     | 29.8 ms: 1.06x slower                                                    |
| genshi_xml      | 62.3 ms                                                                     | 66.2 ms: 1.06x slower                                                    |
| Geometric mean  | (ref)                                                                       | 1.04x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| create_gc_cycles           | 2.80 ms                                                                     | 1.90 ms: 1.47x faster                                                    |
| gc_traversal               | 5.43 ms                                                                     | 4.31 ms: 1.26x faster                                                    |
| python_startup             | 15.1 ms                                                                     | 13.4 ms: 1.13x faster                                                    |
| spectral_norm              | 90.6 ms                                                                     | 82.8 ms: 1.09x faster                                                    |
| regex_dna                  | 253 ms                                                                      | 236 ms: 1.07x faster                                                     |
| async_tree_io_tg           | 833 ms                                                                      | 782 ms: 1.07x faster                                                     |
| unpickle                   | 15.7 us                                                                     | 14.8 us: 1.06x faster                                                    |
| fannkuch                   | 364 ms                                                                      | 346 ms: 1.05x faster                                                     |
| async_tree_io              | 842 ms                                                                      | 805 ms: 1.05x faster                                                     |
| generators                 | 38.8 ms                                                                     | 37.3 ms: 1.04x faster                                                    |
| sympy_sum                  | 179 ms                                                                      | 172 ms: 1.04x faster                                                     |
| regex_v8                   | 25.8 ms                                                                     | 24.8 ms: 1.04x faster                                                    |
| dulwich_log                | 67.0 ms                                                                     | 64.8 ms: 1.03x faster                                                    |
| docutils                   | 3.27 sec                                                                    | 3.17 sec: 1.03x faster                                                   |
| float                      | 77.5 ms                                                                     | 75.3 ms: 1.03x faster                                                    |
| sympy_integrate            | 27.8 ms                                                                     | 27.0 ms: 1.03x faster                                                    |
| comprehensions             | 19.3 us                                                                     | 18.7 us: 1.03x faster                                                    |
| pickle_dict                | 30.7 us                                                                     | 29.8 us: 1.03x faster                                                    |
| pickle_pure_python         | 334 us                                                                      | 325 us: 1.03x faster                                                     |
| raytrace                   | 331 ms                                                                      | 323 ms: 1.03x faster                                                     |
| async_tree_memoization     | 417 ms                                                                      | 407 ms: 1.03x faster                                                     |
| bench_thread_pool          | 969 us                                                                      | 946 us: 1.02x faster                                                     |
| logging_format             | 7.46 us                                                                     | 7.28 us: 1.02x faster                                                    |
| sympy_str                  | 326 ms                                                                      | 318 ms: 1.02x faster                                                     |
| pprint_safe_repr           | 780 ms                                                                      | 762 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                      | 547 ms: 1.02x faster                                                     |
| logging_simple             | 6.76 us                                                                     | 6.63 us: 1.02x faster                                                    |
| xml_etree_iterparse        | 102 ms                                                                      | 99.8 ms: 1.02x faster                                                    |
| sqlglot_transpile          | 1.98 ms                                                                     | 1.94 ms: 1.02x faster                                                    |
| bpe_tokeniser              | 4.83 sec                                                                    | 4.75 sec: 1.02x faster                                                   |
| asyncio_tcp                | 377 ms                                                                      | 371 ms: 1.02x faster                                                     |
| deepcopy_reduce            | 3.00 us                                                                     | 2.95 us: 1.02x faster                                                    |
| crypto_pyaes               | 71.2 ms                                                                     | 70.0 ms: 1.02x faster                                                    |
| typing_runtime_protocols   | 179 us                                                                      | 176 us: 1.01x faster                                                     |
| xml_etree_process          | 57.1 ms                                                                     | 56.4 ms: 1.01x faster                                                    |
| xml_etree_generate         | 79.8 ms                                                                     | 78.8 ms: 1.01x faster                                                    |
| scimark_lu                 | 97.2 ms                                                                     | 96.0 ms: 1.01x faster                                                    |
| async_generators           | 386 ms                                                                      | 382 ms: 1.01x faster                                                     |
| tornado_http               | 124 ms                                                                      | 123 ms: 1.01x faster                                                     |
| python_startup_no_site     | 9.06 ms                                                                     | 8.97 ms: 1.01x faster                                                    |
| 2to3                       | 318 ms                                                                      | 315 ms: 1.01x faster                                                     |
| scimark_fft                | 283 ms                                                                      | 280 ms: 1.01x faster                                                     |
| sqlglot_optimize           | 70.2 ms                                                                     | 69.6 ms: 1.01x faster                                                    |
| mako                       | 9.20 ms                                                                     | 9.15 ms: 1.00x faster                                                    |
| scimark_monte_carlo        | 69.1 ms                                                                     | 68.8 ms: 1.00x faster                                                    |
| hexiom                     | 7.12 ms                                                                     | 7.09 ms: 1.00x faster                                                    |
| pidigits                   | 252 ms                                                                      | 251 ms: 1.00x faster                                                     |
| meteor_contest             | 134 ms                                                                      | 134 ms: 1.00x slower                                                     |
| pathlib                    | 15.7 ms                                                                     | 15.8 ms: 1.01x slower                                                    |
| sqlglot_parse              | 1.50 ms                                                                     | 1.51 ms: 1.01x slower                                                    |
| tomli_loads                | 2.18 sec                                                                    | 2.20 sec: 1.01x slower                                                   |
| unpickle_list              | 4.66 us                                                                     | 4.71 us: 1.01x slower                                                    |
| regex_compile              | 149 ms                                                                      | 150 ms: 1.01x slower                                                     |
| sqlglot_normalize          | 134 ms                                                                      | 136 ms: 1.01x slower                                                     |
| pyflate                    | 450 ms                                                                      | 456 ms: 1.01x slower                                                     |
| json_loads                 | 23.5 us                                                                     | 23.8 us: 1.01x slower                                                    |
| richards                   | 46.5 ms                                                                     | 47.3 ms: 1.02x slower                                                    |
| asyncio_websockets         | 382 ms                                                                      | 390 ms: 1.02x slower                                                     |
| html5lib                   | 71.5 ms                                                                     | 73.1 ms: 1.02x slower                                                    |
| regex_effbot               | 3.51 ms                                                                     | 3.60 ms: 1.02x slower                                                    |
| django_template            | 44.9 ms                                                                     | 46.0 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed    | 566 ms                                                                      | 580 ms: 1.03x slower                                                     |
| scimark_sor                | 102 ms                                                                      | 105 ms: 1.03x slower                                                     |
| nbody                      | 81.0 ms                                                                     | 83.3 ms: 1.03x slower                                                    |
| go                         | 153 ms                                                                      | 158 ms: 1.03x slower                                                     |
| pycparser                  | 1.27 sec                                                                    | 1.31 sec: 1.03x slower                                                   |
| chaos                      | 65.7 ms                                                                     | 68.0 ms: 1.04x slower                                                    |
| coroutines                 | 21.3 ms                                                                     | 22.1 ms: 1.04x slower                                                    |
| coverage                   | 78.8 ms                                                                     | 82.6 ms: 1.05x slower                                                    |
| richards_super             | 52.5 ms                                                                     | 55.4 ms: 1.05x slower                                                    |
| genshi_text                | 28.2 ms                                                                     | 29.8 ms: 1.06x slower                                                    |
| genshi_xml                 | 62.3 ms                                                                     | 66.2 ms: 1.06x slower                                                    |
| logging_silent             | 91.1 ns                                                                     | 98.1 ns: 1.08x slower                                                    |
| unpack_sequence            | 87.5 ns                                                                     | 94.8 ns: 1.08x slower                                                    |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (23): pylint, xml_etree_parse, pprint_pformat, pickle, deltablue, pickle_list, sympy_expand, unpickle_pure_python, async_tree_none_tg, scimark_sparse_mat_mult, telco, deepcopy_memo, asyncio_tcp_ssl, deepcopy, sqlite_synth, mdp, thrift, json_dumps, json, nqueens, async_tree_none, async_tree_memoization_tg, bench_mp_pool
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: sphinx

# HPT report

- Reliability score: 97.86% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x