# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: darwin-arm64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.308x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 196 ms: 1.03x faster                                                         |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.20x faster                                                       |
| html5lib       | 43.5 ms                                                | 32.5 ms: 1.34x faster                                                        |
| sphinx         | 729 ms                                                 | 581 ms: 1.25x faster                                                         |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 67.1 ms: 5.84x faster                                                        |
| async_tree_eager_memoization  | 483 ms                                                 | 146 ms: 3.31x faster                                                         |
| async_tree_eager_io           | 1.01 sec                                               | 370 ms: 2.74x faster                                                         |
| async_tree_io                 | 1.02 sec                                               | 391 ms: 2.60x faster                                                         |
| async_tree_none               | 391 ms                                                 | 168 ms: 2.33x faster                                                         |
| async_tree_memoization        | 481 ms                                                 | 208 ms: 2.31x faster                                                         |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.86x faster                                                         |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 416 ms: 1.61x faster                                                         |
| coroutines                    | 20.5 ms                                                | 19.0 ms: 1.08x faster                                                        |
| async_generators              | 233 ms                                                 | 265 ms: 1.14x slower                                                         |
| Geometric mean                | (ref)                                                  | 2.01x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 48.9 ms: 1.48x faster                                                        |
| nbody          | 92.5 ms                                                | 81.0 ms: 1.14x faster                                                        |
| pidigits       | 280 ms                                                 | 281 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 76.2 ms: 1.25x faster                                                        |
| regex_dna      | 175 ms                                                 | 145 ms: 1.21x faster                                                         |
| regex_v8       | 19.1 ms                                                | 17.9 ms: 1.07x faster                                                        |
| regex_effbot   | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 220 us: 1.29x faster                                                         |
| unpickle_pure_python | 198 us                                                 | 161 us: 1.23x faster                                                         |
| json_dumps           | 8.31 ms                                                | 7.37 ms: 1.13x faster                                                        |
| tomli_loads          | 1.72 sec                                               | 1.57 sec: 1.10x faster                                                       |
| xml_etree_process    | 44.6 ms                                                | 40.9 ms: 1.09x faster                                                        |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.07x faster                                                         |
| xml_etree_iterparse  | 74.5 ms                                                | 72.5 ms: 1.03x faster                                                        |
| xml_etree_generate   | 53.9 ms                                                | 56.5 ms: 1.05x slower                                                        |
| json_loads           | 16.6 us                                                | 18.0 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.0 ms: 1.03x faster                                                        |
| python_startup_no_site | 12.8 ms                                                | 14.1 ms: 1.10x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.91 ms: 1.24x faster                                                        |
| genshi_text     | 17.7 ms                                                | 15.2 ms: 1.16x faster                                                        |
| genshi_xml      | 35.1 ms                                                | 32.6 ms: 1.08x faster                                                        |
| django_template | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                                 |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 67.1 ms: 5.84x faster                                                        |
| typing_runtime_protocols      | 326 us                                                 | 97.8 us: 3.33x faster                                                        |
| async_tree_eager_memoization  | 483 ms                                                 | 146 ms: 3.31x faster                                                         |
| subparsers                    | 39.8 ms                                                | 12.7 ms: 3.14x faster                                                        |
| async_tree_eager_io           | 1.01 sec                                               | 370 ms: 2.74x faster                                                         |
| async_tree_io                 | 1.02 sec                                               | 391 ms: 2.60x faster                                                         |
| async_tree_none               | 391 ms                                                 | 168 ms: 2.33x faster                                                         |
| async_tree_memoization        | 481 ms                                                 | 208 ms: 2.31x faster                                                         |
| deltablue                     | 4.99 ms                                                | 2.34 ms: 2.13x faster                                                        |
| raytrace                      | 327 ms                                                 | 173 ms: 1.89x faster                                                         |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.86x faster                                                         |
| go                            | 163 ms                                                 | 88.0 ms: 1.86x faster                                                        |
| richards_super                | 61.0 ms                                                | 35.5 ms: 1.72x faster                                                        |
| chaos                         | 67.7 ms                                                | 40.6 ms: 1.67x faster                                                        |
| logging_silent                | 117 ns                                                 | 71.3 ns: 1.64x faster                                                        |
| richards                      | 52.3 ms                                                | 32.0 ms: 1.64x faster                                                        |
| sqlglot_parse                 | 1.35 ms                                                | 829 us: 1.63x faster                                                         |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 416 ms: 1.61x faster                                                         |
| scimark_sor                   | 140 ms                                                 | 88.0 ms: 1.59x faster                                                        |
| deepcopy_memo                 | 34.7 us                                                | 22.2 us: 1.56x faster                                                        |
| sqlglot_transpile             | 1.56 ms                                                | 1.00 ms: 1.56x faster                                                        |
| scimark_monte_carlo           | 72.4 ms                                                | 47.4 ms: 1.53x faster                                                        |
| deepcopy                      | 276 us                                                 | 181 us: 1.53x faster                                                         |
| float                         | 72.4 ms                                                | 48.9 ms: 1.48x faster                                                        |
| spectral_norm                 | 95.3 ms                                                | 65.1 ms: 1.46x faster                                                        |
| comprehensions                | 17.3 us                                                | 11.9 us: 1.45x faster                                                        |
| pylint                        | 231 ms                                                 | 160 ms: 1.44x faster                                                         |
| pyflate                       | 448 ms                                                 | 316 ms: 1.42x faster                                                         |
| crypto_pyaes                  | 73.3 ms                                                | 52.5 ms: 1.40x faster                                                        |
| logging_format                | 5.03 us                                                | 3.74 us: 1.35x faster                                                        |
| html5lib                      | 43.5 ms                                                | 32.5 ms: 1.34x faster                                                        |
| k_core                        | 2.01 sec                                               | 1.51 sec: 1.34x faster                                                       |
| logging_simple                | 4.59 us                                                | 3.44 us: 1.33x faster                                                        |
| generators                    | 31.7 ms                                                | 23.9 ms: 1.33x faster                                                        |
| scimark_lu                    | 103 ms                                                 | 77.4 ms: 1.32x faster                                                        |
| pickle_pure_python            | 285 us                                                 | 220 us: 1.29x faster                                                         |
| deepcopy_reduce               | 2.32 us                                                | 1.81 us: 1.28x faster                                                        |
| pycparser                     | 887 ms                                                 | 693 ms: 1.28x faster                                                         |
| hexiom                        | 6.25 ms                                                | 4.90 ms: 1.27x faster                                                        |
| dulwich_log                   | 35.6 ms                                                | 28.2 ms: 1.26x faster                                                        |
| thrift                        | 562 us                                                 | 448 us: 1.25x faster                                                         |
| sphinx                        | 729 ms                                                 | 581 ms: 1.25x faster                                                         |
| regex_compile                 | 95.6 ms                                                | 76.2 ms: 1.25x faster                                                        |
| sqlalchemy_declarative        | 75.7 ms                                                | 60.5 ms: 1.25x faster                                                        |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.27 ms: 1.25x faster                                                        |
| mako                          | 9.81 ms                                                | 7.91 ms: 1.24x faster                                                        |
| unpickle_pure_python          | 198 us                                                 | 161 us: 1.23x faster                                                         |
| sympy_sum                     | 92.7 ms                                                | 76.2 ms: 1.22x faster                                                        |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.21x faster                                                         |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.20x faster                                                       |
| sympy_integrate               | 13.2 ms                                                | 11.1 ms: 1.19x faster                                                        |
| scimark_fft                   | 225 ms                                                 | 190 ms: 1.19x faster                                                         |
| pprint_pformat                | 1.33 sec                                               | 1.12 sec: 1.18x faster                                                       |
| genshi_text                   | 17.7 ms                                                | 15.2 ms: 1.16x faster                                                        |
| pprint_safe_repr              | 648 ms                                                 | 560 ms: 1.16x faster                                                         |
| sympy_str                     | 166 ms                                                 | 144 ms: 1.15x faster                                                         |
| nbody                         | 92.5 ms                                                | 81.0 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.03 ms: 1.13x faster                                                        |
| json_dumps                    | 8.31 ms                                                | 7.37 ms: 1.13x faster                                                        |
| mdp                           | 1.65 sec                                               | 1.48 sec: 1.12x faster                                                       |
| sympy_expand                  | 269 ms                                                 | 243 ms: 1.11x faster                                                         |
| pathlib                       | 25.7 ms                                                | 23.4 ms: 1.10x faster                                                        |
| bpe_tokeniser                 | 3.44 sec                                               | 3.14 sec: 1.10x faster                                                       |
| tomli_loads                   | 1.72 sec                                               | 1.57 sec: 1.10x faster                                                       |
| xml_etree_process             | 44.6 ms                                                | 40.9 ms: 1.09x faster                                                        |
| bench_thread_pool             | 545 us                                                 | 501 us: 1.09x faster                                                         |
| sqlglot_optimize              | 37.2 ms                                                | 34.2 ms: 1.09x faster                                                        |
| coroutines                    | 20.5 ms                                                | 19.0 ms: 1.08x faster                                                        |
| genshi_xml                    | 35.1 ms                                                | 32.6 ms: 1.08x faster                                                        |
| regex_v8                      | 19.1 ms                                                | 17.9 ms: 1.07x faster                                                        |
| nqueens                       | 63.8 ms                                                | 59.7 ms: 1.07x faster                                                        |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.07x faster                                                         |
| connected_components          | 318 ms                                                 | 299 ms: 1.06x faster                                                         |
| django_template               | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                        |
| many_optionals                | 486 us                                                 | 466 us: 1.04x faster                                                         |
| python_startup                | 19.6 ms                                                | 19.0 ms: 1.03x faster                                                        |
| 2to3                          | 201 ms                                                 | 196 ms: 1.03x faster                                                         |
| dask                          | 789 ms                                                 | 767 ms: 1.03x faster                                                         |
| sqlglot_normalize             | 192 ms                                                 | 187 ms: 1.03x faster                                                         |
| xml_etree_iterparse           | 74.5 ms                                                | 72.5 ms: 1.03x faster                                                        |
| json                          | 3.10 ms                                                | 3.05 ms: 1.02x faster                                                        |
| shortest_path                 | 328 ms                                                 | 326 ms: 1.01x faster                                                         |
| pidigits                      | 280 ms                                                 | 281 ms: 1.00x slower                                                         |
| regex_effbot                  | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                        |
| meteor_contest                | 77.8 ms                                                | 79.3 ms: 1.02x slower                                                        |
| fannkuch                      | 303 ms                                                 | 310 ms: 1.02x slower                                                         |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.05x slower                                                        |
| xml_etree_generate            | 53.9 ms                                                | 56.5 ms: 1.05x slower                                                        |
| create_gc_cycles              | 1.16 ms                                                | 1.25 ms: 1.08x slower                                                        |
| bench_mp_pool                 | 56.0 ms                                                | 60.5 ms: 1.08x slower                                                        |
| json_loads                    | 16.6 us                                                | 18.0 us: 1.08x slower                                                        |
| coverage                      | 41.2 ms                                                | 44.7 ms: 1.08x slower                                                        |
| python_startup_no_site        | 12.8 ms                                                | 14.1 ms: 1.10x slower                                                        |
| gc_traversal                  | 2.71 ms                                                | 3.07 ms: 1.13x slower                                                        |
| async_generators              | 233 ms                                                 | 265 ms: 1.14x slower                                                         |
| telco                         | 3.49 ms                                                | 4.64 ms: 1.33x slower                                                        |
| Geometric mean                | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250225-3.14.0a5+-da5ad58-CLANG/bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.308x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.13x