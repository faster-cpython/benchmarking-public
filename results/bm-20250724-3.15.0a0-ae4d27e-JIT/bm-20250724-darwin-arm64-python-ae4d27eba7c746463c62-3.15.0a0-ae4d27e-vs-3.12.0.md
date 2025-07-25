# Results vs. 3.12.0

- fork: python
- ref: ae4d27eba7c746463c62
- machine: darwin-arm64
- commit hash: ae4d27e
- commit date: 2025-07-24
- overall geometric mean: 1.063x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 171 ms: 1.01x slower                                                  |
| docutils       | 1.45 sec                                               | 1.45 sec: 1.00x faster                                                |
| sphinx         | 613 ms                                                 | 575 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 366 ms: 1.84x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 364 ms: 1.83x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 379 ms: 1.77x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 372 ms: 1.66x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 158 ms: 1.61x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 166 ms: 1.59x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.58x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.20x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                 |
| async_generators                 | 299 ms                                                 | 283 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 64.7 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.21x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.78x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 51.3 ms: 1.05x faster                                                 |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 67.6 ms                                                | 71.7 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.14 ms: 1.14x faster                                                 |
| regex_compile  | 75.9 ms                                                | 72.8 ms: 1.04x faster                                                 |
| regex_dna      | 143 ms                                                 | 138 ms: 1.04x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.2 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 145 us                                                 | 128 us: 1.14x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 34.7 ms: 1.12x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 49.6 ms: 1.12x faster                                                 |
| tomli_loads          | 1.36 sec                                               | 1.22 sec: 1.11x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 98.1 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 70.9 ms: 1.06x faster                                                 |
| json_loads           | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| pickle_pure_python   | 197 us                                                 | 207 us: 1.05x slower                                                  |
| json_dumps           | 6.19 ms                                                | 6.63 ms: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 17.3 ms: 1.03x faster                                                 |
| python_startup_no_site | 13.2 ms                                                | 12.8 ms: 1.03x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.48 ms: 1.15x faster                                                 |
| genshi_text     | 14.7 ms                                                | 15.4 ms: 1.05x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 33.1 ms: 1.08x slower                                                 |
| django_template | 19.7 ms                                                | 23.1 ms: 1.17x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.49 sec                                               | 771 ms: 1.93x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 366 ms: 1.84x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 364 ms: 1.83x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 379 ms: 1.77x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 372 ms: 1.66x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 158 ms: 1.61x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 166 ms: 1.59x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.58x faster                                                  |
| deepcopy                         | 226 us                                                 | 174 us: 1.30x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| subparsers                       | 32.1 ms                                                | 25.4 ms: 1.27x faster                                                 |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                                  |
| comprehensions                   | 14.0 us                                                | 11.3 us: 1.24x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.20x faster                                                  |
| generators                       | 29.4 ms                                                | 24.6 ms: 1.20x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 64.3 ms: 1.19x faster                                                 |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                 |
| deepcopy_memo                    | 26.0 us                                                | 22.0 us: 1.18x faster                                                 |
| raytrace                         | 204 ms                                                 | 176 ms: 1.16x faster                                                  |
| mako                             | 7.44 ms                                                | 6.48 ms: 1.15x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 25.5 ms: 1.14x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.14 ms: 1.14x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 128 us: 1.14x faster                                                  |
| pylint                           | 182 ms                                                 | 161 ms: 1.13x faster                                                  |
| xml_etree_process                | 38.9 ms                                                | 34.7 ms: 1.12x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 2.93 sec: 1.12x faster                                                |
| deepcopy_reduce                  | 2.01 us                                                | 1.80 us: 1.12x faster                                                 |
| xml_etree_generate               | 55.4 ms                                                | 49.6 ms: 1.12x faster                                                 |
| go                               | 98.5 ms                                                | 88.2 ms: 1.12x faster                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.22 sec: 1.11x faster                                                |
| xml_etree_parse                  | 108 ms                                                 | 98.1 ms: 1.10x faster                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 444 ms: 1.09x faster                                                  |
| pyflate                          | 311 ms                                                 | 287 ms: 1.08x faster                                                  |
| pprint_pformat                   | 986 ms                                                 | 916 ms: 1.08x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.60 sec: 1.07x faster                                                |
| sphinx                           | 613 ms                                                 | 575 ms: 1.07x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 70.9 ms: 1.06x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.67 us: 1.06x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.39 us: 1.06x faster                                                 |
| pathlib                          | 24.7 ms                                                | 23.4 ms: 1.06x faster                                                 |
| async_generators                 | 299 ms                                                 | 283 ms: 1.06x faster                                                  |
| float                            | 54.1 ms                                                | 51.3 ms: 1.05x faster                                                 |
| chaos                            | 41.6 ms                                                | 39.6 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 72.8 ms: 1.04x faster                                                 |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.04x faster                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 49.7 ms: 1.03x faster                                                 |
| thrift                           | 468 us                                                 | 455 us: 1.03x faster                                                  |
| python_startup                   | 17.8 ms                                                | 17.3 ms: 1.03x faster                                                 |
| python_startup_no_site           | 13.2 ms                                                | 12.8 ms: 1.03x faster                                                 |
| deltablue                        | 2.57 ms                                                | 2.51 ms: 1.02x faster                                                 |
| sympy_integrate                  | 11.1 ms                                                | 10.9 ms: 1.02x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 64.7 ms: 1.02x faster                                                 |
| scimark_fft                      | 194 ms                                                 | 191 ms: 1.02x faster                                                  |
| fannkuch                         | 250 ms                                                 | 248 ms: 1.01x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.45 sec: 1.00x faster                                                |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 77.0 ms: 1.01x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 15.2 ms: 1.01x slower                                                 |
| 2to3                             | 168 ms                                                 | 171 ms: 1.01x slower                                                  |
| sympy_str                        | 144 ms                                                 | 146 ms: 1.02x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.57 us: 1.02x slower                                                 |
| logging_silent                   | 72.5 ns                                                | 73.9 ns: 1.02x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| pycparser                        | 673 ms                                                 | 688 ms: 1.02x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 45.9 ms: 1.03x slower                                                 |
| dask                             | 779 ms                                                 | 804 ms: 1.03x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 76.1 ms: 1.04x slower                                                 |
| nqueens                          | 59.5 ms                                                | 62.0 ms: 1.04x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 15.4 ms: 1.05x slower                                                 |
| hexiom                           | 4.38 ms                                                | 4.61 ms: 1.05x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 207 us: 1.05x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 97.1 us: 1.06x slower                                                 |
| nbody                            | 67.6 ms                                                | 71.7 ms: 1.06x slower                                                 |
| shortest_path                    | 331 ms                                                 | 351 ms: 1.06x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 248 ms: 1.06x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 6.63 ms: 1.07x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 74.1 ms: 1.07x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.37 ms: 1.07x slower                                                 |
| connected_components             | 300 ms                                                 | 323 ms: 1.08x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                                 |
| richards_super                   | 34.6 ms                                                | 37.5 ms: 1.08x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 33.1 ms: 1.08x slower                                                 |
| richards                         | 30.6 ms                                                | 33.7 ms: 1.10x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                                  |
| telco                            | 3.92 ms                                                | 4.48 ms: 1.14x slower                                                 |
| django_template                  | 19.7 ms                                                | 23.1 ms: 1.17x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.21x slower                                                  |
| coverage                         | 38.5 ms                                                | 47.5 ms: 1.23x slower                                                 |
| many_optionals                   | 403 us                                                 | 592 us: 1.47x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.78x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (4): asyncio_websockets, scimark_sor, html5lib, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250724-3.15.0a0-ae4d27e-JIT/bm-20250724-darwin-arm64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.14x