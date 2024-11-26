# Results vs. 3.13.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-x86_64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.038x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 283 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                      |
| html5lib       | 72.9 ms                                                      | 71.8 ms: 1.01x faster                                                       |
| tornado_http   | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 387 ms: 1.18x faster                                                        |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 398 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 781 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 572 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 809 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 563 ms: 1.02x faster                                                        |
| async_generators           | 364 ms                                                       | 358 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 78.7 ms: 1.04x faster                                                       |
| nbody          | 92.1 ms                                                      | 88.9 ms: 1.04x faster                                                       |
| pidigits       | 252 ms                                                       | 252 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 138 ms: 1.03x faster                                                        |
| regex_dna      | 238 ms                                                       | 235 ms: 1.01x faster                                                        |
| regex_v8       | 24.9 ms                                                      | 25.2 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.7 ms                                                      | 59.1 ms: 1.03x faster                                                       |
| pickle_pure_python   | 322 us                                                       | 315 us: 1.02x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| json_dumps           | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                                       |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| unpickle_pure_python | 216 us                                                       | 224 us: 1.04x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 2.59 sec: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 8.96 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.1 ms: 1.13x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 53.6 ms: 1.08x faster                                                       |
| django_template | 38.9 ms                                                      | 40.3 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.91 ms: 1.39x faster                                                       |
| deepcopy                   | 388 us                                                       | 284 us: 1.37x faster                                                        |
| deepcopy_memo              | 38.9 us                                                      | 30.0 us: 1.30x faster                                                       |
| go                         | 167 ms                                                       | 136 ms: 1.23x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.86 us: 1.22x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 387 ms: 1.18x faster                                                        |
| generators                 | 33.9 ms                                                      | 28.9 ms: 1.17x faster                                                       |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                                        |
| genshi_text                | 27.2 ms                                                      | 24.1 ms: 1.13x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 398 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                       |
| genshi_xml                 | 58.0 ms                                                      | 53.6 ms: 1.08x faster                                                       |
| telco                      | 8.77 ms                                                      | 8.11 ms: 1.08x faster                                                       |
| richards_super             | 60.2 ms                                                      | 56.0 ms: 1.08x faster                                                       |
| bench_thread_pool          | 929 us                                                       | 867 us: 1.07x faster                                                        |
| fannkuch                   | 384 ms                                                       | 359 ms: 1.07x faster                                                        |
| scimark_sor                | 125 ms                                                       | 117 ms: 1.07x faster                                                        |
| json                       | 5.62 ms                                                      | 5.29 ms: 1.06x faster                                                       |
| coverage                   | 84.5 ms                                                      | 80.2 ms: 1.05x faster                                                       |
| async_tree_io_tg           | 823 ms                                                       | 781 ms: 1.05x faster                                                        |
| thrift                     | 918 us                                                       | 874 us: 1.05x faster                                                        |
| hexiom                     | 6.47 ms                                                      | 6.19 ms: 1.05x faster                                                       |
| nqueens                    | 92.3 ms                                                      | 88.3 ms: 1.05x faster                                                       |
| richards                   | 52.5 ms                                                      | 50.2 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 572 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 802 ms: 1.04x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.90 sec: 1.04x faster                                                      |
| float                      | 81.6 ms                                                      | 78.7 ms: 1.04x faster                                                       |
| nbody                      | 92.1 ms                                                      | 88.9 ms: 1.04x faster                                                       |
| 2to3                       | 293 ms                                                       | 283 ms: 1.03x faster                                                        |
| regex_compile              | 143 ms                                                       | 138 ms: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 59.1 ms: 1.03x faster                                                       |
| async_tree_io              | 832 ms                                                       | 809 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.66 sec: 1.03x faster                                                      |
| pycparser                  | 1.28 sec                                                     | 1.25 sec: 1.03x faster                                                      |
| sympy_str                  | 297 ms                                                       | 289 ms: 1.03x faster                                                        |
| typing_runtime_protocols   | 176 us                                                       | 172 us: 1.02x faster                                                        |
| sympy_integrate            | 23.4 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| pickle_pure_python         | 322 us                                                       | 315 us: 1.02x faster                                                        |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 563 ms: 1.02x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 95.8 ms: 1.02x faster                                                       |
| sqlglot_normalize          | 119 ms                                                       | 117 ms: 1.02x faster                                                        |
| sympy_expand               | 506 ms                                                       | 499 ms: 1.02x faster                                                        |
| regex_dna                  | 238 ms                                                       | 235 ms: 1.01x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 71.8 ms: 1.01x faster                                                       |
| async_generators           | 364 ms                                                       | 358 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 57.9 ms: 1.01x faster                                                       |
| mdp                        | 2.53 sec                                                     | 2.50 sec: 1.01x faster                                                      |
| spectral_norm              | 97.4 ms                                                      | 96.4 ms: 1.01x faster                                                       |
| pyflate                    | 493 ms                                                       | 489 ms: 1.01x faster                                                        |
| comprehensions             | 17.3 us                                                      | 17.2 us: 1.01x faster                                                       |
| pidigits                   | 252 ms                                                       | 252 ms: 1.00x faster                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 8.96 ms: 1.00x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 66.1 ms: 1.01x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.26 ms: 1.01x slower                                                       |
| regex_v8                   | 24.9 ms                                                      | 25.2 ms: 1.01x slower                                                       |
| logging_simple             | 6.28 us                                                      | 6.37 us: 1.01x slower                                                       |
| json_dumps                 | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| scimark_fft                | 298 ms                                                       | 304 ms: 1.02x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| logging_silent             | 97.5 ns                                                      | 100 ns: 1.03x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 1.81 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 67.2 ms: 1.03x slower                                                       |
| chaos                      | 60.6 ms                                                      | 62.6 ms: 1.03x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                      |
| unpickle_pure_python       | 216 us                                                       | 224 us: 1.04x slower                                                        |
| django_template            | 38.9 ms                                                      | 40.3 ms: 1.04x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 1.42 ms: 1.04x slower                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.59 sec: 1.07x slower                                                      |
| gc_traversal               | 4.48 ms                                                      | 4.87 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (10): bench_mp_pool, logging_format, regex_effbot, deltablue, crypto_pyaes, mako, xml_etree_generate, raytrace, xml_etree_iterparse, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.038x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x