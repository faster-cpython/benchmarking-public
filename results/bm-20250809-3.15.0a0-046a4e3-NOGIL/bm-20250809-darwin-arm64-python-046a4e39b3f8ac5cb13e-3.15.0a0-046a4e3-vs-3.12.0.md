# Results vs. 3.12.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: darwin-arm64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.031x faster
- HPT reliability: 64.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 181 ms: 1.07x slower                                                  |
| docutils       | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                |
| html5lib       | 33.4 ms                                                | 32.8 ms: 1.02x faster                                                 |
| sphinx         | 613 ms                                                 | 581 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 303 ms: 2.22x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 305 ms: 2.19x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 290 ms: 2.13x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 319 ms: 2.10x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 166 ms: 1.92x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 135 ms: 1.89x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 153 ms: 1.72x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 184 ms: 1.68x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 378 ms: 1.40x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 397 ms: 1.33x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.22x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.7 ms: 1.18x faster                                                 |
| async_generators                 | 299 ms                                                 | 282 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 359 ms: 1.03x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 148 ms: 1.05x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 74.0 ms: 1.12x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 115 ms: 2.45x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 47.7 ms: 1.13x faster                                                 |
| pidigits       | 283 ms                                                 | 277 ms: 1.02x faster                                                  |
| nbody          | 67.6 ms                                                | 87.7 ms: 1.30x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.23 ms: 1.09x faster                                                 |
| regex_dna      | 143 ms                                                 | 137 ms: 1.04x faster                                                  |
| regex_v8       | 15.1 ms                                                | 14.7 ms: 1.03x faster                                                 |
| regex_compile  | 75.9 ms                                                | 78.3 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 63.2 ms: 1.20x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 95.6 ms: 1.13x faster                                                 |
| json_dumps           | 6.19 ms                                                | 6.04 ms: 1.02x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 57.1 ms: 1.03x slower                                                 |
| json_loads           | 17.0 us                                                | 18.0 us: 1.06x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 41.5 ms: 1.07x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 164 us: 1.12x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.54 sec: 1.14x slower                                                |
| pickle_pure_python   | 197 us                                                 | 226 us: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.4 ms: 1.09x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 14.7 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 36.5 ms: 1.20x slower                                                 |
| genshi_text     | 14.7 ms                                                | 17.6 ms: 1.20x slower                                                 |
| django_template | 19.7 ms                                                | 23.9 ms: 1.22x slower                                                 |
| mako            | 7.44 ms                                                | 10.6 ms: 1.42x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.25x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.95 ms                                                | 1.30 ms: 2.26x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 303 ms: 2.22x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 305 ms: 2.19x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 290 ms: 2.13x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 319 ms: 2.10x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 166 ms: 1.92x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 135 ms: 1.89x faster                                                  |
| mdp                              | 1.49 sec                                               | 848 ms: 1.76x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 153 ms: 1.72x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 184 ms: 1.68x faster                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 775 us: 1.48x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 378 ms: 1.40x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 397 ms: 1.33x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.22x faster                                                  |
| deepcopy                         | 226 us                                                 | 186 us: 1.22x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 63.2 ms: 1.20x faster                                                 |
| subparsers                       | 32.1 ms                                                | 27.0 ms: 1.19x faster                                                 |
| coroutines                       | 19.7 ms                                                | 16.7 ms: 1.18x faster                                                 |
| generators                       | 29.4 ms                                                | 25.2 ms: 1.17x faster                                                 |
| float                            | 54.1 ms                                                | 47.7 ms: 1.13x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 95.6 ms: 1.13x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 26.0 ms: 1.13x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.37 us: 1.13x faster                                                 |
| deepcopy_memo                    | 26.0 us                                                | 23.2 us: 1.12x faster                                                 |
| comprehensions                   | 14.0 us                                                | 12.6 us: 1.11x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.23 ms: 1.09x faster                                                 |
| pylint                           | 182 ms                                                 | 167 ms: 1.09x faster                                                  |
| go                               | 98.5 ms                                                | 91.4 ms: 1.08x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.61 sec: 1.07x faster                                                |
| raytrace                         | 204 ms                                                 | 191 ms: 1.07x faster                                                  |
| async_generators                 | 299 ms                                                 | 282 ms: 1.06x faster                                                  |
| sphinx                           | 613 ms                                                 | 581 ms: 1.06x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.12 sec: 1.05x faster                                                |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 73.2 ms: 1.04x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.93 us: 1.04x faster                                                 |
| regex_dna                        | 143 ms                                                 | 137 ms: 1.04x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                |
| pycparser                        | 673 ms                                                 | 653 ms: 1.03x faster                                                  |
| regex_v8                         | 15.1 ms                                                | 14.7 ms: 1.03x faster                                                 |
| json_dumps                       | 6.19 ms                                                | 6.04 ms: 1.02x faster                                                 |
| pathlib                          | 24.7 ms                                                | 24.2 ms: 1.02x faster                                                 |
| pidigits                         | 283 ms                                                 | 277 ms: 1.02x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.52 ms: 1.02x faster                                                 |
| html5lib                         | 33.4 ms                                                | 32.8 ms: 1.02x faster                                                 |
| json                             | 3.00 ms                                                | 3.04 ms: 1.01x slower                                                 |
| chaos                            | 41.6 ms                                                | 42.3 ms: 1.02x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 57.1 ms: 1.03x slower                                                 |
| regex_compile                    | 75.9 ms                                                | 78.3 ms: 1.03x slower                                                 |
| dask                             | 779 ms                                                 | 804 ms: 1.03x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 359 ms: 1.03x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 75.5 ns: 1.04x slower                                                 |
| logging_simple                   | 3.60 us                                                | 3.76 us: 1.04x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 148 ms: 1.05x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 205 ms: 1.05x slower                                                  |
| thrift                           | 468 us                                                 | 493 us: 1.05x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.06x slower                                                 |
| logging_format                   | 3.90 us                                                | 4.15 us: 1.06x slower                                                 |
| scimark_sor                      | 85.8 ms                                                | 91.5 ms: 1.07x slower                                                 |
| xml_etree_process                | 38.9 ms                                                | 41.5 ms: 1.07x slower                                                 |
| shortest_path                    | 331 ms                                                 | 353 ms: 1.07x slower                                                  |
| 2to3                             | 168 ms                                                 | 181 ms: 1.07x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 83.0 ms: 1.09x slower                                                 |
| python_startup                   | 17.8 ms                                                | 19.4 ms: 1.09x slower                                                 |
| connected_components             | 300 ms                                                 | 328 ms: 1.10x slower                                                  |
| sympy_str                        | 144 ms                                                 | 159 ms: 1.10x slower                                                  |
| nqueens                          | 59.5 ms                                                | 65.9 ms: 1.11x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 14.7 ms: 1.11x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 49.8 ms: 1.12x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 74.0 ms: 1.12x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 164 us: 1.12x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 58.4 ms: 1.14x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.54 sec: 1.14x slower                                                |
| hexiom                           | 4.38 ms                                                | 5.01 ms: 1.15x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 226 us: 1.15x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 269 ms: 1.15x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.14 sec: 1.15x slower                                                |
| scimark_lu                       | 73.5 ms                                                | 84.8 ms: 1.15x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 558 ms: 1.16x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.64 ms: 1.16x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 76.0 ms: 1.16x slower                                                 |
| fannkuch                         | 250 ms                                                 | 294 ms: 1.18x slower                                                  |
| richards_super                   | 34.6 ms                                                | 41.1 ms: 1.19x slower                                                 |
| richards                         | 30.6 ms                                                | 36.4 ms: 1.19x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 36.5 ms: 1.20x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 17.6 ms: 1.20x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 83.5 ms: 1.21x slower                                                 |
| django_template                  | 19.7 ms                                                | 23.9 ms: 1.22x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 113 us: 1.23x slower                                                  |
| telco                            | 3.92 ms                                                | 5.04 ms: 1.29x slower                                                 |
| nbody                            | 67.6 ms                                                | 87.7 ms: 1.30x slower                                                 |
| mako                             | 7.44 ms                                                | 10.6 ms: 1.42x slower                                                 |
| many_optionals                   | 403 us                                                 | 599 us: 1.49x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 753 us: 1.56x slower                                                  |
| coverage                         | 38.5 ms                                                | 62.6 ms: 1.63x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 115 ms: 2.45x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): pyflate
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 64.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.27x