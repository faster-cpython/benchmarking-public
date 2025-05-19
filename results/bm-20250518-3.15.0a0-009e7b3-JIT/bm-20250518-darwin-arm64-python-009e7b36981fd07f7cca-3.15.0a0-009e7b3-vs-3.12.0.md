# Results vs. 3.12.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: darwin-arm64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.007x faster
- HPT reliability: 98.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 184 ms: 1.09x slower                                                  |
| html5lib       | 33.4 ms                                                | 29.7 ms: 1.12x faster                                                 |
| sphinx         | 613 ms                                                 | 584 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 360 ms: 1.85x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 367 ms: 1.84x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 374 ms: 1.79x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 189 ms: 1.69x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 367 ms: 1.68x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 152 ms: 1.68x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 157 ms: 1.67x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 187 ms: 1.66x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 408 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 412 ms: 1.28x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.20x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.4 ms: 1.20x faster                                                 |
| async_generators                 | 299 ms                                                 | 281 ms: 1.06x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 62.4 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 356 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 385 ms: 1.11x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 166 ms: 1.17x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 126 ms: 2.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.25x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 45.9 ms: 1.18x faster                                                 |
| nbody          | 67.6 ms                                                | 72.9 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.17 ms: 1.12x faster                                                 |
| regex_compile  | 75.9 ms                                                | 67.6 ms: 1.12x faster                                                 |
| regex_dna      | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.7 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.23 sec: 1.10x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 99.7 ms: 1.08x faster                                                 |
| xml_etree_process    | 38.9 ms                                                | 36.0 ms: 1.08x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 51.5 ms: 1.08x faster                                                 |
| unpickle_pure_python | 145 us                                                 | 136 us: 1.07x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 71.2 ms: 1.06x faster                                                 |
| pickle_pure_python   | 197 us                                                 | 200 us: 1.02x slower                                                  |
| json_loads           | 17.0 us                                                | 18.1 us: 1.07x slower                                                 |
| json_dumps           | 6.19 ms                                                | 6.64 ms: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.0 ms: 1.01x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.83 ms: 1.09x faster                                                 |
| genshi_text     | 14.7 ms                                                | 13.8 ms: 1.06x faster                                                 |
| genshi_xml      | 30.5 ms                                                | 29.2 ms: 1.05x faster                                                 |
| django_template | 19.7 ms                                                | 21.0 ms: 1.07x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.4 ms: 2.39x faster                                                 |
| mdp                              | 1.49 sec                                               | 756 ms: 1.97x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 360 ms: 1.85x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 367 ms: 1.84x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 374 ms: 1.79x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 189 ms: 1.69x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 367 ms: 1.68x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 152 ms: 1.68x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 157 ms: 1.67x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 187 ms: 1.66x faster                                                  |
| deepcopy                         | 226 us                                                 | 151 us: 1.49x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 18.5 us: 1.41x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 408 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 412 ms: 1.28x faster                                                  |
| generators                       | 29.4 ms                                                | 23.3 ms: 1.26x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.62 us: 1.24x faster                                                 |
| go                               | 98.5 ms                                                | 79.9 ms: 1.23x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.20x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.4 ms: 1.20x faster                                                 |
| raytrace                         | 204 ms                                                 | 171 ms: 1.19x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 24.8 ms: 1.18x faster                                                 |
| float                            | 54.1 ms                                                | 45.9 ms: 1.18x faster                                                 |
| html5lib                         | 33.4 ms                                                | 29.7 ms: 1.12x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.17 ms: 1.12x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 67.6 ms: 1.12x faster                                                 |
| comprehensions                   | 14.0 us                                                | 12.6 us: 1.11x faster                                                 |
| pylint                           | 182 ms                                                 | 164 ms: 1.11x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 69.2 ms: 1.11x faster                                                 |
| deltablue                        | 2.57 ms                                                | 2.32 ms: 1.10x faster                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.23 sec: 1.10x faster                                                |
| chaos                            | 41.6 ms                                                | 37.9 ms: 1.10x faster                                                 |
| scimark_sor                      | 85.8 ms                                                | 78.2 ms: 1.10x faster                                                 |
| mako                             | 7.44 ms                                                | 6.83 ms: 1.09x faster                                                 |
| pyflate                          | 311 ms                                                 | 287 ms: 1.08x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 99.7 ms: 1.08x faster                                                 |
| xml_etree_process                | 38.9 ms                                                | 36.0 ms: 1.08x faster                                                 |
| xml_etree_generate               | 55.4 ms                                                | 51.5 ms: 1.08x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 136 us: 1.07x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.06 sec: 1.07x faster                                                |
| k_core                           | 1.72 sec                                               | 1.61 sec: 1.07x faster                                                |
| async_generators                 | 299 ms                                                 | 281 ms: 1.06x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 71.2 ms: 1.06x faster                                                 |
| genshi_text                      | 14.7 ms                                                | 13.8 ms: 1.06x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 62.4 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 356 ms: 1.05x faster                                                  |
| sphinx                           | 613 ms                                                 | 584 ms: 1.05x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 29.2 ms: 1.05x faster                                                 |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 74.1 ms: 1.03x faster                                                 |
| sympy_str                        | 144 ms                                                 | 140 ms: 1.03x faster                                                  |
| sympy_integrate                  | 11.1 ms                                                | 10.8 ms: 1.02x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.53 us: 1.02x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.83 us: 1.02x faster                                                 |
| hexiom                           | 4.38 ms                                                | 4.31 ms: 1.02x faster                                                 |
| json                             | 3.00 ms                                                | 3.03 ms: 1.01x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 488 us: 1.01x slower                                                  |
| python_startup                   | 17.8 ms                                                | 18.0 ms: 1.01x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 200 us: 1.02x slower                                                  |
| pycparser                        | 673 ms                                                 | 683 ms: 1.02x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 74.7 ms: 1.02x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 239 ms: 1.02x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 499 ms: 1.03x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.02 sec: 1.03x slower                                                |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.04x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 15.7 ms: 1.04x slower                                                 |
| dask                             | 779 ms                                                 | 816 ms: 1.05x slower                                                  |
| shortest_path                    | 331 ms                                                 | 348 ms: 1.05x slower                                                  |
| richards_super                   | 34.6 ms                                                | 36.6 ms: 1.06x slower                                                 |
| json_loads                       | 17.0 us                                                | 18.1 us: 1.07x slower                                                 |
| django_template                  | 19.7 ms                                                | 21.0 ms: 1.07x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 69.9 ms: 1.07x slower                                                 |
| connected_components             | 300 ms                                                 | 320 ms: 1.07x slower                                                  |
| richards                         | 30.6 ms                                                | 32.7 ms: 1.07x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 6.64 ms: 1.07x slower                                                 |
| nbody                            | 67.6 ms                                                | 72.9 ms: 1.08x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 55.8 ms: 1.08x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 99.8 us: 1.09x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.22 ms: 1.09x slower                                                 |
| 2to3                             | 168 ms                                                 | 184 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 385 ms: 1.11x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 78.0 ms: 1.13x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 221 ms: 1.13x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 166 ms: 1.17x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.70 ms: 1.18x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                 |
| many_optionals                   | 403 us                                                 | 483 us: 1.20x slower                                                  |
| telco                            | 3.92 ms                                                | 4.70 ms: 1.20x slower                                                 |
| fannkuch                         | 250 ms                                                 | 305 ms: 1.22x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 126 ms: 2.69x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 324 ns: 4.47x slower                                                  |
| coverage                         | 38.5 ms                                                | 270 ms: 7.01x slower                                                  |
| thrift                           | 468 us                                                 | 43.4 ms: 92.75x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (6): scimark_monte_carlo, nqueens, asyncio_websockets, pidigits, docutils, pathlib
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 98.49% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.14x