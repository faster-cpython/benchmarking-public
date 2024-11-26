# Results vs. 3.13.0

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-x86_64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.040x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 253 ms: 1.05x faster                                              |
| docutils       | 2.59 sec                                               | 2.64 sec: 1.02x slower                                            |
| html5lib       | 64.2 ms                                                | 62.9 ms: 1.02x faster                                             |
| tornado_http   | 92.4 ms                                                | 89.8 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.20x faster                                              |
| async_tree_memoization     | 442 ms                                                 | 393 ms: 1.12x faster                                              |
| async_tree_none            | 351 ms                                                 | 313 ms: 1.12x faster                                              |
| async_tree_none_tg         | 321 ms                                                 | 300 ms: 1.07x faster                                              |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 567 ms: 1.02x faster                                              |
| async_generators           | 436 ms                                                 | 440 ms: 1.01x slower                                              |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 556 ms: 1.02x slower                                              |
| coroutines                 | 22.7 ms                                                | 23.1 ms: 1.02x slower                                             |
| async_tree_io_tg           | 857 ms                                                 | 874 ms: 1.02x slower                                              |
| async_tree_io              | 842 ms                                                 | 866 ms: 1.03x slower                                              |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.8 ms: 1.03x faster                                             |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.8 ms: 1.06x faster                                             |
| regex_compile  | 132 ms                                                 | 128 ms: 1.04x faster                                              |
| regex_effbot   | 3.73 ms                                                | 3.72 ms: 1.00x faster                                             |
| regex_dna      | 218 ms                                                 | 220 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 58.1 ms: 1.04x faster                                             |
| json_dumps           | 10.6 ms                                                | 10.2 ms: 1.03x faster                                             |
| pickle_pure_python   | 310 us                                                 | 301 us: 1.03x faster                                              |
| xml_etree_generate   | 86.7 ms                                                | 84.2 ms: 1.03x faster                                             |
| tomli_loads          | 2.14 sec                                               | 2.09 sec: 1.03x faster                                            |
| unpickle_pure_python | 216 us                                                 | 213 us: 1.01x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                              |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                             |
| python_startup_no_site | 6.96 ms                                                | 7.00 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 21.6 ms: 1.09x faster                                             |
| genshi_xml      | 50.9 ms                                                | 49.2 ms: 1.04x faster                                             |
| django_template | 35.2 ms                                                | 34.4 ms: 1.02x faster                                             |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                             |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.73 ms: 1.39x faster                                             |
| deepcopy                   | 358 us                                                 | 258 us: 1.39x faster                                              |
| deepcopy_memo              | 39.1 us                                                | 29.5 us: 1.33x faster                                             |
| go                         | 144 ms                                                 | 116 ms: 1.24x faster                                              |
| deepcopy_reduce            | 3.20 us                                                | 2.65 us: 1.21x faster                                             |
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.20x faster                                              |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                             |
| async_tree_memoization     | 442 ms                                                 | 393 ms: 1.12x faster                                              |
| gc_traversal               | 4.37 ms                                                | 3.90 ms: 1.12x faster                                             |
| async_tree_none            | 351 ms                                                 | 313 ms: 1.12x faster                                              |
| pathlib                    | 17.5 ms                                                | 15.8 ms: 1.11x faster                                             |
| genshi_text                | 23.5 ms                                                | 21.6 ms: 1.09x faster                                             |
| richards                   | 48.7 ms                                                | 45.1 ms: 1.08x faster                                             |
| richards_super             | 54.9 ms                                                | 50.9 ms: 1.08x faster                                             |
| async_tree_none_tg         | 321 ms                                                 | 300 ms: 1.07x faster                                              |
| crypto_pyaes               | 75.3 ms                                                | 71.0 ms: 1.06x faster                                             |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.06x faster                                              |
| regex_v8                   | 26.2 ms                                                | 24.8 ms: 1.06x faster                                             |
| 2to3                       | 267 ms                                                 | 253 ms: 1.05x faster                                              |
| json                       | 5.36 ms                                                | 5.10 ms: 1.05x faster                                             |
| logging_format             | 6.40 us                                                | 6.11 us: 1.05x faster                                             |
| xml_etree_process          | 60.6 ms                                                | 58.1 ms: 1.04x faster                                             |
| thrift                     | 809 us                                                 | 776 us: 1.04x faster                                              |
| generators                 | 29.0 ms                                                | 27.8 ms: 1.04x faster                                             |
| bench_thread_pool          | 822 us                                                 | 791 us: 1.04x faster                                              |
| pyflate                    | 471 ms                                                 | 454 ms: 1.04x faster                                              |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.87 ms: 1.04x faster                                             |
| genshi_xml                 | 50.9 ms                                                | 49.2 ms: 1.04x faster                                             |
| regex_compile              | 132 ms                                                 | 128 ms: 1.04x faster                                              |
| typing_runtime_protocols   | 165 us                                                 | 159 us: 1.03x faster                                              |
| logging_silent             | 102 ns                                                 | 98.6 ns: 1.03x faster                                             |
| json_dumps                 | 10.6 ms                                                | 10.2 ms: 1.03x faster                                             |
| float                      | 79.2 ms                                                | 76.8 ms: 1.03x faster                                             |
| pickle_pure_python         | 310 us                                                 | 301 us: 1.03x faster                                              |
| xml_etree_generate         | 86.7 ms                                                | 84.2 ms: 1.03x faster                                             |
| tornado_http               | 92.4 ms                                                | 89.8 ms: 1.03x faster                                             |
| raytrace                   | 267 ms                                                 | 260 ms: 1.03x faster                                              |
| deltablue                  | 3.23 ms                                                | 3.14 ms: 1.03x faster                                             |
| logging_simple             | 5.72 us                                                | 5.57 us: 1.03x faster                                             |
| tomli_loads                | 2.14 sec                                               | 2.09 sec: 1.03x faster                                            |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                            |
| sympy_integrate            | 19.9 ms                                                | 19.4 ms: 1.02x faster                                             |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                              |
| django_template            | 35.2 ms                                                | 34.4 ms: 1.02x faster                                             |
| pprint_safe_repr           | 728 ms                                                 | 713 ms: 1.02x faster                                              |
| html5lib                   | 64.2 ms                                                | 62.9 ms: 1.02x faster                                             |
| sympy_expand               | 463 ms                                                 | 454 ms: 1.02x faster                                              |
| sympy_str                  | 275 ms                                                 | 270 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 567 ms: 1.02x faster                                              |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.02x faster                                            |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                              |
| scimark_fft                | 364 ms                                                 | 359 ms: 1.02x faster                                              |
| sqlglot_optimize           | 53.7 ms                                                | 52.9 ms: 1.02x faster                                             |
| fannkuch                   | 404 ms                                                 | 399 ms: 1.01x faster                                              |
| mdp                        | 2.72 sec                                               | 2.69 sec: 1.01x faster                                            |
| unpickle_pure_python       | 216 us                                                 | 213 us: 1.01x faster                                              |
| hexiom                     | 6.16 ms                                                | 6.09 ms: 1.01x faster                                             |
| telco                      | 8.54 ms                                                | 8.45 ms: 1.01x faster                                             |
| scimark_monte_carlo        | 67.4 ms                                                | 66.9 ms: 1.01x faster                                             |
| sqlglot_transpile          | 1.58 ms                                                | 1.57 ms: 1.01x faster                                             |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                              |
| regex_effbot               | 3.73 ms                                                | 3.72 ms: 1.00x faster                                             |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| python_startup_no_site     | 6.96 ms                                                | 7.00 ms: 1.01x slower                                             |
| dulwich_log                | 64.3 ms                                                | 64.7 ms: 1.01x slower                                             |
| regex_dna                  | 218 ms                                                 | 220 ms: 1.01x slower                                              |
| chaos                      | 58.1 ms                                                | 58.6 ms: 1.01x slower                                             |
| async_generators           | 436 ms                                                 | 440 ms: 1.01x slower                                              |
| bpe_tokeniser              | 4.75 sec                                               | 4.80 sec: 1.01x slower                                            |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 556 ms: 1.02x slower                                              |
| coroutines                 | 22.7 ms                                                | 23.1 ms: 1.02x slower                                             |
| docutils                   | 2.59 sec                                               | 2.64 sec: 1.02x slower                                            |
| async_tree_io_tg           | 857 ms                                                 | 874 ms: 1.02x slower                                              |
| nqueens                    | 78.4 ms                                                | 80.0 ms: 1.02x slower                                             |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                             |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.03x slower                                              |
| async_tree_io              | 842 ms                                                 | 866 ms: 1.03x slower                                              |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (10): scimark_lu, comprehensions, coverage, bench_mp_pool, sqlglot_parse, scimark_sor, json_loads, xml_etree_parse, nbody, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.040x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x