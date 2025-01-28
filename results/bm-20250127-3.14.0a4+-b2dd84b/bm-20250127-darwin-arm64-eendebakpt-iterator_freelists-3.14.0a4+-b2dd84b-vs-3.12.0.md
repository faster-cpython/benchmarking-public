# Results vs. 3.12.0

- fork: eendebakpt
- ref: iterator_freelists
- machine: darwin-arm64
- commit hash: b2dd84b
- commit date: 2025-01-27
- overall geometric mean: 1.100x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 187 ms: 1.11x slower                                                     |
| docutils       | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                   |
| html5lib       | 33.4 ms                                                | 28.9 ms: 1.16x faster                                                    |
| sphinx         | 613 ms                                                 | 559 ms: 1.10x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io                    | 672 ms                                                 | 360 ms: 1.87x faster                                                     |
| async_tree_io_tg                 | 673 ms                                                 | 360 ms: 1.87x faster                                                     |
| async_tree_eager_io              | 666 ms                                                 | 360 ms: 1.85x faster                                                     |
| async_tree_none_tg               | 255 ms                                                 | 152 ms: 1.68x faster                                                     |
| async_tree_eager_io_tg           | 617 ms                                                 | 371 ms: 1.67x faster                                                     |
| async_tree_none                  | 263 ms                                                 | 159 ms: 1.66x faster                                                     |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                     |
| async_tree_memoization           | 310 ms                                                 | 198 ms: 1.57x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 416 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                                     |
| coroutines                       | 19.7 ms                                                | 15.9 ms: 1.24x faster                                                    |
| async_generators                 | 299 ms                                                 | 247 ms: 1.21x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                     |
| async_tree_eager                 | 65.8 ms                                                | 62.1 ms: 1.06x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 358 ms: 1.05x faster                                                     |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 395 ms: 1.14x slower                                                     |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.24x slower                                                     |
| async_tree_eager_tg              | 46.9 ms                                                | 132 ms: 2.81x slower                                                     |
| Geometric mean                   | (ref)                                                  | 1.24x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 46.0 ms: 1.18x faster                                                    |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                     |
| nbody          | 67.6 ms                                                | 68.1 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 66.2 ms: 1.15x faster                                                    |
| regex_effbot   | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                    |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                     |
| regex_v8       | 15.1 ms                                                | 16.6 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 75.5 ms                                                | 71.0 ms: 1.06x faster                                                    |
| xml_etree_generate   | 55.4 ms                                                | 52.3 ms: 1.06x faster                                                    |
| unpickle_pure_python | 145 us                                                 | 138 us: 1.06x faster                                                     |
| xml_etree_process    | 38.9 ms                                                | 38.0 ms: 1.02x faster                                                    |
| pickle_pure_python   | 197 us                                                 | 195 us: 1.01x faster                                                     |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                    |
| json_dumps           | 6.19 ms                                                | 7.40 ms: 1.20x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.6 ms: 1.10x slower                                                    |
| python_startup_no_site | 13.2 ms                                                | 14.8 ms: 1.13x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 13.1 ms: 1.12x faster                                                    |
| genshi_xml      | 30.5 ms                                                | 28.0 ms: 1.09x faster                                                    |
| mako            | 7.44 ms                                                | 6.97 ms: 1.07x faster                                                    |
| django_template | 19.7 ms                                                | 20.3 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                             |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-darwin-arm64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.8 ms: 2.72x faster                                                    |
| async_tree_io                    | 672 ms                                                 | 360 ms: 1.87x faster                                                     |
| async_tree_io_tg                 | 673 ms                                                 | 360 ms: 1.87x faster                                                     |
| async_tree_eager_io              | 666 ms                                                 | 360 ms: 1.85x faster                                                     |
| async_tree_none_tg               | 255 ms                                                 | 152 ms: 1.68x faster                                                     |
| async_tree_eager_io_tg           | 617 ms                                                 | 371 ms: 1.67x faster                                                     |
| async_tree_none                  | 263 ms                                                 | 159 ms: 1.66x faster                                                     |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                     |
| async_tree_memoization           | 310 ms                                                 | 198 ms: 1.57x faster                                                     |
| deepcopy                         | 226 us                                                 | 147 us: 1.54x faster                                                     |
| deepcopy_memo                    | 26.0 us                                                | 17.9 us: 1.45x faster                                                    |
| generators                       | 29.4 ms                                                | 22.4 ms: 1.31x faster                                                    |
| deepcopy_reduce                  | 2.01 us                                                | 1.54 us: 1.31x faster                                                    |
| go                               | 98.5 ms                                                | 77.0 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 416 ms: 1.27x faster                                                     |
| spectral_norm                    | 76.5 ms                                                | 60.4 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                                     |
| coroutines                       | 19.7 ms                                                | 15.9 ms: 1.24x faster                                                    |
| raytrace                         | 204 ms                                                 | 168 ms: 1.21x faster                                                     |
| async_generators                 | 299 ms                                                 | 247 ms: 1.21x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                     |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.64 ms: 1.19x faster                                                    |
| comprehensions                   | 14.0 us                                                | 11.8 us: 1.19x faster                                                    |
| float                            | 54.1 ms                                                | 46.0 ms: 1.18x faster                                                    |
| pylint                           | 182 ms                                                 | 157 ms: 1.16x faster                                                     |
| html5lib                         | 33.4 ms                                                | 28.9 ms: 1.16x faster                                                    |
| bpe_tokeniser                    | 3.28 sec                                               | 2.85 sec: 1.15x faster                                                   |
| k_core                           | 1.72 sec                                               | 1.50 sec: 1.15x faster                                                   |
| regex_compile                    | 75.9 ms                                                | 66.2 ms: 1.15x faster                                                    |
| logging_simple                   | 3.60 us                                                | 3.15 us: 1.15x faster                                                    |
| tomli_loads                      | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                   |
| scimark_fft                      | 194 ms                                                 | 172 ms: 1.13x faster                                                     |
| logging_format                   | 3.90 us                                                | 3.47 us: 1.12x faster                                                    |
| chaos                            | 41.6 ms                                                | 37.1 ms: 1.12x faster                                                    |
| deltablue                        | 2.57 ms                                                | 2.29 ms: 1.12x faster                                                    |
| genshi_text                      | 14.7 ms                                                | 13.1 ms: 1.12x faster                                                    |
| scimark_sor                      | 85.8 ms                                                | 77.0 ms: 1.11x faster                                                    |
| sphinx                           | 613 ms                                                 | 559 ms: 1.10x faster                                                     |
| thrift                           | 468 us                                                 | 427 us: 1.10x faster                                                     |
| genshi_xml                       | 30.5 ms                                                | 28.0 ms: 1.09x faster                                                    |
| logging_silent                   | 72.5 ns                                                | 66.6 ns: 1.09x faster                                                    |
| dulwich_log                      | 29.2 ms                                                | 26.8 ms: 1.09x faster                                                    |
| regex_effbot                     | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                    |
| pathlib                          | 24.7 ms                                                | 22.7 ms: 1.09x faster                                                    |
| pyflate                          | 311 ms                                                 | 287 ms: 1.08x faster                                                     |
| bench_mp_pool                    | 65.5 ms                                                | 60.5 ms: 1.08x faster                                                    |
| sqlalchemy_declarative           | 61.9 ms                                                | 57.6 ms: 1.07x faster                                                    |
| mako                             | 7.44 ms                                                | 6.97 ms: 1.07x faster                                                    |
| pprint_pformat                   | 986 ms                                                 | 924 ms: 1.07x faster                                                     |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                     |
| sqlglot_parse                    | 808 us                                                 | 760 us: 1.06x faster                                                     |
| xml_etree_iterparse              | 75.5 ms                                                | 71.0 ms: 1.06x faster                                                    |
| pprint_safe_repr                 | 483 ms                                                 | 455 ms: 1.06x faster                                                     |
| pycparser                        | 673 ms                                                 | 634 ms: 1.06x faster                                                     |
| xml_etree_generate               | 55.4 ms                                                | 52.3 ms: 1.06x faster                                                    |
| async_tree_eager                 | 65.8 ms                                                | 62.1 ms: 1.06x faster                                                    |
| sqlglot_transpile                | 973 us                                                 | 920 us: 1.06x faster                                                     |
| unpickle_pure_python             | 145 us                                                 | 138 us: 1.06x faster                                                     |
| sympy_str                        | 144 ms                                                 | 136 ms: 1.06x faster                                                     |
| scimark_monte_carlo              | 44.5 ms                                                | 42.2 ms: 1.05x faster                                                    |
| nqueens                          | 59.5 ms                                                | 56.5 ms: 1.05x faster                                                    |
| sympy_sum                        | 76.2 ms                                                | 72.6 ms: 1.05x faster                                                    |
| hexiom                           | 4.38 ms                                                | 4.18 ms: 1.05x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 358 ms: 1.05x faster                                                     |
| docutils                         | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                   |
| sqlglot_optimize                 | 33.2 ms                                                | 31.9 ms: 1.04x faster                                                    |
| fannkuch                         | 250 ms                                                 | 242 ms: 1.03x faster                                                     |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.39 ms: 1.03x faster                                                    |
| bench_thread_pool                | 483 us                                                 | 468 us: 1.03x faster                                                     |
| shortest_path                    | 331 ms                                                 | 323 ms: 1.02x faster                                                     |
| scimark_lu                       | 73.5 ms                                                | 71.8 ms: 1.02x faster                                                    |
| xml_etree_process                | 38.9 ms                                                | 38.0 ms: 1.02x faster                                                    |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                     |
| sqlglot_normalize                | 180 ms                                                 | 176 ms: 1.02x faster                                                     |
| sympy_expand                     | 233 ms                                                 | 229 ms: 1.02x faster                                                     |
| sqlite_synth                     | 1.55 us                                                | 1.52 us: 1.02x faster                                                    |
| connected_components             | 300 ms                                                 | 296 ms: 1.01x faster                                                     |
| dask                             | 779 ms                                                 | 770 ms: 1.01x faster                                                     |
| pickle_pure_python               | 197 us                                                 | 195 us: 1.01x faster                                                     |
| sympy_integrate                  | 11.1 ms                                                | 11.0 ms: 1.01x faster                                                    |
| mdp                              | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                     |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                     |
| richards_super                   | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                    |
| nbody                            | 67.6 ms                                                | 68.1 ms: 1.01x slower                                                    |
| meteor_contest                   | 69.1 ms                                                | 70.1 ms: 1.01x slower                                                    |
| crypto_pyaes                     | 51.4 ms                                                | 52.6 ms: 1.02x slower                                                    |
| richards                         | 30.6 ms                                                | 31.3 ms: 1.02x slower                                                    |
| django_template                  | 19.7 ms                                                | 20.3 ms: 1.03x slower                                                    |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                    |
| gc_traversal                     | 2.95 ms                                                | 3.12 ms: 1.06x slower                                                    |
| many_optionals                   | 403 us                                                 | 431 us: 1.07x slower                                                     |
| regex_v8                         | 15.1 ms                                                | 16.6 ms: 1.10x slower                                                    |
| python_startup                   | 17.8 ms                                                | 19.6 ms: 1.10x slower                                                    |
| 2to3                             | 168 ms                                                 | 187 ms: 1.11x slower                                                     |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.12x slower                                                    |
| python_startup_no_site           | 13.2 ms                                                | 14.8 ms: 1.13x slower                                                    |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 395 ms: 1.14x slower                                                     |
| telco                            | 3.92 ms                                                | 4.56 ms: 1.16x slower                                                    |
| coverage                         | 38.5 ms                                                | 45.7 ms: 1.19x slower                                                    |
| json_dumps                       | 6.19 ms                                                | 7.40 ms: 1.20x slower                                                    |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.24x slower                                                     |
| async_tree_eager_tg              | 46.9 ms                                                | 132 ms: 2.81x slower                                                     |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                             |

Benchmark hidden because not significant (2): json, typing_runtime_protocols
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.100x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x