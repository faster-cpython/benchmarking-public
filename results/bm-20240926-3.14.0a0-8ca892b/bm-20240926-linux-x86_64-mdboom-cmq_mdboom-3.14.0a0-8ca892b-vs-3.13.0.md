# Results vs. 3.13.0

- fork: mdboom
- ref: cmq_mdboom
- machine: linux-x86_64
- commit hash: 8ca892b
- commit date: 2024-09-26
- overall geometric mean: 1.038x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 253 ms: 1.05x faster                                        |
| docutils       | 2.59 sec                                               | 2.66 sec: 1.03x slower                                      |
| html5lib       | 64.2 ms                                                | 63.9 ms: 1.00x faster                                       |
| tornado_http   | 92.4 ms                                                | 90.4 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 389 ms: 1.19x faster                                        |
| async_tree_memoization    | 442 ms                                                 | 392 ms: 1.13x faster                                        |
| async_tree_none           | 351 ms                                                 | 315 ms: 1.11x faster                                        |
| async_tree_none_tg        | 321 ms                                                 | 304 ms: 1.05x faster                                        |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 560 ms: 1.03x faster                                        |
| asyncio_websockets        | 552 ms                                                 | 560 ms: 1.01x slower                                        |
| coroutines                | 22.7 ms                                                | 23.4 ms: 1.03x slower                                       |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                |

Benchmark hidden because not significant (4): async_generators, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.0 ms: 1.04x faster                                       |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                        |
| nbody          | 87.0 ms                                                | 88.0 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.2 ms: 1.08x faster                                       |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                        |
| regex_effbot   | 3.73 ms                                                | 3.70 ms: 1.01x faster                                       |
| regex_dna      | 218 ms                                                 | 229 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 58.4 ms: 1.04x faster                                       |
| tomli_loads          | 2.14 sec                                               | 2.09 sec: 1.03x faster                                      |
| xml_etree_generate   | 86.7 ms                                                | 84.8 ms: 1.02x faster                                       |
| json_loads           | 27.2 us                                                | 26.8 us: 1.02x faster                                       |
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.02x faster                                       |
| pickle_pure_python   | 310 us                                                 | 307 us: 1.01x faster                                        |
| unpickle_pure_python | 216 us                                                 | 214 us: 1.01x faster                                        |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                        |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                       |
| python_startup_no_site | 6.96 ms                                                | 6.98 ms: 1.00x slower                                       |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 21.8 ms: 1.08x faster                                       |
| genshi_xml      | 50.9 ms                                                | 49.2 ms: 1.04x faster                                       |
| django_template | 35.2 ms                                                | 34.0 ms: 1.03x faster                                       |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                       |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| create_gc_cycles          | 2.41 ms                                                | 1.71 ms: 1.41x faster                                       |
| deepcopy                  | 358 us                                                 | 258 us: 1.39x faster                                        |
| deepcopy_memo             | 39.1 us                                                | 29.7 us: 1.32x faster                                       |
| go                        | 144 ms                                                 | 117 ms: 1.23x faster                                        |
| async_tree_memoization_tg | 464 ms                                                 | 389 ms: 1.19x faster                                        |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.19x faster                                       |
| deepcopy_reduce           | 3.20 us                                                | 2.69 us: 1.19x faster                                       |
| async_tree_memoization    | 442 ms                                                 | 392 ms: 1.13x faster                                        |
| gc_traversal              | 4.37 ms                                                | 3.92 ms: 1.11x faster                                       |
| async_tree_none           | 351 ms                                                 | 315 ms: 1.11x faster                                        |
| pathlib                   | 17.5 ms                                                | 16.0 ms: 1.10x faster                                       |
| json                      | 5.36 ms                                                | 4.90 ms: 1.09x faster                                       |
| regex_v8                  | 26.2 ms                                                | 24.2 ms: 1.08x faster                                       |
| genshi_text               | 23.5 ms                                                | 21.8 ms: 1.08x faster                                       |
| pycparser                 | 1.20 sec                                               | 1.12 sec: 1.07x faster                                      |
| mdp                       | 2.72 sec                                               | 2.57 sec: 1.06x faster                                      |
| async_tree_none_tg        | 321 ms                                                 | 304 ms: 1.05x faster                                        |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.79 ms: 1.05x faster                                       |
| 2to3                      | 267 ms                                                 | 253 ms: 1.05x faster                                        |
| richards                  | 48.7 ms                                                | 46.2 ms: 1.05x faster                                       |
| richards_super            | 54.9 ms                                                | 52.2 ms: 1.05x faster                                       |
| thrift                    | 809 us                                                 | 774 us: 1.05x faster                                        |
| generators                | 29.0 ms                                                | 27.8 ms: 1.04x faster                                       |
| float                     | 79.2 ms                                                | 76.0 ms: 1.04x faster                                       |
| bench_thread_pool         | 822 us                                                 | 789 us: 1.04x faster                                        |
| xml_etree_process         | 60.6 ms                                                | 58.4 ms: 1.04x faster                                       |
| typing_runtime_protocols  | 165 us                                                 | 159 us: 1.04x faster                                        |
| regex_compile             | 132 ms                                                 | 127 ms: 1.04x faster                                        |
| logging_format            | 6.40 us                                                | 6.17 us: 1.04x faster                                       |
| genshi_xml                | 50.9 ms                                                | 49.2 ms: 1.04x faster                                       |
| crypto_pyaes              | 75.3 ms                                                | 72.7 ms: 1.04x faster                                       |
| django_template           | 35.2 ms                                                | 34.0 ms: 1.03x faster                                       |
| logging_simple            | 5.72 us                                                | 5.55 us: 1.03x faster                                       |
| sympy_str                 | 275 ms                                                 | 267 ms: 1.03x faster                                        |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 560 ms: 1.03x faster                                        |
| tomli_loads               | 2.14 sec                                               | 2.09 sec: 1.03x faster                                      |
| sympy_sum                 | 150 ms                                                 | 147 ms: 1.02x faster                                        |
| meteor_contest            | 109 ms                                                 | 106 ms: 1.02x faster                                        |
| sympy_expand              | 463 ms                                                 | 453 ms: 1.02x faster                                        |
| xml_etree_generate        | 86.7 ms                                                | 84.8 ms: 1.02x faster                                       |
| tornado_http              | 92.4 ms                                                | 90.4 ms: 1.02x faster                                       |
| telco                     | 8.54 ms                                                | 8.37 ms: 1.02x faster                                       |
| sympy_integrate           | 19.9 ms                                                | 19.5 ms: 1.02x faster                                       |
| pprint_pformat            | 1.49 sec                                               | 1.47 sec: 1.02x faster                                      |
| sqlglot_normalize         | 108 ms                                                 | 106 ms: 1.02x faster                                        |
| scimark_fft               | 364 ms                                                 | 358 ms: 1.02x faster                                        |
| raytrace                  | 267 ms                                                 | 262 ms: 1.02x faster                                        |
| json_loads                | 27.2 us                                                | 26.8 us: 1.02x faster                                       |
| json_dumps                | 10.6 ms                                                | 10.4 ms: 1.02x faster                                       |
| sqlglot_optimize          | 53.7 ms                                                | 53.0 ms: 1.01x faster                                       |
| spectral_norm             | 115 ms                                                 | 114 ms: 1.01x faster                                        |
| pickle_pure_python        | 310 us                                                 | 307 us: 1.01x faster                                        |
| pprint_safe_repr          | 728 ms                                                 | 721 ms: 1.01x faster                                        |
| unpickle_pure_python      | 216 us                                                 | 214 us: 1.01x faster                                        |
| regex_effbot              | 3.73 ms                                                | 3.70 ms: 1.01x faster                                       |
| sqlglot_transpile         | 1.58 ms                                                | 1.57 ms: 1.01x faster                                       |
| scimark_lu                | 113 ms                                                 | 112 ms: 1.01x faster                                        |
| chaos                     | 58.1 ms                                                | 57.7 ms: 1.01x faster                                       |
| html5lib                  | 64.2 ms                                                | 63.9 ms: 1.00x faster                                       |
| scimark_monte_carlo       | 67.4 ms                                                | 67.2 ms: 1.00x faster                                       |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                        |
| python_startup_no_site    | 6.96 ms                                                | 6.98 ms: 1.00x slower                                       |
| deltablue                 | 3.23 ms                                                | 3.24 ms: 1.01x slower                                       |
| hexiom                    | 6.16 ms                                                | 6.20 ms: 1.01x slower                                       |
| bpe_tokeniser             | 4.75 sec                                               | 4.77 sec: 1.01x slower                                      |
| pyflate                   | 471 ms                                                 | 476 ms: 1.01x slower                                        |
| nbody                     | 87.0 ms                                                | 88.0 ms: 1.01x slower                                       |
| asyncio_websockets        | 552 ms                                                 | 560 ms: 1.01x slower                                        |
| mako                      | 11.1 ms                                                | 11.3 ms: 1.02x slower                                       |
| nqueens                   | 78.4 ms                                                | 80.4 ms: 1.03x slower                                       |
| docutils                  | 2.59 sec                                               | 2.66 sec: 1.03x slower                                      |
| coroutines                | 22.7 ms                                                | 23.4 ms: 1.03x slower                                       |
| xml_etree_iterparse       | 101 ms                                                 | 104 ms: 1.03x slower                                        |
| logging_silent            | 102 ns                                                 | 105 ns: 1.03x slower                                        |
| regex_dna                 | 218 ms                                                 | 229 ms: 1.05x slower                                        |
| coverage                  | 84.0 ms                                                | 89.8 ms: 1.07x slower                                       |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                |

Benchmark hidden because not significant (12): async_generators, comprehensions, dulwich_log, scimark_sor, xml_etree_parse, bench_mp_pool, fannkuch, async_tree_cpu_io_mixed_tg, sqlglot_parse, async_tree_io_tg, async_tree_io, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240926-3.14.0a0-8ca892b/bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.038x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x