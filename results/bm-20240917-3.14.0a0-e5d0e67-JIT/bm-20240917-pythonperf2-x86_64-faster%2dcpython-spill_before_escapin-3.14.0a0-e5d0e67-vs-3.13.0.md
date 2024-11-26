# Results vs. 3.13.0

- fork: faster-cpython
- ref: spill_before_escapin
- machine: linux-x86_64
- commit hash: e5d0e67
- commit date: 2024-09-17
- overall geometric mean: 1.021x faster
- HPT reliability: 94.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 310 ms: 1.06x slower                                                                  |
| docutils       | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                                                |
| html5lib       | 72.9 ms                                                      | 72.0 ms: 1.01x faster                                                                 |
| tornado_http   | 119 ms                                                       | 122 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 391 ms: 1.17x faster                                                                  |
| async_tree_none            | 370 ms                                                       | 325 ms: 1.14x faster                                                                  |
| async_tree_none_tg         | 342 ms                                                       | 310 ms: 1.10x faster                                                                  |
| async_tree_memoization     | 447 ms                                                       | 406 ms: 1.10x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                                  |
| async_tree_io_tg           | 823 ms                                                       | 791 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 579 ms: 1.03x faster                                                                  |
| async_tree_io              | 832 ms                                                       | 814 ms: 1.02x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.6 ms: 1.00x slower                                                                 |
| async_generators           | 364 ms                                                       | 386 ms: 1.06x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 78.2 ms: 1.18x faster                                                                 |
| float          | 81.6 ms                                                      | 76.7 ms: 1.06x faster                                                                 |
| pidigits       | 252 ms                                                       | 250 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.58 ms: 1.02x slower                                                                 |
| regex_compile  | 143 ms                                                       | 148 ms: 1.04x slower                                                                  |
| regex_v8       | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                                                 |
| regex_dna      | 238 ms                                                       | 252 ms: 1.06x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.13 sec: 1.14x faster                                                                |
| xml_etree_process    | 60.7 ms                                                      | 55.8 ms: 1.09x faster                                                                 |
| xml_etree_generate   | 85.2 ms                                                      | 80.7 ms: 1.06x faster                                                                 |
| json_loads           | 24.7 us                                                      | 23.9 us: 1.03x faster                                                                 |
| json_dumps           | 10.8 ms                                                      | 10.5 ms: 1.03x faster                                                                 |
| xml_etree_iterparse  | 99.8 ms                                                      | 97.8 ms: 1.02x faster                                                                 |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                                  |
| unpickle_pure_python | 216 us                                                       | 215 us: 1.01x faster                                                                  |
| pickle_pure_python   | 322 us                                                       | 325 us: 1.01x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                                 |
| python_startup_no_site | 8.93 ms                                                      | 8.99 ms: 1.01x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.23 ms: 1.12x faster                                                                 |
| genshi_text     | 27.2 ms                                                      | 29.9 ms: 1.10x slower                                                                 |
| genshi_xml      | 58.0 ms                                                      | 65.0 ms: 1.12x slower                                                                 |
| django_template | 38.9 ms                                                      | 43.6 ms: 1.12x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.89 ms: 1.40x faster                                                                 |
| deepcopy_memo              | 38.9 us                                                      | 28.3 us: 1.37x faster                                                                 |
| deepcopy                   | 388 us                                                       | 300 us: 1.30x faster                                                                  |
| richards                   | 52.5 ms                                                      | 42.8 ms: 1.23x faster                                                                 |
| scimark_sor                | 125 ms                                                       | 103 ms: 1.22x faster                                                                  |
| spectral_norm              | 97.4 ms                                                      | 80.4 ms: 1.21x faster                                                                 |
| richards_super             | 60.2 ms                                                      | 49.7 ms: 1.21x faster                                                                 |
| nbody                      | 92.1 ms                                                      | 78.2 ms: 1.18x faster                                                                 |
| async_tree_memoization_tg  | 458 ms                                                       | 391 ms: 1.17x faster                                                                  |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                                 |
| deepcopy_reduce            | 3.49 us                                                      | 2.99 us: 1.17x faster                                                                 |
| tomli_loads                | 2.43 sec                                                     | 2.13 sec: 1.14x faster                                                                |
| async_tree_none            | 370 ms                                                       | 325 ms: 1.14x faster                                                                  |
| mako                       | 10.3 ms                                                      | 9.23 ms: 1.12x faster                                                                 |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                                 |
| async_tree_none_tg         | 342 ms                                                       | 310 ms: 1.10x faster                                                                  |
| go                         | 167 ms                                                       | 151 ms: 1.10x faster                                                                  |
| async_tree_memoization     | 447 ms                                                       | 406 ms: 1.10x faster                                                                  |
| telco                      | 8.77 ms                                                      | 8.01 ms: 1.09x faster                                                                 |
| xml_etree_process          | 60.7 ms                                                      | 55.8 ms: 1.09x faster                                                                 |
| json                       | 5.62 ms                                                      | 5.22 ms: 1.08x faster                                                                 |
| fannkuch                   | 384 ms                                                       | 357 ms: 1.08x faster                                                                  |
| crypto_pyaes               | 73.5 ms                                                      | 68.8 ms: 1.07x faster                                                                 |
| float                      | 81.6 ms                                                      | 76.7 ms: 1.06x faster                                                                 |
| deltablue                  | 3.38 ms                                                      | 3.19 ms: 1.06x faster                                                                 |
| bpe_tokeniser              | 5.09 sec                                                     | 4.80 sec: 1.06x faster                                                                |
| xml_etree_generate         | 85.2 ms                                                      | 80.7 ms: 1.06x faster                                                                 |
| pprint_safe_repr           | 835 ms                                                       | 797 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                                  |
| async_tree_io_tg           | 823 ms                                                       | 791 ms: 1.04x faster                                                                  |
| coverage                   | 84.5 ms                                                      | 81.2 ms: 1.04x faster                                                                 |
| scimark_fft                | 298 ms                                                       | 288 ms: 1.04x faster                                                                  |
| pyflate                    | 493 ms                                                       | 476 ms: 1.03x faster                                                                  |
| json_loads                 | 24.7 us                                                      | 23.9 us: 1.03x faster                                                                 |
| json_dumps                 | 10.8 ms                                                      | 10.5 ms: 1.03x faster                                                                 |
| thrift                     | 918 us                                                       | 892 us: 1.03x faster                                                                  |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 579 ms: 1.03x faster                                                                  |
| gc_traversal               | 4.48 ms                                                      | 4.36 ms: 1.03x faster                                                                 |
| pprint_pformat             | 1.70 sec                                                     | 1.66 sec: 1.03x faster                                                                |
| async_tree_io              | 832 ms                                                       | 814 ms: 1.02x faster                                                                  |
| xml_etree_iterparse        | 99.8 ms                                                      | 97.8 ms: 1.02x faster                                                                 |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                                  |
| scimark_lu                 | 97.4 ms                                                      | 96.3 ms: 1.01x faster                                                                 |
| html5lib                   | 72.9 ms                                                      | 72.0 ms: 1.01x faster                                                                 |
| pycparser                  | 1.28 sec                                                     | 1.27 sec: 1.01x faster                                                                |
| pidigits                   | 252 ms                                                       | 250 ms: 1.01x faster                                                                  |
| dulwich_log                | 65.5 ms                                                      | 65.0 ms: 1.01x faster                                                                 |
| unpickle_pure_python       | 216 us                                                       | 215 us: 1.01x faster                                                                  |
| meteor_contest             | 130 ms                                                       | 130 ms: 1.00x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.6 ms: 1.00x slower                                                                 |
| python_startup_no_site     | 8.93 ms                                                      | 8.99 ms: 1.01x slower                                                                 |
| pickle_pure_python         | 322 us                                                       | 325 us: 1.01x slower                                                                  |
| mdp                        | 2.53 sec                                                     | 2.55 sec: 1.01x slower                                                                |
| regex_effbot               | 3.51 ms                                                      | 3.58 ms: 1.02x slower                                                                 |
| tornado_http               | 119 ms                                                       | 122 ms: 1.03x slower                                                                  |
| regex_compile              | 143 ms                                                       | 148 ms: 1.04x slower                                                                  |
| sympy_expand               | 506 ms                                                       | 525 ms: 1.04x slower                                                                  |
| logging_format             | 6.95 us                                                      | 7.21 us: 1.04x slower                                                                 |
| scimark_monte_carlo        | 65.2 ms                                                      | 67.7 ms: 1.04x slower                                                                 |
| typing_runtime_protocols   | 176 us                                                       | 184 us: 1.05x slower                                                                  |
| logging_silent             | 97.5 ns                                                      | 102 ns: 1.05x slower                                                                  |
| comprehensions             | 17.3 us                                                      | 18.2 us: 1.05x slower                                                                 |
| logging_simple             | 6.28 us                                                      | 6.60 us: 1.05x slower                                                                 |
| regex_v8                   | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                                                 |
| sympy_str                  | 297 ms                                                       | 313 ms: 1.05x slower                                                                  |
| 2to3                       | 293 ms                                                       | 310 ms: 1.06x slower                                                                  |
| regex_dna                  | 238 ms                                                       | 252 ms: 1.06x slower                                                                  |
| async_generators           | 364 ms                                                       | 386 ms: 1.06x slower                                                                  |
| sqlglot_normalize          | 119 ms                                                       | 127 ms: 1.07x slower                                                                  |
| bench_mp_pool              | 4.82 ms                                                      | 5.19 ms: 1.08x slower                                                                 |
| hexiom                     | 6.47 ms                                                      | 6.99 ms: 1.08x slower                                                                 |
| sqlglot_parse              | 1.37 ms                                                      | 1.49 ms: 1.09x slower                                                                 |
| nqueens                    | 92.3 ms                                                      | 101 ms: 1.09x slower                                                                  |
| chaos                      | 60.6 ms                                                      | 66.4 ms: 1.10x slower                                                                 |
| sqlglot_optimize           | 58.7 ms                                                      | 64.5 ms: 1.10x slower                                                                 |
| genshi_text                | 27.2 ms                                                      | 29.9 ms: 1.10x slower                                                                 |
| generators                 | 33.9 ms                                                      | 37.3 ms: 1.10x slower                                                                 |
| sqlglot_transpile          | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                                 |
| sympy_sum                  | 154 ms                                                       | 170 ms: 1.10x slower                                                                  |
| genshi_xml                 | 58.0 ms                                                      | 65.0 ms: 1.12x slower                                                                 |
| django_template            | 38.9 ms                                                      | 43.6 ms: 1.12x slower                                                                 |
| docutils                   | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                                                |
| sympy_integrate            | 23.4 ms                                                      | 26.7 ms: 1.14x slower                                                                 |
| pylint                     | 345 ms                                                       | 411 ms: 1.19x slower                                                                  |
| raytrace                   | 267 ms                                                       | 328 ms: 1.23x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (3): bench_thread_pool, asyncio_websockets, scimark_sparse_mat_mult
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240917-3.14.0a0-e5d0e67-JIT/bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.021x faster
# HPT report

- Reliability score: 94.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x