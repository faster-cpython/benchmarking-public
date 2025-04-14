# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.081x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 167 ms: 1.01x faster                                                   |
| html5lib       | 33.4 ms                                                | 29.4 ms: 1.14x faster                                                  |
| sphinx         | 613 ms                                                 | 567 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 363 ms: 1.85x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 361 ms: 1.85x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 372 ms: 1.81x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.65x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 160 ms: 1.64x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 376 ms: 1.64x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.58x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 418 ms: 1.26x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.8 ms: 1.24x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 145 ms: 1.15x faster                                                   |
| async_generators                 | 299 ms                                                 | 271 ms: 1.10x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 364 ms: 1.03x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.23x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.79x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): async_tree_eager

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 46.8 ms: 1.16x faster                                                  |
| nbody          | 67.6 ms                                                | 65.0 ms: 1.04x faster                                                  |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 67.8 ms: 1.12x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.25 ms: 1.08x faster                                                  |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| regex_v8       | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.21 sec: 1.12x faster                                                 |
| unpickle_pure_python | 145 us                                                 | 130 us: 1.12x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 50.3 ms: 1.10x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 35.7 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 70.0 ms: 1.08x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| pickle_pure_python   | 197 us                                                 | 194 us: 1.01x faster                                                   |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.26 ms: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.0 ms: 1.07x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 14.1 ms: 1.07x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.48 ms: 1.15x faster                                                  |
| genshi_text     | 14.7 ms                                                | 13.5 ms: 1.08x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 29.0 ms: 1.05x faster                                                  |
| django_template | 19.7 ms                                                | 20.9 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.8 ms: 2.73x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 363 ms: 1.85x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 361 ms: 1.85x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 372 ms: 1.81x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.65x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 160 ms: 1.64x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 376 ms: 1.64x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.58x faster                                                   |
| deepcopy                         | 226 us                                                 | 149 us: 1.52x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 18.4 us: 1.42x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.57 us: 1.28x faster                                                  |
| generators                       | 29.4 ms                                                | 22.9 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 418 ms: 1.26x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.8 ms: 1.24x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 61.6 ms: 1.24x faster                                                  |
| go                               | 98.5 ms                                                | 80.6 ms: 1.22x faster                                                  |
| raytrace                         | 204 ms                                                 | 172 ms: 1.19x faster                                                   |
| float                            | 54.1 ms                                                | 46.8 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 145 ms: 1.15x faster                                                   |
| logging_simple                   | 3.60 us                                                | 3.14 us: 1.15x faster                                                  |
| mako                             | 7.44 ms                                                | 6.48 ms: 1.15x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 2.87 sec: 1.14x faster                                                 |
| pylint                           | 182 ms                                                 | 160 ms: 1.14x faster                                                   |
| html5lib                         | 33.4 ms                                                | 29.4 ms: 1.14x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.44 us: 1.13x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 172 ms: 1.13x faster                                                   |
| comprehensions                   | 14.0 us                                                | 12.5 us: 1.12x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 67.8 ms: 1.12x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.21 sec: 1.12x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 130 us: 1.12x faster                                                   |
| k_core                           | 1.72 sec                                               | 1.56 sec: 1.11x faster                                                 |
| async_generators                 | 299 ms                                                 | 271 ms: 1.10x faster                                                   |
| xml_etree_generate               | 55.4 ms                                                | 50.3 ms: 1.10x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 77.9 ms: 1.10x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 65.9 ns: 1.10x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 59.5 ms: 1.10x faster                                                  |
| pyflate                          | 311 ms                                                 | 283 ms: 1.10x faster                                                   |
| xml_etree_process                | 38.9 ms                                                | 35.7 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.89 ms: 1.09x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.36 ms: 1.09x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.25 ms: 1.08x faster                                                  |
| genshi_text                      | 14.7 ms                                                | 13.5 ms: 1.08x faster                                                  |
| sphinx                           | 613 ms                                                 | 567 ms: 1.08x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 70.0 ms: 1.08x faster                                                  |
| thrift                           | 468 us                                                 | 435 us: 1.08x faster                                                   |
| pathlib                          | 24.7 ms                                                | 23.1 ms: 1.07x faster                                                  |
| chaos                            | 41.6 ms                                                | 39.0 ms: 1.07x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 58.7 ms: 1.05x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 29.0 ms: 1.05x faster                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 42.5 ms: 1.05x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 28.1 ms: 1.04x faster                                                  |
| nbody                            | 67.6 ms                                                | 65.0 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 364 ms: 1.03x faster                                                   |
| sympy_sum                        | 76.2 ms                                                | 74.5 ms: 1.02x faster                                                  |
| sympy_str                        | 144 ms                                                 | 141 ms: 1.02x faster                                                   |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                                   |
| pickle_pure_python               | 197 us                                                 | 194 us: 1.01x faster                                                   |
| 2to3                             | 168 ms                                                 | 167 ms: 1.01x faster                                                   |
| sqlglot_optimize                 | 33.2 ms                                                | 33.1 ms: 1.01x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.00x faster                                                  |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                   |
| sqlglot_normalize                | 180 ms                                                 | 181 ms: 1.01x slower                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.66 ms: 1.01x slower                                                  |
| mdp                              | 1.49 sec                                               | 1.51 sec: 1.02x slower                                                 |
| connected_components             | 300 ms                                                 | 304 ms: 1.02x slower                                                   |
| sympy_expand                     | 233 ms                                                 | 238 ms: 1.02x slower                                                   |
| sqlglot_parse                    | 808 us                                                 | 826 us: 1.02x slower                                                   |
| sqlglot_transpile                | 973 us                                                 | 996 us: 1.02x slower                                                   |
| nqueens                          | 59.5 ms                                                | 61.2 ms: 1.03x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 498 us: 1.03x slower                                                   |
| hexiom                           | 4.38 ms                                                | 4.51 ms: 1.03x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 53.2 ms: 1.03x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                  |
| richards                         | 30.6 ms                                                | 31.7 ms: 1.04x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 95.1 us: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| shortest_path                    | 331 ms                                                 | 344 ms: 1.04x slower                                                   |
| richards_super                   | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.03 sec: 1.04x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 508 ms: 1.05x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.06x slower                                                  |
| django_template                  | 19.7 ms                                                | 20.9 ms: 1.06x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 73.4 ms: 1.06x slower                                                  |
| fannkuch                         | 250 ms                                                 | 266 ms: 1.06x slower                                                   |
| python_startup                   | 17.8 ms                                                | 19.0 ms: 1.07x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 14.1 ms: 1.07x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                  |
| many_optionals                   | 403 us                                                 | 448 us: 1.11x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.12x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| telco                            | 3.92 ms                                                | 4.48 ms: 1.14x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.26 ms: 1.17x slower                                                  |
| coverage                         | 38.5 ms                                                | 45.7 ms: 1.19x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.23x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.79x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (5): docutils, scimark_lu, pycparser, json, async_tree_eager
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.081x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.11x