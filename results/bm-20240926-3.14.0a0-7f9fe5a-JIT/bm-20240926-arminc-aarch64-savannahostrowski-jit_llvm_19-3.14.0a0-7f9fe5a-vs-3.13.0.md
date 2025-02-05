# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-aarch64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.070x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 374 ms: 1.23x slower                                                      |
| docutils       | 2.89 sec                                                 | 3.85 sec: 1.33x slower                                                    |
| html5lib       | 66.4 ms                                                  | 71.3 ms: 1.07x slower                                                     |
| tornado_http   | 128 ms                                                   | 146 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                    | 1.19x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 562 ms: 1.16x faster                                                      |
| async_tree_none            | 497 ms                                                   | 435 ms: 1.14x faster                                                      |
| async_tree_memoization     | 651 ms                                                   | 582 ms: 1.12x faster                                                      |
| async_tree_none_tg         | 470 ms                                                   | 421 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 743 ms: 1.04x faster                                                      |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 746 ms: 1.03x faster                                                      |
| async_generators           | 489 ms                                                   | 506 ms: 1.04x slower                                                      |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                              |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 87.4 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                    | 1.03x faster                                                              |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                     |
| regex_dna      | 253 ms                                                   | 259 ms: 1.02x slower                                                      |
| regex_effbot   | 4.89 ms                                                  | 5.00 ms: 1.02x slower                                                     |
| regex_compile  | 127 ms                                                   | 189 ms: 1.49x slower                                                      |
| Geometric mean | (ref)                                                    | 1.11x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 191 ms: 1.03x faster                                                      |
| json_loads           | 31.7 us                                                  | 31.4 us: 1.01x faster                                                     |
| xml_etree_iterparse  | 149 ms                                                   | 148 ms: 1.01x faster                                                      |
| tomli_loads          | 2.54 sec                                                 | 2.58 sec: 1.02x slower                                                    |
| unpickle_pure_python | 251 us                                                   | 263 us: 1.05x slower                                                      |
| pickle_pure_python   | 357 us                                                   | 377 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                              |

Benchmark hidden because not significant (3): xml_etree_process, json_dumps, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                                     |
| Geometric mean | (ref)                                                    | 1.09x faster                                                              |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.0 ms: 1.03x faster                                                     |
| django_template | 41.6 ms                                                  | 50.0 ms: 1.20x slower                                                     |
| genshi_text     | 27.7 ms                                                  | 34.6 ms: 1.25x slower                                                     |
| genshi_xml      | 60.3 ms                                                  | 80.5 ms: 1.33x slower                                                     |
| Geometric mean  | (ref)                                                    | 1.18x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.32 ms: 1.44x faster                                                     |
| deepcopy_memo              | 50.4 us                                                  | 36.5 us: 1.38x faster                                                     |
| python_startup             | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                                     |
| deepcopy                   | 447 us                                                   | 385 us: 1.16x faster                                                      |
| async_tree_memoization_tg  | 649 ms                                                   | 562 ms: 1.16x faster                                                      |
| async_tree_none            | 497 ms                                                   | 435 ms: 1.14x faster                                                      |
| async_tree_memoization     | 651 ms                                                   | 582 ms: 1.12x faster                                                      |
| async_tree_none_tg         | 470 ms                                                   | 421 ms: 1.12x faster                                                      |
| gc_traversal               | 5.77 ms                                                  | 5.19 ms: 1.11x faster                                                     |
| deepcopy_reduce            | 4.07 us                                                  | 3.79 us: 1.07x faster                                                     |
| float                      | 93.3 ms                                                  | 87.4 ms: 1.07x faster                                                     |
| scimark_sor                | 160 ms                                                   | 150 ms: 1.07x faster                                                      |
| pathlib                    | 22.7 ms                                                  | 21.8 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 743 ms: 1.04x faster                                                      |
| bench_mp_pool              | 7.68 ms                                                  | 7.42 ms: 1.03x faster                                                     |
| xml_etree_parse            | 197 ms                                                   | 191 ms: 1.03x faster                                                      |
| regex_v8                   | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 746 ms: 1.03x faster                                                      |
| mako                       | 13.4 ms                                                  | 13.0 ms: 1.03x faster                                                     |
| json_loads                 | 31.7 us                                                  | 31.4 us: 1.01x faster                                                     |
| xml_etree_iterparse        | 149 ms                                                   | 148 ms: 1.01x faster                                                      |
| coverage                   | 99.1 ms                                                  | 100 ms: 1.01x slower                                                      |
| tomli_loads                | 2.54 sec                                                 | 2.58 sec: 1.02x slower                                                    |
| logging_silent             | 133 ns                                                   | 136 ns: 1.02x slower                                                      |
| regex_dna                  | 253 ms                                                   | 259 ms: 1.02x slower                                                      |
| regex_effbot               | 4.89 ms                                                  | 5.00 ms: 1.02x slower                                                     |
| telco                      | 9.74 ms                                                  | 10.0 ms: 1.03x slower                                                     |
| async_generators           | 489 ms                                                   | 506 ms: 1.04x slower                                                      |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                    |
| mdp                        | 3.34 sec                                                 | 3.47 sec: 1.04x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.80 ms: 1.04x slower                                                     |
| bench_thread_pool          | 1.27 ms                                                  | 1.33 ms: 1.05x slower                                                     |
| logging_format             | 7.82 us                                                  | 8.19 us: 1.05x slower                                                     |
| unpickle_pure_python       | 251 us                                                   | 263 us: 1.05x slower                                                      |
| crypto_pyaes               | 83.7 ms                                                  | 87.9 ms: 1.05x slower                                                     |
| pickle_pure_python         | 357 us                                                   | 377 us: 1.06x slower                                                      |
| logging_simple             | 7.07 us                                                  | 7.48 us: 1.06x slower                                                     |
| fannkuch                   | 461 ms                                                   | 490 ms: 1.06x slower                                                      |
| scimark_lu                 | 139 ms                                                   | 149 ms: 1.07x slower                                                      |
| typing_runtime_protocols   | 193 us                                                   | 207 us: 1.07x slower                                                      |
| html5lib                   | 66.4 ms                                                  | 71.3 ms: 1.07x slower                                                     |
| meteor_contest             | 114 ms                                                   | 123 ms: 1.08x slower                                                      |
| scimark_monte_carlo        | 83.6 ms                                                  | 91.0 ms: 1.09x slower                                                     |
| pyflate                    | 556 ms                                                   | 623 ms: 1.12x slower                                                      |
| deltablue                  | 3.82 ms                                                  | 4.34 ms: 1.14x slower                                                     |
| raytrace                   | 300 ms                                                   | 342 ms: 1.14x slower                                                      |
| tornado_http               | 128 ms                                                   | 146 ms: 1.14x slower                                                      |
| go                         | 160 ms                                                   | 185 ms: 1.16x slower                                                      |
| pycparser                  | 1.27 sec                                                 | 1.48 sec: 1.16x slower                                                    |
| sqlglot_normalize          | 127 ms                                                   | 149 ms: 1.18x slower                                                      |
| comprehensions             | 20.4 us                                                  | 24.1 us: 1.18x slower                                                     |
| nqueens                    | 100 ms                                                   | 119 ms: 1.19x slower                                                      |
| django_template            | 41.6 ms                                                  | 50.0 ms: 1.20x slower                                                     |
| richards                   | 53.6 ms                                                  | 64.8 ms: 1.21x slower                                                     |
| richards_super             | 60.1 ms                                                  | 72.8 ms: 1.21x slower                                                     |
| 2to3                       | 304 ms                                                   | 374 ms: 1.23x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                  | 1.72 ms: 1.25x slower                                                     |
| sqlglot_transpile          | 1.73 ms                                                  | 2.16 ms: 1.25x slower                                                     |
| genshi_text                | 27.7 ms                                                  | 34.6 ms: 1.25x slower                                                     |
| sqlglot_optimize           | 62.2 ms                                                  | 79.0 ms: 1.27x slower                                                     |
| chaos                      | 68.0 ms                                                  | 88.7 ms: 1.30x slower                                                     |
| pprint_safe_repr           | 926 ms                                                   | 1.21 sec: 1.31x slower                                                    |
| sympy_expand               | 457 ms                                                   | 600 ms: 1.31x slower                                                      |
| pprint_pformat             | 1.90 sec                                                 | 2.50 sec: 1.32x slower                                                    |
| docutils                   | 2.89 sec                                                 | 3.85 sec: 1.33x slower                                                    |
| genshi_xml                 | 60.3 ms                                                  | 80.5 ms: 1.33x slower                                                     |
| sympy_integrate            | 20.8 ms                                                  | 28.2 ms: 1.35x slower                                                     |
| sympy_str                  | 264 ms                                                   | 359 ms: 1.36x slower                                                      |
| hexiom                     | 7.11 ms                                                  | 9.84 ms: 1.38x slower                                                     |
| pylint                     | 342 ms                                                   | 474 ms: 1.39x slower                                                      |
| sympy_sum                  | 144 ms                                                   | 208 ms: 1.45x slower                                                      |
| regex_compile              | 127 ms                                                   | 189 ms: 1.49x slower                                                      |
| generators                 | 37.6 ms                                                  | 56.9 ms: 1.51x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.07x slower                                                              |

Benchmark hidden because not significant (13): xml_etree_process, json, nbody, json_dumps, thrift, bpe_tokeniser, coroutines, xml_etree_generate, python_startup_no_site, pidigits, scimark_fft, asyncio_websockets, spectral_norm
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.070x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.99x