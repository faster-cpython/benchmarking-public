# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: darwin-arm64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.030x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 182 ms                                                                 | 171 ms: 1.06x faster                                            |
| docutils       | 1.55 sec                                                               | 1.50 sec: 1.03x faster                                          |
| html5lib       | 32.1 ms                                                                | 31.2 ms: 1.03x faster                                           |
| sphinx         | 661 ms                                                                 | 618 ms: 1.07x faster                                            |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_eager                 | 63.9 ms                                                                | 61.9 ms: 1.03x faster                                           |
| async_tree_eager_tg              | 43.0 ms                                                                | 42.5 ms: 1.01x faster                                           |
| async_tree_none                  | 199 ms                                                                 | 197 ms: 1.01x faster                                            |
| async_tree_eager_cpu_io_mixed    | 364 ms                                                                 | 361 ms: 1.01x faster                                            |
| async_tree_eager_cpu_io_mixed_tg | 337 ms                                                                 | 335 ms: 1.01x faster                                            |
| coroutines                       | 16.4 ms                                                                | 16.3 ms: 1.00x faster                                           |
| async_generators                 | 292 ms                                                                 | 291 ms: 1.00x faster                                            |
| async_tree_io_tg                 | 609 ms                                                                 | 608 ms: 1.00x faster                                            |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                    |

Benchmark hidden because not significant (11): async_tree_eager_io, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 48.2 ms                                                                | 48.1 ms: 1.00x faster                                           |
| nbody          | 65.7 ms                                                                | 65.5 ms: 1.00x faster                                           |
| pidigits       | 283 ms                                                                 | 283 ms: 1.00x slower                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 74.5 ms                                                                | 71.0 ms: 1.05x faster                                           |
| regex_effbot   | 2.50 ms                                                                | 2.47 ms: 1.01x faster                                           |
| regex_v8       | 16.8 ms                                                                | 16.8 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 1.25 sec                                                               | 1.23 sec: 1.01x faster                                          |
| json_loads           | 16.7 us                                                                | 16.5 us: 1.01x faster                                           |
| xml_etree_process    | 34.6 ms                                                                | 34.3 ms: 1.01x faster                                           |
| unpickle_pure_python | 133 us                                                                 | 132 us: 1.01x faster                                            |
| json_dumps           | 7.15 ms                                                                | 7.12 ms: 1.00x faster                                           |
| xml_etree_generate   | 50.4 ms                                                                | 50.3 ms: 1.00x faster                                           |
| pickle_pure_python   | 179 us                                                                 | 179 us: 1.00x faster                                            |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 15.1 ms                                                                | 12.9 ms: 1.17x faster                                           |
| python_startup         | 19.1 ms                                                                | 16.8 ms: 1.14x faster                                           |
| Geometric mean         | (ref)                                                                  | 1.15x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 41.7 ms                                                                | 31.4 ms: 1.33x faster                                           |
| genshi_text     | 16.6 ms                                                                | 14.5 ms: 1.14x faster                                           |
| django_template | 22.7 ms                                                                | 20.3 ms: 1.12x faster                                           |
| mako            | 6.49 ms                                                                | 6.44 ms: 1.01x faster                                           |
| Geometric mean  | (ref)                                                                  | 1.14x faster                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml                       | 41.7 ms                                                                | 31.4 ms: 1.33x faster                                           |
| python_startup_no_site           | 15.1 ms                                                                | 12.9 ms: 1.17x faster                                           |
| genshi_text                      | 16.6 ms                                                                | 14.5 ms: 1.14x faster                                           |
| python_startup                   | 19.1 ms                                                                | 16.8 ms: 1.14x faster                                           |
| django_template                  | 22.7 ms                                                                | 20.3 ms: 1.12x faster                                           |
| hexiom                           | 4.99 ms                                                                | 4.49 ms: 1.11x faster                                           |
| pylint                           | 178 ms                                                                 | 161 ms: 1.10x faster                                            |
| sqlglot_optimize                 | 37.0 ms                                                                | 33.7 ms: 1.10x faster                                           |
| go                               | 98.5 ms                                                                | 90.0 ms: 1.09x faster                                           |
| pprint_safe_repr                 | 501 ms                                                                 | 459 ms: 1.09x faster                                            |
| sqlglot_normalize                | 185 ms                                                                 | 173 ms: 1.07x faster                                            |
| sphinx                           | 661 ms                                                                 | 618 ms: 1.07x faster                                            |
| sympy_integrate                  | 12.5 ms                                                                | 11.7 ms: 1.06x faster                                           |
| richards_super                   | 36.7 ms                                                                | 34.6 ms: 1.06x faster                                           |
| sympy_sum                        | 79.6 ms                                                                | 75.0 ms: 1.06x faster                                           |
| 2to3                             | 182 ms                                                                 | 171 ms: 1.06x faster                                            |
| sqlglot_transpile                | 1.05 ms                                                                | 992 us: 1.06x faster                                            |
| generators                       | 25.5 ms                                                                | 24.1 ms: 1.06x faster                                           |
| richards                         | 32.9 ms                                                                | 31.2 ms: 1.06x faster                                           |
| sympy_str                        | 150 ms                                                                 | 143 ms: 1.05x faster                                            |
| regex_compile                    | 74.5 ms                                                                | 71.0 ms: 1.05x faster                                           |
| sqlglot_parse                    | 862 us                                                                 | 823 us: 1.05x faster                                            |
| pprint_pformat                   | 1.00 sec                                                               | 961 ms: 1.04x faster                                            |
| raytrace                         | 169 ms                                                                 | 162 ms: 1.04x faster                                            |
| sympy_expand                     | 246 ms                                                                 | 237 ms: 1.04x faster                                            |
| pyflate                          | 324 ms                                                                 | 312 ms: 1.04x faster                                            |
| pycparser                        | 677 ms                                                                 | 653 ms: 1.04x faster                                            |
| meteor_contest                   | 75.1 ms                                                                | 72.5 ms: 1.04x faster                                           |
| docutils                         | 1.55 sec                                                               | 1.50 sec: 1.03x faster                                          |
| bench_mp_pool                    | 61.8 ms                                                                | 59.9 ms: 1.03x faster                                           |
| deepcopy                         | 153 us                                                                 | 148 us: 1.03x faster                                            |
| async_tree_eager                 | 63.9 ms                                                                | 61.9 ms: 1.03x faster                                           |
| html5lib                         | 32.1 ms                                                                | 31.2 ms: 1.03x faster                                           |
| comprehensions                   | 13.1 us                                                                | 12.7 us: 1.03x faster                                           |
| deltablue                        | 2.39 ms                                                                | 2.32 ms: 1.03x faster                                           |
| mdp                              | 1.55 sec                                                               | 1.51 sec: 1.03x faster                                          |
| logging_simple                   | 3.11 us                                                                | 3.03 us: 1.03x faster                                           |
| logging_format                   | 3.39 us                                                                | 3.31 us: 1.02x faster                                           |
| chaos                            | 41.3 ms                                                                | 40.3 ms: 1.02x faster                                           |
| dulwich_log                      | 29.0 ms                                                                | 28.5 ms: 1.02x faster                                           |
| nqueens                          | 58.9 ms                                                                | 57.9 ms: 1.02x faster                                           |
| coverage                         | 44.1 ms                                                                | 43.5 ms: 1.01x faster                                           |
| deepcopy_reduce                  | 1.54 us                                                                | 1.52 us: 1.01x faster                                           |
| tomli_loads                      | 1.25 sec                                                               | 1.23 sec: 1.01x faster                                          |
| json                             | 2.88 ms                                                                | 2.84 ms: 1.01x faster                                           |
| bench_thread_pool                | 475 us                                                                 | 470 us: 1.01x faster                                            |
| thrift                           | 422 us                                                                 | 417 us: 1.01x faster                                            |
| async_tree_eager_tg              | 43.0 ms                                                                | 42.5 ms: 1.01x faster                                           |
| regex_effbot                     | 2.50 ms                                                                | 2.47 ms: 1.01x faster                                           |
| async_tree_none                  | 199 ms                                                                 | 197 ms: 1.01x faster                                            |
| logging_silent                   | 69.9 ns                                                                | 69.3 ns: 1.01x faster                                           |
| json_loads                       | 16.7 us                                                                | 16.5 us: 1.01x faster                                           |
| bpe_tokeniser                    | 3.05 sec                                                               | 3.02 sec: 1.01x faster                                          |
| typing_runtime_protocols         | 97.5 us                                                                | 96.7 us: 1.01x faster                                           |
| deepcopy_memo                    | 16.8 us                                                                | 16.7 us: 1.01x faster                                           |
| mako                             | 6.49 ms                                                                | 6.44 ms: 1.01x faster                                           |
| async_tree_eager_cpu_io_mixed    | 364 ms                                                                 | 361 ms: 1.01x faster                                            |
| xml_etree_process                | 34.6 ms                                                                | 34.3 ms: 1.01x faster                                           |
| unpickle_pure_python             | 133 us                                                                 | 132 us: 1.01x faster                                            |
| scimark_lu                       | 65.7 ms                                                                | 65.3 ms: 1.01x faster                                           |
| async_tree_eager_cpu_io_mixed_tg | 337 ms                                                                 | 335 ms: 1.01x faster                                            |
| coroutines                       | 16.4 ms                                                                | 16.3 ms: 1.00x faster                                           |
| async_generators                 | 292 ms                                                                 | 291 ms: 1.00x faster                                            |
| json_dumps                       | 7.15 ms                                                                | 7.12 ms: 1.00x faster                                           |
| float                            | 48.2 ms                                                                | 48.1 ms: 1.00x faster                                           |
| nbody                            | 65.7 ms                                                                | 65.5 ms: 1.00x faster                                           |
| xml_etree_generate               | 50.4 ms                                                                | 50.3 ms: 1.00x faster                                           |
| scimark_sor                      | 85.9 ms                                                                | 85.7 ms: 1.00x faster                                           |
| scimark_monte_carlo              | 45.5 ms                                                                | 45.4 ms: 1.00x faster                                           |
| pickle_pure_python               | 179 us                                                                 | 179 us: 1.00x faster                                            |
| async_tree_io_tg                 | 609 ms                                                                 | 608 ms: 1.00x faster                                            |
| regex_v8                         | 16.8 ms                                                                | 16.8 ms: 1.00x slower                                           |
| pidigits                         | 283 ms                                                                 | 283 ms: 1.00x slower                                            |
| telco                            | 4.56 ms                                                                | 4.57 ms: 1.00x slower                                           |
| create_gc_cycles                 | 1.31 ms                                                                | 1.32 ms: 1.00x slower                                           |
| Geometric mean                   | (ref)                                                                  | 1.03x faster                                                    |

Benchmark hidden because not significant (22): async_tree_eager_io, async_tree_eager_memoization, async_tree_cpu_io_mixed, pathlib, async_tree_memoization, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_eager_io_tg, spectral_norm, gc_traversal, async_tree_eager_memoization_tg, asyncio_websockets, regex_dna, fannkuch, crypto_pyaes, scimark_fft, scimark_sparse_mat_mult, xml_etree_iterparse, xml_etree_parse, tornado_http

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x