# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.001x slower
- HPT reliability: 53.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 317 ms: 1.08x slower                                                          |
| docutils       | 2.81 sec                                                     | 3.21 sec: 1.14x slower                                                        |
| html5lib       | 72.9 ms                                                      | 70.3 ms: 1.04x faster                                                         |
| sphinx         | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                        |
| tornado_http   | 119 ms                                                       | 124 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 373 ms: 1.23x faster                                                          |
| async_tree_none            | 370 ms                                                       | 333 ms: 1.11x faster                                                          |
| async_tree_memoization     | 447 ms                                                       | 408 ms: 1.10x faster                                                          |
| async_tree_none_tg         | 342 ms                                                       | 320 ms: 1.07x faster                                                          |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 576 ms: 1.03x faster                                                          |
| asyncio_websockets         | 395 ms                                                       | 383 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 559 ms: 1.03x faster                                                          |
| async_tree_io_tg           | 823 ms                                                       | 857 ms: 1.04x slower                                                          |
| async_generators           | 364 ms                                                       | 380 ms: 1.05x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                  |

Benchmark hidden because not significant (2): async_tree_io, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 84.6 ms: 1.09x faster                                                         |
| float          | 81.6 ms                                                      | 78.7 ms: 1.04x faster                                                         |
| pidigits       | 252 ms                                                       | 252 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 231 ms: 1.03x faster                                                          |
| regex_effbot   | 3.51 ms                                                      | 3.42 ms: 1.03x faster                                                         |
| regex_compile  | 143 ms                                                       | 153 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.13 sec: 1.14x faster                                                        |
| xml_etree_process    | 60.7 ms                                                      | 56.9 ms: 1.07x faster                                                         |
| xml_etree_generate   | 85.2 ms                                                      | 81.4 ms: 1.05x faster                                                         |
| json_loads           | 24.7 us                                                      | 24.1 us: 1.03x faster                                                         |
| json_dumps           | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                                         |
| unpickle_pure_python | 216 us                                                       | 223 us: 1.03x slower                                                          |
| pickle_pure_python   | 322 us                                                       | 332 us: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 15.0 ms: 1.04x faster                                                         |
| python_startup_no_site | 8.93 ms                                                      | 9.02 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.57 ms: 1.08x faster                                                         |
| genshi_text     | 27.2 ms                                                      | 28.8 ms: 1.06x slower                                                         |
| genshi_xml      | 58.0 ms                                                      | 63.0 ms: 1.09x slower                                                         |
| django_template | 38.9 ms                                                      | 42.7 ms: 1.10x slower                                                         |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 29.7 us: 1.31x faster                                                         |
| async_tree_memoization_tg  | 458 ms                                                       | 373 ms: 1.23x faster                                                          |
| deepcopy                   | 388 us                                                       | 319 us: 1.22x faster                                                          |
| richards_super             | 60.2 ms                                                      | 49.8 ms: 1.21x faster                                                         |
| scimark_sor                | 125 ms                                                       | 104 ms: 1.21x faster                                                          |
| richards                   | 52.5 ms                                                      | 44.5 ms: 1.18x faster                                                         |
| tomli_loads                | 2.43 sec                                                     | 2.13 sec: 1.14x faster                                                        |
| telco                      | 8.77 ms                                                      | 7.74 ms: 1.13x faster                                                         |
| deepcopy_reduce            | 3.49 us                                                      | 3.11 us: 1.12x faster                                                         |
| json                       | 5.62 ms                                                      | 5.03 ms: 1.12x faster                                                         |
| async_tree_none            | 370 ms                                                       | 333 ms: 1.11x faster                                                          |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 408 ms: 1.10x faster                                                          |
| nbody                      | 92.1 ms                                                      | 84.6 ms: 1.09x faster                                                         |
| mako                       | 10.3 ms                                                      | 9.57 ms: 1.08x faster                                                         |
| pyflate                    | 493 ms                                                       | 460 ms: 1.07x faster                                                          |
| async_tree_none_tg         | 342 ms                                                       | 320 ms: 1.07x faster                                                          |
| go                         | 167 ms                                                       | 156 ms: 1.07x faster                                                          |
| xml_etree_process          | 60.7 ms                                                      | 56.9 ms: 1.07x faster                                                         |
| logging_silent             | 97.5 ns                                                      | 91.4 ns: 1.07x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.77 sec: 1.07x faster                                                        |
| coverage                   | 84.5 ms                                                      | 79.8 ms: 1.06x faster                                                         |
| pprint_safe_repr           | 835 ms                                                       | 788 ms: 1.06x faster                                                          |
| fannkuch                   | 384 ms                                                       | 364 ms: 1.06x faster                                                          |
| pprint_pformat             | 1.70 sec                                                     | 1.61 sec: 1.05x faster                                                        |
| xml_etree_generate         | 85.2 ms                                                      | 81.4 ms: 1.05x faster                                                         |
| spectral_norm              | 97.4 ms                                                      | 93.3 ms: 1.04x faster                                                         |
| python_startup             | 15.6 ms                                                      | 15.0 ms: 1.04x faster                                                         |
| float                      | 81.6 ms                                                      | 78.7 ms: 1.04x faster                                                         |
| html5lib                   | 72.9 ms                                                      | 70.3 ms: 1.04x faster                                                         |
| scimark_fft                | 298 ms                                                       | 288 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 576 ms: 1.03x faster                                                          |
| asyncio_websockets         | 395 ms                                                       | 383 ms: 1.03x faster                                                          |
| regex_dna                  | 238 ms                                                       | 231 ms: 1.03x faster                                                          |
| crypto_pyaes               | 73.5 ms                                                      | 71.4 ms: 1.03x faster                                                         |
| regex_effbot               | 3.51 ms                                                      | 3.42 ms: 1.03x faster                                                         |
| scimark_lu                 | 97.4 ms                                                      | 94.7 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 559 ms: 1.03x faster                                                          |
| json_loads                 | 24.7 us                                                      | 24.1 us: 1.03x faster                                                         |
| deltablue                  | 3.38 ms                                                      | 3.30 ms: 1.02x faster                                                         |
| thrift                     | 918 us                                                       | 898 us: 1.02x faster                                                          |
| dulwich_log                | 65.5 ms                                                      | 65.0 ms: 1.01x faster                                                         |
| pidigits                   | 252 ms                                                       | 252 ms: 1.00x faster                                                          |
| python_startup_no_site     | 8.93 ms                                                      | 9.02 ms: 1.01x slower                                                         |
| logging_format             | 6.95 us                                                      | 7.04 us: 1.01x slower                                                         |
| pycparser                  | 1.28 sec                                                     | 1.30 sec: 1.02x slower                                                        |
| bench_thread_pool          | 929 us                                                       | 955 us: 1.03x slower                                                          |
| json_dumps                 | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                                         |
| unpickle_pure_python       | 216 us                                                       | 223 us: 1.03x slower                                                          |
| pickle_pure_python         | 322 us                                                       | 332 us: 1.03x slower                                                          |
| mdp                        | 2.53 sec                                                     | 2.62 sec: 1.03x slower                                                        |
| meteor_contest             | 130 ms                                                       | 135 ms: 1.04x slower                                                          |
| typing_runtime_protocols   | 176 us                                                       | 182 us: 1.04x slower                                                          |
| logging_simple             | 6.28 us                                                      | 6.53 us: 1.04x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 857 ms: 1.04x slower                                                          |
| tornado_http               | 119 ms                                                       | 124 ms: 1.04x slower                                                          |
| async_generators           | 364 ms                                                       | 380 ms: 1.05x slower                                                          |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.41 ms: 1.05x slower                                                         |
| sympy_expand               | 506 ms                                                       | 535 ms: 1.06x slower                                                          |
| genshi_text                | 27.2 ms                                                      | 28.8 ms: 1.06x slower                                                         |
| scimark_monte_carlo        | 65.2 ms                                                      | 69.7 ms: 1.07x slower                                                         |
| regex_compile              | 143 ms                                                       | 153 ms: 1.08x slower                                                          |
| comprehensions             | 17.3 us                                                      | 18.6 us: 1.08x slower                                                         |
| chaos                      | 60.6 ms                                                      | 65.2 ms: 1.08x slower                                                         |
| 2to3                       | 293 ms                                                       | 317 ms: 1.08x slower                                                          |
| genshi_xml                 | 58.0 ms                                                      | 63.0 ms: 1.09x slower                                                         |
| sympy_str                  | 297 ms                                                       | 322 ms: 1.09x slower                                                          |
| nqueens                    | 92.3 ms                                                      | 101 ms: 1.10x slower                                                          |
| django_template            | 38.9 ms                                                      | 42.7 ms: 1.10x slower                                                         |
| create_gc_cycles           | 2.65 ms                                                      | 2.92 ms: 1.10x slower                                                         |
| sqlglot_parse              | 1.37 ms                                                      | 1.51 ms: 1.11x slower                                                         |
| hexiom                     | 6.47 ms                                                      | 7.18 ms: 1.11x slower                                                         |
| raytrace                   | 267 ms                                                       | 299 ms: 1.12x slower                                                          |
| sqlglot_normalize          | 119 ms                                                       | 133 ms: 1.12x slower                                                          |
| sqlglot_transpile          | 1.76 ms                                                      | 1.98 ms: 1.12x slower                                                         |
| sphinx                     | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.21 sec: 1.14x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 176 ms: 1.15x slower                                                          |
| generators                 | 33.9 ms                                                      | 38.9 ms: 1.15x slower                                                         |
| sympy_integrate            | 23.4 ms                                                      | 27.6 ms: 1.18x slower                                                         |
| sqlglot_optimize           | 58.7 ms                                                      | 69.9 ms: 1.19x slower                                                         |
| gc_traversal               | 4.48 ms                                                      | 5.35 ms: 1.20x slower                                                         |
| pylint                     | 345 ms                                                       | 425 ms: 1.23x slower                                                          |
| bench_mp_pool              | 4.82 ms                                                      | 3.14 sec: 652.19x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                                  |

Benchmark hidden because not significant (5): async_tree_io, xml_etree_parse, regex_v8, xml_etree_iterparse, coroutines
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 53.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x