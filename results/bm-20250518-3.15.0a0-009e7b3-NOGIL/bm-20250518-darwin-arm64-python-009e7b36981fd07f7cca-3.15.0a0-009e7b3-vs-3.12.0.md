# Results vs. 3.12.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: darwin-arm64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.053x slower
- HPT reliability: 99.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 205 ms: 1.22x slower                                                  |
| docutils       | 1.45 sec                                               | 1.53 sec: 1.05x slower                                                |
| html5lib       | 33.4 ms                                                | 35.2 ms: 1.05x slower                                                 |
| sphinx         | 613 ms                                                 | 648 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 336 ms: 2.00x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 343 ms: 1.94x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 326 ms: 1.89x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 362 ms: 1.86x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 149 ms: 1.72x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 173 ms: 1.52x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 205 ms: 1.51x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 243 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 453 ms: 1.17x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.9 ms: 1.04x faster                                                 |
| async_generators                 | 299 ms                                                 | 291 ms: 1.03x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 237 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 169 ms: 1.19x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 91.6 ms: 1.39x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.76x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.18x faster                                                          |

Benchmark hidden because not significant (1): async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| float          | 54.1 ms                                                | 53.8 ms: 1.01x faster                                                 |
| nbody          | 67.6 ms                                                | 95.3 ms: 1.41x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.11 ms: 1.16x faster                                                 |
| regex_dna      | 143 ms                                                 | 136 ms: 1.05x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.1 ms: 1.00x faster                                                 |
| regex_compile  | 75.9 ms                                                | 95.8 ms: 1.26x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 66.7 ms: 1.13x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 97.6 ms: 1.11x faster                                                 |
| json_loads           | 17.0 us                                                | 19.1 us: 1.12x slower                                                 |
| xml_etree_generate   | 55.4 ms                                                | 63.4 ms: 1.14x slower                                                 |
| json_dumps           | 6.19 ms                                                | 7.27 ms: 1.17x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.64 sec: 1.21x slower                                                |
| xml_etree_process    | 38.9 ms                                                | 48.2 ms: 1.24x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 190 us: 1.31x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 272 us: 1.38x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.8 ms: 1.12x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 15.3 ms: 1.16x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 38.8 ms: 1.27x slower                                                 |
| genshi_text     | 14.7 ms                                                | 19.4 ms: 1.32x slower                                                 |
| django_template | 19.7 ms                                                | 29.0 ms: 1.47x slower                                                 |
| mako            | 7.44 ms                                                | 11.6 ms: 1.56x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.40x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 15.7 ms: 2.04x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 336 ms: 2.00x faster                                                  |
| gc_traversal                     | 2.95 ms                                                | 1.49 ms: 1.98x faster                                                 |
| async_tree_eager_io              | 666 ms                                                 | 343 ms: 1.94x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 326 ms: 1.89x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 362 ms: 1.86x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 149 ms: 1.72x faster                                                  |
| mdp                              | 1.49 sec                                               | 905 ms: 1.65x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 173 ms: 1.52x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 205 ms: 1.51x faster                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 824 us: 1.40x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 243 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 453 ms: 1.17x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.11 ms: 1.16x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 66.7 ms: 1.13x faster                                                 |
| deepcopy                         | 226 us                                                 | 200 us: 1.13x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.37 us: 1.13x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 97.6 ms: 1.11x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.63 sec: 1.06x faster                                                |
| regex_dna                        | 143 ms                                                 | 136 ms: 1.05x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 28.0 ms: 1.04x faster                                                 |
| coroutines                       | 19.7 ms                                                | 18.9 ms: 1.04x faster                                                 |
| async_generators                 | 299 ms                                                 | 291 ms: 1.03x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 237 ms: 1.02x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 25.6 us: 1.02x faster                                                 |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| float                            | 54.1 ms                                                | 53.8 ms: 1.01x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.27 sec: 1.00x faster                                                |
| regex_v8                         | 15.1 ms                                                | 15.1 ms: 1.00x faster                                                 |
| pathlib                          | 24.7 ms                                                | 25.4 ms: 1.03x slower                                                 |
| docutils                         | 1.45 sec                                               | 1.53 sec: 1.05x slower                                                |
| html5lib                         | 33.4 ms                                                | 35.2 ms: 1.05x slower                                                 |
| sphinx                           | 613 ms                                                 | 648 ms: 1.06x slower                                                  |
| json                             | 3.00 ms                                                | 3.18 ms: 1.06x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 81.0 ms: 1.06x slower                                                 |
| comprehensions                   | 14.0 us                                                | 14.9 us: 1.07x slower                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 2.15 us: 1.07x slower                                                 |
| shortest_path                    | 331 ms                                                 | 359 ms: 1.09x slower                                                  |
| generators                       | 29.4 ms                                                | 31.9 ms: 1.09x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                  |
| pycparser                        | 673 ms                                                 | 734 ms: 1.09x slower                                                  |
| connected_components             | 300 ms                                                 | 333 ms: 1.11x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 12.3 ms: 1.11x slower                                                 |
| python_startup                   | 17.8 ms                                                | 19.8 ms: 1.12x slower                                                 |
| json_loads                       | 17.0 us                                                | 19.1 us: 1.12x slower                                                 |
| raytrace                         | 204 ms                                                 | 228 ms: 1.12x slower                                                  |
| thrift                           | 468 us                                                 | 524 us: 1.12x slower                                                  |
| go                               | 98.5 ms                                                | 111 ms: 1.12x slower                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 73.8 ms: 1.13x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.57 ms: 1.13x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 63.4 ms: 1.14x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 88.3 ms: 1.16x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 15.3 ms: 1.16x slower                                                 |
| pyflate                          | 311 ms                                                 | 364 ms: 1.17x slower                                                  |
| deltablue                        | 2.57 ms                                                | 3.01 ms: 1.17x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 7.27 ms: 1.17x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 229 ms: 1.18x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 102 ms: 1.19x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 169 ms: 1.19x slower                                                  |
| sympy_str                        | 144 ms                                                 | 172 ms: 1.19x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 83.4 ms: 1.21x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.64 sec: 1.21x slower                                                |
| 2to3                             | 168 ms                                                 | 205 ms: 1.22x slower                                                  |
| chaos                            | 41.6 ms                                                | 51.3 ms: 1.23x slower                                                 |
| nqueens                          | 59.5 ms                                                | 73.6 ms: 1.24x slower                                                 |
| xml_etree_process                | 38.9 ms                                                | 48.2 ms: 1.24x slower                                                 |
| fannkuch                         | 250 ms                                                 | 315 ms: 1.26x slower                                                  |
| regex_compile                    | 75.9 ms                                                | 95.8 ms: 1.26x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 297 ms: 1.27x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 38.8 ms: 1.27x slower                                                 |
| pprint_pformat                   | 986 ms                                                 | 1.26 sec: 1.28x slower                                                |
| crypto_pyaes                     | 51.4 ms                                                | 66.1 ms: 1.28x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 621 ms: 1.28x slower                                                  |
| many_optionals                   | 403 us                                                 | 518 us: 1.28x slower                                                  |
| hexiom                           | 4.38 ms                                                | 5.72 ms: 1.31x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 190 us: 1.31x slower                                                  |
| logging_simple                   | 3.60 us                                                | 4.72 us: 1.31x slower                                                 |
| logging_format                   | 3.90 us                                                | 5.11 us: 1.31x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 19.4 ms: 1.32x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 98.2 ms: 1.34x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 124 us: 1.36x slower                                                  |
| richards                         | 30.6 ms                                                | 41.5 ms: 1.36x slower                                                 |
| telco                            | 3.92 ms                                                | 5.33 ms: 1.36x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 272 us: 1.38x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 91.6 ms: 1.39x slower                                                 |
| richards_super                   | 34.6 ms                                                | 48.2 ms: 1.39x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 62.5 ms: 1.41x slower                                                 |
| nbody                            | 67.6 ms                                                | 95.3 ms: 1.41x slower                                                 |
| django_template                  | 19.7 ms                                                | 29.0 ms: 1.47x slower                                                 |
| mako                             | 7.44 ms                                                | 11.6 ms: 1.56x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 762 us: 1.58x slower                                                  |
| coverage                         | 38.5 ms                                                | 66.6 ms: 1.73x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.76x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 373 ns: 5.14x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (2): pylint, async_tree_eager_cpu_io_mixed
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.053x slower

# HPT report

- Reliability score: 99.04% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.28x