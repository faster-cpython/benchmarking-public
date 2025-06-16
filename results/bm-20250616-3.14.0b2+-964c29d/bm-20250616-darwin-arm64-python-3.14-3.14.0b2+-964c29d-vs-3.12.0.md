# Results vs. 3.12.0

- fork: python
- ref: 3.14
- machine: darwin-arm64
- commit hash: 964c29d
- commit date: 2025-06-16
- overall geometric mean: 1.022x slower
- HPT reliability: 97.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 190 ms: 1.13x slower                                   |
| docutils       | 1.45 sec                                               | 1.52 sec: 1.05x slower                                 |
| html5lib       | 33.4 ms                                                | 34.3 ms: 1.03x slower                                  |
| sphinx         | 613 ms                                                 | 620 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 393 ms: 1.70x faster                                   |
| async_tree_io_tg                 | 673 ms                                                 | 403 ms: 1.67x faster                                   |
| async_tree_io                    | 672 ms                                                 | 414 ms: 1.62x faster                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 401 ms: 1.54x faster                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 207 ms: 1.54x faster                                   |
| async_tree_none_tg               | 255 ms                                                 | 171 ms: 1.49x faster                                   |
| async_tree_none                  | 263 ms                                                 | 183 ms: 1.44x faster                                   |
| async_tree_memoization           | 310 ms                                                 | 216 ms: 1.44x faster                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 423 ms: 1.25x faster                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 434 ms: 1.21x faster                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                   |
| async_generators                 | 299 ms                                                 | 274 ms: 1.09x faster                                   |
| coroutines                       | 19.7 ms                                                | 19.3 ms: 1.02x faster                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                   |
| async_tree_eager                 | 65.8 ms                                                | 73.1 ms: 1.11x slower                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 399 ms: 1.15x slower                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                   |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                   |
| float          | 54.1 ms                                                | 58.4 ms: 1.08x slower                                  |
| nbody          | 67.6 ms                                                | 86.5 ms: 1.28x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                  |
| regex_v8       | 15.1 ms                                                | 16.2 ms: 1.07x slower                                  |
| regex_compile  | 75.9 ms                                                | 81.9 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 74.2 ms: 1.02x faster                                  |
| xml_etree_generate   | 55.4 ms                                                | 58.5 ms: 1.06x slower                                  |
| json_loads           | 17.0 us                                                | 18.1 us: 1.06x slower                                  |
| tomli_loads          | 1.36 sec                                               | 1.47 sec: 1.08x slower                                 |
| json_dumps           | 6.19 ms                                                | 6.78 ms: 1.10x slower                                  |
| xml_etree_process    | 38.9 ms                                                | 43.7 ms: 1.12x slower                                  |
| unpickle_pure_python | 145 us                                                 | 177 us: 1.22x slower                                   |
| pickle_pure_python   | 197 us                                                 | 242 us: 1.23x slower                                   |
| Geometric mean       | (ref)                                                  | 1.08x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.4 ms: 1.02x slower                                  |
| python_startup         | 17.8 ms                                                | 18.4 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 7.44 ms                                                | 8.79 ms: 1.18x slower                                  |
| genshi_xml      | 30.5 ms                                                | 37.0 ms: 1.21x slower                                  |
| genshi_text     | 14.7 ms                                                | 17.8 ms: 1.22x slower                                  |
| django_template | 19.7 ms                                                | 25.6 ms: 1.30x slower                                  |
| Geometric mean  | (ref)                                                  | 1.23x slower                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 14.9 ms: 2.15x faster                                  |
| mdp                              | 1.49 sec                                               | 844 ms: 1.77x faster                                   |
| async_tree_eager_io              | 666 ms                                                 | 393 ms: 1.70x faster                                   |
| async_tree_io_tg                 | 673 ms                                                 | 403 ms: 1.67x faster                                   |
| async_tree_io                    | 672 ms                                                 | 414 ms: 1.62x faster                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 401 ms: 1.54x faster                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 207 ms: 1.54x faster                                   |
| async_tree_none_tg               | 255 ms                                                 | 171 ms: 1.49x faster                                   |
| async_tree_none                  | 263 ms                                                 | 183 ms: 1.44x faster                                   |
| async_tree_memoization           | 310 ms                                                 | 216 ms: 1.44x faster                                   |
| deepcopy                         | 226 us                                                 | 177 us: 1.28x faster                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 423 ms: 1.25x faster                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 434 ms: 1.21x faster                                   |
| k_core                           | 1.72 sec                                               | 1.47 sec: 1.17x faster                                 |
| deepcopy_memo                    | 26.0 us                                                | 22.3 us: 1.17x faster                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                   |
| async_generators                 | 299 ms                                                 | 274 ms: 1.09x faster                                   |
| dulwich_log                      | 29.2 ms                                                | 26.9 ms: 1.09x faster                                  |
| pathlib                          | 24.7 ms                                                | 23.0 ms: 1.07x faster                                  |
| pylint                           | 182 ms                                                 | 169 ms: 1.07x faster                                   |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.90 us: 1.06x faster                                  |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                  |
| coroutines                       | 19.7 ms                                                | 19.3 ms: 1.02x faster                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 74.2 ms: 1.02x faster                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                   |
| shortest_path                    | 331 ms                                                 | 326 ms: 1.01x faster                                   |
| dask                             | 779 ms                                                 | 771 ms: 1.01x faster                                   |
| connected_components             | 300 ms                                                 | 297 ms: 1.01x faster                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 3.26 sec: 1.01x faster                                 |
| comprehensions                   | 14.0 us                                                | 13.9 us: 1.01x faster                                  |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                   |
| sphinx                           | 613 ms                                                 | 620 ms: 1.01x slower                                   |
| json                             | 3.00 ms                                                | 3.04 ms: 1.01x slower                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.19 ms: 1.01x slower                                  |
| python_startup_no_site           | 13.2 ms                                                | 13.4 ms: 1.02x slower                                  |
| html5lib                         | 33.4 ms                                                | 34.3 ms: 1.03x slower                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.5 ms: 1.03x slower                                  |
| python_startup                   | 17.8 ms                                                | 18.4 ms: 1.04x slower                                  |
| raytrace                         | 204 ms                                                 | 213 ms: 1.04x slower                                   |
| go                               | 98.5 ms                                                | 103 ms: 1.04x slower                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 64.9 ms: 1.05x slower                                  |
| docutils                         | 1.45 sec                                               | 1.52 sec: 1.05x slower                                 |
| sqlite_synth                     | 1.55 us                                                | 1.63 us: 1.05x slower                                  |
| xml_etree_generate               | 55.4 ms                                                | 58.5 ms: 1.06x slower                                  |
| scimark_fft                      | 194 ms                                                 | 206 ms: 1.06x slower                                   |
| json_loads                       | 17.0 us                                                | 18.1 us: 1.06x slower                                  |
| regex_v8                         | 15.1 ms                                                | 16.2 ms: 1.07x slower                                  |
| sympy_sum                        | 76.2 ms                                                | 81.9 ms: 1.07x slower                                  |
| generators                       | 29.4 ms                                                | 31.6 ms: 1.08x slower                                  |
| scimark_sor                      | 85.8 ms                                                | 92.3 ms: 1.08x slower                                  |
| deltablue                        | 2.57 ms                                                | 2.77 ms: 1.08x slower                                  |
| float                            | 54.1 ms                                                | 58.4 ms: 1.08x slower                                  |
| regex_compile                    | 75.9 ms                                                | 81.9 ms: 1.08x slower                                  |
| sympy_str                        | 144 ms                                                 | 156 ms: 1.08x slower                                   |
| tomli_loads                      | 1.36 sec                                               | 1.47 sec: 1.08x slower                                 |
| meteor_contest                   | 69.1 ms                                                | 75.0 ms: 1.09x slower                                  |
| gc_traversal                     | 2.95 ms                                                | 3.20 ms: 1.09x slower                                  |
| pyflate                          | 311 ms                                                 | 340 ms: 1.10x slower                                   |
| json_dumps                       | 6.19 ms                                                | 6.78 ms: 1.10x slower                                  |
| pycparser                        | 673 ms                                                 | 745 ms: 1.11x slower                                   |
| async_tree_eager                 | 65.8 ms                                                | 73.1 ms: 1.11x slower                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.33 ms: 1.11x slower                                  |
| xml_etree_process                | 38.9 ms                                                | 43.7 ms: 1.12x slower                                  |
| 2to3                             | 168 ms                                                 | 190 ms: 1.13x slower                                   |
| logging_format                   | 3.90 us                                                | 4.41 us: 1.13x slower                                  |
| sympy_expand                     | 233 ms                                                 | 264 ms: 1.13x slower                                   |
| logging_simple                   | 3.60 us                                                | 4.11 us: 1.14x slower                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 399 ms: 1.15x slower                                   |
| scimark_lu                       | 73.5 ms                                                | 84.6 ms: 1.15x slower                                  |
| chaos                            | 41.6 ms                                                | 48.3 ms: 1.16x slower                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                  |
| mako                             | 7.44 ms                                                | 8.79 ms: 1.18x slower                                  |
| hexiom                           | 4.38 ms                                                | 5.17 ms: 1.18x slower                                  |
| crypto_pyaes                     | 51.4 ms                                                | 61.2 ms: 1.19x slower                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 53.3 ms: 1.20x slower                                  |
| richards_super                   | 34.6 ms                                                | 41.6 ms: 1.20x slower                                  |
| telco                            | 3.92 ms                                                | 4.72 ms: 1.21x slower                                  |
| nqueens                          | 59.5 ms                                                | 71.9 ms: 1.21x slower                                  |
| genshi_xml                       | 30.5 ms                                                | 37.0 ms: 1.21x slower                                  |
| genshi_text                      | 14.7 ms                                                | 17.8 ms: 1.22x slower                                  |
| richards                         | 30.6 ms                                                | 37.2 ms: 1.22x slower                                  |
| pprint_pformat                   | 986 ms                                                 | 1.20 sec: 1.22x slower                                 |
| unpickle_pure_python             | 145 us                                                 | 177 us: 1.22x slower                                   |
| pickle_pure_python               | 197 us                                                 | 242 us: 1.23x slower                                   |
| pprint_safe_repr                 | 483 ms                                                 | 594 ms: 1.23x slower                                   |
| fannkuch                         | 250 ms                                                 | 309 ms: 1.24x slower                                   |
| many_optionals                   | 403 us                                                 | 500 us: 1.24x slower                                   |
| typing_runtime_protocols         | 91.5 us                                                | 116 us: 1.26x slower                                   |
| nbody                            | 67.6 ms                                                | 86.5 ms: 1.28x slower                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                   |
| coverage                         | 38.5 ms                                                | 49.8 ms: 1.29x slower                                  |
| django_template                  | 19.7 ms                                                | 25.6 ms: 1.30x slower                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                   |
| logging_silent                   | 72.5 ns                                                | 342 ns: 4.71x slower                                   |
| Geometric mean                   | (ref)                                                  | 1.04x slower                                           |

Benchmark hidden because not significant (3): asyncio_websockets, spectral_norm, regex_dna
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250616-3.14.0b2+-964c29d/bm-20250616-darwin-arm64-python-3.14-3.14.0b2+-964c29d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.022x slower

# HPT report

- Reliability score: 97.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x