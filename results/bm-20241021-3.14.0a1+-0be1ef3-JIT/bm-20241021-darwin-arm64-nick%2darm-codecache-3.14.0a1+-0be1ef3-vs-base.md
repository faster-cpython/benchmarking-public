# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: darwin-arm64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 183 ms                                                                 | 171 ms: 1.07x faster                                            |
| docutils       | 1.55 sec                                                               | 1.50 sec: 1.04x faster                                          |
| html5lib       | 32.3 ms                                                                | 31.2 ms: 1.04x faster                                           |
| sphinx         | 659 ms                                                                 | 618 ms: 1.07x faster                                            |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_eager                 | 64.3 ms                                                                | 61.9 ms: 1.04x faster                                           |
| async_tree_eager_tg              | 42.8 ms                                                                | 42.5 ms: 1.01x faster                                           |
| async_tree_none                  | 198 ms                                                                 | 197 ms: 1.01x faster                                            |
| async_generators                 | 292 ms                                                                 | 291 ms: 1.00x faster                                            |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                 | 335 ms: 1.00x faster                                            |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                    |

Benchmark hidden because not significant (14): async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_memoization, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io, asyncio_websockets, coroutines, async_tree_io_tg, async_tree_eager_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 48.2 ms                                                                | 48.1 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 74.7 ms                                                                | 71.0 ms: 1.05x faster                                           |
| regex_dna      | 142 ms                                                                 | 143 ms: 1.00x slower                                            |
| regex_v8       | 16.7 ms                                                                | 16.8 ms: 1.01x slower                                           |
| regex_effbot   | 2.45 ms                                                                | 2.47 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 1.25 sec                                                               | 1.23 sec: 1.01x faster                                          |
| unpickle_pure_python | 133 us                                                                 | 132 us: 1.01x faster                                            |
| xml_etree_process    | 34.5 ms                                                                | 34.3 ms: 1.00x faster                                           |
| json_dumps           | 7.13 ms                                                                | 7.12 ms: 1.00x faster                                           |
| json_loads           | 16.5 us                                                                | 16.5 us: 1.00x slower                                           |
| xml_etree_generate   | 50.0 ms                                                                | 50.3 ms: 1.00x slower                                           |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                                | 12.9 ms: 1.02x faster                                           |
| python_startup         | 17.2 ms                                                                | 16.8 ms: 1.02x faster                                           |
| Geometric mean         | (ref)                                                                  | 1.02x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 42.2 ms                                                                | 31.4 ms: 1.35x faster                                           |
| genshi_text     | 16.7 ms                                                                | 14.5 ms: 1.15x faster                                           |
| django_template | 23.1 ms                                                                | 20.3 ms: 1.14x faster                                           |
| mako            | 6.47 ms                                                                | 6.44 ms: 1.00x faster                                           |
| Geometric mean  | (ref)                                                                  | 1.15x faster                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml                       | 42.2 ms                                                                | 31.4 ms: 1.35x faster                                           |
| genshi_text                      | 16.7 ms                                                                | 14.5 ms: 1.15x faster                                           |
| django_template                  | 23.1 ms                                                                | 20.3 ms: 1.14x faster                                           |
| hexiom                           | 5.02 ms                                                                | 4.49 ms: 1.12x faster                                           |
| richards                         | 34.5 ms                                                                | 31.2 ms: 1.11x faster                                           |
| sqlglot_optimize                 | 37.3 ms                                                                | 33.7 ms: 1.11x faster                                           |
| pylint                           | 179 ms                                                                 | 161 ms: 1.11x faster                                            |
| go                               | 98.9 ms                                                                | 90.0 ms: 1.10x faster                                           |
| richards_super                   | 37.9 ms                                                                | 34.6 ms: 1.10x faster                                           |
| pprint_safe_repr                 | 497 ms                                                                 | 459 ms: 1.08x faster                                            |
| sqlglot_transpile                | 1.07 ms                                                                | 992 us: 1.08x faster                                            |
| sqlglot_normalize                | 186 ms                                                                 | 173 ms: 1.07x faster                                            |
| sympy_integrate                  | 12.6 ms                                                                | 11.7 ms: 1.07x faster                                           |
| 2to3                             | 183 ms                                                                 | 171 ms: 1.07x faster                                            |
| sphinx                           | 659 ms                                                                 | 618 ms: 1.07x faster                                            |
| sympy_sum                        | 79.6 ms                                                                | 75.0 ms: 1.06x faster                                           |
| sqlglot_parse                    | 869 us                                                                 | 823 us: 1.06x faster                                            |
| sympy_str                        | 151 ms                                                                 | 143 ms: 1.05x faster                                            |
| regex_compile                    | 74.7 ms                                                                | 71.0 ms: 1.05x faster                                           |
| pyflate                          | 327 ms                                                                 | 312 ms: 1.05x faster                                            |
| generators                       | 25.2 ms                                                                | 24.1 ms: 1.05x faster                                           |
| raytrace                         | 170 ms                                                                 | 162 ms: 1.05x faster                                            |
| sympy_expand                     | 248 ms                                                                 | 237 ms: 1.05x faster                                            |
| pycparser                        | 683 ms                                                                 | 653 ms: 1.05x faster                                            |
| deepcopy                         | 154 us                                                                 | 148 us: 1.04x faster                                            |
| pprint_pformat                   | 998 ms                                                                 | 961 ms: 1.04x faster                                            |
| async_tree_eager                 | 64.3 ms                                                                | 61.9 ms: 1.04x faster                                           |
| html5lib                         | 32.3 ms                                                                | 31.2 ms: 1.04x faster                                           |
| docutils                         | 1.55 sec                                                               | 1.50 sec: 1.04x faster                                          |
| chaos                            | 41.7 ms                                                                | 40.3 ms: 1.03x faster                                           |
| deltablue                        | 2.39 ms                                                                | 2.32 ms: 1.03x faster                                           |
| comprehensions                   | 13.0 us                                                                | 12.7 us: 1.03x faster                                           |
| meteor_contest                   | 74.4 ms                                                                | 72.5 ms: 1.03x faster                                           |
| logging_format                   | 3.39 us                                                                | 3.31 us: 1.03x faster                                           |
| logging_simple                   | 3.11 us                                                                | 3.03 us: 1.02x faster                                           |
| bench_mp_pool                    | 61.3 ms                                                                | 59.9 ms: 1.02x faster                                           |
| python_startup_no_site           | 13.2 ms                                                                | 12.9 ms: 1.02x faster                                           |
| python_startup                   | 17.2 ms                                                                | 16.8 ms: 1.02x faster                                           |
| scimark_lu                       | 66.6 ms                                                                | 65.3 ms: 1.02x faster                                           |
| dulwich_log                      | 29.1 ms                                                                | 28.5 ms: 1.02x faster                                           |
| typing_runtime_protocols         | 98.1 us                                                                | 96.7 us: 1.01x faster                                           |
| tomli_loads                      | 1.25 sec                                                               | 1.23 sec: 1.01x faster                                          |
| thrift                           | 423 us                                                                 | 417 us: 1.01x faster                                            |
| mdp                              | 1.53 sec                                                               | 1.51 sec: 1.01x faster                                          |
| unpickle_pure_python             | 133 us                                                                 | 132 us: 1.01x faster                                            |
| bench_thread_pool                | 474 us                                                                 | 470 us: 1.01x faster                                            |
| json                             | 2.86 ms                                                                | 2.84 ms: 1.01x faster                                           |
| deepcopy_memo                    | 16.8 us                                                                | 16.7 us: 1.01x faster                                           |
| async_tree_eager_tg              | 42.8 ms                                                                | 42.5 ms: 1.01x faster                                           |
| nqueens                          | 58.3 ms                                                                | 57.9 ms: 1.01x faster                                           |
| logging_silent                   | 69.7 ns                                                                | 69.3 ns: 1.01x faster                                           |
| bpe_tokeniser                    | 3.04 sec                                                               | 3.02 sec: 1.01x faster                                          |
| async_tree_none                  | 198 ms                                                                 | 197 ms: 1.01x faster                                            |
| xml_etree_process                | 34.5 ms                                                                | 34.3 ms: 1.00x faster                                           |
| mako                             | 6.47 ms                                                                | 6.44 ms: 1.00x faster                                           |
| fannkuch                         | 258 ms                                                                 | 257 ms: 1.00x faster                                            |
| gc_traversal                     | 2.95 ms                                                                | 2.93 ms: 1.00x faster                                           |
| coverage                         | 43.6 ms                                                                | 43.5 ms: 1.00x faster                                           |
| scimark_monte_carlo              | 45.6 ms                                                                | 45.4 ms: 1.00x faster                                           |
| float                            | 48.2 ms                                                                | 48.1 ms: 1.00x faster                                           |
| async_generators                 | 292 ms                                                                 | 291 ms: 1.00x faster                                            |
| scimark_sor                      | 85.9 ms                                                                | 85.7 ms: 1.00x faster                                           |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                 | 335 ms: 1.00x faster                                            |
| json_dumps                       | 7.13 ms                                                                | 7.12 ms: 1.00x faster                                           |
| regex_dna                        | 142 ms                                                                 | 143 ms: 1.00x slower                                            |
| spectral_norm                    | 69.2 ms                                                                | 69.4 ms: 1.00x slower                                           |
| json_loads                       | 16.5 us                                                                | 16.5 us: 1.00x slower                                           |
| scimark_sparse_mat_mult          | 3.15 ms                                                                | 3.17 ms: 1.00x slower                                           |
| telco                            | 4.55 ms                                                                | 4.57 ms: 1.00x slower                                           |
| xml_etree_generate               | 50.0 ms                                                                | 50.3 ms: 1.00x slower                                           |
| regex_v8                         | 16.7 ms                                                                | 16.8 ms: 1.01x slower                                           |
| regex_effbot                     | 2.45 ms                                                                | 2.47 ms: 1.01x slower                                           |
| pathlib                          | 21.9 ms                                                                | 22.3 ms: 1.02x slower                                           |
| Geometric mean                   | (ref)                                                                  | 1.03x faster                                                    |

Benchmark hidden because not significant (24): async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_memoization, xml_etree_parse, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed, xml_etree_iterparse, async_tree_none_tg, async_tree_io, nbody, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io, asyncio_websockets, pickle_pure_python, coroutines, pidigits, async_tree_io_tg, async_tree_eager_io_tg, create_gc_cycles, scimark_fft, crypto_pyaes, deepcopy_reduce, tornado_http

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x