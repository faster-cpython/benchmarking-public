# Results vs. 3.12.0

- fork: python
- ref: 9c7b2af73dee2b997936
- machine: darwin-arm64
- commit hash: 9c7b2af
- commit date: 2025-07-21
- overall geometric mean: 1.070x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 169 ms: 1.00x slower                                                  |
| html5lib       | 33.4 ms                                                | 32.8 ms: 1.02x faster                                                 |
| sphinx         | 613 ms                                                 | 573 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 361 ms: 1.84x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 368 ms: 1.83x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 380 ms: 1.77x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 370 ms: 1.67x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 191 ms: 1.66x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.63x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 165 ms: 1.60x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 194 ms: 1.60x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 412 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 418 ms: 1.26x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.19x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                 |
| async_generators                 | 299 ms                                                 | 284 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 63.9 ms: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 167 ms: 1.18x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.74x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 51.2 ms: 1.06x faster                                                 |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| nbody          | 67.6 ms                                                | 72.4 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.16 ms: 1.13x faster                                                 |
| regex_compile  | 75.9 ms                                                | 72.3 ms: 1.05x faster                                                 |
| regex_dna      | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 145 us                                                 | 127 us: 1.14x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 34.3 ms: 1.13x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 49.3 ms: 1.13x faster                                                 |
| tomli_loads          | 1.36 sec                                               | 1.22 sec: 1.12x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 72.6 ms: 1.04x faster                                                 |
| pickle_pure_python   | 197 us                                                 | 206 us: 1.05x slower                                                  |
| json_dumps           | 6.19 ms                                                | 6.55 ms: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 17.2 ms: 1.03x faster                                                 |
| python_startup_no_site | 13.2 ms                                                | 12.9 ms: 1.02x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.57 ms: 1.13x faster                                                 |
| genshi_text     | 14.7 ms                                                | 15.3 ms: 1.04x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 33.0 ms: 1.08x slower                                                 |
| django_template | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.49 sec                                               | 744 ms: 2.01x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 361 ms: 1.84x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 368 ms: 1.83x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 380 ms: 1.77x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 370 ms: 1.67x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 191 ms: 1.66x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.63x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 165 ms: 1.60x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 194 ms: 1.60x faster                                                  |
| deepcopy                         | 226 us                                                 | 172 us: 1.32x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 412 ms: 1.28x faster                                                  |
| subparsers                       | 32.1 ms                                                | 25.4 ms: 1.27x faster                                                 |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 418 ms: 1.26x faster                                                  |
| comprehensions                   | 14.0 us                                                | 11.2 us: 1.25x faster                                                 |
| deepcopy_memo                    | 26.0 us                                                | 21.5 us: 1.21x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 63.4 ms: 1.21x faster                                                 |
| generators                       | 29.4 ms                                                | 24.5 ms: 1.20x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.19x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                 |
| raytrace                         | 204 ms                                                 | 172 ms: 1.19x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 25.0 ms: 1.17x faster                                                 |
| go                               | 98.5 ms                                                | 86.0 ms: 1.14x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 127 us: 1.14x faster                                                  |
| mako                             | 7.44 ms                                                | 6.57 ms: 1.13x faster                                                 |
| xml_etree_process                | 38.9 ms                                                | 34.3 ms: 1.13x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.78 us: 1.13x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 2.90 sec: 1.13x faster                                                |
| regex_effbot                     | 2.44 ms                                                | 2.16 ms: 1.13x faster                                                 |
| pylint                           | 182 ms                                                 | 161 ms: 1.13x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 49.3 ms: 1.13x faster                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.22 sec: 1.12x faster                                                |
| pyflate                          | 311 ms                                                 | 283 ms: 1.10x faster                                                  |
| pathlib                          | 24.7 ms                                                | 22.7 ms: 1.09x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.59 sec: 1.08x faster                                                |
| chaos                            | 41.6 ms                                                | 38.4 ms: 1.08x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.36 us: 1.07x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.64 us: 1.07x faster                                                 |
| sphinx                           | 613 ms                                                 | 573 ms: 1.07x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.40 ms: 1.07x faster                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 457 ms: 1.06x faster                                                  |
| pprint_pformat                   | 986 ms                                                 | 931 ms: 1.06x faster                                                  |
| float                            | 54.1 ms                                                | 51.2 ms: 1.06x faster                                                 |
| async_generators                 | 299 ms                                                 | 284 ms: 1.05x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 72.3 ms: 1.05x faster                                                 |
| thrift                           | 468 us                                                 | 448 us: 1.04x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 72.6 ms: 1.04x faster                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 49.6 ms: 1.04x faster                                                 |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| python_startup                   | 17.8 ms                                                | 17.2 ms: 1.03x faster                                                 |
| scimark_fft                      | 194 ms                                                 | 188 ms: 1.03x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 83.2 ms: 1.03x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 63.9 ms: 1.03x faster                                                 |
| python_startup_no_site           | 13.2 ms                                                | 12.9 ms: 1.02x faster                                                 |
| html5lib                         | 33.4 ms                                                | 32.8 ms: 1.02x faster                                                 |
| sympy_integrate                  | 11.1 ms                                                | 10.9 ms: 1.01x faster                                                 |
| dask                             | 779 ms                                                 | 770 ms: 1.01x faster                                                  |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| fannkuch                         | 250 ms                                                 | 249 ms: 1.00x faster                                                  |
| 2to3                             | 168 ms                                                 | 169 ms: 1.00x slower                                                  |
| sympy_str                        | 144 ms                                                 | 144 ms: 1.00x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 73.3 ns: 1.01x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 15.3 ms: 1.01x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 45.2 ms: 1.02x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 74.9 ms: 1.02x slower                                                 |
| nqueens                          | 59.5 ms                                                | 61.0 ms: 1.03x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 94.1 us: 1.03x slower                                                 |
| pycparser                        | 673 ms                                                 | 693 ms: 1.03x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.03x slower                                                 |
| hexiom                           | 4.38 ms                                                | 4.53 ms: 1.03x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 71.8 ms: 1.04x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 15.3 ms: 1.04x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 206 us: 1.05x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 245 ms: 1.05x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.30 ms: 1.05x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 6.55 ms: 1.06x slower                                                 |
| shortest_path                    | 331 ms                                                 | 351 ms: 1.06x slower                                                  |
| nbody                            | 67.6 ms                                                | 72.4 ms: 1.07x slower                                                 |
| connected_components             | 300 ms                                                 | 322 ms: 1.07x slower                                                  |
| richards_super                   | 34.6 ms                                                | 37.4 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 33.0 ms: 1.08x slower                                                 |
| richards                         | 30.6 ms                                                | 33.3 ms: 1.09x slower                                                 |
| telco                            | 3.92 ms                                                | 4.39 ms: 1.12x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| django_template                  | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 167 ms: 1.18x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                 |
| coverage                         | 38.5 ms                                                | 47.4 ms: 1.23x slower                                                 |
| many_optionals                   | 403 us                                                 | 593 us: 1.47x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.74x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (5): json_loads, docutils, asyncio_websockets, json, sympy_sum
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250721-3.15.0a0-9c7b2af-JIT/bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.070x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.14x