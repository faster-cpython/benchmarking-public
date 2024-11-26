# Results vs. 3.13.0

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.020x faster
- HPT reliability: 92.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 311 ms: 1.06x slower                                              |
| docutils       | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                            |
| html5lib       | 72.9 ms                                                      | 69.7 ms: 1.05x faster                                             |
| tornado_http   | 119 ms                                                       | 122 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                        | 1.04x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 390 ms: 1.17x faster                                              |
| async_tree_none            | 370 ms                                                       | 323 ms: 1.15x faster                                              |
| async_tree_memoization     | 447 ms                                                       | 403 ms: 1.11x faster                                              |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                              |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                              |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 574 ms: 1.04x faster                                              |
| async_tree_io              | 832 ms                                                       | 802 ms: 1.04x faster                                              |
| coroutines                 | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                             |
| async_generators           | 364 ms                                                       | 384 ms: 1.06x slower                                              |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                      |

Benchmark hidden because not significant (2): async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 81.5 ms: 1.13x faster                                             |
| float          | 81.6 ms                                                      | 73.8 ms: 1.10x faster                                             |
| pidigits       | 252 ms                                                       | 251 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                        | 1.08x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.39 ms: 1.04x faster                                             |
| regex_dna      | 238 ms                                                       | 233 ms: 1.02x faster                                              |
| regex_v8       | 24.9 ms                                                      | 25.5 ms: 1.02x slower                                             |
| regex_compile  | 143 ms                                                       | 149 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                        | 1.00x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|---------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads         | 2.43 sec                                                     | 2.12 sec: 1.15x faster                                            |
| xml_etree_process   | 60.7 ms                                                      | 55.9 ms: 1.09x faster                                             |
| xml_etree_generate  | 85.2 ms                                                      | 79.1 ms: 1.08x faster                                             |
| json_loads          | 24.7 us                                                      | 24.2 us: 1.02x faster                                             |
| json_dumps          | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                             |
| xml_etree_iterparse | 99.8 ms                                                      | 98.3 ms: 1.02x faster                                             |
| pickle_pure_python  | 322 us                                                       | 331 us: 1.03x slower                                              |
| Geometric mean      | (ref)                                                        | 1.04x faster                                                      |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                             |
| python_startup_no_site | 8.93 ms                                                      | 8.99 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.15 ms: 1.13x faster                                             |
| django_template | 38.9 ms                                                      | 43.3 ms: 1.12x slower                                             |
| genshi_text     | 27.2 ms                                                      | 31.1 ms: 1.14x slower                                             |
| genshi_xml      | 58.0 ms                                                      | 66.8 ms: 1.15x slower                                             |
| Geometric mean  | (ref)                                                        | 1.07x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 26.6 us: 1.46x faster                                             |
| create_gc_cycles           | 2.65 ms                                                      | 1.92 ms: 1.38x faster                                             |
| deepcopy                   | 388 us                                                       | 297 us: 1.31x faster                                              |
| spectral_norm              | 97.4 ms                                                      | 81.9 ms: 1.19x faster                                             |
| scimark_sor                | 125 ms                                                       | 105 ms: 1.19x faster                                              |
| deepcopy_reduce            | 3.49 us                                                      | 2.97 us: 1.18x faster                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 390 ms: 1.17x faster                                              |
| richards                   | 52.5 ms                                                      | 44.8 ms: 1.17x faster                                             |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                             |
| richards_super             | 60.2 ms                                                      | 52.3 ms: 1.15x faster                                             |
| tomli_loads                | 2.43 sec                                                     | 2.12 sec: 1.15x faster                                            |
| async_tree_none            | 370 ms                                                       | 323 ms: 1.15x faster                                              |
| nbody                      | 92.1 ms                                                      | 81.5 ms: 1.13x faster                                             |
| mako                       | 10.3 ms                                                      | 9.15 ms: 1.13x faster                                             |
| go                         | 167 ms                                                       | 149 ms: 1.12x faster                                              |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                             |
| async_tree_memoization     | 447 ms                                                       | 403 ms: 1.11x faster                                              |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 3.81 ms: 1.11x faster                                             |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                              |
| float                      | 81.6 ms                                                      | 73.8 ms: 1.10x faster                                             |
| xml_etree_process          | 60.7 ms                                                      | 55.9 ms: 1.09x faster                                             |
| xml_etree_generate         | 85.2 ms                                                      | 79.1 ms: 1.08x faster                                             |
| bpe_tokeniser              | 5.09 sec                                                     | 4.76 sec: 1.07x faster                                            |
| json                       | 5.62 ms                                                      | 5.26 ms: 1.07x faster                                             |
| fannkuch                   | 384 ms                                                       | 360 ms: 1.07x faster                                              |
| telco                      | 8.77 ms                                                      | 8.28 ms: 1.06x faster                                             |
| deltablue                  | 3.38 ms                                                      | 3.21 ms: 1.05x faster                                             |
| pprint_safe_repr           | 835 ms                                                       | 792 ms: 1.05x faster                                              |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                              |
| html5lib                   | 72.9 ms                                                      | 69.7 ms: 1.05x faster                                             |
| pyflate                    | 493 ms                                                       | 474 ms: 1.04x faster                                              |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 574 ms: 1.04x faster                                              |
| regex_effbot               | 3.51 ms                                                      | 3.39 ms: 1.04x faster                                             |
| async_tree_io              | 832 ms                                                       | 802 ms: 1.04x faster                                              |
| scimark_fft                | 298 ms                                                       | 288 ms: 1.04x faster                                              |
| thrift                     | 918 us                                                       | 887 us: 1.03x faster                                              |
| crypto_pyaes               | 73.5 ms                                                      | 71.3 ms: 1.03x faster                                             |
| coverage                   | 84.5 ms                                                      | 82.0 ms: 1.03x faster                                             |
| pprint_pformat             | 1.70 sec                                                     | 1.65 sec: 1.03x faster                                            |
| regex_dna                  | 238 ms                                                       | 233 ms: 1.02x faster                                              |
| json_loads                 | 24.7 us                                                      | 24.2 us: 1.02x faster                                             |
| dulwich_log                | 65.5 ms                                                      | 64.2 ms: 1.02x faster                                             |
| json_dumps                 | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                             |
| xml_etree_iterparse        | 99.8 ms                                                      | 98.3 ms: 1.02x faster                                             |
| gc_traversal               | 4.48 ms                                                      | 4.41 ms: 1.02x faster                                             |
| meteor_contest             | 130 ms                                                       | 129 ms: 1.01x faster                                              |
| pidigits                   | 252 ms                                                       | 251 ms: 1.01x faster                                              |
| python_startup_no_site     | 8.93 ms                                                      | 8.99 ms: 1.01x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                             |
| regex_v8                   | 24.9 ms                                                      | 25.5 ms: 1.02x slower                                             |
| pickle_pure_python         | 322 us                                                       | 331 us: 1.03x slower                                              |
| tornado_http               | 119 ms                                                       | 122 ms: 1.03x slower                                              |
| logging_silent             | 97.5 ns                                                      | 100 ns: 1.03x slower                                              |
| mdp                        | 2.53 sec                                                     | 2.60 sec: 1.03x slower                                            |
| logging_format             | 6.95 us                                                      | 7.17 us: 1.03x slower                                             |
| sympy_str                  | 297 ms                                                       | 308 ms: 1.04x slower                                              |
| sympy_expand               | 506 ms                                                       | 528 ms: 1.04x slower                                              |
| regex_compile              | 143 ms                                                       | 149 ms: 1.05x slower                                              |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.2 ms: 1.05x slower                                             |
| logging_simple             | 6.28 us                                                      | 6.61 us: 1.05x slower                                             |
| async_generators           | 364 ms                                                       | 384 ms: 1.06x slower                                              |
| typing_runtime_protocols   | 176 us                                                       | 186 us: 1.06x slower                                              |
| comprehensions             | 17.3 us                                                      | 18.3 us: 1.06x slower                                             |
| 2to3                       | 293 ms                                                       | 311 ms: 1.06x slower                                              |
| nqueens                    | 92.3 ms                                                      | 98.3 ms: 1.06x slower                                             |
| hexiom                     | 6.47 ms                                                      | 6.92 ms: 1.07x slower                                             |
| bench_mp_pool              | 4.82 ms                                                      | 5.21 ms: 1.08x slower                                             |
| sqlglot_parse              | 1.37 ms                                                      | 1.49 ms: 1.09x slower                                             |
| sympy_sum                  | 154 ms                                                       | 168 ms: 1.09x slower                                              |
| chaos                      | 60.6 ms                                                      | 66.1 ms: 1.09x slower                                             |
| sqlglot_normalize          | 119 ms                                                       | 131 ms: 1.10x slower                                              |
| sqlglot_transpile          | 1.76 ms                                                      | 1.95 ms: 1.11x slower                                             |
| django_template            | 38.9 ms                                                      | 43.3 ms: 1.12x slower                                             |
| sqlglot_optimize           | 58.7 ms                                                      | 65.7 ms: 1.12x slower                                             |
| sympy_integrate            | 23.4 ms                                                      | 26.4 ms: 1.13x slower                                             |
| docutils                   | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                            |
| genshi_text                | 27.2 ms                                                      | 31.1 ms: 1.14x slower                                             |
| genshi_xml                 | 58.0 ms                                                      | 66.8 ms: 1.15x slower                                             |
| pylint                     | 345 ms                                                       | 410 ms: 1.19x slower                                              |
| raytrace                   | 267 ms                                                       | 318 ms: 1.19x slower                                              |
| generators                 | 33.9 ms                                                      | 42.5 ms: 1.25x slower                                             |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                      |

Benchmark hidden because not significant (7): async_tree_io_tg, bench_thread_pool, asyncio_websockets, xml_etree_parse, scimark_lu, unpickle_pure_python, pycparser
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.020x faster
# HPT report

- Reliability score: 92.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x