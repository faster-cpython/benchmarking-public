# Results vs. base

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: darwin-arm64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.021x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 214 ms                                                                 | 193 ms: 1.11x faster                                                         |
| html5lib       | 33.1 ms                                                                | 33.5 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines                       | 18.0 ms                                                                | 17.6 ms: 1.02x faster                                                        |
| async_tree_eager_cpu_io_mixed_tg | 341 ms                                                                 | 343 ms: 1.01x slower                                                         |
| async_generators                 | 304 ms                                                                 | 307 ms: 1.01x slower                                                         |
| async_tree_none                  | 208 ms                                                                 | 212 ms: 1.02x slower                                                         |
| async_tree_eager                 | 67.3 ms                                                                | 69.3 ms: 1.03x slower                                                        |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (14): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_eager_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_io, async_tree_eager_cpu_io_mixed, async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 48.8 ms                                                                | 51.2 ms: 1.05x slower                                                        |
| nbody          | 63.6 ms                                                                | 72.8 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.06x slower                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 16.2 ms                                                                | 16.0 ms: 1.01x faster                                                        |
| regex_effbot   | 2.32 ms                                                                | 2.33 ms: 1.00x slower                                                        |
| regex_dna      | 137 ms                                                                 | 141 ms: 1.03x slower                                                         |
| regex_compile  | 76.0 ms                                                                | 79.1 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 72.7 ms                                                                | 74.1 ms: 1.02x slower                                                        |
| json_dumps           | 7.07 ms                                                                | 7.27 ms: 1.03x slower                                                        |
| pickle_pure_python   | 194 us                                                                 | 201 us: 1.04x slower                                                         |
| tomli_loads          | 1.26 sec                                                               | 1.30 sec: 1.04x slower                                                       |
| xml_etree_process    | 35.2 ms                                                                | 36.6 ms: 1.04x slower                                                        |
| xml_etree_generate   | 49.3 ms                                                                | 51.4 ms: 1.04x slower                                                        |
| unpickle_pure_python | 142 us                                                                 | 148 us: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.03x slower                                                                 |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 19.8 ms                                                                | 19.7 ms: 1.01x faster                                                        |
| python_startup_no_site | 15.1 ms                                                                | 15.0 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 23.2 ms                                                                | 23.8 ms: 1.03x slower                                                        |
| genshi_text     | 16.6 ms                                                                | 17.2 ms: 1.03x slower                                                        |
| genshi_xml      | 40.0 ms                                                                | 42.0 ms: 1.05x slower                                                        |
| mako            | 6.25 ms                                                                | 6.61 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3                             | 214 ms                                                                 | 193 ms: 1.11x faster                                                         |
| sqlalchemy_declarative           | 65.4 ms                                                                | 63.7 ms: 1.03x faster                                                        |
| coroutines                       | 18.0 ms                                                                | 17.6 ms: 1.02x faster                                                        |
| richards_super                   | 39.2 ms                                                                | 38.5 ms: 1.02x faster                                                        |
| regex_v8                         | 16.2 ms                                                                | 16.0 ms: 1.01x faster                                                        |
| sqlalchemy_imperative            | 6.76 ms                                                                | 6.72 ms: 1.01x faster                                                        |
| coverage                         | 44.5 ms                                                                | 44.3 ms: 1.01x faster                                                        |
| python_startup                   | 19.8 ms                                                                | 19.7 ms: 1.01x faster                                                        |
| python_startup_no_site           | 15.1 ms                                                                | 15.0 ms: 1.00x faster                                                        |
| bench_mp_pool                    | 65.3 ms                                                                | 65.2 ms: 1.00x faster                                                        |
| regex_effbot                     | 2.32 ms                                                                | 2.33 ms: 1.00x slower                                                        |
| richards                         | 34.7 ms                                                                | 34.8 ms: 1.00x slower                                                        |
| async_tree_eager_cpu_io_mixed_tg | 341 ms                                                                 | 343 ms: 1.01x slower                                                         |
| mdp                              | 1.60 sec                                                               | 1.61 sec: 1.01x slower                                                       |
| sqlite_synth                     | 1.54 us                                                                | 1.55 us: 1.01x slower                                                        |
| many_optionals                   | 386 us                                                                 | 388 us: 1.01x slower                                                         |
| json                             | 2.85 ms                                                                | 2.88 ms: 1.01x slower                                                        |
| async_generators                 | 304 ms                                                                 | 307 ms: 1.01x slower                                                         |
| html5lib                         | 33.1 ms                                                                | 33.5 ms: 1.01x slower                                                        |
| sympy_expand                     | 256 ms                                                                 | 259 ms: 1.01x slower                                                         |
| k_core                           | 2.22 sec                                                               | 2.25 sec: 1.01x slower                                                       |
| pprint_pformat                   | 1.02 sec                                                               | 1.04 sec: 1.01x slower                                                       |
| pylint                           | 185 ms                                                                 | 188 ms: 1.02x slower                                                         |
| sympy_sum                        | 81.2 ms                                                                | 82.5 ms: 1.02x slower                                                        |
| subparsers                       | 12.3 ms                                                                | 12.5 ms: 1.02x slower                                                        |
| dulwich_log                      | 28.9 ms                                                                | 29.4 ms: 1.02x slower                                                        |
| shortest_path                    | 327 ms                                                                 | 333 ms: 1.02x slower                                                         |
| bench_thread_pool                | 490 us                                                                 | 499 us: 1.02x slower                                                         |
| async_tree_none                  | 208 ms                                                                 | 212 ms: 1.02x slower                                                         |
| pycparser                        | 687 ms                                                                 | 700 ms: 1.02x slower                                                         |
| xml_etree_iterparse              | 72.7 ms                                                                | 74.1 ms: 1.02x slower                                                        |
| nqueens                          | 62.2 ms                                                                | 63.4 ms: 1.02x slower                                                        |
| typing_runtime_protocols         | 100.0 us                                                               | 102 us: 1.02x slower                                                         |
| sympy_str                        | 155 ms                                                                 | 158 ms: 1.02x slower                                                         |
| telco                            | 4.55 ms                                                                | 4.65 ms: 1.02x slower                                                        |
| fannkuch                         | 258 ms                                                                 | 264 ms: 1.02x slower                                                         |
| connected_components             | 296 ms                                                                 | 303 ms: 1.02x slower                                                         |
| deepcopy                         | 159 us                                                                 | 163 us: 1.02x slower                                                         |
| django_template                  | 23.2 ms                                                                | 23.8 ms: 1.03x slower                                                        |
| sqlglot_parse                    | 879 us                                                                 | 903 us: 1.03x slower                                                         |
| logging_format                   | 3.62 us                                                                | 3.72 us: 1.03x slower                                                        |
| deepcopy_reduce                  | 1.56 us                                                                | 1.60 us: 1.03x slower                                                        |
| sqlglot_optimize                 | 37.9 ms                                                                | 39.0 ms: 1.03x slower                                                        |
| json_dumps                       | 7.07 ms                                                                | 7.27 ms: 1.03x slower                                                        |
| sqlglot_transpile                | 1.07 ms                                                                | 1.11 ms: 1.03x slower                                                        |
| sympy_integrate                  | 12.8 ms                                                                | 13.2 ms: 1.03x slower                                                        |
| async_tree_eager                 | 67.3 ms                                                                | 69.3 ms: 1.03x slower                                                        |
| logging_simple                   | 3.31 us                                                                | 3.41 us: 1.03x slower                                                        |
| sqlglot_normalize                | 191 ms                                                                 | 197 ms: 1.03x slower                                                         |
| regex_dna                        | 137 ms                                                                 | 141 ms: 1.03x slower                                                         |
| crypto_pyaes                     | 54.5 ms                                                                | 56.3 ms: 1.03x slower                                                        |
| genshi_text                      | 16.6 ms                                                                | 17.2 ms: 1.03x slower                                                        |
| bpe_tokeniser                    | 2.98 sec                                                               | 3.08 sec: 1.03x slower                                                       |
| scimark_sparse_mat_mult          | 3.07 ms                                                                | 3.17 ms: 1.03x slower                                                        |
| chaos                            | 43.7 ms                                                                | 45.2 ms: 1.04x slower                                                        |
| meteor_contest                   | 74.3 ms                                                                | 76.9 ms: 1.04x slower                                                        |
| pickle_pure_python               | 194 us                                                                 | 201 us: 1.04x slower                                                         |
| tomli_loads                      | 1.26 sec                                                               | 1.30 sec: 1.04x slower                                                       |
| xml_etree_process                | 35.2 ms                                                                | 36.6 ms: 1.04x slower                                                        |
| regex_compile                    | 76.0 ms                                                                | 79.1 ms: 1.04x slower                                                        |
| xml_etree_generate               | 49.3 ms                                                                | 51.4 ms: 1.04x slower                                                        |
| unpickle_pure_python             | 142 us                                                                 | 148 us: 1.04x slower                                                         |
| pprint_safe_repr                 | 485 ms                                                                 | 507 ms: 1.04x slower                                                         |
| go                               | 101 ms                                                                 | 106 ms: 1.05x slower                                                         |
| raytrace                         | 186 ms                                                                 | 195 ms: 1.05x slower                                                         |
| genshi_xml                       | 40.0 ms                                                                | 42.0 ms: 1.05x slower                                                        |
| float                            | 48.8 ms                                                                | 51.2 ms: 1.05x slower                                                        |
| mako                             | 6.25 ms                                                                | 6.61 ms: 1.06x slower                                                        |
| scimark_fft                      | 185 ms                                                                 | 196 ms: 1.06x slower                                                         |
| pyflate                          | 326 ms                                                                 | 347 ms: 1.07x slower                                                         |
| scimark_monte_carlo              | 45.0 ms                                                                | 48.0 ms: 1.07x slower                                                        |
| deltablue                        | 2.61 ms                                                                | 2.79 ms: 1.07x slower                                                        |
| spectral_norm                    | 70.1 ms                                                                | 75.2 ms: 1.07x slower                                                        |
| comprehensions                   | 13.5 us                                                                | 14.4 us: 1.07x slower                                                        |
| scimark_lu                       | 68.7 ms                                                                | 73.7 ms: 1.07x slower                                                        |
| generators                       | 26.6 ms                                                                | 28.6 ms: 1.08x slower                                                        |
| deepcopy_memo                    | 17.6 us                                                                | 19.2 us: 1.09x slower                                                        |
| scimark_sor                      | 87.6 ms                                                                | 96.4 ms: 1.10x slower                                                        |
| hexiom                           | 5.06 ms                                                                | 5.60 ms: 1.11x slower                                                        |
| nbody                            | 63.6 ms                                                                | 72.8 ms: 1.14x slower                                                        |
| logging_silent                   | 74.1 ns                                                                | 85.0 ns: 1.15x slower                                                        |
| Geometric mean                   | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (23): async_tree_cpu_io_mixed_tg, xml_etree_parse, create_gc_cycles, async_tree_memoization_tg, thrift, docutils, pidigits, asyncio_websockets, async_tree_eager_tg, async_tree_cpu_io_mixed, json_loads, async_tree_io_tg, pathlib, async_tree_eager_io_tg, async_tree_eager_memoization_tg, gc_traversal, async_tree_eager_io, async_tree_eager_cpu_io_mixed, async_tree_none_tg, async_tree_io, async_tree_memoization, sphinx, async_tree_eager_memoization

- Geometric mean (including insignificant results): 1.021x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x