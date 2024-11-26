# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: darwin-arm64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.028x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 182 ms                                                                 | 171 ms: 1.06x faster                                                |
| docutils       | 1.55 sec                                                               | 1.49 sec: 1.04x faster                                              |
| html5lib       | 32.1 ms                                                                | 31.1 ms: 1.03x faster                                               |
| sphinx         | 661 ms                                                                 | 617 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_eager                 | 63.9 ms                                                                | 61.8 ms: 1.03x faster                                               |
| async_tree_eager_tg              | 43.0 ms                                                                | 42.4 ms: 1.02x faster                                               |
| async_tree_eager_cpu_io_mixed    | 364 ms                                                                 | 361 ms: 1.01x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 337 ms                                                                 | 335 ms: 1.01x faster                                                |
| coroutines                       | 16.4 ms                                                                | 16.3 ms: 1.01x faster                                               |
| async_tree_none                  | 199 ms                                                                 | 198 ms: 1.00x faster                                                |
| async_generators                 | 292 ms                                                                 | 291 ms: 1.00x faster                                                |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (12): async_tree_eager_io, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_eager_memoization_tg, asyncio_websockets, async_tree_eager_io_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 48.2 ms                                                                | 48.1 ms: 1.00x faster                                               |
| nbody          | 65.7 ms                                                                | 65.6 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 74.5 ms                                                                | 71.0 ms: 1.05x faster                                               |
| regex_effbot   | 2.50 ms                                                                | 2.45 ms: 1.02x faster                                               |
| regex_v8       | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                               |
| regex_dna      | 143 ms                                                                 | 142 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_process   | 34.6 ms                                                                | 34.2 ms: 1.01x faster                                               |
| tomli_loads         | 1.25 sec                                                               | 1.23 sec: 1.01x faster                                              |
| json_loads          | 16.7 us                                                                | 16.6 us: 1.01x faster                                               |
| xml_etree_generate  | 50.4 ms                                                                | 50.2 ms: 1.00x faster                                               |
| pickle_pure_python  | 179 us                                                                 | 179 us: 1.00x slower                                                |
| json_dumps          | 7.15 ms                                                                | 7.17 ms: 1.00x slower                                               |
| xml_etree_iterparse | 72.2 ms                                                                | 72.7 ms: 1.01x slower                                               |
| xml_etree_parse     | 106 ms                                                                 | 108 ms: 1.01x slower                                                |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 15.1 ms                                                                | 13.5 ms: 1.12x faster                                               |
| python_startup         | 19.1 ms                                                                | 17.4 ms: 1.10x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.11x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 41.7 ms                                                                | 32.1 ms: 1.30x faster                                               |
| genshi_text     | 16.6 ms                                                                | 14.4 ms: 1.15x faster                                               |
| django_template | 22.7 ms                                                                | 20.4 ms: 1.11x faster                                               |
| mako            | 6.49 ms                                                                | 6.45 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                                  | 1.14x faster                                                        |

All benchmarks:
===============

| Benchmark                        | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml                       | 41.7 ms                                                                | 32.1 ms: 1.30x faster                                               |
| genshi_text                      | 16.6 ms                                                                | 14.4 ms: 1.15x faster                                               |
| python_startup_no_site           | 15.1 ms                                                                | 13.5 ms: 1.12x faster                                               |
| hexiom                           | 4.99 ms                                                                | 4.49 ms: 1.11x faster                                               |
| django_template                  | 22.7 ms                                                                | 20.4 ms: 1.11x faster                                               |
| sqlglot_optimize                 | 37.0 ms                                                                | 33.6 ms: 1.10x faster                                               |
| pylint                           | 178 ms                                                                 | 162 ms: 1.10x faster                                                |
| python_startup                   | 19.1 ms                                                                | 17.4 ms: 1.10x faster                                               |
| go                               | 98.5 ms                                                                | 89.9 ms: 1.10x faster                                               |
| pprint_safe_repr                 | 501 ms                                                                 | 460 ms: 1.09x faster                                                |
| sphinx                           | 661 ms                                                                 | 617 ms: 1.07x faster                                                |
| sqlglot_normalize                | 185 ms                                                                 | 173 ms: 1.07x faster                                                |
| 2to3                             | 182 ms                                                                 | 171 ms: 1.06x faster                                                |
| richards_super                   | 36.7 ms                                                                | 34.6 ms: 1.06x faster                                               |
| sympy_integrate                  | 12.5 ms                                                                | 11.8 ms: 1.06x faster                                               |
| sqlglot_transpile                | 1.05 ms                                                                | 993 us: 1.06x faster                                                |
| richards                         | 32.9 ms                                                                | 31.1 ms: 1.06x faster                                               |
| generators                       | 25.5 ms                                                                | 24.1 ms: 1.06x faster                                               |
| sympy_sum                        | 79.6 ms                                                                | 75.4 ms: 1.06x faster                                               |
| sympy_str                        | 150 ms                                                                 | 143 ms: 1.05x faster                                                |
| regex_compile                    | 74.5 ms                                                                | 71.0 ms: 1.05x faster                                               |
| sqlglot_parse                    | 862 us                                                                 | 822 us: 1.05x faster                                                |
| raytrace                         | 169 ms                                                                 | 162 ms: 1.05x faster                                                |
| docutils                         | 1.55 sec                                                               | 1.49 sec: 1.04x faster                                              |
| sympy_expand                     | 246 ms                                                                 | 237 ms: 1.04x faster                                                |
| pyflate                          | 324 ms                                                                 | 312 ms: 1.04x faster                                                |
| async_tree_eager                 | 63.9 ms                                                                | 61.8 ms: 1.03x faster                                               |
| pycparser                        | 677 ms                                                                 | 656 ms: 1.03x faster                                                |
| html5lib                         | 32.1 ms                                                                | 31.1 ms: 1.03x faster                                               |
| pprint_pformat                   | 1.00 sec                                                               | 974 ms: 1.03x faster                                                |
| meteor_contest                   | 75.1 ms                                                                | 72.9 ms: 1.03x faster                                               |
| deepcopy                         | 153 us                                                                 | 148 us: 1.03x faster                                                |
| deltablue                        | 2.39 ms                                                                | 2.32 ms: 1.03x faster                                               |
| bench_mp_pool                    | 61.8 ms                                                                | 60.1 ms: 1.03x faster                                               |
| chaos                            | 41.3 ms                                                                | 40.3 ms: 1.03x faster                                               |
| comprehensions                   | 13.1 us                                                                | 12.7 us: 1.02x faster                                               |
| logging_simple                   | 3.11 us                                                                | 3.04 us: 1.02x faster                                               |
| mdp                              | 1.55 sec                                                               | 1.52 sec: 1.02x faster                                              |
| logging_format                   | 3.39 us                                                                | 3.33 us: 1.02x faster                                               |
| regex_effbot                     | 2.50 ms                                                                | 2.45 ms: 1.02x faster                                               |
| dulwich_log                      | 29.0 ms                                                                | 28.5 ms: 1.02x faster                                               |
| nqueens                          | 58.9 ms                                                                | 57.9 ms: 1.02x faster                                               |
| async_tree_eager_tg              | 43.0 ms                                                                | 42.4 ms: 1.02x faster                                               |
| bench_thread_pool                | 475 us                                                                 | 469 us: 1.01x faster                                                |
| fannkuch                         | 257 ms                                                                 | 254 ms: 1.01x faster                                                |
| xml_etree_process                | 34.6 ms                                                                | 34.2 ms: 1.01x faster                                               |
| json                             | 2.88 ms                                                                | 2.84 ms: 1.01x faster                                               |
| scimark_lu                       | 65.7 ms                                                                | 65.0 ms: 1.01x faster                                               |
| tomli_loads                      | 1.25 sec                                                               | 1.23 sec: 1.01x faster                                              |
| coverage                         | 44.1 ms                                                                | 43.7 ms: 1.01x faster                                               |
| bpe_tokeniser                    | 3.05 sec                                                               | 3.02 sec: 1.01x faster                                              |
| logging_silent                   | 69.9 ns                                                                | 69.4 ns: 1.01x faster                                               |
| thrift                           | 422 us                                                                 | 419 us: 1.01x faster                                                |
| async_tree_eager_cpu_io_mixed    | 364 ms                                                                 | 361 ms: 1.01x faster                                                |
| json_loads                       | 16.7 us                                                                | 16.6 us: 1.01x faster                                               |
| regex_v8                         | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                               |
| pathlib                          | 22.5 ms                                                                | 22.3 ms: 1.01x faster                                               |
| deepcopy_reduce                  | 1.54 us                                                                | 1.53 us: 1.01x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 337 ms                                                                 | 335 ms: 1.01x faster                                                |
| deepcopy_memo                    | 16.8 us                                                                | 16.7 us: 1.01x faster                                               |
| coroutines                       | 16.4 ms                                                                | 16.3 ms: 1.01x faster                                               |
| mako                             | 6.49 ms                                                                | 6.45 ms: 1.01x faster                                               |
| async_tree_none                  | 199 ms                                                                 | 198 ms: 1.00x faster                                                |
| regex_dna                        | 143 ms                                                                 | 142 ms: 1.00x faster                                                |
| telco                            | 4.56 ms                                                                | 4.54 ms: 1.00x faster                                               |
| async_generators                 | 292 ms                                                                 | 291 ms: 1.00x faster                                                |
| xml_etree_generate               | 50.4 ms                                                                | 50.2 ms: 1.00x faster                                               |
| scimark_monte_carlo              | 45.5 ms                                                                | 45.3 ms: 1.00x faster                                               |
| spectral_norm                    | 69.5 ms                                                                | 69.3 ms: 1.00x faster                                               |
| scimark_sparse_mat_mult          | 3.16 ms                                                                | 3.15 ms: 1.00x faster                                               |
| float                            | 48.2 ms                                                                | 48.1 ms: 1.00x faster                                               |
| nbody                            | 65.7 ms                                                                | 65.6 ms: 1.00x faster                                               |
| scimark_sor                      | 85.9 ms                                                                | 86.1 ms: 1.00x slower                                               |
| gc_traversal                     | 2.94 ms                                                                | 2.95 ms: 1.00x slower                                               |
| pickle_pure_python               | 179 us                                                                 | 179 us: 1.00x slower                                                |
| json_dumps                       | 7.15 ms                                                                | 7.17 ms: 1.00x slower                                               |
| crypto_pyaes                     | 53.9 ms                                                                | 54.3 ms: 1.01x slower                                               |
| xml_etree_iterparse              | 72.2 ms                                                                | 72.7 ms: 1.01x slower                                               |
| create_gc_cycles                 | 1.31 ms                                                                | 1.32 ms: 1.01x slower                                               |
| xml_etree_parse                  | 106 ms                                                                 | 108 ms: 1.01x slower                                                |
| Geometric mean                   | (ref)                                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (17): async_tree_eager_io, async_tree_eager_memoization, typing_runtime_protocols, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, scimark_fft, async_tree_memoization_tg, async_tree_io, unpickle_pure_python, async_tree_none_tg, async_tree_eager_memoization_tg, asyncio_websockets, async_tree_eager_io_tg, async_tree_io_tg, pidigits, tornado_http

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x