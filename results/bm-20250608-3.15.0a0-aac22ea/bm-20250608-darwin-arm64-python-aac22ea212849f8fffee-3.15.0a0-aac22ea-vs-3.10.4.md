# Results vs. 3.10.4

- fork: python
- ref: aac22ea212849f8fffee
- machine: darwin-arm64
- commit hash: aac22ea
- commit date: 2025-06-08
- overall geometric mean: 1.200x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 265 ms: 1.32x slower                                                  |
| docutils       | 1.74 sec                                               | 1.52 sec: 1.15x faster                                                |
| html5lib       | 43.5 ms                                                | 31.5 ms: 1.38x faster                                                 |
| sphinx         | 729 ms                                                 | 590 ms: 1.23x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.3 ms: 6.09x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.44x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 363 ms: 2.79x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 378 ms: 2.69x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 196 ms: 2.46x faster                                                  |
| async_tree_none               | 391 ms                                                 | 164 ms: 2.38x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                  |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.21x faster                                                 |
| async_generators              | 233 ms                                                 | 264 ms: 1.13x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.07x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.6 ms: 1.46x faster                                                 |
| nbody          | 92.5 ms                                                | 74.9 ms: 1.24x faster                                                 |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 71.9 ms: 1.33x faster                                                 |
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| regex_v8       | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.37 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 218 us: 1.30x faster                                                  |
| json_dumps           | 8.31 ms                                                | 6.56 ms: 1.27x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.36 sec: 1.26x faster                                                |
| unpickle_pure_python | 198 us                                                 | 161 us: 1.23x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 38.9 ms: 1.15x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 99.7 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 69.5 ms: 1.07x faster                                                 |
| json_loads           | 16.6 us                                                | 16.4 us: 1.01x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 53.7 ms: 1.00x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 28.0 ms: 1.43x slower                                                 |
| python_startup_no_site | 12.8 ms                                                | 18.6 ms: 1.46x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.44x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.83 ms: 1.25x faster                                                 |
| genshi_text     | 17.7 ms                                                | 14.7 ms: 1.21x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 31.2 ms: 1.13x faster                                                 |
| django_template | 24.4 ms                                                | 21.9 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.3 ms: 6.09x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.44x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 96.3 us: 3.38x faster                                                 |
| subparsers                    | 39.8 ms                                                | 13.7 ms: 2.91x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 363 ms: 2.79x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 378 ms: 2.69x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 196 ms: 2.46x faster                                                  |
| async_tree_none               | 391 ms                                                 | 164 ms: 2.38x faster                                                  |
| mdp                           | 1.65 sec                                               | 762 ms: 2.17x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.59 ms: 1.93x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                  |
| go                            | 163 ms                                                 | 87.5 ms: 1.87x faster                                                 |
| raytrace                      | 327 ms                                                 | 180 ms: 1.82x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 19.1 us: 1.81x faster                                                 |
| deepcopy                      | 276 us                                                 | 157 us: 1.76x faster                                                  |
| chaos                         | 67.7 ms                                                | 40.3 ms: 1.68x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 88.9 ms: 1.57x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 46.7 ms: 1.55x faster                                                 |
| richards_super                | 61.0 ms                                                | 39.7 ms: 1.54x faster                                                 |
| float                         | 72.4 ms                                                | 49.6 ms: 1.46x faster                                                 |
| richards                      | 52.3 ms                                                | 35.9 ms: 1.46x faster                                                 |
| comprehensions                | 17.3 us                                                | 12.0 us: 1.45x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 24.9 ms: 1.43x faster                                                 |
| pylint                        | 231 ms                                                 | 163 ms: 1.41x faster                                                  |
| pyflate                       | 448 ms                                                 | 318 ms: 1.41x faster                                                  |
| html5lib                      | 43.5 ms                                                | 31.5 ms: 1.38x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                |
| deepcopy_reduce               | 2.32 us                                                | 1.70 us: 1.37x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 71.0 ms: 1.34x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.67 ms: 1.34x faster                                                 |
| pathlib                       | 25.7 ms                                                | 19.3 ms: 1.34x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 71.9 ms: 1.33x faster                                                 |
| generators                    | 31.7 ms                                                | 24.1 ms: 1.31x faster                                                 |
| pycparser                     | 887 ms                                                 | 680 ms: 1.30x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 218 us: 1.30x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 57.3 ms: 1.28x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 6.56 ms: 1.27x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.36 sec: 1.26x faster                                                |
| logging_format                | 5.03 us                                                | 4.00 us: 1.26x faster                                                 |
| mako                          | 9.81 ms                                                | 7.83 ms: 1.25x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.67 us: 1.25x faster                                                 |
| nbody                         | 92.5 ms                                                | 74.9 ms: 1.24x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 161 us: 1.23x faster                                                  |
| sphinx                        | 729 ms                                                 | 590 ms: 1.23x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 83.4 ms: 1.23x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 75.8 ms: 1.22x faster                                                 |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 14.7 ms: 1.21x faster                                                 |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.21x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.0 ms: 1.19x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.13 sec: 1.18x faster                                                |
| pprint_safe_repr              | 648 ms                                                 | 557 ms: 1.16x faster                                                  |
| sympy_str                     | 166 ms                                                 | 143 ms: 1.16x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 196 ms: 1.15x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 38.9 ms: 1.15x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.52 sec: 1.15x faster                                                |
| fannkuch                      | 303 ms                                                 | 267 ms: 1.13x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 31.2 ms: 1.13x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 241 ms: 1.12x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.08 sec: 1.11x faster                                                |
| django_template               | 24.4 ms                                                | 21.9 ms: 1.11x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 99.7 ms: 1.10x faster                                                 |
| json                          | 3.10 ms                                                | 2.89 ms: 1.07x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 69.5 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.23 ms: 1.06x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 73.7 ms: 1.06x faster                                                 |
| many_optionals                | 486 us                                                 | 465 us: 1.04x faster                                                  |
| connected_components          | 318 ms                                                 | 307 ms: 1.04x faster                                                  |
| nqueens                       | 63.8 ms                                                | 61.8 ms: 1.03x faster                                                 |
| json_loads                    | 16.6 us                                                | 16.4 us: 1.01x faster                                                 |
| xml_etree_generate            | 53.9 ms                                                | 53.7 ms: 1.00x faster                                                 |
| shortest_path                 | 328 ms                                                 | 329 ms: 1.00x slower                                                  |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.37 ms: 1.01x slower                                                 |
| dask                          | 789 ms                                                 | 827 ms: 1.05x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.60 us: 1.08x slower                                                 |
| async_generators              | 233 ms                                                 | 264 ms: 1.13x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                 |
| telco                         | 3.49 ms                                                | 4.51 ms: 1.29x slower                                                 |
| 2to3                          | 201 ms                                                 | 265 ms: 1.32x slower                                                  |
| python_startup                | 19.6 ms                                                | 28.0 ms: 1.43x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 18.6 ms: 1.46x slower                                                 |
| logging_silent                | 117 ns                                                 | 335 ns: 2.86x slower                                                  |
| coverage                      | 41.2 ms                                                | 290 ms: 7.03x slower                                                  |
| thrift                        | 562 us                                                 | 322 ms: 573.31x slower                                                |
| Geometric mean                | (ref)                                                  | 1.18x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250608-3.15.0a0-aac22ea/bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.200x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.16x