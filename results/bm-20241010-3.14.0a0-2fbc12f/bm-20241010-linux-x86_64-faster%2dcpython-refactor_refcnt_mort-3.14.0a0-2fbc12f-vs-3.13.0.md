# Results vs. 3.13.0

- fork: faster-cpython
- ref: refactor_refcnt_mort
- machine: linux-x86_64
- commit hash: 2fbc12f
- commit date: 2024-10-10
- overall geometric mean: 1.013x faster
- HPT reliability: 91.45%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 256 ms: 1.04x faster                                                            |
| docutils       | 2.59 sec                                               | 2.65 sec: 1.02x slower                                                          |
| html5lib       | 64.2 ms                                                | 62.6 ms: 1.02x faster                                                           |
| tornado_http   | 92.4 ms                                                | 91.3 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 405 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 408 ms: 1.08x faster                                                            |
| async_tree_none           | 351 ms                                                 | 327 ms: 1.07x faster                                                            |
| async_tree_none_tg        | 321 ms                                                 | 311 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 561 ms: 1.03x faster                                                            |
| async_generators          | 436 ms                                                 | 438 ms: 1.01x slower                                                            |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                            |
| coroutines                | 22.7 ms                                                | 24.2 ms: 1.07x slower                                                           |
| async_tree_io_tg          | 857 ms                                                 | 917 ms: 1.07x slower                                                            |
| async_tree_io             | 842 ms                                                 | 930 ms: 1.11x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                            |
| nbody          | 87.0 ms                                                | 93.0 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.4 ms: 1.07x faster                                                           |
| regex_effbot   | 3.73 ms                                                | 3.57 ms: 1.05x faster                                                           |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                            |
| regex_dna      | 218 ms                                                 | 217 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                           |
| xml_etree_generate   | 86.7 ms                                                | 87.8 ms: 1.01x slower                                                           |
| pickle_pure_python   | 310 us                                                 | 315 us: 1.01x slower                                                            |
| tomli_loads          | 2.14 sec                                               | 2.17 sec: 1.02x slower                                                          |
| unpickle_pure_python | 216 us                                                 | 224 us: 1.04x slower                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.04x slower                                                            |
| json_dumps           | 10.6 ms                                                | 11.6 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 35.0 ms: 1.00x faster                                                           |
| genshi_xml      | 50.9 ms                                                | 51.8 ms: 1.02x slower                                                           |
| mako            | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| create_gc_cycles          | 2.41 ms                                                | 1.78 ms: 1.35x faster                                                           |
| deepcopy                  | 358 us                                                 | 268 us: 1.34x faster                                                            |
| deepcopy_memo             | 39.1 us                                                | 32.2 us: 1.22x faster                                                           |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                           |
| go                        | 144 ms                                                 | 123 ms: 1.17x faster                                                            |
| deepcopy_reduce           | 3.20 us                                                | 2.76 us: 1.16x faster                                                           |
| async_tree_memoization_tg | 464 ms                                                 | 405 ms: 1.15x faster                                                            |
| json                      | 5.36 ms                                                | 4.85 ms: 1.11x faster                                                           |
| gc_traversal              | 4.37 ms                                                | 3.98 ms: 1.10x faster                                                           |
| pathlib                   | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                           |
| async_tree_memoization    | 442 ms                                                 | 408 ms: 1.08x faster                                                            |
| mdp                       | 2.72 sec                                               | 2.52 sec: 1.08x faster                                                          |
| regex_v8                  | 26.2 ms                                                | 24.4 ms: 1.07x faster                                                           |
| async_tree_none           | 351 ms                                                 | 327 ms: 1.07x faster                                                            |
| telco                     | 8.54 ms                                                | 8.02 ms: 1.07x faster                                                           |
| regex_effbot              | 3.73 ms                                                | 3.57 ms: 1.05x faster                                                           |
| crypto_pyaes              | 75.3 ms                                                | 72.1 ms: 1.04x faster                                                           |
| 2to3                      | 267 ms                                                 | 256 ms: 1.04x faster                                                            |
| richards                  | 48.7 ms                                                | 47.1 ms: 1.03x faster                                                           |
| thrift                    | 809 us                                                 | 783 us: 1.03x faster                                                            |
| async_tree_none_tg        | 321 ms                                                 | 311 ms: 1.03x faster                                                            |
| richards_super            | 54.9 ms                                                | 53.3 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 561 ms: 1.03x faster                                                            |
| generators                | 29.0 ms                                                | 28.2 ms: 1.03x faster                                                           |
| html5lib                  | 64.2 ms                                                | 62.6 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.93 ms: 1.02x faster                                                           |
| json_loads                | 27.2 us                                                | 26.7 us: 1.02x faster                                                           |
| regex_compile             | 132 ms                                                 | 130 ms: 1.02x faster                                                            |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.01x faster                                                            |
| tornado_http              | 92.4 ms                                                | 91.3 ms: 1.01x faster                                                           |
| sympy_str                 | 275 ms                                                 | 272 ms: 1.01x faster                                                            |
| pycparser                 | 1.20 sec                                               | 1.19 sec: 1.01x faster                                                          |
| regex_dna                 | 218 ms                                                 | 217 ms: 1.01x faster                                                            |
| sympy_sum                 | 150 ms                                                 | 149 ms: 1.01x faster                                                            |
| typing_runtime_protocols  | 165 us                                                 | 163 us: 1.01x faster                                                            |
| logging_format            | 6.40 us                                                | 6.35 us: 1.01x faster                                                           |
| django_template           | 35.2 ms                                                | 35.0 ms: 1.00x faster                                                           |
| async_generators          | 436 ms                                                 | 438 ms: 1.01x slower                                                            |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                            |
| bpe_tokeniser             | 4.75 sec                                               | 4.79 sec: 1.01x slower                                                          |
| pprint_safe_repr          | 728 ms                                                 | 736 ms: 1.01x slower                                                            |
| sympy_integrate           | 19.9 ms                                                | 20.1 ms: 1.01x slower                                                           |
| pidigits                  | 186 ms                                                 | 189 ms: 1.01x slower                                                            |
| xml_etree_generate        | 86.7 ms                                                | 87.8 ms: 1.01x slower                                                           |
| pickle_pure_python        | 310 us                                                 | 315 us: 1.01x slower                                                            |
| python_startup_no_site    | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                           |
| pprint_pformat            | 1.49 sec                                               | 1.52 sec: 1.01x slower                                                          |
| sqlglot_optimize          | 53.7 ms                                                | 54.5 ms: 1.01x slower                                                           |
| tomli_loads               | 2.14 sec                                               | 2.17 sec: 1.02x slower                                                          |
| spectral_norm             | 115 ms                                                 | 117 ms: 1.02x slower                                                            |
| dulwich_log               | 64.3 ms                                                | 65.4 ms: 1.02x slower                                                           |
| genshi_xml                | 50.9 ms                                                | 51.8 ms: 1.02x slower                                                           |
| sqlglot_transpile         | 1.58 ms                                                | 1.61 ms: 1.02x slower                                                           |
| sqlglot_normalize         | 108 ms                                                 | 110 ms: 1.02x slower                                                            |
| docutils                  | 2.59 sec                                               | 2.65 sec: 1.02x slower                                                          |
| fannkuch                  | 404 ms                                                 | 413 ms: 1.02x slower                                                            |
| scimark_fft               | 364 ms                                                 | 373 ms: 1.02x slower                                                            |
| nqueens                   | 78.4 ms                                                | 80.3 ms: 1.02x slower                                                           |
| scimark_monte_carlo       | 67.4 ms                                                | 69.2 ms: 1.03x slower                                                           |
| pyflate                   | 471 ms                                                 | 483 ms: 1.03x slower                                                            |
| raytrace                  | 267 ms                                                 | 275 ms: 1.03x slower                                                            |
| sqlglot_parse             | 1.27 ms                                                | 1.31 ms: 1.03x slower                                                           |
| comprehensions            | 16.5 us                                                | 17.0 us: 1.03x slower                                                           |
| bench_thread_pool         | 822 us                                                 | 850 us: 1.03x slower                                                            |
| logging_silent            | 102 ns                                                 | 106 ns: 1.04x slower                                                            |
| hexiom                    | 6.16 ms                                                | 6.39 ms: 1.04x slower                                                           |
| unpickle_pure_python      | 216 us                                                 | 224 us: 1.04x slower                                                            |
| deltablue                 | 3.23 ms                                                | 3.36 ms: 1.04x slower                                                           |
| xml_etree_iterparse       | 101 ms                                                 | 105 ms: 1.04x slower                                                            |
| scimark_sor               | 124 ms                                                 | 129 ms: 1.04x slower                                                            |
| mako                      | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                           |
| scimark_lu                | 113 ms                                                 | 119 ms: 1.05x slower                                                            |
| chaos                     | 58.1 ms                                                | 61.2 ms: 1.05x slower                                                           |
| coroutines                | 22.7 ms                                                | 24.2 ms: 1.07x slower                                                           |
| nbody                     | 87.0 ms                                                | 93.0 ms: 1.07x slower                                                           |
| async_tree_io_tg          | 857 ms                                                 | 917 ms: 1.07x slower                                                            |
| coverage                  | 84.0 ms                                                | 91.8 ms: 1.09x slower                                                           |
| json_dumps                | 10.6 ms                                                | 11.6 ms: 1.10x slower                                                           |
| async_tree_io             | 842 ms                                                 | 930 ms: 1.11x slower                                                            |
| bench_mp_pool             | 24.0 ms                                                | 56.3 ms: 2.35x slower                                                           |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, logging_simple, sympy_expand, float, genshi_text, xml_etree_process, xml_etree_parse, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241010-3.14.0a0-2fbc12f/bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.013x faster
# HPT report

- Reliability score: 91.45% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.91x