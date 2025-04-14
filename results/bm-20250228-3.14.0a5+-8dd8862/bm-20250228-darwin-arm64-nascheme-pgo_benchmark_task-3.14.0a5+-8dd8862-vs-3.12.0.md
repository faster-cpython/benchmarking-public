# Results vs. 3.12.0

- fork: nascheme
- ref: pgo_benchmark_task
- machine: darwin-arm64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.135x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 185 ms: 1.10x slower                                                   |
| docutils       | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                 |
| html5lib       | 33.4 ms                                                | 28.2 ms: 1.18x faster                                                  |
| sphinx         | 613 ms                                                 | 577 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 342 ms: 1.97x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 345 ms: 1.93x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 353 ms: 1.90x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 145 ms: 1.82x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 140 ms: 1.82x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 183 ms: 1.74x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 180 ms: 1.73x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 359 ms: 1.72x faster                                                   |
| coroutines                       | 19.7 ms                                                | 14.4 ms: 1.37x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 398 ms: 1.33x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 397 ms: 1.33x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 132 ms: 1.27x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 55.4 ms: 1.19x faster                                                  |
| async_generators                 | 299 ms                                                 | 253 ms: 1.18x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 344 ms: 1.09x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 164 ms: 1.16x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 120 ms: 2.55x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 42.8 ms: 1.26x faster                                                  |
| nbody          | 67.6 ms                                                | 66.9 ms: 1.01x faster                                                  |
| pidigits       | 283 ms                                                 | 281 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 64.0 ms: 1.19x faster                                                  |
| regex_dna      | 143 ms                                                 | 127 ms: 1.12x faster                                                   |
| regex_effbot   | 2.44 ms                                                | 2.22 ms: 1.10x faster                                                  |
| regex_v8       | 15.1 ms                                                | 17.5 ms: 1.16x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 93.7 ms: 1.15x faster                                                  |
| tomli_loads          | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 50.6 ms: 1.09x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 35.8 ms: 1.09x faster                                                  |
| unpickle_pure_python | 145 us                                                 | 134 us: 1.08x faster                                                   |
| pickle_pure_python   | 197 us                                                 | 185 us: 1.07x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 71.2 ms: 1.06x faster                                                  |
| json_loads           | 17.0 us                                                | 17.3 us: 1.01x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.05 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.4 ms: 1.02x slower                                                  |
| python_startup         | 17.8 ms                                                | 18.6 ms: 1.05x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 13.3 ms: 1.11x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 27.8 ms: 1.10x faster                                                  |
| mako            | 7.44 ms                                                | 6.97 ms: 1.07x faster                                                  |
| django_template | 19.7 ms                                                | 20.4 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.9 ms: 2.70x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 342 ms: 1.97x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 345 ms: 1.93x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 353 ms: 1.90x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 145 ms: 1.82x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 140 ms: 1.82x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 183 ms: 1.74x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 180 ms: 1.73x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 359 ms: 1.72x faster                                                   |
| deepcopy                         | 226 us                                                 | 143 us: 1.58x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 16.7 us: 1.56x faster                                                  |
| generators                       | 29.4 ms                                                | 20.7 ms: 1.42x faster                                                  |
| go                               | 98.5 ms                                                | 70.3 ms: 1.40x faster                                                  |
| comprehensions                   | 14.0 us                                                | 9.99 us: 1.40x faster                                                  |
| coroutines                       | 19.7 ms                                                | 14.4 ms: 1.37x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 398 ms: 1.33x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 397 ms: 1.33x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.52 us: 1.33x faster                                                  |
| raytrace                         | 204 ms                                                 | 159 ms: 1.28x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 132 ms: 1.27x faster                                                   |
| float                            | 54.1 ms                                                | 42.8 ms: 1.26x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.04 ms: 1.26x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 59.2 ns: 1.23x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 71.8 ms: 1.20x faster                                                  |
| chaos                            | 41.6 ms                                                | 34.8 ms: 1.19x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 55.4 ms: 1.19x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 64.5 ms: 1.19x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 64.0 ms: 1.19x faster                                                  |
| html5lib                         | 33.4 ms                                                | 28.2 ms: 1.18x faster                                                  |
| async_generators                 | 299 ms                                                 | 253 ms: 1.18x faster                                                   |
| hexiom                           | 4.38 ms                                                | 3.73 ms: 1.17x faster                                                  |
| pylint                           | 182 ms                                                 | 156 ms: 1.17x faster                                                   |
| scimark_fft                      | 194 ms                                                 | 167 ms: 1.16x faster                                                   |
| logging_simple                   | 3.60 us                                                | 3.12 us: 1.16x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.73 ms: 1.15x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.49 sec: 1.15x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 93.7 ms: 1.15x faster                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 38.8 ms: 1.14x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.42 us: 1.14x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                 |
| pprint_pformat                   | 986 ms                                                 | 875 ms: 1.13x faster                                                   |
| regex_dna                        | 143 ms                                                 | 127 ms: 1.12x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 55.3 ms: 1.12x faster                                                  |
| sqlglot_parse                    | 808 us                                                 | 723 us: 1.12x faster                                                   |
| pprint_safe_repr                 | 483 ms                                                 | 434 ms: 1.11x faster                                                   |
| genshi_text                      | 14.7 ms                                                | 13.3 ms: 1.11x faster                                                  |
| thrift                           | 468 us                                                 | 424 us: 1.10x faster                                                   |
| sqlglot_transpile                | 973 us                                                 | 882 us: 1.10x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 2.98 sec: 1.10x faster                                                 |
| genshi_xml                       | 30.5 ms                                                | 27.8 ms: 1.10x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.22 ms: 1.10x faster                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 83.6 us: 1.10x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 50.6 ms: 1.09x faster                                                  |
| meteor_contest                   | 69.1 ms                                                | 63.5 ms: 1.09x faster                                                  |
| xml_etree_process                | 38.9 ms                                                | 35.8 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 344 ms: 1.09x faster                                                   |
| bench_mp_pool                    | 65.5 ms                                                | 60.4 ms: 1.09x faster                                                  |
| unpickle_pure_python             | 145 us                                                 | 134 us: 1.08x faster                                                   |
| dulwich_log                      | 29.2 ms                                                | 27.1 ms: 1.08x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.0 ms: 1.07x faster                                                  |
| mako                             | 7.44 ms                                                | 6.97 ms: 1.07x faster                                                  |
| sympy_str                        | 144 ms                                                 | 135 ms: 1.07x faster                                                   |
| fannkuch                         | 250 ms                                                 | 235 ms: 1.07x faster                                                   |
| pickle_pure_python               | 197 us                                                 | 185 us: 1.07x faster                                                   |
| sphinx                           | 613 ms                                                 | 577 ms: 1.06x faster                                                   |
| nqueens                          | 59.5 ms                                                | 56.1 ms: 1.06x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 71.2 ms: 1.06x faster                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.23 ms: 1.06x faster                                                  |
| richards_super                   | 34.6 ms                                                | 32.7 ms: 1.06x faster                                                  |
| pycparser                        | 673 ms                                                 | 639 ms: 1.05x faster                                                   |
| pyflate                          | 311 ms                                                 | 297 ms: 1.05x faster                                                   |
| sympy_sum                        | 76.2 ms                                                | 73.0 ms: 1.04x faster                                                  |
| richards                         | 30.6 ms                                                | 29.3 ms: 1.04x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.48 us: 1.04x faster                                                  |
| mdp                              | 1.49 sec                                               | 1.44 sec: 1.04x faster                                                 |
| sympy_expand                     | 233 ms                                                 | 225 ms: 1.04x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                 |
| bench_thread_pool                | 483 us                                                 | 469 us: 1.03x faster                                                   |
| shortest_path                    | 331 ms                                                 | 322 ms: 1.03x faster                                                   |
| crypto_pyaes                     | 51.4 ms                                                | 50.5 ms: 1.02x faster                                                  |
| connected_components             | 300 ms                                                 | 294 ms: 1.02x faster                                                   |
| sympy_integrate                  | 11.1 ms                                                | 10.9 ms: 1.02x faster                                                  |
| dask                             | 779 ms                                                 | 767 ms: 1.02x faster                                                   |
| sqlglot_optimize                 | 33.2 ms                                                | 32.9 ms: 1.01x faster                                                  |
| json                             | 3.00 ms                                                | 2.97 ms: 1.01x faster                                                  |
| nbody                            | 67.6 ms                                                | 66.9 ms: 1.01x faster                                                  |
| pidigits                         | 283 ms                                                 | 281 ms: 1.00x faster                                                   |
| sqlglot_normalize                | 180 ms                                                 | 180 ms: 1.00x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.3 us: 1.01x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 13.4 ms: 1.02x slower                                                  |
| django_template                  | 19.7 ms                                                | 20.4 ms: 1.04x slower                                                  |
| python_startup                   | 17.8 ms                                                | 18.6 ms: 1.05x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.09 ms: 1.05x slower                                                  |
| many_optionals                   | 403 us                                                 | 425 us: 1.05x slower                                                   |
| scimark_lu                       | 73.5 ms                                                | 77.9 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| 2to3                             | 168 ms                                                 | 185 ms: 1.10x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.10x slower                                                  |
| telco                            | 3.92 ms                                                | 4.41 ms: 1.12x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.05 ms: 1.14x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 164 ms: 1.16x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 17.5 ms: 1.16x slower                                                  |
| coverage                         | 38.5 ms                                                | 46.6 ms: 1.21x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 120 ms: 2.55x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.135x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.07x