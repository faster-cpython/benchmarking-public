# Results vs. 3.13.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-x86_64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.037x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 255 ms: 1.05x faster                                                  |
| docutils       | 2.59 sec                                               | 2.63 sec: 1.02x slower                                                |
| html5lib       | 64.2 ms                                                | 61.5 ms: 1.04x faster                                                 |
| tornado_http   | 92.4 ms                                                | 90.4 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 389 ms: 1.19x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 392 ms: 1.13x faster                                                  |
| async_tree_none           | 351 ms                                                 | 315 ms: 1.11x faster                                                  |
| async_tree_none_tg        | 321 ms                                                 | 301 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 560 ms: 1.03x faster                                                  |
| async_generators          | 436 ms                                                 | 430 ms: 1.01x faster                                                  |
| asyncio_websockets        | 552 ms                                                 | 558 ms: 1.01x slower                                                  |
| async_tree_io_tg          | 857 ms                                                 | 874 ms: 1.02x slower                                                  |
| async_tree_io             | 842 ms                                                 | 867 ms: 1.03x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (2): coroutines, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 75.6 ms: 1.05x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.05x faster                                                 |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| regex_dna      | 218 ms                                                 | 225 ms: 1.03x slower                                                  |
| regex_effbot   | 3.73 ms                                                | 3.89 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads         | 2.14 sec                                               | 2.06 sec: 1.04x faster                                                |
| xml_etree_process   | 60.6 ms                                                | 58.6 ms: 1.03x faster                                                 |
| json_dumps          | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                 |
| xml_etree_generate  | 86.7 ms                                                | 84.8 ms: 1.02x faster                                                 |
| json_loads          | 27.2 us                                                | 26.7 us: 1.02x faster                                                 |
| pickle_pure_python  | 310 us                                                 | 305 us: 1.02x faster                                                  |
| xml_etree_iterparse | 101 ms                                                 | 103 ms: 1.02x slower                                                  |
| Geometric mean      | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.00 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.1 ms: 1.07x faster                                                 |
| genshi_xml      | 50.9 ms                                                | 48.6 ms: 1.05x faster                                                 |
| django_template | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                  | 358 us                                                 | 255 us: 1.40x faster                                                  |
| create_gc_cycles          | 2.41 ms                                                | 1.72 ms: 1.40x faster                                                 |
| deepcopy_memo             | 39.1 us                                                | 29.9 us: 1.31x faster                                                 |
| deepcopy_reduce           | 3.20 us                                                | 2.64 us: 1.21x faster                                                 |
| go                        | 144 ms                                                 | 119 ms: 1.21x faster                                                  |
| async_tree_memoization_tg | 464 ms                                                 | 389 ms: 1.19x faster                                                  |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| gc_traversal              | 4.37 ms                                                | 3.83 ms: 1.14x faster                                                 |
| async_tree_memoization    | 442 ms                                                 | 392 ms: 1.13x faster                                                  |
| async_tree_none           | 351 ms                                                 | 315 ms: 1.11x faster                                                  |
| pathlib                   | 17.5 ms                                                | 16.0 ms: 1.10x faster                                                 |
| json                      | 5.36 ms                                                | 4.94 ms: 1.09x faster                                                 |
| richards                  | 48.7 ms                                                | 45.4 ms: 1.07x faster                                                 |
| genshi_text               | 23.5 ms                                                | 22.1 ms: 1.07x faster                                                 |
| async_tree_none_tg        | 321 ms                                                 | 301 ms: 1.07x faster                                                  |
| richards_super            | 54.9 ms                                                | 51.6 ms: 1.06x faster                                                 |
| genshi_xml                | 50.9 ms                                                | 48.6 ms: 1.05x faster                                                 |
| 2to3                      | 267 ms                                                 | 255 ms: 1.05x faster                                                  |
| float                     | 79.2 ms                                                | 75.6 ms: 1.05x faster                                                 |
| regex_v8                  | 26.2 ms                                                | 25.1 ms: 1.05x faster                                                 |
| crypto_pyaes              | 75.3 ms                                                | 72.0 ms: 1.05x faster                                                 |
| html5lib                  | 64.2 ms                                                | 61.5 ms: 1.04x faster                                                 |
| thrift                    | 809 us                                                 | 777 us: 1.04x faster                                                  |
| bench_thread_pool         | 822 us                                                 | 789 us: 1.04x faster                                                  |
| tomli_loads               | 2.14 sec                                               | 2.06 sec: 1.04x faster                                                |
| typing_runtime_protocols  | 165 us                                                 | 159 us: 1.03x faster                                                  |
| xml_etree_process         | 60.6 ms                                                | 58.6 ms: 1.03x faster                                                 |
| regex_compile             | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| logging_format            | 6.40 us                                                | 6.20 us: 1.03x faster                                                 |
| sympy_sum                 | 150 ms                                                 | 146 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 560 ms: 1.03x faster                                                  |
| sympy_str                 | 275 ms                                                 | 267 ms: 1.03x faster                                                  |
| json_dumps                | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                 |
| pprint_safe_repr          | 728 ms                                                 | 708 ms: 1.03x faster                                                  |
| django_template           | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                 |
| pprint_pformat            | 1.49 sec                                               | 1.45 sec: 1.03x faster                                                |
| generators                | 29.0 ms                                                | 28.2 ms: 1.03x faster                                                 |
| spectral_norm             | 115 ms                                                 | 112 ms: 1.03x faster                                                  |
| pycparser                 | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                |
| sympy_expand              | 463 ms                                                 | 453 ms: 1.02x faster                                                  |
| xml_etree_generate        | 86.7 ms                                                | 84.8 ms: 1.02x faster                                                 |
| tornado_http              | 92.4 ms                                                | 90.4 ms: 1.02x faster                                                 |
| json_loads                | 27.2 us                                                | 26.7 us: 1.02x faster                                                 |
| pickle_pure_python        | 310 us                                                 | 305 us: 1.02x faster                                                  |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.95 ms: 1.02x faster                                                 |
| logging_simple            | 5.72 us                                                | 5.62 us: 1.02x faster                                                 |
| sympy_integrate           | 19.9 ms                                                | 19.6 ms: 1.02x faster                                                 |
| sqlglot_normalize         | 108 ms                                                 | 106 ms: 1.01x faster                                                  |
| comprehensions            | 16.5 us                                                | 16.2 us: 1.01x faster                                                 |
| telco                     | 8.54 ms                                                | 8.43 ms: 1.01x faster                                                 |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.01x faster                                                  |
| async_generators          | 436 ms                                                 | 430 ms: 1.01x faster                                                  |
| mdp                       | 2.72 sec                                               | 2.69 sec: 1.01x faster                                                |
| sqlglot_optimize          | 53.7 ms                                                | 53.1 ms: 1.01x faster                                                 |
| raytrace                  | 267 ms                                                 | 264 ms: 1.01x faster                                                  |
| scimark_lu                | 113 ms                                                 | 112 ms: 1.01x faster                                                  |
| sqlglot_transpile         | 1.58 ms                                                | 1.58 ms: 1.00x faster                                                 |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| hexiom                    | 6.16 ms                                                | 6.19 ms: 1.00x slower                                                 |
| python_startup_no_site    | 6.96 ms                                                | 7.00 ms: 1.01x slower                                                 |
| pyflate                   | 471 ms                                                 | 473 ms: 1.01x slower                                                  |
| bpe_tokeniser             | 4.75 sec                                               | 4.77 sec: 1.01x slower                                                |
| dulwich_log               | 64.3 ms                                                | 64.8 ms: 1.01x slower                                                 |
| deltablue                 | 3.23 ms                                                | 3.25 ms: 1.01x slower                                                 |
| sqlglot_parse             | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                 |
| chaos                     | 58.1 ms                                                | 58.6 ms: 1.01x slower                                                 |
| scimark_monte_carlo       | 67.4 ms                                                | 68.2 ms: 1.01x slower                                                 |
| asyncio_websockets        | 552 ms                                                 | 558 ms: 1.01x slower                                                  |
| nqueens                   | 78.4 ms                                                | 79.4 ms: 1.01x slower                                                 |
| docutils                  | 2.59 sec                                               | 2.63 sec: 1.02x slower                                                |
| scimark_fft               | 364 ms                                                 | 370 ms: 1.02x slower                                                  |
| async_tree_io_tg          | 857 ms                                                 | 874 ms: 1.02x slower                                                  |
| xml_etree_iterparse       | 101 ms                                                 | 103 ms: 1.02x slower                                                  |
| regex_dna                 | 218 ms                                                 | 225 ms: 1.03x slower                                                  |
| async_tree_io             | 842 ms                                                 | 867 ms: 1.03x slower                                                  |
| logging_silent            | 102 ns                                                 | 106 ns: 1.04x slower                                                  |
| regex_effbot              | 3.73 ms                                                | 3.89 ms: 1.04x slower                                                 |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (11): coverage, nbody, fannkuch, scimark_sor, xml_etree_parse, bench_mp_pool, unpickle_pure_python, mako, coroutines, async_tree_cpu_io_mixed_tg, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x