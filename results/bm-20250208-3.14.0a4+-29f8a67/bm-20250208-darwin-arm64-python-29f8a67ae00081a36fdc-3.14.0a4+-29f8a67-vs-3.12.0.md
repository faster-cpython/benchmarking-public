# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.089x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 163 ms: 1.03x faster                                                   |
| docutils       | 1.45 sec                                               | 1.41 sec: 1.03x faster                                                 |
| html5lib       | 33.4 ms                                                | 29.2 ms: 1.14x faster                                                  |
| sphinx         | 613 ms                                                 | 566 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 362 ms: 1.84x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 366 ms: 1.84x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 381 ms: 1.76x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.64x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 377 ms: 1.64x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.58x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 417 ms: 1.27x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.9 ms: 1.24x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| async_generators                 | 299 ms                                                 | 252 ms: 1.18x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 62.6 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 393 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.24x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 132 ms: 2.81x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 46.9 ms: 1.15x faster                                                  |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| nbody          | 67.6 ms                                                | 71.1 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 67.1 ms: 1.13x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.36 ms: 1.03x faster                                                  |
| regex_dna      | 143 ms                                                 | 144 ms: 1.01x slower                                                   |
| regex_v8       | 15.1 ms                                                | 17.1 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.20 sec: 1.13x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 70.4 ms: 1.07x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 53.4 ms: 1.04x faster                                                  |
| unpickle_pure_python | 145 us                                                 | 143 us: 1.02x faster                                                   |
| xml_etree_process    | 38.9 ms                                                | 38.6 ms: 1.01x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 199 us: 1.01x slower                                                   |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.29 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                  |
| python_startup         | 17.8 ms                                                | 18.6 ms: 1.05x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 13.5 ms: 1.08x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 28.4 ms: 1.08x faster                                                  |
| mako            | 7.44 ms                                                | 7.37 ms: 1.01x faster                                                  |
| django_template | 19.7 ms                                                | 20.8 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.8 ms: 2.73x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 362 ms: 1.84x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 366 ms: 1.84x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 381 ms: 1.76x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.64x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 377 ms: 1.64x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.58x faster                                                   |
| deepcopy                         | 226 us                                                 | 148 us: 1.52x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 18.4 us: 1.41x faster                                                  |
| generators                       | 29.4 ms                                                | 22.9 ms: 1.28x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.58 us: 1.27x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 417 ms: 1.27x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 61.0 ms: 1.25x faster                                                  |
| coroutines                       | 19.7 ms                                                | 15.9 ms: 1.24x faster                                                  |
| go                               | 98.5 ms                                                | 79.6 ms: 1.24x faster                                                  |
| raytrace                         | 204 ms                                                 | 171 ms: 1.19x faster                                                   |
| comprehensions                   | 14.0 us                                                | 11.8 us: 1.19x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| async_generators                 | 299 ms                                                 | 252 ms: 1.18x faster                                                   |
| float                            | 54.1 ms                                                | 46.9 ms: 1.15x faster                                                  |
| pylint                           | 182 ms                                                 | 159 ms: 1.15x faster                                                   |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.75 ms: 1.14x faster                                                  |
| html5lib                         | 33.4 ms                                                | 29.2 ms: 1.14x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.51 sec: 1.14x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 2.89 sec: 1.14x faster                                                 |
| scimark_fft                      | 194 ms                                                 | 172 ms: 1.13x faster                                                   |
| regex_compile                    | 75.9 ms                                                | 67.1 ms: 1.13x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.19 us: 1.13x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.20 sec: 1.13x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.49 us: 1.12x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 59.2 ms: 1.11x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 65.9 ns: 1.10x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 78.1 ms: 1.10x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.34 ms: 1.10x faster                                                  |
| genshi_text                      | 14.7 ms                                                | 13.5 ms: 1.08x faster                                                  |
| sphinx                           | 613 ms                                                 | 566 ms: 1.08x faster                                                   |
| pyflate                          | 311 ms                                                 | 288 ms: 1.08x faster                                                   |
| pathlib                          | 24.7 ms                                                | 22.9 ms: 1.08x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 28.4 ms: 1.08x faster                                                  |
| thrift                           | 468 us                                                 | 436 us: 1.07x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 70.4 ms: 1.07x faster                                                  |
| chaos                            | 41.6 ms                                                | 38.9 ms: 1.07x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 27.3 ms: 1.07x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 58.1 ms: 1.07x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| sqlglot_transpile                | 973 us                                                 | 919 us: 1.06x faster                                                   |
| pprint_pformat                   | 986 ms                                                 | 931 ms: 1.06x faster                                                   |
| sqlglot_parse                    | 808 us                                                 | 763 us: 1.06x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 62.6 ms: 1.05x faster                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 462 ms: 1.05x faster                                                   |
| sympy_sum                        | 76.2 ms                                                | 73.1 ms: 1.04x faster                                                  |
| sympy_str                        | 144 ms                                                 | 138 ms: 1.04x faster                                                   |
| pycparser                        | 673 ms                                                 | 647 ms: 1.04x faster                                                   |
| scimark_monte_carlo              | 44.5 ms                                                | 42.7 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                   |
| xml_etree_generate               | 55.4 ms                                                | 53.4 ms: 1.04x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.36 ms: 1.03x faster                                                  |
| 2to3                             | 168 ms                                                 | 163 ms: 1.03x faster                                                   |
| sqlglot_optimize                 | 33.2 ms                                                | 32.2 ms: 1.03x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.41 sec: 1.03x faster                                                 |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.43 ms: 1.03x faster                                                  |
| nqueens                          | 59.5 ms                                                | 58.3 ms: 1.02x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.52 us: 1.02x faster                                                  |
| shortest_path                    | 331 ms                                                 | 325 ms: 1.02x faster                                                   |
| unpickle_pure_python             | 145 us                                                 | 143 us: 1.02x faster                                                   |
| hexiom                           | 4.38 ms                                                | 4.31 ms: 1.02x faster                                                  |
| sqlglot_normalize                | 180 ms                                                 | 177 ms: 1.01x faster                                                   |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                   |
| mako                             | 7.44 ms                                                | 7.37 ms: 1.01x faster                                                  |
| mdp                              | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                 |
| connected_components             | 300 ms                                                 | 297 ms: 1.01x faster                                                   |
| xml_etree_process                | 38.9 ms                                                | 38.6 ms: 1.01x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 73.0 ms: 1.01x faster                                                  |
| sympy_expand                     | 233 ms                                                 | 232 ms: 1.01x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| sympy_integrate                  | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 92.4 us: 1.01x slower                                                  |
| regex_dna                        | 143 ms                                                 | 144 ms: 1.01x slower                                                   |
| pickle_pure_python               | 197 us                                                 | 199 us: 1.01x slower                                                   |
| fannkuch                         | 250 ms                                                 | 254 ms: 1.01x slower                                                   |
| bench_thread_pool                | 483 us                                                 | 491 us: 1.02x slower                                                   |
| meteor_contest                   | 69.1 ms                                                | 70.3 ms: 1.02x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 52.5 ms: 1.02x slower                                                  |
| richards_super                   | 34.6 ms                                                | 35.9 ms: 1.04x slower                                                  |
| richards                         | 30.6 ms                                                | 31.7 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                  |
| python_startup                   | 17.8 ms                                                | 18.6 ms: 1.05x slower                                                  |
| nbody                            | 67.6 ms                                                | 71.1 ms: 1.05x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.05x slower                                                  |
| django_template                  | 19.7 ms                                                | 20.8 ms: 1.06x slower                                                  |
| many_optionals                   | 403 us                                                 | 432 us: 1.07x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 393 ms: 1.13x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 17.1 ms: 1.14x slower                                                  |
| telco                            | 3.92 ms                                                | 4.55 ms: 1.16x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.29 ms: 1.18x slower                                                  |
| coverage                         | 38.5 ms                                                | 46.0 ms: 1.20x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.24x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 132 ms: 2.81x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (1): json
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.089x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.13x