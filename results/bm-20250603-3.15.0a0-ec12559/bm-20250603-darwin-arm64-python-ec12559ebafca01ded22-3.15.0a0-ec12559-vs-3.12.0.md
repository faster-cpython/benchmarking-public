# Results vs. 3.12.0

- fork: python
- ref: ec12559ebafca01ded22
- machine: darwin-arm64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.024x slower
- HPT reliability: 61.25%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 211 ms: 1.25x slower                                                  |
| docutils       | 1.45 sec                                               | 1.48 sec: 1.02x slower                                                |
| html5lib       | 33.4 ms                                                | 31.7 ms: 1.05x faster                                                 |
| sphinx         | 613 ms                                                 | 588 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 369 ms: 1.81x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 374 ms: 1.80x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 383 ms: 1.76x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 194 ms: 1.64x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 379 ms: 1.63x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 159 ms: 1.61x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 165 ms: 1.59x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.57x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 416 ms: 1.26x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| coroutines                       | 19.7 ms                                                | 17.1 ms: 1.15x faster                                                 |
| async_generators                 | 299 ms                                                 | 262 ms: 1.14x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 64.4 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.21x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.78x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.9 ms: 1.09x faster                                                 |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                  |
| nbody          | 67.6 ms                                                | 75.3 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 72.0 ms: 1.05x faster                                                 |
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                 |
| regex_v8       | 15.1 ms                                                | 16.1 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 53.7 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 73.4 ms: 1.03x faster                                                 |
| xml_etree_process    | 38.9 ms                                                | 39.0 ms: 1.00x slower                                                 |
| json_dumps           | 6.19 ms                                                | 6.55 ms: 1.06x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 161 us: 1.11x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 219 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 20.3 ms: 1.14x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 15.8 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 14.7 ms: 1.00x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 31.3 ms: 1.03x slower                                                 |
| mako            | 7.44 ms                                                | 7.81 ms: 1.05x slower                                                 |
| django_template | 19.7 ms                                                | 22.2 ms: 1.13x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.7 ms: 2.35x faster                                                 |
| mdp                              | 1.49 sec                                               | 764 ms: 1.95x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 369 ms: 1.81x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 374 ms: 1.80x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 383 ms: 1.76x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 194 ms: 1.64x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 379 ms: 1.63x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 159 ms: 1.61x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 165 ms: 1.59x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.57x faster                                                  |
| deepcopy                         | 226 us                                                 | 157 us: 1.44x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 19.2 us: 1.35x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 416 ms: 1.26x faster                                                  |
| generators                       | 29.4 ms                                                | 24.1 ms: 1.22x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.69 us: 1.19x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 25.0 ms: 1.17x faster                                                 |
| comprehensions                   | 14.0 us                                                | 12.0 us: 1.16x faster                                                 |
| coroutines                       | 19.7 ms                                                | 17.1 ms: 1.15x faster                                                 |
| async_generators                 | 299 ms                                                 | 262 ms: 1.14x faster                                                  |
| raytrace                         | 204 ms                                                 | 180 ms: 1.13x faster                                                  |
| go                               | 98.5 ms                                                | 87.6 ms: 1.12x faster                                                 |
| pylint                           | 182 ms                                                 | 164 ms: 1.11x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.55 sec: 1.11x faster                                                |
| float                            | 54.1 ms                                                | 49.9 ms: 1.09x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 71.0 ms: 1.08x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.09 sec: 1.06x faster                                                |
| pathlib                          | 24.7 ms                                                | 23.3 ms: 1.06x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 72.0 ms: 1.05x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| html5lib                         | 33.4 ms                                                | 31.7 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                  |
| sphinx                           | 613 ms                                                 | 588 ms: 1.04x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                 |
| json                             | 3.00 ms                                                | 2.90 ms: 1.04x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                                 |
| chaos                            | 41.6 ms                                                | 40.3 ms: 1.03x faster                                                 |
| xml_etree_generate               | 55.4 ms                                                | 53.7 ms: 1.03x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 73.4 ms: 1.03x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 64.4 ms: 1.02x faster                                                 |
| sympy_str                        | 144 ms                                                 | 143 ms: 1.01x faster                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.0 ms: 1.00x faster                                                 |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 39.0 ms: 1.00x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 14.7 ms: 1.00x slower                                                 |
| deltablue                        | 2.57 ms                                                | 2.58 ms: 1.01x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 196 ms: 1.01x slower                                                  |
| pycparser                        | 673 ms                                                 | 683 ms: 1.01x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.48 sec: 1.02x slower                                                |
| logging_simple                   | 3.60 us                                                | 3.69 us: 1.02x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 31.3 ms: 1.03x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.23 ms: 1.03x slower                                                 |
| logging_format                   | 3.90 us                                                | 4.01 us: 1.03x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.03x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 242 ms: 1.04x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 89.0 ms: 1.04x slower                                                 |
| shortest_path                    | 331 ms                                                 | 344 ms: 1.04x slower                                                  |
| nqueens                          | 59.5 ms                                                | 62.1 ms: 1.04x slower                                                 |
| pyflate                          | 311 ms                                                 | 325 ms: 1.05x slower                                                  |
| mako                             | 7.44 ms                                                | 7.81 ms: 1.05x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 46.7 ms: 1.05x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 96.5 us: 1.05x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 6.55 ms: 1.06x slower                                                 |
| dask                             | 779 ms                                                 | 827 ms: 1.06x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 16.1 ms: 1.07x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 73.6 ms: 1.07x slower                                                 |
| fannkuch                         | 250 ms                                                 | 267 ms: 1.07x slower                                                  |
| hexiom                           | 4.38 ms                                                | 4.67 ms: 1.07x slower                                                 |
| connected_components             | 300 ms                                                 | 321 ms: 1.07x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.23 ms: 1.10x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 161 us: 1.11x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 219 us: 1.11x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 57.2 ms: 1.11x slower                                                 |
| nbody                            | 67.6 ms                                                | 75.3 ms: 1.12x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                  |
| django_template                  | 19.7 ms                                                | 22.2 ms: 1.13x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 83.6 ms: 1.14x slower                                                 |
| pprint_pformat                   | 986 ms                                                 | 1.12 sec: 1.14x slower                                                |
| python_startup                   | 17.8 ms                                                | 20.3 ms: 1.14x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 555 ms: 1.15x slower                                                  |
| many_optionals                   | 403 us                                                 | 467 us: 1.16x slower                                                  |
| telco                            | 3.92 ms                                                | 4.55 ms: 1.16x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.35 ms: 1.17x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 15.8 ms: 1.20x slower                                                 |
| richards                         | 30.6 ms                                                | 36.7 ms: 1.20x slower                                                 |
| richards_super                   | 34.6 ms                                                | 41.5 ms: 1.20x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.21x slower                                                  |
| 2to3                             | 168 ms                                                 | 211 ms: 1.25x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.78x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 339 ns: 4.68x slower                                                  |
| coverage                         | 38.5 ms                                                | 292 ms: 7.58x slower                                                  |
| thrift                           | 468 us                                                 | 43.6 ms: 93.33x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (4): sympy_sum, asyncio_websockets, regex_dna, tomli_loads
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250603-3.15.0a0-ec12559/bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.024x slower

# HPT report

- Reliability score: 61.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x