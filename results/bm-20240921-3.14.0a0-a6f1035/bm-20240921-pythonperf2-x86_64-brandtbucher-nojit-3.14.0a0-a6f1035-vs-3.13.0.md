# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.029x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                               |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                             |
| html5lib       | 72.9 ms                                                      | 70.9 ms: 1.03x faster                                              |
| tornado_http   | 119 ms                                                       | 116 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                        | 1.01x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 389 ms: 1.18x faster                                               |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                               |
| async_tree_memoization     | 447 ms                                                       | 397 ms: 1.13x faster                                               |
| async_tree_none_tg         | 342 ms                                                       | 307 ms: 1.11x faster                                               |
| async_tree_io_tg           | 823 ms                                                       | 774 ms: 1.06x faster                                               |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 569 ms: 1.05x faster                                               |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 559 ms: 1.03x faster                                               |
| async_generators           | 364 ms                                                       | 362 ms: 1.00x faster                                               |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.02x slower                                              |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                       |

Benchmark hidden because not significant (2): async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 89.1 ms: 1.03x faster                                              |
| float          | 81.6 ms                                                      | 79.6 ms: 1.02x faster                                              |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                        | 1.02x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.03x faster                                               |
| regex_dna      | 238 ms                                                       | 237 ms: 1.01x faster                                               |
| regex_v8       | 24.9 ms                                                      | 25.0 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                        | 1.01x faster                                                       |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|---------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_process   | 60.7 ms                                                      | 59.2 ms: 1.03x faster                                              |
| xml_etree_generate  | 85.2 ms                                                      | 84.8 ms: 1.01x faster                                              |
| json_dumps          | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                              |
| xml_etree_parse     | 144 ms                                                       | 145 ms: 1.01x slower                                               |
| xml_etree_iterparse | 99.8 ms                                                      | 101 ms: 1.02x slower                                               |
| tomli_loads         | 2.43 sec                                                     | 2.58 sec: 1.06x slower                                             |
| Geometric mean      | (ref)                                                        | 1.01x slower                                                       |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                              |
| python_startup_no_site | 8.93 ms                                                      | 8.98 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.8 ms: 1.10x faster                                              |
| genshi_xml      | 58.0 ms                                                      | 55.4 ms: 1.05x faster                                              |
| django_template | 38.9 ms                                                      | 39.6 ms: 1.02x slower                                              |
| mako            | 10.3 ms                                                      | 10.6 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 291 us: 1.33x faster                                               |
| create_gc_cycles           | 2.65 ms                                                      | 1.99 ms: 1.33x faster                                              |
| deepcopy_memo              | 38.9 us                                                      | 30.1 us: 1.29x faster                                              |
| go                         | 167 ms                                                       | 135 ms: 1.24x faster                                               |
| generators                 | 33.9 ms                                                      | 28.8 ms: 1.18x faster                                              |
| async_tree_memoization_tg  | 458 ms                                                       | 389 ms: 1.18x faster                                               |
| deepcopy_reduce            | 3.49 us                                                      | 2.97 us: 1.17x faster                                              |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                              |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                               |
| async_tree_memoization     | 447 ms                                                       | 397 ms: 1.13x faster                                               |
| async_tree_none_tg         | 342 ms                                                       | 307 ms: 1.11x faster                                               |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                              |
| genshi_text                | 27.2 ms                                                      | 24.8 ms: 1.10x faster                                              |
| richards_super             | 60.2 ms                                                      | 55.8 ms: 1.08x faster                                              |
| json                       | 5.62 ms                                                      | 5.23 ms: 1.07x faster                                              |
| async_tree_io_tg           | 823 ms                                                       | 774 ms: 1.06x faster                                               |
| fannkuch                   | 384 ms                                                       | 365 ms: 1.05x faster                                               |
| richards                   | 52.5 ms                                                      | 50.0 ms: 1.05x faster                                              |
| thrift                     | 918 us                                                       | 875 us: 1.05x faster                                               |
| genshi_xml                 | 58.0 ms                                                      | 55.4 ms: 1.05x faster                                              |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 569 ms: 1.05x faster                                               |
| pycparser                  | 1.28 sec                                                     | 1.23 sec: 1.04x faster                                             |
| bench_mp_pool              | 4.82 ms                                                      | 4.63 ms: 1.04x faster                                              |
| bench_thread_pool          | 929 us                                                       | 894 us: 1.04x faster                                               |
| telco                      | 8.77 ms                                                      | 8.45 ms: 1.04x faster                                              |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                               |
| nbody                      | 92.1 ms                                                      | 89.1 ms: 1.03x faster                                              |
| hexiom                     | 6.47 ms                                                      | 6.26 ms: 1.03x faster                                              |
| bpe_tokeniser              | 5.09 sec                                                     | 4.94 sec: 1.03x faster                                             |
| tornado_http               | 119 ms                                                       | 116 ms: 1.03x faster                                               |
| html5lib                   | 72.9 ms                                                      | 70.9 ms: 1.03x faster                                              |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.03x faster                                               |
| regex_compile              | 143 ms                                                       | 139 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 559 ms: 1.03x faster                                               |
| xml_etree_process          | 60.7 ms                                                      | 59.2 ms: 1.03x faster                                              |
| pprint_safe_repr           | 835 ms                                                       | 815 ms: 1.03x faster                                               |
| float                      | 81.6 ms                                                      | 79.6 ms: 1.02x faster                                              |
| sympy_expand               | 506 ms                                                       | 497 ms: 1.02x faster                                               |
| pyflate                    | 493 ms                                                       | 483 ms: 1.02x faster                                               |
| typing_runtime_protocols   | 176 us                                                       | 172 us: 1.02x faster                                               |
| sympy_str                  | 297 ms                                                       | 291 ms: 1.02x faster                                               |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                               |
| sympy_integrate            | 23.4 ms                                                      | 23.1 ms: 1.01x faster                                              |
| pprint_pformat             | 1.70 sec                                                     | 1.68 sec: 1.01x faster                                             |
| nqueens                    | 92.3 ms                                                      | 91.4 ms: 1.01x faster                                              |
| regex_dna                  | 238 ms                                                       | 237 ms: 1.01x faster                                               |
| mdp                        | 2.53 sec                                                     | 2.51 sec: 1.01x faster                                             |
| xml_etree_generate         | 85.2 ms                                                      | 84.8 ms: 1.01x faster                                              |
| async_generators           | 364 ms                                                       | 362 ms: 1.00x faster                                               |
| regex_v8                   | 24.9 ms                                                      | 25.0 ms: 1.00x slower                                              |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                               |
| sqlglot_normalize          | 119 ms                                                       | 119 ms: 1.00x slower                                               |
| python_startup_no_site     | 8.93 ms                                                      | 8.98 ms: 1.01x slower                                              |
| sqlglot_optimize           | 58.7 ms                                                      | 59.1 ms: 1.01x slower                                              |
| json_dumps                 | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                              |
| deltablue                  | 3.38 ms                                                      | 3.42 ms: 1.01x slower                                              |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                               |
| dulwich_log                | 65.5 ms                                                      | 66.5 ms: 1.01x slower                                              |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.02x slower                                               |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.02x slower                                              |
| coverage                   | 84.5 ms                                                      | 86.1 ms: 1.02x slower                                              |
| scimark_lu                 | 97.4 ms                                                      | 99.2 ms: 1.02x slower                                              |
| django_template            | 38.9 ms                                                      | 39.6 ms: 1.02x slower                                              |
| mako                       | 10.3 ms                                                      | 10.6 ms: 1.02x slower                                              |
| comprehensions             | 17.3 us                                                      | 17.7 us: 1.02x slower                                              |
| raytrace                   | 267 ms                                                       | 275 ms: 1.03x slower                                               |
| logging_format             | 6.95 us                                                      | 7.15 us: 1.03x slower                                              |
| logging_silent             | 97.5 ns                                                      | 100 ns: 1.03x slower                                               |
| scimark_fft                | 298 ms                                                       | 307 ms: 1.03x slower                                               |
| sqlglot_transpile          | 1.76 ms                                                      | 1.81 ms: 1.03x slower                                              |
| scimark_sor                | 125 ms                                                       | 129 ms: 1.03x slower                                               |
| chaos                      | 60.6 ms                                                      | 62.5 ms: 1.03x slower                                              |
| scimark_monte_carlo        | 65.2 ms                                                      | 67.4 ms: 1.03x slower                                              |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.40 ms: 1.05x slower                                              |
| sqlglot_parse              | 1.37 ms                                                      | 1.43 ms: 1.05x slower                                              |
| logging_simple             | 6.28 us                                                      | 6.58 us: 1.05x slower                                              |
| gc_traversal               | 4.48 ms                                                      | 4.70 ms: 1.05x slower                                              |
| tomli_loads                | 2.43 sec                                                     | 2.58 sec: 1.06x slower                                             |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                       |

Benchmark hidden because not significant (9): async_tree_io, asyncio_websockets, crypto_pyaes, regex_effbot, unpickle_pure_python, spectral_norm, json_loads, pickle_pure_python, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.029x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x