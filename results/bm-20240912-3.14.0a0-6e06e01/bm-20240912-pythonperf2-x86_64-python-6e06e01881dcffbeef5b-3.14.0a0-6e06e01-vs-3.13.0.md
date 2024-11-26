# Results vs. 3.13.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.036x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 72.9 ms                                                      | 71.5 ms: 1.02x faster                                                       |
| tornado_http   | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 391 ms: 1.17x faster                                                        |
| async_tree_none            | 370 ms                                                       | 322 ms: 1.15x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 400 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 310 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 795 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 803 ms: 1.04x faster                                                        |
| async_generators           | 364 ms                                                       | 361 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                       |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 87.2 ms: 1.06x faster                                                       |
| float          | 81.6 ms                                                      | 78.3 ms: 1.04x faster                                                       |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 140 ms: 1.02x faster                                                        |
| regex_dna      | 238 ms                                                       | 241 ms: 1.01x slower                                                        |
| regex_v8       | 24.9 ms                                                      | 25.5 ms: 1.02x slower                                                       |
| regex_effbot   | 3.51 ms                                                      | 3.64 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 317 us: 1.01x faster                                                        |
| xml_etree_process    | 60.7 ms                                                      | 59.9 ms: 1.01x faster                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 85.6 ms: 1.00x slower                                                       |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.01x slower                                                       |
| unpickle_pure_python | 216 us                                                       | 220 us: 1.02x slower                                                        |
| xml_etree_iterparse  | 99.8 ms                                                      | 102 ms: 1.02x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 2.53 sec: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 8.94 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 54.6 ms: 1.06x faster                                                       |
| django_template | 38.9 ms                                                      | 38.3 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.92 ms: 1.38x faster                                                       |
| deepcopy                   | 388 us                                                       | 286 us: 1.36x faster                                                        |
| deepcopy_memo              | 38.9 us                                                      | 30.2 us: 1.29x faster                                                       |
| go                         | 167 ms                                                       | 134 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.90 us: 1.20x faster                                                       |
| python_startup             | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 391 ms: 1.17x faster                                                        |
| generators                 | 33.9 ms                                                      | 29.3 ms: 1.16x faster                                                       |
| async_tree_none            | 370 ms                                                       | 322 ms: 1.15x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.6 ms: 1.12x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 400 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 310 ms: 1.10x faster                                                        |
| genshi_text                | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                       |
| fannkuch                   | 384 ms                                                       | 356 ms: 1.08x faster                                                        |
| bench_thread_pool          | 929 us                                                       | 865 us: 1.07x faster                                                        |
| json                       | 5.62 ms                                                      | 5.24 ms: 1.07x faster                                                       |
| thrift                     | 918 us                                                       | 859 us: 1.07x faster                                                        |
| richards_super             | 60.2 ms                                                      | 56.5 ms: 1.07x faster                                                       |
| scimark_sor                | 125 ms                                                       | 117 ms: 1.06x faster                                                        |
| genshi_xml                 | 58.0 ms                                                      | 54.6 ms: 1.06x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.21 sec: 1.06x faster                                                      |
| nbody                      | 92.1 ms                                                      | 87.2 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                        |
| telco                      | 8.77 ms                                                      | 8.33 ms: 1.05x faster                                                       |
| richards                   | 52.5 ms                                                      | 50.3 ms: 1.04x faster                                                       |
| nqueens                    | 92.3 ms                                                      | 88.5 ms: 1.04x faster                                                       |
| hexiom                     | 6.47 ms                                                      | 6.21 ms: 1.04x faster                                                       |
| float                      | 81.6 ms                                                      | 78.3 ms: 1.04x faster                                                       |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 795 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 803 ms: 1.04x faster                                                        |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.97 sec: 1.02x faster                                                      |
| pprint_safe_repr           | 835 ms                                                       | 815 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.66 sec: 1.02x faster                                                      |
| coverage                   | 84.5 ms                                                      | 82.8 ms: 1.02x faster                                                       |
| html5lib                   | 72.9 ms                                                      | 71.5 ms: 1.02x faster                                                       |
| sympy_str                  | 297 ms                                                       | 291 ms: 1.02x faster                                                        |
| comprehensions             | 17.3 us                                                      | 17.0 us: 1.02x faster                                                       |
| sympy_integrate            | 23.4 ms                                                      | 23.0 ms: 1.02x faster                                                       |
| scimark_lu                 | 97.4 ms                                                      | 95.7 ms: 1.02x faster                                                       |
| regex_compile              | 143 ms                                                       | 140 ms: 1.02x faster                                                        |
| pickle_pure_python         | 322 us                                                       | 317 us: 1.01x faster                                                        |
| django_template            | 38.9 ms                                                      | 38.3 ms: 1.01x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 59.9 ms: 1.01x faster                                                       |
| sympy_expand               | 506 ms                                                       | 500 ms: 1.01x faster                                                        |
| logging_format             | 6.95 us                                                      | 6.87 us: 1.01x faster                                                       |
| mdp                        | 2.53 sec                                                     | 2.50 sec: 1.01x faster                                                      |
| spectral_norm              | 97.4 ms                                                      | 96.6 ms: 1.01x faster                                                       |
| async_generators           | 364 ms                                                       | 361 ms: 1.01x faster                                                        |
| gc_traversal               | 4.48 ms                                                      | 4.45 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 119 ms                                                       | 118 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 8.94 ms: 1.00x slower                                                       |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| crypto_pyaes               | 73.5 ms                                                      | 73.8 ms: 1.00x slower                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 85.6 ms: 1.00x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 59.0 ms: 1.01x slower                                                       |
| scimark_fft                | 298 ms                                                       | 300 ms: 1.01x slower                                                        |
| regex_dna                  | 238 ms                                                       | 241 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 1.79 ms: 1.01x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.01x slower                                                       |
| logging_simple             | 6.28 us                                                      | 6.37 us: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.29 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 216 us                                                       | 220 us: 1.02x slower                                                        |
| raytrace                   | 267 ms                                                       | 272 ms: 1.02x slower                                                        |
| logging_silent             | 97.5 ns                                                      | 99.3 ns: 1.02x slower                                                       |
| xml_etree_iterparse        | 99.8 ms                                                      | 102 ms: 1.02x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 25.5 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 66.8 ms: 1.03x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 67.3 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 1.41 ms: 1.03x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| chaos                      | 60.6 ms                                                      | 62.7 ms: 1.04x slower                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.64 ms: 1.04x slower                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.53 sec: 1.04x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (9): xml_etree_parse, typing_runtime_protocols, pyflate, deltablue, json_dumps, asyncio_websockets, mako, bench_mp_pool, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.036x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x