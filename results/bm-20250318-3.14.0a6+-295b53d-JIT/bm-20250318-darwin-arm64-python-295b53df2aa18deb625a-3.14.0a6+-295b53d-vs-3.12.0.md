# Results vs. 3.12.0

- fork: python
- ref: 295b53df2aa18deb625a
- machine: darwin-arm64
- commit hash: 295b53d
- commit date: 2025-03-18
- overall geometric mean: 1.036x faster
- HPT reliability: 81.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 171 ms: 1.02x slower                                                   |
| docutils       | 1.45 sec                                               | 1.49 sec: 1.02x slower                                                 |
| html5lib       | 33.4 ms                                                | 32.4 ms: 1.03x faster                                                  |
| sphinx         | 613 ms                                                 | 598 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 378 ms: 1.76x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 388 ms: 1.73x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 393 ms: 1.71x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 388 ms: 1.59x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 162 ms: 1.58x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 203 ms: 1.57x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 169 ms: 1.56x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 206 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 422 ms: 1.25x faster                                                   |
| coroutines                       | 19.7 ms                                                | 17.3 ms: 1.14x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.13x faster                                                   |
| async_generators                 | 299 ms                                                 | 288 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 363 ms: 1.03x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 66.3 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 135 ms: 2.87x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.18x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 46.1 ms: 1.17x faster                                                  |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| nbody          | 67.6 ms                                                | 69.7 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.25 ms: 1.08x faster                                                  |
| regex_compile  | 75.9 ms                                                | 74.0 ms: 1.03x faster                                                  |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| regex_v8       | 15.1 ms                                                | 15.8 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 55.4 ms                                                | 51.9 ms: 1.07x faster                                                  |
| tomli_loads          | 1.36 sec                                               | 1.27 sec: 1.07x faster                                                 |
| xml_etree_process    | 38.9 ms                                                | 36.9 ms: 1.05x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 73.1 ms: 1.03x faster                                                  |
| unpickle_pure_python | 145 us                                                 | 143 us: 1.02x faster                                                   |
| json_loads           | 17.0 us                                                | 18.0 us: 1.05x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 213 us: 1.08x slower                                                   |
| json_dumps           | 6.19 ms                                                | 7.56 ms: 1.22x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 17.6 ms: 1.01x faster                                                  |
| python_startup_no_site | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.72 ms: 1.11x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 32.0 ms: 1.05x slower                                                  |
| genshi_text     | 14.7 ms                                                | 15.4 ms: 1.05x slower                                                  |
| django_template | 19.7 ms                                                | 22.6 ms: 1.15x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.8 ms: 2.51x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 378 ms: 1.76x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 388 ms: 1.73x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 393 ms: 1.71x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 388 ms: 1.59x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 162 ms: 1.58x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 203 ms: 1.57x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 169 ms: 1.56x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 206 ms: 1.50x faster                                                   |
| deepcopy                         | 226 us                                                 | 163 us: 1.39x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 422 ms: 1.25x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 20.9 us: 1.25x faster                                                  |
| generators                       | 29.4 ms                                                | 25.0 ms: 1.18x faster                                                  |
| float                            | 54.1 ms                                                | 46.1 ms: 1.17x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 65.3 ms: 1.17x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.72 us: 1.17x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.24 ms: 1.14x faster                                                  |
| coroutines                       | 19.7 ms                                                | 17.3 ms: 1.14x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.13x faster                                                   |
| dulwich_log                      | 29.2 ms                                                | 26.2 ms: 1.12x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.55 sec: 1.11x faster                                                 |
| mako                             | 7.44 ms                                                | 6.72 ms: 1.11x faster                                                  |
| comprehensions                   | 14.0 us                                                | 12.7 us: 1.11x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.25 ms: 1.08x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 61.0 ms: 1.07x faster                                                  |
| pylint                           | 182 ms                                                 | 170 ms: 1.07x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 3.07 sec: 1.07x faster                                                 |
| xml_etree_generate               | 55.4 ms                                                | 51.9 ms: 1.07x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.27 sec: 1.07x faster                                                 |
| raytrace                         | 204 ms                                                 | 193 ms: 1.06x faster                                                   |
| xml_etree_process                | 38.9 ms                                                | 36.9 ms: 1.05x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| async_generators                 | 299 ms                                                 | 288 ms: 1.04x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 73.1 ms: 1.03x faster                                                  |
| html5lib                         | 33.4 ms                                                | 32.4 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 363 ms: 1.03x faster                                                   |
| pathlib                          | 24.7 ms                                                | 24.0 ms: 1.03x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 74.0 ms: 1.03x faster                                                  |
| sphinx                           | 613 ms                                                 | 598 ms: 1.02x faster                                                   |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| unpickle_pure_python             | 145 us                                                 | 143 us: 1.02x faster                                                   |
| thrift                           | 468 us                                                 | 461 us: 1.01x faster                                                   |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                                   |
| python_startup                   | 17.8 ms                                                | 17.6 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.11 ms: 1.01x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 61.4 ms: 1.01x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 193 ms: 1.01x faster                                                   |
| mdp                              | 1.49 sec                                               | 1.49 sec: 1.00x faster                                                 |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| logging_format                   | 3.90 us                                                | 3.92 us: 1.00x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 66.3 ms: 1.01x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 76.9 ms: 1.01x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.56 us: 1.01x slower                                                  |
| richards_super                   | 34.6 ms                                                | 35.0 ms: 1.01x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                  |
| shortest_path                    | 331 ms                                                 | 335 ms: 1.01x slower                                                   |
| connected_components             | 300 ms                                                 | 305 ms: 1.02x slower                                                   |
| 2to3                             | 168 ms                                                 | 171 ms: 1.02x slower                                                   |
| go                               | 98.5 ms                                                | 100 ms: 1.02x slower                                                   |
| richards                         | 30.6 ms                                                | 31.3 ms: 1.02x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.49 sec: 1.02x slower                                                 |
| sympy_str                        | 144 ms                                                 | 148 ms: 1.03x slower                                                   |
| nbody                            | 67.6 ms                                                | 69.7 ms: 1.03x slower                                                  |
| pyflate                          | 311 ms                                                 | 323 ms: 1.04x slower                                                   |
| scimark_sor                      | 85.8 ms                                                | 89.1 ms: 1.04x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 46.5 ms: 1.05x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 15.8 ms: 1.05x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 32.0 ms: 1.05x slower                                                  |
| json                             | 3.00 ms                                                | 3.15 ms: 1.05x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 507 us: 1.05x slower                                                   |
| genshi_text                      | 14.7 ms                                                | 15.4 ms: 1.05x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.05x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.13 ms: 1.06x slower                                                  |
| pycparser                        | 673 ms                                                 | 715 ms: 1.06x slower                                                   |
| chaos                            | 41.6 ms                                                | 44.5 ms: 1.07x slower                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.05 ms: 1.07x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 251 ms: 1.08x slower                                                   |
| pprint_pformat                   | 986 ms                                                 | 1.06 sec: 1.08x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 213 us: 1.08x slower                                                   |
| typing_runtime_protocols         | 91.5 us                                                | 99.2 us: 1.08x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 79.7 ms: 1.08x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 12.0 ms: 1.09x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 527 ms: 1.09x slower                                                   |
| meteor_contest                   | 69.1 ms                                                | 76.0 ms: 1.10x slower                                                  |
| nqueens                          | 59.5 ms                                                | 66.0 ms: 1.11x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.30 ms: 1.13x slower                                                  |
| django_template                  | 19.7 ms                                                | 22.6 ms: 1.15x slower                                                  |
| hexiom                           | 4.38 ms                                                | 5.03 ms: 1.15x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                   |
| telco                            | 3.92 ms                                                | 4.58 ms: 1.17x slower                                                  |
| many_optionals                   | 403 us                                                 | 473 us: 1.17x slower                                                   |
| fannkuch                         | 250 ms                                                 | 294 ms: 1.17x slower                                                   |
| crypto_pyaes                     | 51.4 ms                                                | 60.7 ms: 1.18x slower                                                  |
| coverage                         | 38.5 ms                                                | 46.8 ms: 1.22x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.56 ms: 1.22x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 135 ms: 2.87x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (3): logging_simple, asyncio_websockets, logging_silent
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250318-3.14.0a6+-295b53d-JIT/bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 81.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x