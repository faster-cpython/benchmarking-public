# Results vs. 3.12.0

- fork: gpshead
- ref: traceback_timestamps
- machine: darwin-arm64
- commit hash: e4f54d4
- commit date: 2025-06-08
- overall geometric mean: 1.045x slower
- HPT reliability: 63.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 262 ms: 1.56x slower                                                   |
| docutils       | 1.45 sec                                               | 1.52 sec: 1.04x slower                                                 |
| html5lib       | 33.4 ms                                                | 31.5 ms: 1.06x faster                                                  |
| sphinx         | 613 ms                                                 | 592 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 363 ms: 1.84x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 374 ms: 1.80x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 377 ms: 1.78x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.66x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 157 ms: 1.63x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 164 ms: 1.61x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.19x faster                                                   |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                                  |
| async_generators                 | 299 ms                                                 | 267 ms: 1.12x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 64.3 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.19x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.76x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.7 ms: 1.09x faster                                                  |
| nbody          | 67.6 ms                                                | 74.0 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 71.8 ms: 1.06x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.38 ms: 1.03x faster                                                  |
| regex_dna      | 143 ms                                                 | 143 ms: 1.00x slower                                                   |
| regex_v8       | 15.1 ms                                                | 16.4 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 69.6 ms: 1.09x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 99.7 ms: 1.08x faster                                                  |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                                  |
| xml_etree_generate   | 55.4 ms                                                | 53.8 ms: 1.03x faster                                                  |
| tomli_loads          | 1.36 sec                                               | 1.36 sec: 1.01x slower                                                 |
| json_dumps           | 6.19 ms                                                | 6.56 ms: 1.06x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 217 us: 1.10x slower                                                   |
| unpickle_pure_python | 145 us                                                 | 160 us: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 18.7 ms: 1.42x slower                                                  |
| python_startup         | 17.8 ms                                                | 28.1 ms: 1.58x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 31.1 ms: 1.02x slower                                                  |
| mako            | 7.44 ms                                                | 7.87 ms: 1.06x slower                                                  |
| django_template | 19.7 ms                                                | 21.9 ms: 1.11x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.7 ms: 2.34x faster                                                  |
| mdp                              | 1.49 sec                                               | 761 ms: 1.96x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 363 ms: 1.84x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 374 ms: 1.80x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 377 ms: 1.78x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.66x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 157 ms: 1.63x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 164 ms: 1.61x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                   |
| deepcopy                         | 226 us                                                 | 159 us: 1.42x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 19.3 us: 1.35x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                                   |
| pathlib                          | 24.7 ms                                                | 19.3 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                   |
| generators                       | 29.4 ms                                                | 24.2 ms: 1.21x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.19x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.70 us: 1.19x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 24.9 ms: 1.17x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.47 sec: 1.17x faster                                                 |
| comprehensions                   | 14.0 us                                                | 12.0 us: 1.16x faster                                                  |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                                  |
| raytrace                         | 204 ms                                                 | 180 ms: 1.13x faster                                                   |
| go                               | 98.5 ms                                                | 87.7 ms: 1.12x faster                                                  |
| async_generators                 | 299 ms                                                 | 267 ms: 1.12x faster                                                   |
| pylint                           | 182 ms                                                 | 163 ms: 1.11x faster                                                   |
| float                            | 54.1 ms                                                | 49.7 ms: 1.09x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 69.6 ms: 1.09x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 99.7 ms: 1.08x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 70.9 ms: 1.08x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.08 sec: 1.06x faster                                                 |
| html5lib                         | 33.4 ms                                                | 31.5 ms: 1.06x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 71.8 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                   |
| json                             | 3.00 ms                                                | 2.87 ms: 1.05x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                                  |
| sphinx                           | 613 ms                                                 | 592 ms: 1.04x faster                                                   |
| chaos                            | 41.6 ms                                                | 40.4 ms: 1.03x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 53.8 ms: 1.03x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.38 ms: 1.03x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 64.3 ms: 1.02x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 75.7 ms: 1.01x faster                                                  |
| regex_dna                        | 143 ms                                                 | 143 ms: 1.00x slower                                                   |
| tomli_loads                      | 1.36 sec                                               | 1.36 sec: 1.01x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 196 ms: 1.01x slower                                                   |
| deltablue                        | 2.57 ms                                                | 2.59 ms: 1.01x slower                                                  |
| logging_simple                   | 3.60 us                                                | 3.67 us: 1.02x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 31.1 ms: 1.02x slower                                                  |
| logging_format                   | 3.90 us                                                | 3.98 us: 1.02x slower                                                  |
| pyflate                          | 311 ms                                                 | 318 ms: 1.02x slower                                                   |
| connected_components             | 300 ms                                                 | 307 ms: 1.02x slower                                                   |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.23 ms: 1.03x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 241 ms: 1.03x slower                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.03x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 88.9 ms: 1.04x slower                                                  |
| nqueens                          | 59.5 ms                                                | 61.9 ms: 1.04x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.52 sec: 1.04x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 46.7 ms: 1.05x slower                                                  |
| mako                             | 7.44 ms                                                | 7.87 ms: 1.06x slower                                                  |
| dask                             | 779 ms                                                 | 823 ms: 1.06x slower                                                   |
| json_dumps                       | 6.19 ms                                                | 6.56 ms: 1.06x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 97.1 us: 1.06x slower                                                  |
| hexiom                           | 4.38 ms                                                | 4.66 ms: 1.07x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 73.9 ms: 1.07x slower                                                  |
| fannkuch                         | 250 ms                                                 | 268 ms: 1.07x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 16.4 ms: 1.09x slower                                                  |
| nbody                            | 67.6 ms                                                | 74.0 ms: 1.09x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 217 us: 1.10x slower                                                   |
| unpickle_pure_python             | 145 us                                                 | 160 us: 1.10x slower                                                   |
| crypto_pyaes                     | 51.4 ms                                                | 57.1 ms: 1.11x slower                                                  |
| django_template                  | 19.7 ms                                                | 21.9 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                   |
| scimark_lu                       | 73.5 ms                                                | 83.2 ms: 1.13x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.13 sec: 1.14x slower                                                 |
| telco                            | 3.92 ms                                                | 4.50 ms: 1.15x slower                                                  |
| richards_super                   | 34.6 ms                                                | 39.8 ms: 1.15x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 556 ms: 1.15x slower                                                   |
| many_optionals                   | 403 us                                                 | 467 us: 1.16x slower                                                   |
| richards                         | 30.6 ms                                                | 35.9 ms: 1.17x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.19x slower                                                   |
| python_startup_no_site           | 13.2 ms                                                | 18.7 ms: 1.42x slower                                                  |
| 2to3                             | 168 ms                                                 | 262 ms: 1.56x slower                                                   |
| python_startup                   | 17.8 ms                                                | 28.1 ms: 1.58x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.76x slower                                                   |
| logging_silent                   | 72.5 ns                                                | 331 ns: 4.56x slower                                                   |
| coverage                         | 38.5 ms                                                | 291 ms: 7.56x slower                                                   |
| thrift                           | 468 us                                                 | 340 ms: 726.13x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.06x slower                                                           |

Benchmark hidden because not significant (8): shortest_path, sympy_str, asyncio_websockets, sympy_integrate, pidigits, xml_etree_process, genshi_text, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250608-3.15.0a0-e4f54d4/bm-20250608-darwin-arm64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.045x slower

# HPT report

- Reliability score: 63.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x