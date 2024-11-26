# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.255x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x slower
- Memory change: 0.56x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 254 ms: 1.36x slower                                                  |
| docutils       | 1.44 sec                                               | 1.79 sec: 1.25x slower                                                |
| html5lib       | 36.6 ms                                                | 52.3 ms: 1.43x slower                                                 |
| tornado_http   | 75.8 ms                                                | 110 ms: 1.46x slower                                                  |
| Geometric mean | (ref)                                                  | 1.37x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 274 ms: 1.05x faster                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 488 ms: 1.02x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 521 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 476 ms: 1.06x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 550 ms: 1.08x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 216 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 407 ms: 1.09x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 504 ms: 1.10x slower                                                  |
| async_tree_memoization           | 268 ms                                                 | 300 ms: 1.12x slower                                                  |
| async_tree_none                  | 215 ms                                                 | 243 ms: 1.13x slower                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 192 ms: 1.14x slower                                                  |
| async_generators                 | 295 ms                                                 | 336 ms: 1.14x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 167 ms: 1.21x slower                                                  |
| coroutines                       | 19.8 ms                                                | 26.0 ms: 1.32x slower                                                 |
| async_tree_eager                 | 70.1 ms                                                | 111 ms: 1.58x slower                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 78.6 ms: 1.64x slower                                                 |
| asyncio_websockets               | 242 ms                                                 | 405 ms: 1.68x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.17x slower                                                          |

Benchmark hidden because not significant (1): async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 56.0 ms                                                | 98.7 ms: 1.76x slower                                                 |
| nbody          | 74.0 ms                                                | 159 ms: 2.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.55x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                 |
| regex_dna      | 149 ms                                                 | 139 ms: 1.07x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                 |
| regex_compile  | 78.6 ms                                                | 125 ms: 1.60x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 73.6 ms                                                | 78.2 ms: 1.06x slower                                                 |
| json_loads           | 17.0 us                                                | 19.4 us: 1.14x slower                                                 |
| json_dumps           | 6.52 ms                                                | 8.12 ms: 1.24x slower                                                 |
| xml_etree_generate   | 57.0 ms                                                | 71.9 ms: 1.26x slower                                                 |
| tomli_loads          | 1.57 sec                                               | 2.07 sec: 1.32x slower                                                |
| xml_etree_process    | 41.0 ms                                                | 59.8 ms: 1.46x slower                                                 |
| pickle_pure_python   | 214 us                                                 | 365 us: 1.70x slower                                                  |
| unpickle_pure_python | 164 us                                                 | 280 us: 1.71x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.30x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 19.2 ms: 1.02x slower                                                 |
| python_startup_no_site | 14.5 ms                                                | 15.6 ms: 1.08x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 51.6 ms: 1.50x slower                                                 |
| genshi_text     | 16.9 ms                                                | 25.8 ms: 1.53x slower                                                 |
| django_template | 22.2 ms                                                | 37.9 ms: 1.71x slower                                                 |
| mako            | 7.68 ms                                                | 13.7 ms: 1.79x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.63x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize                | 189 ms                                                 | 110 ms: 1.72x faster                                                  |
| create_gc_cycles                 | 1.17 ms                                                | 696 us: 1.68x faster                                                  |
| gc_traversal                     | 2.91 ms                                                | 2.05 ms: 1.42x faster                                                 |
| bench_mp_pool                    | 62.5 ms                                                | 56.7 ms: 1.10x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                 |
| regex_dna                        | 149 ms                                                 | 139 ms: 1.07x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 274 ms: 1.05x faster                                                  |
| xml_etree_parse                  | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| python_startup                   | 18.9 ms                                                | 19.2 ms: 1.02x slower                                                 |
| regex_v8                         | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                 |
| async_tree_eager_io_tg           | 477 ms                                                 | 488 ms: 1.02x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 521 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 476 ms: 1.06x slower                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 78.2 ms: 1.06x slower                                                 |
| python_startup_no_site           | 14.5 ms                                                | 15.6 ms: 1.08x slower                                                 |
| deepcopy                         | 237 us                                                 | 256 us: 1.08x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 550 ms: 1.08x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 216 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 407 ms: 1.09x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 504 ms: 1.10x slower                                                  |
| async_tree_memoization           | 268 ms                                                 | 300 ms: 1.12x slower                                                  |
| generators                       | 31.5 ms                                                | 35.3 ms: 1.12x slower                                                 |
| async_tree_none                  | 215 ms                                                 | 243 ms: 1.13x slower                                                  |
| json                             | 3.03 ms                                                | 3.42 ms: 1.13x slower                                                 |
| pathlib                          | 23.4 ms                                                | 26.5 ms: 1.13x slower                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 192 ms: 1.14x slower                                                  |
| async_generators                 | 295 ms                                                 | 336 ms: 1.14x slower                                                  |
| json_loads                       | 17.0 us                                                | 19.4 us: 1.14x slower                                                 |
| deepcopy_memo                    | 27.4 us                                                | 32.4 us: 1.18x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 167 ms: 1.21x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 89.9 ms: 1.22x slower                                                 |
| coverage                         | 46.0 ms                                                | 56.8 ms: 1.24x slower                                                 |
| deepcopy_reduce                  | 2.07 us                                                | 2.57 us: 1.24x slower                                                 |
| json_dumps                       | 6.52 ms                                                | 8.12 ms: 1.24x slower                                                 |
| pylint                           | 180 ms                                                 | 224 ms: 1.25x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.79 sec: 1.25x slower                                                |
| mdp                              | 1.49 sec                                               | 1.87 sec: 1.25x slower                                                |
| bpe_tokeniser                    | 3.25 sec                                               | 4.08 sec: 1.26x slower                                                |
| nqueens                          | 62.5 ms                                                | 78.7 ms: 1.26x slower                                                 |
| telco                            | 4.76 ms                                                | 5.99 ms: 1.26x slower                                                 |
| xml_etree_generate               | 57.0 ms                                                | 71.9 ms: 1.26x slower                                                 |
| fannkuch                         | 284 ms                                                 | 358 ms: 1.26x slower                                                  |
| coroutines                       | 19.8 ms                                                | 26.0 ms: 1.32x slower                                                 |
| tomli_loads                      | 1.57 sec                                               | 2.07 sec: 1.32x slower                                                |
| 2to3                             | 187 ms                                                 | 254 ms: 1.36x slower                                                  |
| pycparser                        | 705 ms                                                 | 961 ms: 1.36x slower                                                  |
| scimark_fft                      | 201 ms                                                 | 279 ms: 1.39x slower                                                  |
| pyflate                          | 351 ms                                                 | 489 ms: 1.39x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 16.0 ms: 1.41x slower                                                 |
| html5lib                         | 36.6 ms                                                | 52.3 ms: 1.43x slower                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 4.32 ms: 1.45x slower                                                 |
| crypto_pyaes                     | 54.2 ms                                                | 78.9 ms: 1.45x slower                                                 |
| tornado_http                     | 75.8 ms                                                | 110 ms: 1.46x slower                                                  |
| xml_etree_process                | 41.0 ms                                                | 59.8 ms: 1.46x slower                                                 |
| dulwich_log                      | 28.5 ms                                                | 42.1 ms: 1.48x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 151 us: 1.49x slower                                                  |
| genshi_xml                       | 34.4 ms                                                | 51.6 ms: 1.50x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 25.8 ms: 1.53x slower                                                 |
| thrift                           | 466 us                                                 | 716 us: 1.54x slower                                                  |
| comprehensions                   | 12.3 us                                                | 19.3 us: 1.57x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 55.0 ms: 1.57x slower                                                 |
| async_tree_eager                 | 70.1 ms                                                | 111 ms: 1.58x slower                                                  |
| scimark_sor                      | 105 ms                                                 | 167 ms: 1.58x slower                                                  |
| regex_compile                    | 78.6 ms                                                | 125 ms: 1.60x slower                                                  |
| bench_thread_pool                | 505 us                                                 | 810 us: 1.61x slower                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.74 sec: 1.61x slower                                                |
| pprint_safe_repr                 | 533 ms                                                 | 859 ms: 1.61x slower                                                  |
| go                               | 115 ms                                                 | 186 ms: 1.62x slower                                                  |
| sympy_str                        | 145 ms                                                 | 236 ms: 1.62x slower                                                  |
| hexiom                           | 4.86 ms                                                | 7.94 ms: 1.63x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 82.6 ms: 1.64x slower                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 78.6 ms: 1.64x slower                                                 |
| richards                         | 35.2 ms                                                | 58.8 ms: 1.67x slower                                                 |
| asyncio_websockets               | 242 ms                                                 | 405 ms: 1.68x slower                                                  |
| pickle_pure_python               | 214 us                                                 | 365 us: 1.70x slower                                                  |
| django_template                  | 22.2 ms                                                | 37.9 ms: 1.71x slower                                                 |
| unpickle_pure_python             | 164 us                                                 | 280 us: 1.71x slower                                                  |
| richards_super                   | 39.1 ms                                                | 68.3 ms: 1.75x slower                                                 |
| spectral_norm                    | 76.3 ms                                                | 134 ms: 1.76x slower                                                  |
| logging_simple                   | 3.60 us                                                | 6.34 us: 1.76x slower                                                 |
| float                            | 56.0 ms                                                | 98.7 ms: 1.76x slower                                                 |
| sympy_expand                     | 246 ms                                                 | 438 ms: 1.78x slower                                                  |
| logging_format                   | 3.89 us                                                | 6.92 us: 1.78x slower                                                 |
| mako                             | 7.68 ms                                                | 13.7 ms: 1.79x slower                                                 |
| sympy_sum                        | 75.4 ms                                                | 142 ms: 1.88x slower                                                  |
| chaos                            | 41.2 ms                                                | 78.5 ms: 1.91x slower                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.97 ms: 1.93x slower                                                 |
| sqlglot_parse                    | 856 us                                                 | 1.72 ms: 2.01x slower                                                 |
| logging_silent                   | 70.1 ns                                                | 143 ns: 2.04x slower                                                  |
| scimark_lu                       | 76.7 ms                                                | 158 ms: 2.06x slower                                                  |
| nbody                            | 74.0 ms                                                | 159 ms: 2.15x slower                                                  |
| raytrace                         | 181 ms                                                 | 390 ms: 2.16x slower                                                  |
| deltablue                        | 2.68 ms                                                | 5.96 ms: 2.23x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.34x slower                                                          |

Benchmark hidden because not significant (1): async_tree_eager_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.255x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.25x
- 95% likely to have a slowdown of 1.25x
- 99% likely to have a slowdown of 1.22x

# Memory
- memory change: 0.56x