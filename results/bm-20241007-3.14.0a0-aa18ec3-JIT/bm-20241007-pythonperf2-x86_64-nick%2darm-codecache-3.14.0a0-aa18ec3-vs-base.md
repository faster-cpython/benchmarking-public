# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 318 ms                                                                      | 317 ms: 1.00x faster                                                 |
| docutils       | 3.27 sec                                                                    | 3.19 sec: 1.03x faster                                               |
| html5lib       | 71.5 ms                                                                     | 73.1 ms: 1.02x slower                                                |
| tornado_http   | 124 ms                                                                      | 122 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 833 ms                                                                      | 792 ms: 1.05x faster                                                 |
| async_tree_io              | 842 ms                                                                      | 804 ms: 1.05x faster                                                 |
| async_tree_memoization     | 417 ms                                                                      | 406 ms: 1.03x faster                                                 |
| asyncio_tcp                | 377 ms                                                                      | 369 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                      | 549 ms: 1.02x faster                                                 |
| async_generators           | 386 ms                                                                      | 383 ms: 1.01x faster                                                 |
| coroutines                 | 21.3 ms                                                                     | 21.2 ms: 1.00x faster                                                |
| asyncio_websockets         | 382 ms                                                                      | 389 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed    | 566 ms                                                                      | 580 ms: 1.02x slower                                                 |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                         |

Benchmark hidden because not significant (4): async_tree_none_tg, asyncio_tcp_ssl, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 77.5 ms                                                                     | 75.8 ms: 1.02x faster                                                |
| pidigits       | 252 ms                                                                      | 250 ms: 1.01x faster                                                 |
| nbody          | 81.0 ms                                                                     | 84.2 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 25.8 ms                                                                     | 24.7 ms: 1.04x faster                                                |
| regex_dna      | 253 ms                                                                      | 245 ms: 1.03x faster                                                 |
| regex_effbot   | 3.51 ms                                                                     | 3.43 ms: 1.02x faster                                                |
| regex_compile  | 149 ms                                                                      | 152 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 145 ms                                                                      | 140 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 102 ms                                                                      | 98.4 ms: 1.03x faster                                                |
| pickle_list          | 4.31 us                                                                     | 4.20 us: 1.03x faster                                                |
| xml_etree_generate   | 79.8 ms                                                                     | 78.0 ms: 1.02x faster                                                |
| json_dumps           | 10.7 ms                                                                     | 10.5 ms: 1.02x faster                                                |
| unpickle_pure_python | 219 us                                                                      | 215 us: 1.02x faster                                                 |
| xml_etree_process    | 57.1 ms                                                                     | 56.2 ms: 1.02x faster                                                |
| pickle_pure_python   | 334 us                                                                      | 329 us: 1.01x faster                                                 |
| pickle_dict          | 30.7 us                                                                     | 30.8 us: 1.00x slower                                                |
| json_loads           | 23.5 us                                                                     | 23.8 us: 1.01x slower                                                |
| unpickle_list        | 4.66 us                                                                     | 4.76 us: 1.02x slower                                                |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                         |

Benchmark hidden because not significant (3): unpickle, tomli_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 15.1 ms                                                                     | 13.4 ms: 1.13x faster                                                |
| python_startup_no_site | 9.06 ms                                                                     | 8.96 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                                       | 1.07x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 44.9 ms                                                                     | 43.2 ms: 1.04x faster                                                |
| genshi_text     | 28.2 ms                                                                     | 29.0 ms: 1.03x slower                                                |
| genshi_xml      | 62.3 ms                                                                     | 64.4 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| create_gc_cycles           | 2.80 ms                                                                     | 1.87 ms: 1.50x faster                                                |
| gc_traversal               | 5.43 ms                                                                     | 4.30 ms: 1.27x faster                                                |
| python_startup             | 15.1 ms                                                                     | 13.4 ms: 1.13x faster                                                |
| spectral_norm              | 90.6 ms                                                                     | 83.3 ms: 1.09x faster                                                |
| async_tree_io_tg           | 833 ms                                                                      | 792 ms: 1.05x faster                                                 |
| richards                   | 46.5 ms                                                                     | 44.2 ms: 1.05x faster                                                |
| async_tree_io              | 842 ms                                                                      | 804 ms: 1.05x faster                                                 |
| dulwich_log                | 67.0 ms                                                                     | 64.0 ms: 1.05x faster                                                |
| regex_v8                   | 25.8 ms                                                                     | 24.7 ms: 1.04x faster                                                |
| django_template            | 44.9 ms                                                                     | 43.2 ms: 1.04x faster                                                |
| logging_format             | 7.46 us                                                                     | 7.18 us: 1.04x faster                                                |
| richards_super             | 52.5 ms                                                                     | 50.6 ms: 1.04x faster                                                |
| xml_etree_parse            | 145 ms                                                                      | 140 ms: 1.04x faster                                                 |
| sympy_sum                  | 179 ms                                                                      | 173 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 102 ms                                                                      | 98.4 ms: 1.03x faster                                                |
| pprint_safe_repr           | 780 ms                                                                      | 755 ms: 1.03x faster                                                 |
| regex_dna                  | 253 ms                                                                      | 245 ms: 1.03x faster                                                 |
| raytrace                   | 331 ms                                                                      | 322 ms: 1.03x faster                                                 |
| sqlglot_normalize          | 134 ms                                                                      | 130 ms: 1.03x faster                                                 |
| bpe_tokeniser              | 4.83 sec                                                                    | 4.70 sec: 1.03x faster                                               |
| async_tree_memoization     | 417 ms                                                                      | 406 ms: 1.03x faster                                                 |
| pickle_list                | 4.31 us                                                                     | 4.20 us: 1.03x faster                                                |
| comprehensions             | 19.3 us                                                                     | 18.8 us: 1.03x faster                                                |
| docutils                   | 3.27 sec                                                                    | 3.19 sec: 1.03x faster                                               |
| sympy_str                  | 326 ms                                                                      | 318 ms: 1.02x faster                                                 |
| xml_etree_generate         | 79.8 ms                                                                     | 78.0 ms: 1.02x faster                                                |
| regex_effbot               | 3.51 ms                                                                     | 3.43 ms: 1.02x faster                                                |
| float                      | 77.5 ms                                                                     | 75.8 ms: 1.02x faster                                                |
| bench_thread_pool          | 969 us                                                                      | 947 us: 1.02x faster                                                 |
| logging_simple             | 6.76 us                                                                     | 6.61 us: 1.02x faster                                                |
| asyncio_tcp                | 377 ms                                                                      | 369 ms: 1.02x faster                                                 |
| sympy_integrate            | 27.8 ms                                                                     | 27.2 ms: 1.02x faster                                                |
| json_dumps                 | 10.7 ms                                                                     | 10.5 ms: 1.02x faster                                                |
| fannkuch                   | 364 ms                                                                      | 356 ms: 1.02x faster                                                 |
| sqlglot_optimize           | 70.2 ms                                                                     | 68.7 ms: 1.02x faster                                                |
| pprint_pformat             | 1.61 sec                                                                    | 1.58 sec: 1.02x faster                                               |
| unpickle_pure_python       | 219 us                                                                      | 215 us: 1.02x faster                                                 |
| sympy_expand               | 536 ms                                                                      | 525 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                      | 549 ms: 1.02x faster                                                 |
| xml_etree_process          | 57.1 ms                                                                     | 56.2 ms: 1.02x faster                                                |
| tornado_http               | 124 ms                                                                      | 122 ms: 1.02x faster                                                 |
| pickle_pure_python         | 334 us                                                                      | 329 us: 1.01x faster                                                 |
| deepcopy_reduce            | 3.00 us                                                                     | 2.96 us: 1.01x faster                                                |
| mdp                        | 2.59 sec                                                                    | 2.56 sec: 1.01x faster                                               |
| python_startup_no_site     | 9.06 ms                                                                     | 8.96 ms: 1.01x faster                                                |
| nqueens                    | 102 ms                                                                      | 101 ms: 1.01x faster                                                 |
| pidigits                   | 252 ms                                                                      | 250 ms: 1.01x faster                                                 |
| hexiom                     | 7.12 ms                                                                     | 7.06 ms: 1.01x faster                                                |
| deltablue                  | 3.23 ms                                                                     | 3.21 ms: 1.01x faster                                                |
| async_generators           | 386 ms                                                                      | 383 ms: 1.01x faster                                                 |
| scimark_monte_carlo        | 69.1 ms                                                                     | 68.7 ms: 1.01x faster                                                |
| crypto_pyaes               | 71.2 ms                                                                     | 70.7 ms: 1.01x faster                                                |
| meteor_contest             | 134 ms                                                                      | 133 ms: 1.01x faster                                                 |
| coroutines                 | 21.3 ms                                                                     | 21.2 ms: 1.00x faster                                                |
| 2to3                       | 318 ms                                                                      | 317 ms: 1.00x faster                                                 |
| scimark_sparse_mat_mult    | 4.15 ms                                                                     | 4.14 ms: 1.00x faster                                                |
| pickle_dict                | 30.7 us                                                                     | 30.8 us: 1.00x slower                                                |
| json                       | 5.16 ms                                                                     | 5.20 ms: 1.01x slower                                                |
| unpack_sequence            | 87.5 ns                                                                     | 88.7 ns: 1.01x slower                                                |
| json_loads                 | 23.5 us                                                                     | 23.8 us: 1.01x slower                                                |
| sqlglot_parse              | 1.50 ms                                                                     | 1.52 ms: 1.02x slower                                                |
| deepcopy_memo              | 27.3 us                                                                     | 27.7 us: 1.02x slower                                                |
| chaos                      | 65.7 ms                                                                     | 66.8 ms: 1.02x slower                                                |
| pycparser                  | 1.27 sec                                                                    | 1.29 sec: 1.02x slower                                               |
| asyncio_websockets         | 382 ms                                                                      | 389 ms: 1.02x slower                                                 |
| generators                 | 38.8 ms                                                                     | 39.5 ms: 1.02x slower                                                |
| unpickle_list              | 4.66 us                                                                     | 4.76 us: 1.02x slower                                                |
| html5lib                   | 71.5 ms                                                                     | 73.1 ms: 1.02x slower                                                |
| coverage                   | 78.8 ms                                                                     | 80.7 ms: 1.02x slower                                                |
| regex_compile              | 149 ms                                                                      | 152 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed    | 566 ms                                                                      | 580 ms: 1.02x slower                                                 |
| genshi_text                | 28.2 ms                                                                     | 29.0 ms: 1.03x slower                                                |
| genshi_xml                 | 62.3 ms                                                                     | 64.4 ms: 1.03x slower                                                |
| nbody                      | 81.0 ms                                                                     | 84.2 ms: 1.04x slower                                                |
| scimark_sor                | 102 ms                                                                      | 107 ms: 1.04x slower                                                 |
| typing_runtime_protocols   | 179 us                                                                      | 189 us: 1.06x slower                                                 |
| logging_silent             | 91.1 ns                                                                     | 98.9 ns: 1.09x slower                                                |
| bench_mp_pool              | 2.25 sec                                                                    | 4.58 sec: 2.04x slower                                               |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                         |

Benchmark hidden because not significant (19): pylint, async_tree_none_tg, unpickle, sqlite_synth, tomli_loads, scimark_lu, deepcopy, asyncio_tcp_ssl, mako, scimark_fft, go, pickle, sqlglot_transpile, pathlib, pyflate, async_tree_none, thrift, async_tree_memoization_tg, telco
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x