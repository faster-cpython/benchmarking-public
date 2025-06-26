# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: darwin-arm64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.013x slower
- HPT reliability: 94.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 186 ms: 1.11x slower                                                  |
| docutils       | 1.45 sec                                               | 1.51 sec: 1.04x slower                                                |
| html5lib       | 33.4 ms                                                | 34.2 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 393 ms: 1.69x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 405 ms: 1.66x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 414 ms: 1.62x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 402 ms: 1.54x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 207 ms: 1.54x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 171 ms: 1.49x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 215 ms: 1.44x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 183 ms: 1.44x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 425 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 434 ms: 1.21x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| async_generators                 | 299 ms                                                 | 272 ms: 1.10x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.9 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 369 ms: 1.01x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 72.9 ms: 1.11x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 290 ms: 1.03x slower                                                  |
| float          | 54.1 ms                                                | 57.4 ms: 1.06x slower                                                 |
| nbody          | 67.6 ms                                                | 84.8 ms: 1.26x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.37 ms: 1.03x faster                                                 |
| regex_dna      | 143 ms                                                 | 143 ms: 1.00x slower                                                  |
| regex_compile  | 75.9 ms                                                | 81.2 ms: 1.07x slower                                                 |
| regex_v8       | 15.1 ms                                                | 16.3 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.04x faster                                                  |
| json_loads           | 17.0 us                                                | 16.6 us: 1.03x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 74.0 ms: 1.02x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 58.1 ms: 1.05x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.45 sec: 1.07x slower                                                |
| json_dumps           | 6.19 ms                                                | 6.82 ms: 1.10x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 43.0 ms: 1.11x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 178 us: 1.22x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 241 us: 1.23x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 17.4 ms: 1.02x faster                                                 |
| python_startup_no_site | 13.2 ms                                                | 13.0 ms: 1.02x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 36.1 ms: 1.18x slower                                                 |
| genshi_text     | 14.7 ms                                                | 17.7 ms: 1.21x slower                                                 |
| mako            | 7.44 ms                                                | 9.04 ms: 1.21x slower                                                 |
| django_template | 19.7 ms                                                | 25.1 ms: 1.27x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.22x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 14.8 ms: 2.17x faster                                                 |
| mdp                              | 1.49 sec                                               | 827 ms: 1.81x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 393 ms: 1.69x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 405 ms: 1.66x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 414 ms: 1.62x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 402 ms: 1.54x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 207 ms: 1.54x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 171 ms: 1.49x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 215 ms: 1.44x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 183 ms: 1.44x faster                                                  |
| deepcopy                         | 226 us                                                 | 175 us: 1.29x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 425 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 434 ms: 1.21x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 21.9 us: 1.19x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.47 sec: 1.17x faster                                                |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 26.4 ms: 1.11x faster                                                 |
| async_generators                 | 299 ms                                                 | 272 ms: 1.10x faster                                                  |
| pathlib                          | 24.7 ms                                                | 22.6 ms: 1.09x faster                                                 |
| pylint                           | 182 ms                                                 | 168 ms: 1.08x faster                                                  |
| comprehensions                   | 14.0 us                                                | 13.1 us: 1.07x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.89 us: 1.06x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.04x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.9 ms: 1.04x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.37 ms: 1.03x faster                                                 |
| json                             | 3.00 ms                                                | 2.92 ms: 1.03x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.03x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 74.8 ms: 1.02x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 74.0 ms: 1.02x faster                                                 |
| python_startup                   | 17.8 ms                                                | 17.4 ms: 1.02x faster                                                 |
| python_startup_no_site           | 13.2 ms                                                | 13.0 ms: 1.02x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.23 sec: 1.01x faster                                                |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 369 ms: 1.01x faster                                                  |
| dask                             | 779 ms                                                 | 771 ms: 1.01x faster                                                  |
| shortest_path                    | 331 ms                                                 | 327 ms: 1.01x faster                                                  |
| regex_dna                        | 143 ms                                                 | 143 ms: 1.00x slower                                                  |
| thrift                           | 468 us                                                 | 469 us: 1.00x slower                                                  |
| go                               | 98.5 ms                                                | 99.1 ms: 1.01x slower                                                 |
| connected_components             | 300 ms                                                 | 303 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.18 ms: 1.01x slower                                                 |
| sympy_integrate                  | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                 |
| html5lib                         | 33.4 ms                                                | 34.2 ms: 1.02x slower                                                 |
| pidigits                         | 283 ms                                                 | 290 ms: 1.03x slower                                                  |
| raytrace                         | 204 ms                                                 | 212 ms: 1.04x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 89.2 ms: 1.04x slower                                                 |
| docutils                         | 1.45 sec                                               | 1.51 sec: 1.04x slower                                                |
| scimark_fft                      | 194 ms                                                 | 203 ms: 1.04x slower                                                  |
| xml_etree_generate               | 55.4 ms                                                | 58.1 ms: 1.05x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.63 us: 1.05x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                 |
| float                            | 54.1 ms                                                | 57.4 ms: 1.06x slower                                                 |
| regex_compile                    | 75.9 ms                                                | 81.2 ms: 1.07x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.45 sec: 1.07x slower                                                |
| pyflate                          | 311 ms                                                 | 333 ms: 1.07x slower                                                  |
| sympy_str                        | 144 ms                                                 | 154 ms: 1.07x slower                                                  |
| generators                       | 29.4 ms                                                | 31.5 ms: 1.07x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 74.6 ms: 1.08x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 16.3 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                                 |
| deltablue                        | 2.57 ms                                                | 2.80 ms: 1.09x slower                                                 |
| pycparser                        | 673 ms                                                 | 740 ms: 1.10x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 6.82 ms: 1.10x slower                                                 |
| 2to3                             | 168 ms                                                 | 186 ms: 1.11x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 43.0 ms: 1.11x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 72.9 ms: 1.11x slower                                                 |
| logging_format                   | 3.90 us                                                | 4.35 us: 1.11x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 262 ms: 1.12x slower                                                  |
| logging_simple                   | 3.60 us                                                | 4.05 us: 1.12x slower                                                 |
| chaos                            | 41.6 ms                                                | 47.3 ms: 1.14x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 84.4 ms: 1.15x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.15x slower                                                  |
| hexiom                           | 4.38 ms                                                | 5.08 ms: 1.16x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.35 ms: 1.17x slower                                                 |
| nqueens                          | 59.5 ms                                                | 70.2 ms: 1.18x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 36.1 ms: 1.18x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 53.0 ms: 1.19x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 61.4 ms: 1.19x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 109 us: 1.20x slower                                                  |
| richards_super                   | 34.6 ms                                                | 41.7 ms: 1.20x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 17.7 ms: 1.21x slower                                                 |
| mako                             | 7.44 ms                                                | 9.04 ms: 1.21x slower                                                 |
| richards                         | 30.6 ms                                                | 37.2 ms: 1.22x slower                                                 |
| fannkuch                         | 250 ms                                                 | 304 ms: 1.22x slower                                                  |
| telco                            | 3.92 ms                                                | 4.77 ms: 1.22x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 178 us: 1.22x slower                                                  |
| many_optionals                   | 403 us                                                 | 493 us: 1.22x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 241 us: 1.23x slower                                                  |
| nbody                            | 67.6 ms                                                | 84.8 ms: 1.26x slower                                                 |
| coverage                         | 38.5 ms                                                | 48.9 ms: 1.27x slower                                                 |
| django_template                  | 19.7 ms                                                | 25.1 ms: 1.27x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.27 sec: 1.29x slower                                                |
| pprint_safe_repr                 | 483 ms                                                 | 629 ms: 1.30x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 342 ns: 4.72x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, sphinx
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 94.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x