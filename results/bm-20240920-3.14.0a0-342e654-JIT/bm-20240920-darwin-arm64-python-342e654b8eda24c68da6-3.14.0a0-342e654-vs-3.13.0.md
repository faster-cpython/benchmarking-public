# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.055x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.47x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 176 ms: 1.06x faster                                                  |
| docutils       | 1.44 sec                                               | 1.56 sec: 1.09x slower                                                |
| html5lib       | 36.6 ms                                                | 33.8 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 42.4 ms: 1.13x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 257 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 123 ms: 1.12x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 63.7 ms: 1.10x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 247 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 201 ms: 1.07x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 334 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 361 ms: 1.03x faster                                                  |
| async_generators                 | 295 ms                                                 | 290 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 461 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 541 ms: 1.09x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 589 ms: 1.16x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 677 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 700 ms: 1.47x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 46.1 ms: 1.22x faster                                                 |
| nbody          | 74.0 ms                                                | 63.6 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 74.3 ms: 1.06x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.49 ms: 1.06x faster                                                 |
| regex_v8       | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                 |
| regex_dna      | 149 ms                                                 | 148 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 164 us                                                 | 131 us: 1.26x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.25 sec: 1.25x faster                                                |
| pickle_pure_python   | 214 us                                                 | 178 us: 1.20x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 34.1 ms: 1.20x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 50.1 ms: 1.14x faster                                                 |
| json_dumps           | 6.52 ms                                                | 6.19 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 73.6 ms                                                | 72.3 ms: 1.02x faster                                                 |
| json_loads           | 17.0 us                                                | 16.9 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 14.4 ms: 1.31x faster                                                 |
| python_startup_no_site | 14.5 ms                                                | 11.5 ms: 1.25x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.45 ms: 1.19x faster                                                 |
| genshi_text     | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| django_template | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                 |
| genshi_xml      | 34.4 ms                                                | 41.1 ms: 1.20x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.1 us: 1.70x faster                                                 |
| deepcopy                         | 237 us                                                 | 153 us: 1.54x faster                                                  |
| deepcopy_reduce                  | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| python_startup                   | 18.9 ms                                                | 14.4 ms: 1.31x faster                                                 |
| create_gc_cycles                 | 1.17 ms                                                | 904 us: 1.29x faster                                                  |
| generators                       | 31.5 ms                                                | 24.6 ms: 1.28x faster                                                 |
| bench_mp_pool                    | 62.5 ms                                                | 49.4 ms: 1.27x faster                                                 |
| unpickle_pure_python             | 164 us                                                 | 131 us: 1.26x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.25 sec: 1.25x faster                                                |
| python_startup_no_site           | 14.5 ms                                                | 11.5 ms: 1.25x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                 |
| float                            | 56.0 ms                                                | 46.1 ms: 1.22x faster                                                 |
| scimark_lu                       | 76.7 ms                                                | 63.4 ms: 1.21x faster                                                 |
| pickle_pure_python               | 214 us                                                 | 178 us: 1.20x faster                                                  |
| xml_etree_process                | 41.0 ms                                                | 34.1 ms: 1.20x faster                                                 |
| scimark_sor                      | 105 ms                                                 | 87.7 ms: 1.20x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.02 us: 1.19x faster                                                 |
| mako                             | 7.68 ms                                                | 6.45 ms: 1.19x faster                                                 |
| gc_traversal                     | 2.91 ms                                                | 2.45 ms: 1.19x faster                                                 |
| logging_format                   | 3.89 us                                                | 3.31 us: 1.18x faster                                                 |
| nbody                            | 74.0 ms                                                | 63.6 ms: 1.16x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.35 ms: 1.14x faster                                                 |
| spectral_norm                    | 76.3 ms                                                | 67.0 ms: 1.14x faster                                                 |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| xml_etree_generate               | 57.0 ms                                                | 50.1 ms: 1.14x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 42.4 ms: 1.13x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 257 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 123 ms: 1.12x faster                                                  |
| logging_silent                   | 70.1 ns                                                | 62.8 ns: 1.12x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 63.7 ms: 1.10x faster                                                 |
| thrift                           | 466 us                                                 | 425 us: 1.10x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 247 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| html5lib                         | 36.6 ms                                                | 33.8 ms: 1.08x faster                                                 |
| pyflate                          | 351 ms                                                 | 326 ms: 1.08x faster                                                  |
| fannkuch                         | 284 ms                                                 | 263 ms: 1.08x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 469 us: 1.07x faster                                                  |
| nqueens                          | 62.5 ms                                                | 58.2 ms: 1.07x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 94.3 us: 1.07x faster                                                 |
| async_tree_none                  | 215 ms                                                 | 201 ms: 1.07x faster                                                  |
| 2to3                             | 187 ms                                                 | 176 ms: 1.06x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.06x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 47.4 ms: 1.06x faster                                                 |
| regex_compile                    | 78.6 ms                                                | 74.3 ms: 1.06x faster                                                 |
| bpe_tokeniser                    | 3.25 sec                                               | 3.07 sec: 1.06x faster                                                |
| regex_effbot                     | 2.63 ms                                                | 2.49 ms: 1.06x faster                                                 |
| json_dumps                       | 6.52 ms                                                | 6.19 ms: 1.05x faster                                                 |
| crypto_pyaes                     | 54.2 ms                                                | 51.7 ms: 1.05x faster                                                 |
| pprint_safe_repr                 | 533 ms                                                 | 509 ms: 1.05x faster                                                  |
| raytrace                         | 181 ms                                                 | 173 ms: 1.05x faster                                                  |
| json                             | 3.03 ms                                                | 2.91 ms: 1.04x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 1.04 sec: 1.04x faster                                                |
| pycparser                        | 705 ms                                                 | 678 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 334 ms: 1.04x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 183 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 361 ms: 1.03x faster                                                  |
| hexiom                           | 4.86 ms                                                | 4.74 ms: 1.03x faster                                                 |
| chaos                            | 41.2 ms                                                | 40.1 ms: 1.03x faster                                                 |
| coverage                         | 46.0 ms                                                | 44.8 ms: 1.03x faster                                                 |
| mdp                              | 1.49 sec                                               | 1.46 sec: 1.03x faster                                                |
| regex_v8                         | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                 |
| pathlib                          | 23.4 ms                                                | 22.9 ms: 1.02x faster                                                 |
| async_generators                 | 295 ms                                                 | 290 ms: 1.02x faster                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 72.3 ms: 1.02x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| sympy_str                        | 145 ms                                                 | 143 ms: 1.01x faster                                                  |
| regex_dna                        | 149 ms                                                 | 148 ms: 1.01x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 850 us: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.9 us: 1.01x faster                                                 |
| telco                            | 4.76 ms                                                | 4.80 ms: 1.01x slower                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.04 ms: 1.01x slower                                                 |
| dulwich_log                      | 28.5 ms                                                | 29.0 ms: 1.02x slower                                                 |
| django_template                  | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 75.2 ms: 1.02x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 35.5 ms: 1.02x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 461 ms: 1.03x slower                                                  |
| comprehensions                   | 12.3 us                                                | 12.8 us: 1.05x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.56 sec: 1.09x slower                                                |
| async_tree_io_tg                 | 497 ms                                                 | 541 ms: 1.09x slower                                                  |
| pylint                           | 180 ms                                                 | 205 ms: 1.14x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 589 ms: 1.16x slower                                                  |
| richards_super                   | 39.1 ms                                                | 46.4 ms: 1.19x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 41.1 ms: 1.20x slower                                                 |
| richards                         | 35.2 ms                                                | 44.4 ms: 1.26x slower                                                 |
| async_tree_eager_io              | 514 ms                                                 | 677 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 700 ms: 1.47x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (6): scimark_sparse_mat_mult, sympy_sum, async_tree_cpu_io_mixed, xml_etree_parse, sympy_expand, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.055x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.47x