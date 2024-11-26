# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.224x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x slower
- Memory change: 0.71x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 246 ms: 1.32x slower                                                  |
| docutils       | 1.44 sec                                               | 1.75 sec: 1.22x slower                                                |
| html5lib       | 36.6 ms                                                | 51.2 ms: 1.40x slower                                                 |
| tornado_http   | 75.8 ms                                                | 127 ms: 1.67x slower                                                  |
| Geometric mean | (ref)                                                  | 1.39x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 263 ms: 1.09x faster                                                  |
| async_tree_eager_io              | 514 ms                                                 | 484 ms: 1.06x faster                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 464 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 525 ms: 1.04x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 206 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 485 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 367 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 395 ms: 1.06x slower                                                  |
| async_tree_memoization           | 268 ms                                                 | 288 ms: 1.07x slower                                                  |
| async_tree_none                  | 215 ms                                                 | 233 ms: 1.08x slower                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 184 ms: 1.09x slower                                                  |
| async_generators                 | 295 ms                                                 | 331 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 159 ms: 1.15x slower                                                  |
| coroutines                       | 19.8 ms                                                | 25.0 ms: 1.27x slower                                                 |
| async_tree_eager                 | 70.1 ms                                                | 106 ms: 1.52x slower                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 74.9 ms: 1.57x slower                                                 |
| asyncio_websockets               | 242 ms                                                 | 405 ms: 1.67x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.12x slower                                                          |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 56.0 ms                                                | 93.8 ms: 1.67x slower                                                 |
| nbody          | 74.0 ms                                                | 154 ms: 2.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.51x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.44 ms: 1.08x faster                                                 |
| regex_dna      | 149 ms                                                 | 139 ms: 1.08x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.1 ms: 1.01x slower                                                 |
| regex_compile  | 78.6 ms                                                | 119 ms: 1.52x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 73.6 ms                                                | 75.6 ms: 1.03x slower                                                 |
| json_loads           | 17.0 us                                                | 18.8 us: 1.11x slower                                                 |
| json_dumps           | 6.52 ms                                                | 7.74 ms: 1.19x slower                                                 |
| xml_etree_generate   | 57.0 ms                                                | 68.1 ms: 1.20x slower                                                 |
| tomli_loads          | 1.57 sec                                               | 1.99 sec: 1.27x slower                                                |
| xml_etree_process    | 41.0 ms                                                | 57.2 ms: 1.40x slower                                                 |
| unpickle_pure_python | 164 us                                                 | 262 us: 1.60x slower                                                  |
| pickle_pure_python   | 214 us                                                 | 346 us: 1.61x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.25x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 17.0 ms: 1.11x faster                                                 |
| python_startup_no_site | 14.5 ms                                                | 13.6 ms: 1.07x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 49.6 ms: 1.44x slower                                                 |
| genshi_text     | 16.9 ms                                                | 24.9 ms: 1.48x slower                                                 |
| django_template | 22.2 ms                                                | 35.3 ms: 1.59x slower                                                 |
| mako            | 7.68 ms                                                | 13.3 ms: 1.73x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.56x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize                | 189 ms                                                 | 102 ms: 1.85x faster                                                  |
| create_gc_cycles                 | 1.17 ms                                                | 686 us: 1.70x faster                                                  |
| gc_traversal                     | 2.91 ms                                                | 2.05 ms: 1.42x faster                                                 |
| bench_mp_pool                    | 62.5 ms                                                | 54.9 ms: 1.14x faster                                                 |
| python_startup                   | 18.9 ms                                                | 17.0 ms: 1.11x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 263 ms: 1.09x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.44 ms: 1.08x faster                                                 |
| regex_dna                        | 149 ms                                                 | 139 ms: 1.08x faster                                                  |
| python_startup_no_site           | 14.5 ms                                                | 13.6 ms: 1.07x faster                                                 |
| async_tree_eager_io              | 514 ms                                                 | 484 ms: 1.06x faster                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 464 ms: 1.03x faster                                                  |
| xml_etree_parse                  | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 17.1 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 460 ms: 1.03x slower                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 75.6 ms: 1.03x slower                                                 |
| async_tree_io                    | 507 ms                                                 | 525 ms: 1.04x slower                                                  |
| deepcopy                         | 237 us                                                 | 245 us: 1.04x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 206 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 485 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 367 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 395 ms: 1.06x slower                                                  |
| async_tree_memoization           | 268 ms                                                 | 288 ms: 1.07x slower                                                  |
| async_tree_none                  | 215 ms                                                 | 233 ms: 1.08x slower                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 184 ms: 1.09x slower                                                  |
| pathlib                          | 23.4 ms                                                | 25.6 ms: 1.10x slower                                                 |
| generators                       | 31.5 ms                                                | 34.6 ms: 1.10x slower                                                 |
| json                             | 3.03 ms                                                | 3.35 ms: 1.11x slower                                                 |
| json_loads                       | 17.0 us                                                | 18.8 us: 1.11x slower                                                 |
| async_generators                 | 295 ms                                                 | 331 ms: 1.12x slower                                                  |
| deepcopy_memo                    | 27.4 us                                                | 31.2 us: 1.14x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 159 ms: 1.15x slower                                                  |
| json_dumps                       | 6.52 ms                                                | 7.74 ms: 1.19x slower                                                 |
| deepcopy_reduce                  | 2.07 us                                                | 2.46 us: 1.19x slower                                                 |
| pylint                           | 180 ms                                                 | 215 ms: 1.20x slower                                                  |
| telco                            | 4.76 ms                                                | 5.69 ms: 1.20x slower                                                 |
| xml_etree_generate               | 57.0 ms                                                | 68.1 ms: 1.20x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 88.7 ms: 1.20x slower                                                 |
| nqueens                          | 62.5 ms                                                | 75.5 ms: 1.21x slower                                                 |
| coverage                         | 46.0 ms                                                | 55.6 ms: 1.21x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.75 sec: 1.22x slower                                                |
| bpe_tokeniser                    | 3.25 sec                                               | 3.95 sec: 1.22x slower                                                |
| mdp                              | 1.49 sec                                               | 1.83 sec: 1.23x slower                                                |
| fannkuch                         | 284 ms                                                 | 352 ms: 1.24x slower                                                  |
| coroutines                       | 19.8 ms                                                | 25.0 ms: 1.27x slower                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.99 sec: 1.27x slower                                                |
| pycparser                        | 705 ms                                                 | 913 ms: 1.29x slower                                                  |
| scimark_fft                      | 201 ms                                                 | 263 ms: 1.31x slower                                                  |
| 2to3                             | 187 ms                                                 | 246 ms: 1.32x slower                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 4.06 ms: 1.36x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 15.4 ms: 1.36x slower                                                 |
| pyflate                          | 351 ms                                                 | 479 ms: 1.36x slower                                                  |
| xml_etree_process                | 41.0 ms                                                | 57.2 ms: 1.40x slower                                                 |
| html5lib                         | 36.6 ms                                                | 51.2 ms: 1.40x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 142 us: 1.40x slower                                                  |
| crypto_pyaes                     | 54.2 ms                                                | 77.4 ms: 1.43x slower                                                 |
| dulwich_log                      | 28.5 ms                                                | 40.7 ms: 1.43x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 49.6 ms: 1.44x slower                                                 |
| thrift                           | 466 us                                                 | 679 us: 1.46x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 50.9 ms: 1.46x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 24.9 ms: 1.48x slower                                                 |
| async_tree_eager                 | 70.1 ms                                                | 106 ms: 1.52x slower                                                  |
| pprint_safe_repr                 | 533 ms                                                 | 808 ms: 1.52x slower                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.64 sec: 1.52x slower                                                |
| regex_compile                    | 78.6 ms                                                | 119 ms: 1.52x slower                                                  |
| comprehensions                   | 12.3 us                                                | 18.7 us: 1.52x slower                                                 |
| spectral_norm                    | 76.3 ms                                                | 118 ms: 1.55x slower                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 78.1 ms: 1.55x slower                                                 |
| sympy_str                        | 145 ms                                                 | 227 ms: 1.56x slower                                                  |
| scimark_sor                      | 105 ms                                                 | 165 ms: 1.56x slower                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 74.9 ms: 1.57x slower                                                 |
| hexiom                           | 4.86 ms                                                | 7.63 ms: 1.57x slower                                                 |
| bench_thread_pool                | 505 us                                                 | 792 us: 1.57x slower                                                  |
| go                               | 115 ms                                                 | 181 ms: 1.58x slower                                                  |
| richards                         | 35.2 ms                                                | 55.6 ms: 1.58x slower                                                 |
| django_template                  | 22.2 ms                                                | 35.3 ms: 1.59x slower                                                 |
| unpickle_pure_python             | 164 us                                                 | 262 us: 1.60x slower                                                  |
| pickle_pure_python               | 214 us                                                 | 346 us: 1.61x slower                                                  |
| richards_super                   | 39.1 ms                                                | 64.3 ms: 1.64x slower                                                 |
| float                            | 56.0 ms                                                | 93.8 ms: 1.67x slower                                                 |
| tornado_http                     | 75.8 ms                                                | 127 ms: 1.67x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 405 ms: 1.67x slower                                                  |
| logging_simple                   | 3.60 us                                                | 6.05 us: 1.68x slower                                                 |
| logging_format                   | 3.89 us                                                | 6.60 us: 1.69x slower                                                 |
| sympy_expand                     | 246 ms                                                 | 421 ms: 1.71x slower                                                  |
| mako                             | 7.68 ms                                                | 13.3 ms: 1.73x slower                                                 |
| chaos                            | 41.2 ms                                                | 74.2 ms: 1.80x slower                                                 |
| sympy_sum                        | 75.4 ms                                                | 137 ms: 1.82x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.88 ms: 1.84x slower                                                 |
| scimark_lu                       | 76.7 ms                                                | 144 ms: 1.88x slower                                                  |
| sqlglot_parse                    | 856 us                                                 | 1.64 ms: 1.92x slower                                                 |
| logging_silent                   | 70.1 ns                                                | 135 ns: 1.93x slower                                                  |
| raytrace                         | 181 ms                                                 | 373 ms: 2.06x slower                                                  |
| nbody                            | 74.0 ms                                                | 154 ms: 2.08x slower                                                  |
| deltablue                        | 2.68 ms                                                | 5.63 ms: 2.10x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.29x slower                                                          |

Benchmark hidden because not significant (1): async_tree_io_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240920-3.14.0a0-342e654-NOGIL/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.224x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.20x
- 99% likely to have a slowdown of 1.18x

# Memory
- memory change: 0.71x