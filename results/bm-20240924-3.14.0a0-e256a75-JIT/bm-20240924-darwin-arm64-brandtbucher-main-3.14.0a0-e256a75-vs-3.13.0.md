# Results vs. 3.13.0

- fork: brandtbucher
- ref: main
- machine: darwin-arm64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.052x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.54x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 175 ms: 1.07x faster                                        |
| docutils       | 1.44 sec                                               | 1.55 sec: 1.08x slower                                      |
| html5lib       | 36.6 ms                                                | 32.6 ms: 1.12x faster                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                       |
| async_tree_eager_tg              | 47.8 ms                                                | 42.3 ms: 1.13x faster                                       |
| async_tree_memoization_tg        | 288 ms                                                 | 256 ms: 1.13x faster                                        |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 123 ms: 1.12x faster                                        |
| async_tree_eager                 | 70.1 ms                                                | 63.8 ms: 1.10x faster                                       |
| async_tree_memoization           | 268 ms                                                 | 247 ms: 1.09x faster                                        |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.08x faster                                        |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                        |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.06x faster                                        |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.04x faster                                        |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                        |
| async_generators                 | 295 ms                                                 | 293 ms: 1.01x faster                                        |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 459 ms: 1.02x slower                                        |
| async_tree_io_tg                 | 497 ms                                                 | 554 ms: 1.12x slower                                        |
| async_tree_io                    | 507 ms                                                 | 589 ms: 1.16x slower                                        |
| async_tree_eager_io              | 514 ms                                                 | 677 ms: 1.32x slower                                        |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                        |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                        |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 56.0 ms                                                | 46.1 ms: 1.22x faster                                       |
| nbody          | 74.0 ms                                                | 63.5 ms: 1.17x faster                                       |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                  | 1.13x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                       |
| regex_compile  | 78.6 ms                                                | 75.6 ms: 1.04x faster                                       |
| regex_v8       | 17.0 ms                                                | 16.6 ms: 1.03x faster                                       |
| regex_dna      | 149 ms                                                 | 145 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.25 sec: 1.26x faster                                      |
| unpickle_pure_python | 164 us                                                 | 131 us: 1.25x faster                                        |
| pickle_pure_python   | 214 us                                                 | 178 us: 1.21x faster                                        |
| xml_etree_process    | 41.0 ms                                                | 34.0 ms: 1.20x faster                                       |
| xml_etree_generate   | 57.0 ms                                                | 49.7 ms: 1.15x faster                                       |
| json_dumps           | 6.52 ms                                                | 6.31 ms: 1.03x faster                                       |
| xml_etree_iterparse  | 73.6 ms                                                | 71.6 ms: 1.03x faster                                       |
| json_loads           | 17.0 us                                                | 16.8 us: 1.01x faster                                       |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 15.3 ms: 1.23x faster                                       |
| python_startup_no_site | 14.5 ms                                                | 12.5 ms: 1.16x faster                                       |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.48 ms: 1.19x faster                                       |
| django_template | 22.2 ms                                                | 22.4 ms: 1.01x slower                                       |
| genshi_text     | 16.9 ms                                                | 17.1 ms: 1.01x slower                                       |
| genshi_xml      | 34.4 ms                                                | 41.6 ms: 1.21x slower                                       |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.3 us: 1.68x faster                                       |
| deepcopy                         | 237 us                                                 | 155 us: 1.53x faster                                        |
| deepcopy_reduce                  | 2.07 us                                                | 1.52 us: 1.37x faster                                       |
| create_gc_cycles                 | 1.17 ms                                                | 902 us: 1.30x faster                                        |
| generators                       | 31.5 ms                                                | 24.4 ms: 1.29x faster                                       |
| tomli_loads                      | 1.57 sec                                               | 1.25 sec: 1.26x faster                                      |
| unpickle_pure_python             | 164 us                                                 | 131 us: 1.25x faster                                        |
| python_startup                   | 18.9 ms                                                | 15.3 ms: 1.23x faster                                       |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                       |
| bench_mp_pool                    | 62.5 ms                                                | 50.9 ms: 1.23x faster                                       |
| float                            | 56.0 ms                                                | 46.1 ms: 1.22x faster                                       |
| logging_simple                   | 3.60 us                                                | 2.97 us: 1.21x faster                                       |
| pickle_pure_python               | 214 us                                                 | 178 us: 1.21x faster                                        |
| xml_etree_process                | 41.0 ms                                                | 34.0 ms: 1.20x faster                                       |
| scimark_lu                       | 76.7 ms                                                | 63.7 ms: 1.20x faster                                       |
| scimark_sor                      | 105 ms                                                 | 87.8 ms: 1.20x faster                                       |
| logging_format                   | 3.89 us                                                | 3.27 us: 1.19x faster                                       |
| gc_traversal                     | 2.91 ms                                                | 2.45 ms: 1.19x faster                                       |
| mako                             | 7.68 ms                                                | 6.48 ms: 1.19x faster                                       |
| nbody                            | 74.0 ms                                                | 63.5 ms: 1.17x faster                                       |
| python_startup_no_site           | 14.5 ms                                                | 12.5 ms: 1.16x faster                                       |
| xml_etree_generate               | 57.0 ms                                                | 49.7 ms: 1.15x faster                                       |
| deltablue                        | 2.68 ms                                                | 2.35 ms: 1.14x faster                                       |
| spectral_norm                    | 76.3 ms                                                | 67.0 ms: 1.14x faster                                       |
| logging_silent                   | 70.1 ns                                                | 62.0 ns: 1.13x faster                                       |
| async_tree_eager_tg              | 47.8 ms                                                | 42.3 ms: 1.13x faster                                       |
| async_tree_memoization_tg        | 288 ms                                                 | 256 ms: 1.13x faster                                        |
| html5lib                         | 36.6 ms                                                | 32.6 ms: 1.12x faster                                       |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 123 ms: 1.12x faster                                        |
| go                               | 115 ms                                                 | 103 ms: 1.11x faster                                        |
| thrift                           | 466 us                                                 | 423 us: 1.10x faster                                        |
| async_tree_eager                 | 70.1 ms                                                | 63.8 ms: 1.10x faster                                       |
| async_tree_memoization           | 268 ms                                                 | 247 ms: 1.09x faster                                        |
| nqueens                          | 62.5 ms                                                | 57.7 ms: 1.08x faster                                       |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.08x faster                                        |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                        |
| scimark_fft                      | 201 ms                                                 | 186 ms: 1.08x faster                                        |
| pprint_safe_repr                 | 533 ms                                                 | 495 ms: 1.08x faster                                        |
| pyflate                          | 351 ms                                                 | 328 ms: 1.07x faster                                        |
| fannkuch                         | 284 ms                                                 | 265 ms: 1.07x faster                                        |
| bench_thread_pool                | 505 us                                                 | 471 us: 1.07x faster                                        |
| 2to3                             | 187 ms                                                 | 175 ms: 1.07x faster                                        |
| pprint_pformat                   | 1.08 sec                                               | 1.01 sec: 1.07x faster                                      |
| regex_effbot                     | 2.63 ms                                                | 2.46 ms: 1.07x faster                                       |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.06x faster                                        |
| typing_runtime_protocols         | 101 us                                                 | 95.2 us: 1.06x faster                                       |
| bpe_tokeniser                    | 3.25 sec                                               | 3.06 sec: 1.06x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 47.9 ms: 1.05x faster                                       |
| raytrace                         | 181 ms                                                 | 173 ms: 1.04x faster                                        |
| crypto_pyaes                     | 54.2 ms                                                | 52.1 ms: 1.04x faster                                       |
| sqlglot_normalize                | 189 ms                                                 | 181 ms: 1.04x faster                                        |
| regex_compile                    | 78.6 ms                                                | 75.6 ms: 1.04x faster                                       |
| pycparser                        | 705 ms                                                 | 680 ms: 1.04x faster                                        |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.04x faster                                        |
| coverage                         | 46.0 ms                                                | 44.4 ms: 1.04x faster                                       |
| json_dumps                       | 6.52 ms                                                | 6.31 ms: 1.03x faster                                       |
| json                             | 3.03 ms                                                | 2.94 ms: 1.03x faster                                       |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                        |
| chaos                            | 41.2 ms                                                | 40.0 ms: 1.03x faster                                       |
| xml_etree_iterparse              | 73.6 ms                                                | 71.6 ms: 1.03x faster                                       |
| regex_v8                         | 17.0 ms                                                | 16.6 ms: 1.03x faster                                       |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.02x faster                                        |
| mdp                              | 1.49 sec                                               | 1.46 sec: 1.02x faster                                      |
| hexiom                           | 4.86 ms                                                | 4.76 ms: 1.02x faster                                       |
| sympy_str                        | 145 ms                                                 | 144 ms: 1.01x faster                                        |
| telco                            | 4.76 ms                                                | 4.72 ms: 1.01x faster                                       |
| sqlglot_parse                    | 856 us                                                 | 850 us: 1.01x faster                                        |
| async_generators                 | 295 ms                                                 | 293 ms: 1.01x faster                                        |
| json_loads                       | 17.0 us                                                | 16.8 us: 1.01x faster                                       |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                        |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.98 ms: 1.00x faster                                       |
| sympy_expand                     | 246 ms                                                 | 247 ms: 1.00x slower                                        |
| django_template                  | 22.2 ms                                                | 22.4 ms: 1.01x slower                                       |
| genshi_text                      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                       |
| sqlglot_transpile                | 1.02 ms                                                | 1.04 ms: 1.02x slower                                       |
| sqlglot_optimize                 | 34.9 ms                                                | 35.5 ms: 1.02x slower                                       |
| dulwich_log                      | 28.5 ms                                                | 29.0 ms: 1.02x slower                                       |
| meteor_contest                   | 74.0 ms                                                | 75.3 ms: 1.02x slower                                       |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.02x slower                                       |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 459 ms: 1.02x slower                                        |
| pathlib                          | 23.4 ms                                                | 24.2 ms: 1.04x slower                                       |
| comprehensions                   | 12.3 us                                                | 12.7 us: 1.04x slower                                       |
| docutils                         | 1.44 sec                                               | 1.55 sec: 1.08x slower                                      |
| async_tree_io_tg                 | 497 ms                                                 | 554 ms: 1.12x slower                                        |
| pylint                           | 180 ms                                                 | 206 ms: 1.14x slower                                        |
| async_tree_io                    | 507 ms                                                 | 589 ms: 1.16x slower                                        |
| genshi_xml                       | 34.4 ms                                                | 41.6 ms: 1.21x slower                                       |
| richards_super                   | 39.1 ms                                                | 47.6 ms: 1.22x slower                                       |
| richards                         | 35.2 ms                                                | 44.4 ms: 1.26x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 677 ms: 1.32x slower                                        |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                        |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                        |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, sympy_sum, xml_etree_parse, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.052x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.54x