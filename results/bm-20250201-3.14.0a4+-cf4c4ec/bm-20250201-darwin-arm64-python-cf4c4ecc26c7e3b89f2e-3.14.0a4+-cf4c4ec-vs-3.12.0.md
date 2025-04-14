# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: darwin-arm64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.109x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 158 ms: 1.06x faster                                                   |
| docutils       | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                 |
| html5lib       | 33.4 ms                                                | 28.6 ms: 1.17x faster                                                  |
| sphinx         | 613 ms                                                 | 558 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 359 ms: 1.86x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 363 ms: 1.85x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 367 ms: 1.83x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 153 ms: 1.67x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 158 ms: 1.67x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 371 ms: 1.66x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 194 ms: 1.64x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 194 ms: 1.60x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 413 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 416 ms: 1.27x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.7 ms: 1.25x faster                                                  |
| async_generators                 | 299 ms                                                 | 246 ms: 1.21x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 61.9 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 358 ms: 1.04x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 173 ms: 1.22x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.77x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 46.2 ms: 1.17x faster                                                  |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| nbody          | 67.6 ms                                                | 68.6 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 65.5 ms: 1.16x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.28 ms: 1.07x faster                                                  |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| regex_v8       | 15.1 ms                                                | 16.8 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.18 sec: 1.15x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 70.6 ms: 1.07x faster                                                  |
| xml_etree_generate   | 55.4 ms                                                | 51.9 ms: 1.07x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| unpickle_pure_python | 145 us                                                 | 137 us: 1.06x faster                                                   |
| xml_etree_process    | 38.9 ms                                                | 37.7 ms: 1.03x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 195 us: 1.01x faster                                                   |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.29 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 11.4 ms: 1.16x faster                                                  |
| python_startup         | 17.8 ms                                                | 16.0 ms: 1.11x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 13.3 ms: 1.10x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 28.0 ms: 1.09x faster                                                  |
| mako            | 7.44 ms                                                | 7.21 ms: 1.03x faster                                                  |
| django_template | 19.7 ms                                                | 20.4 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.7 ms: 2.74x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 359 ms: 1.86x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 363 ms: 1.85x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 367 ms: 1.83x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 153 ms: 1.67x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 158 ms: 1.67x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 371 ms: 1.66x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 194 ms: 1.64x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 194 ms: 1.60x faster                                                   |
| deepcopy                         | 226 us                                                 | 146 us: 1.55x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 17.7 us: 1.47x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.52 us: 1.32x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 59.6 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 413 ms: 1.28x faster                                                   |
| go                               | 98.5 ms                                                | 77.2 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 416 ms: 1.27x faster                                                   |
| generators                       | 29.4 ms                                                | 23.1 ms: 1.27x faster                                                  |
| coroutines                       | 19.7 ms                                                | 15.7 ms: 1.25x faster                                                  |
| raytrace                         | 204 ms                                                 | 168 ms: 1.22x faster                                                   |
| async_generators                 | 299 ms                                                 | 246 ms: 1.21x faster                                                   |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.62 ms: 1.20x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| comprehensions                   | 14.0 us                                                | 11.8 us: 1.18x faster                                                  |
| float                            | 54.1 ms                                                | 46.2 ms: 1.17x faster                                                  |
| html5lib                         | 33.4 ms                                                | 28.6 ms: 1.17x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.10 us: 1.16x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 65.5 ms: 1.16x faster                                                  |
| python_startup_no_site           | 13.2 ms                                                | 11.4 ms: 1.16x faster                                                  |
| pylint                           | 182 ms                                                 | 158 ms: 1.15x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 2.85 sec: 1.15x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.40 us: 1.15x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.18 sec: 1.15x faster                                                 |
| scimark_fft                      | 194 ms                                                 | 170 ms: 1.14x faster                                                   |
| k_core                           | 1.72 sec                                               | 1.51 sec: 1.14x faster                                                 |
| pathlib                          | 24.7 ms                                                | 21.8 ms: 1.13x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 75.9 ms: 1.13x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 58.2 ms: 1.13x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.28 ms: 1.13x faster                                                  |
| chaos                            | 41.6 ms                                                | 37.3 ms: 1.12x faster                                                  |
| python_startup                   | 17.8 ms                                                | 16.0 ms: 1.11x faster                                                  |
| genshi_text                      | 14.7 ms                                                | 13.3 ms: 1.10x faster                                                  |
| sphinx                           | 613 ms                                                 | 558 ms: 1.10x faster                                                   |
| pyflate                          | 311 ms                                                 | 283 ms: 1.10x faster                                                   |
| thrift                           | 468 us                                                 | 426 us: 1.10x faster                                                   |
| genshi_xml                       | 30.5 ms                                                | 28.0 ms: 1.09x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 67.3 ns: 1.08x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 57.6 ms: 1.08x faster                                                  |
| pprint_pformat                   | 986 ms                                                 | 919 ms: 1.07x faster                                                   |
| dulwich_log                      | 29.2 ms                                                | 27.2 ms: 1.07x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.28 ms: 1.07x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 70.6 ms: 1.07x faster                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 452 ms: 1.07x faster                                                   |
| sqlglot_parse                    | 808 us                                                 | 757 us: 1.07x faster                                                   |
| xml_etree_generate               | 55.4 ms                                                | 51.9 ms: 1.07x faster                                                  |
| sqlglot_transpile                | 973 us                                                 | 915 us: 1.06x faster                                                   |
| 2to3                             | 168 ms                                                 | 158 ms: 1.06x faster                                                   |
| pycparser                        | 673 ms                                                 | 633 ms: 1.06x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 61.9 ms: 1.06x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| sympy_str                        | 144 ms                                                 | 136 ms: 1.06x faster                                                   |
| unpickle_pure_python             | 145 us                                                 | 137 us: 1.06x faster                                                   |
| scimark_monte_carlo              | 44.5 ms                                                | 42.1 ms: 1.06x faster                                                  |
| nqueens                          | 59.5 ms                                                | 56.5 ms: 1.05x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 72.3 ms: 1.05x faster                                                  |
| hexiom                           | 4.38 ms                                                | 4.16 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 358 ms: 1.04x faster                                                   |
| sqlglot_optimize                 | 33.2 ms                                                | 31.8 ms: 1.04x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                 |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.34 ms: 1.04x faster                                                  |
| mako                             | 7.44 ms                                                | 7.21 ms: 1.03x faster                                                  |
| xml_etree_process                | 38.9 ms                                                | 37.7 ms: 1.03x faster                                                  |
| fannkuch                         | 250 ms                                                 | 243 ms: 1.03x faster                                                   |
| scimark_lu                       | 73.5 ms                                                | 71.7 ms: 1.03x faster                                                  |
| sympy_expand                     | 233 ms                                                 | 228 ms: 1.02x faster                                                   |
| shortest_path                    | 331 ms                                                 | 323 ms: 1.02x faster                                                   |
| sqlglot_normalize                | 180 ms                                                 | 176 ms: 1.02x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.52 us: 1.02x faster                                                  |
| dask                             | 779 ms                                                 | 766 ms: 1.02x faster                                                   |
| connected_components             | 300 ms                                                 | 295 ms: 1.02x faster                                                   |
| json                             | 3.00 ms                                                | 2.96 ms: 1.01x faster                                                  |
| bench_thread_pool                | 483 us                                                 | 477 us: 1.01x faster                                                   |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| mdp                              | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                 |
| pickle_pure_python               | 197 us                                                 | 195 us: 1.01x faster                                                   |
| sympy_integrate                  | 11.1 ms                                                | 11.0 ms: 1.01x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| richards_super                   | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 69.8 ms: 1.01x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 92.7 us: 1.01x slower                                                  |
| nbody                            | 67.6 ms                                                | 68.6 ms: 1.02x slower                                                  |
| richards                         | 30.6 ms                                                | 31.2 ms: 1.02x slower                                                  |
| django_template                  | 19.7 ms                                                | 20.4 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.10 ms: 1.05x slower                                                  |
| many_optionals                   | 403 us                                                 | 431 us: 1.07x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 16.8 ms: 1.12x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.12x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                   |
| telco                            | 3.92 ms                                                | 4.54 ms: 1.16x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.29 ms: 1.18x slower                                                  |
| coverage                         | 38.5 ms                                                | 45.8 ms: 1.19x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 173 ms: 1.22x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.77x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (1): crypto_pyaes
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.109x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x