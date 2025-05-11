# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: darwin-arm64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.059x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 158 ms: 1.07x faster                                                  |
| docutils       | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                |
| html5lib       | 33.4 ms                                                | 29.5 ms: 1.13x faster                                                 |
| sphinx         | 613 ms                                                 | 560 ms: 1.10x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 336 ms: 1.98x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 341 ms: 1.97x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 342 ms: 1.97x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 348 ms: 1.78x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 144 ms: 1.77x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 181 ms: 1.76x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 151 ms: 1.75x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 179 ms: 1.73x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 402 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 406 ms: 1.30x faster                                                  |
| coroutines                       | 19.7 ms                                                | 15.3 ms: 1.29x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 57.2 ms: 1.15x faster                                                 |
| async_generators                 | 299 ms                                                 | 267 ms: 1.12x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 350 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 382 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 160 ms: 1.13x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 120 ms: 2.56x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 44.1 ms: 1.23x faster                                                 |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| nbody          | 67.6 ms                                                | 73.5 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 61.9 ms: 1.23x faster                                                 |
| regex_effbot   | 2.44 ms                                                | 2.21 ms: 1.10x faster                                                 |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.6 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                |
| unpickle_pure_python | 145 us                                                 | 130 us: 1.12x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 188 us: 1.05x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 72.6 ms: 1.04x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 39.3 ms: 1.01x slower                                                 |
| json_loads           | 17.0 us                                                | 18.3 us: 1.07x slower                                                 |
| json_dumps           | 6.19 ms                                                | 7.34 ms: 1.19x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 17.6 ms: 1.01x faster                                                 |
| python_startup_no_site | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.9 ms: 1.13x faster                                                 |
| genshi_xml      | 30.5 ms                                                | 27.1 ms: 1.12x faster                                                 |
| mako            | 7.44 ms                                                | 7.25 ms: 1.03x faster                                                 |
| django_template | 19.7 ms                                                | 19.6 ms: 1.00x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.6 ms: 2.54x faster                                                 |
| mdp                              | 1.49 sec                                               | 706 ms: 2.11x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 336 ms: 1.98x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 341 ms: 1.97x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 342 ms: 1.97x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 348 ms: 1.78x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 144 ms: 1.77x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 181 ms: 1.76x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 151 ms: 1.75x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 179 ms: 1.73x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 16.4 us: 1.59x faster                                                 |
| generators                       | 29.4 ms                                                | 18.9 ms: 1.56x faster                                                 |
| deepcopy                         | 226 us                                                 | 145 us: 1.56x faster                                                  |
| go                               | 98.5 ms                                                | 71.1 ms: 1.38x faster                                                 |
| comprehensions                   | 14.0 us                                                | 10.5 us: 1.33x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 402 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 406 ms: 1.30x faster                                                  |
| coroutines                       | 19.7 ms                                                | 15.3 ms: 1.29x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.58 us: 1.28x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.05 ms: 1.26x faster                                                 |
| float                            | 54.1 ms                                                | 44.1 ms: 1.23x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 23.8 ms: 1.23x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 61.9 ms: 1.23x faster                                                 |
| raytrace                         | 204 ms                                                 | 168 ms: 1.21x faster                                                  |
| pylint                           | 182 ms                                                 | 152 ms: 1.19x faster                                                  |
| chaos                            | 41.6 ms                                                | 35.6 ms: 1.17x faster                                                 |
| hexiom                           | 4.38 ms                                                | 3.77 ms: 1.16x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 57.2 ms: 1.15x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 2.89 sec: 1.14x faster                                                |
| tomli_loads                      | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                |
| genshi_text                      | 14.7 ms                                                | 12.9 ms: 1.13x faster                                                 |
| html5lib                         | 33.4 ms                                                | 29.5 ms: 1.13x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                |
| pyflate                          | 311 ms                                                 | 277 ms: 1.12x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 27.1 ms: 1.12x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 130 us: 1.12x faster                                                  |
| async_generators                 | 299 ms                                                 | 267 ms: 1.12x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 68.9 ms: 1.11x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.26 us: 1.11x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.21 ms: 1.10x faster                                                 |
| scimark_sor                      | 85.8 ms                                                | 77.7 ms: 1.10x faster                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 40.5 ms: 1.10x faster                                                 |
| sympy_str                        | 144 ms                                                 | 131 ms: 1.10x faster                                                  |
| pathlib                          | 24.7 ms                                                | 22.5 ms: 1.10x faster                                                 |
| sphinx                           | 613 ms                                                 | 560 ms: 1.10x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 69.7 ms: 1.09x faster                                                 |
| nqueens                          | 59.5 ms                                                | 54.5 ms: 1.09x faster                                                 |
| sympy_integrate                  | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.59 us: 1.09x faster                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 448 ms: 1.08x faster                                                  |
| pprint_pformat                   | 986 ms                                                 | 915 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 350 ms: 1.07x faster                                                  |
| pycparser                        | 673 ms                                                 | 630 ms: 1.07x faster                                                  |
| 2to3                             | 168 ms                                                 | 158 ms: 1.07x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 69.7 ms: 1.05x faster                                                 |
| sympy_expand                     | 233 ms                                                 | 222 ms: 1.05x faster                                                  |
| pickle_pure_python               | 197 us                                                 | 188 us: 1.05x faster                                                  |
| richards_super                   | 34.6 ms                                                | 33.2 ms: 1.04x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 72.6 ms: 1.04x faster                                                 |
| richards                         | 30.6 ms                                                | 29.5 ms: 1.04x faster                                                 |
| docutils                         | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                |
| crypto_pyaes                     | 51.4 ms                                                | 49.8 ms: 1.03x faster                                                 |
| mako                             | 7.44 ms                                                | 7.25 ms: 1.03x faster                                                 |
| bench_thread_pool                | 483 us                                                 | 473 us: 1.02x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                  |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| shortest_path                    | 331 ms                                                 | 328 ms: 1.01x faster                                                  |
| python_startup                   | 17.8 ms                                                | 17.6 ms: 1.01x faster                                                 |
| django_template                  | 19.7 ms                                                | 19.6 ms: 1.00x faster                                                 |
| connected_components             | 300 ms                                                 | 302 ms: 1.01x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.56 us: 1.01x slower                                                 |
| xml_etree_process                | 38.9 ms                                                | 39.3 ms: 1.01x slower                                                 |
| json                             | 3.00 ms                                                | 3.05 ms: 1.02x slower                                                 |
| fannkuch                         | 250 ms                                                 | 255 ms: 1.02x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 70.6 ms: 1.02x slower                                                 |
| dask                             | 779 ms                                                 | 802 ms: 1.03x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 15.6 ms: 1.03x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 68.9 ms: 1.05x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 205 ms: 1.06x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.37 ms: 1.07x slower                                                 |
| json_loads                       | 17.0 us                                                | 18.3 us: 1.07x slower                                                 |
| nbody                            | 67.6 ms                                                | 73.5 ms: 1.09x slower                                                 |
| many_optionals                   | 403 us                                                 | 440 us: 1.09x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.22 ms: 1.09x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 382 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 160 ms: 1.13x slower                                                  |
| telco                            | 3.92 ms                                                | 4.51 ms: 1.15x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.34 ms: 1.17x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 7.34 ms: 1.19x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 120 ms: 2.56x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 302 ns: 4.17x slower                                                  |
| coverage                         | 38.5 ms                                                | 258 ms: 6.70x slower                                                  |
| thrift                           | 468 us                                                 | 43.1 ms: 92.08x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (3): typing_runtime_protocols, asyncio_websockets, xml_etree_generate
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.12x