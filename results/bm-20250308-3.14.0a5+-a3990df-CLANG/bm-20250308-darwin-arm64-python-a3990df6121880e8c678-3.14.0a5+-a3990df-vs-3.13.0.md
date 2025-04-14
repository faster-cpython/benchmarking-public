# Results vs. 3.13.0

- fork: python
- ref: a3990df6121880e8c678
- machine: darwin-arm64
- commit hash: a3990df
- commit date: 2025-03-08
- overall geometric mean: 1.158x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 150 ms: 1.19x faster                                                   |
| docutils       | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                 |
| html5lib       | 36.7 ms                                                | 29.0 ms: 1.27x faster                                                  |
| sphinx         | 602 ms                                                 | 540 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 184 ms: 1.57x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 331 ms: 1.54x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 337 ms: 1.48x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 343 ms: 1.48x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 182 ms: 1.47x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 149 ms: 1.42x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 143 ms: 1.39x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 345 ms: 1.39x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.0 ms: 1.34x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 131 ms: 1.28x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 55.7 ms: 1.26x faster                                                  |
| async_generators                 | 294 ms                                                 | 235 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 409 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 400 ms: 1.12x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 343 ms: 1.09x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 121 ms: 2.55x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 44.0 ms: 1.27x faster                                                  |
| nbody          | 73.6 ms                                                | 63.7 ms: 1.16x faster                                                  |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 62.1 ms: 1.26x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                  |
| regex_dna      | 149 ms                                                 | 145 ms: 1.02x faster                                                   |
| regex_v8       | 17.0 ms                                                | 17.6 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.14 sec: 1.38x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 123 us: 1.35x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 33.3 ms: 1.24x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 48.1 ms: 1.19x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 184 us: 1.17x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 68.8 ms: 1.08x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.13 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.4 ms: 1.03x slower                                                  |
| python_startup_no_site | 13.7 ms                                                | 15.0 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.5 ms: 1.35x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 26.7 ms: 1.27x faster                                                  |
| mako            | 7.75 ms                                                | 7.10 ms: 1.09x faster                                                  |
| django_template | 20.5 ms                                                | 18.8 ms: 1.09x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators                       | 31.9 ms                                                | 18.0 ms: 1.77x faster                                                  |
| deepcopy                         | 236 us                                                 | 138 us: 1.71x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 16.3 us: 1.68x faster                                                  |
| go                               | 117 ms                                                 | 70.5 ms: 1.66x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 184 ms: 1.57x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 331 ms: 1.54x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 337 ms: 1.48x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 343 ms: 1.48x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 182 ms: 1.47x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 74.3 ms: 1.42x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.47 us: 1.42x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 149 ms: 1.42x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 143 ms: 1.39x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 345 ms: 1.39x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.14 sec: 1.38x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 12.5 ms: 1.35x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 123 us: 1.35x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.0 ms: 1.34x faster                                                  |
| richards                         | 36.2 ms                                                | 27.8 ms: 1.30x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.05 ms: 1.29x faster                                                  |
| hexiom                           | 4.87 ms                                                | 3.79 ms: 1.28x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 131 ms: 1.28x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 39.4 ms: 1.28x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 26.7 ms: 1.27x faster                                                  |
| float                            | 55.8 ms                                                | 44.0 ms: 1.27x faster                                                  |
| html5lib                         | 36.7 ms                                                | 29.0 ms: 1.27x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 62.1 ms: 1.26x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 55.7 ms: 1.26x faster                                                  |
| richards_super                   | 39.2 ms                                                | 31.4 ms: 1.25x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 23.0 ms: 1.25x faster                                                  |
| async_generators                 | 294 ms                                                 | 235 ms: 1.25x faster                                                   |
| pprint_pformat                   | 1.10 sec                                               | 882 ms: 1.25x faster                                                   |
| xml_etree_process                | 41.3 ms                                                | 33.3 ms: 1.24x faster                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 843 us: 1.23x faster                                                   |
| comprehensions                   | 12.0 us                                                | 9.76 us: 1.23x faster                                                  |
| sqlglot_parse                    | 852 us                                                 | 696 us: 1.22x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 443 ms: 1.22x faster                                                   |
| nqueens                          | 61.8 ms                                                | 50.8 ms: 1.22x faster                                                  |
| pylint                           | 180 ms                                                 | 149 ms: 1.21x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 83.4 us: 1.21x faster                                                  |
| logging_simple                   | 3.56 us                                                | 2.95 us: 1.21x faster                                                  |
| logging_silent                   | 71.0 ns                                                | 59.2 ns: 1.20x faster                                                  |
| 2to3                             | 179 ms                                                 | 150 ms: 1.19x faster                                                   |
| pyflate                          | 352 ms                                                 | 295 ms: 1.19x faster                                                   |
| logging_format                   | 3.85 us                                                | 3.24 us: 1.19x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 48.1 ms: 1.19x faster                                                  |
| chaos                            | 41.1 ms                                                | 34.9 ms: 1.18x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 184 us: 1.17x faster                                                   |
| sqlglot_optimize                 | 34.7 ms                                                | 29.8 ms: 1.16x faster                                                  |
| sqlglot_normalize                | 188 ms                                                 | 163 ms: 1.16x faster                                                   |
| nbody                            | 73.6 ms                                                | 63.7 ms: 1.16x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.83 sec: 1.15x faster                                                 |
| scimark_fft                      | 200 ms                                                 | 174 ms: 1.15x faster                                                   |
| sympy_expand                     | 248 ms                                                 | 216 ms: 1.15x faster                                                   |
| thrift                           | 466 us                                                 | 407 us: 1.14x faster                                                   |
| sympy_str                        | 146 ms                                                 | 128 ms: 1.14x faster                                                   |
| pycparser                        | 701 ms                                                 | 617 ms: 1.14x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 67.9 ms: 1.13x faster                                                  |
| raytrace                         | 181 ms                                                 | 161 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 409 ms: 1.12x faster                                                   |
| crypto_pyaes                     | 55.3 ms                                                | 49.3 ms: 1.12x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 400 ms: 1.12x faster                                                   |
| sphinx                           | 602 ms                                                 | 540 ms: 1.12x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 10.1 ms: 1.11x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 454 us: 1.11x faster                                                   |
| telco                            | 4.84 ms                                                | 4.38 ms: 1.11x faster                                                  |
| fannkuch                         | 279 ms                                                 | 254 ms: 1.10x faster                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.10 ms: 1.10x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 69.2 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.73 ms: 1.09x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.47 sec: 1.09x faster                                                 |
| mako                             | 7.75 ms                                                | 7.10 ms: 1.09x faster                                                  |
| django_template                  | 20.5 ms                                                | 18.8 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 343 ms: 1.09x faster                                                   |
| connected_components             | 319 ms                                                 | 293 ms: 1.09x faster                                                   |
| sympy_sum                        | 75.1 ms                                                | 69.2 ms: 1.08x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 54.5 ms: 1.08x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 68.8 ms: 1.08x faster                                                  |
| shortest_path                    | 345 ms                                                 | 320 ms: 1.08x faster                                                   |
| meteor_contest                   | 74.0 ms                                                | 68.8 ms: 1.07x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 60.4 ms: 1.07x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| mdp                              | 1.50 sec                                               | 1.42 sec: 1.05x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.50 us: 1.04x faster                                                  |
| coverage                         | 46.2 ms                                                | 44.8 ms: 1.03x faster                                                  |
| pathlib                          | 23.2 ms                                                | 22.6 ms: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.02x faster                                                   |
| json                             | 3.04 ms                                                | 3.00 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| dask                             | 771 ms                                                 | 767 ms: 1.01x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| many_optionals                   | 409 us                                                 | 418 us: 1.02x slower                                                   |
| python_startup                   | 18.8 ms                                                | 19.4 ms: 1.03x slower                                                  |
| regex_v8                         | 17.0 ms                                                | 17.6 ms: 1.03x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.07 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.26 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                   |
| python_startup_no_site           | 13.7 ms                                                | 15.0 ms: 1.09x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.13 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                   |
| subparsers                       | 9.44 ms                                                | 11.3 ms: 1.20x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 121 ms: 2.55x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.158x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.08x