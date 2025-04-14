# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: darwin-arm64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.067x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 164 ms: 1.09x faster                                                   |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                 |
| html5lib       | 36.7 ms                                                | 31.7 ms: 1.16x faster                                                  |
| sphinx         | 602 ms                                                 | 586 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 195 ms: 1.48x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 360 ms: 1.42x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 362 ms: 1.38x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 369 ms: 1.38x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 196 ms: 1.36x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.32x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 153 ms: 1.29x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 371 ms: 1.29x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.6 ms: 1.28x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 144 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 412 ms: 1.12x faster                                                   |
| async_generators                 | 294 ms                                                 | 271 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.08x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 65.7 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 174 ms: 1.26x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.75x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 45.5 ms: 1.23x faster                                                  |
| nbody          | 73.6 ms                                                | 63.9 ms: 1.15x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.24 ms: 1.17x faster                                                  |
| regex_compile  | 78.3 ms                                                | 67.5 ms: 1.16x faster                                                  |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.21 sec: 1.30x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 130 us: 1.27x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 35.4 ms: 1.17x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 49.6 ms: 1.15x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 191 us: 1.12x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 69.4 ms: 1.07x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.10 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 12.1 ms: 1.13x faster                                                  |
| python_startup         | 18.8 ms                                                | 16.6 ms: 1.13x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 6.39 ms: 1.21x faster                                                  |
| genshi_text     | 16.9 ms                                                | 15.6 ms: 1.09x faster                                                  |
| django_template | 20.5 ms                                                | 22.2 ms: 1.08x slower                                                  |
| genshi_xml      | 34.1 ms                                                | 40.2 ms: 1.18x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 17.7 us: 1.55x faster                                                  |
| deepcopy                         | 236 us                                                 | 159 us: 1.49x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 195 ms: 1.48x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 360 ms: 1.42x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 362 ms: 1.38x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 369 ms: 1.38x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 196 ms: 1.36x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.57 us: 1.33x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.32x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.21 sec: 1.30x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 153 ms: 1.29x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 371 ms: 1.29x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.6 ms: 1.28x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 130 us: 1.27x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 83.9 ms: 1.26x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 61.9 ms: 1.24x faster                                                  |
| float                            | 55.8 ms                                                | 45.5 ms: 1.23x faster                                                  |
| mako                             | 7.75 ms                                                | 6.39 ms: 1.21x faster                                                  |
| go                               | 117 ms                                                 | 97.5 ms: 1.20x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.24 ms: 1.17x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 35.4 ms: 1.17x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 144 ms: 1.16x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 67.5 ms: 1.16x faster                                                  |
| html5lib                         | 36.7 ms                                                | 31.7 ms: 1.16x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 173 ms: 1.16x faster                                                   |
| nbody                            | 73.6 ms                                                | 63.9 ms: 1.15x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 49.6 ms: 1.15x faster                                                  |
| generators                       | 31.9 ms                                                | 27.8 ms: 1.15x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.85 sec: 1.14x faster                                                 |
| pyflate                          | 352 ms                                                 | 308 ms: 1.14x faster                                                   |
| python_startup_no_site           | 13.7 ms                                                | 12.1 ms: 1.13x faster                                                  |
| python_startup                   | 18.8 ms                                                | 16.6 ms: 1.13x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 191 us: 1.12x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 412 ms: 1.12x faster                                                   |
| bench_mp_pool                    | 64.7 ms                                                | 58.1 ms: 1.11x faster                                                  |
| pylint                           | 180 ms                                                 | 163 ms: 1.10x faster                                                   |
| 2to3                             | 179 ms                                                 | 164 ms: 1.09x faster                                                   |
| scimark_lu                       | 75.9 ms                                                | 69.7 ms: 1.09x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 46.3 ms: 1.09x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 15.6 ms: 1.09x faster                                                  |
| async_generators                 | 294 ms                                                 | 271 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.08x faster                                                   |
| telco                            | 4.84 ms                                                | 4.51 ms: 1.07x faster                                                  |
| connected_components             | 319 ms                                                 | 297 ms: 1.07x faster                                                   |
| pprint_pformat                   | 1.10 sec                                               | 1.03 sec: 1.07x faster                                                 |
| thrift                           | 466 us                                                 | 436 us: 1.07x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 69.4 ms: 1.07x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 65.7 ms: 1.06x faster                                                  |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 510 ms: 1.06x faster                                                   |
| deltablue                        | 2.65 ms                                                | 2.50 ms: 1.06x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 95.7 us: 1.05x faster                                                  |
| richards                         | 36.2 ms                                                | 34.4 ms: 1.05x faster                                                  |
| shortest_path                    | 345 ms                                                 | 328 ms: 1.05x faster                                                   |
| pathlib                          | 23.2 ms                                                | 22.1 ms: 1.05x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 52.7 ms: 1.05x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 237 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                   |
| logging_simple                   | 3.56 us                                                | 3.45 us: 1.03x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.74 us: 1.03x faster                                                  |
| json                             | 3.04 ms                                                | 2.95 ms: 1.03x faster                                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 33.7 ms: 1.03x faster                                                  |
| sphinx                           | 602 ms                                                 | 586 ms: 1.03x faster                                                   |
| sympy_str                        | 146 ms                                                 | 142 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.92 ms: 1.02x faster                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 1.02 ms: 1.02x faster                                                  |
| richards_super                   | 39.2 ms                                                | 38.4 ms: 1.02x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| sqlglot_normalize                | 188 ms                                                 | 185 ms: 1.02x faster                                                   |
| sqlalchemy_declarative           | 59.0 ms                                                | 58.3 ms: 1.01x faster                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.64 ms: 1.01x faster                                                  |
| sqlglot_parse                    | 852 us                                                 | 844 us: 1.01x faster                                                   |
| meteor_contest                   | 74.0 ms                                                | 73.5 ms: 1.01x faster                                                  |
| dask                             | 771 ms                                                 | 767 ms: 1.01x faster                                                   |
| sympy_sum                        | 75.1 ms                                                | 74.6 ms: 1.01x faster                                                  |
| coverage                         | 46.2 ms                                                | 46.0 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.00x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 28.6 ms: 1.00x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 505 us: 1.00x slower                                                   |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                 |
| chaos                            | 41.1 ms                                                | 41.7 ms: 1.01x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.01x slower                                                  |
| nqueens                          | 61.8 ms                                                | 63.2 ms: 1.02x slower                                                  |
| mdp                              | 1.50 sec                                               | 1.55 sec: 1.04x slower                                                 |
| raytrace                         | 181 ms                                                 | 188 ms: 1.04x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| hexiom                           | 4.87 ms                                                | 5.05 ms: 1.04x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.11 ms: 1.06x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.07x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 76.3 ns: 1.07x slower                                                  |
| django_template                  | 20.5 ms                                                | 22.2 ms: 1.08x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.10 ms: 1.10x slower                                                  |
| many_optionals                   | 409 us                                                 | 457 us: 1.12x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                                   |
| comprehensions                   | 12.0 us                                                | 13.8 us: 1.16x slower                                                  |
| genshi_xml                       | 34.1 ms                                                | 40.2 ms: 1.18x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 174 ms: 1.26x slower                                                   |
| subparsers                       | 9.44 ms                                                | 12.2 ms: 1.29x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.75x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (4): pycparser, asyncio_websockets, fannkuch, pidigits
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.067x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.09x