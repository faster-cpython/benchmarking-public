# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: f072492
- commit date: 2024-10-04
- overall geometric mean: 1.035x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 257 ms: 1.04x faster                                           |
| docutils       | 2.59 sec                                               | 2.63 sec: 1.01x slower                                         |
| html5lib       | 64.2 ms                                                | 62.3 ms: 1.03x faster                                          |
| tornado_http   | 92.4 ms                                                | 91.1 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 383 ms: 1.21x faster                                           |
| async_tree_none            | 351 ms                                                 | 310 ms: 1.13x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 398 ms: 1.11x faster                                           |
| async_tree_none_tg         | 321 ms                                                 | 299 ms: 1.07x faster                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 524 ms: 1.04x faster                                           |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                          |
| async_tree_io_tg           | 857 ms                                                 | 891 ms: 1.04x slower                                           |
| async_tree_io              | 842 ms                                                 | 888 ms: 1.06x slower                                           |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                   |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 79.2 ms                                                | 77.5 ms: 1.02x faster                                          |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                           |
| nbody          | 87.0 ms                                                | 89.0 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                  | 1.00x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.54 ms: 1.05x faster                                          |
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.05x faster                                          |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                           |
| regex_dna      | 218 ms                                                 | 227 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads         | 2.14 sec                                               | 2.07 sec: 1.03x faster                                         |
| json_dumps          | 10.6 ms                                                | 10.3 ms: 1.03x faster                                          |
| xml_etree_process   | 60.6 ms                                                | 59.0 ms: 1.03x faster                                          |
| pickle_pure_python  | 310 us                                                 | 306 us: 1.02x faster                                           |
| json_loads          | 27.2 us                                                | 26.9 us: 1.01x faster                                          |
| xml_etree_generate  | 86.7 ms                                                | 86.3 ms: 1.01x faster                                          |
| xml_etree_iterparse | 101 ms                                                 | 105 ms: 1.04x slower                                           |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.2 ms: 1.12x faster                                          |
| python_startup_no_site | 6.96 ms                                                | 7.38 ms: 1.06x slower                                          |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.5 ms: 1.05x faster                                          |
| django_template | 35.2 ms                                                | 33.8 ms: 1.04x faster                                          |
| genshi_xml      | 50.9 ms                                                | 50.1 ms: 1.02x faster                                          |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                          |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.75 ms: 1.37x faster                                          |
| deepcopy                   | 358 us                                                 | 262 us: 1.37x faster                                           |
| deepcopy_memo              | 39.1 us                                                | 29.5 us: 1.33x faster                                          |
| async_tree_memoization_tg  | 464 ms                                                 | 383 ms: 1.21x faster                                           |
| go                         | 144 ms                                                 | 119 ms: 1.20x faster                                           |
| gc_traversal               | 4.37 ms                                                | 3.68 ms: 1.19x faster                                          |
| deepcopy_reduce            | 3.20 us                                                | 2.70 us: 1.18x faster                                          |
| async_tree_none            | 351 ms                                                 | 310 ms: 1.13x faster                                           |
| python_startup             | 12.5 ms                                                | 11.2 ms: 1.12x faster                                          |
| async_tree_memoization     | 442 ms                                                 | 398 ms: 1.11x faster                                           |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.10x faster                                          |
| mdp                        | 2.72 sec                                               | 2.52 sec: 1.08x faster                                         |
| crypto_pyaes               | 75.3 ms                                                | 69.9 ms: 1.08x faster                                          |
| async_tree_none_tg         | 321 ms                                                 | 299 ms: 1.07x faster                                           |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                         |
| json                       | 5.36 ms                                                | 5.03 ms: 1.07x faster                                          |
| telco                      | 8.54 ms                                                | 8.04 ms: 1.06x faster                                          |
| thrift                     | 809 us                                                 | 767 us: 1.05x faster                                           |
| regex_effbot               | 3.73 ms                                                | 3.54 ms: 1.05x faster                                          |
| richards                   | 48.7 ms                                                | 46.3 ms: 1.05x faster                                          |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.05x faster                                           |
| genshi_text                | 23.5 ms                                                | 22.5 ms: 1.05x faster                                          |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.05x faster                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 524 ms: 1.04x faster                                           |
| typing_runtime_protocols   | 165 us                                                 | 158 us: 1.04x faster                                           |
| richards_super             | 54.9 ms                                                | 52.6 ms: 1.04x faster                                          |
| django_template            | 35.2 ms                                                | 33.8 ms: 1.04x faster                                          |
| 2to3                       | 267 ms                                                 | 257 ms: 1.04x faster                                           |
| tomli_loads                | 2.14 sec                                               | 2.07 sec: 1.03x faster                                         |
| html5lib                   | 64.2 ms                                                | 62.3 ms: 1.03x faster                                          |
| generators                 | 29.0 ms                                                | 28.1 ms: 1.03x faster                                          |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                           |
| json_dumps                 | 10.6 ms                                                | 10.3 ms: 1.03x faster                                          |
| logging_format             | 6.40 us                                                | 6.22 us: 1.03x faster                                          |
| xml_etree_process          | 60.6 ms                                                | 59.0 ms: 1.03x faster                                          |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                           |
| sympy_str                  | 275 ms                                                 | 268 ms: 1.03x faster                                           |
| logging_simple             | 5.72 us                                                | 5.58 us: 1.03x faster                                          |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.92 ms: 1.03x faster                                          |
| pprint_safe_repr           | 728 ms                                                 | 712 ms: 1.02x faster                                           |
| fannkuch                   | 404 ms                                                 | 396 ms: 1.02x faster                                           |
| float                      | 79.2 ms                                                | 77.5 ms: 1.02x faster                                          |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.02x faster                                           |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                           |
| sympy_expand               | 463 ms                                                 | 455 ms: 1.02x faster                                           |
| genshi_xml                 | 50.9 ms                                                | 50.1 ms: 1.02x faster                                          |
| pickle_pure_python         | 310 us                                                 | 306 us: 1.02x faster                                           |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.02x faster                                         |
| tornado_http               | 92.4 ms                                                | 91.1 ms: 1.01x faster                                          |
| json_loads                 | 27.2 us                                                | 26.9 us: 1.01x faster                                          |
| sqlglot_optimize           | 53.7 ms                                                | 53.2 ms: 1.01x faster                                          |
| dulwich_log                | 64.3 ms                                                | 63.9 ms: 1.01x faster                                          |
| xml_etree_generate         | 86.7 ms                                                | 86.3 ms: 1.01x faster                                          |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                           |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                          |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                          |
| nqueens                    | 78.4 ms                                                | 79.2 ms: 1.01x slower                                          |
| scimark_sor                | 124 ms                                                 | 125 ms: 1.01x slower                                           |
| coverage                   | 84.0 ms                                                | 85.2 ms: 1.01x slower                                          |
| docutils                   | 2.59 sec                                               | 2.63 sec: 1.01x slower                                         |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                          |
| hexiom                     | 6.16 ms                                                | 6.27 ms: 1.02x slower                                          |
| pyflate                    | 471 ms                                                 | 479 ms: 1.02x slower                                           |
| deltablue                  | 3.23 ms                                                | 3.28 ms: 1.02x slower                                          |
| chaos                      | 58.1 ms                                                | 59.1 ms: 1.02x slower                                          |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                          |
| scimark_monte_carlo        | 67.4 ms                                                | 69.0 ms: 1.02x slower                                          |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                           |
| nbody                      | 87.0 ms                                                | 89.0 ms: 1.02x slower                                          |
| scimark_fft                | 364 ms                                                 | 376 ms: 1.03x slower                                           |
| bench_thread_pool          | 822 us                                                 | 851 us: 1.04x slower                                           |
| xml_etree_iterparse        | 101 ms                                                 | 105 ms: 1.04x slower                                           |
| regex_dna                  | 218 ms                                                 | 227 ms: 1.04x slower                                           |
| async_tree_io_tg           | 857 ms                                                 | 891 ms: 1.04x slower                                           |
| async_tree_io              | 842 ms                                                 | 888 ms: 1.06x slower                                           |
| python_startup_no_site     | 6.96 ms                                                | 7.38 ms: 1.06x slower                                          |
| bench_mp_pool              | 24.0 ms                                                | 60.3 ms: 2.51x slower                                          |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, sqlglot_transpile, sympy_integrate, async_generators, scimark_lu, raytrace, bpe_tokeniser, unpickle_pure_python, asyncio_websockets, xml_etree_parse, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241004-3.14.0a0-f072492/bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.035x faster
# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x