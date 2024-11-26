# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 8738ae5
- commit date: 2024-10-07
- overall geometric mean: 1.033x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 255 ms: 1.05x faster                                           |
| docutils       | 2.59 sec                                               | 2.64 sec: 1.02x slower                                         |
| html5lib       | 64.2 ms                                                | 61.4 ms: 1.05x faster                                          |
| tornado_http   | 92.4 ms                                                | 90.2 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 402 ms: 1.15x faster                                           |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                           |
| async_tree_none           | 351 ms                                                 | 322 ms: 1.09x faster                                           |
| async_tree_none_tg        | 321 ms                                                 | 308 ms: 1.04x faster                                           |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 563 ms: 1.02x faster                                           |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                           |
| coroutines                | 22.7 ms                                                | 23.0 ms: 1.01x slower                                          |
| async_tree_io_tg          | 857 ms                                                 | 916 ms: 1.07x slower                                           |
| async_tree_io             | 842 ms                                                 | 929 ms: 1.10x slower                                           |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (2): async_generators, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.8 ms: 1.03x faster                                          |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.4 ms: 1.03x faster                                          |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                           |
| regex_effbot   | 3.73 ms                                                | 3.69 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.03x faster                                          |
| tomli_loads          | 2.14 sec                                               | 2.09 sec: 1.02x faster                                         |
| xml_etree_process    | 60.6 ms                                                | 59.2 ms: 1.02x faster                                          |
| pickle_pure_python   | 310 us                                                 | 305 us: 1.02x faster                                           |
| json_loads           | 27.2 us                                                | 26.9 us: 1.01x faster                                          |
| unpickle_pure_python | 216 us                                                 | 216 us: 1.00x slower                                           |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                           |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                          |
| python_startup_no_site | 6.96 ms                                                | 7.01 ms: 1.01x slower                                          |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.4 ms: 1.05x faster                                          |
| django_template | 35.2 ms                                                | 33.9 ms: 1.04x faster                                          |
| genshi_xml      | 50.9 ms                                                | 49.6 ms: 1.03x faster                                          |
| mako            | 11.1 ms                                                | 11.0 ms: 1.01x faster                                          |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy                  | 358 us                                                 | 263 us: 1.36x faster                                           |
| create_gc_cycles          | 2.41 ms                                                | 1.77 ms: 1.36x faster                                          |
| deepcopy_memo             | 39.1 us                                                | 30.5 us: 1.28x faster                                          |
| gc_traversal              | 4.37 ms                                                | 3.61 ms: 1.21x faster                                          |
| go                        | 144 ms                                                 | 120 ms: 1.19x faster                                           |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.18x faster                                          |
| deepcopy_reduce           | 3.20 us                                                | 2.71 us: 1.18x faster                                          |
| async_tree_memoization_tg | 464 ms                                                 | 402 ms: 1.15x faster                                           |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                           |
| pathlib                   | 17.5 ms                                                | 15.9 ms: 1.10x faster                                          |
| async_tree_none           | 351 ms                                                 | 322 ms: 1.09x faster                                           |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.66 ms: 1.08x faster                                          |
| pycparser                 | 1.20 sec                                               | 1.13 sec: 1.06x faster                                         |
| thrift                    | 809 us                                                 | 767 us: 1.05x faster                                           |
| crypto_pyaes              | 75.3 ms                                                | 71.5 ms: 1.05x faster                                          |
| genshi_text               | 23.5 ms                                                | 22.4 ms: 1.05x faster                                          |
| json                      | 5.36 ms                                                | 5.12 ms: 1.05x faster                                          |
| telco                     | 8.54 ms                                                | 8.16 ms: 1.05x faster                                          |
| generators                | 29.0 ms                                                | 27.7 ms: 1.05x faster                                          |
| 2to3                      | 267 ms                                                 | 255 ms: 1.05x faster                                           |
| html5lib                  | 64.2 ms                                                | 61.4 ms: 1.05x faster                                          |
| async_tree_none_tg        | 321 ms                                                 | 308 ms: 1.04x faster                                           |
| django_template           | 35.2 ms                                                | 33.9 ms: 1.04x faster                                          |
| regex_v8                  | 26.2 ms                                                | 25.4 ms: 1.03x faster                                          |
| float                     | 79.2 ms                                                | 76.8 ms: 1.03x faster                                          |
| json_dumps                | 10.6 ms                                                | 10.3 ms: 1.03x faster                                          |
| sympy_str                 | 275 ms                                                 | 267 ms: 1.03x faster                                           |
| richards                  | 48.7 ms                                                | 47.4 ms: 1.03x faster                                          |
| sympy_sum                 | 150 ms                                                 | 146 ms: 1.03x faster                                           |
| genshi_xml                | 50.9 ms                                                | 49.6 ms: 1.03x faster                                          |
| typing_runtime_protocols  | 165 us                                                 | 161 us: 1.03x faster                                           |
| richards_super            | 54.9 ms                                                | 53.5 ms: 1.03x faster                                          |
| tomli_loads               | 2.14 sec                                               | 2.09 sec: 1.02x faster                                         |
| tornado_http              | 92.4 ms                                                | 90.2 ms: 1.02x faster                                          |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 563 ms: 1.02x faster                                           |
| xml_etree_process         | 60.6 ms                                                | 59.2 ms: 1.02x faster                                          |
| spectral_norm             | 115 ms                                                 | 113 ms: 1.02x faster                                           |
| logging_format            | 6.40 us                                                | 6.26 us: 1.02x faster                                          |
| regex_compile             | 132 ms                                                 | 129 ms: 1.02x faster                                           |
| sympy_expand              | 463 ms                                                 | 455 ms: 1.02x faster                                           |
| pickle_pure_python        | 310 us                                                 | 305 us: 1.02x faster                                           |
| fannkuch                  | 404 ms                                                 | 398 ms: 1.02x faster                                           |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.01x faster                                           |
| logging_simple            | 5.72 us                                                | 5.65 us: 1.01x faster                                          |
| regex_effbot              | 3.73 ms                                                | 3.69 ms: 1.01x faster                                          |
| json_loads                | 27.2 us                                                | 26.9 us: 1.01x faster                                          |
| scimark_fft               | 364 ms                                                 | 360 ms: 1.01x faster                                           |
| pprint_pformat            | 1.49 sec                                               | 1.48 sec: 1.01x faster                                         |
| pprint_safe_repr          | 728 ms                                                 | 721 ms: 1.01x faster                                           |
| raytrace                  | 267 ms                                                 | 265 ms: 1.01x faster                                           |
| scimark_lu                | 113 ms                                                 | 112 ms: 1.01x faster                                           |
| sqlglot_optimize          | 53.7 ms                                                | 53.4 ms: 1.01x faster                                          |
| bpe_tokeniser             | 4.75 sec                                               | 4.71 sec: 1.01x faster                                         |
| sympy_integrate           | 19.9 ms                                                | 19.8 ms: 1.01x faster                                          |
| mako                      | 11.1 ms                                                | 11.0 ms: 1.01x faster                                          |
| logging_silent            | 102 ns                                                 | 101 ns: 1.01x faster                                           |
| scimark_sor               | 124 ms                                                 | 123 ms: 1.00x faster                                           |
| mdp                       | 2.72 sec                                               | 2.71 sec: 1.00x faster                                         |
| dulwich_log               | 64.3 ms                                                | 64.6 ms: 1.00x slower                                          |
| unpickle_pure_python      | 216 us                                                 | 216 us: 1.00x slower                                           |
| sqlglot_normalize         | 108 ms                                                 | 108 ms: 1.00x slower                                           |
| comprehensions            | 16.5 us                                                | 16.6 us: 1.01x slower                                          |
| sqlglot_transpile         | 1.58 ms                                                | 1.59 ms: 1.01x slower                                          |
| python_startup_no_site    | 6.96 ms                                                | 7.01 ms: 1.01x slower                                          |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                           |
| hexiom                    | 6.16 ms                                                | 6.22 ms: 1.01x slower                                          |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                           |
| pyflate                   | 471 ms                                                 | 476 ms: 1.01x slower                                           |
| coverage                  | 84.0 ms                                                | 84.8 ms: 1.01x slower                                          |
| deltablue                 | 3.23 ms                                                | 3.26 ms: 1.01x slower                                          |
| scimark_monte_carlo       | 67.4 ms                                                | 68.2 ms: 1.01x slower                                          |
| coroutines                | 22.7 ms                                                | 23.0 ms: 1.01x slower                                          |
| nqueens                   | 78.4 ms                                                | 79.7 ms: 1.02x slower                                          |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                          |
| docutils                  | 2.59 sec                                               | 2.64 sec: 1.02x slower                                         |
| xml_etree_iterparse       | 101 ms                                                 | 104 ms: 1.03x slower                                           |
| chaos                     | 58.1 ms                                                | 59.8 ms: 1.03x slower                                          |
| bench_thread_pool         | 822 us                                                 | 853 us: 1.04x slower                                           |
| async_tree_io_tg          | 857 ms                                                 | 916 ms: 1.07x slower                                           |
| async_tree_io             | 842 ms                                                 | 929 ms: 1.10x slower                                           |
| bench_mp_pool             | 24.0 ms                                                | 56.0 ms: 2.33x slower                                          |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (7): async_generators, nbody, xml_etree_generate, regex_dna, async_tree_cpu_io_mixed_tg, xml_etree_parse, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241007-3.14.0a0-8738ae5/bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x