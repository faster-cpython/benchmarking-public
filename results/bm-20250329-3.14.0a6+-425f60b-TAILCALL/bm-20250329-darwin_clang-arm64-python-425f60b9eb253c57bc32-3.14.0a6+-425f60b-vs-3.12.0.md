# Results vs. 3.12.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: darwin-arm64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.158x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 151 ms: 1.11x faster                                                   |
| docutils       | 1.45 sec                                               | 1.38 sec: 1.06x faster                                                 |
| html5lib       | 33.4 ms                                                | 29.1 ms: 1.15x faster                                                  |
| sphinx         | 613 ms                                                 | 553 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 335 ms: 2.01x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 339 ms: 1.98x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 339 ms: 1.97x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 346 ms: 1.78x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 144 ms: 1.77x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 181 ms: 1.76x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.75x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 179 ms: 1.73x faster                                                   |
| coroutines                       | 19.7 ms                                                | 14.7 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 399 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 399 ms: 1.32x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 131 ms: 1.28x faster                                                   |
| async_generators                 | 299 ms                                                 | 239 ms: 1.25x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 56.6 ms: 1.16x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 345 ms: 1.08x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 377 ms: 1.09x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 161 ms: 1.14x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 122 ms: 2.59x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 43.2 ms: 1.25x faster                                                  |
| nbody          | 67.6 ms                                                | 61.6 ms: 1.10x faster                                                  |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 62.9 ms: 1.21x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.37 ms: 1.03x faster                                                  |
| regex_dna      | 143 ms                                                 | 148 ms: 1.04x slower                                                   |
| regex_v8       | 15.1 ms                                                | 16.6 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.17 sec: 1.16x faster                                                 |
| unpickle_pure_python | 145 us                                                 | 128 us: 1.13x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 48.9 ms: 1.13x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 34.8 ms: 1.12x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 98.3 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 69.9 ms: 1.08x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 186 us: 1.06x faster                                                   |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.21 ms: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.3 ms: 1.09x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 14.9 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.7 ms: 1.15x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 27.2 ms: 1.12x faster                                                  |
| django_template | 19.7 ms                                                | 19.4 ms: 1.02x faster                                                  |
| mako            | 7.44 ms                                                | 7.35 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.7 ms: 2.75x faster                                                  |
| mdp                              | 1.49 sec                                               | 690 ms: 2.16x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 335 ms: 2.01x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 339 ms: 1.98x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 339 ms: 1.97x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 346 ms: 1.78x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 144 ms: 1.77x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 181 ms: 1.76x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.75x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 179 ms: 1.73x faster                                                   |
| generators                       | 29.4 ms                                                | 17.8 ms: 1.65x faster                                                  |
| deepcopy                         | 226 us                                                 | 142 us: 1.60x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 16.4 us: 1.58x faster                                                  |
| comprehensions                   | 14.0 us                                                | 10.2 us: 1.38x faster                                                  |
| go                               | 98.5 ms                                                | 72.6 ms: 1.36x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.50 us: 1.34x faster                                                  |
| coroutines                       | 19.7 ms                                                | 14.7 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 399 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 399 ms: 1.32x faster                                                   |
| raytrace                         | 204 ms                                                 | 155 ms: 1.31x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 131 ms: 1.28x faster                                                   |
| logging_silent                   | 72.5 ns                                                | 56.9 ns: 1.27x faster                                                  |
| float                            | 54.1 ms                                                | 43.2 ms: 1.25x faster                                                  |
| async_generators                 | 299 ms                                                 | 239 ms: 1.25x faster                                                   |
| dulwich_log                      | 29.2 ms                                                | 23.5 ms: 1.24x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.08 ms: 1.24x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 62.6 ms: 1.22x faster                                                  |
| logging_simple                   | 3.60 us                                                | 2.96 us: 1.22x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 62.9 ms: 1.21x faster                                                  |
| pylint                           | 182 ms                                                 | 151 ms: 1.20x faster                                                   |
| logging_format                   | 3.90 us                                                | 3.25 us: 1.20x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 71.8 ms: 1.20x faster                                                  |
| chaos                            | 41.6 ms                                                | 35.3 ms: 1.18x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 2.81 sec: 1.17x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 56.6 ms: 1.16x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.17 sec: 1.16x faster                                                 |
| hexiom                           | 4.38 ms                                                | 3.80 ms: 1.15x faster                                                  |
| genshi_text                      | 14.7 ms                                                | 12.7 ms: 1.15x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.50 sec: 1.15x faster                                                 |
| html5lib                         | 33.4 ms                                                | 29.1 ms: 1.15x faster                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 38.8 ms: 1.14x faster                                                  |
| nqueens                          | 59.5 ms                                                | 52.4 ms: 1.14x faster                                                  |
| unpickle_pure_python             | 145 us                                                 | 128 us: 1.13x faster                                                   |
| xml_etree_generate               | 55.4 ms                                                | 48.9 ms: 1.13x faster                                                  |
| pyflate                          | 311 ms                                                 | 276 ms: 1.13x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 55.0 ms: 1.13x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 27.2 ms: 1.12x faster                                                  |
| xml_etree_process                | 38.9 ms                                                | 34.8 ms: 1.12x faster                                                  |
| sympy_integrate                  | 11.1 ms                                                | 9.94 ms: 1.11x faster                                                  |
| 2to3                             | 168 ms                                                 | 151 ms: 1.11x faster                                                   |
| scimark_lu                       | 73.5 ms                                                | 66.1 ms: 1.11x faster                                                  |
| sphinx                           | 613 ms                                                 | 553 ms: 1.11x faster                                                   |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.84 ms: 1.11x faster                                                  |
| sympy_str                        | 144 ms                                                 | 130 ms: 1.10x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 98.3 ms: 1.10x faster                                                  |
| nbody                            | 67.6 ms                                                | 61.6 ms: 1.10x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 69.8 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 345 ms: 1.08x faster                                                   |
| scimark_fft                      | 194 ms                                                 | 180 ms: 1.08x faster                                                   |
| bench_mp_pool                    | 65.5 ms                                                | 60.6 ms: 1.08x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 69.9 ms: 1.08x faster                                                  |
| pycparser                        | 673 ms                                                 | 627 ms: 1.07x faster                                                   |
| pathlib                          | 24.7 ms                                                | 23.1 ms: 1.07x faster                                                  |
| richards_super                   | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.22 ms: 1.06x faster                                                  |
| sympy_expand                     | 233 ms                                                 | 220 ms: 1.06x faster                                                   |
| pprint_pformat                   | 986 ms                                                 | 931 ms: 1.06x faster                                                   |
| pickle_pure_python               | 197 us                                                 | 186 us: 1.06x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.38 sec: 1.06x faster                                                 |
| richards                         | 30.6 ms                                                | 29.0 ms: 1.05x faster                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 87.0 us: 1.05x faster                                                  |
| bench_thread_pool                | 483 us                                                 | 460 us: 1.05x faster                                                   |
| crypto_pyaes                     | 51.4 ms                                                | 49.3 ms: 1.04x faster                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 466 ms: 1.04x faster                                                   |
| regex_effbot                     | 2.44 ms                                                | 2.37 ms: 1.03x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.52 us: 1.02x faster                                                  |
| django_template                  | 19.7 ms                                                | 19.4 ms: 1.02x faster                                                  |
| mako                             | 7.44 ms                                                | 7.35 ms: 1.01x faster                                                  |
| shortest_path                    | 331 ms                                                 | 327 ms: 1.01x faster                                                   |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| meteor_contest                   | 69.1 ms                                                | 70.2 ms: 1.02x slower                                                  |
| regex_dna                        | 143 ms                                                 | 148 ms: 1.04x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.10 ms: 1.05x slower                                                  |
| many_optionals                   | 403 us                                                 | 429 us: 1.06x slower                                                   |
| python_startup                   | 17.8 ms                                                | 19.3 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 377 ms: 1.09x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 16.6 ms: 1.10x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.11x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 14.9 ms: 1.13x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 161 ms: 1.14x slower                                                   |
| telco                            | 3.92 ms                                                | 4.46 ms: 1.14x slower                                                  |
| coverage                         | 38.5 ms                                                | 44.7 ms: 1.16x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.21 ms: 1.17x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 122 ms: 2.59x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (3): connected_components, fannkuch, json
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.158x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.12x