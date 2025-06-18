# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: darwin-arm64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.011x slower
- HPT reliability: 86.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 186 ms                                                                | 187 ms: 1.00x slower                                                  |
| docutils       | 1.51 sec                                                              | 1.64 sec: 1.09x slower                                                |
| html5lib       | 34.1 ms                                                               | 33.3 ms: 1.02x faster                                                 |
| sphinx         | 616 ms                                                                | 647 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none                  | 182 ms                                                                | 173 ms: 1.05x faster                                                  |
| async_tree_memoization           | 214 ms                                                                | 204 ms: 1.05x faster                                                  |
| async_tree_io_tg                 | 405 ms                                                                | 387 ms: 1.05x faster                                                  |
| coroutines                       | 18.9 ms                                                               | 18.1 ms: 1.04x faster                                                 |
| async_tree_io                    | 413 ms                                                                | 400 ms: 1.03x faster                                                  |
| async_tree_eager                 | 72.7 ms                                                               | 70.5 ms: 1.03x faster                                                 |
| async_tree_none_tg               | 171 ms                                                                | 167 ms: 1.02x faster                                                  |
| async_tree_memoization_tg        | 207 ms                                                                | 202 ms: 1.02x faster                                                  |
| async_tree_eager_memoization     | 151 ms                                                                | 148 ms: 1.02x faster                                                  |
| async_tree_eager_io              | 392 ms                                                                | 386 ms: 1.02x faster                                                  |
| async_tree_eager_memoization_tg  | 183 ms                                                                | 180 ms: 1.02x faster                                                  |
| async_tree_eager_tg              | 143 ms                                                                | 141 ms: 1.02x faster                                                  |
| asyncio_websockets               | 242 ms                                                                | 243 ms: 1.00x slower                                                  |
| async_tree_cpu_io_mixed          | 432 ms                                                                | 450 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 422 ms                                                                | 446 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 367 ms                                                                | 389 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 399 ms                                                                | 425 ms: 1.07x slower                                                  |
| async_generators                 | 273 ms                                                                | 310 ms: 1.14x slower                                                  |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): async_tree_eager_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 57.6 ms                                                               | 51.4 ms: 1.12x faster                                                 |
| nbody          | 84.8 ms                                                               | 83.1 ms: 1.02x faster                                                 |
| pidigits       | 284 ms                                                                | 285 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 81.2 ms                                                               | 74.2 ms: 1.09x faster                                                 |
| regex_effbot   | 2.37 ms                                                               | 2.19 ms: 1.08x faster                                                 |
| regex_dna      | 143 ms                                                                | 145 ms: 1.01x slower                                                  |
| regex_v8       | 16.3 ms                                                               | 17.4 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 178 us                                                                | 155 us: 1.15x faster                                                  |
| pickle_pure_python   | 241 us                                                                | 221 us: 1.09x faster                                                  |
| tomli_loads          | 1.46 sec                                                              | 1.39 sec: 1.05x faster                                                |
| xml_etree_process    | 42.9 ms                                                               | 43.9 ms: 1.02x slower                                                 |
| xml_etree_iterparse  | 74.2 ms                                                               | 76.0 ms: 1.02x slower                                                 |
| xml_etree_parse      | 104 ms                                                                | 112 ms: 1.07x slower                                                  |
| xml_etree_generate   | 58.2 ms                                                               | 65.2 ms: 1.12x slower                                                 |
| json_dumps           | 6.81 ms                                                               | 8.09 ms: 1.19x slower                                                 |
| json_loads           | 16.6 us                                                               | 22.7 us: 1.37x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.3 ms                                                               | 20.2 ms: 1.10x slower                                                 |
| python_startup_no_site | 13.8 ms                                                               | 15.3 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                               | 15.7 ms: 1.13x faster                                                 |
| mako            | 9.01 ms                                                               | 8.21 ms: 1.10x faster                                                 |
| genshi_xml      | 36.2 ms                                                               | 33.1 ms: 1.09x faster                                                 |
| django_template | 25.1 ms                                                               | 25.5 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                       | 31.5 ms                                                               | 22.8 ms: 1.38x faster                                                 |
| go                               | 99.3 ms                                                               | 77.2 ms: 1.29x faster                                                 |
| sqlglot_v2_parse                 | 991 us                                                                | 848 us: 1.17x faster                                                  |
| unpickle_pure_python             | 178 us                                                                | 155 us: 1.15x faster                                                  |
| genshi_text                      | 17.7 ms                                                               | 15.7 ms: 1.13x faster                                                 |
| scimark_monte_carlo              | 52.5 ms                                                               | 46.7 ms: 1.12x faster                                                 |
| sqlglot_v2_transpile             | 1.17 ms                                                               | 1.04 ms: 1.12x faster                                                 |
| deepcopy_memo                    | 21.7 us                                                               | 19.3 us: 1.12x faster                                                 |
| float                            | 57.6 ms                                                               | 51.4 ms: 1.12x faster                                                 |
| hexiom                           | 5.08 ms                                                               | 4.58 ms: 1.11x faster                                                 |
| comprehensions                   | 13.1 us                                                               | 12.0 us: 1.10x faster                                                 |
| pyflate                          | 333 ms                                                                | 303 ms: 1.10x faster                                                  |
| mako                             | 9.01 ms                                                               | 8.21 ms: 1.10x faster                                                 |
| regex_compile                    | 81.2 ms                                                               | 74.2 ms: 1.09x faster                                                 |
| genshi_xml                       | 36.2 ms                                                               | 33.1 ms: 1.09x faster                                                 |
| pickle_pure_python               | 241 us                                                                | 221 us: 1.09x faster                                                  |
| regex_effbot                     | 2.37 ms                                                               | 2.19 ms: 1.08x faster                                                 |
| deltablue                        | 2.80 ms                                                               | 2.61 ms: 1.07x faster                                                 |
| chaos                            | 47.2 ms                                                               | 44.1 ms: 1.07x faster                                                 |
| pprint_pformat                   | 1.26 sec                                                              | 1.19 sec: 1.06x faster                                                |
| pprint_safe_repr                 | 622 ms                                                                | 586 ms: 1.06x faster                                                  |
| async_tree_none                  | 182 ms                                                                | 173 ms: 1.05x faster                                                  |
| tomli_loads                      | 1.46 sec                                                              | 1.39 sec: 1.05x faster                                                |
| async_tree_memoization           | 214 ms                                                                | 204 ms: 1.05x faster                                                  |
| async_tree_io_tg                 | 405 ms                                                                | 387 ms: 1.05x faster                                                  |
| nqueens                          | 70.4 ms                                                               | 67.5 ms: 1.04x faster                                                 |
| coroutines                       | 18.9 ms                                                               | 18.1 ms: 1.04x faster                                                 |
| richards                         | 37.1 ms                                                               | 35.9 ms: 1.03x faster                                                 |
| async_tree_io                    | 413 ms                                                                | 400 ms: 1.03x faster                                                  |
| async_tree_eager                 | 72.7 ms                                                               | 70.5 ms: 1.03x faster                                                 |
| richards_super                   | 41.5 ms                                                               | 40.4 ms: 1.03x faster                                                 |
| html5lib                         | 34.1 ms                                                               | 33.3 ms: 1.02x faster                                                 |
| async_tree_none_tg               | 171 ms                                                                | 167 ms: 1.02x faster                                                  |
| async_tree_memoization_tg        | 207 ms                                                                | 202 ms: 1.02x faster                                                  |
| logging_simple                   | 4.05 us                                                               | 3.96 us: 1.02x faster                                                 |
| crypto_pyaes                     | 61.4 ms                                                               | 60.1 ms: 1.02x faster                                                 |
| nbody                            | 84.8 ms                                                               | 83.1 ms: 1.02x faster                                                 |
| async_tree_eager_memoization     | 151 ms                                                                | 148 ms: 1.02x faster                                                  |
| async_tree_eager_io              | 392 ms                                                                | 386 ms: 1.02x faster                                                  |
| async_tree_eager_memoization_tg  | 183 ms                                                                | 180 ms: 1.02x faster                                                  |
| async_tree_eager_tg              | 143 ms                                                                | 141 ms: 1.02x faster                                                  |
| logging_format                   | 4.34 us                                                               | 4.29 us: 1.01x faster                                                 |
| asyncio_websockets               | 242 ms                                                                | 243 ms: 1.00x slower                                                  |
| pidigits                         | 284 ms                                                                | 285 ms: 1.00x slower                                                  |
| 2to3                             | 186 ms                                                                | 187 ms: 1.00x slower                                                  |
| regex_dna                        | 143 ms                                                                | 145 ms: 1.01x slower                                                  |
| django_template                  | 25.1 ms                                                               | 25.5 ms: 1.02x slower                                                 |
| dulwich_log                      | 26.4 ms                                                               | 27.0 ms: 1.02x slower                                                 |
| fannkuch                         | 305 ms                                                                | 311 ms: 1.02x slower                                                  |
| scimark_sor                      | 89.2 ms                                                               | 91.2 ms: 1.02x slower                                                 |
| meteor_contest                   | 74.1 ms                                                               | 75.8 ms: 1.02x slower                                                 |
| xml_etree_process                | 42.9 ms                                                               | 43.9 ms: 1.02x slower                                                 |
| xml_etree_iterparse              | 74.2 ms                                                               | 76.0 ms: 1.02x slower                                                 |
| scimark_lu                       | 84.4 ms                                                               | 86.6 ms: 1.03x slower                                                 |
| create_gc_cycles                 | 1.35 ms                                                               | 1.39 ms: 1.03x slower                                                 |
| connected_components             | 303 ms                                                                | 312 ms: 1.03x slower                                                  |
| shortest_path                    | 327 ms                                                                | 340 ms: 1.04x slower                                                  |
| sqlglot_v2_normalize             | 76.3 ms                                                               | 79.3 ms: 1.04x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                               | 11.8 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed          | 432 ms                                                                | 450 ms: 1.04x slower                                                  |
| k_core                           | 1.47 sec                                                              | 1.54 sec: 1.05x slower                                                |
| sympy_sum                        | 81.4 ms                                                               | 85.1 ms: 1.05x slower                                                 |
| deepcopy_reduce                  | 1.89 us                                                               | 1.98 us: 1.05x slower                                                 |
| pylint                           | 168 ms                                                                | 176 ms: 1.05x slower                                                  |
| sphinx                           | 616 ms                                                                | 647 ms: 1.05x slower                                                  |
| many_optionals                   | 493 us                                                                | 520 us: 1.06x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 422 ms                                                                | 446 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 367 ms                                                                | 389 ms: 1.06x slower                                                  |
| sympy_str                        | 155 ms                                                                | 164 ms: 1.06x slower                                                  |
| deepcopy                         | 175 us                                                                | 186 us: 1.06x slower                                                  |
| sqlglot_v2_optimize              | 36.5 ms                                                               | 38.8 ms: 1.06x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 399 ms                                                                | 425 ms: 1.07x slower                                                  |
| regex_v8                         | 16.3 ms                                                               | 17.4 ms: 1.07x slower                                                 |
| spectral_norm                    | 74.8 ms                                                               | 79.9 ms: 1.07x slower                                                 |
| mdp                              | 825 ms                                                                | 883 ms: 1.07x slower                                                  |
| xml_etree_parse                  | 104 ms                                                                | 112 ms: 1.07x slower                                                  |
| subparsers                       | 14.8 ms                                                               | 15.9 ms: 1.08x slower                                                 |
| pathlib                          | 22.5 ms                                                               | 24.3 ms: 1.08x slower                                                 |
| docutils                         | 1.51 sec                                                              | 1.64 sec: 1.09x slower                                                |
| sympy_expand                     | 262 ms                                                                | 286 ms: 1.09x slower                                                  |
| typing_runtime_protocols         | 110 us                                                                | 120 us: 1.10x slower                                                  |
| python_startup                   | 18.3 ms                                                               | 20.2 ms: 1.10x slower                                                 |
| python_startup_no_site           | 13.8 ms                                                               | 15.3 ms: 1.11x slower                                                 |
| bpe_tokeniser                    | 3.26 sec                                                              | 3.65 sec: 1.12x slower                                                |
| xml_etree_generate               | 58.2 ms                                                               | 65.2 ms: 1.12x slower                                                 |
| async_generators                 | 273 ms                                                                | 310 ms: 1.14x slower                                                  |
| telco                            | 4.77 ms                                                               | 5.50 ms: 1.15x slower                                                 |
| sqlite_synth                     | 1.61 us                                                               | 1.89 us: 1.17x slower                                                 |
| json_dumps                       | 6.81 ms                                                               | 8.09 ms: 1.19x slower                                                 |
| logging_silent                   | 343 ns                                                                | 413 ns: 1.20x slower                                                  |
| coverage                         | 49.1 ms                                                               | 59.8 ms: 1.22x slower                                                 |
| thrift                           | 468 us                                                                | 571 us: 1.22x slower                                                  |
| json                             | 2.93 ms                                                               | 3.83 ms: 1.30x slower                                                 |
| scimark_sparse_mat_mult          | 3.20 ms                                                               | 4.19 ms: 1.31x slower                                                 |
| scimark_fft                      | 204 ms                                                                | 267 ms: 1.31x slower                                                  |
| json_loads                       | 16.6 us                                                               | 22.7 us: 1.37x slower                                                 |
| Geometric mean                   | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (5): async_tree_eager_io_tg, raytrace, dask, gc_traversal, pycparser
Ignored benchmarks (10) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 86.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.97x