# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: darwin-arm64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.001x faster
- HPT reliability: 91.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 189 ms: 1.12x slower                                             |
| docutils       | 1.45 sec                                               | 1.43 sec: 1.02x faster                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                     |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 320 ms: 2.10x faster                                             |
| async_tree_eager_io              | 666 ms                                                 | 329 ms: 2.02x faster                                             |
| async_tree_eager_io_tg           | 617 ms                                                 | 312 ms: 1.98x faster                                             |
| async_tree_io                    | 672 ms                                                 | 343 ms: 1.96x faster                                             |
| async_tree_none_tg               | 255 ms                                                 | 136 ms: 1.87x faster                                             |
| async_tree_memoization_tg        | 318 ms                                                 | 176 ms: 1.81x faster                                             |
| async_tree_none                  | 263 ms                                                 | 160 ms: 1.64x faster                                             |
| async_tree_memoization           | 310 ms                                                 | 199 ms: 1.56x faster                                             |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 386 ms: 1.37x faster                                             |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 409 ms: 1.29x faster                                             |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                            |
| async_generators                 | 299 ms                                                 | 260 ms: 1.15x faster                                             |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                             |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                             |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 370 ms: 1.01x faster                                             |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 368 ms: 1.06x slower                                             |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 162 ms: 1.14x slower                                             |
| async_tree_eager                 | 65.8 ms                                                | 81.5 ms: 1.24x slower                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 120 ms: 2.57x slower                                             |
| Geometric mean                   | (ref)                                                  | 1.27x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 54.1 ms                                                | 50.7 ms: 1.07x faster                                            |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                             |
| nbody          | 67.6 ms                                                | 87.6 ms: 1.30x slower                                            |
| Geometric mean | (ref)                                                  | 1.06x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.08 ms: 1.17x faster                                            |
| regex_dna      | 143 ms                                                 | 137 ms: 1.04x faster                                             |
| regex_compile  | 75.9 ms                                                | 77.1 ms: 1.01x slower                                            |
| regex_v8       | 15.1 ms                                                | 15.5 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 62.5 ms: 1.21x faster                                            |
| xml_etree_parse      | 108 ms                                                 | 99.6 ms: 1.08x faster                                            |
| xml_etree_generate   | 55.4 ms                                                | 56.1 ms: 1.01x slower                                            |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                            |
| unpickle_pure_python | 145 us                                                 | 162 us: 1.11x slower                                             |
| pickle_pure_python   | 197 us                                                 | 224 us: 1.14x slower                                             |
| xml_etree_process    | 38.9 ms                                                | 45.6 ms: 1.17x slower                                            |
| json_dumps           | 6.19 ms                                                | 7.96 ms: 1.29x slower                                            |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                     |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 20.7 ms: 1.17x slower                                            |
| python_startup_no_site | 13.2 ms                                                | 16.1 ms: 1.22x slower                                            |
| Geometric mean         | (ref)                                                  | 1.19x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 33.1 ms: 1.09x slower                                            |
| genshi_text     | 14.7 ms                                                | 17.2 ms: 1.17x slower                                            |
| django_template | 19.7 ms                                                | 24.6 ms: 1.25x slower                                            |
| mako            | 7.44 ms                                                | 9.98 ms: 1.34x slower                                            |
| Geometric mean  | (ref)                                                  | 1.21x slower                                                     |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.4 ms: 2.41x faster                                            |
| async_tree_io_tg                 | 673 ms                                                 | 320 ms: 2.10x faster                                             |
| async_tree_eager_io              | 666 ms                                                 | 329 ms: 2.02x faster                                             |
| async_tree_eager_io_tg           | 617 ms                                                 | 312 ms: 1.98x faster                                             |
| async_tree_io                    | 672 ms                                                 | 343 ms: 1.96x faster                                             |
| async_tree_none_tg               | 255 ms                                                 | 136 ms: 1.87x faster                                             |
| async_tree_memoization_tg        | 318 ms                                                 | 176 ms: 1.81x faster                                             |
| async_tree_none                  | 263 ms                                                 | 160 ms: 1.64x faster                                             |
| async_tree_memoization           | 310 ms                                                 | 199 ms: 1.56x faster                                             |
| create_gc_cycles                 | 1.15 ms                                                | 821 us: 1.40x faster                                             |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 386 ms: 1.37x faster                                             |
| deepcopy                         | 226 us                                                 | 173 us: 1.30x faster                                             |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 409 ms: 1.29x faster                                             |
| gc_traversal                     | 2.95 ms                                                | 2.31 ms: 1.28x faster                                            |
| generators                       | 29.4 ms                                                | 23.8 ms: 1.23x faster                                            |
| xml_etree_iterparse              | 75.5 ms                                                | 62.5 ms: 1.21x faster                                            |
| deepcopy_memo                    | 26.0 us                                                | 21.8 us: 1.20x faster                                            |
| sqlite_synth                     | 1.55 us                                                | 1.31 us: 1.18x faster                                            |
| regex_effbot                     | 2.44 ms                                                | 2.08 ms: 1.17x faster                                            |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                            |
| async_generators                 | 299 ms                                                 | 260 ms: 1.15x faster                                             |
| deepcopy_reduce                  | 2.01 us                                                | 1.78 us: 1.13x faster                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                             |
| bpe_tokeniser                    | 3.28 sec                                               | 3.03 sec: 1.08x faster                                           |
| xml_etree_parse                  | 108 ms                                                 | 99.6 ms: 1.08x faster                                            |
| pathlib                          | 24.7 ms                                                | 22.9 ms: 1.08x faster                                            |
| pylint                           | 182 ms                                                 | 170 ms: 1.07x faster                                             |
| float                            | 54.1 ms                                                | 50.7 ms: 1.07x faster                                            |
| k_core                           | 1.72 sec                                               | 1.62 sec: 1.06x faster                                           |
| regex_dna                        | 143 ms                                                 | 137 ms: 1.04x faster                                             |
| spectral_norm                    | 76.5 ms                                                | 74.2 ms: 1.03x faster                                            |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                             |
| docutils                         | 1.45 sec                                               | 1.43 sec: 1.02x faster                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 370 ms: 1.01x faster                                             |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                             |
| json                             | 3.00 ms                                                | 2.98 ms: 1.01x faster                                            |
| xml_etree_generate               | 55.4 ms                                                | 56.1 ms: 1.01x slower                                            |
| dulwich_log                      | 29.2 ms                                                | 29.6 ms: 1.01x slower                                            |
| nqueens                          | 59.5 ms                                                | 60.4 ms: 1.01x slower                                            |
| regex_compile                    | 75.9 ms                                                | 77.1 ms: 1.01x slower                                            |
| comprehensions                   | 14.0 us                                                | 14.2 us: 1.02x slower                                            |
| pyflate                          | 311 ms                                                 | 317 ms: 1.02x slower                                             |
| bench_mp_pool                    | 65.5 ms                                                | 66.9 ms: 1.02x slower                                            |
| regex_v8                         | 15.1 ms                                                | 15.5 ms: 1.03x slower                                            |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                            |
| sympy_sum                        | 76.2 ms                                                | 80.4 ms: 1.05x slower                                            |
| logging_simple                   | 3.60 us                                                | 3.81 us: 1.06x slower                                            |
| shortest_path                    | 331 ms                                                 | 350 ms: 1.06x slower                                             |
| go                               | 98.5 ms                                                | 104 ms: 1.06x slower                                             |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 368 ms: 1.06x slower                                             |
| sqlglot_normalize                | 180 ms                                                 | 191 ms: 1.06x slower                                             |
| sqlglot_optimize                 | 33.2 ms                                                | 35.4 ms: 1.07x slower                                            |
| logging_format                   | 3.90 us                                                | 4.18 us: 1.07x slower                                            |
| mdp                              | 1.49 sec                                               | 1.60 sec: 1.07x slower                                           |
| sympy_str                        | 144 ms                                                 | 156 ms: 1.08x slower                                             |
| scimark_fft                      | 194 ms                                                 | 211 ms: 1.08x slower                                             |
| genshi_xml                       | 30.5 ms                                                | 33.1 ms: 1.09x slower                                            |
| sqlalchemy_declarative           | 61.9 ms                                                | 67.4 ms: 1.09x slower                                            |
| connected_components             | 300 ms                                                 | 326 ms: 1.09x slower                                             |
| thrift                           | 468 us                                                 | 519 us: 1.11x slower                                             |
| sympy_integrate                  | 11.1 ms                                                | 12.3 ms: 1.11x slower                                            |
| chaos                            | 41.6 ms                                                | 46.2 ms: 1.11x slower                                            |
| unpickle_pure_python             | 145 us                                                 | 162 us: 1.11x slower                                             |
| pprint_pformat                   | 986 ms                                                 | 1.10 sec: 1.12x slower                                           |
| 2to3                             | 168 ms                                                 | 189 ms: 1.12x slower                                             |
| pprint_safe_repr                 | 483 ms                                                 | 541 ms: 1.12x slower                                             |
| scimark_sor                      | 85.8 ms                                                | 96.8 ms: 1.13x slower                                            |
| sympy_expand                     | 233 ms                                                 | 265 ms: 1.13x slower                                             |
| pickle_pure_python               | 197 us                                                 | 224 us: 1.14x slower                                             |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.58 ms: 1.14x slower                                            |
| fannkuch                         | 250 ms                                                 | 285 ms: 1.14x slower                                             |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 162 ms: 1.14x slower                                             |
| meteor_contest                   | 69.1 ms                                                | 79.4 ms: 1.15x slower                                            |
| many_optionals                   | 403 us                                                 | 466 us: 1.16x slower                                             |
| python_startup                   | 17.8 ms                                                | 20.7 ms: 1.17x slower                                            |
| xml_etree_process                | 38.9 ms                                                | 45.6 ms: 1.17x slower                                            |
| genshi_text                      | 14.7 ms                                                | 17.2 ms: 1.17x slower                                            |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.78 ms: 1.18x slower                                            |
| crypto_pyaes                     | 51.4 ms                                                | 61.5 ms: 1.20x slower                                            |
| python_startup_no_site           | 13.2 ms                                                | 16.1 ms: 1.22x slower                                            |
| raytrace                         | 204 ms                                                 | 249 ms: 1.22x slower                                             |
| sqlglot_transpile                | 973 us                                                 | 1.19 ms: 1.23x slower                                            |
| hexiom                           | 4.38 ms                                                | 5.40 ms: 1.23x slower                                            |
| async_tree_eager                 | 65.8 ms                                                | 81.5 ms: 1.24x slower                                            |
| sqlglot_parse                    | 808 us                                                 | 1.01 ms: 1.24x slower                                            |
| django_template                  | 19.7 ms                                                | 24.6 ms: 1.25x slower                                            |
| telco                            | 3.92 ms                                                | 4.92 ms: 1.25x slower                                            |
| typing_runtime_protocols         | 91.5 us                                                | 117 us: 1.28x slower                                             |
| logging_silent                   | 72.5 ns                                                | 92.6 ns: 1.28x slower                                            |
| richards_super                   | 34.6 ms                                                | 44.2 ms: 1.28x slower                                            |
| scimark_monte_carlo              | 44.5 ms                                                | 56.9 ms: 1.28x slower                                            |
| json_dumps                       | 6.19 ms                                                | 7.96 ms: 1.29x slower                                            |
| richards                         | 30.6 ms                                                | 39.4 ms: 1.29x slower                                            |
| nbody                            | 67.6 ms                                                | 87.6 ms: 1.30x slower                                            |
| deltablue                        | 2.57 ms                                                | 3.41 ms: 1.33x slower                                            |
| coverage                         | 38.5 ms                                                | 51.3 ms: 1.33x slower                                            |
| mako                             | 7.44 ms                                                | 9.98 ms: 1.34x slower                                            |
| scimark_lu                       | 73.5 ms                                                | 99.1 ms: 1.35x slower                                            |
| bench_thread_pool                | 483 us                                                 | 794 us: 1.64x slower                                             |
| async_tree_eager_tg              | 46.9 ms                                                | 120 ms: 2.57x slower                                             |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                     |

Benchmark hidden because not significant (4): html5lib, pycparser, tomli_loads, sphinx
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 91.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.21x