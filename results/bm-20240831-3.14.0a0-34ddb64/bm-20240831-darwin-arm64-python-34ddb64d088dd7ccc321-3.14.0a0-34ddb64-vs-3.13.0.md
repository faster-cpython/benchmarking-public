# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.093x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 160 ms: 1.17x faster                                                  |
| docutils       | 1.44 sec                                               | 1.46 sec: 1.02x slower                                                |
| html5lib       | 36.6 ms                                                | 30.0 ms: 1.22x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 244 ms: 1.18x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 61.0 ms: 1.15x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 42.2 ms: 1.13x faster                                                 |
| async_tree_none                  | 215 ms                                                 | 193 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 125 ms: 1.11x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 250 ms: 1.07x faster                                                  |
| async_generators                 | 295 ms                                                 | 281 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 361 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 459 ms: 1.02x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 568 ms: 1.14x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 595 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 679 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 720 ms: 1.51x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 59.3 ms: 1.25x faster                                                 |
| float          | 56.0 ms                                                | 48.6 ms: 1.15x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 67.7 ms: 1.16x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 181 us: 1.18x faster                                                  |
| unpickle_pure_python | 164 us                                                 | 143 us: 1.15x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 37.4 ms: 1.09x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 53.2 ms: 1.07x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                |
| json_dumps           | 6.52 ms                                                | 6.38 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 73.6 ms                                                | 74.3 ms: 1.01x slower                                                 |
| json_loads           | 17.0 us                                                | 17.2 us: 1.02x slower                                                 |
| xml_etree_parse      | 107 ms                                                 | 109 ms: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 16.8 ms: 1.12x faster                                                 |
| python_startup_no_site | 14.5 ms                                                | 13.9 ms: 1.04x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| django_template | 22.2 ms                                                | 19.8 ms: 1.12x faster                                                 |
| mako            | 7.68 ms                                                | 7.03 ms: 1.09x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.7 us: 1.64x faster                                                 |
| deepcopy                         | 237 us                                                 | 146 us: 1.62x faster                                                  |
| generators                       | 31.5 ms                                                | 20.4 ms: 1.54x faster                                                 |
| go                               | 115 ms                                                 | 79.0 ms: 1.46x faster                                                 |
| deepcopy_reduce                  | 2.07 us                                                | 1.52 us: 1.36x faster                                                 |
| create_gc_cycles                 | 1.17 ms                                                | 896 us: 1.30x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 48.6 ms: 1.29x faster                                                 |
| nbody                            | 74.0 ms                                                | 59.3 ms: 1.25x faster                                                 |
| comprehensions                   | 12.3 us                                                | 9.96 us: 1.23x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.18 ms: 1.23x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                 |
| html5lib                         | 36.6 ms                                                | 30.0 ms: 1.22x faster                                                 |
| raytrace                         | 181 ms                                                 | 149 ms: 1.21x faster                                                  |
| hexiom                           | 4.86 ms                                                | 4.06 ms: 1.20x faster                                                 |
| gc_traversal                     | 2.91 ms                                                | 2.45 ms: 1.19x faster                                                 |
| pickle_pure_python               | 214 us                                                 | 181 us: 1.18x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 244 ms: 1.18x faster                                                  |
| nqueens                          | 62.5 ms                                                | 53.2 ms: 1.18x faster                                                 |
| pprint_safe_repr                 | 533 ms                                                 | 456 ms: 1.17x faster                                                  |
| 2to3                             | 187 ms                                                 | 160 ms: 1.17x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 43.2 ms: 1.17x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 930 ms: 1.17x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.10 us: 1.16x faster                                                 |
| regex_compile                    | 78.6 ms                                                | 67.7 ms: 1.16x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 739 us: 1.16x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 437 us: 1.16x faster                                                  |
| chaos                            | 41.2 ms                                                | 35.7 ms: 1.15x faster                                                 |
| float                            | 56.0 ms                                                | 48.6 ms: 1.15x faster                                                 |
| scimark_lu                       | 76.7 ms                                                | 66.6 ms: 1.15x faster                                                 |
| logging_silent                   | 70.1 ns                                                | 60.9 ns: 1.15x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 61.0 ms: 1.15x faster                                                 |
| unpickle_pure_python             | 164 us                                                 | 143 us: 1.15x faster                                                  |
| logging_format                   | 3.89 us                                                | 3.40 us: 1.15x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 898 us: 1.14x faster                                                  |
| spectral_norm                    | 76.3 ms                                                | 67.1 ms: 1.14x faster                                                 |
| genshi_xml                       | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| scimark_sor                      | 105 ms                                                 | 92.9 ms: 1.13x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 167 ms: 1.13x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 42.2 ms: 1.13x faster                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 31.0 ms: 1.13x faster                                                 |
| python_startup                   | 18.9 ms                                                | 16.8 ms: 1.12x faster                                                 |
| django_template                  | 22.2 ms                                                | 19.8 ms: 1.12x faster                                                 |
| async_tree_none                  | 215 ms                                                 | 193 ms: 1.12x faster                                                  |
| richards                         | 35.2 ms                                                | 31.6 ms: 1.11x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 90.9 us: 1.11x faster                                                 |
| richards_super                   | 39.1 ms                                                | 35.3 ms: 1.11x faster                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 125 ms: 1.11x faster                                                  |
| sympy_str                        | 145 ms                                                 | 132 ms: 1.10x faster                                                  |
| thrift                           | 466 us                                                 | 424 us: 1.10x faster                                                  |
| pycparser                        | 705 ms                                                 | 642 ms: 1.10x faster                                                  |
| pyflate                          | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| xml_etree_process                | 41.0 ms                                                | 37.4 ms: 1.09x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.09x faster                                                 |
| mako                             | 7.68 ms                                                | 7.03 ms: 1.09x faster                                                 |
| sympy_sum                        | 75.4 ms                                                | 69.1 ms: 1.09x faster                                                 |
| fannkuch                         | 284 ms                                                 | 261 ms: 1.09x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 227 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| crypto_pyaes                     | 54.2 ms                                                | 50.6 ms: 1.07x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 250 ms: 1.07x faster                                                  |
| xml_etree_generate               | 57.0 ms                                                | 53.2 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.79 ms: 1.07x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                |
| regex_effbot                     | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| async_generators                 | 295 ms                                                 | 281 ms: 1.05x faster                                                  |
| mdp                              | 1.49 sec                                               | 1.42 sec: 1.05x faster                                                |
| python_startup_no_site           | 14.5 ms                                                | 13.9 ms: 1.04x faster                                                 |
| dulwich_log                      | 28.5 ms                                                | 27.4 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 361 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| json                             | 3.03 ms                                                | 2.95 ms: 1.03x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 72.2 ms: 1.02x faster                                                 |
| coverage                         | 46.0 ms                                                | 44.9 ms: 1.02x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                 |
| json_dumps                       | 6.52 ms                                                | 6.38 ms: 1.02x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| telco                            | 4.76 ms                                                | 4.79 ms: 1.01x slower                                                 |
| xml_etree_iterparse              | 73.6 ms                                                | 74.3 ms: 1.01x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.2 us: 1.02x slower                                                 |
| xml_etree_parse                  | 107 ms                                                 | 109 ms: 1.02x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.46 sec: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 459 ms: 1.02x slower                                                  |
| pathlib                          | 23.4 ms                                                | 24.2 ms: 1.03x slower                                                 |
| async_tree_io_tg                 | 497 ms                                                 | 568 ms: 1.14x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 595 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 679 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 720 ms: 1.51x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (5): bpe_tokeniser, async_tree_cpu_io_mixed, async_tree_none_tg, pylint, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.093x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.39x