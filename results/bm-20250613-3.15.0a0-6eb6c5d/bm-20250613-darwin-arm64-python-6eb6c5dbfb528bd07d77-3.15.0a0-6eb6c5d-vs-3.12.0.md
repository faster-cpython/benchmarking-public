# Results vs. 3.12.0

- fork: python
- ref: 6eb6c5dbfb528bd07d77
- machine: darwin-arm64
- commit hash: 6eb6c5d
- commit date: 2025-06-13
- overall geometric mean: 1.081x slower
- HPT reliability: 97.39%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 186 ms: 1.10x slower                                                  |
| docutils       | 1.45 sec                                               | 1.51 sec: 1.04x slower                                                |
| html5lib       | 33.4 ms                                                | 34.2 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 393 ms: 1.70x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 405 ms: 1.66x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 413 ms: 1.62x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 207 ms: 1.54x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 403 ms: 1.53x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 170 ms: 1.50x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 215 ms: 1.45x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 183 ms: 1.44x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 422 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 433 ms: 1.22x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| async_generators                 | 299 ms                                                 | 273 ms: 1.09x faster                                                  |
| coroutines                       | 19.7 ms                                                | 19.3 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 73.0 ms: 1.11x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 183 ms: 1.29x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                  |
| float          | 54.1 ms                                                | 57.7 ms: 1.07x slower                                                 |
| nbody          | 67.6 ms                                                | 84.7 ms: 1.25x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                 |
| regex_v8       | 15.1 ms                                                | 16.1 ms: 1.07x slower                                                 |
| regex_compile  | 75.9 ms                                                | 81.4 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| json_loads           | 17.0 us                                                | 16.6 us: 1.03x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 74.2 ms: 1.02x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 58.1 ms: 1.05x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.45 sec: 1.07x slower                                                |
| json_dumps           | 6.19 ms                                                | 6.83 ms: 1.10x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 43.0 ms: 1.11x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 177 us: 1.22x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 241 us: 1.22x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 17.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 13.2 ms                                                | 13.1 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 36.5 ms: 1.20x slower                                                 |
| genshi_text     | 14.7 ms                                                | 17.6 ms: 1.20x slower                                                 |
| mako            | 7.44 ms                                                | 9.19 ms: 1.23x slower                                                 |
| django_template | 19.7 ms                                                | 25.1 ms: 1.27x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.23x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 14.9 ms: 2.16x faster                                                 |
| mdp                              | 1.49 sec                                               | 829 ms: 1.80x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 393 ms: 1.70x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 405 ms: 1.66x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 413 ms: 1.62x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 207 ms: 1.54x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 403 ms: 1.53x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 170 ms: 1.50x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 215 ms: 1.45x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 183 ms: 1.44x faster                                                  |
| deepcopy                         | 226 us                                                 | 175 us: 1.29x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 422 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 433 ms: 1.22x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 21.8 us: 1.19x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.46 sec: 1.18x faster                                                |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| async_generators                 | 299 ms                                                 | 273 ms: 1.09x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 26.8 ms: 1.09x faster                                                 |
| pylint                           | 182 ms                                                 | 168 ms: 1.08x faster                                                  |
| comprehensions                   | 14.0 us                                                | 13.1 us: 1.07x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.90 us: 1.06x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.03x faster                                                 |
| json                             | 3.00 ms                                                | 2.94 ms: 1.02x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 74.9 ms: 1.02x faster                                                 |
| coroutines                       | 19.7 ms                                                | 19.3 ms: 1.02x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 74.2 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                                  |
| python_startup                   | 17.8 ms                                                | 17.5 ms: 1.02x faster                                                 |
| dask                             | 779 ms                                                 | 770 ms: 1.01x faster                                                  |
| python_startup_no_site           | 13.2 ms                                                | 13.1 ms: 1.01x faster                                                 |
| shortest_path                    | 331 ms                                                 | 328 ms: 1.01x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.28 sec: 1.00x faster                                                |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.17 ms: 1.01x slower                                                 |
| go                               | 98.5 ms                                                | 100 ms: 1.02x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                 |
| html5lib                         | 33.4 ms                                                | 34.2 ms: 1.03x slower                                                 |
| connected_components             | 300 ms                                                 | 308 ms: 1.03x slower                                                  |
| raytrace                         | 204 ms                                                 | 212 ms: 1.04x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.51 sec: 1.04x slower                                                |
| sqlite_synth                     | 1.55 us                                                | 1.61 us: 1.04x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 58.1 ms: 1.05x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 206 ms: 1.06x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 90.9 ms: 1.06x slower                                                 |
| float                            | 54.1 ms                                                | 57.7 ms: 1.07x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 81.3 ms: 1.07x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 16.1 ms: 1.07x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.45 sec: 1.07x slower                                                |
| regex_compile                    | 75.9 ms                                                | 81.4 ms: 1.07x slower                                                 |
| generators                       | 29.4 ms                                                | 31.5 ms: 1.07x slower                                                 |
| sympy_str                        | 144 ms                                                 | 154 ms: 1.07x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 74.5 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                                 |
| pyflate                          | 311 ms                                                 | 336 ms: 1.08x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.81 ms: 1.10x slower                                                 |
| pycparser                        | 673 ms                                                 | 741 ms: 1.10x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 6.83 ms: 1.10x slower                                                 |
| 2to3                             | 168 ms                                                 | 186 ms: 1.10x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 43.0 ms: 1.11x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 73.0 ms: 1.11x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 261 ms: 1.12x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.44 us: 1.14x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 84.3 ms: 1.15x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                  |
| logging_simple                   | 3.60 us                                                | 4.19 us: 1.16x slower                                                 |
| chaos                            | 41.6 ms                                                | 48.4 ms: 1.16x slower                                                 |
| hexiom                           | 4.38 ms                                                | 5.10 ms: 1.17x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.35 ms: 1.17x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 52.8 ms: 1.19x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 61.4 ms: 1.19x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 36.5 ms: 1.20x slower                                                 |
| nqueens                          | 59.5 ms                                                | 71.2 ms: 1.20x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 17.6 ms: 1.20x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 110 us: 1.21x slower                                                  |
| richards_super                   | 34.6 ms                                                | 41.9 ms: 1.21x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 177 us: 1.22x slower                                                  |
| telco                            | 3.92 ms                                                | 4.80 ms: 1.22x slower                                                 |
| richards                         | 30.6 ms                                                | 37.4 ms: 1.22x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 241 us: 1.22x slower                                                  |
| many_optionals                   | 403 us                                                 | 494 us: 1.23x slower                                                  |
| mako                             | 7.44 ms                                                | 9.19 ms: 1.23x slower                                                 |
| fannkuch                         | 250 ms                                                 | 310 ms: 1.24x slower                                                  |
| nbody                            | 67.6 ms                                                | 84.7 ms: 1.25x slower                                                 |
| django_template                  | 19.7 ms                                                | 25.1 ms: 1.27x slower                                                 |
| pprint_pformat                   | 986 ms                                                 | 1.27 sec: 1.29x slower                                                |
| pprint_safe_repr                 | 483 ms                                                 | 623 ms: 1.29x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 183 ms: 1.29x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 347 ns: 4.78x slower                                                  |
| coverage                         | 38.5 ms                                                | 335 ms: 8.71x slower                                                  |
| thrift                           | 468 us                                                 | 43.9 ms: 93.98x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.10x slower                                                          |

Benchmark hidden because not significant (4): asyncio_websockets, regex_dna, pathlib, sphinx
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250613-3.15.0a0-6eb6c5d/bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.081x slower

# HPT report

- Reliability score: 97.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x