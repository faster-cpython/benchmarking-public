# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.223x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x slower
- Memory change: 0.49x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 249 ms: 1.33x slower                                                  |
| docutils       | 1.44 sec                                               | 1.76 sec: 1.23x slower                                                |
| html5lib       | 36.6 ms                                                | 53.2 ms: 1.46x slower                                                 |
| tornado_http   | 75.8 ms                                                | 104 ms: 1.38x slower                                                  |
| Geometric mean | (ref)                                                  | 1.34x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 266 ms: 1.08x faster                                                  |
| async_tree_eager_io              | 514 ms                                                 | 490 ms: 1.05x faster                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 465 ms: 1.03x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 239 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 466 ms: 1.04x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 207 ms: 1.04x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 530 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 370 ms: 1.07x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 490 ms: 1.07x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 398 ms: 1.07x slower                                                  |
| async_tree_memoization           | 268 ms                                                 | 292 ms: 1.09x slower                                                  |
| async_tree_none                  | 215 ms                                                 | 235 ms: 1.09x slower                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 187 ms: 1.11x slower                                                  |
| async_generators                 | 295 ms                                                 | 332 ms: 1.13x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 162 ms: 1.17x slower                                                  |
| coroutines                       | 19.8 ms                                                | 24.7 ms: 1.25x slower                                                 |
| async_tree_eager                 | 70.1 ms                                                | 106 ms: 1.51x slower                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 75.5 ms: 1.58x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.10x slower                                                          |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 56.0 ms                                                | 93.0 ms: 1.66x slower                                                 |
| nbody          | 74.0 ms                                                | 154 ms: 2.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.51x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.51 ms: 1.05x faster                                                 |
| regex_dna      | 149 ms                                                 | 146 ms: 1.02x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                 |
| regex_compile  | 78.6 ms                                                | 119 ms: 1.52x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 73.6 ms                                                | 75.9 ms: 1.03x slower                                                 |
| json_loads           | 17.0 us                                                | 18.5 us: 1.09x slower                                                 |
| xml_etree_generate   | 57.0 ms                                                | 67.9 ms: 1.19x slower                                                 |
| json_dumps           | 6.52 ms                                                | 7.91 ms: 1.21x slower                                                 |
| tomli_loads          | 1.57 sec                                               | 1.99 sec: 1.27x slower                                                |
| xml_etree_process    | 41.0 ms                                                | 56.3 ms: 1.37x slower                                                 |
| unpickle_pure_python | 164 us                                                 | 262 us: 1.60x slower                                                  |
| pickle_pure_python   | 214 us                                                 | 346 us: 1.61x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.24x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 17.4 ms: 1.09x faster                                                 |
| python_startup_no_site | 14.5 ms                                                | 13.9 ms: 1.04x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 49.8 ms: 1.45x slower                                                 |
| genshi_text     | 16.9 ms                                                | 24.7 ms: 1.46x slower                                                 |
| django_template | 22.2 ms                                                | 36.1 ms: 1.63x slower                                                 |
| mako            | 7.68 ms                                                | 13.3 ms: 1.73x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.56x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize                | 189 ms                                                 | 103 ms: 1.84x faster                                                  |
| create_gc_cycles                 | 1.17 ms                                                | 679 us: 1.72x faster                                                  |
| gc_traversal                     | 2.91 ms                                                | 2.05 ms: 1.42x faster                                                 |
| bench_mp_pool                    | 62.5 ms                                                | 57.2 ms: 1.09x faster                                                 |
| python_startup                   | 18.9 ms                                                | 17.4 ms: 1.09x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 266 ms: 1.08x faster                                                  |
| async_tree_eager_io              | 514 ms                                                 | 490 ms: 1.05x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.51 ms: 1.05x faster                                                 |
| python_startup_no_site           | 14.5 ms                                                | 13.9 ms: 1.04x faster                                                 |
| xml_etree_parse                  | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 465 ms: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                 | 146 ms: 1.02x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 239 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                 |
| deepcopy                         | 237 us                                                 | 243 us: 1.03x slower                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 75.9 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 466 ms: 1.04x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 207 ms: 1.04x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 530 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 370 ms: 1.07x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 490 ms: 1.07x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 398 ms: 1.07x slower                                                  |
| pathlib                          | 23.4 ms                                                | 25.1 ms: 1.07x slower                                                 |
| async_tree_memoization           | 268 ms                                                 | 292 ms: 1.09x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.5 us: 1.09x slower                                                 |
| async_tree_none                  | 215 ms                                                 | 235 ms: 1.09x slower                                                  |
| json                             | 3.03 ms                                                | 3.33 ms: 1.10x slower                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 187 ms: 1.11x slower                                                  |
| generators                       | 31.5 ms                                                | 35.0 ms: 1.11x slower                                                 |
| deepcopy_memo                    | 27.4 us                                                | 30.6 us: 1.12x slower                                                 |
| async_generators                 | 295 ms                                                 | 332 ms: 1.13x slower                                                  |
| telco                            | 4.76 ms                                                | 5.42 ms: 1.14x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 162 ms: 1.17x slower                                                  |
| deepcopy_reduce                  | 2.07 us                                                | 2.45 us: 1.18x slower                                                 |
| coverage                         | 46.0 ms                                                | 54.4 ms: 1.18x slower                                                 |
| xml_etree_generate               | 57.0 ms                                                | 67.9 ms: 1.19x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 88.9 ms: 1.20x slower                                                 |
| pylint                           | 180 ms                                                 | 217 ms: 1.20x slower                                                  |
| json_dumps                       | 6.52 ms                                                | 7.91 ms: 1.21x slower                                                 |
| bpe_tokeniser                    | 3.25 sec                                               | 3.97 sec: 1.22x slower                                                |
| nqueens                          | 62.5 ms                                                | 76.4 ms: 1.22x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.76 sec: 1.23x slower                                                |
| fannkuch                         | 284 ms                                                 | 354 ms: 1.25x slower                                                  |
| coroutines                       | 19.8 ms                                                | 24.7 ms: 1.25x slower                                                 |
| mdp                              | 1.49 sec                                               | 1.88 sec: 1.26x slower                                                |
| tomli_loads                      | 1.57 sec                                               | 1.99 sec: 1.27x slower                                                |
| pycparser                        | 705 ms                                                 | 915 ms: 1.30x slower                                                  |
| scimark_fft                      | 201 ms                                                 | 266 ms: 1.33x slower                                                  |
| 2to3                             | 187 ms                                                 | 249 ms: 1.33x slower                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 4.07 ms: 1.36x slower                                                 |
| xml_etree_process                | 41.0 ms                                                | 56.3 ms: 1.37x slower                                                 |
| tornado_http                     | 75.8 ms                                                | 104 ms: 1.38x slower                                                  |
| pyflate                          | 351 ms                                                 | 490 ms: 1.39x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 142 us: 1.40x slower                                                  |
| thrift                           | 466 us                                                 | 667 us: 1.43x slower                                                  |
| crypto_pyaes                     | 54.2 ms                                                | 77.8 ms: 1.43x slower                                                 |
| dulwich_log                      | 28.5 ms                                                | 40.9 ms: 1.44x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 16.3 ms: 1.44x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 49.8 ms: 1.45x slower                                                 |
| html5lib                         | 36.6 ms                                                | 53.2 ms: 1.46x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 24.7 ms: 1.46x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 51.6 ms: 1.48x slower                                                 |
| async_tree_eager                 | 70.1 ms                                                | 106 ms: 1.51x slower                                                  |
| pprint_safe_repr                 | 533 ms                                                 | 810 ms: 1.52x slower                                                  |
| regex_compile                    | 78.6 ms                                                | 119 ms: 1.52x slower                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.65 sec: 1.52x slower                                                |
| comprehensions                   | 12.3 us                                                | 18.7 us: 1.53x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 78.4 ms: 1.56x slower                                                 |
| scimark_sor                      | 105 ms                                                 | 164 ms: 1.56x slower                                                  |
| spectral_norm                    | 76.3 ms                                                | 119 ms: 1.56x slower                                                  |
| go                               | 115 ms                                                 | 182 ms: 1.58x slower                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 75.5 ms: 1.58x slower                                                 |
| richards                         | 35.2 ms                                                | 55.6 ms: 1.58x slower                                                 |
| bench_thread_pool                | 505 us                                                 | 798 us: 1.58x slower                                                  |
| hexiom                           | 4.86 ms                                                | 7.74 ms: 1.59x slower                                                 |
| unpickle_pure_python             | 164 us                                                 | 262 us: 1.60x slower                                                  |
| sympy_str                        | 145 ms                                                 | 233 ms: 1.60x slower                                                  |
| pickle_pure_python               | 214 us                                                 | 346 us: 1.61x slower                                                  |
| django_template                  | 22.2 ms                                                | 36.1 ms: 1.63x slower                                                 |
| richards_super                   | 39.1 ms                                                | 64.7 ms: 1.65x slower                                                 |
| float                            | 56.0 ms                                                | 93.0 ms: 1.66x slower                                                 |
| logging_simple                   | 3.60 us                                                | 6.10 us: 1.69x slower                                                 |
| logging_format                   | 3.89 us                                                | 6.64 us: 1.70x slower                                                 |
| mako                             | 7.68 ms                                                | 13.3 ms: 1.73x slower                                                 |
| sympy_expand                     | 246 ms                                                 | 427 ms: 1.73x slower                                                  |
| chaos                            | 41.2 ms                                                | 74.7 ms: 1.81x slower                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.90 ms: 1.85x slower                                                 |
| sympy_sum                        | 75.4 ms                                                | 141 ms: 1.87x slower                                                  |
| scimark_lu                       | 76.7 ms                                                | 145 ms: 1.89x slower                                                  |
| sqlglot_parse                    | 856 us                                                 | 1.65 ms: 1.93x slower                                                 |
| logging_silent                   | 70.1 ns                                                | 136 ns: 1.94x slower                                                  |
| raytrace                         | 181 ms                                                 | 373 ms: 2.06x slower                                                  |
| nbody                            | 74.0 ms                                                | 154 ms: 2.08x slower                                                  |
| deltablue                        | 2.68 ms                                                | 5.61 ms: 2.10x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.29x slower                                                          |

Benchmark hidden because not significant (1): async_tree_io_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241005-3.14.0a0-16cd6cc-NOGIL/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.223x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.20x
- 99% likely to have a slowdown of 1.17x

# Memory
- memory change: 0.49x