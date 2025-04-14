# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: darwin-arm64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.064x faster
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 164 ms: 1.03x faster                                                   |
| html5lib       | 33.4 ms                                                | 31.7 ms: 1.05x faster                                                  |
| sphinx         | 613 ms                                                 | 586 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 362 ms: 1.86x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 360 ms: 1.85x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 369 ms: 1.82x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 153 ms: 1.67x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 371 ms: 1.66x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.64x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 195 ms: 1.64x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.58x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 412 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.6 ms: 1.26x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 144 ms: 1.16x faster                                                   |
| async_generators                 | 299 ms                                                 | 271 ms: 1.10x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 174 ms: 1.22x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.78x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): async_tree_eager

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 45.5 ms: 1.19x faster                                                  |
| nbody          | 67.6 ms                                                | 63.9 ms: 1.06x faster                                                  |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 67.5 ms: 1.12x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                  |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| regex_v8       | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.21 sec: 1.12x faster                                                 |
| unpickle_pure_python | 145 us                                                 | 130 us: 1.12x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 49.6 ms: 1.12x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 35.4 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 69.4 ms: 1.09x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| pickle_pure_python   | 197 us                                                 | 191 us: 1.03x faster                                                   |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.10 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 12.1 ms: 1.09x faster                                                  |
| python_startup         | 17.8 ms                                                | 16.6 ms: 1.07x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.39 ms: 1.16x faster                                                  |
| genshi_text     | 14.7 ms                                                | 15.6 ms: 1.06x slower                                                  |
| django_template | 19.7 ms                                                | 22.2 ms: 1.13x slower                                                  |
| genshi_xml      | 30.5 ms                                                | 40.2 ms: 1.32x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.2 ms: 2.63x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 362 ms: 1.86x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 360 ms: 1.85x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 369 ms: 1.82x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 153 ms: 1.67x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 371 ms: 1.66x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.64x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 195 ms: 1.64x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.58x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 17.7 us: 1.47x faster                                                  |
| deepcopy                         | 226 us                                                 | 159 us: 1.42x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.57 us: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 412 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.6 ms: 1.26x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 61.9 ms: 1.24x faster                                                  |
| float                            | 54.1 ms                                                | 45.5 ms: 1.19x faster                                                  |
| mako                             | 7.44 ms                                                | 6.39 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 144 ms: 1.16x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 2.85 sec: 1.15x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 58.1 ms: 1.13x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 173 ms: 1.13x faster                                                   |
| regex_compile                    | 75.9 ms                                                | 67.5 ms: 1.12x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.21 sec: 1.12x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 130 us: 1.12x faster                                                   |
| pathlib                          | 24.7 ms                                                | 22.1 ms: 1.12x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 49.6 ms: 1.12x faster                                                  |
| pylint                           | 182 ms                                                 | 163 ms: 1.11x faster                                                   |
| async_generators                 | 299 ms                                                 | 271 ms: 1.10x faster                                                   |
| xml_etree_process                | 38.9 ms                                                | 35.4 ms: 1.10x faster                                                  |
| python_startup_no_site           | 13.2 ms                                                | 12.1 ms: 1.09x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 69.4 ms: 1.09x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                  |
| raytrace                         | 204 ms                                                 | 188 ms: 1.09x faster                                                   |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.92 ms: 1.08x faster                                                  |
| thrift                           | 468 us                                                 | 436 us: 1.07x faster                                                   |
| python_startup                   | 17.8 ms                                                | 16.6 ms: 1.07x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 58.3 ms: 1.06x faster                                                  |
| nbody                            | 67.6 ms                                                | 63.9 ms: 1.06x faster                                                  |
| generators                       | 29.4 ms                                                | 27.8 ms: 1.06x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 69.7 ms: 1.05x faster                                                  |
| html5lib                         | 33.4 ms                                                | 31.7 ms: 1.05x faster                                                  |
| sphinx                           | 613 ms                                                 | 586 ms: 1.05x faster                                                   |
| logging_simple                   | 3.60 us                                                | 3.45 us: 1.05x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.74 us: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                   |
| pickle_pure_python               | 197 us                                                 | 191 us: 1.03x faster                                                   |
| deltablue                        | 2.57 ms                                                | 2.50 ms: 1.03x faster                                                  |
| 2to3                             | 168 ms                                                 | 164 ms: 1.03x faster                                                   |
| scimark_sor                      | 85.8 ms                                                | 83.9 ms: 1.02x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 28.6 ms: 1.02x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 74.6 ms: 1.02x faster                                                  |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| json                             | 3.00 ms                                                | 2.95 ms: 1.02x faster                                                  |
| dask                             | 779 ms                                                 | 767 ms: 1.02x faster                                                   |
| sympy_str                        | 144 ms                                                 | 142 ms: 1.01x faster                                                   |
| comprehensions                   | 14.0 us                                                | 13.8 us: 1.01x faster                                                  |
| pyflate                          | 311 ms                                                 | 308 ms: 1.01x faster                                                   |
| go                               | 98.5 ms                                                | 97.5 ms: 1.01x faster                                                  |
| connected_components             | 300 ms                                                 | 297 ms: 1.01x faster                                                   |
| shortest_path                    | 331 ms                                                 | 328 ms: 1.01x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.64 ms: 1.01x slower                                                  |
| sqlglot_optimize                 | 33.2 ms                                                | 33.7 ms: 1.02x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 237 ms: 1.02x slower                                                   |
| crypto_pyaes                     | 51.4 ms                                                | 52.7 ms: 1.02x slower                                                  |
| sqlglot_normalize                | 180 ms                                                 | 185 ms: 1.03x slower                                                   |
| pycparser                        | 673 ms                                                 | 697 ms: 1.04x slower                                                   |
| sympy_integrate                  | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| mdp                              | 1.49 sec                                               | 1.55 sec: 1.04x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 46.3 ms: 1.04x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.03 sec: 1.04x slower                                                 |
| sqlglot_transpile                | 973 us                                                 | 1.02 ms: 1.04x slower                                                  |
| sqlglot_parse                    | 808 us                                                 | 844 us: 1.04x slower                                                   |
| typing_runtime_protocols         | 91.5 us                                                | 95.7 us: 1.05x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 505 us: 1.05x slower                                                   |
| logging_silent                   | 72.5 ns                                                | 76.3 ns: 1.05x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 510 ms: 1.05x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.06x slower                                                  |
| nqueens                          | 59.5 ms                                                | 63.2 ms: 1.06x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 15.6 ms: 1.06x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 73.5 ms: 1.06x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                  |
| richards_super                   | 34.6 ms                                                | 38.4 ms: 1.11x slower                                                  |
| fannkuch                         | 250 ms                                                 | 278 ms: 1.11x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                                   |
| richards                         | 30.6 ms                                                | 34.4 ms: 1.12x slower                                                  |
| django_template                  | 19.7 ms                                                | 22.2 ms: 1.13x slower                                                  |
| many_optionals                   | 403 us                                                 | 457 us: 1.13x slower                                                   |
| json_dumps                       | 6.19 ms                                                | 7.10 ms: 1.15x slower                                                  |
| telco                            | 3.92 ms                                                | 4.51 ms: 1.15x slower                                                  |
| hexiom                           | 4.38 ms                                                | 5.05 ms: 1.15x slower                                                  |
| coverage                         | 38.5 ms                                                | 46.0 ms: 1.19x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 174 ms: 1.22x slower                                                   |
| genshi_xml                       | 30.5 ms                                                | 40.2 ms: 1.32x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.78x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (4): async_tree_eager, docutils, sqlite_synth, chaos
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 99.78% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x