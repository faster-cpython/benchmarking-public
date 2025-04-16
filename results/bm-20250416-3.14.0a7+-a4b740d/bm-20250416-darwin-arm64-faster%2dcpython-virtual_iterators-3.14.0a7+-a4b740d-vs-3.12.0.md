# Results vs. 3.12.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: darwin-arm64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.034x slower
- HPT reliability: 99.44%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 218 ms: 1.30x slower                                                          |
| docutils       | 1.45 sec                                               | 1.59 sec: 1.09x slower                                                        |
| html5lib       | 33.4 ms                                                | 36.3 ms: 1.09x slower                                                         |
| sphinx         | 613 ms                                                 | 620 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.12x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 406 ms: 1.66x faster                                                          |
| async_tree_eager_io              | 666 ms                                                 | 405 ms: 1.65x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 424 ms: 1.58x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 413 ms: 1.49x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 214 ms: 1.48x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 174 ms: 1.46x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 185 ms: 1.43x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 221 ms: 1.40x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 424 ms: 1.25x faster                                                          |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 431 ms: 1.22x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                          |
| async_generators                 | 299 ms                                                 | 272 ms: 1.10x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 370 ms: 1.01x faster                                                          |
| asyncio_websockets               | 243 ms                                                 | 245 ms: 1.01x slower                                                          |
| coroutines                       | 19.7 ms                                                | 20.3 ms: 1.03x slower                                                         |
| async_tree_eager                 | 65.8 ms                                                | 75.2 ms: 1.14x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                          |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 189 ms: 1.33x slower                                                          |
| async_tree_eager_tg              | 46.9 ms                                                | 147 ms: 3.13x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.12x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| float          | 54.1 ms                                                | 56.4 ms: 1.04x slower                                                         |
| nbody          | 67.6 ms                                                | 87.0 ms: 1.29x slower                                                         |
| Geometric mean | (ref)                                                  | 1.10x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.30 ms: 1.06x faster                                                         |
| regex_dna      | 143 ms                                                 | 141 ms: 1.02x faster                                                          |
| regex_v8       | 15.1 ms                                                | 15.8 ms: 1.05x slower                                                         |
| regex_compile  | 75.9 ms                                                | 82.8 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                          |
| xml_etree_iterparse  | 75.5 ms                                                | 76.3 ms: 1.01x slower                                                         |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                                         |
| tomli_loads          | 1.36 sec                                               | 1.48 sec: 1.09x slower                                                        |
| xml_etree_generate   | 55.4 ms                                                | 62.2 ms: 1.12x slower                                                         |
| xml_etree_process    | 38.9 ms                                                | 46.0 ms: 1.18x slower                                                         |
| unpickle_pure_python | 145 us                                                 | 181 us: 1.25x slower                                                          |
| pickle_pure_python   | 197 us                                                 | 247 us: 1.25x slower                                                          |
| json_dumps           | 6.19 ms                                                | 7.78 ms: 1.26x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.0 ms: 1.07x slower                                                         |
| python_startup_no_site | 13.2 ms                                                | 14.7 ms: 1.11x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 8.88 ms: 1.19x slower                                                         |
| genshi_xml      | 30.5 ms                                                | 37.4 ms: 1.23x slower                                                         |
| genshi_text     | 14.7 ms                                                | 19.4 ms: 1.33x slower                                                         |
| django_template | 19.7 ms                                                | 26.9 ms: 1.37x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.28x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.6 ms: 2.37x faster                                                         |
| mdp                              | 1.49 sec                                               | 849 ms: 1.76x faster                                                          |
| async_tree_io_tg                 | 673 ms                                                 | 406 ms: 1.66x faster                                                          |
| async_tree_eager_io              | 666 ms                                                 | 405 ms: 1.65x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 424 ms: 1.58x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 413 ms: 1.49x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 214 ms: 1.48x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 174 ms: 1.46x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 185 ms: 1.43x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 221 ms: 1.40x faster                                                          |
| deepcopy                         | 226 us                                                 | 177 us: 1.27x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 424 ms: 1.25x faster                                                          |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 431 ms: 1.22x faster                                                          |
| deepcopy_memo                    | 26.0 us                                                | 23.1 us: 1.13x faster                                                         |
| k_core                           | 1.72 sec                                               | 1.54 sec: 1.12x faster                                                        |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                          |
| async_generators                 | 299 ms                                                 | 272 ms: 1.10x faster                                                          |
| dulwich_log                      | 29.2 ms                                                | 26.8 ms: 1.09x faster                                                         |
| comprehensions                   | 14.0 us                                                | 13.1 us: 1.07x faster                                                         |
| regex_effbot                     | 2.44 ms                                                | 2.30 ms: 1.06x faster                                                         |
| deepcopy_reduce                  | 2.01 us                                                | 1.90 us: 1.06x faster                                                         |
| pathlib                          | 24.7 ms                                                | 24.3 ms: 1.02x faster                                                         |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.02x faster                                                          |
| spectral_norm                    | 76.5 ms                                                | 75.6 ms: 1.01x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 370 ms: 1.01x faster                                                          |
| xml_etree_parse                  | 108 ms                                                 | 107 ms: 1.01x faster                                                          |
| raytrace                         | 204 ms                                                 | 202 ms: 1.01x faster                                                          |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| asyncio_websockets               | 243 ms                                                 | 245 ms: 1.01x slower                                                          |
| xml_etree_iterparse              | 75.5 ms                                                | 76.3 ms: 1.01x slower                                                         |
| sphinx                           | 613 ms                                                 | 620 ms: 1.01x slower                                                          |
| bpe_tokeniser                    | 3.28 sec                                               | 3.32 sec: 1.01x slower                                                        |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.18 ms: 1.01x slower                                                         |
| bench_mp_pool                    | 65.5 ms                                                | 66.3 ms: 1.01x slower                                                         |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.03x slower                                                         |
| json                             | 3.00 ms                                                | 3.09 ms: 1.03x slower                                                         |
| shortest_path                    | 331 ms                                                 | 341 ms: 1.03x slower                                                          |
| coroutines                       | 19.7 ms                                                | 20.3 ms: 1.03x slower                                                         |
| sqlalchemy_declarative           | 61.9 ms                                                | 64.4 ms: 1.04x slower                                                         |
| float                            | 54.1 ms                                                | 56.4 ms: 1.04x slower                                                         |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                                         |
| regex_v8                         | 15.1 ms                                                | 15.8 ms: 1.05x slower                                                         |
| connected_components             | 300 ms                                                 | 317 ms: 1.06x slower                                                          |
| gc_traversal                     | 2.95 ms                                                | 3.13 ms: 1.06x slower                                                         |
| python_startup                   | 17.8 ms                                                | 19.0 ms: 1.07x slower                                                         |
| logging_silent                   | 72.5 ns                                                | 78.0 ns: 1.07x slower                                                         |
| go                               | 98.5 ms                                                | 106 ms: 1.08x slower                                                          |
| generators                       | 29.4 ms                                                | 31.8 ms: 1.08x slower                                                         |
| scimark_fft                      | 194 ms                                                 | 211 ms: 1.08x slower                                                          |
| pyflate                          | 311 ms                                                 | 338 ms: 1.09x slower                                                          |
| html5lib                         | 33.4 ms                                                | 36.3 ms: 1.09x slower                                                         |
| deltablue                        | 2.57 ms                                                | 2.80 ms: 1.09x slower                                                         |
| regex_compile                    | 75.9 ms                                                | 82.8 ms: 1.09x slower                                                         |
| scimark_sor                      | 85.8 ms                                                | 93.7 ms: 1.09x slower                                                         |
| tomli_loads                      | 1.36 sec                                               | 1.48 sec: 1.09x slower                                                        |
| docutils                         | 1.45 sec                                               | 1.59 sec: 1.09x slower                                                        |
| logging_format                   | 3.90 us                                                | 4.29 us: 1.10x slower                                                         |
| meteor_contest                   | 69.1 ms                                                | 76.1 ms: 1.10x slower                                                         |
| logging_simple                   | 3.60 us                                                | 3.98 us: 1.11x slower                                                         |
| python_startup_no_site           | 13.2 ms                                                | 14.7 ms: 1.11x slower                                                         |
| pycparser                        | 673 ms                                                 | 750 ms: 1.11x slower                                                          |
| bench_thread_pool                | 483 us                                                 | 542 us: 1.12x slower                                                          |
| xml_etree_generate               | 55.4 ms                                                | 62.2 ms: 1.12x slower                                                         |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.13x slower                                                         |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.48 ms: 1.13x slower                                                         |
| async_tree_eager                 | 65.8 ms                                                | 75.2 ms: 1.14x slower                                                         |
| typing_runtime_protocols         | 91.5 us                                                | 105 us: 1.14x slower                                                          |
| scimark_lu                       | 73.5 ms                                                | 84.6 ms: 1.15x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                          |
| hexiom                           | 4.38 ms                                                | 5.12 ms: 1.17x slower                                                         |
| chaos                            | 41.6 ms                                                | 49.2 ms: 1.18x slower                                                         |
| xml_etree_process                | 38.9 ms                                                | 46.0 ms: 1.18x slower                                                         |
| many_optionals                   | 403 us                                                 | 478 us: 1.19x slower                                                          |
| pprint_pformat                   | 986 ms                                                 | 1.17 sec: 1.19x slower                                                        |
| crypto_pyaes                     | 51.4 ms                                                | 61.3 ms: 1.19x slower                                                         |
| mako                             | 7.44 ms                                                | 8.88 ms: 1.19x slower                                                         |
| pprint_safe_repr                 | 483 ms                                                 | 578 ms: 1.20x slower                                                          |
| nqueens                          | 59.5 ms                                                | 73.0 ms: 1.23x slower                                                         |
| genshi_xml                       | 30.5 ms                                                | 37.4 ms: 1.23x slower                                                         |
| scimark_monte_carlo              | 44.5 ms                                                | 54.9 ms: 1.23x slower                                                         |
| unpickle_pure_python             | 145 us                                                 | 181 us: 1.25x slower                                                          |
| telco                            | 3.92 ms                                                | 4.90 ms: 1.25x slower                                                         |
| pickle_pure_python               | 197 us                                                 | 247 us: 1.25x slower                                                          |
| json_dumps                       | 6.19 ms                                                | 7.78 ms: 1.26x slower                                                         |
| fannkuch                         | 250 ms                                                 | 315 ms: 1.26x slower                                                          |
| coverage                         | 38.5 ms                                                | 48.8 ms: 1.27x slower                                                         |
| richards                         | 30.6 ms                                                | 39.0 ms: 1.28x slower                                                         |
| nbody                            | 67.6 ms                                                | 87.0 ms: 1.29x slower                                                         |
| 2to3                             | 168 ms                                                 | 218 ms: 1.30x slower                                                          |
| richards_super                   | 34.6 ms                                                | 45.4 ms: 1.31x slower                                                         |
| genshi_text                      | 14.7 ms                                                | 19.4 ms: 1.33x slower                                                         |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 189 ms: 1.33x slower                                                          |
| django_template                  | 19.7 ms                                                | 26.9 ms: 1.37x slower                                                         |
| async_tree_eager_tg              | 46.9 ms                                                | 147 ms: 3.13x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                                  |
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250416-3.14.0a7+-a4b740d/bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.034x slower

# HPT report

- Reliability score: 99.44% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x