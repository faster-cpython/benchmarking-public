# Results vs. base

- fork: python
- ref: v3.14.0a5
- machine: darwin-arm64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.054x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 164 ms                                                                 | 176 ms: 1.07x slower                                       |
| docutils       | 1.45 sec                                                               | 1.51 sec: 1.04x slower                                     |
| html5lib       | 29.5 ms                                                                | 33.1 ms: 1.12x slower                                      |
| sphinx         | 568 ms                                                                 | 598 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                                  | 1.07x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed    | 363 ms                                                                 | 369 ms: 1.02x slower                                       |
| async_tree_eager_cpu_io_mixed_tg | 393 ms                                                                 | 401 ms: 1.02x slower                                       |
| async_tree_cpu_io_mixed          | 416 ms                                                                 | 426 ms: 1.02x slower                                       |
| async_tree_cpu_io_mixed_tg       | 417 ms                                                                 | 429 ms: 1.03x slower                                       |
| async_generators                 | 273 ms                                                                 | 283 ms: 1.04x slower                                       |
| async_tree_eager_memoization     | 145 ms                                                                 | 151 ms: 1.04x slower                                       |
| async_tree_memoization_tg        | 197 ms                                                                 | 208 ms: 1.06x slower                                       |
| async_tree_eager                 | 65.9 ms                                                                | 69.9 ms: 1.06x slower                                      |
| async_tree_eager_io_tg           | 373 ms                                                                 | 397 ms: 1.07x slower                                       |
| async_tree_none                  | 162 ms                                                                 | 173 ms: 1.07x slower                                       |
| async_tree_eager_memoization_tg  | 175 ms                                                                 | 187 ms: 1.07x slower                                       |
| async_tree_eager_tg              | 131 ms                                                                 | 141 ms: 1.07x slower                                       |
| async_tree_memoization           | 197 ms                                                                 | 211 ms: 1.07x slower                                       |
| async_tree_io_tg                 | 364 ms                                                                 | 391 ms: 1.07x slower                                       |
| async_tree_none_tg               | 155 ms                                                                 | 167 ms: 1.08x slower                                       |
| async_tree_eager_io              | 364 ms                                                                 | 394 ms: 1.08x slower                                       |
| async_tree_io                    | 372 ms                                                                 | 407 ms: 1.09x slower                                       |
| coroutines                       | 15.8 ms                                                                | 17.9 ms: 1.13x slower                                      |
| Geometric mean                   | (ref)                                                                  | 1.06x slower                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 65.6 ms                                                                | 65.0 ms: 1.01x faster                                      |
| pidigits       | 283 ms                                                                 | 284 ms: 1.00x slower                                       |
| float          | 46.9 ms                                                                | 52.6 ms: 1.12x slower                                      |
| Geometric mean | (ref)                                                                  | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.24 ms                                                                | 2.24 ms: 1.00x slower                                      |
| regex_v8       | 16.7 ms                                                                | 16.9 ms: 1.01x slower                                      |
| regex_compile  | 67.9 ms                                                                | 73.5 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| json_loads           | 17.8 us                                                                | 17.9 us: 1.00x slower                                      |
| xml_etree_iterparse  | 69.6 ms                                                                | 70.7 ms: 1.02x slower                                      |
| xml_etree_generate   | 49.9 ms                                                                | 50.6 ms: 1.02x slower                                      |
| xml_etree_parse      | 98.6 ms                                                                | 101 ms: 1.03x slower                                       |
| unpickle_pure_python | 130 us                                                                 | 134 us: 1.03x slower                                       |
| json_dumps           | 7.30 ms                                                                | 7.53 ms: 1.03x slower                                      |
| xml_etree_process    | 35.5 ms                                                                | 36.7 ms: 1.03x slower                                      |
| tomli_loads          | 1.21 sec                                                               | 1.29 sec: 1.06x slower                                     |
| pickle_pure_python   | 194 us                                                                 | 210 us: 1.08x slower                                       |
| Geometric mean       | (ref)                                                                  | 1.03x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 14.3 ms                                                                | 12.8 ms: 1.12x faster                                      |
| python_startup         | 19.2 ms                                                                | 17.5 ms: 1.10x faster                                      |
| Geometric mean         | (ref)                                                                  | 1.11x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 6.46 ms                                                                | 6.49 ms: 1.00x slower                                      |
| django_template | 21.0 ms                                                                | 23.9 ms: 1.14x slower                                      |
| genshi_xml      | 29.3 ms                                                                | 33.3 ms: 1.14x slower                                      |
| genshi_text     | 13.6 ms                                                                | 15.8 ms: 1.16x slower                                      |
| Geometric mean  | (ref)                                                                  | 1.11x slower                                               |

All benchmarks:
===============

| Benchmark                        | bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site           | 14.3 ms                                                                | 12.8 ms: 1.12x faster                                      |
| python_startup                   | 19.2 ms                                                                | 17.5 ms: 1.10x faster                                      |
| telco                            | 4.57 ms                                                                | 4.49 ms: 1.02x faster                                      |
| scimark_sparse_mat_mult          | 2.90 ms                                                                | 2.87 ms: 1.01x faster                                      |
| nbody                            | 65.6 ms                                                                | 65.0 ms: 1.01x faster                                      |
| scimark_fft                      | 173 ms                                                                 | 172 ms: 1.01x faster                                       |
| regex_effbot                     | 2.24 ms                                                                | 2.24 ms: 1.00x slower                                      |
| pidigits                         | 283 ms                                                                 | 284 ms: 1.00x slower                                       |
| shortest_path                    | 328 ms                                                                 | 329 ms: 1.00x slower                                       |
| create_gc_cycles                 | 1.28 ms                                                                | 1.28 ms: 1.00x slower                                      |
| bpe_tokeniser                    | 2.87 sec                                                               | 2.88 sec: 1.00x slower                                     |
| mako                             | 6.46 ms                                                                | 6.49 ms: 1.00x slower                                      |
| json_loads                       | 17.8 us                                                                | 17.9 us: 1.00x slower                                      |
| json                             | 2.98 ms                                                                | 3.01 ms: 1.01x slower                                      |
| regex_v8                         | 16.7 ms                                                                | 16.9 ms: 1.01x slower                                      |
| sqlite_synth                     | 1.53 us                                                                | 1.55 us: 1.01x slower                                      |
| xml_etree_iterparse              | 69.6 ms                                                                | 70.7 ms: 1.02x slower                                      |
| xml_etree_generate               | 49.9 ms                                                                | 50.6 ms: 1.02x slower                                      |
| async_tree_eager_cpu_io_mixed    | 363 ms                                                                 | 369 ms: 1.02x slower                                       |
| async_tree_eager_cpu_io_mixed_tg | 393 ms                                                                 | 401 ms: 1.02x slower                                       |
| bench_mp_pool                    | 58.9 ms                                                                | 60.3 ms: 1.02x slower                                      |
| crypto_pyaes                     | 52.7 ms                                                                | 53.9 ms: 1.02x slower                                      |
| async_tree_cpu_io_mixed          | 416 ms                                                                 | 426 ms: 1.02x slower                                       |
| xml_etree_parse                  | 98.6 ms                                                                | 101 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed_tg       | 417 ms                                                                 | 429 ms: 1.03x slower                                       |
| pprint_pformat                   | 1.03 sec                                                               | 1.06 sec: 1.03x slower                                     |
| mdp                              | 1.53 sec                                                               | 1.58 sec: 1.03x slower                                     |
| unpickle_pure_python             | 130 us                                                                 | 134 us: 1.03x slower                                       |
| coverage                         | 46.1 ms                                                                | 47.5 ms: 1.03x slower                                      |
| json_dumps                       | 7.30 ms                                                                | 7.53 ms: 1.03x slower                                      |
| xml_etree_process                | 35.5 ms                                                                | 36.7 ms: 1.03x slower                                      |
| async_generators                 | 273 ms                                                                 | 283 ms: 1.04x slower                                       |
| nqueens                          | 61.6 ms                                                                | 64.0 ms: 1.04x slower                                      |
| bench_thread_pool                | 497 us                                                                 | 518 us: 1.04x slower                                       |
| docutils                         | 1.45 sec                                                               | 1.51 sec: 1.04x slower                                     |
| async_tree_eager_memoization     | 145 ms                                                                 | 151 ms: 1.04x slower                                       |
| subparsers                       | 12.0 ms                                                                | 12.5 ms: 1.04x slower                                      |
| sqlalchemy_declarative           | 58.9 ms                                                                | 61.7 ms: 1.05x slower                                      |
| sympy_sum                        | 74.7 ms                                                                | 78.4 ms: 1.05x slower                                      |
| pycparser                        | 677 ms                                                                 | 713 ms: 1.05x slower                                       |
| sphinx                           | 568 ms                                                                 | 598 ms: 1.05x slower                                       |
| many_optionals                   | 446 us                                                                 | 470 us: 1.05x slower                                       |
| comprehensions                   | 12.3 us                                                                | 13.0 us: 1.06x slower                                      |
| pylint                           | 161 ms                                                                 | 170 ms: 1.06x slower                                       |
| dulwich_log                      | 27.9 ms                                                                | 29.6 ms: 1.06x slower                                      |
| async_tree_memoization_tg        | 197 ms                                                                 | 208 ms: 1.06x slower                                       |
| async_tree_eager                 | 65.9 ms                                                                | 69.9 ms: 1.06x slower                                      |
| tomli_loads                      | 1.21 sec                                                               | 1.29 sec: 1.06x slower                                     |
| hexiom                           | 4.67 ms                                                                | 4.97 ms: 1.06x slower                                      |
| thrift                           | 434 us                                                                 | 461 us: 1.06x slower                                       |
| sympy_integrate                  | 11.4 ms                                                                | 12.1 ms: 1.06x slower                                      |
| async_tree_eager_io_tg           | 373 ms                                                                 | 397 ms: 1.07x slower                                       |
| typing_runtime_protocols         | 95.3 us                                                                | 102 us: 1.07x slower                                       |
| async_tree_none                  | 162 ms                                                                 | 173 ms: 1.07x slower                                       |
| pyflate                          | 284 ms                                                                 | 303 ms: 1.07x slower                                       |
| sqlglot_transpile                | 997 us                                                                 | 1.06 ms: 1.07x slower                                      |
| sympy_expand                     | 239 ms                                                                 | 256 ms: 1.07x slower                                       |
| async_tree_eager_memoization_tg  | 175 ms                                                                 | 187 ms: 1.07x slower                                       |
| sympy_str                        | 141 ms                                                                 | 151 ms: 1.07x slower                                       |
| async_tree_eager_tg              | 131 ms                                                                 | 141 ms: 1.07x slower                                       |
| sqlglot_optimize                 | 33.2 ms                                                                | 35.6 ms: 1.07x slower                                      |
| sqlglot_parse                    | 828 us                                                                 | 887 us: 1.07x slower                                       |
| sqlalchemy_imperative            | 6.63 ms                                                                | 7.10 ms: 1.07x slower                                      |
| async_tree_memoization           | 197 ms                                                                 | 211 ms: 1.07x slower                                       |
| 2to3                             | 164 ms                                                                 | 176 ms: 1.07x slower                                       |
| async_tree_io_tg                 | 364 ms                                                                 | 391 ms: 1.07x slower                                       |
| async_tree_none_tg               | 155 ms                                                                 | 167 ms: 1.08x slower                                       |
| pickle_pure_python               | 194 us                                                                 | 210 us: 1.08x slower                                       |
| sqlglot_normalize                | 182 ms                                                                 | 196 ms: 1.08x slower                                       |
| async_tree_eager_io              | 364 ms                                                                 | 394 ms: 1.08x slower                                       |
| regex_compile                    | 67.9 ms                                                                | 73.5 ms: 1.08x slower                                      |
| spectral_norm                    | 61.3 ms                                                                | 66.9 ms: 1.09x slower                                      |
| async_tree_io                    | 372 ms                                                                 | 407 ms: 1.09x slower                                       |
| deepcopy_reduce                  | 1.58 us                                                                | 1.77 us: 1.12x slower                                      |
| chaos                            | 39.2 ms                                                                | 43.8 ms: 1.12x slower                                      |
| deepcopy                         | 150 us                                                                 | 168 us: 1.12x slower                                       |
| html5lib                         | 29.5 ms                                                                | 33.1 ms: 1.12x slower                                      |
| logging_silent                   | 67.4 ns                                                                | 75.6 ns: 1.12x slower                                      |
| float                            | 46.9 ms                                                                | 52.6 ms: 1.12x slower                                      |
| scimark_lu                       | 73.5 ms                                                                | 83.0 ms: 1.13x slower                                      |
| coroutines                       | 15.8 ms                                                                | 17.9 ms: 1.13x slower                                      |
| logging_format                   | 3.44 us                                                                | 3.91 us: 1.14x slower                                      |
| django_template                  | 21.0 ms                                                                | 23.9 ms: 1.14x slower                                      |
| genshi_xml                       | 29.3 ms                                                                | 33.3 ms: 1.14x slower                                      |
| logging_simple                   | 3.13 us                                                                | 3.60 us: 1.15x slower                                      |
| genshi_text                      | 13.6 ms                                                                | 15.8 ms: 1.16x slower                                      |
| raytrace                         | 171 ms                                                                 | 199 ms: 1.16x slower                                       |
| deepcopy_memo                    | 18.3 us                                                                | 21.2 us: 1.16x slower                                      |
| scimark_monte_carlo              | 42.5 ms                                                                | 49.4 ms: 1.16x slower                                      |
| go                               | 80.5 ms                                                                | 94.2 ms: 1.17x slower                                      |
| deltablue                        | 2.35 ms                                                                | 2.77 ms: 1.18x slower                                      |
| scimark_sor                      | 77.7 ms                                                                | 92.3 ms: 1.19x slower                                      |
| richards_super                   | 35.1 ms                                                                | 41.7 ms: 1.19x slower                                      |
| richards                         | 31.4 ms                                                                | 37.7 ms: 1.20x slower                                      |
| generators                       | 22.9 ms                                                                | 28.5 ms: 1.24x slower                                      |
| Geometric mean                   | (ref)                                                                  | 1.06x slower                                               |

Benchmark hidden because not significant (10): gc_traversal, meteor_contest, pprint_safe_repr, regex_dna, dask, asyncio_websockets, fannkuch, connected_components, k_core, pathlib

- Geometric mean (including insignificant results): 1.054x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 0.99x