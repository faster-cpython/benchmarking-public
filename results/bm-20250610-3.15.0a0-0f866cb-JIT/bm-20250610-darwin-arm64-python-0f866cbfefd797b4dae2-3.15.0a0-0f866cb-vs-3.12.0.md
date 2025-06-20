# Results vs. 3.12.0

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: darwin-arm64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.005x slower
- HPT reliability: 90.24%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 185 ms: 1.10x slower                                                  |
| docutils       | 1.45 sec                                               | 1.57 sec: 1.08x slower                                                |
| html5lib       | 33.4 ms                                                | 34.1 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 387 ms: 1.72x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 397 ms: 1.70x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 406 ms: 1.65x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 203 ms: 1.57x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 397 ms: 1.56x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 167 ms: 1.53x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 208 ms: 1.49x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 178 ms: 1.48x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 422 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 427 ms: 1.23x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| async_generators                 | 299 ms                                                 | 286 ms: 1.04x faster                                                  |
| coroutines                       | 19.7 ms                                                | 19.2 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 71.7 ms: 1.09x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 180 ms: 1.27x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 141 ms: 3.00x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| float          | 54.1 ms                                                | 57.9 ms: 1.07x slower                                                 |
| nbody          | 67.6 ms                                                | 76.6 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                 |
| regex_compile  | 75.9 ms                                                | 79.7 ms: 1.05x slower                                                 |
| regex_v8       | 15.1 ms                                                | 16.2 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 55.4 ms                                                | 51.9 ms: 1.07x faster                                                 |
| unpickle_pure_python | 145 us                                                 | 138 us: 1.06x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 37.7 ms: 1.03x faster                                                 |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 73.7 ms: 1.02x faster                                                 |
| tomli_loads          | 1.36 sec                                               | 1.34 sec: 1.01x faster                                                |
| json_dumps           | 6.19 ms                                                | 6.86 ms: 1.11x slower                                                 |
| pickle_pure_python   | 197 us                                                 | 226 us: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 20.2 ms: 1.14x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 15.6 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.94 ms: 1.07x faster                                                 |
| genshi_xml      | 30.5 ms                                                | 36.2 ms: 1.19x slower                                                 |
| genshi_text     | 14.7 ms                                                | 17.7 ms: 1.21x slower                                                 |
| django_template | 19.7 ms                                                | 25.3 ms: 1.28x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 15.0 ms: 2.15x faster                                                 |
| mdp                              | 1.49 sec                                               | 826 ms: 1.81x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 387 ms: 1.72x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 397 ms: 1.70x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 406 ms: 1.65x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 203 ms: 1.57x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 397 ms: 1.56x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 167 ms: 1.53x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 208 ms: 1.49x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 178 ms: 1.48x faster                                                  |
| deepcopy                         | 226 us                                                 | 174 us: 1.30x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 422 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 427 ms: 1.23x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 22.3 us: 1.17x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.53 sec: 1.13x faster                                                |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 26.7 ms: 1.09x faster                                                 |
| pathlib                          | 24.7 ms                                                | 22.9 ms: 1.08x faster                                                 |
| pylint                           | 182 ms                                                 | 170 ms: 1.07x faster                                                  |
| mako                             | 7.44 ms                                                | 6.94 ms: 1.07x faster                                                 |
| comprehensions                   | 14.0 us                                                | 13.1 us: 1.07x faster                                                 |
| xml_etree_generate               | 55.4 ms                                                | 51.9 ms: 1.07x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.90 us: 1.06x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.10 sec: 1.06x faster                                                |
| unpickle_pure_python             | 145 us                                                 | 138 us: 1.06x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| async_generators                 | 299 ms                                                 | 286 ms: 1.04x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                 |
| xml_etree_process                | 38.9 ms                                                | 37.7 ms: 1.03x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 74.3 ms: 1.03x faster                                                 |
| json                             | 3.00 ms                                                | 2.93 ms: 1.03x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 73.7 ms: 1.02x faster                                                 |
| coroutines                       | 19.7 ms                                                | 19.2 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.34 sec: 1.01x faster                                                |
| dask                             | 779 ms                                                 | 772 ms: 1.01x faster                                                  |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| thrift                           | 468 us                                                 | 472 us: 1.01x slower                                                  |
| go                               | 98.5 ms                                                | 100 ms: 1.02x slower                                                  |
| html5lib                         | 33.4 ms                                                | 34.1 ms: 1.02x slower                                                 |
| shortest_path                    | 331 ms                                                 | 339 ms: 1.02x slower                                                  |
| pyflate                          | 311 ms                                                 | 321 ms: 1.03x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                 |
| raytrace                         | 204 ms                                                 | 211 ms: 1.03x slower                                                  |
| connected_components             | 300 ms                                                 | 310 ms: 1.03x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.62 us: 1.05x slower                                                 |
| regex_compile                    | 75.9 ms                                                | 79.7 ms: 1.05x slower                                                 |
| scimark_sor                      | 85.8 ms                                                | 90.6 ms: 1.06x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 206 ms: 1.06x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                 |
| float                            | 54.1 ms                                                | 57.9 ms: 1.07x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 16.2 ms: 1.08x slower                                                 |
| sympy_str                        | 144 ms                                                 | 155 ms: 1.08x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.57 sec: 1.08x slower                                                |
| generators                       | 29.4 ms                                                | 31.7 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.20 ms: 1.08x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 71.7 ms: 1.09x slower                                                 |
| 2to3                             | 168 ms                                                 | 185 ms: 1.10x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 6.86 ms: 1.11x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 77.0 ms: 1.11x slower                                                 |
| pycparser                        | 673 ms                                                 | 753 ms: 1.12x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.89 ms: 1.13x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 58.0 ms: 1.13x slower                                                 |
| logging_format                   | 3.90 us                                                | 4.40 us: 1.13x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 265 ms: 1.13x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.56 ms: 1.13x slower                                                 |
| nbody                            | 67.6 ms                                                | 76.6 ms: 1.13x slower                                                 |
| logging_simple                   | 3.60 us                                                | 4.10 us: 1.14x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 104 us: 1.14x slower                                                  |
| python_startup                   | 17.8 ms                                                | 20.2 ms: 1.14x slower                                                 |
| hexiom                           | 4.38 ms                                                | 5.01 ms: 1.14x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 84.3 ms: 1.15x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 226 us: 1.15x slower                                                  |
| chaos                            | 41.6 ms                                                | 47.9 ms: 1.15x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                  |
| telco                            | 3.92 ms                                                | 4.57 ms: 1.17x slower                                                 |
| nqueens                          | 59.5 ms                                                | 69.4 ms: 1.17x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 15.6 ms: 1.19x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 36.2 ms: 1.19x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 53.5 ms: 1.20x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 17.7 ms: 1.21x slower                                                 |
| fannkuch                         | 250 ms                                                 | 302 ms: 1.21x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 585 ms: 1.21x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.20 sec: 1.21x slower                                                |
| richards_super                   | 34.6 ms                                                | 42.2 ms: 1.22x slower                                                 |
| richards                         | 30.6 ms                                                | 37.6 ms: 1.23x slower                                                 |
| many_optionals                   | 403 us                                                 | 508 us: 1.26x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 180 ms: 1.27x slower                                                  |
| django_template                  | 19.7 ms                                                | 25.3 ms: 1.28x slower                                                 |
| coverage                         | 38.5 ms                                                | 49.6 ms: 1.29x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 141 ms: 3.00x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 344 ns: 4.74x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, regex_dna, sphinx
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 90.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x