# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.045x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 279 ms: 1.05x faster                                                 |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                               |
| html5lib       | 72.9 ms                                                      | 70.8 ms: 1.03x faster                                                |
| tornado_http   | 119 ms                                                       | 115 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 389 ms: 1.18x faster                                                 |
| async_tree_none            | 370 ms                                                       | 318 ms: 1.16x faster                                                 |
| async_tree_memoization     | 447 ms                                                       | 398 ms: 1.12x faster                                                 |
| async_tree_none_tg         | 342 ms                                                       | 305 ms: 1.12x faster                                                 |
| async_tree_io_tg           | 823 ms                                                       | 780 ms: 1.06x faster                                                 |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 571 ms: 1.04x faster                                                 |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                                |
| async_tree_io              | 832 ms                                                       | 806 ms: 1.03x faster                                                 |
| async_generators           | 364 ms                                                       | 353 ms: 1.03x faster                                                 |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                 |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 87.3 ms: 1.05x faster                                                |
| float          | 81.6 ms                                                      | 78.8 ms: 1.04x faster                                                |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                        | 1.03x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.02x faster                                                 |
| regex_effbot   | 3.51 ms                                                      | 3.50 ms: 1.00x faster                                                |
| regex_dna      | 238 ms                                                       | 252 ms: 1.06x slower                                                 |
| regex_v8       | 24.9 ms                                                      | 26.9 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                        | 1.03x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 310 us: 1.04x faster                                                 |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                 |
| xml_etree_process    | 60.7 ms                                                      | 59.6 ms: 1.02x faster                                                |
| xml_etree_iterparse  | 99.8 ms                                                      | 98.5 ms: 1.01x faster                                                |
| json_loads           | 24.7 us                                                      | 24.6 us: 1.00x faster                                                |
| unpickle_pure_python | 216 us                                                       | 217 us: 1.00x slower                                                 |
| tomli_loads          | 2.43 sec                                                     | 2.52 sec: 1.04x slower                                               |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                         |

Benchmark hidden because not significant (2): xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.5 ms: 1.16x faster                                                |
| python_startup_no_site | 8.93 ms                                                      | 9.01 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                        | 1.07x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                |
| genshi_xml      | 58.0 ms                                                      | 52.8 ms: 1.10x faster                                                |
| django_template | 38.9 ms                                                      | 39.0 ms: 1.00x slower                                                |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 285 us: 1.36x faster                                                 |
| deepcopy_memo              | 38.9 us                                                      | 29.0 us: 1.34x faster                                                |
| create_gc_cycles           | 2.65 ms                                                      | 2.02 ms: 1.31x faster                                                |
| go                         | 167 ms                                                       | 133 ms: 1.25x faster                                                 |
| deepcopy_reduce            | 3.49 us                                                      | 2.89 us: 1.21x faster                                                |
| generators                 | 33.9 ms                                                      | 28.1 ms: 1.21x faster                                                |
| async_tree_memoization_tg  | 458 ms                                                       | 389 ms: 1.18x faster                                                 |
| async_tree_none            | 370 ms                                                       | 318 ms: 1.16x faster                                                 |
| python_startup             | 15.6 ms                                                      | 13.5 ms: 1.16x faster                                                |
| scimark_sor                | 125 ms                                                       | 111 ms: 1.13x faster                                                 |
| genshi_text                | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                |
| async_tree_memoization     | 447 ms                                                       | 398 ms: 1.12x faster                                                 |
| async_tree_none_tg         | 342 ms                                                       | 305 ms: 1.12x faster                                                 |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                |
| telco                      | 8.77 ms                                                      | 7.96 ms: 1.10x faster                                                |
| genshi_xml                 | 58.0 ms                                                      | 52.8 ms: 1.10x faster                                                |
| json                       | 5.62 ms                                                      | 5.19 ms: 1.08x faster                                                |
| richards_super             | 60.2 ms                                                      | 55.8 ms: 1.08x faster                                                |
| fannkuch                   | 384 ms                                                       | 359 ms: 1.07x faster                                                 |
| thrift                     | 918 us                                                       | 864 us: 1.06x faster                                                 |
| bpe_tokeniser              | 5.09 sec                                                     | 4.82 sec: 1.06x faster                                               |
| async_tree_io_tg           | 823 ms                                                       | 780 ms: 1.06x faster                                                 |
| nbody                      | 92.1 ms                                                      | 87.3 ms: 1.05x faster                                                |
| pycparser                  | 1.28 sec                                                     | 1.22 sec: 1.05x faster                                               |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                                 |
| hexiom                     | 6.47 ms                                                      | 6.16 ms: 1.05x faster                                                |
| 2to3                       | 293 ms                                                       | 279 ms: 1.05x faster                                                 |
| scimark_fft                | 298 ms                                                       | 284 ms: 1.05x faster                                                 |
| pprint_safe_repr           | 835 ms                                                       | 797 ms: 1.05x faster                                                 |
| scimark_lu                 | 97.4 ms                                                      | 93.1 ms: 1.05x faster                                                |
| meteor_contest             | 130 ms                                                       | 125 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 571 ms: 1.04x faster                                                 |
| pprint_pformat             | 1.70 sec                                                     | 1.63 sec: 1.04x faster                                               |
| bench_thread_pool          | 929 us                                                       | 895 us: 1.04x faster                                                 |
| nqueens                    | 92.3 ms                                                      | 89.0 ms: 1.04x faster                                                |
| pickle_pure_python         | 322 us                                                       | 310 us: 1.04x faster                                                 |
| float                      | 81.6 ms                                                      | 78.8 ms: 1.04x faster                                                |
| richards                   | 52.5 ms                                                      | 50.8 ms: 1.03x faster                                                |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                                |
| async_tree_io              | 832 ms                                                       | 806 ms: 1.03x faster                                                 |
| typing_runtime_protocols   | 176 us                                                       | 170 us: 1.03x faster                                                 |
| async_generators           | 364 ms                                                       | 353 ms: 1.03x faster                                                 |
| tornado_http               | 119 ms                                                       | 115 ms: 1.03x faster                                                 |
| html5lib                   | 72.9 ms                                                      | 70.8 ms: 1.03x faster                                                |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                 |
| regex_compile              | 143 ms                                                       | 139 ms: 1.02x faster                                                 |
| scimark_monte_carlo        | 65.2 ms                                                      | 63.8 ms: 1.02x faster                                                |
| logging_simple             | 6.28 us                                                      | 6.14 us: 1.02x faster                                                |
| sympy_str                  | 297 ms                                                       | 291 ms: 1.02x faster                                                 |
| sympy_expand               | 506 ms                                                       | 497 ms: 1.02x faster                                                 |
| xml_etree_process          | 60.7 ms                                                      | 59.6 ms: 1.02x faster                                                |
| crypto_pyaes               | 73.5 ms                                                      | 72.3 ms: 1.02x faster                                                |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                 |
| sqlglot_normalize          | 119 ms                                                       | 117 ms: 1.01x faster                                                 |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                 |
| xml_etree_iterparse        | 99.8 ms                                                      | 98.5 ms: 1.01x faster                                                |
| mdp                        | 2.53 sec                                                     | 2.50 sec: 1.01x faster                                               |
| coverage                   | 84.5 ms                                                      | 83.6 ms: 1.01x faster                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.17 ms: 1.01x faster                                                |
| pyflate                    | 493 ms                                                       | 488 ms: 1.01x faster                                                 |
| logging_format             | 6.95 us                                                      | 6.89 us: 1.01x faster                                                |
| raytrace                   | 267 ms                                                       | 266 ms: 1.01x faster                                                 |
| spectral_norm              | 97.4 ms                                                      | 96.8 ms: 1.01x faster                                                |
| json_loads                 | 24.7 us                                                      | 24.6 us: 1.00x faster                                                |
| sympy_integrate            | 23.4 ms                                                      | 23.3 ms: 1.00x faster                                                |
| regex_effbot               | 3.51 ms                                                      | 3.50 ms: 1.00x faster                                                |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                 |
| unpickle_pure_python       | 216 us                                                       | 217 us: 1.00x slower                                                 |
| django_template            | 38.9 ms                                                      | 39.0 ms: 1.00x slower                                                |
| sqlglot_optimize           | 58.7 ms                                                      | 59.0 ms: 1.01x slower                                                |
| python_startup_no_site     | 8.93 ms                                                      | 9.01 ms: 1.01x slower                                                |
| gc_traversal               | 4.48 ms                                                      | 4.53 ms: 1.01x slower                                                |
| sqlglot_transpile          | 1.76 ms                                                      | 1.79 ms: 1.01x slower                                                |
| dulwich_log                | 65.5 ms                                                      | 66.7 ms: 1.02x slower                                                |
| logging_silent             | 97.5 ns                                                      | 99.3 ns: 1.02x slower                                                |
| chaos                      | 60.6 ms                                                      | 62.5 ms: 1.03x slower                                                |
| sqlglot_parse              | 1.37 ms                                                      | 1.41 ms: 1.03x slower                                                |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                               |
| tomli_loads                | 2.43 sec                                                     | 2.52 sec: 1.04x slower                                               |
| regex_dna                  | 238 ms                                                       | 252 ms: 1.06x slower                                                 |
| regex_v8                   | 24.9 ms                                                      | 26.9 ms: 1.08x slower                                                |
| bench_mp_pool              | 4.82 ms                                                      | 1.98 sec: 410.39x slower                                             |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                         |

Benchmark hidden because not significant (6): xml_etree_generate, deltablue, json_dumps, comprehensions, pylint, mako
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.045x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x