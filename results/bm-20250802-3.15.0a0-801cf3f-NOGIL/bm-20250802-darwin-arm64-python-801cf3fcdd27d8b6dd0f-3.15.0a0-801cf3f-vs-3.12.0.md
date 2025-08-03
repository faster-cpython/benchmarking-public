# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: darwin-arm64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.035x faster
- HPT reliability: 63.30%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 184 ms: 1.09x slower                                                  |
| docutils       | 1.45 sec                                               | 1.39 sec: 1.04x faster                                                |
| html5lib       | 33.4 ms                                                | 32.4 ms: 1.03x faster                                                 |
| sphinx         | 613 ms                                                 | 580 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 302 ms: 2.22x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 305 ms: 2.19x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 290 ms: 2.13x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 319 ms: 2.11x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 166 ms: 1.91x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 135 ms: 1.89x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 153 ms: 1.72x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 184 ms: 1.69x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 379 ms: 1.39x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 397 ms: 1.33x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.21x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.8 ms: 1.17x faster                                                 |
| async_generators                 | 299 ms                                                 | 284 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 360 ms: 1.04x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 148 ms: 1.05x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 73.8 ms: 1.12x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 115 ms: 2.44x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 46.9 ms: 1.15x faster                                                 |
| pidigits       | 283 ms                                                 | 277 ms: 1.02x faster                                                  |
| nbody          | 67.6 ms                                                | 87.0 ms: 1.29x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.23 ms: 1.09x faster                                                 |
| regex_dna      | 143 ms                                                 | 137 ms: 1.04x faster                                                  |
| regex_v8       | 15.1 ms                                                | 14.8 ms: 1.02x faster                                                 |
| regex_compile  | 75.9 ms                                                | 78.0 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 63.3 ms: 1.19x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 95.8 ms: 1.13x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 56.9 ms: 1.03x slower                                                 |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 41.4 ms: 1.06x slower                                                 |
| json_dumps           | 6.19 ms                                                | 6.80 ms: 1.10x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.52 sec: 1.12x slower                                                |
| unpickle_pure_python | 145 us                                                 | 163 us: 1.12x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 222 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.0 ms: 1.07x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 14.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 36.2 ms: 1.19x slower                                                 |
| genshi_text     | 14.7 ms                                                | 17.5 ms: 1.19x slower                                                 |
| django_template | 19.7 ms                                                | 23.9 ms: 1.21x slower                                                 |
| mako            | 7.44 ms                                                | 10.4 ms: 1.40x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.25x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.95 ms                                                | 1.30 ms: 2.27x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 302 ms: 2.22x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 305 ms: 2.19x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 290 ms: 2.13x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 319 ms: 2.11x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 166 ms: 1.91x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 135 ms: 1.89x faster                                                  |
| mdp                              | 1.49 sec                                               | 835 ms: 1.79x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 153 ms: 1.72x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 184 ms: 1.69x faster                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 782 us: 1.47x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 379 ms: 1.39x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 397 ms: 1.33x faster                                                  |
| deepcopy                         | 226 us                                                 | 182 us: 1.24x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.21x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 63.3 ms: 1.19x faster                                                 |
| subparsers                       | 32.1 ms                                                | 27.2 ms: 1.18x faster                                                 |
| generators                       | 29.4 ms                                                | 25.0 ms: 1.17x faster                                                 |
| coroutines                       | 19.7 ms                                                | 16.8 ms: 1.17x faster                                                 |
| float                            | 54.1 ms                                                | 46.9 ms: 1.15x faster                                                 |
| deepcopy_memo                    | 26.0 us                                                | 22.6 us: 1.15x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 25.8 ms: 1.13x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.37 us: 1.13x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 95.8 ms: 1.13x faster                                                 |
| comprehensions                   | 14.0 us                                                | 12.6 us: 1.11x faster                                                 |
| go                               | 98.5 ms                                                | 89.3 ms: 1.10x faster                                                 |
| pylint                           | 182 ms                                                 | 166 ms: 1.10x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.23 ms: 1.09x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.60 sec: 1.08x faster                                                |
| pathlib                          | 24.7 ms                                                | 23.0 ms: 1.08x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.05 sec: 1.07x faster                                                |
| raytrace                         | 204 ms                                                 | 191 ms: 1.07x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.90 us: 1.06x faster                                                 |
| sphinx                           | 613 ms                                                 | 580 ms: 1.06x faster                                                  |
| async_generators                 | 299 ms                                                 | 284 ms: 1.05x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 72.8 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.39 sec: 1.04x faster                                                |
| regex_dna                        | 143 ms                                                 | 137 ms: 1.04x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.48 ms: 1.03x faster                                                 |
| html5lib                         | 33.4 ms                                                | 32.4 ms: 1.03x faster                                                 |
| regex_v8                         | 15.1 ms                                                | 14.8 ms: 1.02x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                  |
| pidigits                         | 283 ms                                                 | 277 ms: 1.02x faster                                                  |
| pyflate                          | 311 ms                                                 | 307 ms: 1.01x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 87.3 ms: 1.02x slower                                                 |
| logging_simple                   | 3.60 us                                                | 3.70 us: 1.03x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 56.9 ms: 1.03x slower                                                 |
| regex_compile                    | 75.9 ms                                                | 78.0 ms: 1.03x slower                                                 |
| pycparser                        | 673 ms                                                 | 694 ms: 1.03x slower                                                  |
| dask                             | 779 ms                                                 | 807 ms: 1.04x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 360 ms: 1.04x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 202 ms: 1.04x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                 |
| logging_silent                   | 72.5 ns                                                | 75.7 ns: 1.04x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 148 ms: 1.05x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                 |
| logging_format                   | 3.90 us                                                | 4.11 us: 1.05x slower                                                 |
| shortest_path                    | 331 ms                                                 | 351 ms: 1.06x slower                                                  |
| thrift                           | 468 us                                                 | 497 us: 1.06x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 41.4 ms: 1.06x slower                                                 |
| python_startup                   | 17.8 ms                                                | 19.0 ms: 1.07x slower                                                 |
| connected_components             | 300 ms                                                 | 323 ms: 1.08x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 82.4 ms: 1.08x slower                                                 |
| nqueens                          | 59.5 ms                                                | 64.6 ms: 1.08x slower                                                 |
| sympy_str                        | 144 ms                                                 | 157 ms: 1.09x slower                                                  |
| 2to3                             | 168 ms                                                 | 184 ms: 1.09x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 6.80 ms: 1.10x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 14.5 ms: 1.10x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 49.2 ms: 1.11x slower                                                 |
| hexiom                           | 4.38 ms                                                | 4.85 ms: 1.11x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.52 sec: 1.12x slower                                                |
| async_tree_eager                 | 65.8 ms                                                | 73.8 ms: 1.12x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 163 us: 1.12x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 222 us: 1.13x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 58.3 ms: 1.13x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 74.3 ms: 1.13x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.57 ms: 1.13x slower                                                 |
| fannkuch                         | 250 ms                                                 | 287 ms: 1.15x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 84.4 ms: 1.15x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 273 ms: 1.17x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 80.8 ms: 1.17x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 36.2 ms: 1.19x slower                                                 |
| pprint_pformat                   | 986 ms                                                 | 1.17 sec: 1.19x slower                                                |
| richards_super                   | 34.6 ms                                                | 41.2 ms: 1.19x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 17.5 ms: 1.19x slower                                                 |
| richards                         | 30.6 ms                                                | 36.5 ms: 1.19x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 578 ms: 1.20x slower                                                  |
| django_template                  | 19.7 ms                                                | 23.9 ms: 1.21x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 113 us: 1.24x slower                                                  |
| telco                            | 3.92 ms                                                | 4.96 ms: 1.27x slower                                                 |
| nbody                            | 67.6 ms                                                | 87.0 ms: 1.29x slower                                                 |
| mako                             | 7.44 ms                                                | 10.4 ms: 1.40x slower                                                 |
| many_optionals                   | 403 us                                                 | 606 us: 1.50x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 756 us: 1.57x slower                                                  |
| coverage                         | 38.5 ms                                                | 61.7 ms: 1.60x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 115 ms: 2.44x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (2): chaos, json
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 63.30% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.27x