# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: darwin-arm64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.049x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.89x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 176 ms: 1.07x faster                                                    |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                  |
| html5lib       | 36.6 ms                                                | 33.0 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 258 ms: 1.12x faster                                                    |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 124 ms: 1.11x faster                                                    |
| async_tree_eager_tg              | 47.8 ms                                                | 43.0 ms: 1.11x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 64.7 ms: 1.08x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                    |
| async_tree_memoization           | 268 ms                                                 | 249 ms: 1.08x faster                                                    |
| async_tree_none                  | 215 ms                                                 | 202 ms: 1.07x faster                                                    |
| async_tree_none_tg               | 198 ms                                                 | 187 ms: 1.06x faster                                                    |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                    |
| async_generators                 | 295 ms                                                 | 292 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 462 ms: 1.03x slower                                                    |
| async_tree_io_tg                 | 497 ms                                                 | 545 ms: 1.10x slower                                                    |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                    |
| async_tree_eager_io              | 514 ms                                                 | 677 ms: 1.32x slower                                                    |
| async_tree_eager_io_tg           | 477 ms                                                 | 706 ms: 1.48x slower                                                    |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                    |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                            |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 45.8 ms: 1.22x faster                                                   |
| nbody          | 74.0 ms                                                | 64.2 ms: 1.15x faster                                                   |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.12x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.48 ms: 1.06x faster                                                   |
| regex_compile  | 78.6 ms                                                | 76.0 ms: 1.03x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                   |
| regex_dna      | 149 ms                                                 | 146 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                  |
| unpickle_pure_python | 164 us                                                 | 131 us: 1.25x faster                                                    |
| pickle_pure_python   | 214 us                                                 | 176 us: 1.22x faster                                                    |
| xml_etree_process    | 41.0 ms                                                | 34.2 ms: 1.20x faster                                                   |
| xml_etree_generate   | 57.0 ms                                                | 50.5 ms: 1.13x faster                                                   |
| json_dumps           | 6.52 ms                                                | 6.18 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 73.6 ms                                                | 71.4 ms: 1.03x faster                                                   |
| json_loads           | 17.0 us                                                | 16.9 us: 1.00x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 16.8 ms: 1.12x faster                                                   |
| python_startup_no_site | 14.5 ms                                                | 13.7 ms: 1.06x faster                                                   |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.43 ms: 1.19x faster                                                   |
| genshi_text     | 16.9 ms                                                | 16.5 ms: 1.02x faster                                                   |
| django_template | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                   |
| genshi_xml      | 34.4 ms                                                | 41.2 ms: 1.20x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                            |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.0 us: 1.71x faster                                                   |
| deepcopy                         | 237 us                                                 | 154 us: 1.54x faster                                                    |
| deepcopy_reduce                  | 2.07 us                                                | 1.51 us: 1.37x faster                                                   |
| create_gc_cycles                 | 1.17 ms                                                | 898 us: 1.30x faster                                                    |
| generators                       | 31.5 ms                                                | 24.4 ms: 1.29x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                  |
| unpickle_pure_python             | 164 us                                                 | 131 us: 1.25x faster                                                    |
| float                            | 56.0 ms                                                | 45.8 ms: 1.22x faster                                                   |
| pickle_pure_python               | 214 us                                                 | 176 us: 1.22x faster                                                    |
| bench_mp_pool                    | 62.5 ms                                                | 51.5 ms: 1.21x faster                                                   |
| scimark_lu                       | 76.7 ms                                                | 63.2 ms: 1.21x faster                                                   |
| scimark_sor                      | 105 ms                                                 | 87.4 ms: 1.21x faster                                                   |
| logging_simple                   | 3.60 us                                                | 3.01 us: 1.20x faster                                                   |
| xml_etree_process                | 41.0 ms                                                | 34.2 ms: 1.20x faster                                                   |
| mako                             | 7.68 ms                                                | 6.43 ms: 1.19x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                   |
| gc_traversal                     | 2.91 ms                                                | 2.46 ms: 1.19x faster                                                   |
| logging_format                   | 3.89 us                                                | 3.29 us: 1.18x faster                                                   |
| nbody                            | 74.0 ms                                                | 64.2 ms: 1.15x faster                                                   |
| spectral_norm                    | 76.3 ms                                                | 66.7 ms: 1.14x faster                                                   |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                                    |
| deltablue                        | 2.68 ms                                                | 2.35 ms: 1.14x faster                                                   |
| xml_etree_generate               | 57.0 ms                                                | 50.5 ms: 1.13x faster                                                   |
| python_startup                   | 18.9 ms                                                | 16.8 ms: 1.12x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 258 ms: 1.12x faster                                                    |
| logging_silent                   | 70.1 ns                                                | 63.0 ns: 1.11x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 124 ms: 1.11x faster                                                    |
| async_tree_eager_tg              | 47.8 ms                                                | 43.0 ms: 1.11x faster                                                   |
| html5lib                         | 36.6 ms                                                | 33.0 ms: 1.11x faster                                                   |
| thrift                           | 466 us                                                 | 424 us: 1.10x faster                                                    |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                                    |
| nqueens                          | 62.5 ms                                                | 57.7 ms: 1.08x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 64.7 ms: 1.08x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 93.6 us: 1.08x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                    |
| async_tree_memoization           | 268 ms                                                 | 249 ms: 1.08x faster                                                    |
| async_tree_none                  | 215 ms                                                 | 202 ms: 1.07x faster                                                    |
| fannkuch                         | 284 ms                                                 | 266 ms: 1.07x faster                                                    |
| 2to3                             | 187 ms                                                 | 176 ms: 1.07x faster                                                    |
| bench_thread_pool                | 505 us                                                 | 474 us: 1.07x faster                                                    |
| pyflate                          | 351 ms                                                 | 330 ms: 1.06x faster                                                    |
| regex_effbot                     | 2.63 ms                                                | 2.48 ms: 1.06x faster                                                   |
| python_startup_no_site           | 14.5 ms                                                | 13.7 ms: 1.06x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 187 ms: 1.06x faster                                                    |
| bpe_tokeniser                    | 3.25 sec                                               | 3.07 sec: 1.06x faster                                                  |
| json_dumps                       | 6.52 ms                                                | 6.18 ms: 1.06x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 48.0 ms: 1.05x faster                                                   |
| pprint_safe_repr                 | 533 ms                                                 | 509 ms: 1.05x faster                                                    |
| raytrace                         | 181 ms                                                 | 173 ms: 1.05x faster                                                    |
| pprint_pformat                   | 1.08 sec                                               | 1.04 sec: 1.05x faster                                                  |
| crypto_pyaes                     | 54.2 ms                                                | 52.0 ms: 1.04x faster                                                   |
| json                             | 3.03 ms                                                | 2.92 ms: 1.04x faster                                                   |
| sqlglot_normalize                | 189 ms                                                 | 182 ms: 1.04x faster                                                    |
| regex_compile                    | 78.6 ms                                                | 76.0 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                    |
| xml_etree_iterparse              | 73.6 ms                                                | 71.4 ms: 1.03x faster                                                   |
| coverage                         | 46.0 ms                                                | 44.7 ms: 1.03x faster                                                   |
| chaos                            | 41.2 ms                                                | 40.1 ms: 1.03x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                   |
| pycparser                        | 705 ms                                                 | 688 ms: 1.03x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                    |
| genshi_text                      | 16.9 ms                                                | 16.5 ms: 1.02x faster                                                   |
| telco                            | 4.76 ms                                                | 4.65 ms: 1.02x faster                                                   |
| hexiom                           | 4.86 ms                                                | 4.75 ms: 1.02x faster                                                   |
| regex_dna                        | 149 ms                                                 | 146 ms: 1.02x faster                                                    |
| mdp                              | 1.49 sec                                               | 1.47 sec: 1.02x faster                                                  |
| async_generators                 | 295 ms                                                 | 292 ms: 1.01x faster                                                    |
| sympy_str                        | 145 ms                                                 | 144 ms: 1.01x faster                                                    |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                    |
| json_loads                       | 17.0 us                                                | 16.9 us: 1.00x faster                                                   |
| meteor_contest                   | 74.0 ms                                                | 74.4 ms: 1.01x slower                                                   |
| sympy_expand                     | 246 ms                                                 | 248 ms: 1.01x slower                                                    |
| django_template                  | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                   |
| sympy_sum                        | 75.4 ms                                                | 76.4 ms: 1.01x slower                                                   |
| sqlglot_optimize                 | 34.9 ms                                                | 35.4 ms: 1.01x slower                                                   |
| sqlglot_transpile                | 1.02 ms                                                | 1.04 ms: 1.02x slower                                                   |
| dulwich_log                      | 28.5 ms                                                | 29.1 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 462 ms: 1.03x slower                                                    |
| sympy_integrate                  | 11.3 ms                                                | 11.7 ms: 1.03x slower                                                   |
| comprehensions                   | 12.3 us                                                | 12.8 us: 1.05x slower                                                   |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 545 ms: 1.10x slower                                                    |
| pylint                           | 180 ms                                                 | 206 ms: 1.15x slower                                                    |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                    |
| richards_super                   | 39.1 ms                                                | 46.7 ms: 1.19x slower                                                   |
| genshi_xml                       | 34.4 ms                                                | 41.2 ms: 1.20x slower                                                   |
| richards                         | 35.2 ms                                                | 44.6 ms: 1.27x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 677 ms: 1.32x slower                                                    |
| async_tree_eager_io_tg           | 477 ms                                                 | 706 ms: 1.48x slower                                                    |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                    |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (6): pathlib, sqlglot_parse, scimark_sparse_mat_mult, xml_etree_parse, async_tree_cpu_io_mixed, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.049x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.89x