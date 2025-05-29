# Results vs. 3.12.0

- fork: python
- ref: d05053a203d922c8056f
- machine: darwin-arm64
- commit hash: d05053a
- commit date: 2025-02-09
- overall geometric mean: 1.161x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| docutils       | 1.45 sec                                               | 1.35 sec: 1.07x faster                                                 |
| html5lib       | 33.4 ms                                                | 28.7 ms: 1.16x faster                                                  |
| sphinx         | 613 ms                                                 | 538 ms: 1.14x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io                    | 672 ms                                                 | 339 ms: 1.98x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 341 ms: 1.97x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 343 ms: 1.94x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 346 ms: 1.78x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 144 ms: 1.77x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.76x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 184 ms: 1.73x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 183 ms: 1.70x faster                                                   |
| coroutines                       | 19.7 ms                                                | 14.5 ms: 1.36x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 401 ms: 1.31x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 403 ms: 1.31x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 134 ms: 1.25x faster                                                   |
| async_generators                 | 299 ms                                                 | 247 ms: 1.21x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 58.2 ms: 1.13x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 348 ms: 1.07x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 164 ms: 1.16x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 122 ms: 2.61x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 43.4 ms: 1.25x faster                                                  |
| nbody          | 67.6 ms                                                | 62.0 ms: 1.09x faster                                                  |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 62.1 ms: 1.22x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.36 ms: 1.03x faster                                                  |
| regex_dna      | 143 ms                                                 | 146 ms: 1.02x slower                                                   |
| regex_v8       | 15.1 ms                                                | 17.8 ms: 1.18x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.15 sec: 1.18x faster                                                 |
| unpickle_pure_python | 145 us                                                 | 125 us: 1.17x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 48.2 ms: 1.15x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 33.9 ms: 1.15x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 69.0 ms: 1.09x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 181 us: 1.09x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 100 ms: 1.07x faster                                                   |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.04 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 17.2 ms: 1.03x faster                                                  |
| python_startup_no_site | 13.2 ms                                                | 12.8 ms: 1.03x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.3 ms: 1.19x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 26.0 ms: 1.17x faster                                                  |
| mako            | 7.44 ms                                                | 6.95 ms: 1.07x faster                                                  |
| django_template | 19.7 ms                                                | 19.0 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-darwin-arm64-python-d05053a203d922c8056f-3.14.0a4+-d05053a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.3 ms: 2.85x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 339 ms: 1.98x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 341 ms: 1.97x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 343 ms: 1.94x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 346 ms: 1.78x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 144 ms: 1.77x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.76x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 184 ms: 1.73x faster                                                   |
| generators                       | 29.4 ms                                                | 17.1 ms: 1.71x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 183 ms: 1.70x faster                                                   |
| deepcopy                         | 226 us                                                 | 139 us: 1.63x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 16.2 us: 1.60x faster                                                  |
| go                               | 98.5 ms                                                | 70.3 ms: 1.40x faster                                                  |
| coroutines                       | 19.7 ms                                                | 14.5 ms: 1.36x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.49 us: 1.35x faster                                                  |
| comprehensions                   | 14.0 us                                                | 10.5 us: 1.33x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 58.1 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 401 ms: 1.31x faster                                                   |
| raytrace                         | 204 ms                                                 | 155 ms: 1.31x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 403 ms: 1.31x faster                                                   |
| deltablue                        | 2.57 ms                                                | 2.02 ms: 1.27x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 134 ms: 1.25x faster                                                   |
| logging_silent                   | 72.5 ns                                                | 58.1 ns: 1.25x faster                                                  |
| float                            | 54.1 ms                                                | 43.4 ms: 1.25x faster                                                  |
| logging_simple                   | 3.60 us                                                | 2.90 us: 1.24x faster                                                  |
| pylint                           | 182 ms                                                 | 147 ms: 1.24x faster                                                   |
| regex_compile                    | 75.9 ms                                                | 62.1 ms: 1.22x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.21 us: 1.21x faster                                                  |
| async_generators                 | 299 ms                                                 | 247 ms: 1.21x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 2.74 sec: 1.20x faster                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.64 ms: 1.19x faster                                                  |
| genshi_text                      | 14.7 ms                                                | 12.3 ms: 1.19x faster                                                  |
| sqlglot_parse                    | 808 us                                                 | 680 us: 1.19x faster                                                   |
| nqueens                          | 59.5 ms                                                | 50.5 ms: 1.18x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.15 sec: 1.18x faster                                                 |
| sqlglot_transpile                | 973 us                                                 | 827 us: 1.18x faster                                                   |
| chaos                            | 41.6 ms                                                | 35.4 ms: 1.18x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 73.0 ms: 1.18x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.47 sec: 1.17x faster                                                 |
| genshi_xml                       | 30.5 ms                                                | 26.0 ms: 1.17x faster                                                  |
| unpickle_pure_python             | 145 us                                                 | 125 us: 1.17x faster                                                   |
| html5lib                         | 33.4 ms                                                | 28.7 ms: 1.16x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 168 ms: 1.16x faster                                                   |
| thrift                           | 468 us                                                 | 406 us: 1.15x faster                                                   |
| xml_etree_generate               | 55.4 ms                                                | 48.2 ms: 1.15x faster                                                  |
| hexiom                           | 4.38 ms                                                | 3.81 ms: 1.15x faster                                                  |
| xml_etree_process                | 38.9 ms                                                | 33.9 ms: 1.15x faster                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 38.8 ms: 1.15x faster                                                  |
| sphinx                           | 613 ms                                                 | 538 ms: 1.14x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 54.6 ms: 1.13x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 57.9 ms: 1.13x faster                                                  |
| pyflate                          | 311 ms                                                 | 275 ms: 1.13x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 58.2 ms: 1.13x faster                                                  |
| pprint_pformat                   | 986 ms                                                 | 878 ms: 1.12x faster                                                   |
| sympy_str                        | 144 ms                                                 | 128 ms: 1.12x faster                                                   |
| richards_super                   | 34.6 ms                                                | 30.9 ms: 1.12x faster                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 432 ms: 1.12x faster                                                   |
| dulwich_log                      | 29.2 ms                                                | 26.2 ms: 1.11x faster                                                  |
| richards                         | 30.6 ms                                                | 27.5 ms: 1.11x faster                                                  |
| sqlglot_optimize                 | 33.2 ms                                                | 29.8 ms: 1.11x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 66.0 ms: 1.11x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 68.6 ms: 1.11x faster                                                  |
| 2to3                             | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| pathlib                          | 24.7 ms                                                | 22.2 ms: 1.11x faster                                                  |
| sqlglot_normalize                | 180 ms                                                 | 164 ms: 1.10x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 69.0 ms: 1.09x faster                                                  |
| pycparser                        | 673 ms                                                 | 615 ms: 1.09x faster                                                   |
| sympy_integrate                  | 11.1 ms                                                | 10.1 ms: 1.09x faster                                                  |
| nbody                            | 67.6 ms                                                | 62.0 ms: 1.09x faster                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 47.3 ms: 1.09x faster                                                  |
| pickle_pure_python               | 197 us                                                 | 181 us: 1.09x faster                                                   |
| sympy_expand                     | 233 ms                                                 | 216 ms: 1.08x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 348 ms: 1.07x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.35 sec: 1.07x faster                                                 |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.14 ms: 1.07x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 100 ms: 1.07x faster                                                   |
| mako                             | 7.44 ms                                                | 6.95 ms: 1.07x faster                                                  |
| bench_thread_pool                | 483 us                                                 | 455 us: 1.06x faster                                                   |
| mdp                              | 1.49 sec                                               | 1.42 sec: 1.05x faster                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 87.2 us: 1.05x faster                                                  |
| django_template                  | 19.7 ms                                                | 19.0 ms: 1.04x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.36 ms: 1.03x faster                                                  |
| python_startup                   | 17.8 ms                                                | 17.2 ms: 1.03x faster                                                  |
| shortest_path                    | 331 ms                                                 | 322 ms: 1.03x faster                                                   |
| python_startup_no_site           | 13.2 ms                                                | 12.8 ms: 1.03x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.51 us: 1.02x faster                                                  |
| connected_components             | 300 ms                                                 | 295 ms: 1.02x faster                                                   |
| fannkuch                         | 250 ms                                                 | 247 ms: 1.01x faster                                                   |
| dask                             | 779 ms                                                 | 770 ms: 1.01x faster                                                   |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| meteor_contest                   | 69.1 ms                                                | 69.6 ms: 1.01x slower                                                  |
| regex_dna                        | 143 ms                                                 | 146 ms: 1.02x slower                                                   |
| many_optionals                   | 403 us                                                 | 413 us: 1.03x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.08 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.11x slower                                                  |
| telco                            | 3.92 ms                                                | 4.45 ms: 1.14x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.04 ms: 1.14x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 164 ms: 1.16x slower                                                   |
| coverage                         | 38.5 ms                                                | 45.1 ms: 1.17x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 17.8 ms: 1.18x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 122 ms: 2.61x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (2): json, asyncio_websockets
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.161x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.08x