# Results vs. base

- fork: brandtbucher
- ref: jump_backoff
- machine: darwin-arm64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.012x faster
- HPT reliability: 99.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 213 ms                                                                 | 177 ms: 1.20x faster                                                 |
| docutils       | 1.60 sec                                                               | 1.55 sec: 1.03x faster                                               |
| html5lib       | 32.9 ms                                                                | 32.6 ms: 1.01x faster                                                |
| sphinx         | 676 ms                                                                 | 649 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.07x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines                       | 17.6 ms                                                                | 17.4 ms: 1.01x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 341 ms                                                                 | 340 ms: 1.00x faster                                                 |
| async_tree_eager_tg              | 45.2 ms                                                                | 45.6 ms: 1.01x slower                                                |
| async_tree_eager                 | 66.2 ms                                                                | 67.3 ms: 1.02x slower                                                |
| async_tree_none_tg               | 206 ms                                                                 | 218 ms: 1.06x slower                                                 |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (14): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, asyncio_websockets, async_tree_none, async_tree_eager_io, async_generators, async_tree_memoization, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 63.5 ms                                                                | 63.0 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 75.5 ms                                                                | 73.4 ms: 1.03x faster                                                |
| regex_v8       | 15.9 ms                                                                | 15.8 ms: 1.01x faster                                                |
| regex_dna      | 137 ms                                                                 | 136 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 141 us                                                                 | 122 us: 1.15x faster                                                 |
| xml_etree_parse      | 106 ms                                                                 | 105 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 72.8 ms                                                                | 72.0 ms: 1.01x faster                                                |
| json_dumps           | 7.09 ms                                                                | 7.11 ms: 1.00x slower                                                |
| xml_etree_generate   | 49.5 ms                                                                | 49.8 ms: 1.01x slower                                                |
| pickle_pure_python   | 192 us                                                                 | 194 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (3): json_loads, tomli_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 15.1 ms                                                                | 15.0 ms: 1.01x faster                                                |
| python_startup         | 19.8 ms                                                                | 19.7 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 16.7 ms                                                                | 15.7 ms: 1.06x faster                                                |
| django_template | 23.3 ms                                                                | 22.3 ms: 1.05x faster                                                |
| genshi_xml      | 39.1 ms                                                                | 38.6 ms: 1.01x faster                                                |
| mako            | 6.26 ms                                                                | 6.23 ms: 1.00x faster                                                |
| Geometric mean  | (ref)                                                                  | 1.03x faster                                                         |

All benchmarks:
===============

| Benchmark                        | bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3                             | 213 ms                                                                 | 177 ms: 1.20x faster                                                 |
| unpickle_pure_python             | 141 us                                                                 | 122 us: 1.15x faster                                                 |
| pylint                           | 216 ms                                                                 | 195 ms: 1.11x faster                                                 |
| sqlalchemy_declarative           | 65.5 ms                                                                | 59.4 ms: 1.10x faster                                                |
| sqlglot_optimize                 | 37.8 ms                                                                | 34.9 ms: 1.08x faster                                                |
| sympy_integrate                  | 12.8 ms                                                                | 12.0 ms: 1.07x faster                                                |
| genshi_text                      | 16.7 ms                                                                | 15.7 ms: 1.06x faster                                                |
| sympy_sum                        | 80.5 ms                                                                | 75.8 ms: 1.06x faster                                                |
| richards_super                   | 39.6 ms                                                                | 37.3 ms: 1.06x faster                                                |
| bench_mp_pool                    | 65.6 ms                                                                | 62.2 ms: 1.06x faster                                                |
| richards                         | 35.1 ms                                                                | 33.4 ms: 1.05x faster                                                |
| sympy_str                        | 154 ms                                                                 | 147 ms: 1.05x faster                                                 |
| django_template                  | 23.3 ms                                                                | 22.3 ms: 1.05x faster                                                |
| sphinx                           | 676 ms                                                                 | 649 ms: 1.04x faster                                                 |
| sqlglot_normalize                | 194 ms                                                                 | 187 ms: 1.04x faster                                                 |
| sqlglot_transpile                | 1.09 ms                                                                | 1.06 ms: 1.03x faster                                                |
| hexiom                           | 5.08 ms                                                                | 4.93 ms: 1.03x faster                                                |
| docutils                         | 1.60 sec                                                               | 1.55 sec: 1.03x faster                                               |
| regex_compile                    | 75.5 ms                                                                | 73.4 ms: 1.03x faster                                                |
| sqlalchemy_imperative            | 6.77 ms                                                                | 6.64 ms: 1.02x faster                                                |
| meteor_contest                   | 73.7 ms                                                                | 72.6 ms: 1.02x faster                                                |
| xml_etree_parse                  | 106 ms                                                                 | 105 ms: 1.01x faster                                                 |
| genshi_xml                       | 39.1 ms                                                                | 38.6 ms: 1.01x faster                                                |
| deltablue                        | 2.62 ms                                                                | 2.59 ms: 1.01x faster                                                |
| pprint_safe_repr                 | 485 ms                                                                 | 480 ms: 1.01x faster                                                 |
| sqlglot_parse                    | 883 us                                                                 | 873 us: 1.01x faster                                                 |
| xml_etree_iterparse              | 72.8 ms                                                                | 72.0 ms: 1.01x faster                                                |
| pycparser                        | 680 ms                                                                 | 672 ms: 1.01x faster                                                 |
| bench_thread_pool                | 487 us                                                                 | 482 us: 1.01x faster                                                 |
| python_startup_no_site           | 15.1 ms                                                                | 15.0 ms: 1.01x faster                                                |
| html5lib                         | 32.9 ms                                                                | 32.6 ms: 1.01x faster                                                |
| coroutines                       | 17.6 ms                                                                | 17.4 ms: 1.01x faster                                                |
| go                               | 101 ms                                                                 | 99.9 ms: 1.01x faster                                                |
| generators                       | 26.9 ms                                                                | 26.7 ms: 1.01x faster                                                |
| regex_v8                         | 15.9 ms                                                                | 15.8 ms: 1.01x faster                                                |
| nbody                            | 63.5 ms                                                                | 63.0 ms: 1.01x faster                                                |
| nqueens                          | 61.7 ms                                                                | 61.3 ms: 1.01x faster                                                |
| typing_runtime_protocols         | 99.9 us                                                                | 99.2 us: 1.01x faster                                                |
| regex_dna                        | 137 ms                                                                 | 136 ms: 1.01x faster                                                 |
| python_startup                   | 19.8 ms                                                                | 19.7 ms: 1.01x faster                                                |
| coverage                         | 44.5 ms                                                                | 44.3 ms: 1.01x faster                                                |
| sympy_expand                     | 257 ms                                                                 | 255 ms: 1.00x faster                                                 |
| mako                             | 6.26 ms                                                                | 6.23 ms: 1.00x faster                                                |
| deepcopy_reduce                  | 1.55 us                                                                | 1.54 us: 1.00x faster                                                |
| chaos                            | 43.5 ms                                                                | 43.4 ms: 1.00x faster                                                |
| sqlite_synth                     | 1.54 us                                                                | 1.54 us: 1.00x faster                                                |
| pprint_pformat                   | 985 ms                                                                 | 982 ms: 1.00x faster                                                 |
| scimark_sor                      | 87.4 ms                                                                | 87.2 ms: 1.00x faster                                                |
| spectral_norm                    | 69.9 ms                                                                | 69.8 ms: 1.00x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 341 ms                                                                 | 340 ms: 1.00x faster                                                 |
| crypto_pyaes                     | 54.6 ms                                                                | 54.8 ms: 1.00x slower                                                |
| json_dumps                       | 7.09 ms                                                                | 7.11 ms: 1.00x slower                                                |
| mdp                              | 1.58 sec                                                               | 1.59 sec: 1.00x slower                                               |
| gc_traversal                     | 2.92 ms                                                                | 2.93 ms: 1.00x slower                                                |
| scimark_monte_carlo              | 45.0 ms                                                                | 45.2 ms: 1.00x slower                                                |
| scimark_fft                      | 185 ms                                                                 | 186 ms: 1.00x slower                                                 |
| logging_silent                   | 73.4 ns                                                                | 73.8 ns: 1.00x slower                                                |
| pyflate                          | 326 ms                                                                 | 328 ms: 1.01x slower                                                 |
| dulwich_log                      | 28.9 ms                                                                | 29.1 ms: 1.01x slower                                                |
| xml_etree_generate               | 49.5 ms                                                                | 49.8 ms: 1.01x slower                                                |
| comprehensions                   | 13.6 us                                                                | 13.7 us: 1.01x slower                                                |
| pathlib                          | 22.7 ms                                                                | 22.9 ms: 1.01x slower                                                |
| async_tree_eager_tg              | 45.2 ms                                                                | 45.6 ms: 1.01x slower                                                |
| pickle_pure_python               | 192 us                                                                 | 194 us: 1.01x slower                                                 |
| raytrace                         | 184 ms                                                                 | 186 ms: 1.01x slower                                                 |
| thrift                           | 437 us                                                                 | 441 us: 1.01x slower                                                 |
| logging_simple                   | 3.30 us                                                                | 3.33 us: 1.01x slower                                                |
| k_core                           | 2.24 sec                                                               | 2.26 sec: 1.01x slower                                               |
| shortest_path                    | 328 ms                                                                 | 332 ms: 1.01x slower                                                 |
| logging_format                   | 3.62 us                                                                | 3.66 us: 1.01x slower                                                |
| create_gc_cycles                 | 1.31 ms                                                                | 1.33 ms: 1.01x slower                                                |
| async_tree_eager                 | 66.2 ms                                                                | 67.3 ms: 1.02x slower                                                |
| telco                            | 4.38 ms                                                                | 4.48 ms: 1.02x slower                                                |
| bpe_tokeniser                    | 2.97 sec                                                               | 3.08 sec: 1.04x slower                                               |
| async_tree_none_tg               | 206 ms                                                                 | 218 ms: 1.06x slower                                                 |
| fannkuch                         | 261 ms                                                                 | 278 ms: 1.06x slower                                                 |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (26): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, json_loads, tomli_loads, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_eager_io_tg, connected_components, float, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, scimark_lu, deepcopy_memo, deepcopy, scimark_sparse_mat_mult, asyncio_websockets, async_tree_none, async_tree_eager_io, xml_etree_process, pidigits, regex_effbot, async_generators, json, async_tree_memoization, async_tree_eager_memoization

- Geometric mean (including insignificant results): 1.012x faster
# HPT report

- Reliability score: 99.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.95x