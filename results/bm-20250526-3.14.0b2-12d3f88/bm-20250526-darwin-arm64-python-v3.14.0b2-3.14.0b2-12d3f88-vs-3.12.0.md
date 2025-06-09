# Results vs. 3.12.0

- fork: python
- ref: v3.14.0b2
- machine: darwin-arm64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.031x slower
- HPT reliability: 98.72%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 190 ms: 1.13x slower                                       |
| docutils       | 1.45 sec                                               | 1.53 sec: 1.05x slower                                     |
| html5lib       | 33.4 ms                                                | 34.1 ms: 1.02x slower                                      |
| sphinx         | 613 ms                                                 | 627 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 394 ms: 1.69x faster                                       |
| async_tree_io_tg                 | 673 ms                                                 | 405 ms: 1.66x faster                                       |
| async_tree_io                    | 672 ms                                                 | 416 ms: 1.61x faster                                       |
| async_tree_eager_io_tg           | 617 ms                                                 | 402 ms: 1.53x faster                                       |
| async_tree_memoization_tg        | 318 ms                                                 | 208 ms: 1.53x faster                                       |
| async_tree_none_tg               | 255 ms                                                 | 171 ms: 1.49x faster                                       |
| async_tree_memoization           | 310 ms                                                 | 216 ms: 1.43x faster                                       |
| async_tree_none                  | 263 ms                                                 | 184 ms: 1.43x faster                                       |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 423 ms: 1.25x faster                                       |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 435 ms: 1.21x faster                                       |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                       |
| async_generators                 | 299 ms                                                 | 274 ms: 1.09x faster                                       |
| coroutines                       | 19.7 ms                                                | 19.3 ms: 1.02x faster                                      |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 369 ms: 1.01x faster                                       |
| async_tree_eager                 | 65.8 ms                                                | 73.6 ms: 1.12x slower                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                       |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                       |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                       |
| float          | 54.1 ms                                                | 58.7 ms: 1.08x slower                                      |
| nbody          | 67.6 ms                                                | 86.7 ms: 1.28x slower                                      |
| Geometric mean | (ref)                                                  | 1.12x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                      |
| regex_v8       | 15.1 ms                                                | 16.2 ms: 1.07x slower                                      |
| regex_compile  | 75.9 ms                                                | 82.4 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 100 ms: 1.07x faster                                       |
| xml_etree_iterparse  | 75.5 ms                                                | 70.7 ms: 1.07x faster                                      |
| xml_etree_generate   | 55.4 ms                                                | 58.8 ms: 1.06x slower                                      |
| json_loads           | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| tomli_loads          | 1.36 sec                                               | 1.47 sec: 1.08x slower                                     |
| json_dumps           | 6.19 ms                                                | 6.85 ms: 1.11x slower                                      |
| xml_etree_process    | 38.9 ms                                                | 43.9 ms: 1.13x slower                                      |
| unpickle_pure_python | 145 us                                                 | 177 us: 1.22x slower                                       |
| pickle_pure_python   | 197 us                                                 | 241 us: 1.22x slower                                       |
| Geometric mean       | (ref)                                                  | 1.08x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 18.7 ms: 1.42x slower                                      |
| python_startup         | 17.8 ms                                                | 31.4 ms: 1.77x slower                                      |
| Geometric mean         | (ref)                                                  | 1.58x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 7.44 ms                                                | 8.72 ms: 1.17x slower                                      |
| genshi_xml      | 30.5 ms                                                | 37.0 ms: 1.21x slower                                      |
| genshi_text     | 14.7 ms                                                | 18.1 ms: 1.23x slower                                      |
| django_template | 19.7 ms                                                | 25.6 ms: 1.30x slower                                      |
| Geometric mean  | (ref)                                                  | 1.23x slower                                               |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 15.0 ms: 2.15x faster                                      |
| mdp                              | 1.49 sec                                               | 852 ms: 1.75x faster                                       |
| async_tree_eager_io              | 666 ms                                                 | 394 ms: 1.69x faster                                       |
| async_tree_io_tg                 | 673 ms                                                 | 405 ms: 1.66x faster                                       |
| async_tree_io                    | 672 ms                                                 | 416 ms: 1.61x faster                                       |
| async_tree_eager_io_tg           | 617 ms                                                 | 402 ms: 1.53x faster                                       |
| async_tree_memoization_tg        | 318 ms                                                 | 208 ms: 1.53x faster                                       |
| async_tree_none_tg               | 255 ms                                                 | 171 ms: 1.49x faster                                       |
| async_tree_memoization           | 310 ms                                                 | 216 ms: 1.43x faster                                       |
| async_tree_none                  | 263 ms                                                 | 184 ms: 1.43x faster                                       |
| deepcopy                         | 226 us                                                 | 180 us: 1.26x faster                                       |
| pathlib                          | 24.7 ms                                                | 19.7 ms: 1.25x faster                                      |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 423 ms: 1.25x faster                                       |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 435 ms: 1.21x faster                                       |
| k_core                           | 1.72 sec                                               | 1.47 sec: 1.17x faster                                     |
| deepcopy_memo                    | 26.0 us                                                | 22.5 us: 1.16x faster                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                       |
| dulwich_log                      | 29.2 ms                                                | 26.8 ms: 1.09x faster                                      |
| async_generators                 | 299 ms                                                 | 274 ms: 1.09x faster                                       |
| xml_etree_parse                  | 108 ms                                                 | 100 ms: 1.07x faster                                       |
| xml_etree_iterparse              | 75.5 ms                                                | 70.7 ms: 1.07x faster                                      |
| pylint                           | 182 ms                                                 | 172 ms: 1.06x faster                                       |
| deepcopy_reduce                  | 2.01 us                                                | 1.93 us: 1.04x faster                                      |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                      |
| shortest_path                    | 331 ms                                                 | 325 ms: 1.02x faster                                       |
| coroutines                       | 19.7 ms                                                | 19.3 ms: 1.02x faster                                      |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 369 ms: 1.01x faster                                       |
| connected_components             | 300 ms                                                 | 298 ms: 1.01x faster                                       |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                       |
| comprehensions                   | 14.0 us                                                | 14.0 us: 1.00x slower                                      |
| spectral_norm                    | 76.5 ms                                                | 77.0 ms: 1.01x slower                                      |
| json                             | 3.00 ms                                                | 3.05 ms: 1.01x slower                                      |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.19 ms: 1.01x slower                                      |
| html5lib                         | 33.4 ms                                                | 34.1 ms: 1.02x slower                                      |
| sphinx                           | 613 ms                                                 | 627 ms: 1.02x slower                                       |
| sympy_integrate                  | 11.1 ms                                                | 11.5 ms: 1.04x slower                                      |
| go                               | 98.5 ms                                                | 103 ms: 1.04x slower                                       |
| raytrace                         | 204 ms                                                 | 213 ms: 1.04x slower                                       |
| docutils                         | 1.45 sec                                               | 1.53 sec: 1.05x slower                                     |
| sqlite_synth                     | 1.55 us                                                | 1.62 us: 1.05x slower                                      |
| sqlalchemy_declarative           | 61.9 ms                                                | 65.1 ms: 1.05x slower                                      |
| xml_etree_generate               | 55.4 ms                                                | 58.8 ms: 1.06x slower                                      |
| scimark_fft                      | 194 ms                                                 | 206 ms: 1.06x slower                                       |
| json_loads                       | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| regex_v8                         | 15.1 ms                                                | 16.2 ms: 1.07x slower                                      |
| sympy_sum                        | 76.2 ms                                                | 81.9 ms: 1.07x slower                                      |
| generators                       | 29.4 ms                                                | 31.6 ms: 1.08x slower                                      |
| gc_traversal                     | 2.95 ms                                                | 3.18 ms: 1.08x slower                                      |
| tomli_loads                      | 1.36 sec                                               | 1.47 sec: 1.08x slower                                     |
| scimark_sor                      | 85.8 ms                                                | 92.8 ms: 1.08x slower                                      |
| deltablue                        | 2.57 ms                                                | 2.78 ms: 1.08x slower                                      |
| float                            | 54.1 ms                                                | 58.7 ms: 1.08x slower                                      |
| regex_compile                    | 75.9 ms                                                | 82.4 ms: 1.08x slower                                      |
| meteor_contest                   | 69.1 ms                                                | 75.0 ms: 1.09x slower                                      |
| sympy_str                        | 144 ms                                                 | 156 ms: 1.09x slower                                       |
| pyflate                          | 311 ms                                                 | 342 ms: 1.10x slower                                       |
| pycparser                        | 673 ms                                                 | 745 ms: 1.11x slower                                       |
| json_dumps                       | 6.19 ms                                                | 6.85 ms: 1.11x slower                                      |
| async_tree_eager                 | 65.8 ms                                                | 73.6 ms: 1.12x slower                                      |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.39 ms: 1.12x slower                                      |
| xml_etree_process                | 38.9 ms                                                | 43.9 ms: 1.13x slower                                      |
| 2to3                             | 168 ms                                                 | 190 ms: 1.13x slower                                       |
| logging_format                   | 3.90 us                                                | 4.41 us: 1.13x slower                                      |
| sympy_expand                     | 233 ms                                                 | 265 ms: 1.13x slower                                       |
| scimark_lu                       | 73.5 ms                                                | 83.6 ms: 1.14x slower                                      |
| logging_simple                   | 3.60 us                                                | 4.10 us: 1.14x slower                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                       |
| chaos                            | 41.6 ms                                                | 48.3 ms: 1.16x slower                                      |
| mako                             | 7.44 ms                                                | 8.72 ms: 1.17x slower                                      |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                      |
| hexiom                           | 4.38 ms                                                | 5.17 ms: 1.18x slower                                      |
| crypto_pyaes                     | 51.4 ms                                                | 61.5 ms: 1.20x slower                                      |
| telco                            | 3.92 ms                                                | 4.73 ms: 1.21x slower                                      |
| richards_super                   | 34.6 ms                                                | 41.9 ms: 1.21x slower                                      |
| scimark_monte_carlo              | 44.5 ms                                                | 53.8 ms: 1.21x slower                                      |
| nqueens                          | 59.5 ms                                                | 72.1 ms: 1.21x slower                                      |
| genshi_xml                       | 30.5 ms                                                | 37.0 ms: 1.21x slower                                      |
| unpickle_pure_python             | 145 us                                                 | 177 us: 1.22x slower                                       |
| pprint_pformat                   | 986 ms                                                 | 1.20 sec: 1.22x slower                                     |
| pickle_pure_python               | 197 us                                                 | 241 us: 1.22x slower                                       |
| richards                         | 30.6 ms                                                | 37.5 ms: 1.23x slower                                      |
| genshi_text                      | 14.7 ms                                                | 18.1 ms: 1.23x slower                                      |
| pprint_safe_repr                 | 483 ms                                                 | 598 ms: 1.24x slower                                       |
| many_optionals                   | 403 us                                                 | 501 us: 1.24x slower                                       |
| fannkuch                         | 250 ms                                                 | 312 ms: 1.25x slower                                       |
| typing_runtime_protocols         | 91.5 us                                                | 115 us: 1.25x slower                                       |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                       |
| nbody                            | 67.6 ms                                                | 86.7 ms: 1.28x slower                                      |
| coverage                         | 38.5 ms                                                | 49.6 ms: 1.29x slower                                      |
| django_template                  | 19.7 ms                                                | 25.6 ms: 1.30x slower                                      |
| python_startup_no_site           | 13.2 ms                                                | 18.7 ms: 1.42x slower                                      |
| python_startup                   | 17.8 ms                                                | 31.4 ms: 1.77x slower                                      |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                       |
| logging_silent                   | 72.5 ns                                                | 346 ns: 4.77x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.05x slower                                               |

Benchmark hidden because not significant (3): asyncio_websockets, regex_dna, bpe_tokeniser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.031x slower

# HPT report

- Reliability score: 98.72% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x