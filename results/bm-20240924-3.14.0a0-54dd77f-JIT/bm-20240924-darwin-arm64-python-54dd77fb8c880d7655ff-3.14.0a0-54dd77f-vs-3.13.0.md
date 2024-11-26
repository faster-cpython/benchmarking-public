# Results vs. 3.13.0

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: darwin-arm64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.050x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.67x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 176 ms: 1.06x faster                                                  |
| docutils       | 1.44 sec                                               | 1.56 sec: 1.09x slower                                                |
| html5lib       | 36.6 ms                                                | 32.3 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.4 ms: 1.20x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 42.2 ms: 1.13x faster                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 124 ms: 1.12x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 258 ms: 1.12x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 64.1 ms: 1.09x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 249 ms: 1.08x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 201 ms: 1.07x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 188 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                  |
| async_generators                 | 295 ms                                                 | 292 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 464 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 547 ms: 1.10x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 678 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 705 ms: 1.48x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 46.1 ms: 1.22x faster                                                 |
| nbody          | 74.0 ms                                                | 63.5 ms: 1.17x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_compile  | 78.6 ms                                                | 75.6 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                |
| unpickle_pure_python | 164 us                                                 | 131 us: 1.25x faster                                                  |
| pickle_pure_python   | 214 us                                                 | 179 us: 1.20x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 34.3 ms: 1.20x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 51.1 ms: 1.11x faster                                                 |
| json_dumps           | 6.52 ms                                                | 6.17 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 73.6 ms                                                | 71.7 ms: 1.03x faster                                                 |
| xml_etree_parse      | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| json_loads           | 17.0 us                                                | 16.8 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 16.9 ms: 1.12x faster                                                 |
| python_startup_no_site | 14.5 ms                                                | 13.8 ms: 1.05x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                 |
| genshi_text     | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                 |
| django_template | 22.2 ms                                                | 22.8 ms: 1.03x slower                                                 |
| genshi_xml      | 34.4 ms                                                | 41.3 ms: 1.20x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.0 us: 1.71x faster                                                 |
| deepcopy                         | 237 us                                                 | 152 us: 1.56x faster                                                  |
| deepcopy_reduce                  | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| create_gc_cycles                 | 1.17 ms                                                | 905 us: 1.29x faster                                                  |
| generators                       | 31.5 ms                                                | 24.4 ms: 1.29x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                |
| unpickle_pure_python             | 164 us                                                 | 131 us: 1.25x faster                                                  |
| float                            | 56.0 ms                                                | 46.1 ms: 1.22x faster                                                 |
| bench_mp_pool                    | 62.5 ms                                                | 51.6 ms: 1.21x faster                                                 |
| scimark_sor                      | 105 ms                                                 | 87.3 ms: 1.21x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.4 ms: 1.20x faster                                                 |
| pickle_pure_python               | 214 us                                                 | 179 us: 1.20x faster                                                  |
| scimark_lu                       | 76.7 ms                                                | 63.9 ms: 1.20x faster                                                 |
| xml_etree_process                | 41.0 ms                                                | 34.3 ms: 1.20x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.02 us: 1.19x faster                                                 |
| mako                             | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                 |
| gc_traversal                     | 2.91 ms                                                | 2.46 ms: 1.18x faster                                                 |
| logging_format                   | 3.89 us                                                | 3.31 us: 1.18x faster                                                 |
| nbody                            | 74.0 ms                                                | 63.5 ms: 1.17x faster                                                 |
| go                               | 115 ms                                                 | 100 ms: 1.15x faster                                                  |
| spectral_norm                    | 76.3 ms                                                | 66.7 ms: 1.14x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.36 ms: 1.14x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 42.2 ms: 1.13x faster                                                 |
| html5lib                         | 36.6 ms                                                | 32.3 ms: 1.13x faster                                                 |
| logging_silent                   | 70.1 ns                                                | 62.5 ns: 1.12x faster                                                 |
| python_startup                   | 18.9 ms                                                | 16.9 ms: 1.12x faster                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 124 ms: 1.12x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 258 ms: 1.12x faster                                                  |
| xml_etree_generate               | 57.0 ms                                                | 51.1 ms: 1.11x faster                                                 |
| thrift                           | 466 us                                                 | 424 us: 1.10x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 64.1 ms: 1.09x faster                                                 |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.08x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 93.6 us: 1.08x faster                                                 |
| nqueens                          | 62.5 ms                                                | 57.9 ms: 1.08x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 249 ms: 1.08x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 470 us: 1.07x faster                                                  |
| pyflate                          | 351 ms                                                 | 327 ms: 1.07x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 201 ms: 1.07x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| 2to3                             | 187 ms                                                 | 176 ms: 1.06x faster                                                  |
| json_dumps                       | 6.52 ms                                                | 6.17 ms: 1.06x faster                                                 |
| pprint_safe_repr                 | 533 ms                                                 | 504 ms: 1.06x faster                                                  |
| bpe_tokeniser                    | 3.25 sec                                               | 3.07 sec: 1.06x faster                                                |
| async_tree_none_tg               | 198 ms                                                 | 188 ms: 1.05x faster                                                  |
| fannkuch                         | 284 ms                                                 | 269 ms: 1.05x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 180 ms: 1.05x faster                                                  |
| python_startup_no_site           | 14.5 ms                                                | 13.8 ms: 1.05x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 48.0 ms: 1.05x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 1.03 sec: 1.05x faster                                                |
| raytrace                         | 181 ms                                                 | 173 ms: 1.05x faster                                                  |
| json                             | 3.03 ms                                                | 2.90 ms: 1.04x faster                                                 |
| crypto_pyaes                     | 54.2 ms                                                | 52.0 ms: 1.04x faster                                                 |
| regex_compile                    | 78.6 ms                                                | 75.6 ms: 1.04x faster                                                 |
| mdp                              | 1.49 sec                                               | 1.44 sec: 1.03x faster                                                |
| coverage                         | 46.0 ms                                                | 44.4 ms: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                  |
| chaos                            | 41.2 ms                                                | 39.9 ms: 1.03x faster                                                 |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                 |
| pycparser                        | 705 ms                                                 | 685 ms: 1.03x faster                                                  |
| hexiom                           | 4.86 ms                                                | 4.73 ms: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 71.7 ms: 1.03x faster                                                 |
| sympy_str                        | 145 ms                                                 | 144 ms: 1.01x faster                                                  |
| xml_etree_parse                  | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| async_generators                 | 295 ms                                                 | 292 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.96 ms: 1.01x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.8 us: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                 |
| telco                            | 4.76 ms                                                | 4.78 ms: 1.00x slower                                                 |
| sympy_sum                        | 75.4 ms                                                | 75.8 ms: 1.01x slower                                                 |
| sympy_expand                     | 246 ms                                                 | 248 ms: 1.01x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 35.3 ms: 1.01x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 74.9 ms: 1.01x slower                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.04 ms: 1.02x slower                                                 |
| dulwich_log                      | 28.5 ms                                                | 29.0 ms: 1.02x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.6 ms: 1.02x slower                                                 |
| django_template                  | 22.2 ms                                                | 22.8 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 464 ms: 1.03x slower                                                  |
| comprehensions                   | 12.3 us                                                | 12.7 us: 1.04x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.56 sec: 1.09x slower                                                |
| async_tree_io_tg                 | 497 ms                                                 | 547 ms: 1.10x slower                                                  |
| pylint                           | 180 ms                                                 | 205 ms: 1.14x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                  |
| genshi_xml                       | 34.4 ms                                                | 41.3 ms: 1.20x slower                                                 |
| richards_super                   | 39.1 ms                                                | 47.9 ms: 1.23x slower                                                 |
| richards                         | 35.2 ms                                                | 45.9 ms: 1.30x slower                                                 |
| async_tree_eager_io              | 514 ms                                                 | 678 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 705 ms: 1.48x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (4): sqlglot_parse, async_tree_cpu_io_mixed, pathlib, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.050x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.67x