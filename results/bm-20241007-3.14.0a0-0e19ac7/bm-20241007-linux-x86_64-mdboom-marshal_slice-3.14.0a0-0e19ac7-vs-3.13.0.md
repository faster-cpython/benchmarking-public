# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.036x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 253 ms: 1.05x faster                                           |
| docutils       | 2.59 sec                                               | 2.62 sec: 1.01x slower                                         |
| html5lib       | 64.2 ms                                                | 61.4 ms: 1.05x faster                                          |
| tornado_http   | 92.4 ms                                                | 90.2 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 400 ms: 1.16x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 389 ms: 1.14x faster                                           |
| async_tree_none            | 351 ms                                                 | 320 ms: 1.10x faster                                           |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.05x faster                                           |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 555 ms: 1.04x faster                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 536 ms: 1.02x faster                                           |
| async_generators           | 436 ms                                                 | 433 ms: 1.01x faster                                           |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                           |
| async_tree_io_tg           | 857 ms                                                 | 915 ms: 1.07x slower                                           |
| async_tree_io              | 842 ms                                                 | 924 ms: 1.10x slower                                           |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                   |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.1 ms: 1.04x faster                                          |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.2 ms: 1.04x faster                                          |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                           |
| regex_effbot   | 3.73 ms                                                | 3.70 ms: 1.01x faster                                          |
| regex_dna      | 218 ms                                                 | 220 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.07 sec: 1.04x faster                                         |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.03x faster                                          |
| xml_etree_process    | 60.6 ms                                                | 59.0 ms: 1.03x faster                                          |
| pickle_pure_python   | 310 us                                                 | 305 us: 1.02x faster                                           |
| xml_etree_generate   | 86.7 ms                                                | 86.1 ms: 1.01x faster                                          |
| json_loads           | 27.2 us                                                | 27.1 us: 1.01x faster                                          |
| unpickle_pure_python | 216 us                                                 | 215 us: 1.00x faster                                           |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                           |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                          |
| python_startup_no_site | 6.96 ms                                                | 7.01 ms: 1.01x slower                                          |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 21.9 ms: 1.08x faster                                          |
| genshi_xml      | 50.9 ms                                                | 49.3 ms: 1.03x faster                                          |
| django_template | 35.2 ms                                                | 34.2 ms: 1.03x faster                                          |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                          |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 260 us: 1.38x faster                                           |
| create_gc_cycles           | 2.41 ms                                                | 1.79 ms: 1.35x faster                                          |
| deepcopy_memo              | 39.1 us                                                | 29.7 us: 1.32x faster                                          |
| go                         | 144 ms                                                 | 119 ms: 1.21x faster                                           |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.18x faster                                          |
| deepcopy_reduce            | 3.20 us                                                | 2.71 us: 1.18x faster                                          |
| async_tree_memoization_tg  | 464 ms                                                 | 400 ms: 1.16x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 389 ms: 1.14x faster                                           |
| pathlib                    | 17.5 ms                                                | 15.8 ms: 1.11x faster                                          |
| gc_traversal               | 4.37 ms                                                | 3.95 ms: 1.11x faster                                          |
| async_tree_none            | 351 ms                                                 | 320 ms: 1.10x faster                                           |
| mdp                        | 2.72 sec                                               | 2.52 sec: 1.08x faster                                         |
| genshi_text                | 23.5 ms                                                | 21.9 ms: 1.08x faster                                          |
| telco                      | 8.54 ms                                                | 8.01 ms: 1.07x faster                                          |
| richards                   | 48.7 ms                                                | 46.0 ms: 1.06x faster                                          |
| json                       | 5.36 ms                                                | 5.07 ms: 1.06x faster                                          |
| thrift                     | 809 us                                                 | 767 us: 1.05x faster                                           |
| 2to3                       | 267 ms                                                 | 253 ms: 1.05x faster                                           |
| richards_super             | 54.9 ms                                                | 52.1 ms: 1.05x faster                                          |
| crypto_pyaes               | 75.3 ms                                                | 71.7 ms: 1.05x faster                                          |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.82 ms: 1.05x faster                                          |
| generators                 | 29.0 ms                                                | 27.7 ms: 1.05x faster                                          |
| html5lib                   | 64.2 ms                                                | 61.4 ms: 1.05x faster                                          |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.05x faster                                           |
| float                      | 79.2 ms                                                | 76.1 ms: 1.04x faster                                          |
| regex_v8                   | 26.2 ms                                                | 25.2 ms: 1.04x faster                                          |
| logging_format             | 6.40 us                                                | 6.15 us: 1.04x faster                                          |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                           |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 555 ms: 1.04x faster                                           |
| typing_runtime_protocols   | 165 us                                                 | 159 us: 1.04x faster                                           |
| tomli_loads                | 2.14 sec                                               | 2.07 sec: 1.04x faster                                         |
| pprint_safe_repr           | 728 ms                                                 | 703 ms: 1.04x faster                                           |
| pprint_pformat             | 1.49 sec                                               | 1.44 sec: 1.04x faster                                         |
| genshi_xml                 | 50.9 ms                                                | 49.3 ms: 1.03x faster                                          |
| logging_simple             | 5.72 us                                                | 5.55 us: 1.03x faster                                          |
| json_dumps                 | 10.6 ms                                                | 10.3 ms: 1.03x faster                                          |
| sympy_expand               | 463 ms                                                 | 450 ms: 1.03x faster                                           |
| sympy_str                  | 275 ms                                                 | 267 ms: 1.03x faster                                           |
| django_template            | 35.2 ms                                                | 34.2 ms: 1.03x faster                                          |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                           |
| xml_etree_process          | 60.6 ms                                                | 59.0 ms: 1.03x faster                                          |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                           |
| tornado_http               | 92.4 ms                                                | 90.2 ms: 1.02x faster                                          |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                         |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                           |
| pickle_pure_python         | 310 us                                                 | 305 us: 1.02x faster                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 536 ms: 1.02x faster                                           |
| fannkuch                   | 404 ms                                                 | 399 ms: 1.01x faster                                           |
| raytrace                   | 267 ms                                                 | 264 ms: 1.01x faster                                           |
| sqlglot_optimize           | 53.7 ms                                                | 53.3 ms: 1.01x faster                                          |
| scimark_lu                 | 113 ms                                                 | 112 ms: 1.01x faster                                           |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                           |
| xml_etree_generate         | 86.7 ms                                                | 86.1 ms: 1.01x faster                                          |
| regex_effbot               | 3.73 ms                                                | 3.70 ms: 1.01x faster                                          |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.01x faster                                          |
| async_generators           | 436 ms                                                 | 433 ms: 1.01x faster                                           |
| json_loads                 | 27.2 us                                                | 27.1 us: 1.01x faster                                          |
| unpickle_pure_python       | 216 us                                                 | 215 us: 1.00x faster                                           |
| scimark_sor                | 124 ms                                                 | 124 ms: 1.00x slower                                           |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                           |
| scimark_monte_carlo        | 67.4 ms                                                | 67.8 ms: 1.01x slower                                          |
| coverage                   | 84.0 ms                                                | 84.5 ms: 1.01x slower                                          |
| python_startup_no_site     | 6.96 ms                                                | 7.01 ms: 1.01x slower                                          |
| regex_dna                  | 218 ms                                                 | 220 ms: 1.01x slower                                           |
| deltablue                  | 3.23 ms                                                | 3.26 ms: 1.01x slower                                          |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                           |
| docutils                   | 2.59 sec                                               | 2.62 sec: 1.01x slower                                         |
| hexiom                     | 6.16 ms                                                | 6.24 ms: 1.01x slower                                          |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                           |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.03x slower                                           |
| chaos                      | 58.1 ms                                                | 59.8 ms: 1.03x slower                                          |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.03x slower                                          |
| bench_thread_pool          | 822 us                                                 | 856 us: 1.04x slower                                           |
| nqueens                    | 78.4 ms                                                | 82.2 ms: 1.05x slower                                          |
| async_tree_io_tg           | 857 ms                                                 | 915 ms: 1.07x slower                                           |
| async_tree_io              | 842 ms                                                 | 924 ms: 1.10x slower                                           |
| bench_mp_pool              | 24.0 ms                                                | 55.9 ms: 2.33x slower                                          |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                   |

Benchmark hidden because not significant (11): bpe_tokeniser, nbody, sqlglot_transpile, scimark_fft, sqlglot_parse, dulwich_log, pyflate, comprehensions, coroutines, xml_etree_parse, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.036x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x