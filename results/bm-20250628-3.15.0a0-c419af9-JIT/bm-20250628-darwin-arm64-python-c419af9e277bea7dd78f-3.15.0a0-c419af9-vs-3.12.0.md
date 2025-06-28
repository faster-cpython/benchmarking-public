# Results vs. 3.12.0

- fork: python
- ref: c419af9e277bea7dd78f
- machine: darwin-arm64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.060x faster
- HPT reliability: 95.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 172 ms: 1.02x slower                                                  |
| html5lib       | 33.4 ms                                                | 31.5 ms: 1.06x faster                                                 |
| sphinx         | 613 ms                                                 | 584 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 360 ms: 1.85x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 374 ms: 1.79x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 377 ms: 1.78x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 371 ms: 1.66x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.64x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 163 ms: 1.62x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 194 ms: 1.60x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                                 |
| async_generators                 | 299 ms                                                 | 280 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 358 ms: 1.04x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 64.3 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.18x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 128 ms: 2.74x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.9 ms: 1.08x faster                                                 |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                  |
| nbody          | 67.6 ms                                                | 75.4 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 71.1 ms: 1.07x faster                                                 |
| regex_effbot   | 2.44 ms                                                | 2.37 ms: 1.03x faster                                                 |
| regex_dna      | 143 ms                                                 | 143 ms: 1.00x slower                                                  |
| regex_v8       | 15.1 ms                                                | 16.2 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.23 sec: 1.10x faster                                                |
| xml_etree_process    | 38.9 ms                                                | 35.6 ms: 1.09x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 50.9 ms: 1.09x faster                                                 |
| unpickle_pure_python | 145 us                                                 | 134 us: 1.09x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 72.5 ms: 1.04x faster                                                 |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| json_dumps           | 6.19 ms                                                | 6.55 ms: 1.06x slower                                                 |
| pickle_pure_python   | 197 us                                                 | 210 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.5 ms: 1.04x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 13.8 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.93 ms: 1.07x faster                                                 |
| genshi_text     | 14.7 ms                                                | 14.9 ms: 1.01x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 31.1 ms: 1.02x slower                                                 |
| django_template | 19.7 ms                                                | 21.8 ms: 1.11x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.8 ms: 2.33x faster                                                 |
| mdp                              | 1.49 sec                                               | 759 ms: 1.97x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 360 ms: 1.85x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 374 ms: 1.79x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 377 ms: 1.78x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 371 ms: 1.66x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.64x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 163 ms: 1.62x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 194 ms: 1.60x faster                                                  |
| deepcopy                         | 226 us                                                 | 155 us: 1.45x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 19.5 us: 1.33x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                  |
| generators                       | 29.4 ms                                                | 24.0 ms: 1.22x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.67 us: 1.21x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 25.1 ms: 1.17x faster                                                 |
| comprehensions                   | 14.0 us                                                | 12.1 us: 1.16x faster                                                 |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                                 |
| raytrace                         | 204 ms                                                 | 179 ms: 1.14x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                |
| pathlib                          | 24.7 ms                                                | 21.9 ms: 1.13x faster                                                 |
| go                               | 98.5 ms                                                | 87.3 ms: 1.13x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 67.9 ms: 1.13x faster                                                 |
| pylint                           | 182 ms                                                 | 163 ms: 1.12x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.23 sec: 1.10x faster                                                |
| xml_etree_process                | 38.9 ms                                                | 35.6 ms: 1.09x faster                                                 |
| xml_etree_generate               | 55.4 ms                                                | 50.9 ms: 1.09x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 134 us: 1.09x faster                                                  |
| float                            | 54.1 ms                                                | 49.9 ms: 1.08x faster                                                 |
| mako                             | 7.44 ms                                                | 6.93 ms: 1.07x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 71.1 ms: 1.07x faster                                                 |
| async_generators                 | 299 ms                                                 | 280 ms: 1.07x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.08 sec: 1.07x faster                                                |
| pyflate                          | 311 ms                                                 | 292 ms: 1.07x faster                                                  |
| html5lib                         | 33.4 ms                                                | 31.5 ms: 1.06x faster                                                 |
| thrift                           | 468 us                                                 | 443 us: 1.06x faster                                                  |
| chaos                            | 41.6 ms                                                | 39.5 ms: 1.05x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.05x faster                                                  |
| sphinx                           | 613 ms                                                 | 584 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 358 ms: 1.04x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 72.5 ms: 1.04x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.47 us: 1.04x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.76 us: 1.04x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.37 ms: 1.03x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 64.3 ms: 1.02x faster                                                 |
| json                             | 3.00 ms                                                | 2.94 ms: 1.02x faster                                                 |
| dask                             | 779 ms                                                 | 766 ms: 1.02x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 75.7 ms: 1.01x faster                                                 |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                  |
| regex_dna                        | 143 ms                                                 | 143 ms: 1.00x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 14.9 ms: 1.01x slower                                                 |
| shortest_path                    | 331 ms                                                 | 337 ms: 1.02x slower                                                  |
| 2to3                             | 168 ms                                                 | 172 ms: 1.02x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 31.1 ms: 1.02x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.58 us: 1.02x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 199 ms: 1.03x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 45.9 ms: 1.03x slower                                                 |
| nqueens                          | 59.5 ms                                                | 61.5 ms: 1.03x slower                                                 |
| connected_components             | 300 ms                                                 | 311 ms: 1.04x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.67 ms: 1.04x slower                                                 |
| scimark_sor                      | 85.8 ms                                                | 89.2 ms: 1.04x slower                                                 |
| python_startup                   | 17.8 ms                                                | 18.5 ms: 1.04x slower                                                 |
| pycparser                        | 673 ms                                                 | 702 ms: 1.04x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 244 ms: 1.04x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 13.8 ms: 1.05x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 6.55 ms: 1.06x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 97.6 us: 1.07x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 210 us: 1.07x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 16.2 ms: 1.08x slower                                                 |
| hexiom                           | 4.38 ms                                                | 4.72 ms: 1.08x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 55.6 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.22 ms: 1.09x slower                                                 |
| pprint_pformat                   | 986 ms                                                 | 1.08 sec: 1.09x slower                                                |
| meteor_contest                   | 69.1 ms                                                | 76.1 ms: 1.10x slower                                                 |
| django_template                  | 19.7 ms                                                | 21.8 ms: 1.11x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 537 ms: 1.11x slower                                                  |
| nbody                            | 67.6 ms                                                | 75.4 ms: 1.12x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 82.0 ms: 1.12x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.12x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.54 ms: 1.12x slower                                                 |
| richards_super                   | 34.6 ms                                                | 39.9 ms: 1.15x slower                                                 |
| richards                         | 30.6 ms                                                | 35.8 ms: 1.17x slower                                                 |
| telco                            | 3.92 ms                                                | 4.61 ms: 1.18x slower                                                 |
| many_optionals                   | 403 us                                                 | 476 us: 1.18x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.18x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.37 ms: 1.19x slower                                                 |
| fannkuch                         | 250 ms                                                 | 302 ms: 1.21x slower                                                  |
| coverage                         | 38.5 ms                                                | 47.9 ms: 1.24x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 128 ms: 2.74x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (5): sympy_str, sympy_integrate, asyncio_websockets, logging_silent, docutils
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 95.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.14x